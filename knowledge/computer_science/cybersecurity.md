---
key: cybersecurity
title: "Cybersecurity"
program: computer_science
course_level: 3
dna16: "0701201811064643"
l4_address: "S6:P2134155929"
chain256_anchor: "1330984475685543012317877220135805822442776613580878469868194049171887315153343114006722190713581081911451481358042622668713661711437088394904280489183740131358167508495393135814656734510786821578913754539781037936336354135804950158562813581741094018934123"
updated_at: "2026-09-07T13:26:13.580Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Cybersecurity

> The course assumes foundational knowledge and applies cybersecurity principles to real situations using standard tools and frameworks.

## Foundations

Cybersecurity is the discipline and practice of protecting information systems, networks, and data from unauthorized access, disruption, modification, or destruction. At its core, cybersecurity rests on the triad of Confidentiality, Integrity, and Availability (CIA). Confidentiality ensures information is accessible only to authorized entities; Integrity guarantees accuracy and trustworthiness of data; Availability ensures timely and reliable access to information and resources. First principles include threat modeling, risk assessment, defense-in-depth, least privilege, and fail-safe defaults. Cybersecurity integrates cryptography, system hardening, network security, identity and access management (IAM), incident response, and governance to create resilient digital ecosystems.

In computer science, cybersecurity refers to the practice of protecting digital information, computer systems, and networks from unauthorized access, use, disclosure, disruption, modification, or destruction. This is achieved through a combination of technical, administrative, and physical controls. A **threat** is a potential occurrence that could compromise security, while a **vulnerability** is a weakness in a system that can be exploited by a threat. **Risk** is the likelihood that a threat will occur and the potential impact if it does. A **asset** is any resource, such as data, hardware, or software, that needs to be protected. **Confidentiality**, **integrity**, and **availability** (CIA) are the three primary goals of cybersecurity: protecting sensitive information from unauthorized access (confidentiality), ensuring that data is not modified without authorization (integrity), and ensuring that data and systems are accessible when needed (availability). **Authentication** is the process of verifying the identity of users, devices, or systems, while **authorization** is the process of determining what actions an authenticated entity can perform. Understanding these core definitions and principles is essential for a cybersecurity practitioner to develop effective security strategies and mitigate potential risks.

In computer science, cybersecurity refers to the practice of protecting digital information, computer systems, and networks from unauthorized access, use, disclosure, disruption, modification, or destruction. This is achieved through a combination of technical, administrative, and physical controls. A **threat** is a potential occurrence that could compromise security, while a **vulnerability** is a weakness in a system that can be exploited by a threat. **Risk** is the likelihood that a threat will occur and the potential impact if it does. A **countermeasure** is a control or safeguard implemented to mitigate or prevent a threat. 
Key concepts include **confidentiality**, **integrity**, and **availability** (CIA), which are the fundamental principles of information security. **Confidentiality** refers to protecting sensitive information from unauthorized access. **Integrity** ensures that data is accurate, complete, and not modified without authorization. **Availability** ensures that data and systems are accessible and usable when needed. 
Understanding these core definitions and principles is essential for a cybersecurity practitioner to develop effective strategies for protecting computer systems and networks from various types of **malicious software** (malware), such as **viruses**, **worms**, and **trojans**, as well as other cyber threats.

## Section

RISK MANAGEMENT FRAMEWORK (RMF)  
Developed by NIST (SP 800-37), RMF is a structured process to integrate security and risk management into the system lifecycle. It comprises six steps:  
1. **Categorize Information System** (FIPS 199): Define system impact levels (Low, Moderate, High) based on confidentiality, integrity, and availability.  
2. **Select Security Controls** (NIST SP 800-53): Tailor baseline controls to system categorization; controls are grouped into families (e.g., Access Control, Audit and Accountability).  
3. **Implement Controls**: Deploy selected controls with documented procedures.  
4. **Assess Controls** (SP 800-53A): Conduct security control assessments using test plans, interviews, and technical testing to determine effectiveness.  
5. **Authorize System**: Authorizing Official (AO) reviews security package and issues Authorization to Operate (ATO) or denial.  
6. **Monitor Controls**: Continuous monitoring through automated tools and periodic reassessment to detect changes in risk posture.  
RMF emphasizes iterative risk management and compliance with federal standards.

MITRE ATT&CK FRAMEWORK  
MITRE ATT&CK is a globally accessible knowledge base of adversary tactics and techniques based on real-world observations. It is structured into:  
- **Tactics**: The adversary’s tactical goals (e.g., Initial Access, Persistence, Privilege Escalation).  
- **Techniques**: Specific methods used to achieve tactics (e.g., Spearphishing Attachment, DLL Injection).  
- **Sub-techniques**: Granular variations of techniques.  
Security teams map detected adversary behaviors to ATT&CK IDs (e.g., T1078 for Valid Accounts) to understand attack patterns and improve detection. ATT&CK Navigator is used for visualization and gap analysis. Integration with SIEM and EDR platforms enables automated detection and response aligned to ATT&CK.

ZERO TRUST ARCHITECTURE (ZTA)  
Defined by NIST SP 800-207, Zero Trust assumes no implicit trust inside or outside the network perimeter. Core principles:  
- **Continuous Verification**: Authenticate and authorize every access request dynamically using multifactor authentication (MFA), device posture, and user behavior analytics.  
- **Least Privilege Access**: Enforce granular access controls based on identity, device, location, and risk context.  
- **Microsegmentation**: Divide network into isolated segments to limit lateral movement.  
- **Assume Breach**: Design systems assuming adversaries are already present.  
Implementation involves Policy Engine (PE), Policy Administrator (PA), and Policy Enforcement Point (PEP) components. Technologies include Identity Providers (IdP), Software-Defined Perimeter (SDP), and Secure Access Service Edge (SASE).

CRYPTOGRAPHIC PROTOCOLS AND STANDARDS  
Cryptography underpins confidentiality and integrity in cybersecurity. Key standards and protocols include:  
- **AES (Advanced Encryption Standard)**: Symmetric cipher with key sizes 128, 192, 256 bits; block size 128 bits; standardized by NIST FIPS 197.  
- **RSA**: Asymmetric encryption algorithm based on integer factorization; typical key sizes 2048 or 3072 bits for secure communication.  
- **TLS (Transport Layer Security)**: Protocol for secure communication; latest version TLS 1.3 (RFC 8446) mandates ephemeral key exchange (ECDHE) and AEAD ciphers (AES-GCM, ChaCha20-Poly1305).  
- **HMAC (Hash-based Message Authentication Code)**: Combines cryptographic hash functions with a secret key for message integrity and authentication.  
- **PKI (Public Key Infrastructure)**: Framework for digital certificates and certificate authorities (CAs) enabling trust establishment.  
Proper cryptographic lifecycle management includes key generation, storage (HSMs), rotation, and revocation.

INCIDENT RESPONSE (IR) PROCESS  
Structured by frameworks such as NIST SP 800-61 Rev. 2, the IR lifecycle includes:  
1. **Preparation**: Establish IR team, tools, communication plans, and training.  
2. **Detection and Analysis**: Use IDS/IPS, SIEM, and endpoint telemetry to identify incidents; classify severity and scope.  
3. **Containment, Eradication, and Recovery**: Short-term containment (e.g., isolate affected systems), eradicate root cause (malware removal, patching), and restore systems to operational state.  
4. **Post-Incident Activity**: Conduct lessons learned sessions, update policies, and improve defenses.  
Key metrics include Mean Time to Detect (MTTD) and Mean Time to Respond (MTTR). Automation with SOAR platforms accelerates response.

IDENTITY AND ACCESS MANAGEMENT (IAM)  
IAM governs user identities and access privileges to resources. Core components:  
- **Authentication**: Verifying user identity via passwords, biometrics, tokens, or MFA (e.g., TOTP, FIDO2).  
- **Authorization**: Enforcing access policies using Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), or Policy-Based Access Control (PBAC).  
- **Identity Federation**: Using standards like SAML 2.0, OAuth 2.0, and OpenID Connect to enable single sign-on (SSO) across domains.  
- **Privileged Access Management (PAM)**: Controls and audits elevated access, often using Just-In-Time (JIT) provisioning and session recording.  
IAM solutions must integrate with directory services (e.g., Active Directory, LDAP) and support least privilege principles.

SECURITY METRICS AND MEASUREMENT  
Quantitative metrics enable objective security posture assessment:  
- **Vulnerability Management**: Number of critical/high vulnerabilities, time to patch (goal <30 days for critical CVEs per CISA guidelines).  
- **Attack Surface Reduction**: Count of exposed services, open ports, and unnecessary privileges.  
- **Security Incident Metrics**: MTTD, MTTR, number of incidents per quarter.  
- **Compliance Scores**: Percentage adherence to frameworks like CIS Controls, ISO 27001.  
- **Risk Scores**: Using FAIR (Factor Analysis of Information Risk) model to quantify probable loss magnitude and frequency.  
Dashboards and KPIs must align with organizational risk appetite and regulatory requirements.

## Mastery Levels

L1: Understand basic CIA triad and common cyber threats (phishing, malware).  
L2: Apply fundamental security controls (firewalls, antivirus) and password hygiene.  
L3: Conduct vulnerability scans and interpret results using CVSS scores.  
L4: Develop and implement incident response playbooks per NIST guidelines.  
L5: Design and enforce IAM policies with MFA and RBAC in enterprise environments.  
L6: Architect Zero Trust networks integrating microsegmentation and continuous monitoring.  
L7: Lead threat hunting using MITRE ATT&CK to identify advanced persistent threats (APTs).  
L8: Innovate cybersecurity strategy with risk quantification (FAIR), cryptographic protocol design, and adversarial simulation at enterprise scale.

## Mechanisms

In computer science, cybersecurity mechanisms involve a series of steps and processes that work together to protect computer systems, networks, and data from unauthorized access, use, disclosure, disruption, modification, or destruction. The causal chain begins with threat identification, where potential vulnerabilities and risks are assessed and prioritized. This is followed by the implementation of security controls, such as firewalls, intrusion detection systems, and encryption algorithms, which are designed to prevent or detect malicious activity. 
When a potential threat is detected, the system triggers an alert and notification process, which informs system administrators or security personnel of the potential issue. This is followed by an incident response process, which involves containment, eradication, recovery, and post-incident activities to minimize the impact of the threat. 
Access control mechanisms, such as authentication, authorization, and accounting (AAA), are also crucial in ensuring that only authorized users have access to system resources and data. These mechanisms involve verifying user identities, granting or denying access based on user roles and permissions, and monitoring user activity to detect potential security breaches. 
The causal chain is further reinforced by continuous monitoring and evaluation, which involves regularly assessing system security controls, updating security protocols, and conducting penetration testing and vulnerability assessments to identify and address potential weaknesses. 
Ultimately, the effectiveness of cybersecurity mechanisms depends on the ability to integrate these various processes and controls into a comprehensive security framework that can adapt to evolving threats and vulnerabilities.

In computer science, cybersecurity mechanisms involve a series of steps and processes that work together to protect computer systems, networks, and data from unauthorized access, use, disclosure, disruption, modification, or destruction. The causal chain begins with threat identification, where potential vulnerabilities and risks are assessed and prioritized. This is followed by the implementation of security controls, such as firewalls, intrusion detection systems, and encryption algorithms, which are designed to prevent or detect malicious activity. 
When a potential threat is detected, the system triggers an alert and notification process, which informs system administrators or security personnel of the potential issue. This is followed by an analysis and response phase, where the threat is evaluated and mitigated through the implementation of countermeasures, such as blocking malicious traffic or isolating affected systems. 
The causal chain also involves continuous monitoring and evaluation, where system logs and network traffic are analyzed to identify potential security incidents and improve the overall security posture of the system. This is achieved through the use of security information and event management (SIEM) systems, which provide real-time visibility into security-related data and enable proactive threat detection and response. 
Ultimately, the goal of cybersecurity mechanisms is to ensure the confidentiality, integrity, and availability of computer systems and data, and to prevent or minimize the impact of security breaches and other malicious activity.

## Methods And Frameworks

In computer science, various methods and frameworks are employed to ensure cybersecurity. The NIST Cybersecurity Framework provides a structured approach to managing and reducing cybersecurity risk, comprising five core functions: Identify, Protect, Detect, Respond, and Recover. The CIA Triad (Confidentiality, Integrity, and Availability) model is used to guide cybersecurity policies and procedures. The OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) methodology is a risk-based approach to cybersecurity, focusing on identifying and mitigating critical threats. The STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privilege) threat model is used to identify and categorize potential threats. The DREAD (Damage potential, Reproducibility, Exploitability, Affected users, and Discoverability) risk assessment formula is applied to calculate the risk of a potential threat. Each method and framework has its specific use case and failure mode, such as the NIST framework being too general for small organizations, while the CIA Triad may not account for emerging threats. Understanding the strengths and limitations of each method and framework is crucial for effective cybersecurity implementation.

In computer science, cybersecurity employs various methods and frameworks to protect computer systems and networks from threats. The NIST Cybersecurity Framework provides a structured approach to managing cybersecurity risk, comprising five core functions: Identify, Protect, Detect, Respond, and Recover. The CIA Triad (Confidentiality, Integrity, Availability) model is used to guide cybersecurity decisions, ensuring that data is protected from unauthorized access, modification, and disruption. The OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) method is a risk-based approach to cybersecurity, focusing on identifying and mitigating critical threats. The STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege) threat model is used to identify potential threats to system security. Each of these methods and frameworks has its own failure mode, such as over-reliance on a single framework or inadequate consideration of emerging threats. The Bell-LaPadula model and the Biba model are used to enforce access control and data integrity, respectively. The failure mode of these models often lies in their inability to adapt to complex, dynamic systems. Ultimately, a combination of these methods and frameworks, tailored to the specific needs of an organization, is necessary to ensure effective cybersecurity.

## Worked Examples

To illustrate key concepts in cybersecurity, consider the following examples. 
1. **Password Strength**: A company requires passwords to be at least 12 characters long, containing at least one uppercase letter, one lowercase letter, one digit, and one special character. If a user chooses a password that meets these criteria, what is the minimum number of possible passwords, assuming 26 uppercase letters, 26 lowercase letters, 10 digits, and 32 special characters? 
The minimum number of possible passwords can be calculated as 26 (uppercase) * 26 (lowercase) * 10 (digit) * 32 (special character) * (26+26+10+32)^8 (for the remaining 8 characters), which equals 26 * 26 * 10 * 32 * 94^8.
2. **Encryption**: A message is encrypted using AES-128, which has a block size of 128 bits. If the message is 1024 bits long, how many blocks will be required to encrypt the message? 
Since each block is 128 bits, the number of blocks required is 1024 / 128 = 8.
3. **Network Security**: A network has 100 devices, each with an equal chance of being compromised. If the probability of a device being compromised is 0.01, what is the expected number of compromised devices? 
The expected number of compromised devices can be calculated as the number of devices * probability of compromise, which equals 100 * 0.01 = 1.

1. **Password Cracking**: Suppose we have a password with a length of 8 characters, consisting of uppercase and lowercase letters, and digits. To calculate the number of possible combinations, we use the formula for permutations with repetition: n^r, where n is the number of options (62 for uppercase and lowercase letters, and digits) and r is the length of the password. So, 62^8 = 218,340,105,584,896 possible combinations. If a password cracking algorithm can try 100,000 combinations per second, it would take approximately 218,340,105,584,896 / 100,000 = 2,183,401,055 seconds or around 69.5 years to try all combinations.

2. **Firewall Configuration**: A company has a network with 100 devices and wants to configure a firewall to block incoming traffic on ports 80 (HTTP) and 22 (SSH), except for a specific IP address (192.168.1.100). The firewall rules would be: (i) block incoming traffic on port 80, (ii) block incoming traffic on port 22, and (iii) allow incoming traffic on ports 80 and 22 from IP address 192.168.1.100. This configuration ensures that only the specified device can access the network via HTTP and SSH.

3. **Encryption Key Size**: Consider an encryption algorithm that uses a 128-bit key. To determine the number of possible keys, we use the formula 2^n, where n is the key size in bits. So, 2^128 = 3.4 x 10^38 possible keys. If an attacker can try 1 million keys per second, it would take approximately 3.4 x 10^38 / 1,000,000 = 3.4 x 10^31 seconds or around 1.08 x 10^24 years to try all possible keys, making it computationally infeasible to brute-force the encryption.

## Applications

In computer science, cybersecurity has numerous practical applications across various domains. In network security, firewalls and intrusion detection systems are used to protect against unauthorized access and malicious activity. Cryptography is applied to secure online transactions, such as online banking and e-commerce, through protocols like SSL/TLS. In operating system security, access control mechanisms like role-based access control (RBAC) and mandatory access control (MAC) are used to restrict user privileges and prevent unauthorized access to sensitive data. 
In cloud computing, security measures like encryption, secure data storage, and identity and access management (IAM) are used to protect data and applications. In mobile device security, techniques like secure boot, encryption, and application sandboxing are used to prevent malware and unauthorized access. 
In application security, secure coding practices like input validation, secure authentication, and authorization are used to prevent vulnerabilities like SQL injection and cross-site scripting (XSS). Additionally, cybersecurity is applied in IoT security to protect connected devices from unauthorized access and malicious activity, and in incident response to quickly respond to and contain security breaches.

Cybersecurity has numerous applications in various domains, including finance, healthcare, and government. In finance, cybersecurity is used to protect sensitive financial information, such as credit card numbers and bank account details, from unauthorized access. This is achieved through the implementation of secure protocols, such as HTTPS and TLS, and the use of encryption algorithms, like AES. In healthcare, cybersecurity is crucial for protecting patient data, including medical records and personal identifiable information. The Health Insurance Portability and Accountability Act (HIPAA) sets standards for securing patient data, which includes implementing access controls, encrypting data, and monitoring systems for potential security breaches. In government, cybersecurity is used to protect classified information and prevent cyber attacks on critical infrastructure, such as power grids and transportation systems. Additionally, cybersecurity is applied in cloud computing, where data is stored and processed remotely, and in the Internet of Things (IoT), where devices are connected to the internet and vulnerable to attacks. In these domains, cybersecurity measures, such as firewalls, intrusion detection systems, and secure coding practices, are used to prevent and detect security threats. Furthermore, incident response plans are developed to respond to security breaches and minimize damage. Overall, cybersecurity is essential for protecting sensitive information and preventing financial loss, reputational damage, and legal liability.

## Common Errors

In computer science, cybersecurity practitioners often make mistakes that compromise the security of systems and data. One common error is the use of weak passwords or password policies, such as allowing easily guessable passwords or not implementing multi-factor authentication. This is wrong because it allows attackers to gain unauthorized access to systems using brute-force or dictionary attacks. Another error is the failure to keep software up-to-date, leaving known vulnerabilities unpatched and exploitable by attackers. Additionally, practitioners may misconfigure firewalls or access control lists, allowing unauthorized access to sensitive data or systems. The use of insecure communication protocols, such as unencrypted HTTP or Telnet, is also a common mistake, as it allows attackers to intercept or eavesdrop on sensitive data. Furthermore, the lack of regular security audits and penetration testing can lead to undetected vulnerabilities and weaknesses, allowing attackers to exploit them. These errors are often due to a lack of understanding of security principles, inadequate training, or insufficient resources. By understanding these common errors, practitioners can take steps to avoid them and improve the overall security posture of their systems and data.

In computer science, cybersecurity practitioners often make mistakes that compromise the security of systems and data. One common error is the use of weak passwords or inadequate password policies, allowing attackers to gain unauthorized access through brute-force attacks or password guessing. Another mistake is the failure to keep software up-to-date, leaving vulnerabilities unpatched and exploitable by malicious actors. Additionally, the misuse of secure communication protocols, such as SSL/TLS, can lead to man-in-the-middle attacks and eavesdropping. Insufficient access control and privilege management can also result in unauthorized access to sensitive data and systems. Furthermore, the lack of regular security audits and penetration testing can lead to undetected vulnerabilities, allowing attackers to remain hidden in the system for extended periods. These errors often stem from a lack of understanding of security principles, inadequate training, or insufficient resources, highlighting the importance of ongoing education and investment in cybersecurity measures.

## Advanced

The graduate-level extensions of cybersecurity involve the application of advanced cryptographic techniques, such as homomorphic encryption and zero-knowledge proofs, to enable secure computation on private data. Another key area is the development of formal methods for verifying the security of complex systems, including the use of model checking and proof assistants like Coq. Open questions in the field include the development of effective defenses against sophisticated attacks, such as advanced persistent threats (APTs) and ransomware, as well as the creation of secure and scalable solutions for emerging technologies like the Internet of Things (IoT) and cloud computing. The field is moving towards a greater emphasis on artificial intelligence (AI) and machine learning (ML) for cybersecurity, including the use of anomaly detection and predictive analytics to identify potential threats. Additionally, there is a growing focus on the human factor in cybersecurity, including the development of user-centered security design and the study of the psychological and social factors that influence security behavior. Researchers are also exploring the application of cybersecurity principles to new domains, such as autonomous vehicles and industrial control systems. Furthermore, the increasing use of quantum computing is driving the development of quantum-resistant cryptographic algorithms, such as lattice-based cryptography and code-based cryptography, to ensure the long-term security of digital communications.

At the graduate level, cybersecurity extends into specialized areas such as cryptography, formal methods, and artificial intelligence for security. Advanced cryptographic techniques, including homomorphic encryption and zero-knowledge proofs, enable computations on encrypted data without decrypting it, ensuring confidentiality and integrity. Formal methods, such as model checking and theorem proving, provide rigorous approaches to verifying the security properties of systems. The application of artificial intelligence and machine learning to cybersecurity involves developing predictive models for threat detection, incident response, and security information and event management (SIEM) systems. Open questions in the field include the development of secure multi-party computation protocols, the mitigation of side-channel attacks, and the creation of effective defenses against advanced persistent threats (APTs). The field is moving towards a greater emphasis on security by design, DevSecOps, and the integration of security into the software development lifecycle. Additionally, the increasing use of cloud computing, Internet of Things (IoT), and edge computing is driving the need for new security architectures and protocols that can address the unique challenges of these environments. Researchers are also exploring the application of emerging technologies, such as blockchain and quantum computing, to cybersecurity, and the potential impact of these technologies on the field.
