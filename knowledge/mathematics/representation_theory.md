---
key: representation_theory
title: "Representation Theory"
program: mathematics
course_level: 5
dna16: ""
l4_address: "S6:P738779287"
chain256_anchor: "1241381941104545175027223973591301101870952959130603594672841494153921688636486312318392928859130993998774235913026495538416780900638811444497420682364598945913063394153012591315468766017473710675339316781261096478991889591302024913797859130989252833178829"
updated_at: "2026-09-07T11:03:59.136Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Representation Theory

> The course assumes prior knowledge of abstract algebra and linear algebra, and delves into specialized topics like character theory and highest weight theory.

## Foundations

Representation theory studies abstract algebraic structures by representing their elements as linear transformations of vector spaces, thereby translating algebraic problems into linear algebraic ones. At its core, a *representation* of a group \( G \) over a field \( K \) is a homomorphism \(\rho: G \to \mathrm{GL}(V)\), where \( V \) is a finite-dimensional \( K \)-vector space and \(\mathrm{GL}(V)\) its group of invertible linear operators. This framework extends naturally to associative algebras, Lie algebras, and other algebraic objects. The fundamental principle is that understanding the module category of these objects reveals their structure, symmetry, and invariants. Key foundational results include Maschke’s theorem (complete reducibility of finite group representations over fields of characteristic zero or not dividing \(|G|\)), Schur's lemma (endomorphisms of simple modules are scalars), and the correspondence between irreducible representations and simple modules.

Representation theory is a branch of mathematics that studies the ways in which a group can act on a vector space. A **group**, denoted as G, is a set of elements with a binary operation (often called multiplication) that satisfies four properties: **closure**, meaning the result of combining any two elements is also an element in the group; **associativity**, meaning the order in which elements are combined does not change the result; **identity**, meaning there exists an element that does not change the result when combined with any other element; and **invertibility**, meaning each element has an inverse that, when combined, gives the identity element.

A **representation** of a group G is a pair (V, ρ), where V is a vector space over a field F, and ρ is a **homomorphism** from G to the general linear group GL(V) of invertible linear transformations from V to itself. This means ρ assigns to each element g in G a linear transformation ρ(g) in GL(V) such that ρ(g₁g₂) = ρ(g₁)ρ(g₂) for all g₁, g₂ in G. The vector space V is called the **representation space**, and the dimension of V is called the **dimension** of the representation.

A **subrepresentation** is a subspace W of V that is invariant under the action of G, meaning ρ(g)(W) ⊆ W for all g in G. A representation is **irreducible** if its only subrepresentations are the zero subspace and the representation space itself. The **direct sum** of representations (V₁, ρ₁) and (V₂, ρ₂) is the representation (V₁ ⊕ V₂, ρ₁ ⊕ ρ₂), where (ρ₁ ⊕ ρ₂)(g)(v₁, v₂) = (ρ₁(g)v₁, ρ₂(g)v₂) for all g in G, v₁ in V₁, and v₂ in V₂.

Representation theory is a branch of mathematics that studies the ways in which a group can act on a vector space. A **group**, denoted as G, is a set of elements with a binary operation (often called multiplication) that satisfies four properties: **closure**, **associativity**, **identity**, and **invertibility**. A **vector space**, denoted as V, is a set of vectors with two operations: addition and scalar multiplication, satisfying certain axioms such as **commutativity**, **associativity**, and **distributivity**. A **representation** of a group G on a vector space V is a **homomorphism** from G to the general linear group GL(V) of invertible linear transformations from V to itself. This homomorphism, denoted as ρ, assigns to each element g in G a linear transformation ρ(g) in GL(V), such that ρ(g₁g₂) = ρ(g₁)ρ(g₂) for all g₁, g₂ in G. The **degree** of a representation is the dimension of the vector space V. A **subrepresentation** is a subspace of V that is invariant under the action of G. A representation is **irreducible** if it has no non-trivial subrepresentations. The **kernel** of a representation ρ is the set of elements g in G such that ρ(g) is the identity transformation.

## Section

Maschke’s Theorem and Complete Reducibility  
Maschke’s theorem states that if \( G \) is a finite group and \( K \) a field with \(\mathrm{char}(K) \nmid |G|\), then every finite-dimensional \( K \)-representation of \( G \) is completely reducible. Explicitly, given a subrepresentation \( W \subseteq V \), there exists a complementary \( G \)-invariant subspace \( U \) such that \( V = W \oplus U \). The proof uses the averaging operator: for a projection \( P: V \to W \), define  
\[
P_G = \frac{1}{|G|} \sum_{g \in G} \rho(g) P \rho(g)^{-1},
\]  
which is a \( G \)-equivariant projection onto \( W \). This result underpins the decomposition of group algebras into simple components and the classification of irreducible representations.

Character Theory and Orthogonality Relations  
For finite groups over \(\mathbb{C}\), the character \(\chi_\rho(g) = \mathrm{tr}(\rho(g))\) encodes representation data. The set of irreducible characters \(\{\chi_i\}\) forms an orthonormal basis of class functions with respect to the inner product  
\[
\langle \chi, \psi \rangle = \frac{1}{|G|} \sum_{g \in G} \chi(g) \overline{\psi(g)}.
\]  
Orthogonality relations:  
\[
\langle \chi_i, \chi_j \rangle = \delta_{ij}, \quad \sum_i \chi_i(g) \overline{\chi_i(h)} = \frac{|G|}{|C_G(g)|} \delta_{g \sim h},
\]  
where \(C_G(g)\) is the centralizer of \(g\) and \(\delta_{g \sim h}\) is 1 if \(g\) and \(h\) are conjugate, 0 otherwise. Characters classify irreducibles and facilitate decomposition of arbitrary representations.

Highest Weight Theory for Semisimple Lie Algebras  
For a semisimple Lie algebra \(\mathfrak{g}\) over \(\mathbb{C}\), irreducible finite-dimensional representations correspond bijectively to dominant integral weights. The Cartan subalgebra \(\mathfrak{h}\) decomposes \(\mathfrak{g}\) into root spaces \(\mathfrak{g}_\alpha\). Given a fixed positive root system \(\Delta^+\), the highest weight \(\lambda \in \mathfrak{h}^*\) satisfies \(\lambda + \alpha \notin \mathrm{wt}(V)\) for all \(\alpha \in \Delta^+\). The Verma module \(M(\lambda)\) is induced from the Borel subalgebra \(\mathfrak{b} = \mathfrak{h} \oplus \mathfrak{n}_+\), and its unique simple quotient \(L(\lambda)\) realizes the irreducible representation. Weyl’s character formula gives the character of \(L(\lambda)\):  
\[
\mathrm{ch}\,L(\lambda) = \frac{\sum_{w \in W} \epsilon(w) e^{w(\lambda + \rho)}}{\prod_{\alpha \in \Delta^+} (e^{\alpha/2} - e^{-\alpha/2})},
\]  
where \(W\) is the Weyl group, \(\epsilon(w)\) its sign, and \(\rho\) the half-sum of positive roots.

Modular Representation Theory and Blocks  
When the characteristic \(p\) of the field divides \(|G|\), Maschke’s theorem fails, and representations are not semisimple. The group algebra \(kG\) decomposes into *blocks*, indecomposable two-sided ideals corresponding to primitive central idempotents. Each block contains a subset of irreducible modules and governs extension groups \(\mathrm{Ext}^1\). The theory of *defect groups* and *Brauer correspondences* relates blocks to \(p\)-subgroups of \(G\). Tools include Green correspondence and the use of projective covers. The complexity of modular representations is encoded in the *Auslander–Reiten* quiver of the block.

Induced Representations and Frobenius Reciprocity  
Given a subgroup \(H \leq G\) and a representation \(\sigma: H \to \mathrm{GL}(W)\), the induced representation \(\mathrm{Ind}_H^G \sigma\) acts on  
\[
V = \{ f: G \to W \mid f(hg) = \sigma(h) f(g), \forall h \in H, g \in G \},
\]  
with \(G\) acting by right translation. Frobenius reciprocity states:  
\[
\mathrm{Hom}_G(\mathrm{Ind}_H^G \sigma, \rho) \cong \mathrm{Hom}_H(\sigma, \mathrm{Res}_H^G \rho).
\]  
This powerful adjunction allows transfer of representation-theoretic problems between groups and subgroups, crucial in Mackey theory and character induction.

Tannakian Reconstruction and Tensor Categories  
Tannakian formalism reconstructs a group (or group scheme) from its category of representations equipped with a fiber functor to vector spaces. A neutral Tannakian category \(\mathcal{C}\) over \(K\) is a rigid abelian tensor category with an exact faithful \(K\)-linear tensor functor \(\omega: \mathcal{C} \to \mathrm{Vect}_K\). By Deligne’s theorem, \(\mathcal{C} \cong \mathrm{Rep}_K(G)\) for an affine group scheme \(G\). This categorical viewpoint generalizes classical representation theory to quantum groups, supergroups, and motivic Galois groups.

Langlands Correspondence and Automorphic Representations  
Representation theory of reductive groups over local and global fields underlies the Langlands program. Smooth admissible representations of \(p\)-adic groups \(G(F)\) correspond to Langlands parameters: homomorphisms from the Weil–Deligne group \(W_F'\) into the Langlands dual group \(^L G\). The local Langlands correspondence classifies irreducible admissible representations via these parameters. Globally, automorphic representations decompose \(L^2(G(\mathbb{Q}) \backslash G(\mathbb{A}))\) into irreducibles, connecting harmonic analysis, number theory, and arithmetic geometry.

## Mastery Levels

L1: Understand the definition of a group representation as a homomorphism into \(\mathrm{GL}(V)\).  
L2: Apply Maschke’s theorem to decompose finite group representations over \(\mathbb{C}\).  
L3: Compute characters and use orthogonality relations to identify irreducibles.  
L4: Construct Verma modules and identify highest weight modules for \(\mathfrak{sl}_2(\mathbb{C})\).  
L5: Analyze blocks and projective modules in modular representation theory for \(p\)-groups.  
L6: Use Frobenius reciprocity to induce and restrict representations between subgroups.  
L7: Employ Tannakian duality to reconstruct affine group schemes from tensor categories.  
L8: Classify admissible representations of reductive \(p\)-adic groups via the local Langlands correspondence.

## Mechanisms

Representation theory is a branch of mathematics that studies the ways in which a group can act on a vector space, providing a framework for understanding the symmetries of an object. The mechanism of representation theory works as follows: 
1. A group G is given, consisting of a set of elements with a binary operation that satisfies certain properties (closure, associativity, identity, and invertibility). 
2. A vector space V is chosen, over a field F, with the standard operations of vector addition and scalar multiplication. 
3. A representation of G on V is a homomorphism ρ: G → GL(V), where GL(V) is the general linear group of V, consisting of all invertible linear transformations from V to itself. 
4. The representation ρ assigns to each element g in G a linear transformation ρ(g) in GL(V), such that the group operation in G is preserved: ρ(g₁g₂) = ρ(g₁) ∘ ρ(g₂) for all g₁, g₂ in G. 
5. The vector space V is then said to be a G-module, with the action of G on V defined by the representation ρ. 
6. The study of the representation ρ, including its properties and behavior, provides insight into the structure of the group G and its action on the vector space V. 
7. Decomposing the representation into irreducible components, which are representations that cannot be further decomposed, allows for a more detailed understanding of the group's action and the symmetries of the object being studied. 
This mechanism enables the application of representation theory to various areas of mathematics, such as algebra, geometry, and analysis, providing a powerful tool for understanding and analyzing symmetries and group actions.

Representation theory is a branch of mathematics that studies the ways in which a group can act on a vector space, providing a framework for understanding the symmetries of an object. The mechanism of representation theory works as follows: 
1. A group G is given, which is a set of elements with a binary operation (such as multiplication or addition) that satisfies certain properties (closure, associativity, identity, and invertibility).
2. A vector space V is chosen, over a field F (such as the real or complex numbers), which is a set of vectors with operations of addition and scalar multiplication.
3. A representation of G on V is a homomorphism ρ from G to the general linear group GL(V) of invertible linear transformations from V to itself. This means that for each element g in G, ρ(g) is a linear transformation from V to V, and the mapping ρ preserves the group operation.
4. The representation ρ induces a group action of G on V, where each element g in G acts on a vector v in V by applying the linear transformation ρ(g) to v.
5. The vector space V can be decomposed into irreducible subspaces, which are subspaces that cannot be further decomposed into smaller invariant subspaces under the action of G.
6. The irreducible subspaces are the building blocks of the representation, and they can be used to classify the representations of G.
7. The character of a representation ρ is a function that assigns to each element g in G the trace of the linear transformation ρ(g). The character is a powerful tool for studying representations, as it encodes information about the representation and can be used to distinguish between different representations.
8. The orthogonality relations for characters provide a way to decompose a representation into its irreducible components and to compute the multiplicity of each irreducible component.
9. The representation theory of G can be used to study the symmetries of an object, such as a molecule or a crystal, by associating the object with a group G of symmetries and a vector space V of states or configurations.
10. The representation theory of G provides a framework for understanding the structure and properties of the object, such as its energy levels, vibrational modes, and other physical properties.

## Methods And Frameworks

In representation theory, several methods and frameworks are employed to study the representations of algebraic structures such as groups, Lie algebras, and associative algebras. The character theory method is used to study the representations of finite groups, where the character of a representation is a function that encodes information about the representation. This method is particularly useful when the group is finite and the representation is finite-dimensional. However, it can be computationally intensive and may not provide a complete understanding of the representation.

The Frobenius reciprocity formula is a fundamental tool in representation theory, relating the representations of a group and its subgroups. It is used to induce and restrict representations, and is essential in understanding the relationships between representations of different groups. However, it requires a good understanding of the group and its subgroups, and can be difficult to apply in practice.

The Peter-Weyl theorem provides a framework for studying the representations of compact groups, where it states that every irreducible representation of a compact group is finite-dimensional and can be embedded into the regular representation. This theorem is useful when studying the representations of compact Lie groups, but may not be applicable to non-compact groups.

The Mackey theory is a framework for studying the representations of locally compact groups, where it provides a way to induce and restrict representations. This theory is useful when studying the representations of infinite groups, but can be technically demanding and requires a good understanding of measure theory and functional analysis.

The failure mode of these methods and frameworks often arises from the complexity of the algebraic structures being studied, or the lack of information about the representations. For example, the character theory method may not be able to distinguish between non-isomorphic representations, while the Frobenius reciprocity formula may not provide a clear understanding of the relationships between representations. Additionally, the Peter-Weyl theorem and Mackey theory may not be applicable to all types of groups, and may require additional assumptions or technical conditions.

In representation theory, several methods and frameworks are employed to study the representations of algebraic structures such as groups, rings, and Lie algebras. The character theory method is used to study the representations of finite groups, where the character of a representation is a function that encodes information about the representation. This method is particularly useful when the group is finite and the representation is finite-dimensional. However, it can be computationally intensive and may not provide a complete picture of the representation.

The Frobenius reciprocity formula is a fundamental tool in representation theory, which describes the relationship between the representations of a group and its subgroups. It is used to induce representations from a subgroup to the entire group and to restrict representations from the group to a subgroup. This formula is essential in understanding the representation theory of finite groups and is a crucial component of the character theory method.

The Mackey theory framework is used to study the representations of locally compact groups, which are groups that have a topology and are "locally compact". This framework provides a way to decompose the representation of a group into irreducible components and is particularly useful in understanding the representation theory of infinite groups.

The Peter-Weyl theorem is a fundamental result in representation theory, which describes the representation theory of compact groups. It states that any representation of a compact group can be decomposed into a direct sum of irreducible representations, and provides a way to classify the irreducible representations of a compact group. However, this theorem only applies to compact groups and may not be applicable to non-compact groups.

The failure mode of these methods and frameworks often occurs when the algebraic structure is too complex or when the representation is infinite-dimensional. In such cases, the character theory method may not be computationally feasible, the Frobenius reciprocity formula may not provide a complete picture of the representation, and the Mackey theory framework may not be applicable. Additionally, the Peter-Weyl theorem may not be applicable to non-compact groups, and alternative methods such as the theory of unitary representations may be required.

## Worked Examples

To illustrate the principles of representation theory, consider the following examples. 
1. Let G be the cyclic group of order 3, and let V be a 2-dimensional vector space over the complex numbers. Suppose we have a representation ρ: G → GL(V) given by ρ(g) = [[1, 0], [0, 1]] and ρ(g^2) = [[ω, 0], [0, ω^2]], where ω is a primitive cube root of unity and g is a generator of G. To find the character of this representation, we compute the trace of ρ(g) and ρ(g^2), which are 2 and ω + ω^2 = -1, respectively. 
2. Consider the symmetric group S3 and the representation given by the permutation matrices of the elements of S3. For example, if σ = (12), then ρ(σ) = [[0, 1, 0], [1, 0, 0], [0, 0, 1]]. The character of this representation can be computed by finding the trace of the matrices corresponding to each conjugacy class of S3. 
3. Let G be the dihedral group of order 6, and let V be a 2-dimensional vector space over the real numbers. Suppose we have a representation ρ: G → GL(V) given by ρ(r) = [[0, -1], [1, 0]] and ρ(s) = [[1, 0], [0, -1]], where r is a rotation by 60 degrees and s is a reflection. To find the invariant subspaces of this representation, we need to find the subspaces of V that are fixed by ρ(G).

To illustrate the principles of representation theory, consider the following examples. 
Let's start with a simple example of a group representation. Suppose we have a group G = {e, g} of order 2, where e is the identity element and g is the non-identity element. A representation of G is a homomorphism ρ: G → GL(V), where V is a vector space. For instance, consider a 1-dimensional vector space V = ℝ. We can define a representation ρ: G → GL(ℝ) by ρ(e) = 1 and ρ(g) = -1. This representation is a group homomorphism because ρ(e) = 1, ρ(g) = -1, and ρ(gg) = ρ(e) = 1 = (-1)(-1) = ρ(g)ρ(g).

Next, consider the symmetric group S₃, which consists of all permutations of 3 elements. One representation of S₃ is the standard representation, where each permutation is represented by a 3x3 permutation matrix. For example, the permutation (12) can be represented by the matrix [[0, 1, 0], [1, 0, 0], [0, 0, 1]]. The character of this representation can be computed by taking the trace of each permutation matrix.

Lastly, consider the group G = ℤ₃, the cyclic group of order 3. A representation of G is a homomorphism ρ: G → GL(V). Suppose V = ℂ, the complex numbers. We can define a representation ρ: G → GL(ℂ) by ρ(0) = 1, ρ(1) = ω, and ρ(2) = ω², where ω is a primitive cube root of unity. This is a valid representation because ρ(0) = 1, ρ(1) = ω, ρ(2) = ω², and ρ(1+2) = ρ(0) = 1 = ωω² = ρ(1)ρ(2).

## Applications

Representation theory has numerous applications in various fields of mathematics and physics. In physics, it is used to describe the symmetries of physical systems, such as the rotation group SO(3) and the Lorentz group. The representations of these groups are used to classify the energy levels and transition probabilities of quantum mechanical systems. For example, the representation theory of the symmetric group Sn is used to describe the spectra of atoms and molecules. In number theory, representation theory is used to study the properties of L-functions and the distribution of prime numbers. The Langlands program, a central problem in number theory, relies heavily on representation theory to establish a connection between Galois representations and automorphic forms. In algebraic geometry, representation theory is used to study the cohomology of algebraic varieties and the geometry of moduli spaces. The geometric invariant theory, developed by David Mumford, uses representation theory to construct moduli spaces of algebraic curves and other geometric objects. Additionally, representation theory has applications in computer science, particularly in the study of algorithms for solving systems of linear equations and computing the discrete Fourier transform. The representation theory of finite groups is used to construct efficient algorithms for solving these problems.

## Common Errors

In representation theory, a common mistake is confusing the representation of a group with the group itself. This error arises from failing to distinguish between the abstract group and its concrete realization as a group of linear transformations. For instance, considering the group SL(2,ℝ) of 2x2 matrices with determinant 1, a representation of this group is a homomorphism from SL(2,ℝ) to GL(n,ℝ) for some n, not the group SL(2,ℝ) itself. Another error is neglecting to verify that a given representation is indeed a homomorphism, i.e., that it preserves the group operation. This can lead to incorrect conclusions about the properties of the representation, such as its irreducibility or decomposability. Furthermore, when working with induced representations, practitioners often forget to check that the subgroup is closed under conjugation, which is a necessary condition for the induction procedure to be well-defined. Additionally, mistakes can occur when computing character tables, such as incorrectly applying the orthogonality relations or misidentifying the conjugacy classes of the group. These errors can be avoided by carefully applying the definitions and theorems of representation theory, and by verifying each step of the computation.

In representation theory, a common mistake is confusing the character of a representation with the representation itself. The character of a representation is a function that encodes information about the representation, but it is not the representation. Specifically, the character of a representation ρ of a group G is a function χρ: G → ℂ, defined as the trace of the matrix ρ(g) for each g in G. Many properties of the representation can be deduced from its character, but they are not the same object. 
Another error is assuming that all representations of a group are completely reducible. While this is true for finite groups over fields of characteristic zero, such as the field of complex numbers, it is not true in general. For infinite groups or fields of positive characteristic, a representation may not be completely reducible, meaning it cannot be expressed as a direct sum of irreducible representations. 
Additionally, practitioners may mistakenly assume that the irreducible representations of a group can be easily found. However, determining the irreducible representations of a group can be a difficult task, especially for large or complex groups. This often requires advanced techniques, such as the use of the Peter-Weyl theorem or the theory of induced representations. 
Lastly, a common mistake is neglecting to consider the base field when studying representations. The properties of a representation can depend heavily on the base field, and results that hold over one field may not hold over another. For example, a representation may be irreducible over the field of real numbers but reducible over the field of complex numbers.

## Advanced

Representation theory has several advanced extensions that are currently being explored at the graduate level. One key area is the study of representations of infinite-dimensional algebras, such as affine Lie algebras and vertex operator algebras. These representations have connections to conformal field theory, string theory, and the geometric Langlands program. Another area of research is the development of categorification, which seeks to elevate representation-theoretic constructions to the level of categories and higher categories. This has led to new insights into the structure of representation categories and the development of new invariants, such as Khovanov homology. The field is also moving towards a deeper understanding of the representation theory of non-reductive groups, such as the Lorentz group and other non-compact Lie groups. Open questions include the development of a satisfactory representation theory for these groups and the resolution of the Kazhdan-Lusztig conjecture, which relates the representation theory of reductive groups to the geometry of flag varieties. Additionally, researchers are exploring the connections between representation theory and other areas of mathematics, such as number theory, algebraic geometry, and topology, through the use of tools like the Langlands program and the geometric representation theory of D-modules.

Representation theory has several advanced extensions that are currently being explored at the graduate level. One such area is the study of representations of infinite-dimensional algebras, such as affine Lie algebras and vertex operator algebras. These representations have connections to conformal field theory, string theory, and the geometric Langlands program. Another area of research is the development of categorification, which seeks to elevate representation-theoretic constructions to the level of categories and higher categories. This has led to new insights into the representation theory of quantum groups, Hecke algebras, and other objects. The field is also moving towards a deeper understanding of the representation theory of reductive groups over local fields, with applications to number theory and the Langlands program. Open questions include the resolution of the Kazhdan-Lusztig conjecture for affine Lie algebras and the development of a comprehensive theory of representations of wild quivers. Researchers are also exploring the connections between representation theory and other areas of mathematics, such as topology, geometry, and combinatorics, with potential applications to physics and computer science. The study of representations of algebraic objects, such as Hopf algebras and operads, is also an active area of research, with implications for the study of symmetries and invariants in mathematics and physics.
