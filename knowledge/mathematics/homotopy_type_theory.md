---
key: homotopy_type_theory
title: "Homotopy Type Theory"
program: mathematics
course_level: 3
dna16: ""
l4_address: "S6:P1142142344"
chain256_anchor: "0743992237564326022722891164284610717136930528461569174900203092036313660018341208005490599828460555419245672846151592010418103903112989335464611165156384432846071592420775284608972228683522000729509924251988164053181957284614703651145428461703854500180087"
updated_at: "2026-08-26T05:59:28.467Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Homotopy Type Theory

> name heuristic - model placement unavailable

## Foundations

Homotopy Type Theory (HoTT) is a foundational framework synthesizing intensional Martin-Löf Type Theory (MLTT) with concepts from homotopy theory and higher category theory. It reinterprets types as spaces (homotopy types), terms as points, and equalities as paths, thereby internalizing homotopical notions into type theory. The core innovation is the Univalence Axiom (Voevodsky, 2013), which states that equivalences between types correspond to identifications, collapsing equivalence and equality. This elevates identity types (Id-types) from mere propositional equalities to structured path spaces, enabling the encoding of ∞-groupoid structures within type theory. The foundational syntax includes dependent types, Π-types (dependent function types), Σ-types (dependent pair types), identity types, and universes (types of types), with intensional identity types supporting higher inductive types (HITs) to construct spaces like spheres and suspensions. HoTT thereby provides a computationally amenable language for synthetic homotopy theory and a new paradigm for foundations of mathematics.

1. IDENTITY TYPES AND PATH SPACES:  
Identity types Id_A(a,b) represent the type of paths between points a,b : A. Formally, for any type A : 𝒰 and terms a,b : A, Id_A(a,b) is a type whose inhabitants correspond to homotopies from a to b. The introduction rule is refl_a : Id_A(a,a), representing the constant path. Elimination (J-rule) allows reasoning by path induction: given C : Π(x,y:A).Id_A(x,y) → 𝒰 and d : Π(x:A).C(x,x,refl_x), one obtains f : Π(x,y:A)(p:Id_A(x,y)).C(x,y,p). This encodes the fundamental groupoid structure of types, with higher identity types iterating to form ∞-groupoids.

2. UNIVALENCE AXIOM:  
Formulated by Voevodsky, the Univalence Axiom states that for types A,B : 𝒰, the canonical map  
ua : (A ≃ B) → Id_𝒰(A,B)  
is an equivalence, where A ≃ B is the type of equivalences (homotopy equivalences) between A and B. This axiom identifies equivalence with equality in the universe, enabling transport of properties and constructions along equivalences. It is a higher inductive principle that cannot be derived from MLTT alone and is crucial for synthetic homotopy theory, allowing the construction of isomorphic structures to be identified.

3. HIGHER INDUCTIVE TYPES (HITs):  
HITs extend inductive types by allowing constructors for points, paths, and higher paths simultaneously. For example, the circle S¹ is defined as a HIT with:  
- base : S¹  
- loop : Id_{S¹}(base, base)  
This encodes the fundamental group π₁(S¹) ≅ ℤ synthetically. HITs enable the direct encoding of homotopical spaces and their universal properties inside type theory, facilitating synthetic proofs of classical results such as the Seifert-van Kampen theorem and computations of homotopy groups.

4. HIGHER CATEGORY THEORY INTERPRETATION:  
Types in HoTT correspond to ∞-groupoids, with identity types modeling morphisms, 2-morphisms, etc. The syntax of MLTT with identity types models weak ω-groupoids, where composition and coherence conditions are encoded via higher identities. This provides a computational framework for higher category theory, allowing formalization of ∞-categories, (∞,1)-categories, and their homotopical properties within type theory.

5. SEMANTICS VIA MODEL CATEGORIES AND SIMPLICIAL SETS:  
HoTT can be semantically interpreted in Quillen model categories, particularly the category of simplicial sets with the Kan model structure. Types correspond to Kan complexes, terms to vertices, and identity types to path spaces. The univalence axiom corresponds to the existence of a univalent universe object in these models (Voevodsky’s simplicial set model). This semantic grounding ensures consistency and provides tools for constructing models of HoTT.

6. TRANSPORT AND EQUIVALENCE:  
Given a family of types P : A → 𝒰 and a path p : Id_A(a,b), transport along p is a function  
transport^P_p : P(a) → P(b),  
defined by path induction. Transport enables the movement of data and proofs along equalities, fundamental for reasoning about dependent types. Combined with univalence, transport along equivalences allows the replacement of types by equivalent ones in all contexts, underpinning the structural nature of mathematics in HoTT.

7. SYNTHETIC HOMOTOPY THEORY APPLICATIONS:  
HoTT enables the synthetic development of classical homotopy theory results without recourse to set-theoretic topology. For instance, the calculation of π₁(S¹) = ℤ is established via the encode-decode method, employing HITs and identity types. Similarly, the Blakers-Massey theorem and Freudenthal suspension theorem have synthetic proofs in HoTT, illustrating its power as a unifying framework for algebraic topology and type theory.

In Homotopy Type Theory (HoTT), the core definitions are based on type theory, which is a branch of mathematical logic. A **type** is a set of objects, and each object is said to **inhabit** or be an **element** of that type. The **propositional equality** of two objects of the same type, denoted as $a = b$, is a **proposition**, which is a statement that can be either true or false. A **type family** is a collection of types indexed by the elements of another type. 
The **homotopy** aspect of HoTT is based on the concept of **paths** between objects of the same type. A path from $a$ to $b$ is denoted as $p : a = b$, and it represents a continuous deformation of $a$ into $b$. Two objects are **homotopy equivalent** if there is a path between them. 
The **univalence axiom**, introduced by Vladimir Voevodsky, states that two types are equal if and only if they are homotopy equivalent. This axiom is a fundamental principle of HoTT, as it allows for the identification of equivalent types. 
A **function** from one type to another is a relation between the elements of the two types, and it assigns to each element of the domain type an element of the codomain type. The **dependent sum** and **dependent product** are two important constructions in HoTT, which generalize the notions of disjoint union and Cartesian product, respectively. 
The **Martin-Löf type theory**, developed by Per Martin-Löf, is a formal system that provides the foundation for HoTT. It includes rules for constructing and manipulating types, as well as a notion of **judgment**, which is a statement about the validity of a proposition or the inhabitation of a type.

## Mastery Levels

L1 Beginner: "Types are spaces, and equalities are paths."  
L2 Novice: "Identity types encode homotopical paths between terms."  
L3 Intermediate: "Univalence equates equivalences with equalities in universes."  
L4 Advanced: "Higher inductive types construct spaces with specified path constructors."  
L5 Proficient: "Types form ∞-groupoids modeled by iterated identity types."  
L6 Expert: "Simplicial sets provide a Quillen model validating univalence."  
L7 Master: "Synthetic proofs of classical homotopy theorems use HITs and path induction."  
L8 Grandmaster: "HoTT unifies foundations, homotopy, and higher category theory via computational higher groupoids and univalent universes."

## Mechanisms

In Homotopy Type Theory (HoTT), the mechanisms underlying the theory rely on the interplay between type theory, homotopy theory, and higher-dimensional category theory. The core idea is to interpret types as spaces and propositions as subspaces, where the equality type x = y represents the space of paths between x and y. The type formers, such as dependent sums and products, are interpreted as constructing new spaces from existing ones. 
The univalence axiom, a central component of HoTT, states that equivalent types are equal, which is formalized as an equivalence between the type of equivalences between two types and the type of equalities between them. This axiom has far-reaching consequences, including the ability to transport structures along equivalences, which is a key feature of HoTT. 
The mechanisms of HoTT can be broken down into several key steps: 
1. Type formation: Types are formed using type formers, such as dependent sums and products, which construct new spaces from existing ones. 
2. Equality type formation: The equality type x = y is formed, representing the space of paths between x and y. 
3. Univalence axiom application: The univalence axiom is applied to equivalent types, establishing an equivalence between the type of equivalences and the type of equalities. 
4. Structure transport: Structures are transported along equivalences, allowing for the transfer of properties between equivalent types. 
5. Homotopy theory application: Homotopy theory is applied to the spaces represented by types, allowing for the study of their properties and behavior. 
These mechanisms work together to provide a framework for reasoning about spaces and their properties, enabling the development of new insights and results in mathematics.

## Methods And Frameworks

In Homotopy Type Theory (HoTT), several methods and frameworks facilitate the study of homotopy types and their properties. The Univalence Axiom is a central concept, stating that equivalent types are equal, and is used to establish equivalences between types. The transport method is used to transfer properties along equivalences, while the encode-decode method is employed to construct homotopies between functions. The Seifert-van Kampen theorem provides a framework for computing the fundamental group of a space, and the Blakers-Massey theorem is used to establish excision properties. The model of simplicial sets, developed by Kan, provides a framework for studying homotopy types using combinatorial methods. The cubical model, introduced by Coquand, provides an alternative framework for studying homotopy types using cubical structures. Each of these methods and frameworks has its own failure mode, such as the univalence axiom failing for non-univalent types, and the transport method failing when the equivalence is not an equivalence of structures. Understanding these methods and frameworks, as well as their limitations, is crucial for working effectively in HoTT.

## Worked Examples

To illustrate the principles of Homotopy Type Theory, consider the following examples. 
1. Given a type $A$ with two elements $a, b: A$, and a function $f: A \to A$ defined by $f(a) = b$ and $f(b) = a$, show that $a$ and $b$ are homotopy equivalent. 
The homotopy equivalence can be established by exhibiting a homotopy $H: A \times I \to A$ between the identity function $id_A$ and the function $f$, where $I$ is the interval type. 
2. Let $S^1$ be the circle type, defined as the type of pairs $(x, y: \mathbb{R})$ satisfying $x^2 + y^2 = 1$. 
Show that the function $loop: S^1 \to S^1$ defined by $loop(x, y) = (-x, -y)$ is homotopic to the identity function. 
A homotopy $H: S^1 \times I \to S^1$ can be defined by $H((x, y), t) = ((1-t)x + tx, (1-t)y + ty)$ for $t: I$. 
3. Consider the type $A$ of integers $\mathbb{Z}$, and the function $f: A \to A$ defined by $f(n) = n + 1$. 
Show that $f$ is not homotopic to the identity function $id_A$. 
Assume for contradiction that there exists a homotopy $H: A \times I \to A$ between $f$ and $id_A$. 
Then for any $n: A$, we have $H(n, 0) = n$ and $H(n, 1) = n + 1$. 
However, since $A$ is discrete, any homotopy $H$ must be constant in the $I$ direction, contradicting the assumption.

## Applications

Homotopy Type Theory (HoTT) has far-reaching implications in various areas of mathematics and computer science. In type theory, HoTT provides a framework for reasoning about the equality of types, enabling the development of more expressive and flexible type systems. This has significant applications in programming languages, particularly in the design of dependently typed programming languages such as Idris and Agda. The univalence axiom, a central concept in HoTT, allows for the equivalence of types to be expressed as an equality, facilitating the construction of more efficient and expressive type checkers. 
In algebraic topology, HoTT provides a new perspective on the study of homotopy groups and spaces, allowing for the formalization of classical results in a more synthetic and intuitive manner. The use of HoTT in this context enables the development of new tools and techniques for computing homotopy groups and studying the properties of spaces. 
Furthermore, HoTT has connections to higher category theory, providing a framework for the study of higher-dimensional categorical structures. This has potential applications in areas such as quantum field theory and condensed matter physics, where higher-dimensional structures play a crucial role. 
The applications of HoTT are still an active area of research, with potential implications for fields such as formal verification, programming language design, and pure mathematics.

## Common Errors

In Homotopy Type Theory (HoTT), several common mistakes arise from misunderstandings of its foundational concepts and their implications. One such error is the confusion between the propositional and judgmental equalities. Practitioners may incorrectly assume that these two types of equalities are interchangeable, which is not the case. Propositional equality is a type that asserts the equality of two terms, whereas judgmental equality is a meta-level statement about the equality of two terms. This distinction is crucial because HoTT relies on the difference between these equalities to construct its homotopy-theoretic interpretations.

Another mistake is the failure to recognize that the univalence axiom does not imply the existence of a global choice operator. The univalence axiom states that equivalent types are equal, but this does not provide a way to uniformly select an element from each non-empty type. This error stems from a misunderstanding of the relationship between the univalence axiom and the axiom of choice.

Furthermore, some practitioners may incorrectly assume that HoTT is a simple extension of traditional type theory, neglecting the fundamental shift in perspective that HoTT introduces. HoTT views types as spaces and terms as points in these spaces, which leads to a new understanding of equality, composition, and other basic concepts. This shift requires a reevaluation of many traditional notions and techniques, and failure to recognize this can lead to incorrect applications of HoTT principles.

Lastly, a common error is to overlook the importance of coherence conditions in HoTT. Coherence conditions ensure that the higher-dimensional structure of types is well-behaved, which is essential for many constructions and proofs in HoTT. Neglecting these conditions can result in incorrect or incomplete arguments, highlighting the need for careful attention to the homotopical aspects of type theory.

## Advanced

Homotopy Type Theory (HoTT) has given rise to several advanced extensions and open questions, driving current research in the field. One key area is the study of Higher Inductive Types (HITs), which provide a framework for constructing higher-dimensional objects. The homotopy theory of HITs is an active area of research, with connections to algebraic topology and higher category theory. Another direction is the development of Cubical Type Theory, which provides an alternative to the traditional homotopy theory of HoTT. This approach has been shown to be equivalent to HoTT, but offers a more geometric and computational perspective. The study of Univalence Axiom and its consequences is also an active area, with implications for the foundations of mathematics and the nature of equality. Open questions include the construction of a homotopy theory of types, the development of a satisfactory theory of higher-dimensional modal logic, and the integration of HoTT with other areas of mathematics, such as algebraic geometry and differential geometry. Researchers are also exploring the potential applications of HoTT to other fields, including computer science, physics, and philosophy, driving the field forward and expanding its connections to other areas of mathematics and beyond.
