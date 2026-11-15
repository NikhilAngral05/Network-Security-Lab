# Experiment 8: Simulate UDP Traffic Using NS-2

## Aim

Simulate constant-bit-rate (CBR) UDP traffic between two network nodes and inspect the resulting trace and animation.

## Requirements

- Network Simulator 2 (NS-2)
- Network Animator (NAM), included with or installed alongside NS-2

## Procedure

1. Open a terminal in the `Codes` folder.
2. Run the simulation with `ns udp_cbr_simulation.tcl`.
3. NS-2 writes `out.tr` (the packet trace) and `out.nam` (the animation trace) to the current directory. The script opens the animation with NAM when the simulation finishes.
4. In NAM, observe the packets sent from the source node to the destination node over the duplex link.

## Simulation Setup

The script creates two nodes connected by a 1 Mb/s duplex link with 10 ms delay and a DropTail queue. A UDP agent sends 500-byte CBR packets every 0.01 seconds, starting at 0.5 seconds and stopping at 4.5 seconds. The simulation ends at 5 seconds.

## Result

The simulation produces a trace and a NAM animation of UDP CBR traffic between the two nodes.
