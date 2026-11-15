set simulator [new Simulator]

set traceFile [open out.tr w]
set namFile [open out.nam w]
$simulator trace-all $traceFile
$simulator namtrace-all $namFile

set sender [$simulator node]
set receiver [$simulator node]
$simulator duplex-link $sender $receiver 1Mb 10ms DropTail

set udpAgent [new Agent/UDP]
set sinkAgent [new Agent/Null]
$simulator attach-agent $sender $udpAgent
$simulator attach-agent $receiver $sinkAgent
$simulator connect $udpAgent $sinkAgent

set traffic [new Application/Traffic/CBR]
$traffic set packetSize_ 500
$traffic set interval_ 0.01
$traffic attach-agent $udpAgent

proc finish {} {
    global simulator traceFile namFile
    $simulator flush-trace
    close $traceFile
    close $namFile
    exec nam out.nam &
    exit 0
}

$simulator at 0.5 "$traffic start"
$simulator at 4.5 "$traffic stop"
$simulator at 5.0 "finish"
$simulator run
