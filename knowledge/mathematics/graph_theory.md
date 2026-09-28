---
key: graph_theory
title: "Graph Theory"
program: mathematics
course_level: 3
dna16: "0701201842610255"
l4_address: "S6:P1960514806"
chain256_anchor: "1214580771220379030566203711334206230341217933420174604421414898157828209582705909656069851233420872422860813342001457657674487807437662908826370366693003053342004757975301334217090235742936130700461552639261082916877697334210553146062133421271300044668895"
updated_at: "2026-08-26T05:57:33.426Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Graph Theory

> name heuristic - model placement unavailable

## Foundations

Graph theory is the mathematical study of graphs, defined as ordered pairs \( G = (V, E) \) where \( V \) is a finite set of vertices (nodes) and \( E \subseteq V \times V \) is a set of edges (links). Edges may be undirected (unordered pairs) or directed (ordered pairs), yielding undirected or directed graphs (digraphs). Graph theory abstracts relationships and connectivity, foundational in combinatorics, computer science, and discrete mathematics. Key first principles include adjacency, incidence, degree (number of incident edges per vertex), paths, cycles, connectivity, and subgraphs. Graphs may have loops or multiple edges (multigraphs), but simple graphs exclude these. Central problems involve traversal, coloring, matching, and optimization.

1. ADJACENCY AND INCIDENCE MATRICES:  
The adjacency matrix \( A \) of a graph \( G \) with \( n = |V| \) vertices is an \( n \times n \) matrix where \( A_{ij} = 1 \) if edge \((v_i, v_j) \in E\), else 0. For undirected graphs, \( A \) is symmetric. The incidence matrix \( B \) is an \( n \times m \) matrix (\(m = |E|\)) with \( B_{ij} = 1 \) if vertex \( v_i \) is incident to edge \( e_j \), 0 otherwise; for directed graphs, entries are \( +1 \) for heads and \(-1\) for tails. These matrices enable algebraic graph analysis, e.g., spectral graph theory uses eigenvalues of \( A \) or the Laplacian \( L = D - A \) (where \( D \) is the degree matrix) to study connectivity and expansion.

2. PATHS, CYCLES, AND CONNECTIVITY:  
A path is a sequence of vertices with consecutive edges; a cycle is a path whose start and end vertices coincide. The length of a path is the number of edges. Connectivity is characterized by the existence of paths between vertices. The graph is connected if any two vertices are joined by a path. Menger’s theorem states that the minimum number of vertices (or edges) whose removal disconnects two nonadjacent vertices equals the maximum number of pairwise internally vertex-disjoint (or edge-disjoint) paths between them. The concept of strongly connected components applies to digraphs, where each component is a maximal subgraph with directed paths between every pair of vertices.

3. GRAPH COLORING AND CHROMATIC POLYNOMIALS:  
Vertex coloring assigns colors to vertices so that no two adjacent vertices share the same color. The chromatic number \(\chi(G)\) is the minimum number of colors needed. The Four Color Theorem asserts \(\chi(G) \leq 4\) for planar graphs. The chromatic polynomial \( P(G, k) \) counts the number of proper \( k \)-colorings of \( G \). It satisfies the deletion-contraction recurrence:  
\[ P(G, k) = P(G - e, k) - P(G / e, k) \]  
where \( G - e \) is \( G \) with edge \( e \) deleted, and \( G / e \) is \( G \) with \( e \) contracted. Chromatic polynomials generalize coloring and relate to the Tutte polynomial.

4. MATCHINGS AND HALL’S THEOREM:  
A matching \( M \subseteq E \) is a set of edges without common vertices. A maximum matching has the largest cardinality. In bipartite graphs \( G = (U \cup W, E) \), Hall’s Marriage Theorem provides a necessary and sufficient condition for a perfect matching covering \( U \): for every subset \( S \subseteq U \),  
\[ |N(S)| \geq |S| \]  
where \( N(S) \) is the neighborhood of \( S \). The Hungarian algorithm solves the maximum bipartite matching problem in \( O(n^3) \) time, and Edmonds’ Blossom algorithm generalizes to non-bipartite graphs.

5. PLANAR GRAPHS AND KURATOWSKI’S THEOREM:  
A planar graph can be embedded in the plane without edge crossings. Kuratowski’s theorem states that a graph is planar if and only if it contains no subgraph homeomorphic to \( K_5 \) (complete graph on 5 vertices) or \( K_{3,3} \) (complete bipartite graph with partitions of size 3). Euler’s formula for connected planar graphs:  
\[ |V| - |E| + |F| = 2 \]  
where \( F \) is the number of faces in a planar embedding. This formula bounds edges by \( |E| \leq 3|V| - 6 \) for simple planar graphs.

6. SPECTRAL GRAPH THEORY AND LAPLACIAN MATRICES:  
The Laplacian matrix \( L = D - A \) is symmetric positive semidefinite. Its eigenvalues \( 0 = \lambda_1 \leq \lambda_2 \leq \cdots \leq \lambda_n \) encode structural properties:  
- \( \lambda_2 \), the algebraic connectivity or Fiedler value, measures graph connectivity; \( \lambda_2 > 0 \) iff \( G \) is connected.  
- The multiplicity of 0 eigenvalues equals the number of connected components.  
Spectral clustering algorithms partition graphs by eigenvectors of \( L \). Cheeger’s inequality relates \( \lambda_2 \) to isoperimetric constants, bounding expansion.

7. RANDOM GRAPHS AND ERDŐS-RÉNYI MODEL:  
The Erdős-Rényi model \( G(n, p) \) constructs a graph on \( n \) vertices where each edge is included independently with probability \( p \). Threshold functions characterize phase transitions, e.g., the emergence of a giant component occurs near \( p = \frac{1}{n} \). The expected number of edges is \( \binom{n}{2} p \). Connectivity threshold is at \( p = \frac{\ln n}{n} \). The model underpins probabilistic combinatorics and network theory.

In graph theory, a **graph** is a non-empty set of objects, where some pairs of these objects are connected by links. The objects are called **vertices** (or **nodes**), and the links are called **edges**. A graph is typically denoted as G = (V, E), where V is the set of vertices and E is the set of edges. A **simple graph** is an undirected graph that has no multiple edges between any pair of vertices and no self-loops (edges that begin and end at the same vertex). In a **directed graph** (or **digraph**), the edges have direction and are called **arcs**. The number of edges incident to a vertex is called its **degree**. In a directed graph, the **in-degree** of a vertex is the number of edges ending at that vertex, and the **out-degree** is the number of edges starting at that vertex. A **subgraph** is a graph whose vertices and edges are subsets of another graph. A **path** is a sequence of vertices and edges where each edge's endpoints are the preceding and following vertices in the sequence. A **cycle** is a path that starts and ends at the same vertex, with no repeated edges. Two vertices are **adjacent** if they are connected by an edge. A graph is **connected** if there is a path between every pair of vertices.

## Mastery Levels

L1: Understand basic definitions of vertices, edges, and simple graphs.  
L2: Compute adjacency and incidence matrices for small graphs.  
L3: Identify paths, cycles, and connected components in given graphs.  
L4: Apply Hall’s theorem to verify perfect matchings in bipartite graphs.  
L5: Use chromatic polynomials and the deletion-contraction recurrence for coloring counts.  
L6: Prove planarity using Kuratowski’s theorem and Euler’s formula.  
L7: Analyze spectral properties of Laplacians to infer connectivity and cluster structure.  
L8: Formulate and prove advanced theorems in random graph theory and spectral graph optimization.

## Mechanisms

Graph theory operates through several key mechanisms that enable the representation and analysis of complex relationships between objects. The fundamental mechanism involves the use of vertices (also known as nodes) and edges to model these relationships. Vertices represent the objects of interest, while edges represent the connections or relationships between these objects. The causal chain begins with the definition of a graph, which is a set of vertices connected by edges. Each edge has two endpoints, and the relationship between vertices is determined by the presence or absence of an edge between them. The next step in the mechanism is the assignment of properties to the edges, such as weight, direction, or label, which allows for the representation of different types of relationships. The graph can then be analyzed using various algorithms and techniques, such as graph traversal, shortest path algorithms, and network flow algorithms, to extract information about the relationships between the objects. The traversal of a graph, for example, involves visiting each vertex in a systematic order, following the edges to move from one vertex to another. This process can be used to identify connected components, find the shortest path between two vertices, or determine the minimum spanning tree of a graph. The mechanism of graph theory also involves the use of graph invariants, such as degree sequence, adjacency matrix, and Laplacian matrix, which provide a way to describe and compare the structure of different graphs. Overall, the mechanisms of graph theory provide a powerful framework for modeling and analyzing complex relationships in a wide range of fields, from computer science and engineering to biology and social science.

## Methods And Frameworks

Graph theory employs various methods and frameworks to analyze and solve problems. The Adjacency Matrix method is used to represent graphs as matrices, facilitating computations such as graph isomorphism and shortest paths. It is particularly useful for dense graphs, but its failure mode lies in its inefficiency for sparse graphs due to excessive memory usage. 
The Incident Matrix method, on the other hand, is suitable for representing bipartite graphs and is useful for finding matchings and coverings. However, its failure mode is the difficulty in computing graph properties such as connectivity and shortest paths. 
Dijkstra's algorithm is a widely used method for finding the shortest path between two nodes in a weighted graph, with a failure mode of being inefficient for graphs with negative weight edges. 
The Depth-First Search (DFS) and Breadth-First Search (BFS) traversal methods are used to search and explore graphs, with DFS being more suitable for detecting cycles and BFS for finding shortest paths in unweighted graphs. 
The failure mode of these traversal methods lies in their inability to handle very large graphs due to excessive memory and time complexity. 
Euler's formula for planar graphs, V - E + F = 2, is a fundamental framework for analyzing planar graphs, with a failure mode of not being applicable to non-planar graphs. 
The Handshaking Lemma, which states that the sum of degrees of all vertices in a graph is equal to twice the number of edges, is a useful framework for analyzing graph properties, but its failure mode is the assumption that the graph is connected. 
These methods and frameworks are essential tools for solving problems in graph theory, and understanding their strengths and limitations is crucial for applying them effectively.

## Worked Examples

To illustrate the application of graph theory, consider the following problems. 
1. In a graph with 5 vertices, suppose the edges have weights as follows: between vertices 1 and 2, the weight is 3; between 1 and 3, the weight is 2; between 2 and 3, the weight is 1; between 2 and 4, the weight is 4; between 3 and 4, the weight is 5; and between 4 and 5, the weight is 2. Find the minimum spanning tree using Kruskal's algorithm. 
First, sort the edges by weight: (2,3) with weight 1, (1,3) with weight 2, (1,2) with weight 3, (4,5) with weight 2, (2,4) with weight 4, (3,4) with weight 5. 
Then, select the smallest edge (2,3) and add it to the tree. Next, add (1,3) and (4,5). The edge (1,2) would create a cycle, so it is not added. The minimum spanning tree has total weight 1 + 2 + 2 = 5. 
2. A graph has 4 vertices and 4 edges with the following connections: (1,2), (2,3), (3,4), and (4,1). Determine if this graph is Eulerian. 
A graph is Eulerian if it is connected and every vertex has even degree. This graph is connected since there is a path between every pair of vertices. The degrees of the vertices are: vertex 1 has degree 2, vertex 2 has degree 2, vertex 3 has degree 2, and vertex 4 has degree 2. Since all vertices have even degree, the graph is Eulerian. 
3. Consider a complete graph with 4 vertices (K4). Find the number of Hamiltonian cycles. 
A Hamiltonian cycle visits each vertex exactly once before returning to the starting vertex. For K4, we can start at any vertex, say 1. From vertex 1, there are 3 choices for the next vertex. After visiting the second vertex, there are 2 choices for the third vertex. The last vertex is fixed, as is the return to vertex 1. Thus, there are 3! = 6 Hamiltonian cycles starting from vertex 1. Since there are 4 possible starting vertices, but each cycle is counted 4 times (once for each starting point), the total number of distinct Hamiltonian cycles is 6.

## Applications

Graph theory has numerous applications in various fields, including computer science, operations research, and engineering. In computer networks, graph theory is used to model and analyze network topology, ensuring efficient data transmission and minimizing delays. The shortest path problem, which involves finding the minimum-weight path between two nodes in a weighted graph, is a fundamental problem in graph theory with applications in traffic routing and logistics. 
In social network analysis, graph theory is used to study the structure and behavior of social networks, including the identification of clusters, communities, and influential individuals. The concept of centrality measures, such as degree centrality and betweenness centrality, helps to identify key nodes and edges in a network. 
In biology, graph theory is applied to the study of protein-protein interactions, gene regulatory networks, and phylogenetic trees. The analysis of these networks helps researchers understand the underlying mechanisms and relationships between different biological components. 
In transportation systems, graph theory is used to optimize routes, schedules, and traffic flow, reducing congestion and improving travel times. The traveling salesman problem, which involves finding the shortest possible tour that visits a set of cities and returns to the starting point, is a classic problem in graph theory with applications in logistics and supply chain management. 
The application of graph theory to real-world problems involves the use of various algorithms and techniques, such as Dijkstra's algorithm, Bellman-Ford algorithm, and topological sorting, to name a few. These algorithms enable the efficient solution of graph-related problems, making graph theory a fundamental tool in many fields.

## Common Errors

In graph theory, common mistakes often arise from misconceptions about basic definitions and properties. One frequent error is confusing the terms "connected" and "biconnected". A connected graph is one in which there is a path between every pair of vertices, whereas a biconnected graph is a connected graph that remains connected after the removal of any single vertex. Practitioners may incorrectly assume that a graph is biconnected simply because it is connected, overlooking the possibility of articulation points (vertices whose removal increases the number of connected components). Another mistake is misinterpreting the concept of graph isomorphism. Graphs are isomorphic if there exists a bijection between their vertex sets that preserves adjacency, but some may incorrectly conclude that two graphs are isomorphic based solely on visual inspection or similarity in degree sequences, without verifying the formal definition. Additionally, when applying graph algorithms, such as Dijkstra's or Bellman-Ford, errors can occur if the practitioner fails to consider the possibility of negative-weight edges or neglects to initialize distances and predecessors correctly. These mistakes can lead to incorrect results or inefficient computations, highlighting the importance of careful attention to definitions and algorithmic details in graph theory.

## Advanced

Graph theory has numerous advanced extensions and open questions that are currently being explored by researchers. One such area is the study of graph invariants, such as the Tutte polynomial, which encodes information about a graph's structure and properties. Another area is the investigation of graph minors, which involves studying the properties of graphs that can be obtained by contracting edges or deleting vertices. The Graph Minor Theorem, proved by Robertson and Seymour, is a fundamental result in this area. Additionally, the study of graph homomorphisms and the related concept of graph limits are active areas of research. The field is also moving towards the study of random graphs and their properties, such as the emergence of giant components and the behavior of random graph processes. Open questions in graph theory include the famous P versus NP problem, which deals with the complexity of graph algorithms, and the Erdős-Hajnal conjecture, which concerns the structure of graphs with certain properties. Researchers are also exploring the applications of graph theory to other fields, such as computer science, biology, and physics, and developing new tools and techniques to analyze and understand complex networks. The use of algebraic and topological methods, such as graph cohomology and graph topology, is also becoming increasingly important in the study of graph theory.
