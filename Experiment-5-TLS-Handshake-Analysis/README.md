# Experiment 5: TLS Handshake Analysis Using Wireshark

## Aim
To examine the TLS handshake process and understand how secure communication is established between a web browser and a server using Wireshark.

## Theory

- **TLS (Transport Layer Security):** A protocol that protects data exchanged over a network.
- **HTTPS:** A secure version of HTTP that uses TLS to protect web communication.
- **TLS Handshake:** The exchange of messages used to negotiate security settings and establish a secure connection.
- **Session Keys:** Cryptographic keys used to protect data transmitted during a secure session.
- **Wireshark:** A network protocol analyzer used to capture and inspect network packets.

## Tools Required

- Kali Linux
- Wireshark
- Web browser
- Internet connection

## Procedure

### Step 1: Start Packet Capture
Open Wireshark and select the active network interface to capture network traffic.

### Step 2: Generate HTTPS Traffic
Open a secure website in the browser to generate TLS communication packets.

### Step 3: Apply Display Filter
Enter the following filter to display TLS-related packets:

```text
tls
```

### Step 4: Examine Handshake Messages
Inspect the captured packets to identify messages such as Client Hello, Server Hello, and Certificate.

### Step 5: Review Security Parameters
Examine the TLS version, cipher suite, and certificate information available in the packet details.

### Step 6: Observe Connection Establishment
Review the visible handshake messages to understand how the client and server establish secure communication.

## Visualization

```text
     ┌────────────────────────┐
     │ Launch Wireshark       │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Choose Network         │
     │ Interface              │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Open HTTPS Website     │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Filter TLS Packets     │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Inspect Handshake      │
     │ Messages               │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Review Security        │
     │ Parameters             │
     └────────────┬───────────┘
                  ↓
     ┌────────────────────────┐
     │ Record Findings        │
     └────────────────────────┘
```

## Results

1. TLS handshake packets were captured and analyzed using Wireshark.
2. Important handshake messages were identified during connection establishment.
3. TLS version, cipher suite, and certificate details were examined where available.
4. Packet analysis demonstrated how TLS helps establish secure communication between a browser and a web server.

## Improvements

TLS handshake analysis can be improved by automating packet inspection, validating certificates, and comparing TLS 1.2 with TLS 1.3.

## Conclusion

The experiment demonstrated how Wireshark can be used to inspect TLS handshake messages and understand the process of establishing a secure HTTPS connection.
