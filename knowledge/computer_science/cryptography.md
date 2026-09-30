---
key: cryptography
title: "Cryptography"
program: computer_science
course_level: 5
dna16: "0701201824672581"
l4_address: "S6:P1413809388"
chain256_anchor: "0210277058910809177918396999238101853538569323810060306717203455092291473667333201915477518823811148572068732381108519175087974218143814650175011744230441032381145457389552238112418866049048710675491899954226005510954374238112014345903923810615932685515168"
updated_at: "2026-09-07T05:16:23.818Z"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Cryptography

> The course assumes prior knowledge of computational hardness assumptions, complexity theory, and probability, and delves into specialized topics like symmetric-key and asymmetric-k

## Foundations

Cryptography is the discipline of securing communication and data through mathematical transformations, ensuring confidentiality, integrity, authenticity, and non-repudiation. At its core, cryptography relies on rigorous computational hardness assumptions—such as integer factorization or discrete logarithms—to construct primitives that resist adversarial inversion within feasible time. The foundational principles are:  
- **Confidentiality:** Prevent unauthorized data access.  
- **Integrity:** Detect unauthorized data modification.  
- **Authentication:** Verify identities and message origin.  
- **Non-repudiation:** Prevent denial of actions by entities.

Cryptographic systems are built upon formal models (e.g., IND-CPA, IND-CCA security), leveraging complexity theory and probability to define adversarial capabilities and security guarantees. The cryptographic landscape divides broadly into symmetric-key and asymmetric-key paradigms, each with distinct mathematical frameworks and operational modes.

In computer science, cryptography refers to the practice and study of techniques for secure communication by transforming plaintext, defined as intelligible data, into ciphertext, defined as unintelligible data. A cryptosystem, also known as a cipher system, consists of a set of algorithms used for encryption, defined as the process of converting plaintext into ciphertext, and decryption, defined as the process of converting ciphertext back into plaintext.

Key concepts include confidentiality, integrity, and authenticity. Confidentiality ensures that only authorized parties can access the data. Integrity ensures that the data is not modified during transmission. Authenticity ensures that the data originates from the claimed source.

A cryptographic protocol is a set of rules and procedures used to achieve secure communication. Symmetric-key cryptography uses the same secret key for both encryption and decryption, whereas asymmetric-key cryptography, also known as public-key cryptography, uses a pair of keys: a public key for encryption and a private key for decryption.

Cryptanalysis is the study of methods for obtaining the meaning of encrypted information without access to the decryption key, often involving attacks such as brute force, frequency analysis, and side-channel attacks. A cryptographic hash function is a one-way function that takes input data of any size and produces a fixed-size string of characters, known as a message digest, which can be used for data integrity and authenticity verification.

In computer science, cryptography refers to the practice and study of techniques for secure communication by transforming plaintext (readable data) into ciphertext (unreadable data) to protect it from unauthorized access. A **cryptosystem** is a computer system that employs cryptography, utilizing **algorithms** (well-defined procedures for computations) to ensure data confidentiality, integrity, and authenticity. **Encryption** is the process of converting plaintext into ciphertext using an **encryption algorithm** and a **key** (a secret parameter that determines the transformation). The reverse process, **decryption**, converts ciphertext back into plaintext using a **decryption algorithm** and the corresponding key. **Symmetric-key cryptography** uses the same key for both encryption and decryption, whereas **asymmetric-key cryptography** (or **public-key cryptography**) uses a pair of keys: a **public key** for encryption and a corresponding **private key** for decryption. **Cryptanalysis** is the study of methods for obtaining the plaintext from the ciphertext without access to the key, aiming to break the encryption. A **cryptographer** designs and develops cryptosystems, while a **cryptologist** studies both cryptography and cryptanalysis. Understanding these core definitions and principles is essential for a practitioner in the field of cryptography.

## Symmetric-Key Cryptography

Symmetric cryptography uses a shared secret key for both encryption and decryption. The canonical framework is the **Advanced Encryption Standard (AES)**, standardized by NIST in FIPS 197 (2001). AES operates on 128-bit blocks using substitution-permutation networks with key sizes of 128, 192, or 256 bits. The core AES round function includes:  
- **SubBytes:** Nonlinear byte substitution using an invertible S-box derived from multiplicative inverses in GF(2^8).  
- **ShiftRows:** Cyclically shifts rows to achieve diffusion.  
- **MixColumns:** Matrix multiplication over GF(2^8) for column mixing.  
- **AddRoundKey:** XOR with round key derived via Rijndael key schedule.

AES-256 uses 14 rounds, AES-192 12 rounds, and AES-128 10 rounds. Modes of operation (e.g., CBC, CTR, GCM) define how block ciphers secure variable-length data and provide additional security properties like integrity (GCM).

## Asymmetric-Key Cryptography

Public-key cryptography involves key pairs: a public key for encryption or signature verification, and a private key for decryption or signing. The RSA algorithm (Rivest-Shamir-Adleman, 1977) is seminal:  
- Key generation: Select large primes \( p, q \), compute \( n = pq \), \(\phi(n) = (p-1)(q-1)\).  
- Choose public exponent \( e \) (commonly 65537).  
- Compute private exponent \( d \equiv e^{-1} \mod \phi(n) \).  
Encryption: \( c = m^e \mod n \). Decryption: \( m = c^d \mod n \).  
Security depends on integer factorization hardness. RSA is often paired with padding schemes like OAEP (Optimal Asymmetric Encryption Padding) to achieve IND-CCA security.

Elliptic Curve Cryptography (ECC) uses algebraic groups of points on elliptic curves over finite fields. The Elliptic Curve Digital Signature Algorithm (ECDSA) and Elliptic Curve Diffie-Hellman (ECDH) are primary protocols. For example, NIST P-256 curve defined by:  
\[ y^2 = x^3 - 3x + b \quad \text{over } \mathbb{F}_p, p=2^{256} - 2^{224} + 2^{192} + 2^{96} - 1 \]  
ECDSA signature generation:  
- Select random \( k \in [1, n-1] \), compute \( R = kG \), \( r = R_x \mod n \).  
- Compute \( s = k^{-1}(h(m) + dr) \mod n \), where \( d \) is private key.  
Signature: \( (r,s) \). Verification involves elliptic curve point operations verifying congruences.

## Hash Functions And Message Authentication

Cryptographic hash functions map arbitrary-length inputs to fixed-length outputs, exhibiting preimage resistance, second-preimage resistance, and collision resistance. SHA-2 family (SHA-256, SHA-512) is widely used, employing Merkle-Damgård construction with 64 or 80 rounds of compression functions operating on 512-bit blocks. SHA-3 (Keccak) uses sponge construction with parameters \( r \) (rate) and \( c \) (capacity) to absorb and squeeze data.

Message Authentication Codes (MACs) provide integrity and authenticity. HMAC (Hash-based MAC) uses:  
\[ \text{HMAC}_K(m) = H((K \oplus opad) \| H((K \oplus ipad) \| m)) \]  
where \( K \) is the key, \( H \) the hash function, and \( opad, ipad \) fixed padding constants.

## Key Exchange Protocols

Key exchange enables secure symmetric key establishment over insecure channels. Diffie-Hellman (DH) protocol operates in cyclic groups \( G \) of prime order \( q \) with generator \( g \):  
- Alice selects \( a \in [1,q-1] \), sends \( A = g^a \).  
- Bob selects \( b \in [1,q-1] \), sends \( B = g^b \).  
- Shared secret: \( s = B^a = A^b = g^{ab} \).  
Elliptic Curve Diffie-Hellman (ECDH) applies the same principle on elliptic curve groups, offering equivalent security with smaller key sizes.

## Digital Signatures

Digital signatures provide non-repudiation and authenticity. RSA signatures use PKCS#1 v1.5 or PSS padding:  
- Signature \( s = m^d \mod n \) (with padding).  
ECDSA and EdDSA are elliptic curve-based schemes with deterministic or randomized nonce generation to prevent side-channel attacks. Ed25519 (EdDSA variant) uses Curve25519 and SHA-512, providing fast, secure signatures with deterministic nonce \( k = H(d \| m) \).

## Post-Quantum Cryptography

Emerging cryptosystems resist quantum adversaries. Lattice-based schemes like CRYSTALS-Kyber (encryption) and CRYSTALS-Dilithium (signatures) rely on hardness of Learning With Errors (LWE) problems. Kyber uses module lattices with parameters:  
- Modulus \( q = 3329 \), dimension \( n=256 \), security level ~128 bits.  
Key generation, encapsulation, and decapsulation involve polynomial arithmetic in rings \( \mathbb{Z}_q[x]/(x^n + 1) \).

## Mastery Levels

L1: Understand symmetric vs. asymmetric cryptography distinctions.  
L2: Implement AES-128 encryption in CBC mode with PKCS#7 padding.  
L3: Derive RSA keys and perform modular exponentiation for encryption/decryption.  
L4: Compute ECDSA signatures on NIST P-256 and verify them.  
L5: Analyze security proofs of IND-CCA2 for OAEP padding in RSA.  
L6: Design and analyze a secure key exchange protocol using ephemeral ECDH with forward secrecy.  
L7: Implement and optimize lattice-based Kyber encryption, understanding parameter trade-offs.  
L8: Formally prove security reductions in the random oracle model for combined signature and encryption schemes under quantum adversaries.

## Mechanisms

Cryptography relies on several key mechanisms to ensure secure data transmission. The process begins with plaintext, the original message to be encrypted. The plaintext is then fed into an encryption algorithm, which uses a secret key to transform the data into ciphertext, the encrypted message. This transformation is based on a series of complex mathematical operations, such as substitution and transposition, that alter the plaintext's digital representation. The encryption algorithm's security relies on the difficulty of reversing these operations without knowledge of the secret key. The ciphertext is then transmitted over an insecure channel, such as the internet. Upon receipt, the ciphertext is fed into a decryption algorithm, which uses the same secret key to reverse the encryption process, transforming the ciphertext back into plaintext. The decryption algorithm's ability to recover the original plaintext relies on the causal chain of encryption, where the decryption process is the inverse of the encryption process, allowing the original message to be recovered. This causal chain is based on the principle of reversibility, where the encryption and decryption processes are inverses of each other, ensuring that the original message can be recovered from the ciphertext. Symmetric-key cryptography uses the same secret key for both encryption and decryption, while asymmetric-key cryptography uses a pair of keys, one for encryption and another for decryption, providing an additional layer of security.

Cryptography relies on complex mathematical algorithms to secure data. The process begins with plaintext, the original message to be encrypted. This plaintext is then fed into an encryption algorithm, which uses a secret key to transform the data into ciphertext, the encrypted message. The encryption algorithm works by applying a series of substitutions and permutations to the plaintext, based on the secret key. The key determines the specific transformations applied, making it difficult for unauthorized parties to reverse the process without the key. The encrypted ciphertext is then transmitted or stored, and can only be decrypted by someone with access to the same secret key, using a corresponding decryption algorithm. This decryption algorithm reverses the transformations applied during encryption, restoring the original plaintext. The security of the system relies on the secrecy of the key and the computational infeasibility of reversing the encryption process without it. Symmetric-key cryptography uses the same key for both encryption and decryption, while asymmetric-key cryptography uses a pair of keys: a public key for encryption and a private key for decryption.

## Methods And Frameworks

In computer science, cryptography relies on various methods and frameworks to ensure secure data transmission and protection. The Advanced Encryption Standard (AES) is a widely used symmetric-key block cipher, suitable for bulk data encryption due to its high speed and low latency. The RSA algorithm, on the other hand, is an asymmetric-key algorithm commonly used for secure data transmission over the internet, particularly in SSL/TLS protocols. The Diffie-Hellman key exchange is a method for securely exchanging cryptographic keys over a public channel, often used in conjunction with other encryption algorithms. The Elliptic Curve Cryptography (ECC) framework provides a more efficient alternative to traditional public-key cryptosystems, offering similar security with smaller key sizes. Failure modes for these methods include side-channel attacks, such as timing and power analysis attacks, which can compromise the security of AES and other symmetric-key algorithms. Asymmetric-key algorithms like RSA are vulnerable to factorization attacks, while ECC is susceptible to invalid curve attacks. The choice of method and framework depends on the specific use case, considering factors such as data size, transmission speed, and computational resources.

Cryptography employs various methods and frameworks to ensure secure data transmission and storage. The Advanced Encryption Standard (AES) is a widely used symmetric-key block cipher, suitable for bulk data encryption due to its high speed and low latency. RSA is an asymmetric-key algorithm, often used for key exchange and digital signatures, where its high security and ease of implementation make it a popular choice. The Diffie-Hellman key exchange is a method for securely exchanging cryptographic keys over an insecure channel, commonly used in SSL/TLS protocols. 
The Elliptic Curve Cryptography (ECC) framework offers high security with smaller key sizes, making it suitable for resource-constrained devices. 
Failure modes include side-channel attacks, such as timing and power analysis attacks, which can compromise AES and other symmetric-key ciphers. Asymmetric-key algorithms like RSA are vulnerable to factorization attacks, while ECC is susceptible to invalid curve attacks. 
Key management is crucial, as poor key exchange and storage can lead to security breaches. 
Hybrid approaches, combining symmetric and asymmetric encryption, can provide a balance between security and performance. 
Cryptographic hash functions, such as SHA-256, are used for data integrity and authenticity verification, but are vulnerable to collision attacks. 
Understanding the strengths and weaknesses of each method and framework is essential for selecting the appropriate cryptographic technique for a given application.

## Worked Examples

To illustrate the application of cryptographic principles, consider the following examples.

1. **Encryption using Caesar Cipher**: Suppose we want to encrypt the message "HELLO" using a Caesar Cipher with a shift of 3. We replace each letter with the letter 3 positions ahead of it in the alphabet. Thus, "H" becomes "K", "E" becomes "H", "L" becomes "O", "L" becomes "O", and "O" becomes "R". The encrypted message is "KHOOR".

2. **Decrypting using RSA**: Given a public key (e, n) = (17, 323), and a ciphertext c = 279, to decrypt it, we first need the private key (d, n). Assuming we have the private key (d, n) = (275, 323), we can decrypt c using the formula m = c^d mod n. Calculating 279^275 mod 323 gives us the original message m.

3. **Hash Function Collision**: Suppose we have a hash function H(x) that produces a 4-bit output. If we input two different messages, "ABC" and "DEF", and both produce the same hash output, say "1010", this is a collision. In practice, a good hash function should minimize collisions. For instance, if H("ABC") = H("DEF") = 1010, we need to re-evaluate our choice of hash function to ensure data integrity.

1. **Encryption using Caesar Cipher**: Suppose we want to encrypt the message "HELLO" using a Caesar Cipher with a shift of 3. The encryption process involves shifting each letter 3 positions forward in the alphabet. Thus, "H" becomes "K", "E" becomes "H", "L" becomes "O", "L" becomes "O", and "O" becomes "R". The encrypted message is "KHOOR".

2. **Decryption using RSA**: Given a public key (e, n) = (17, 323), and a ciphertext c = 279, to decrypt the message, we first need the private key (d, n). Assuming we have the private key (d, n) = (275, 323), we can decrypt the message using the formula m = c^d mod n. Calculating this gives m = 279^275 mod 323 = 88. The decrypted message is the number 88, which corresponds to the character represented by the ASCII value 88, which is "X".

3. **Hash Function Collision**: Suppose we have two different input messages, "ABC" and "DEF", and we apply a hash function (such as SHA-256) to both. The hash values for "ABC" and "DEF" are distinct, for example, "ABC" might hash to "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad" and "DEF" might hash to "2d2a2d2a2d2a2d2a2d2a2d2a2d2a". A collision occurs when two different inputs produce the same output hash value. However, due to the large output space of SHA-256 (2^256), the probability of a collision occurring naturally is extremely low, making it suitable for data integrity applications.

## Applications

Cryptography has numerous applications in computer science, particularly in secure communication, data protection, and authentication. In practice, cryptographic techniques are used to protect online transactions, such as online banking and e-commerce, by encrypting sensitive data like credit card numbers and personal identifiable information. Secure Sockets Layer/Transport Layer Security (SSL/TLS) protocols, which utilize public-key cryptography, are widely used to establish secure connections between web browsers and servers.

In the domain of cloud computing, cryptography is used to ensure the confidentiality, integrity, and availability of data stored in cloud storage services. Homomorphic encryption, for instance, enables computations to be performed on encrypted data without decrypting it first, thereby maintaining data privacy.

Digital signatures, a type of asymmetric cryptography, are used to authenticate the sender of a message and ensure the integrity of the message itself. This is particularly important in software distribution, where digital signatures verify the authenticity of software updates and prevent tampering.

Cryptography is also essential in virtual private networks (VPNs), which use encryption to secure internet traffic between a user's device and a VPN server, thereby protecting against eavesdropping and interception. Additionally, cryptographic hash functions are used in password storage and verification, allowing passwords to be stored securely without revealing the actual password.

In the field of cybersecurity, cryptography is used to develop secure protocols for secure communication, such as IPsec and PGP, which provide encryption, authentication, and integrity checking for data transmitted over the internet. Overall, cryptography plays a vital role in protecting sensitive information and ensuring the security and trustworthiness of computer systems and networks.

Cryptography has numerous applications in computer science, particularly in secure communication, data protection, and authentication. In practice, cryptographic techniques are used to protect online transactions, such as online banking and e-commerce, by encrypting sensitive data like credit card numbers and personal identifiable information. Secure Sockets Layer/Transport Layer Security (SSL/TLS) protocols, which utilize public-key cryptography, are widely used to establish secure connections between web browsers and servers. Digital signatures, based on asymmetric cryptography, are used to authenticate the sender of a message and ensure the integrity of the message. Cryptography is also used in virtual private networks (VPNs) to secure data transmission between remote locations. Additionally, cryptographic hash functions are used in password storage and data integrity verification. In cloud computing, cryptography is used to protect data at rest and in transit, ensuring the confidentiality and integrity of data stored in cloud storage services. Furthermore, cryptographic techniques like homomorphic encryption and secure multi-party computation enable secure computation on private data, allowing for secure data analysis and processing without compromising data privacy.

## Common Errors

In cryptography, common errors often stem from misunderstandings of cryptographic principles or incorrect implementations. One mistake is using insufficiently secure key sizes, such as using 512-bit or 1024-bit RSA keys, which can be factored by modern computers, compromising the security of the system. Another error is the incorrect use of encryption modes, such as using Electronic Codebook (ECB) mode for encrypting large amounts of data, which can lead to information leakage due to its deterministic nature. 
Practitioners also often make mistakes in implementing secure random number generation, which is crucial for generating keys and nonces. Using predictable or weak random numbers can compromise the security of the entire system. Additionally, errors in key management, such as hardcoding keys or using insecure key storage, can also lead to security breaches. 
Furthermore, neglecting to implement authentication mechanisms, such as digital signatures or message authentication codes (MACs), can make encrypted data vulnerable to tampering and forgery attacks. Implementing cryptographic protocols without considering side-channel attacks, such as timing or power analysis attacks, can also lead to security vulnerabilities. 
These errors highlight the importance of careful consideration of cryptographic principles and best practices in the design and implementation of secure systems. By understanding these common mistakes, practitioners can avoid them and ensure the security and integrity of their systems.

In cryptography, practitioners often make mistakes that can compromise the security of their systems. One common error is using insufficiently secure random number generators, which can lead to predictable keys and compromised encryption. Another mistake is using outdated or broken encryption algorithms, such as MD5 or SHA-1, which are vulnerable to collisions and other attacks. Additionally, many practitioners fail to properly implement secure key exchange protocols, such as Diffie-Hellman or RSA, which can lead to man-in-the-middle attacks. 
Incorrect usage of modes of operation, such as using ECB mode for encrypting large amounts of data, can also lead to security vulnerabilities. Furthermore, neglecting to regularly update and patch cryptographic software and libraries can expose systems to known vulnerabilities. 
Practitioners may also make mistakes in key management, such as using hardcoded or default keys, or failing to properly rotate and revoke keys. These errors can be attributed to a lack of understanding of cryptographic principles, insufficient testing and validation, and inadequate security protocols. 
It is essential for practitioners to stay up-to-date with the latest cryptographic techniques and best practices to avoid these common errors and ensure the security of their systems.

## Advanced

In advanced cryptography, researchers explore extensions of classical cryptographic techniques, such as homomorphic encryption, which enables computations on encrypted data without decrypting it first. Zero-knowledge proofs, a fundamental concept in cryptography, allow one party to prove the validity of a statement without revealing any underlying information. Graduate-level studies also delve into the realm of quantum cryptography, where the principles of quantum mechanics are leveraged to create unbreakable encryption methods, such as quantum key distribution. Open questions in the field include the development of secure multi-party computation protocols, which enable multiple parties to jointly perform computations on private data without revealing their individual inputs. The field is moving towards the development of more efficient and secure cryptographic protocols, such as lattice-based cryptography and code-based cryptography, which are resistant to quantum computer attacks. Additionally, the study of side-channel attacks and countermeasures is an active area of research, as these attacks can compromise the security of even the most theoretically secure cryptographic systems. The intersection of cryptography with other areas of computer science, such as machine learning and artificial intelligence, is also being explored, with applications in secure data sharing and privacy-preserving data analysis.

In advanced cryptography, researchers explore extensions of classical cryptographic techniques, such as homomorphic encryption, which enables computations on encrypted data without decrypting it first. Zero-knowledge proofs, a fundamental concept in cryptographic protocols, allow one party to prove the validity of a statement without revealing any underlying information. Lattice-based cryptography and code-based cryptography are being investigated as potential replacements for traditional public-key cryptosystems, which are vulnerable to quantum computer attacks. Quantum cryptography, on the other hand, leverages the principles of quantum mechanics to provide theoretically unbreakable encryption. Open questions in the field include the development of secure multi-party computation protocols, the construction of efficient and secure digital signatures, and the study of side-channel attacks, which exploit information about the implementation of a cryptographic system to compromise its security. The field is moving towards the development of more efficient and scalable cryptographic protocols, such as oblivious transfer and secure function evaluation, which are essential for enabling secure computation on distributed data. Furthermore, the increasing use of machine learning and artificial intelligence in cryptography is raising new questions about the security and privacy of cryptographic systems, and the potential for adversarial attacks on these systems.
