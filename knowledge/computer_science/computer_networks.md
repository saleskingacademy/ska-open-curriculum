---
key: computer_networks
title: "Computer Networks"
program: computer_science
course_level: 3
dna16: "0701201817599406"
l4_address: "S6:P1818455209"
chain256_anchor: "0738217235464159089384007343183304624620350918330995593279991353170969920039828805830475847618330912241576691833084829160697173403409441290290610581671797091833118529938536183312401558835395591743485606925139056691234245183317449509374018330429616333077019"
updated_at: "2026-08-26T07:50:18.334Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Computer Networks

> name heuristic - model placement unavailable

## Foundations

Computer networks are structured systems enabling data exchange among interconnected computing devices through communication channels. At their core, networks rely on layered abstractions—most notably the OSI and TCP/IP models—to modularize functions such as physical signaling, data framing, routing, and application-level protocols. The fundamental principles include addressing (unique identification via IP/MAC), routing (path determination via algorithms like Dijkstra’s or Bellman-Ford), switching (frame forwarding in LANs), and reliable data delivery (error detection/correction, flow and congestion control). Packet switching, the dominant paradigm, segments data into discrete packets, enabling statistical multiplexing and dynamic resource sharing, contrasting with circuit switching. Protocols define syntax, semantics, and timing of communication, ensuring interoperability across heterogeneous systems.

In computer science, a **computer network** is a collection of interconnected devices that communicate with each other to share resources and exchange data. A **device** can be a computer, printer, server, or any other hardware component that can send and receive data. **Interconnected** means that these devices are linked together using physical or wireless connections, such as cables, Wi-Fi, or Ethernet. 
**Communication** occurs through the transmission of **data packets**, which are small units of data that contain control information and user data. **Packets** are transmitted according to a set of rules, known as **protocols**, which govern data formatting, transmission, routing, and reception. 
Key concepts include **nodes**, which are devices that connect to the network, and **links**, which are the physical or logical connections between nodes. A **network topology** describes the physical or logical arrangement of nodes and links, such as bus, star, or mesh. 
Understanding these core definitions and principles is essential for designing, implementing, and managing computer networks, which enable communication, resource sharing, and data exchange between devices.

## Physical Layer

The Physical Layer transmits raw bitstreams over physical media. Key frameworks include Shannon’s Channel Capacity Theorem: \( C = B \log_2(1 + SNR) \), where \(C\) is capacity (bps), \(B\) bandwidth (Hz), and \(SNR\) signal-to-noise ratio. Common media: twisted pair (Cat6 supports up to 10 Gbps over 55m), coaxial cable, fiber optics (single-mode fiber exceeding 100 Gbps over 40 km). Encoding schemes such as NRZ, Manchester, and PAM-5 (used in Gigabit Ethernet) translate bits into electrical/optical signals. Physical layer standards include IEEE 802.3 (Ethernet), ITU-T G.652 (single-mode fiber). Signal attenuation, dispersion, and noise are mitigated via repeaters, amplifiers, and equalization.

## Data Link Layer

Responsible for node-to-node data transfer and error detection/correction. The HDLC protocol employs framing with flags (0x7E), bit stuffing, and CRC-32 for error detection. Ethernet (IEEE 802.3) uses CSMA/CD for medium access control, with frame structure: preamble (7 bytes), SFD (1 byte), destination/source MAC (6 bytes each), EtherType (2 bytes), payload (46-1500 bytes), and CRC (4 bytes). VLAN tagging (IEEE 802.1Q) inserts a 4-byte tag for network segmentation. ARP resolves IPv4 addresses to MAC addresses using broadcast requests and unicast replies, critical for LAN operation. Flow control employs mechanisms like sliding window (Go-Back-N, Selective Repeat) with sequence numbers modulo \(2^n\).

## Network Layer

Handles logical addressing and routing. IPv4 addressing uses 32-bit addresses, subnet masks, and CIDR notation (e.g., 192.168.1.0/24). Routing algorithms include:  
- Distance Vector (RIP): periodic updates every 30s, hop count metric capped at 15.  
- Link State (OSPF): uses Dijkstra’s algorithm on a link-state database, converges faster and supports hierarchical areas.  
IP fragmentation divides packets exceeding MTU (usually 1500 bytes for Ethernet) into fragments with offset fields. ICMP provides error reporting (Type 3: Destination Unreachable) and diagnostics (Type 8: Echo Request). IPv6 expands addressing to 128 bits, introduces simplified header, and mandates IPSec support.

## Transport Layer

Provides end-to-end communication services. TCP implements reliable, connection-oriented byte streams with mechanisms: three-way handshake (SYN, SYN-ACK, ACK), congestion control (slow start, congestion avoidance, fast retransmit, fast recovery), and flow control (sliding window with dynamic window size). TCP header includes 16-bit sequence and acknowledgment numbers, window size, and flags (SYN, ACK, FIN, RST). UDP offers connectionless, low-overhead datagram service without reliability guarantees. The formula for TCP throughput under loss:  
\[ \text{Throughput} \approx \frac{MSS}{RTT \times \sqrt{p}} \]  
where MSS is maximum segment size, RTT round-trip time, and \(p\) packet loss probability.

## Application Layer

Defines protocols for end-user services. HTTP/1.1 uses request-response model over TCP port 80, supports persistent connections and chunked transfer encoding. DNS resolves domain names to IP addresses via hierarchical queries: root servers → TLD servers → authoritative servers. SMTP (port 25) facilitates email transmission with commands like HELO, MAIL FROM, RCPT TO. FTP uses separate control (port 21) and data (port 20) connections, supporting active and passive modes. TLS provides cryptographic security atop TCP, employing asymmetric key exchange (RSA, ECDHE), symmetric encryption (AES-128/256), and MAC (HMAC-SHA256).

## Network Security

Encompasses confidentiality, integrity, authentication, and availability. IPsec operates at the network layer with AH (Authentication Header) and ESP (Encapsulating Security Payload) protocols, enabling tunnel and transport modes. Firewalls implement packet filtering using rules based on IP addresses, ports, and protocols; stateful inspection tracks connection states. Intrusion Detection Systems (IDS) apply signature-based or anomaly-based detection. DDoS mitigation employs rate limiting, blackholing, and scrubbing centers. Public Key Infrastructure (PKI) underpins trust with certificate authorities issuing X.509 certificates, validated via certificate chains and revocation lists (CRLs, OCSP).

## Mastery Levels

L1: Understand basic network components—routers, switches, IP addresses.  
L2: Configure simple LAN with IPv4 addressing and DHCP.  
L3: Analyze packet headers and trace routes using tools like Wireshark and traceroute.  
L4: Implement subnetting and VLAN segmentation for network optimization.  
L5: Deploy routing protocols (OSPF, BGP) and interpret routing tables.  
L6: Design and troubleshoot TCP congestion control and flow mechanisms under variable RTTs.  
L7: Architect secure VPNs using IPsec with custom policy sets and cryptographic suites.  
L8: Innovate scalable, multi-protocol network architectures integrating SDN, NFV, and quantum-safe cryptography.

## Mechanisms

In computer networks, data transmission occurs through a series of mechanisms that enable devices to communicate with each other. The process begins with the creation of data packets, which are formatted according to the Internet Protocol (IP) and include source and destination IP addresses, as well as sequence numbers for reassembly. The packets are then passed to the network interface, where they are framed with headers and trailers that provide error detection and correction capabilities. The framed packets are transmitted over the physical medium, such as Ethernet or Wi-Fi, to the nearest router. The router examines the destination IP address and forwards the packet to the next hop on the path to the destination network. This process, known as routing, is facilitated by routing tables that are constructed using protocols such as Border Gateway Protocol (BGP) or Open Shortest Path First (OSPF). As the packet traverses the network, it may be subject to congestion control mechanisms, such as TCP's slow-start algorithm, which regulate the transmission rate to prevent network overload. Upon arrival at the destination device, the packet is reassembled into its original form and delivered to the intended application, which interprets the data according to the specified protocol, such as HTTP or FTP. Throughout this process, error detection and correction mechanisms, such as checksums and acknowledgments, ensure the integrity and reliability of the data transmission.

## Methods And Frameworks

In computer networks, several methods and frameworks are employed to design, analyze, and optimize network performance. The OSI model is a 7-layer framework used to standardize network communication, with each layer having distinct functions. The TCP/IP model is a 4-layer framework used in the internet, with layers for network access, internet, transport, and application. 
The Distance-Vector Routing method is used in routing protocols such as RIP, where each router shares its routing table with neighbors, and is suitable for small networks. 
Link-State Routing method is used in protocols like OSPF, where each router shares its link state with all other routers, and is suitable for large networks. 
The Shortest Path Routing formula, using Dijkstra's algorithm or Bellman-Ford algorithm, is used to find the minimum hop path between two nodes in a network. 
Failure modes include routing loops, network congestion, and packet loss, which can be mitigated using methods like packet buffering, traffic shaping, and error correction. 
The Waterfall model is a framework used in network development, where each phase is completed before moving to the next, and is suitable for small, well-defined networks. 
The Agile model is a framework used in network development, where development is iterative and incremental, and is suitable for large, complex networks. 
Each method and framework has its strengths and weaknesses, and the choice of which to use depends on the specific network requirements and constraints.

## Worked Examples

To illustrate key concepts in computer networks, consider the following examples. 
1. Calculating Network Throughput: A network has a bandwidth of 100 Mbps and a packet size of 1000 bytes. If the network is 90% utilized, what is the throughput in packets per second? 
First, convert the bandwidth to bytes per second: 100 Mbps * (10^6 bits/1 Mbps) * (1 byte/8 bits) = 12,500,000 bytes/second. 
Then, calculate the throughput: 12,500,000 bytes/second * 0.9 * (1 packet/1000 bytes) = 11,250 packets/second. 
2. Determining Network Delay: A packet travels over a network with a propagation delay of 10 ms, a transmission delay of 5 ms, and a processing delay of 2 ms. What is the total delay experienced by the packet? 
The total delay is the sum of the individual delays: 10 ms (propagation) + 5 ms (transmission) + 2 ms (processing) = 17 ms. 
3. Calculating Subnet Masks: A network has an IP address of 192.168.1.0 and a subnet mask of 255.255.255.224. How many subnets and hosts are possible? 
First, convert the subnet mask to binary: 255.255.255.224 = 11111111.11111111.11111111.11100000. 
Then, calculate the number of subnets (2^(number of subnet bits)) and hosts (2^(number of host bits) - 2): 2^3 = 8 subnets, 2^5 - 2 = 30 hosts.

## Applications

Computer networks have numerous applications in various domains. In the field of education, networks enable the creation of online learning platforms, allowing students to access course materials, participate in discussions, and submit assignments remotely. In healthcare, networks facilitate the exchange of medical records, telemedicine, and remote monitoring of patients. In finance, networks secure online transactions, enable mobile banking, and support stock trading. In the context of the Internet of Things (IoT), networks connect devices such as sensors, actuators, and smart home devices, enabling automation and data collection. Additionally, networks are crucial in cloud computing, allowing users to access and share resources, such as storage and applications, over the internet. In the realm of entertainment, networks support online gaming, video streaming, and social media platforms. Furthermore, networks play a vital role in organizational operations, including communication, data sharing, and collaboration among employees. The design and implementation of computer networks must consider factors such as scalability, security, and reliability to support these diverse applications.

## Common Errors

In computer networks, practitioners often make mistakes that can lead to network failures, security breaches, or performance degradation. One common error is the incorrect configuration of subnet masks, which can result in IP address conflicts and routing issues. Another mistake is the failure to implement proper network segmentation, allowing malicious traffic to spread across the network. Many practitioners also neglect to regularly update network device firmware and software, leaving them vulnerable to known security exploits. Additionally, incorrect implementation of Quality of Service (QoS) policies can lead to network congestion and poor performance. Furthermore, misunderstanding the differences between TCP and UDP protocols can result in inappropriate protocol selection for specific applications, causing issues with reliability and throughput. These errors often stem from a lack of understanding of fundamental networking concepts, such as the OSI model, TCP/IP protocol suite, and network architecture design principles.

## Advanced

The field of computer networks is continually evolving, with ongoing research focused on addressing emerging challenges and exploring new technologies. At the graduate level, students delve into advanced topics such as software-defined networking (SDN), network functions virtualization (NFV), and network slicing. These concepts enable the creation of more flexible, scalable, and secure networks. Researchers are also investigating the application of artificial intelligence (AI) and machine learning (ML) to network management, including predictive maintenance, traffic optimization, and anomaly detection. Open questions in the field include the development of robust security protocols for IoT devices, the optimization of network protocols for real-time applications, and the design of scalable architectures for edge computing. Furthermore, the increasing adoption of 5G and 6G networks is driving research into new wireless technologies, such as millimeter wave and terahertz communications, and the integration of networking with other fields, like cloud computing and data science. As the field continues to advance, it is likely that we will see the emergence of new network architectures, such as fog computing and tactile internet, which will require innovative solutions to address the associated challenges.
