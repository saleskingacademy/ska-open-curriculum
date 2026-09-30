---
key: information_science
title: "Information Science"
program: general_studies
course_level: 3
dna16: "0701201814357773"
l4_address: "S6:P2135438767"
chain256_anchor: "1077288351479377153263202132137014988378032013700121404787606579111993351681808406532406996613700928586503671370011375425969065401263787543423201757568024021370147170968965137001439802343577220613701630661615111239479092137017816707336913700379438619647931"
updated_at: "2026-08-26T06:58:13.702Z"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Information Science

> name heuristic - model placement unavailable

## Foundations

Information Science is the interdisciplinary study of the collection, classification, manipulation, storage, retrieval, and dissemination of information. Rooted in the convergence of computer science, library science, cognitive psychology, and communication theory, it formalizes how data is transformed into meaningful knowledge within socio-technical systems. At its core, Information Science investigates the lifecycle of information artifacts and the human and machine agents interacting with them, guided by principles such as Shannon’s Information Theory (entropy \(H = -\sum p_i \log_2 p_i\)), the DIKW hierarchy (Data → Information → Knowledge → Wisdom), and the socio-technical feedback loops that govern information ecosystems.

Information science, as a social science discipline, examines the social, cultural, and political contexts of information production, dissemination, and consumption. **Information** refers to data that has been given meaning through interpretation and context, thereby becoming relevant and useful to individuals or groups. **Data**, in contrast, are raw, uninterpreted symbols, signals, or messages. A **message** is a unit of information conveyed through a medium, such as text, image, or sound. **Medium** refers to the channel or platform through which information is transmitted, including print, digital, or face-to-face communication. **Communication** is the process of exchanging information between individuals, groups, or organizations, involving **encoding** (converting information into a message), **transmission** (sending the message through a medium), and **decoding** (interpreting the message). **Information systems** are social and technological networks that facilitate the creation, dissemination, and use of information, including libraries, archives, and digital platforms. **Knowledge** is the outcome of information processing, involving the integration of new information with existing understanding and experience. Understanding these core concepts and their relationships is essential for practitioners in the field of information science.

## Section

INFORMATION RETRIEVAL FRAMEWORK  
The Vector Space Model (Salton et al., 1975) forms a foundational retrieval framework. Documents and queries are represented as vectors in an n-dimensional term space, where each dimension corresponds to a unique term weighted by TF-IDF (Term Frequency-Inverse Document Frequency):  
\[
\text{TF-IDF}_{t,d} = tf_{t,d} \times \log\frac{N}{df_t}
\]  
where \(tf_{t,d}\) is term frequency of term \(t\) in document \(d\), \(N\) the total number of documents, and \(df_t\) the document frequency of term \(t\). Retrieval ranking is computed via cosine similarity:  
\[
\cos(\theta) = \frac{\vec{d} \cdot \vec{q}}{\|\vec{d}\| \|\vec{q}\|}
\]  
This model underpins search engines and informs relevance feedback loops.

KNOWLEDGE ORGANIZATION SYSTEMS (KOS)  
Taxonomies, thesauri, and ontologies are structured vocabularies enabling semantic interoperability. The Simple Knowledge Organization System (SKOS) standard (W3C, 2009) encodes concepts and semantic relations (broader, narrower, related) using RDF triples. Ontologies extend KOS with axioms and constraints, formalized in Description Logics (DL), e.g., \(\mathcal{ALC}\) logic, enabling automated reasoning via tableau algorithms. The Protégé platform (Stanford) operationalizes ontology development, supporting OWL-DL compliance.

INFORMATION BEHAVIOR MODELS  
Wilson’s (1999) nested model of information behavior distinguishes information seeking, searching, and use. Belkin’s ASK (Anomalous State of Knowledge) model formalizes user query formulation as a function of cognitive states. The Ellis Model (1989) identifies discrete information-seeking activities: starting, chaining, browsing, differentiating, monitoring, and extracting, which inform user-centered system design.

DATA CURATION AND METADATA STANDARDS  
Data curation ensures long-term usability and provenance. The Open Archival Information System (OAIS) Reference Model (ISO 14721:2012) defines functional entities: Ingest, Archival Storage, Data Management, Administration, Preservation Planning, and Access. Metadata schemas such as Dublin Core (15 core elements) and PREMIS (Preservation Metadata) provide standardized descriptors critical for interoperability. The FAIR principles (Wilkinson et al., 2016) codify data stewardship: Findable, Accessible, Interoperable, Reusable.

INFORMATION VISUALIZATION TECHNIQUES  
Information visualization translates abstract data into graphical representations to leverage human perceptual capabilities. The Shneiderman’s Mantra ("Overview first, zoom and filter, then details-on-demand") guides interactive visualization design. Techniques include node-link diagrams for networks, heatmaps for matrix data, and dimensionality reduction algorithms such as t-SNE (van der Maaten & Hinton, 2008) for high-dimensional data embedding, optimizing cluster separability.

INFORMATION ETHICS AND POLICY  
Information Science critically examines ethical frameworks governing information access, privacy, and intellectual property. The Fair Information Practice Principles (FIPPs) establish guidelines on data collection, use, and security. The GDPR (EU, 2018) codifies data subject rights and organizational obligations, influencing system design. The Principle of Least Privilege and Differential Privacy (Dwork, 2006) offer technical mechanisms to enforce ethical standards.

INFORMATION SYSTEMS DESIGN AND EVALUATION  
The Systems Development Life Cycle (SDLC) formalizes design phases: requirements analysis, system design, implementation, testing, deployment, and maintenance. Usability evaluation employs Nielsen’s heuristics (1994), including visibility of system status, match between system and real world, user control, and error prevention. Information system success is quantitatively measured using DeLone and McLean’s IS Success Model (1992), comprising system quality, information quality, service quality, use, user satisfaction, and net benefits.

## Mastery Levels

L1: Recognizes information as data with context, understanding basic search operations.  
L2: Applies Boolean logic and simple keyword queries in information retrieval.  
L3: Implements TF-IDF weighting and cosine similarity for document ranking.  
L4: Designs controlled vocabularies and understands ontology basics using OWL.  
L5: Models user information behavior using Ellis and Belkin frameworks.  
L6: Develops metadata schemas compliant with Dublin Core and FAIR principles.  
L7: Constructs interactive visualizations employing t-SNE and Shneiderman’s Mantra.  
L8: Leads ethical information system design integrating GDPR, differential privacy, and IS success metrics.

## Mechanisms

Information science in the social sciences context operates through several mechanisms that facilitate the creation, dissemination, and use of information. The first mechanism involves the generation of information, which typically starts with data collection from various sources such as surveys, experiments, or existing literature. This data is then analyzed and interpreted to form meaningful information. The second mechanism is the storage and organization of information, often through databases, libraries, or digital repositories, which enable efficient retrieval and access. The third mechanism is the dissemination of information, which can occur through various channels such as academic journals, books, conferences, or online platforms. The causal chain becomes explicit when considering how these mechanisms interact: the generation of information leads to its storage, which in turn facilitates its dissemination. Dissemination then leads to the use of information by individuals or groups, who may apply it to solve problems, make decisions, or create new knowledge. This use of information can feedback into the generation of new information, creating a continuous cycle. Furthermore, social and technological factors influence these mechanisms, with advancements in technology, for instance, enhancing the speed and reach of information dissemination, and social norms affecting what information is considered valuable or relevant. Understanding these mechanisms and their interactions is crucial for managing information effectively in the social sciences.

## Methods And Frameworks

In information science, as studied in social sciences, several methods and frameworks are employed to analyze and understand the complex interactions between information, people, and society. The Social Network Analysis (SNA) method is used to examine the relationships and information flows within social networks, and is particularly useful when studying the diffusion of information or the impact of social structures on information exchange. However, SNA's failure mode lies in its inability to account for the content and context of the information being exchanged. 
The Uses and Gratifications (U&G) framework is applied to understand how people use information to satisfy their needs and desires, and is effective when investigating the motivations behind information-seeking behaviors. Nevertheless, U&G's limitation arises from its focus on individual-level analysis, neglecting the broader social and cultural contexts that shape information use. 
The Technological Acceptance Model (TAM) is utilized to predict how people adopt and use new information technologies, and is suitable when evaluating the likelihood of a new technology being accepted by a particular group. Nonetheless, TAM's failure mode stems from its oversimplification of the complex factors influencing technological adoption, such as social and cultural factors. 
The Information Worlds (IW) framework is employed to examine how different social groups create and negotiate meaning around information, and is valuable when analyzing the power dynamics and social inequalities that shape information access and use. However, IW's limitation lies in its emphasis on the social construction of information, potentially overlooking the material and technological aspects of information production and dissemination. 
The Sense-Making Methodology (SMM) is used to study how people make sense of and interpret information, and is particularly useful when investigating the cognitive and emotional processes involved in information processing. Nevertheless, SMM's failure mode arises from its focus on individual-level sense-making, neglecting the collective and social aspects of information interpretation. 
These methods and frameworks provide a foundation for understanding the complex interactions between information, people, and society, but it is essential to recognize their limitations and potential failure modes to apply them effectively in information science research.

## Worked Examples

To illustrate the application of information science concepts in social sciences, consider the following examples. 
1. A researcher wants to calculate the information entropy of a dataset containing survey responses from 100 participants, where 60 responded "yes" and 40 responded "no" to a particular question. Using the formula for entropy (H = -Σ(p * log2(p))), where p is the probability of each response, we calculate the entropy as H = -((0.6 * log2(0.6)) + (0.4 * log2(0.4))) = -((0.6 * -0.74) + (0.4 * -1.32)) = -(-0.44 - 0.53) = 0.97 bits. 
2. A social media platform has 1 million users, with an average of 500 friends per user. If the platform wants to recommend friends to a user based on their mutual friends, and assuming a random graph model, the probability of two users being friends is 500/1,000,000 = 0.0005. Using the concept of small-world networks, we can estimate the average path length between two users as approximately log(1,000,000)/log(500) = 4. 
3. A library has a collection of 10,000 books, with 2000 books on a particular topic. If a user searches for books on this topic using a keyword search, and the search algorithm returns 1500 relevant books out of 2000 total relevant books, with 300 irrelevant books, we can calculate the precision (1500/1800 = 0.83) and recall (1500/2000 = 0.75) of the search algorithm. These metrics can be used to evaluate the effectiveness of the search algorithm in retrieving relevant information.

## Applications

In the social sciences, Information Science is applied in various domains to understand and address complex information-related issues. One key application is in the field of library and information services, where information scientists design and implement systems for organizing, retrieving, and disseminating information. For instance, they develop taxonomies and ontologies to categorize and link related information, facilitating discovery and access to relevant knowledge. In the context of archival science, information scientists apply principles of preservation and conservation to ensure the long-term availability and usability of historical records and cultural heritage materials. Additionally, information scientists work in the domain of human-computer interaction, designing user-centered information systems that accommodate diverse user needs and behaviors. They also contribute to the development of information policies and laws, such as copyright and intellectual property regulations, to govern the creation, dissemination, and use of information in society. Furthermore, information scientists apply their knowledge in the field of information literacy, educating individuals and communities on how to critically evaluate and effectively use information to make informed decisions. By understanding the social, cultural, and technological contexts of information, information scientists can develop targeted interventions to address issues like misinformation, disinformation, and information inequality.

## Common Errors

In the field of Information Science as studied in Social Sciences, practitioners often make mistakes that can compromise the validity and reliability of their research. One common error is the conflation of information with knowledge, where information is mistakenly assumed to be equivalent to knowledge. This error arises from a lack of understanding of the distinction between the two concepts: information refers to the raw data or messages, whereas knowledge implies the interpretation, contextualization, and application of that information. Another error is the failure to consider the social and cultural contexts in which information is created, disseminated, and used. This can lead to the neglect of power dynamics, social inequalities, and cultural biases that shape information production and consumption. Furthermore, practitioners may also fall into the trap of technicism, where they overemphasize the role of technology in information systems, neglecting the social and organizational factors that influence information behaviors and practices. Additionally, the assumption of a neutral or objective information system is another common mistake, as information systems are often embedded in social and cultural contexts that shape their design, implementation, and use. These errors can be avoided by adopting a critical and nuanced approach to Information Science, one that recognizes the complex interplay between social, cultural, and technological factors that shape information behaviors and practices.

## Advanced

In the social sciences, advanced information science explores the complex interplay between information, society, and technology. Graduate-level research delves into the critical examination of information systems, infrastructures, and institutions, analyzing their impact on social structures, power dynamics, and cultural norms. Key areas of investigation include the political economy of information, information policy and governance, and the social implications of emerging technologies such as artificial intelligence and big data. Open questions in the field concern the tension between information privacy and surveillance, the digital divide and unequal access to information, and the role of information in shaping social movements and collective action. The field is moving towards a deeper understanding of the intersections between information, power, and social justice, with a growing focus on critical information studies, postcolonial perspectives, and the development of more nuanced and contextualized theories of information and society. Researchers are also exploring new methodologies, such as critical discourse analysis and participatory action research, to study the complex and dynamic relationships between information, technology, and society.
