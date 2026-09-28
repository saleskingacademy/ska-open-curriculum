---
key: quantum_computing
title: "Quantum Computing"
program: computer_science
course_level: 6
dna16: "0701201896568898"
l4_address: "S6:P489446160"
chain256_anchor: "1376714772258801021339527855152515047662823715251620106994801296081699153335693604645789855215250476342752691525072982300772616802224755297834961103161179101525038292922527152517616452655504701739664039207540044844374320152508134576154315251381583073406622"
updated_at: "2026-09-07T02:11:15.253Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Quantum Computing

> The course assumes advanced mathematical background and prior knowledge of quantum mechanics and computer science concepts.

## Foundations

Quantum computing is a computational paradigm leveraging quantum mechanical phenomena—superposition, entanglement, and interference—to process information encoded in quantum bits (qubits). Unlike classical bits, qubits exist in Hilbert space as vectors \(|\psi\rangle = \alpha|0\rangle + \beta|1\rangle\), where \(\alpha, \beta \in \mathbb{C}\) and \(|\alpha|^2 + |\beta|^2 = 1\). Quantum gates are unitary operators acting on qubits, evolving their states coherently. Measurement collapses the qubit state probabilistically. Quantum algorithms exploit amplitude amplification and interference patterns to achieve computational speedups, notably in factoring (Shor’s algorithm) and unstructured search (Grover’s algorithm). The quantum circuit model formalizes computation as sequences of gates on qubit registers, while alternative models include adiabatic and topological quantum computing.

In computer science, quantum computing refers to the use of quantum-mechanical phenomena, such as superposition and entanglement, to perform computations. A **qubit** (quantum bit) is the fundamental unit of quantum information, which can exist in multiple states simultaneously, represented by a complex-valued vector in a two-dimensional Hilbert space. **Superposition** is the ability of a qubit to exist in a linear combination of states, denoted as |0and |1, allowing for the exploration of an exponentially large solution space. **Entanglement** is a phenomenon where two or more qubits become correlated, enabling the creation of a shared quantum state. A **quantum gate** is a basic operation that manipulates qubits, analogous to logic gates in classical computing. **Quantum circuits** are composed of a sequence of quantum gates, which are used to perform computations on qubits. The **no-cloning theorem** states that it is impossible to create a perfect copy of an arbitrary quantum state, which has implications for quantum error correction and quantum communication. Understanding these core concepts is essential for a practitioner in the field of quantum computing.

## Quantum States And Qubits

Qubits are represented in a two-dimensional complex Hilbert space \(\mathcal{H}_2\). The Bloch sphere parameterizes pure states as \(|\psi\rangle = \cos(\theta/2)|0\rangle + e^{i\phi}\sin(\theta/2)|1\rangle\), with \(\theta \in [0,\pi]\), \(\phi \in [0,2\pi)\). Mixed states are described by density matrices \(\rho\), positive semidefinite operators with \(\mathrm{Tr}(\rho)=1\). Multi-qubit states reside in the tensor product space \(\mathcal{H}_2^{\otimes n}\). Entanglement metrics include concurrence \(C(\rho)\) and entanglement entropy \(S(\rho) = -\mathrm{Tr}(\rho \log_2 \rho)\). Bell states \(|\Phi^{\pm}\rangle = \frac{1}{\sqrt{2}}(|00\rangle \pm |11\rangle)\) exemplify maximally entangled two-qubit states.

## Quantum Gates And Circuits

Quantum gates are unitary matrices \(U \in U(2^n)\) acting on \(n\)-qubit states. Fundamental single-qubit gates include Pauli operators \(X, Y, Z\), Hadamard \(H = \frac{1}{\sqrt{2}}\begin{bmatrix}1 & 1 \\ 1 & -1\end{bmatrix}\), phase gate \(S = \begin{bmatrix}1 & 0 \\ 0 & i\end{bmatrix}\), and \(T = \begin{bmatrix}1 & 0 \\ 0 & e^{i\pi/4}\end{bmatrix}\). Two-qubit gates such as CNOT \(\mathrm{CNOT} = |0\rangle\langle0| \otimes I + |1\rangle\langle1| \otimes X\) enable entanglement generation. Universal gate sets include \(\{H, T, \mathrm{CNOT}\}\). Quantum circuits are sequences of these gates, with complexity measured in gate count and circuit depth. Circuit synthesis algorithms optimize gate decompositions to minimize error and resource overhead.

## Quantum Algorithms

Key quantum algorithms demonstrate exponential or polynomial speedups over classical counterparts. Shor’s algorithm factors an integer \(N\) in polynomial time \(O((\log N)^3)\) using quantum Fourier transform (QFT) and modular exponentiation. Grover’s algorithm performs unstructured search over \(N\) items in \(O(\sqrt{N})\) time via amplitude amplification, iterating the Grover operator \(G = (2|\psi\rangle\langle\psi| - I)O_f\) approximately \(\pi/4 \sqrt{N}\) times. Quantum phase estimation (QPE) extracts eigenvalues \(e^{2\pi i \phi}\) of unitary operators with precision \(\epsilon\) in \(O(1/\epsilon)\) steps, underpinning many algorithms. Variational Quantum Eigensolver (VQE) and Quantum Approximate Optimization Algorithm (QAOA) hybridize classical optimization with parameterized quantum circuits for near-term devices.

## Quantum Error Correction And Noise

Quantum error correction (QEC) protects fragile quantum information against decoherence and operational errors. The 9-qubit Shor code encodes one logical qubit into 9 physical qubits, correcting arbitrary single-qubit errors. The 7-qubit Steane code uses CSS (Calderbank-Shor-Steane) construction, correcting single-qubit errors with transversal gates. Surface codes, defined on 2D lattices, achieve high threshold error rates (~1%) and scalability, employing stabilizer formalism with syndrome measurements. Logical qubit fidelity depends on physical error rates \(p\), with thresholds \(p_{th}\) determining fault-tolerance feasibility. Quantum noise channels include depolarizing, amplitude damping, and phase damping, modeled by Kraus operators \(E_i\).

## Quantum Hardware Architectures

Physical realizations include superconducting qubits (transmons), trapped ions, photonic qubits, and topological qubits (Majorana zero modes). Superconducting qubits operate at ~10 mK with coherence times \(T_1 \sim 100 \mu s\), gate times ~10-50 ns, and fidelities >99%. Trapped ions achieve longer coherence (~seconds) but slower gates (~100 µs). Photonic systems leverage linear optics and measurement-based schemes. Topological qubits promise intrinsic error resilience via non-Abelian anyons but remain experimental. Control electronics, cryogenics, and qubit connectivity graphs critically impact scalability and error rates.

## Quantum Complexity Theory

Quantum complexity classes include BQP (Bounded-error Quantum Polynomial time), containing problems efficiently solvable on quantum computers. BQP is believed to strictly contain classical classes P and BPP but is contained in PSPACE. Problems like integer factoring and discrete logarithm lie in BQP but not known in P. QMA (Quantum Merlin-Arthur) generalizes NP with quantum proofs. Oracle separations and complexity-theoretic conjectures guide understanding of quantum advantage limits. Quantum supremacy experiments demonstrate tasks infeasible for classical supercomputers, e.g., random circuit sampling by Google’s Sycamore processor.

## Mastery Levels

L1: Understand qubits as superpositions of classical bits.  
L2: Implement basic quantum gates and simple circuits on simulators.  
L3: Analyze entanglement and Bell inequalities quantitatively.  
L4: Execute Grover’s and Shor’s algorithms step-by-step.  
L5: Design error-correcting codes and simulate noise models.  
L6: Optimize quantum circuits for hardware constraints and gate fidelity.  
L7: Develop hybrid quantum-classical algorithms for NISQ devices.  
L8: Contribute to fault-tolerant architectures and quantum complexity theory.

## Mechanisms

Quantum computing relies on the principles of quantum mechanics to perform computations. The process begins with the preparation of qubits, which are the fundamental units of quantum information. Qubits are unique because they can exist in multiple states simultaneously, known as a superposition. This allows a single qubit to process multiple possibilities at the same time. The next step involves entangling qubits, which creates a correlation between them, enabling the state of one qubit to depend on the state of the other. Quantum gates, the quantum equivalent of logic gates in classical computing, are then applied to the qubits to manipulate their states. These gates perform operations such as rotations, entanglement, and measurements, which are the basic building blocks of quantum algorithms. The sequence of quantum gates applied to the qubits constitutes a quantum circuit, which is the quantum equivalent of a digital circuit in classical computing. Quantum algorithms, such as Shor's algorithm for factorization and Grover's algorithm for search, are then implemented using these quantum circuits. The final step involves measuring the qubits to extract the result of the computation, which collapses the superposition of states into a single outcome. This process, known as wave function collapse, is a fundamental aspect of quantum measurement. The causal chain is as follows: qubit preparation -> entanglement -> application of quantum gates -> execution of quantum algorithm -> measurement -> result extraction.

## Methods And Frameworks

Quantum computing utilizes several methods and frameworks to solve complex problems. The Quantum Circuit Model is a widely used framework, where quantum algorithms are represented as a sequence of quantum gates, such as Hadamard, Pauli-X, and CNOT gates. This model is useful for solving problems like Shor's algorithm for factorization and Grover's algorithm for search. However, its failure mode lies in the accumulation of errors due to noisy quantum gates. 
The Adiabatic Quantum Computing model is another framework, which uses a slow and continuous transformation of a quantum system to find the global minimum of a complex function. This model is useful for solving optimization problems, but its failure mode is the potential for getting stuck in a local minimum. 
The Density Matrix formulation is a mathematical method used to describe the behavior of quantum systems, particularly in the presence of noise and decoherence. This method is useful for analyzing the robustness of quantum algorithms, but its failure mode lies in the computational complexity of calculating the density matrix for large systems. 
The Variational Quantum Eigensolver (VQE) is a hybrid quantum-classical method used to find the ground state of a quantum system. This method is useful for solving chemistry and materials science problems, but its failure mode is the potential for converging to a local minimum instead of the global minimum. 
The Quantum Approximate Optimization Algorithm (QAOA) is a method used to solve optimization problems, particularly those with a large number of local minima. This method is useful for solving problems like MaxCut and Sherrington-Kirkpatrick, but its failure mode lies in the need for careful tuning of its parameters to achieve good performance.

## Worked Examples

To illustrate the principles of quantum computing, consider the following examples. 
1. Quantum Parallelism: Suppose we have a function f(x) that takes an integer x and returns either 0 or 1. We want to evaluate f(x) for x = 0 to 7 using a quantum computer. We can create a quantum circuit with 3 qubits, representing the 8 possible inputs. By applying a Hadamard gate to each qubit, we create a superposition of all 8 states. Then, we apply the function f(x) to each state in the superposition, resulting in a superposition of the 8 possible outputs. Finally, we measure the output, collapsing the superposition to one of the 8 possible outcomes. 
2. Quantum Teleportation: Consider two parties, Alice and Bob, who share an entangled pair of qubits. Alice wants to send a qubit to Bob without physically transmitting it. She can measure her qubit in the entangled pair, causing Bob's qubit to be instantaneously affected, regardless of the distance between them. Then, Bob can apply a correction operation to his qubit, based on Alice's measurement outcome, to recover the original state of the qubit. 
3. Quantum Error Correction: Suppose we have a quantum computer with a 3-qubit register, and we want to protect it against bit flip errors. We can use a simple error correction code, such as the 3-qubit bit flip code. We encode each qubit into 3 qubits, using the encoding |0= |000and |1= |111. If a bit flip error occurs on one of the qubits, we can detect and correct it by measuring the parity of the 3 qubits. For example, if the original state is |000and a bit flip error occurs on the first qubit, resulting in |100, we can measure the parity of the 3 qubits and correct the error by flipping the first qubit back to |0.

## Applications

Quantum computing has various applications in practice, particularly in domains that require complex computations and simulations. In cryptography, quantum computers can potentially break certain classical encryption algorithms, such as RSA and elliptic curve cryptography, using Shor's algorithm. However, this also leads to the development of quantum-resistant cryptography, like lattice-based cryptography and code-based cryptography. 
In optimization problems, quantum computers can be used to solve complex problems more efficiently, such as the traveling salesman problem, using quantum algorithms like the Quantum Approximate Optimization Algorithm (QAOA). 
Additionally, quantum computing can be applied to machine learning, enabling faster processing of large datasets and improving the performance of certain machine learning algorithms, such as k-means and support vector machines, using quantum algorithms like Quantum k-Means and Quantum Support Vector Machines. 
In simulation and modeling, quantum computers can be used to simulate complex quantum systems, allowing for breakthroughs in fields like chemistry and materials science, by solving the Schrödinger equation more efficiently. 
These applications demonstrate the potential of quantum computing to revolutionize various fields and solve complex problems more efficiently.

## Common Errors

In quantum computing, practitioners often make mistakes due to misunderstandings of quantum principles and their application to computational problems. One common error is the assumption that quantum parallelism, enabled by superposition, allows for an exponential speedup in all computational tasks. However, this is incorrect because quantum algorithms must be designed to take advantage of quantum interference to cancel out incorrect solutions, and not all problems can be decomposed in a way that leverages this property. Another mistake is the failure to consider the effects of noise and error correction in quantum computations. Quantum bits (qubits) are prone to decoherence, which causes loss of quantum coherence due to interactions with the environment, leading to errors in computation. Ignoring the need for robust error correction mechanisms can result in unreliable outcomes. Additionally, some practitioners incorrectly assume that quantum computing is simply a matter of scaling up classical computing architectures, neglecting the fundamentally different principles of quantum information processing, such as the use of quantum gates and the importance of maintaining quantum coherence. These misunderstandings can lead to incorrect algorithm design, inefficient use of quantum resources, and unrealistic expectations about the capabilities of quantum computing systems.

## Advanced

The graduate-level extensions of quantum computing involve exploring the theoretical foundations and limitations of quantum computation. One key area of research is quantum complexity theory, which studies the resources required to solve computational problems on a quantum computer. This includes understanding the relationships between quantum classes such as BQP (Bounded-Error Quantum Polynomial Time) and NP (Nondeterministic Polynomial Time), and exploring the implications of quantum computing for cryptography and coding theory. Another area of research is the development of quantum algorithms for solving specific problems, such as simulating quantum systems, factoring large numbers, and searching unsorted databases. Open questions in the field include the resolution of the quantum fault tolerance threshold, which determines the maximum error rate that can be tolerated in a quantum computation, and the development of a scalable and reliable method for quantum error correction. The field is moving towards the development of practical quantum computing architectures, such as topological quantum computing and adiabatic quantum computing, and exploring the applications of quantum computing in fields such as machine learning, optimization, and materials science. Researchers are also investigating the potential for quantum computing to solve problems that are intractable on classical computers, such as simulating complex quantum systems and optimizing complex processes.
