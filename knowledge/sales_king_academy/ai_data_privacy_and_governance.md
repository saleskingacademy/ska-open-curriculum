---
key: ai_data_privacy_and_governance
title: "AI Data Privacy And Governance"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-10-08"
chapter: "Sales King Academy, Volume 1, Chapter 4"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# AI Data Privacy and Governance

The earlier chapters of this volume showed what AI can do for a business and how to decide where it belongs. This chapter deals with the question that decides whether a business can keep using AI at all: what happens to the data. Every AI feature reads something, and in a sales or service business that something is usually information about real people. You will learn the core principles of privacy law, how personal data moves through an AI system, which technical safeguards work and how to measure them, how to build a governance programme that a small team can actually run, and how to answer the questions customers and regulators will ask. The chapter closes with a field case from the Sales King Academy platform, where a privacy leak was closed at a single point in the system, and a lab you complete on the live site.

This chapter explains general principles of privacy law for business learners. It is not legal advice. Laws differ by country and state and change over time, so a business with a specific question should consult a qualified lawyer in its jurisdiction.

## Learning objectives

By the end of this chapter you will be able to:

1. Define personal data, sensitive data and confidential business data, and explain why AI systems raise new risks for each.
2. State the core principles shared by modern privacy laws, including purpose limitation, data minimization, storage limitation and accountability.
3. Map the flow of personal data through an AI feature, from collection to prompt, retrieval, logs, memory and output.
4. Distinguish controllers from processors and list what a data processing agreement with an AI provider should cover.
5. Choose and measure technical safeguards such as redaction, pseudonymization, access control and output filtering.
6. Build a simple AI governance programme: a use policy, a system register, a risk assessment and an incident process.
7. Describe the main obligations of the GDPR, the California privacy rules and the EU AI Act at a level suitable for business planning.
8. Handle individual rights requests and breach deadlines correctly when AI systems hold copies of personal data.
9. Inspect what personal data the Sales King Academy platform shows you, and test where its privacy boundaries sit.

## 1. Why AI changes the privacy problem

Privacy is not new. Businesses have kept customer files, mailing lists and payment records for as long as there have been businesses, and laws about how those records may be used are decades old. What AI changes is how easily data moves, how many copies of it exist and how hard it is to see where it went.

### Three kinds of data a business must protect

It helps to separate three categories, because each carries different duties.

**Personal data** is any information that relates to an identified or identifiable person. A name, an email address, a phone number, a home address, an account number, a photograph, an IP address and a customer ID linked to a person are all personal data. So is information that identifies someone only when combined with other details, such as "the regional sales manager in our Tulsa office who joined in March." Privacy laws are built around this category.

**Sensitive personal data** is the subset that can cause serious harm if misused. Under European law the special categories include health information, racial or ethnic origin, political opinions, religious or philosophical beliefs, trade union membership, genetic data, biometric data used for identification, and information about a person's sex life or sexual orientation. Other laws add items such as government identification numbers, precise location, financial account credentials and the contents of private messages. Sensitive data generally needs a stronger legal reason to process it and stronger protection while it is held.

**Confidential business data** may contain no personal data at all: pricing models, unreleased product plans, source code, contract terms, a customer list's revenue figures. Privacy law may not cover it, but contracts, trade secret law and plain business sense do. Many AI leaks that make the news involve this category, such as an employee pasting internal code or a draft contract into a public tool.

### What is different about AI

Four features of AI systems create risk that ordinary software does not.

**Copying is effortless.** Using an AI assistant means sending it text. A salesperson who wants a summary of a long email thread pastes the whole thread, with every signature block, phone number and forwarded attachment inside it. In one action, personal data about a dozen people has been copied to an outside service.

**Copies multiply.** A single AI request can create several lasting copies: the prompt stored in the provider's logs, the conversation saved in the user's history, chunks placed in a search index for retrieval, a summary written back to the CRM, and possibly a memory entry the assistant keeps for later conversations. Each copy has its own retention period and its own access rules, and each must be found when a person asks for their data to be deleted.

**Outputs can reveal inputs.** A model that has been given a document can repeat parts of it to anyone who later asks the right question in the same context. A model trained or fine-tuned on personal data can sometimes reproduce fragments of that data. An assistant connected to a shared knowledge base can answer one user's question with another user's information if access rules are not enforced at the moment of retrieval.

**Instructions can hide in data.** As Chapter 1 explained, an AI system that reads outside content can be manipulated by instructions hidden in that content. In a privacy setting, the danger is that a malicious email or web page tells the assistant to collect and send out data it has access to.

None of these risks means a business should avoid AI. They mean it should know where its data goes, keep only what it needs, and put controls at the points where data leaves its hands.

## 2. The principles behind privacy law

Privacy laws around the world differ in detail, but most rest on a shared set of principles that trace back to fair information practice ideas developed in the 1970s and 1980s. The European Union's General Data Protection Regulation (GDPR) states them most completely, and other laws, including the California rules, borrow many of them. A business that builds its AI use around these principles will be in good shape under most regimes, even before it checks the specific rules that apply.

### The seven core principles

1. **Lawfulness, fairness and transparency.** There must be a legal basis for using the data, the use must not be unfair to the person, and people must be told in clear language what is done with their data.
2. **Purpose limitation.** Data collected for one stated purpose should not be reused for a different, incompatible purpose. Contact details collected to deliver an order are not automatically available for training a marketing model.
3. **Data minimization.** Collect and use only the data that is adequate and necessary for the purpose. A call summary does not need the customer's date of birth.
4. **Accuracy.** Personal data should be correct and kept up to date, and wrong data should be fixed or deleted. This matters for AI because a model's confident but wrong statement about a person, written into a CRM, becomes inaccurate personal data.
5. **Storage limitation.** Data should be kept in identifiable form only as long as the purpose requires. Logs and conversation histories are the most common place where this principle quietly fails.
6. **Integrity and confidentiality.** Data must be protected against unauthorized access, loss and damage with appropriate security.
7. **Accountability.** The organization must not only follow the principles but be able to show that it does, through records, policies and evidence.

### Legal bases for processing

Under the GDPR, every use of personal data needs one of six legal bases: the person's **consent**; necessity for a **contract** with the person; a **legal obligation**; protecting someone's **vital interests**; a task in the **public interest**; or the organization's **legitimate interests**, where those interests are not overridden by the person's rights. Most business AI uses rely on contract or legitimate interests. Consent is often misunderstood as the default; in practice it is the right basis only when the person has a genuine choice and can withdraw it easily, and it becomes awkward when the data has already been built into a system that cannot easily forget it.

United States law works differently. There is no single national privacy law covering all businesses. Instead, a growing number of states have comprehensive consumer privacy laws, with California's the most developed, and federal laws cover particular sectors and groups. The US approach leans more on notice and the right to opt out than on requiring a legal basis in advance. A business that serves customers in several places must follow each set of rules that applies to it, which is one reason many companies simply adopt the stricter European-style principles everywhere.

### Rights individuals hold

Modern privacy laws give people rights over their data. The common ones are the right to know what data is held and how it is used, the right to receive a copy, the right to correct it, the right to have it deleted, the right to object to or opt out of certain uses (such as selling or sharing data for targeted advertising), and the right to data portability. The GDPR adds a specific protection for automated decisions, discussed in Section 6. Every one of these rights touches AI systems, because AI systems hold copies of personal data in places that ordinary record-keeping does not reach.

### Privacy by design and by default

Privacy by design means building privacy protections into a system from the start rather than adding them after a problem. Privacy by default means that the most protective setting is the one a user gets without doing anything. For AI features, this translates into practical choices: an assistant that does not keep conversation memory unless the user turns it on, a summarizer that drops payment fields before sending text, and a reporting screen that shows aggregated figures rather than individual records unless the viewer has a reason to see them. The GDPR makes data protection by design and by default a legal duty, but the idea is good practice everywhere.

## 3. Mapping how data flows through an AI system

You cannot protect what you cannot see. The first practical step in AI privacy is a **data flow map**: a record of every place personal data enters, travels through, is stored in, and leaves an AI feature.

### The stages of an AI data flow

A typical AI feature in a sales or service business has these stages.

1. **Collection.** Data enters the business through forms, calls, emails, purchases, website tracking or imports from other systems.
2. **Storage in systems of record.** The CRM, the billing system, the support desk and the email platform hold the master copies.
3. **Selection.** When an AI feature runs, some code or some person decides which data to include in the request. This is the most important control point, because it decides how much leaves the system.
4. **Prompt assembly.** Instructions, the user's question and the selected data are combined into the text sent to the model.
5. **Retrieval.** If the feature uses retrieval-augmented generation, passages are pulled from a search index. The index itself is a copy of the source documents, often split into chunks and converted to embeddings.
6. **Model processing.** The provider receives the request, runs the model and returns the output. The provider may log the request for abuse monitoring or debugging, for a period set by its terms.
7. **Output handling.** The answer is shown to a user, written into a record, sent as an email or used to trigger an action.
8. **Memory and logs.** The conversation, the output and any extracted facts may be stored for later use, for audit, or for improving the system.
9. **Deletion.** Each copy is eventually deleted, or should be.

For each stage, the map records what data is present, where it is physically stored, who can access it, how long it is kept, and which legal basis covers it.

### Controllers, processors and the agreement between them

Privacy law distinguishes the organization that decides why and how personal data is used, called the **controller**, from an organization that handles the data on the controller's behalf and under its instructions, called the **processor**. When a business sends customer data to an AI provider to generate summaries for the business, the business is normally the controller and the provider is a processor. In California's terms, the provider is usually a **service provider**.

The controller stays responsible. A business cannot hand its privacy duties to a vendor by signing up for a service. What it can do is put a **data processing agreement** (DPA) in place, which binds the processor to act only on the controller's instructions and to protect the data. Under the GDPR such a contract is mandatory. A good DPA with an AI provider covers:

- the purpose and duration of processing and the types of data involved;
- a commitment that the provider will use the data only to provide the service, and in particular whether it may use inputs or outputs to train or improve its models;
- how long prompts and outputs are retained, and how they are deleted;
- where the data is stored and processed, and the legal mechanism for any transfer abroad;
- the security measures the provider maintains;
- a list of **subprocessors**, the other companies the provider uses, with notice of changes;
- how quickly the provider will report a security breach;
- help with individual rights requests and with audits.

Providers usually offer different terms for consumer products and business products. Consumer tiers may by default use conversations to improve models, while business tiers typically do not. This is why a company policy that says "use only approved business accounts" is one of the most effective privacy controls available.

### International transfers

When data moves across borders, additional rules can apply. The GDPR restricts transfers of personal data out of the European Economic Area unless the destination has been recognized as offering adequate protection or the parties use approved safeguards such as standard contractual clauses. For an AI feature, the transfer question is often hidden: the business may be in one country, its customer in another, and the provider's data centre in a third. The data flow map should record the location of each stage so that this question can be answered.

### Worked example 1: Minimizing what a call summarizer sends

A software reseller uses an AI tool to summarize sales calls. For each of its 1,200 calls a month, the integration sends the call transcript plus the full CRM record of the contact. The CRM record has 22 fields. A review shows that only 6 of them help the summary: name, company, job title, deal stage, products of interest and last meeting date. Five of the 22 fields are sensitive or confidential: date of birth, home address, personal mobile number, the last four digits of a payment card, and a free-text "notes" field that sometimes contains health-related remarks such as a client's medical leave.

**Before the change**, each month the integration sends 1,200 × 22 = 26,400 field values to the provider, including 1,200 × 5 = 6,000 sensitive values.

**After the change**, the integration sends only the 6 needed fields: 1,200 × 6 = 7,200 field values a month, and no sensitive values at all. Exposure has fallen by 19,200 field values a month, a reduction of nearly three quarters, and the sensitive exposure has gone to zero.

There is a cost benefit too. The full CRM block averaged 450 tokens per request; the trimmed block averages 120 tokens. Across 1,200 calls, input falls from 540,000 tokens to 144,000 tokens a month, a saving of 396,000 tokens, and the summaries do not get worse because the removed fields never helped them.

The lesson is that minimization is not only a legal duty. It is usually the cheapest and most reliable privacy control, because data that is never sent cannot leak, cannot be retained by a vendor, and cannot be mentioned in an output.

## 4. Technical safeguards and how to measure them

Policies tell people what to do; technical safeguards make the right thing happen even when someone forgets. This section covers the main safeguards used with AI systems and, just as important, how to test whether they work.

### Redaction

**Redaction** removes or masks sensitive items in text before it is sent to a model or stored. A redactor might replace an email address with "[EMAIL]", a phone number with "[PHONE]" and a card number with "[CARD]". Simple redactors use patterns, such as the shape of an email address or a sixteen-digit number with the right check digit. More capable redactors use trained models to find names, addresses and other items that do not follow a fixed shape.

No redactor is perfect. It can miss items (a phone number written as "five five five, one two one two") and it can mask things that were not sensitive (a product code that happens to look like an account number). Redaction is therefore measured with the same two numbers used for any detection task:

- **Recall** is the share of real sensitive items the redactor caught. Low recall means leaks.
- **Precision** is the share of masked items that really were sensitive. Low precision means useful information is destroyed and users start to work around the tool.

### Worked example 2: Testing a redactor

A support team plans to redact customer emails before an AI assistant drafts replies. Before switching it on, they build a test set of 200 real emails, with names changed, and have two staff members mark every sensitive item by hand. They find 340 sensitive items, an average of 340 ÷ 200 = 1.7 per email.

The redactor masks 335 items. Of these, 323 are real sensitive items and 12 are false alarms.

- **Recall** = 323 ÷ 340 = 0.95, or 95 percent. The redactor misses 17 of the 340 items.
- **Precision** = 323 ÷ 335 ≈ 0.964, or about 96.4 percent. About 3.6 percent of masked items were harmless text.

Ninety-five percent sounds good until it is applied to real volume. The team handles 10,000 emails a month. At 1.7 sensitive items per email, that is 17,000 sensitive items a month. A 5 percent miss rate lets about 17,000 × 0.05 = 850 sensitive items a month through to the AI provider.

That number drives the decision. If the provider is covered by a strong DPA, keeps no data after processing and does not train on it, 850 items reaching it may be an acceptable residual risk, and the redactor is a useful extra layer. If the drafted replies are stored in a shared knowledge base that many staff can search, those 850 items a month accumulate into a growing pile of exposed data, and the team needs either a better redactor or a second control, such as blocking any reply that still contains a card-shaped number. Measuring recall turns a vague sense of safety into a figure that can be managed.

### Pseudonymization and anonymization

**Pseudonymization** replaces identifying details with a code, such as replacing "Maria Lopez" with "Customer 48213", while keeping a separate key that can link the code back to the person. It is a strong safeguard because the AI provider never sees the real identity. But pseudonymized data is still personal data under the GDPR, because the business holds the key and could re-identify the person.

**Anonymization** removes the possibility of identification altogether, so that neither the business nor anyone else can reasonably link the data back to a person. Truly anonymous data falls outside privacy law. True anonymization is harder than it looks: a combination of postcode, birth date and gender can single out many individuals, and a detailed purchase history can be as unique as a fingerprint. Treat any claim that data is "anonymous" with caution, and test it by asking whether someone with access to other data sources could work out who a record belongs to.

### Access control and permission-aware retrieval

An AI assistant should see only what the person using it is allowed to see. This principle, **least privilege**, sounds obvious but fails in a specific way with AI. A business builds a search index from all its documents so the assistant can answer questions, and the index is built with an administrator's access. Now any employee who asks the assistant a question can receive passages from documents they could never open directly, such as salary spreadsheets or board minutes.

The fix is **permission-aware retrieval**: every chunk in the index carries the access rules of the document it came from, and every search is filtered by the identity of the person asking, at the moment of the search. The same rule applies to multi-customer platforms, where one customer's data must never appear in another customer's answers. This separation is called **tenant isolation**, and it should be enforced in the data layer, not by asking the model to be careful.

### Encryption

Data should be encrypted **in transit**, using secure connections between every component, and **at rest**, in databases, file stores, backups and logs. Encryption at rest protects against theft of storage media and some kinds of breach, but it does not protect against a legitimate user or a connected AI assistant that is allowed to read the data. It is necessary but not sufficient.

### Retention and deletion

Every store of personal data needs a retention period, and the period needs to be enforced by the system, not by good intentions. Conversation logs, prompt logs, debugging traces, analytics events and backups are the usual offenders. A practical approach is to set a default retention period for each store in the data flow map, delete automatically when it expires, and keep a short list of documented exceptions, such as records needed for tax or legal holds.

Backups need special thought. They are essential for recovering from data loss, and a business that cannot restore its data has a different kind of disaster. But backups also hold copies of personal data, including data that has since been deleted from the live system on a person's request. A common, defensible approach is to keep backups for a limited period, protect them strongly, and make sure that if a backup is ever restored, previously processed deletion requests are applied again.

### Output filtering at a single choke point

Some data should never leave a system, whatever any component tries to do. Examples include internal identifiers, secret keys, other customers' data and raw database fields. Rather than relying on every screen and every API route to remember not to include them, a strong design passes all outgoing responses through one filter that removes forbidden fields before anything reaches a user. This is called a **choke point** control. Its strength is that it covers code written in the future, by people who never read the privacy policy. The SKA field case later in this chapter shows this design in use.

### Logging without over-logging

Logs are needed for security, debugging and accountability, and they are also one of the largest stores of personal data in most systems. Good practice is to log the facts needed to trace an event (who, what action, when, which record, which AI system and version) without logging full prompts and outputs by default. Where full content must be logged for a period, for example during testing, the period should be short and the access tightly limited.

## 5. Building a governance programme a small team can run

**AI governance** is the set of policies, roles, records and checks that make sure an organization uses AI deliberately, lawfully and safely. Large companies run governance through committees and dedicated staff. A small business needs the same functions in a lighter form. This section describes a programme that a team of five or fifty can run with a few hours a month.

### The AI use policy

The policy is the document every employee reads. It should fit on two pages and answer these questions:

- **Which tools are approved?** Name them, and say which account type to use (for example, company business accounts only).
- **What data may never be entered?** Typically: payment card numbers, government ID numbers, passwords and keys, health information, and any data a customer contract forbids sharing.
- **What output needs human review?** Typically: anything sent to a customer, anything that changes a financial or legal record, and anything published.
- **What must be disclosed?** When customers interact with an AI system, how is that made clear?
- **Who approves a new AI use?** Name a person, not a committee that never meets.
- **How do people report a problem?** Give a channel and promise that honest reports will not be punished.

The policy should be short enough to remember and specific enough to follow. "Use AI responsibly" is not a policy. "Never paste a customer's full email thread into an AI tool; use the approved summarizer in the CRM, which removes contact details" is.

### The AI system register

The register is a simple table, kept up to date, listing every AI system the business uses. For each system it records the name and vendor, the business purpose, the owner, the data it touches, the legal basis, the DPA status, where data is stored, the retention period, who can use it, the risk rating and the date of the last review. Many businesses discover, when they first build a register, that staff are using several AI tools nobody approved. That discovery is the point: the register turns hidden use into managed use.

### Risk assessment

Not every AI use needs the same scrutiny. A tool that drafts internal meeting agendas is low risk; a tool that screens job applicants is high risk. A simple and widely used method is to rate each system on **likelihood** that something goes wrong and **impact** if it does, each on a scale of 1 to 5, and multiply them.

Under the GDPR, processing that is likely to result in a high risk to people's rights requires a formal **data protection impact assessment** (DPIA) before it starts. Uses involving systematic evaluation of people, large-scale processing of sensitive data, or new technologies applied to personal data are typical triggers. A DPIA describes the processing, assesses whether it is necessary and proportionate, identifies the risks to individuals and records the measures taken to address them. Even where it is not legally required, the DPIA format is a useful discipline for any high-risk AI use.

### Worked example 3: Ranking an AI register by risk

A marketing agency with 30 staff builds its first AI register and rates five systems, using 1 for lowest and 5 for highest.

| System | Purpose | Likelihood | Impact | Score |
|---|---|---|---|---|
| A | Summarizes client calls into the CRM | 3 | 4 | 12 |
| B | Website chatbot answering prospect questions | 4 | 3 | 12 |
| C | Screens job applications and ranks candidates | 3 | 5 | 15 |
| D | Internal coding assistant for the web team | 2 | 3 | 6 |
| E | Drafts social media posts from briefs | 3 | 2 | 6 |

Each score is likelihood multiplied by impact: for system C, 3 × 5 = 15; for A, 3 × 4 = 12; for B, 4 × 3 = 12; for D, 2 × 3 = 6; and for E, 3 × 2 = 6.

System C comes first. Hiring decisions have serious effects on people, may involve sensitive data, and fall into a category that the EU AI Act treats as high risk. The agency decides that the tool may only suggest which applications a person should read first, that a person reviews every application regardless of its rank, and that it will run a DPIA and check whether rankings differ by group.

Systems A and B tie at 12. The agency breaks the tie by the number of people affected: the chatbot talks to strangers who have not agreed to anything, so B is reviewed second, with a check that it discloses it is an AI and does not collect more than a contact form would. A is reviewed third, using the minimization approach from Worked example 1.

Systems D and E score 6 and are reviewed once a year. The scoring is rough, and two reasonable people could rate a system differently by a point. That is acceptable. Its purpose is to make the agency spend its limited attention on the right systems first and to leave a record of why.

### Human review and the audit trail

For every AI-assisted action that affects a customer, the business should be able to answer later: what did the AI produce, who reviewed it, what was changed, and what was sent? This **audit trail** is what makes accountability possible. It need not be elaborate. A CRM that records "draft generated by assistant, edited and sent by J. Rivera at 10:42" is an audit trail. A process where AI drafts are copied into personal email and sent without a record is not.

### Incident response

An incident is any event where personal data may have been exposed, lost, altered or misused. AI-related incidents include an employee pasting customer data into an unapproved tool, an assistant showing one customer's data to another, a prompt injection that causes data to be sent out, and an unexpected training use discovered in a vendor's terms. The incident process should say who is told first, how the facts are gathered and preserved, how the risk to individuals is assessed, and who decides on notification. Practise it once, with a made-up scenario, before you need it.

### Frameworks worth knowing

Several published frameworks help organize AI governance. The **NIST AI Risk Management Framework**, published by the US National Institute of Standards and Technology, organizes the work into four functions: Govern, Map, Measure and Manage. The **ISO/IEC 42001** standard sets out requirements for an AI management system, in the same style as the well-known ISO/IEC 27001 standard for information security management. Neither is required for most small businesses, but both are useful checklists, and larger customers increasingly ask suppliers whether they follow one.

## 6. The regulatory landscape for business AI

This section describes the major laws a business using AI is likely to meet. It deliberately stays at the level of principles and obligations, because specific thresholds, deadlines and penalties change and vary by jurisdiction. Always check the current rules that apply to your business.

### The GDPR and AI

The GDPR applies to organizations established in the European Union and to organizations elsewhere that offer goods or services to people in the EU or monitor their behaviour there. The United Kingdom has its own version, often called the UK GDPR, which follows the same structure. Beyond the principles and rights already described, several provisions bear directly on AI.

- **Automated decision-making.** People have the right not to be subject to a decision based solely on automated processing, including profiling, that produces legal effects or similarly significant effects on them, such as refusing credit or rejecting a job application, except in limited circumstances. Where such decisions are allowed, the person is entitled to safeguards, including the ability to obtain human intervention, to express their view and to contest the decision. In practice, a business that wants to use AI in decisions like these should keep a meaningful human in the loop, which means a person with the authority and information to change the outcome, not one who rubber-stamps it.
- **Transparency about logic.** Where automated decisions of this kind are made, people must be given meaningful information about the logic involved and its likely consequences.
- **DPIAs** for high-risk processing, described in Section 5.
- **Breach notification.** A personal data breach must generally be reported to the relevant supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware of it, unless it is unlikely to result in a risk to people. Where the risk to people is high, they must be told as well.
- **Rights requests.** Requests from individuals must be answered without undue delay and generally within one month, which can be extended by up to two further months for complex or numerous requests.

### California and other US state laws

California's consumer privacy law, the California Consumer Privacy Act, as expanded by the California Privacy Rights Act, gives California residents the right to know what personal information a business collects and how it is used and shared, to delete it, to correct it, to opt out of its sale or sharing for cross-context behavioural advertising, and to limit the use of sensitive personal information. Businesses may not discriminate against people for using these rights. The law applies to businesses that meet certain size or data-volume thresholds, and it has its own regulator, the California Privacy Protection Agency, which has been developing rules on topics including automated decision-making technology. Other states have passed comprehensive privacy laws with broadly similar rights. A business should check which state laws apply to it based on where its customers live and its size.

### Sector laws

Some data is covered by laws specific to its sector. In the United States, health information held by healthcare providers, health plans and their business associates is governed by HIPAA, which requires a specific business associate agreement before a vendor, including an AI vendor, handles that information. Financial institutions have duties under the Gramm-Leach-Bliley Act. Online services directed at children under 13 must follow the Children's Online Privacy Protection Act. Employment, credit and insurance decisions are subject to anti-discrimination and fair-lending laws that apply whether a person or a model makes the decision.

### The EU AI Act

The European Union's AI Act, adopted in 2024 and applying in stages over several years, regulates AI systems themselves rather than only the data they use. It takes a risk-based approach:

- **Unacceptable risk.** A short list of practices is prohibited, such as social scoring of people and certain manipulative techniques that exploit vulnerabilities.
- **High risk.** AI used in specified areas, including employment and worker management, access to education, creditworthiness assessment and access to essential services, carries obligations such as risk management, data quality, documentation, logging, human oversight, accuracy and security.
- **Transparency obligations.** Systems that interact with people, such as chatbots, must make clear that the person is dealing with an AI, and AI-generated or manipulated content of certain kinds must be labelled.
- **Minimal risk.** Most other uses, such as spam filters or writing assistants, face no specific new obligations.

The Act also sets obligations for providers of general-purpose AI models. For most small businesses, the immediate practical points are to avoid prohibited uses, to recognize when a use falls into a high-risk area such as hiring, and to disclose AI interactions clearly.

### Contracts and customer expectations

Laws set the minimum. Customer contracts often go further. Enterprise customers commonly include clauses that forbid sending their data to third parties without approval, require notice of subprocessors, or forbid using their data to train AI models. A salesperson who pastes a client's confidential pricing into a public AI tool may breach a contract even where no privacy law applies. The governance programme should include a check of key customer contracts for AI-related restrictions.

### Worked example 4: Counting the breach clock

A training company serving clients in Germany discovers on Tuesday, 10 March 2026, at 14:30, that an AI assistant connected to its course platform has been showing parts of other learners' progress reports, including names and test scores, to any learner who asked about "class results." Its staff confirm the problem and become aware that personal data has been exposed at that time.

Under the GDPR, the company must notify its supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware. Counting 72 hours from Tuesday at 14:30 gives **Friday, 13 March 2026, at 14:30**. The clock runs on calendar hours, not working hours, so a weekend or holiday in the middle would not pause it.

The company's incident plan sets out what happens in those 72 hours:

- **Hours 0 to 2:** switch off the assistant's access to progress reports, preserve the logs, and notify the incident lead.
- **Hours 2 to 24:** use the logs to establish how many learners' data was shown, to whom and over what period.
- **Hours 24 to 48:** assess the risk to learners. Test scores and names are not special category data, but disclosure to fellow learners could cause embarrassment or harm, particularly in workplace training.
- **By hour 72:** submit the notification with the facts known so far. The rules allow information to be provided in phases if the investigation is not complete, so missing details are not a reason to miss the deadline.

The company also decides whether the risk to learners is high enough that they must be told directly, and it records its reasoning either way. The point of the example is that the 72-hour window is short, and a business that has never practised its incident process will spend most of it working out who should do what.

## 7. Choosing and managing AI vendors

Most businesses use AI through vendors, so vendor due diligence is where much of AI privacy is won or lost. The vendor's marketing page is not due diligence. The contract, the DPA, the security documentation and the actual product settings are.

### Questions to ask every AI vendor

1. **Training use.** Will our inputs, outputs or files be used to train or improve any model? Is that off by default for our account type, and is it written into the contract?
2. **Retention.** How long are prompts, outputs and uploaded files kept, including in logs and backups? Can we set a shorter period or request deletion?
3. **Location.** Where is data processed and stored? Which legal mechanism covers any international transfer?
4. **Subprocessors.** Which other companies handle our data, including the underlying model provider if the vendor is a wrapper around someone else's model?
5. **Access.** Which of the vendor's staff can see our data, under what circumstances, and is that access logged?
6. **Security.** Which independent audits or certifications does the vendor hold, such as SOC 2 reports or ISO/IEC 27001 certification, and will they share the report?
7. **Isolation.** If the product serves many customers, how is our data kept separate from theirs, including in search indexes and model memory?
8. **Breach notice.** How quickly will the vendor tell us about an incident affecting our data?
9. **Rights support.** Can we find and delete all data about a specific person when they ask?
10. **Exit.** If we stop using the service, can we export our data, and will the vendor confirm deletion?

### Wrappers and chains of vendors

Many AI products are built on top of a model supplied by another company. The product you buy may send your data to its own servers, then to a model provider, then to a logging service. Each link in the chain is a processor or subprocessor, and the weakest link decides the real level of protection. Ask for the full chain.

### Consumer tools at work

The most common AI privacy failure in small businesses is not a sophisticated attack. It is staff using personal accounts on consumer AI tools for work tasks, because those tools are convenient and the approved tool is slower or does not exist. Banning consumer tools rarely works on its own. Providing an approved tool that is as convenient, with proper business terms, and explaining why it matters, works much better.

### Case study: Harborline Insurance Brokers

Harborline Insurance Brokers is a fictional company, invented for this chapter. It is a regional broker with 40 staff that sells business insurance to small firms.

**The situation.** Harborline's account managers spend hours each week writing renewal summaries for clients: what coverage the client holds, what changed in the year, what claims were made and what the broker recommends. Several account managers began pasting client files into a free consumer AI tool on their personal accounts to draft these summaries. The files included claim details, some of which described employee injuries, along with business financial figures.

**The trigger.** A large client's procurement team sent Harborline a supplier security questionnaire that included the question: "Do you use AI tools to process our data? If so, list them and attach the relevant data processing terms." The operations manager could not answer. Nobody knew which tools were in use or what their terms said.

**What Harborline did.** The operations manager ran a two-week programme.

1. **Amnesty and inventory.** Staff were asked, with a promise of no penalty, which AI tools they had used for work and with what data. The register that resulted listed seven tools, four on personal accounts.
2. **Risk ranking.** Using the likelihood-times-impact method, the renewal summary use scored highest, because injury claim details are health-related information about third parties and the client contracts forbade unapproved third-party processing.
3. **An approved route.** Harborline bought business accounts for one AI service whose terms excluded training on customer data, set a short retention period, and signed a DPA. It built a template that pulled only the needed fields from the policy system, and replaced injured employees' names with role descriptions such as "warehouse employee."
4. **Policy and training.** A two-page AI use policy named the approved tool, listed forbidden data, and required account managers to review every summary before sending.
5. **Clean-up.** Staff deleted the client data from their personal AI histories, and the firm recorded the steps taken.
6. **Answer to the client.** Harborline answered the questionnaire honestly, including that unapproved use had occurred and what had been done about it.

**The result.** The client accepted the answer and renewed, and its procurement lead noted that Harborline's register and DPA made it one of the better-prepared suppliers they reviewed. The renewal summaries now take less time than before, because the template pulls the right fields automatically.

**What the case shows.** Unapproved AI use was a symptom of a real need. The fix was not to forbid AI but to give staff a better approved route, minimize the data it receives, and be able to prove what happens to client data. Governance turned a liability in a sales process into an advantage.

## 8. Individual rights in AI systems

Rights requests are where hidden copies of personal data come to light. A person who asks "what do you hold about me?" or "delete my data" is entitled to an answer that covers every system, including the AI ones.

### Finding the data

The data flow map from Section 3 is the starting point. For a typical AI feature, a complete search covers:

- the systems of record (CRM, billing, support desk);
- conversation histories and chat logs;
- AI memory stores, if the assistant remembers facts about users;
- search indexes and embedding stores built from documents that mention the person;
- prompt and output logs, both the business's own and the vendor's;
- records written by AI, such as call summaries;
- backups, handled under the backup policy.

A practical habit that makes this possible is to tag every stored item with the identifier of the person it relates to. A memory store where each entry is labelled with a user ID can be searched and cleared in seconds. A pile of untagged text chunks cannot.

### Deletion and trained models

Deleting a record from a database is straightforward. Removing a person's data from a model that was trained or fine-tuned on it is not, because the model's parameters do not store records in a form that can be found and removed. Research into "machine unlearning" exists, but for practical business purposes the reliable approach is to avoid training models on personal data in the first place, or to train only on data that has been properly anonymized, so that deletion requests never reach the model. If a business does fine-tune on personal data, it should document the legal basis, the retention plan and how it would respond to a deletion request, which may mean retraining without the person's data.

### Correction

The right to correct inaccurate data has a specific AI angle. If an assistant writes a wrong statement about a customer into the CRM, such as recording that the customer cancelled when they only paused, that is inaccurate personal data and must be corrected. If an AI system generates a false statement about a person in an answer, the business should be able to stop the system from repeating it. Grounding answers in verified records, rather than in generated text, makes correction possible because there is a single place to fix.

### Access and explanation

When a person asks to see their data, the answer should include data held in AI systems, in a readable form. Where AI has been used to make or support a decision about them, a clear explanation of what data was used and how it shaped the outcome is good practice everywhere and required in some situations.

## 9. Privacy threats specific to AI, and their controls

Beyond the ordinary risks of storing data, AI systems face several specific threats. Each has known controls.

**Cross-user leakage.** One user's data appears in another user's answer, through a shared memory, a shared search index or a cached response. *Controls:* tenant isolation in the data layer, per-user memory, and cache keys that include the user's identity and permissions wherever answers depend on private data.

**Prompt injection leading to data theft.** A document, email or web page contains instructions telling the assistant to collect private data and send it somewhere, for example by embedding it in a link. *Controls:* treat all retrieved content as data rather than instructions, limit the actions an assistant can take, require confirmation for actions that send data outside, and filter outputs for links or formats that could carry data out.

**Over-broad tool access.** An AI agent connected to email, CRM and file storage with full permissions can do far more damage than one connected with narrow, read-only permissions. *Controls:* least privilege, separate credentials per tool, short-lived tokens and logging of every tool call.

**Inference of sensitive traits.** A model can infer sensitive facts, such as health conditions or financial difficulty, from ordinary data like purchase histories. Using such inferences can be as harmful, and in some laws as regulated, as using the sensitive data directly. *Controls:* do not build features that infer special category traits without a clear legal basis and a DPIA, and test outputs for such inferences.

**Exposure of internal identifiers.** Internal record numbers, system keys and debug fields appear in responses because a developer returned a whole database record rather than selecting fields. Individually they may seem harmless, but they reveal how a system works and can help an attacker. *Controls:* return only selected fields, and add a single outgoing filter that strips forbidden fields from every response.

**Memorization in trained models.** A model trained on personal data reproduces it verbatim when prompted. *Controls:* train on anonymized or synthetic data, deduplicate training data (repeated passages are memorized more readily), and test the model by prompting it for known records before release.

### Ethics beyond compliance

Compliance is the floor. Several ethical questions go further than any law requires. Would the customer be surprised to learn how their data was used? Does a feature treat some groups of people worse than others, for example a lead-scoring model that consistently ranks prospects from certain postcodes lower? Is the business collecting data because it needs it, or because it might be useful one day? A business that asks these questions routinely tends to stay ahead of regulation, because regulation usually follows public discomfort.

## 10. Governance as a sales advantage

For a business that sells to other businesses, privacy and governance are not only costs. They shorten sales cycles. Enterprise buyers send security questionnaires, ask for DPAs, and increasingly ask specific questions about AI: which models are used, whether customer data trains them, how outputs are reviewed and how incidents are handled. A supplier that can answer within a day, with a register, a policy and a standard DPA ready to send, moves through procurement faster than one that needs three weeks to find out what its own staff are doing.

A practical **trust pack** for a small business might contain:

- the AI use policy;
- a summary of the AI system register showing which systems touch customer data;
- the list of processors and subprocessors;
- the standard DPA;
- a short description of security measures and any certifications or audit reports;
- the incident response commitment, including notification timing;
- a statement of whether customer data is used to train any model.

Keeping this pack current takes perhaps a day a quarter. It turns governance from an internal chore into something the sales team can hand to a prospect, and it reinforces the message that the business takes care with what it is given.

## SKA Field Case Study: Closing a privacy leak at one choke point

This case comes from the operation of Sales King Academy itself, the platform on which you are taking this course.

### The situation

Sales King Academy runs 26 specialist AI agents, a CRM, automations, a Beats wallet and a course catalogue on one platform. Behind the scenes, the platform keeps internal numbering and addressing records, called chain numbers, that it uses to organize its knowledge and the activity on the platform. Each user, by contrast, is identified to themselves by a 16-digit DNA-16 identifier. Each agent also keeps private memory for each user, separate from every other user's.

The platform's stated privacy rule is simple: a user sees only their own DNA-16, their own usage and their own Beats balance, and never the internal chain numbers.

### The problems it caused

On 7 October 2026, an audit of the platform found that the rule was not being kept everywhere. Internal chain numbers were appearing in some API responses and on some screens.

This was not a leak of another person's private information, but it was a real privacy and security problem for three reasons.

1. **It broke the platform's own promise.** A privacy rule that holds on most screens but not all of them is not a rule users can rely on.
2. **It exposed internal structure.** Internal identifiers show how a system is organized. They help anyone trying to probe a system for weaknesses, and they can make it easier to link activity together.
3. **It showed a design weakness.** The numbers appeared because individual routes and screens returned more than they needed. Fixing them one at a time would leave the next new route free to make the same mistake.

### What was done

Rather than patching each response, the platform added a **single outgoing filter**. Every response leaving the platform now passes through one point that strips internal chain numbers before anything reaches a user's screen or an API client. Users see only their DNA-16, their usage and their Beats.

This is the choke point control described in Section 4. Its value is that it does not depend on every developer, or every AI-assisted piece of code, remembering the rule. New features added later inherit the protection automatically.

The case also connects to two other design choices already in place on the platform. Each agent's memory is private per user, which is the tenant isolation principle from Section 4 applied at the level of individual people. And the chat source badges show users where each answer came from, which supports the transparency principle from Section 2.

### What it shows

The case illustrates four points from this chapter:

1. **Privacy by default is a design property, not a policy statement.** The written rule existed before the audit. What made it true was a control that enforces it.
2. **Choke points beat checklists.** One filter on everything outgoing is easier to test and harder to bypass than a rule every route must follow.
3. **Audits find what good intentions miss.** The leak was found because someone went looking, which is why the governance programme in Section 5 includes regular reviews.
4. **Minimization applies to outputs too.** Users were not harmed by having fewer fields on their screens. The removed numbers served no purpose for them.

### What remains open

Several questions are not settled by the filter alone, and they are good practice questions for any platform:

- How will the platform test, on each release, that the filter still catches everything, including fields added in future? A standing automated test that scans responses for the forbidden pattern would answer this.
- The platform recovered from a data loss in September 2026 using nightly database backups kept in a separate, access-controlled backup location. A governance review should confirm what those backups contain, who can access them and how long they are kept. **[founder figure: backup retention period and access settings]**
- How long are chat conversations and per-user agent memories retained, and can a user delete them? **[founder figure: conversation and memory retention policy]**
- How many responses contained chain numbers before the fix, and over what period? **[founder figure: count and duration of exposed responses]**

### Discussion questions

1. Why is a single outgoing filter more reliable than fixing each screen that showed internal numbers?
2. What would a choke point filter not protect against, and which other controls would cover those gaps?
3. If you were writing the platform's trust pack for an enterprise buyer, how would you describe this incident and its fix?

## SKA Lab: Find the privacy boundaries of a live AI platform

In this lab you use the live Sales King Academy platform to see the privacy principles in this chapter at work, and to test where its boundaries sit. You need a free account. Use only made-up information in any test data you enter; never enter real customer details, passwords or payment information into a test.

### Steps

1. **Sign in** at saleskingacademy.com. Look through your account, usage and wallet screens and list every piece of information the platform shows about you. Check whether your DNA-16 identifier, your usage and your Beats balance are shown, and whether you see any other long internal numbers.
2. **Ask an agent what it remembers.** Open a chat with one agent, such as Mentor, and tell it a harmless made-up fact, for example "My test company is called Bluefinch Tiles." Later in the same session, ask the agent what it knows about your company. Then open a different agent, such as Closer, and ask the same question. Record whether the second agent knows the fact. Compare your result with the platform's description of private per-agent, per-user memory.
3. **Check the source badges.** Ask an agent a question about this chapter's material, such as "What is data minimization?", and note the source badge. Then ask a question that needs live information, and note how that badge differs. Consider what each badge tells you about where your question's data went.
4. **Inspect the CRM with test data.** Open the CRM and create one contact using entirely fictional details. Note which fields the CRM asks for, and mark each field as needed or not needed for a simple sales follow-up, using the minimization test from Worked example 1.
5. **Review your vault connections.** Open the vault connections area, where customers connect their own tools. Without connecting anything new, list which connections are available and, for one of them, write down what data you would expect it to give the platform access to. Decide whether you would connect it for a business, and what you would check first, using the vendor questions in Section 7.
6. **Look at Automations.** Open Automations and review what an automation can do. For one automation you might build, write down what personal data it would touch and whether a person reviews its output before it reaches a customer.

### Record your results

| Step | What you checked | What you observed | Matches the privacy principle? (yes / no / cannot tell) | Notes |
|---|---|---|---|---|
| 1 | Data shown about you | | | |
| 2 | Memory across agents | | | |
| 3 | Source badges | | | |
| 4 | CRM fields needed | | | |
| 5 | Vault connection data | | | |
| 6 | Automation data and review | | | |

### Reflect

Write three to five sentences answering: Which privacy control on the platform did you find most convincing, and why? Where would you add a control if this were your business's system? What one change to your own team's AI use does this lab suggest?

## Summary

AI does not create privacy duties from nothing, but it makes data easier to copy, multiplies the places it is stored, lets outputs reveal inputs, and opens the door to hidden instructions. Privacy laws share a common set of principles: lawfulness, fairness and transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity and confidentiality; and accountability. Individuals hold rights to know, access, correct and delete their data and to object to certain uses, and those rights reach every AI system that holds a copy.

A data flow map shows where personal data enters, moves and rests in an AI feature, and where it leaves the business's control. The business usually remains the controller, the AI provider is usually a processor, and a data processing agreement should cover training use, retention, location, subprocessors, security and breach notice. Technical safeguards include minimization, redaction, pseudonymization, permission-aware retrieval, tenant isolation, encryption, enforced retention and a single outgoing filter. Each should be measured, as recall and precision measure a redactor.

Governance gives these controls a structure a small team can run: a short use policy, a register of AI systems, a likelihood-times-impact risk rating with DPIAs for high-risk uses, an audit trail of AI-assisted actions and a practised incident process. The GDPR, California's privacy rules, sector laws and the EU AI Act set the legal frame. Done well, governance shortens sales cycles as well as reducing risk. The Sales King Academy field case showed privacy by default enforced at one choke point, so the platform's rule no longer depends on every screen remembering it.

## Key terms

- **Personal data**: any information relating to an identified or identifiable person.
- **Sensitive personal data**: personal data whose misuse can cause serious harm, such as health or biometric data, which needs stronger justification and protection.
- **Purpose limitation**: the principle that data collected for one purpose should not be reused for an incompatible one.
- **Data minimization**: using only the personal data a task actually needs.
- **Storage limitation**: keeping personal data in identifiable form only as long as needed.
- **Accountability**: the duty to follow privacy principles and be able to prove it.
- **Controller**: the organization that decides why and how personal data is used.
- **Processor**: an organization that handles personal data on a controller's behalf and under its instructions.
- **Subprocessor**: another company a processor uses to handle the controller's data.
- **Data processing agreement (DPA)**: a contract binding a processor to protect data and act only on the controller's instructions.
- **Data flow map**: a record of where personal data enters, travels, is stored and leaves a system.
- **Redaction**: removing or masking sensitive items in text before it is sent or stored.
- **Recall**: the share of real sensitive items a detector finds.
- **Precision**: the share of flagged items that are truly sensitive.
- **Pseudonymization**: replacing identifiers with codes while keeping a key, so the data remains personal data.
- **Anonymization**: irreversibly removing the ability to identify a person from data.
- **Least privilege**: giving each user or system only the access it needs.
- **Permission-aware retrieval**: filtering search results by the asking user's access rights at the moment of the search.
- **Tenant isolation**: keeping each customer's data separate in a shared system.
- **Choke point control**: a single place all data must pass through, where a rule is enforced for everything.
- **AI system register**: a maintained list of AI systems in use, their data, owners, risks and reviews.
- **Data protection impact assessment (DPIA)**: a structured assessment of the risks of high-risk processing and the measures to address them.
- **Audit trail**: a record of who did what, when and with which system.
- **Automated decision-making**: decisions made by technology without meaningful human involvement.
- **Trust pack**: a ready set of policy, processor and security documents for customers' reviews.

## Review questions

1. What are the three categories of data a business must protect, and how do they differ?
2. Name four features of AI systems that create privacy risks ordinary software does not.
3. What are the seven core principles of the GDPR?
4. Why is consent often not the best legal basis for business AI processing?
5. In an AI feature's data flow, which stage is the most important control point, and why?
6. What is the difference between a controller and a processor?
7. List five things a data processing agreement with an AI provider should cover.
8. A redactor catches 470 of 500 real sensitive items and flags 20 harmless items as sensitive. What are its recall and precision?
9. Why is pseudonymized data still personal data under the GDPR?
10. What is permission-aware retrieval, and what failure does it prevent?
11. How is a likelihood-times-impact risk score calculated, and what is it used for?
12. Under the GDPR, how quickly must a personal data breach generally be reported to the supervisory authority?
13. What protection does the GDPR give people against solely automated decisions with significant effects?
14. What are the four risk levels in the EU AI Act?
15. Why is it hard to honour a deletion request for data used to train a model, and what is the practical solution?
16. In the SKA field case, why was a single outgoing filter chosen instead of fixing each screen?

## Answer key

1. Personal data relates to an identifiable person. Sensitive personal data is the subset whose misuse causes serious harm, such as health or biometric data, and needs stronger protection. Confidential business data, such as pricing or code, may contain no personal data but is protected by contracts and trade secret law.
2. Copying data into prompts is effortless; one request creates many lasting copies; outputs can reveal inputs; and instructions hidden in data can manipulate the system.
3. Lawfulness, fairness and transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity and confidentiality; and accountability.
4. Consent is valid only when the person has a genuine choice and can withdraw it easily. Withdrawal is hard to honour once data is built into a system, and most business uses fit contract or legitimate interests better.
5. Selection, where code or a person decides which data goes into the request, because it decides how much data leaves the business's systems.
6. The controller decides why and how personal data is used and remains responsible. The processor handles the data on the controller's behalf and only under its instructions.
7. Any five of: purpose and duration; whether data may be used for training; retention and deletion; storage location and transfer mechanism; security measures; the subprocessor list; breach notification timing; help with rights requests and audits.
8. Recall is 470 ÷ 500 = 94 percent. The redactor flagged 470 + 20 = 490 items, so precision is 470 ÷ 490, about 95.9 percent.
9. Because the business keeps a key that can link the codes back to real people, so the people remain identifiable.
10. It filters search results by the asking user's access rights at the moment of the search. It prevents an assistant from showing passages from documents the user is not allowed to open.
11. Each system is rated for likelihood of a problem and impact if it occurs, usually from 1 to 5, and the two are multiplied. The score ranks systems so the highest-risk ones are reviewed and controlled first.
12. Without undue delay and, where feasible, within 72 hours of becoming aware of it, unless it is unlikely to result in a risk to people.
13. The right not to be subject to such decisions, except in limited cases, and where they are allowed, safeguards including human intervention, the chance to express a view and the right to contest the decision.
14. Unacceptable risk (prohibited), high risk, limited risk with transparency obligations, and minimal risk.
15. A trained model does not store records in a form that can be found and removed. The practical solution is to avoid training on personal data, or to train only on properly anonymized data, or to retrain without the person's data if necessary.
16. A single filter enforces the rule on every response, including routes added in future, and is easier to test. Fixing screens one at a time would leave each new route free to repeat the mistake.

## Further reading

- European Union, Regulation (EU) 2016/679, the General Data Protection Regulation (GDPR).
- European Union, Regulation (EU) 2024/1689, the Artificial Intelligence Act.
- State of California, California Consumer Privacy Act, as amended by the California Privacy Rights Act.
- National Institute of Standards and Technology, *Artificial Intelligence Risk Management Framework (AI RMF 1.0)*.
- National Institute of Standards and Technology, *NIST Privacy Framework*.
- International Organization for Standardization and International Electrotechnical Commission, ISO/IEC 42001, *Artificial intelligence: Management system*.
- International Organization for Standardization and International Electrotechnical Commission, ISO/IEC 27001, *Information security management systems: Requirements*.
- Daniel J. Solove, *Understanding Privacy*.
- Shoshana Zuboff, *The Age of Surveillance Capitalism*.
