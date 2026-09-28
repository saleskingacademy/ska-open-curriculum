---
key: distributed_systems
title: "Distributed Systems"
program: computer_science
course_level: 4
dna16: "0701201816782365"
l4_address: "S6:P886522232"
chain256_anchor: "0718127059501009133274460847139308363512272013930608593276868020087426814186140006871395097713931771137640581393014765306980004401602775644517101130185206471393080922311365139313612718241748940376772636488247114629360103139302824442344613930133773244691247"
updated_at: "2026-08-26T07:51:13.937Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Distributed Systems

> name heuristic - model placement unavailable

## Foundations

Distributed systems are collections of independent computers that appear to users as a single coherent system. Their core principle is **concurrency of components**, **lack of a global clock**, and **independent failures**, which necessitate algorithms for coordination, consistency, fault tolerance, and scalability. At the heart lies the **CAP theorem** (Brewer’s theorem, 2000), stating that a distributed system can simultaneously guarantee only two of Consistency, Availability, and Partition tolerance. Distributed systems leverage **message passing** over unreliable networks, requiring protocols for **consensus**, **replication**, and **failure detection**. The **happens-before relation** (Lamport, 1978) formalizes event ordering without a global clock, enabling causal consistency models. Key challenges include **partial failures**, **network partitions**, and **heterogeneity**.

In computer science, a Distributed System is a collection of independent computers, known as nodes, that appear to be a single, cohesive system to users. These nodes, also referred to as hosts or machines, are connected through a communication network and coordinate their actions to achieve a common goal. A key characteristic of distributed systems is the lack of a shared memory space, meaning each node has its own private memory.

Core definitions include: 
- **Node**: an independent computer within the distributed system, capable of performing computations and storing data.
- **Network**: the communication infrastructure that connects nodes, enabling them to exchange information.
- **Distributed Algorithm**: a set of rules that nodes follow to achieve a specific goal, taking into account the decentralized nature of the system.
- **Concurrency**: the ability of nodes to perform tasks simultaneously, which is fundamental to achieving scalability and efficiency in distributed systems.
- **Fault Tolerance**: the system's ability to continue functioning even when one or more nodes fail or experience errors, ensuring reliability and availability.
- **Scalability**: the system's capacity to handle increased load and expand its capabilities by adding more nodes, without compromising performance.

Understanding these first principles and vocabulary is crucial for designing, implementing, and maintaining distributed systems that meet the requirements of modern computing applications.

## Section

CONSENSUS ALGORITHMS – RAFT  
Raft (Ongaro & Ousterhout, 2014) is a consensus algorithm designed for understandability and practical deployment. It ensures **state machine replication** by electing a leader who manages log replication. Raft operates in terms of terms and log entries:  
1. **Leader election**: Nodes start as followers, become candidates on timeout, request votes; majority grants elect leader.  
2. **Log replication**: Leader appends commands to logs, sends AppendEntries RPCs; followers acknowledge.  
3. **Safety**: Leader only commits entries replicated on a majority, ensuring linearizability.  
Raft’s state transitions and RPCs (RequestVote, AppendEntries) are precisely defined. It tolerates up to ⌊(N-1)/2⌋ crash failures in an N-node cluster. Raft is implemented in systems like etcd, Consul, and HashiCorp Vault.

VECTOR CLOCKS & CAUSALITY  
Vector clocks (Fidge, 1988; Mattern, 1989) extend Lamport clocks to capture causality precisely. Each node maintains a vector of counters, incrementing its own on events and merging received vectors by element-wise max. For events a and b with vectors V(a) and V(b):  
- a → b (a happens-before b) iff ∀i: V(a)[i] ≤ V(b)[i] and ∃j: V(a)[j] < V(b)[j].  
Vector clocks enable detection of concurrent events and are foundational for **causal consistency** in systems like COPS (Lloyd et al., 2011) and DynamoDB’s causal reads.

FAILURE DETECTION – Φ ACCRUAL FAILURE DETECTOR  
The Φ Accrual Failure Detector (Hayashibara et al., 2004) models failure suspicion as a continuous variable Φ rather than a binary suspect/trust. It estimates the probability that a heartbeat is late based on a history of inter-arrival times, using a normal distribution model.  
- Φ = -log10(1 - F(t)), where F(t) is the cumulative distribution function of heartbeat arrival times.  
- A threshold (e.g., Φ > 8) triggers suspicion.  
This probabilistic model adapts to network variability, improving failure detection accuracy in systems like Apache Cassandra.

CONSISTENCY MODELS – LINEARIZABILITY VS SEQUENTIAL CONSISTENCY  
Linearizability (Herlihy & Wing, 1990) is the gold standard consistency model: operations appear instantaneous and respect real-time ordering. Formally, a history H is linearizable if there exists a sequential permutation S of H preserving program order and real-time order, matching the specification.  
Sequential consistency (Lamport, 1979) relaxes this by only requiring a total order consistent with program order, ignoring real-time constraints.  
Systems like Google Spanner provide linearizability using TrueTime API, while DynamoDB offers eventual and sequential consistency options.

REPLICATION STRATEGIES – QUORUM SYSTEMS  
Quorum systems ensure consistency and availability by requiring read and write quorums to intersect. For N replicas, read quorum size R and write quorum size W satisfy R + W > N to guarantee overlapping sets.  
Example: In Cassandra, default N=3, W=2, R=2 ensures strong consistency on writes and reads. Quorum protocols balance latency and durability, enabling tunable consistency models.

TIME SYNCHRONIZATION – NTP & TRUE TIME  
Network Time Protocol (NTP, Mills 1985) synchronizes clocks with millisecond accuracy over the internet. It uses hierarchical strata and round-trip delay estimation.  
Google’s TrueTime API (Corbett et al., 2013) provides globally synchronized timestamps with bounded uncertainty ε (~7 ms), enabling external consistency in Spanner. TrueTime returns intervals [earliest, latest], allowing transactions to commit only when uncertainty windows do not overlap, ensuring linearizability.

DISTRIBUTED TRANSACTIONS – TWO-PHASE COMMIT (2PC)  
2PC is a blocking atomic commit protocol:  
1. **Prepare phase**: Coordinator asks participants to prepare; participants vote commit or abort.  
2. **Commit phase**: If all vote commit, coordinator sends commit; else abort.  
2PC guarantees atomicity but is vulnerable to coordinator failure, causing blocking. Optimizations include presumed commit/abort and three-phase commit (3PC) to reduce blocking.

## Mastery Levels

L1: Understand distributed systems as multiple computers working together.  
L2: Explain the CAP theorem and its implications.  
L3: Implement a basic leader election using Raft or Paxos.  
L4: Use vector clocks to detect concurrent events and causal relationships.  
L5: Configure quorum sizes to balance consistency and availability in a replicated database.  
L6: Analyze failure detection using Φ accrual failure detectors under network variability.  
L7: Design a globally consistent system using TrueTime or equivalent time synchronization.  
L8: Prove correctness and liveness properties of consensus algorithms under asynchronous failure models.

## Mechanisms

In a distributed system, mechanisms refer to the underlying processes and protocols that enable the coordination and communication among nodes. The causal chain of events in a distributed system can be broken down into several key steps: 
1. **Node Initialization**: Each node in the system initializes itself, which involves setting up its internal state, loading necessary software components, and establishing connections with other nodes. 
2. **Message Passing**: Nodes communicate with each other by sending and receiving messages, which can be achieved through various protocols such as TCP/IP, HTTP, or custom-designed protocols. 
3. **Request-Response Cycle**: A node sends a request to another node, which processes the request and sends a response back to the originating node. This cycle is the fundamental mechanism for achieving coordination and data exchange in a distributed system. 
4. **Synchronization**: To maintain consistency and ensure correct behavior, nodes may need to synchronize their actions, which can be achieved through mechanisms such as locks, semaphores, or distributed transaction protocols. 
5. **Fault Tolerance**: Distributed systems often employ mechanisms to detect and recover from node failures, such as replication, redundancy, and failure detection protocols, to ensure the overall system remains operational. 
6. **Scalability**: As the system grows, mechanisms such as load balancing, data partitioning, and distributed caching are used to ensure the system can handle increased traffic and data volume. 
These mechanisms work together to enable the distribution of resources, services, and data across multiple nodes, allowing the system to achieve its desired functionality and performance.

## Methods And Frameworks

In distributed systems, several methods and frameworks are employed to achieve scalability, reliability, and performance. The CAP Theorem, also known as Brewer's Theorem, states that it is impossible for a distributed system to simultaneously guarantee more than two out of the following three properties: Consistency, Availability, and Partition tolerance. 
The Paxos algorithm is used for achieving consensus in a distributed system, ensuring that all nodes agree on a single value. It is suitable for systems that require strong consistency, but may suffer from low availability during partitions. 
The Byzantine Fault Tolerance (BFT) algorithm is used to achieve consensus in the presence of malicious or faulty nodes. It is suitable for systems that require high security and trust, but may incur high communication overhead. 
The Leader-Based approach is used for distributed systems that require a single leader node to coordinate the actions of other nodes. It is suitable for systems that require low latency and high throughput, but may suffer from single point of failure. 
The Peer-to-Peer approach is used for distributed systems where all nodes are equal and can act as both clients and servers. It is suitable for systems that require high scalability and fault tolerance, but may suffer from high complexity and difficulty in managing node interactions. 
Each of these methods and frameworks has its own failure mode, such as network partitions, node failures, and communication errors, which must be carefully considered when designing a distributed system.

## Worked Examples

Consider a distributed system consisting of 5 nodes, each with a processing capacity of 100 MIPS (Millions of Instructions Per Second). If the system is tasked with processing 500,000 instructions, and each node has a communication overhead of 10 milliseconds per message, calculate the total processing time if the instructions are divided evenly among the nodes. 
First, calculate the processing time per node: 500,000 instructions / (5 nodes * 100 MIPS) = 1000 seconds or 1000 / 1000 = 1 second per node. 
Next, consider the communication overhead: since each node must communicate with every other node, there are 5 * (5-1) / 2 = 10 messages. With an overhead of 10 milliseconds per message, the total communication overhead is 10 * 10 = 100 milliseconds or 0.1 seconds. 
Thus, the total processing time is 1 second (processing) + 0.1 seconds (communication) = 1.1 seconds. 
In another example, suppose we have a distributed database with 3 nodes, each containing a replica of the data. If each node can process queries at a rate of 50 queries per second, and the system receives 120 queries per second, calculate the query processing capacity of the system. 
The total query processing capacity is the sum of the capacities of each node: 3 nodes * 50 queries/second/node = 150 queries/second. 
Since the system receives 120 queries/second, which is less than the total capacity, the system can process all incoming queries. 
Lastly, consider a distributed file system with 4 nodes, each with a storage capacity of 1 TB (Terabyte). If the system is tasked with storing 2.5 TB of data, and each node has a failure probability of 0.01 (1%), calculate the probability that the system can still function if one node fails. 
First, calculate the total storage capacity: 4 nodes * 1 TB/node = 4 TB. 
Since 2.5 TB is less than the total capacity, the system can store all the data. 
If one node fails, the remaining capacity is 3 TB, which is still greater than the required 2.5 TB. 
The probability that a given node fails is 0.01, and the probability that it does not fail is 0.99. 
Since there are 4 nodes, and the system can still function if one node fails, the probability of failure is the probability that more than one node fails. 
Using the binomial probability formula, we can calculate this probability as 1 - (probability that 0 nodes fail + probability that 1 node fails). 
This equals 1 - (0.99^4 + 4 * 0.01 * 0.99^3) = 1 - (0.9606 + 0.0388) = 1 - 0.9994 = 0.0006. 
Thus, the probability that the system fails is 0.0006 or 0.06%.

## Applications

Distributed systems are used in various domains, including cloud computing, where resources such as computing power, storage, and networking are provided as a service over the internet. In cloud computing, distributed systems enable scalability, reliability, and fault tolerance by allowing multiple machines to work together to provide services. For example, Amazon Web Services (AWS) and Microsoft Azure use distributed systems to manage their large-scale infrastructure. 
In big data analytics, distributed systems such as Hadoop and Spark enable the processing of large datasets across multiple machines, allowing for faster and more efficient data analysis. Distributed databases, such as Google's Bigtable and Amazon's DynamoDB, provide a scalable and reliable way to store and manage large amounts of data. 
In financial systems, distributed systems are used to support high-volume transaction processing, such as in stock exchanges and online payment systems. They provide low-latency and high-throughput processing, ensuring that transactions are processed quickly and reliably. 
Distributed systems are also used in real-time systems, such as air traffic control and autonomous vehicles, where low-latency and high-reliability are critical. They enable the processing and analysis of large amounts of data in real-time, supporting time-critical decision-making. 
In addition, distributed systems are used in social media platforms, such as Facebook and Twitter, to manage large amounts of user data and provide scalable and reliable services. They enable the handling of high volumes of user requests, ensuring that users can access and share information quickly and efficiently. 
The use of distributed systems in these domains enables organizations to build scalable, reliable, and efficient systems that can support large-scale applications and services.

## Common Errors

In distributed systems, practitioners often make mistakes that can lead to system failures, inconsistencies, or poor performance. One common error is assuming that the network is reliable, which can result in neglecting to implement adequate error handling and fault tolerance mechanisms. This can cause systems to fail or behave unexpectedly when network partitions or failures occur. Another mistake is not properly considering the trade-offs between consistency, availability, and partition tolerance, as outlined in the CAP theorem. This can lead to systems that are overly restrictive or prone to inconsistencies. Additionally, practitioners may overlook the importance of clock synchronization and assume that all nodes in the system have identical clocks, which can cause issues with timestamp-based protocols and algorithms. Furthermore, not accounting for the fallacies of distributed computing, such as assuming that latency is zero or that the network is homogeneous, can result in systems that are poorly optimized or behave unpredictably. These errors can be avoided by carefully considering the fundamental principles of distributed systems and designing systems that are robust, fault-tolerant, and scalable.

## Advanced

Distributed systems research has expanded to address complex issues such as scalability, fault tolerance, and security in large-scale deployments. Graduate-level studies delve into advanced topics like distributed transaction protocols, such as two-phase commit and Paxos, which ensure consistency across distributed databases. The CAP theorem, which states that it is impossible for a distributed data store to simultaneously guarantee more than two out of consistency, availability, and partition tolerance, is a fundamental concept in this area. Open questions include optimizing distributed system performance under varying network conditions and developing more efficient algorithms for leader election, consensus, and fault detection. The field is moving towards edge computing, fog computing, and serverless architectures, which require innovative solutions for distributed resource management, scheduling, and communication. Additionally, the integration of distributed systems with emerging technologies like blockchain, artificial intelligence, and the Internet of Things (IoT) presents new challenges and opportunities for research and development.
