---
key: ai_tools_and_platforms
title: "AI Tools And Platforms"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-09-30"
chapter: "Sales King Academy, Volume 1, Chapter 2"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# AI Tools and Platforms

This chapter maps the tools a business actually uses to put AI to work. It sorts the crowded market into a handful of categories, explains what each category is for, and gives you a method for choosing tools that fit your business instead of the latest advertisement. You will learn how the pieces connect through APIs, automation platforms and tool protocols, how to compare tools on cost, quality, data handling and lock-in, and how to assemble a small, reliable stack. The chapter closes with a field case on the tool stack that runs Sales King Academy and a lab in which you build and test your own agent on the live platform.

## Learning objectives

By the end of this chapter you will be able to:

1. Name the seven main categories of AI tools and describe what each is for.
2. Explain the difference between a model, a platform and an application.
3. Compare closed and open-weight models on capability, cost, control and licensing.
4. Describe how tools connect through APIs, webhooks, automation platforms and tool protocols such as the Model Context Protocol.
5. Evaluate a tool against a structured scorecard covering fit, quality, cost, data handling, integration and lock-in.
6. Design a small AI tool stack with fallbacks for a sales and marketing team.
7. Manage the credentials that connect tools safely.
8. Build, instruct and test a custom agent on the Sales King Academy platform.

## 1. Models, platforms and applications

The AI market is noisy because three different things are sold under the same word, "AI". Separating them makes every buying decision easier.

A **model** is the trained system that does the work, such as a language model that writes text or a vision model that reads images. Models are made by a small number of companies and research groups. On its own, a model is just a capability; it has no screens, no user accounts and no connection to your business data.

A **platform** is the infrastructure that runs models and lets developers build with them. It provides access to one or more models through an API, handles scaling and billing, and often adds services such as storage, search and monitoring. Cloud providers and model makers both sell platforms.

An **application** is a finished product that people use to get a job done, such as a writing assistant, a CRM with AI features, or a meeting-notes tool. Applications are built on top of models and platforms, and add the screens, workflows, permissions and integrations that make the capability usable.

The same underlying model may reach you through all three routes: directly through the model maker's API, through a cloud platform that hosts it, and inside several applications. Knowing which layer you are buying tells you what you control. With an application you control little beyond settings; with a platform you control the workflow and data; with a model you run yourself, you control almost everything, including the work of keeping it running.

### Worked example 1: Same capability, three routes

A marketing agency wants AI to draft first versions of client blog posts.

- **Application route:** subscribe to a writing application with templates and a team workspace. Setup takes an afternoon. The agency cannot change how the tool gathers source material, and every writer pays a monthly seat price.
- **Platform route:** use a model through an API, connected to the agency's own document folder so drafts are grounded in each client's brand guide. Setup takes a developer a few days. The agency pays per use and controls the workflow.
- **Self-hosted route:** run an open-weight model on rented servers. The agency controls everything, including where data goes, but must maintain the servers and update the model.

For a ten-person agency, the platform route usually wins. The brand-guide grounding is the real source of quality, and it needs more control than an application offers but far less effort than self-hosting.

## 2. The seven categories of AI tools

Almost every AI product a business will meet falls into one of seven categories.

**1. General assistants.** Chat-based tools that answer questions, draft text, summarise documents and analyse files, offered by the major model makers and by large software companies. They are flexible and quick to adopt, and they are the right starting point for individual productivity. Their weakness for business processes is that, unless connected to company systems, they work only from what a person pastes in.

**2. Model APIs.** Direct programmatic access to models, charged per use. This is the building block for anything custom: a support assistant, a lead-scoring step, an automated report. Several companies offer closed models through APIs, and many open-weight models are available through hosting providers.

**3. Cloud AI platforms.** The major cloud providers, and edge networks such as Cloudflare, offer catalogues of models alongside storage, databases, search and security in one account. For a business already on a cloud, this keeps billing, data and access control in one place.

**4. AI inside business applications.** CRMs, email platforms, office suites, help desks and accounting tools now include AI features: drafting emails in the CRM, summarising meetings, suggesting next steps, answering customer questions from a help centre. These features are often the fastest win, because the data is already there.

**5. Automation and integration platforms.** Tools that connect applications through triggers and actions, such as "when a form is submitted, create a CRM contact and send a welcome email". Most now include AI steps that classify, extract or draft inside a workflow. They let non-developers build real automations.

**6. Knowledge and search tools.** Systems that index documents and make them searchable by meaning, including vector databases that store embeddings. They are the retrieval half of retrieval-augmented generation and decide how well an assistant can answer from your own material.

**7. Agents and agent builders.** Tools that let an AI system plan steps and take actions across other tools, together with builders that let a business configure its own agents with instructions, knowledge and permissions. They offer the most leverage and need the most care, as Chapter 1 explained.

Product names and features in all seven categories change quickly; a list of vendors written today will be out of date within months. The categories change slowly, which is why this chapter teaches them rather than a product list.

## 3. Closed and open-weight models

Models come in two broad kinds, and the choice affects cost, control and legal terms.

A **closed model** is available only through its maker's services. You cannot download it or inspect its parameters. Closed models from the leading companies are generally the most capable for difficult reasoning and writing tasks, are simple to use, and are maintained by the maker. In exchange, you depend on the maker's prices, availability and terms, and your data is processed on their systems.

An **open-weight model** has its trained parameters published, so anyone can download and run it under the terms of its licence. Open-weight models range from small ones that run on a laptop to large ones that need data-centre hardware. They let a business keep data on its own infrastructure, fine-tune the model on its own examples, and avoid per-token fees at high volume. The costs are hardware, engineering time and responsibility for keeping the system secure and up to date.

**Licences matter.** "Open" does not always mean "free for any use". Some open-weight models use standard permissive licences such as Apache 2.0, which allow commercial use, modification and redistribution with few conditions. Others use custom licences that restrict certain uses, require attribution, or limit very large companies. Before building a product on an open-weight model, read its licence as carefully as you would read a supplier contract.

**Output terms matter too.** Closed-model providers set terms for how outputs may be used. For example, some providers allow outputs to be used to train specialised models but not to train models that compete with the provider's own. If you plan to use generated text to train your own model, record which model produced which text and check the terms that applied.

### Worked example 2: Choosing a model type

A regional insurance broker wants to classify 50,000 incoming emails a month into twelve categories. The emails contain policy numbers and personal details.

- **Closed model via API:** best out-of-the-box accuracy, simple setup, but every email leaves the broker's systems. The broker must confirm that the provider's data terms and its own obligations to customers permit this.
- **Open-weight model, self-hosted:** emails stay in-house. A small open model fine-tuned on 2,000 hand-labelled emails can match a large closed model on a narrow, fixed task like twelve-way classification, at lower cost per email once running.

Because the task is narrow, the volume high and the data sensitive, the open-weight route is the stronger choice. It requires a licence permitting commercial use and someone responsible for maintaining it. If those are not available, the closed route with redacted emails (policy numbers and names removed before sending) is the safe alternative.

## 4. How tools connect

A business rarely uses one AI tool alone. Value comes from connecting AI to the systems that hold customers, orders, messages and documents. Four connection methods do most of the work.

### APIs

An **application programming interface** is a defined way for one program to ask another for data or actions: "give me the contact with this email address", "create a deal worth $5,000", "generate a reply to this message". Nearly every modern business application offers an API. The program making the call identifies itself with a credential, usually an API key or an OAuth token, and the receiving system checks that credential before doing anything.

### Webhooks

A **webhook** reverses the direction. Instead of your system repeatedly asking "has anything happened?", the other system sends a message the moment something happens, such as a payment completing or a form being submitted. Webhooks make automations react in seconds. They also create a security duty: anyone who learns the address could send fake events, so the receiving system must check a **signature**, a code the sender computes from a shared secret, and reject any message whose signature does not match. A webhook handler that skips this check is an open door.

### Automation platforms

Automation platforms let people connect applications without writing code, by choosing a **trigger** ("new row in a spreadsheet") and one or more **actions** ("send an email", "create a CRM record"). Most now include AI actions such as "classify this text" or "draft a reply". They are ideal for straightforward workflows between popular applications. Their limits appear with complex logic, high volumes (they usually charge per task run), and processes that need careful error handling.

### Tool protocols for AI

When an AI assistant or agent needs to use other tools, it needs a consistent way to discover what tools exist, what each one does and how to call it. The **Model Context Protocol**, usually called MCP, is an open standard for this, introduced in late 2024 and now supported by many assistants and applications. A business application that offers an **MCP server** exposes its functions, such as "search deals" or "create task", in a form any MCP-capable assistant can use. This turns connecting an assistant to a new system from a custom project into a configuration step.

### Design rules for connections

Whatever the method, four rules prevent most integration failures:

- **Expect failure.** Every call can time out or return an error. Set time limits, retry only when it is safe, and record what failed.
- **Make actions idempotent.** An idempotent operation has the same effect whether it runs once or several times. Use unique identifiers so a retried "create invoice" call cannot create two invoices.
- **Verify what comes in.** Check webhook signatures, validate data formats, and treat any text from outside as data, never as instructions to an AI.
- **Grant the least access.** Give each connection only the permissions its job needs: read-only where reading is enough, and access limited to specific records or folders where the tool allows it.

### Worked example 3: Wiring a lead workflow

A consulting firm wants every website enquiry to become a CRM contact, get an AI-drafted reply for review, and trigger a Slack message to the partner on duty.

1. The website form sends a **webhook** to the firm's automation platform when submitted. The platform checks the signature.
2. An **AI step** extracts company name, industry and stated need, and classifies the enquiry as consulting, speaking or other.
3. An **API call** searches the CRM for the email address. If found, it updates the record; if not, it creates one, using the form's submission ID as a unique key so a retry cannot create a duplicate.
4. A second **AI step** drafts a reply grounded in the firm's service descriptions and saves it as a draft email, not sent.
5. A **chat message** notifies the partner with a link to the draft.

Nothing reaches a client without a person pressing send, but the partner's work drops from fifteen minutes to one.

## 5. Evaluating a tool: the scorecard

Tool demonstrations are designed to impress. A scorecard keeps decisions grounded. Score each candidate from 1 (poor) to 5 (excellent) on six criteria, weighting them for your situation.

| Criterion | Questions to ask |
|---|---|
| **Fit** | Does it do the specific task we need, for our volume, in our language and industry? |
| **Quality** | How does it score on our own test set of real examples (Chapter 1, Section 7)? |
| **Cost** | What is the full monthly cost at our real volume, including seats, usage, add-ons and staff time? |
| **Data handling** | Where is our data processed and stored, how long is it kept, and is it used to train the vendor's models? |
| **Integration** | Does it connect to our CRM, email and documents through APIs, native integrations or MCP? |
| **Lock-in** | Can we export our data, prompts and configurations in usable formats if we leave? |

Two rules keep the scorecard honest. First, **test on your own data**, never only on the vendor's examples. Second, **price at your real volume**: a tool that is cheap for ten users may be expensive for fifty, and per-task automation pricing can rise sharply as usage grows.

### Worked example 4: Scoring two meeting-notes tools

A sales team of twelve compares two tools that record calls, write summaries and push next steps to the CRM. Weights reflect what matters most to this team.

| Criterion | Weight | Tool A | Tool B |
|---|---|---|---|
| Fit | 20% | 5 | 4 |
| Quality (20 real calls scored) | 25% | 4 | 4 |
| Cost at 12 users | 15% | 2 | 4 |
| Data handling | 15% | 3 | 5 |
| CRM integration | 15% | 5 | 3 |
| Lock-in (export) | 10% | 3 | 4 |
| **Weighted score** | | **3.80** | **4.00** |

Tool A has the better CRM integration, but Tool B is cheaper, keeps recordings in the team's region and exports cleanly. Tool B wins narrowly. The deciding question becomes whether Tool B's weaker CRM sync can be covered by a simple automation step. If it can, the choice is clear.

## 6. Designing a small stack

A **stack** is the set of tools a business uses together. The aim is the smallest stack that does the job reliably. Every added tool brings another bill, another login, another integration to maintain and another place for data to leak.

A practical stack for a small sales and marketing team usually has five layers:

1. **A system of record**: the CRM, holding contacts, companies, deals and activity. Everything else reads from and writes to it.
2. **A general assistant** for individual work: research, drafting, summarising and analysis.
3. **A model API or cloud AI platform** for custom workflows that need grounding in company material.
4. **An automation layer** connecting the CRM, email, forms, calendar and chat.
5. **A knowledge source**: one maintained folder or knowledge base of product details, pricing, policies, case studies and approved messaging, which grounds every AI step.

### Fallbacks

Any external service will sometimes be slow, down or rate-limited. For any AI step customers depend on, design a **fallback**: a second model or provider that can take over, or a clear degraded mode, such as queuing the task for later or routing it to a person. Fallbacks are cheap to plan and expensive to improvise during an outage.

### Worked example 5: A stack with fallbacks

A software company's inbound sales team designs its stack:

- **CRM** as the system of record.
- **Primary model** from a leading provider for drafting replies, grounded in the knowledge base.
- **Fallback model** from a second provider, used automatically if the primary fails twice in a row. Replies drafted by the fallback are marked for human review before sending.
- **Automation platform** for form-to-CRM routing, with failed runs sent to a shared inbox, not silently dropped.
- **Knowledge base** of approved product and pricing pages, owned by the head of marketing and reviewed monthly.

During a primary-provider outage, drafts keep flowing through the fallback with a review flag, and no enquiry is lost. The only extra cost is a second provider account that is rarely used.

## 7. Credentials: the keys to every connection

Every connection runs on a **credential**, such as an API key, OAuth token, password or webhook secret. Credentials are the most valuable and most mishandled items in any AI stack. A leaked key can let a stranger read customer data, send email in your name or run up large bills on your account.

Five practices prevent most credential problems:

1. **Store secrets in a secrets manager**, such as the encrypted secret store your hosting platform or automation tool provides, never in code, documents, spreadsheets, chat messages or AI prompts.
2. **Give each key the least permission** its job needs, and a separate key for each integration, so one leak does not expose everything.
3. **Record where each key is used.** When a key is rotated, every system that uses it must be updated, or connections break.
4. **Rotate keys** on a schedule and immediately after any exposure, such as a key pasted into a message or committed to a repository.
5. **Watch for expiry.** Many tokens expire. An expired token in a deployment or automation pipeline fails silently until someone notices that nothing has run.

The field case below includes an example of what happens when practice 3 and practice 5 are missed.

## 8. Costs, contracts and lock-in

AI tools are priced in several ways, often combined. Understanding the model is the only way to predict the bill.

- **Per seat:** a fixed monthly price per user. Predictable, but you pay for every seat whether it is used or not.
- **Per use:** charges per token, request, minute of audio, image or task run. You pay only for what you use, but costs rise with volume and can spike without warning.
- **Tiered plans:** bundles of features and usage limits. Watch what happens at the limit: some tools stop, some slow down, and some charge overage fees.
- **Add-ons:** AI features sold as extras on top of an existing subscription. These are easy to add and easy to forget.

### Controlling spend

Set a **budget cap** or alert on every usage-billed service, so a runaway automation or a leaked key cannot run up an unlimited bill. Review usage monthly against the value each tool delivers, and cancel seats nobody uses. For usage-based tools, the levers from Chapter 1 apply: send less text, route simple tasks to cheaper models, and reuse answers where possible.

### Contracts

Before committing to a tool, read five parts of its terms:

1. **Data use:** whether your inputs and outputs are used to train the vendor's models, and how to opt out.
2. **Data location and retention:** where data is stored and for how long, which matters for privacy laws and customer contracts.
3. **Output rights:** who owns what the tool produces, and any limits on how you may use it.
4. **Service levels:** what uptime the vendor commits to and what happens when it fails.
5. **Exit:** how to export your data and how long the vendor keeps it after you leave.

### Lock-in

**Lock-in** is the cost of leaving a tool. It grows when your data, prompts, workflows and staff habits exist only inside one vendor's product. Some lock-in is the price of convenience, but it should be a choice. Keep your own copy of key assets, such as prompts, knowledge documents, test sets and customer data, in systems you control, and prefer tools that export in standard formats.

### Worked example 6: The real monthly bill

A twenty-person marketing team adds up its AI costs, using illustrative prices.

| Item | Pricing | Monthly cost |
|---|---|---|
| General assistant, 20 seats at $25 | Per seat | $500 |
| Model API for campaign workflows, about 40 million tokens | Per use | $180 |
| Automation platform, 30,000 task runs | Tier plus overage | $240 |
| AI add-on in the email platform | Add-on | $150 |
| Staff time reviewing AI output, 30 hours at $40 | People | $1,200 |
| **Total** | | **$2,270** |

Two findings stand out. First, the largest cost is people, not software, which is typical and the reason review processes deserve design attention. Second, usage logs show 7 of the 20 assistant seats had no activity for two months; cancelling them saves $175 a month with no loss.

## 9. Running tools over time

Choosing a tool is the start, not the end. AI tools change more often than most software, and a tool that worked well in spring can drift by autumn.

**Model updates.** Providers update and retire models. An update can improve quality or change behaviour in ways that break a carefully tuned workflow. Where possible, pin a specific model version for important workflows, and re-run your test set before moving to a new one.

**Monitoring.** Track a few numbers for every AI workflow: volume, error rate, cost, and a quality measure such as the share of drafts accepted without edits. A sudden change in any of them is a signal to investigate.

**Ownership.** Every tool needs a named owner who holds its test set, watches its numbers, manages its credentials and decides when it should change or be retired. Tools without owners accumulate quietly and fail quietly.

**Documentation.** Keep a one-page record for every AI tool in the stack: what it does, who owns it, which systems and credentials it connects to, which model version it uses, where its test set lives, what it costs each month, and how to switch it off. The record takes twenty minutes to write and pays for itself the first time the owner is away, a credential expires, or an auditor, customer or new employee asks how a decision was made. Store these records together in the knowledge source, and update each one whenever the tool, its model or its connections change, so the documentation stays as current as the stack it describes.

**Retirement.** Review the stack twice a year. Remove tools that are unused, duplicated by another tool, or no longer worth their cost. Before retiring a tool, export its data, revoke its credentials and remove its integrations, so nothing continues to run or hold access unnoticed.

### Worked example 7: A silent drift

An online retailer uses an AI step to write product descriptions from supplier data. Quality is checked weekly by sampling ten descriptions against a rubric. One week the score drops from an average of 7.4 to 5.9 out of 8. Investigation shows the provider moved the workflow to a newer model version automatically, and the new version ignores the instruction to avoid superlatives. The owner pins the previous version, updates the instructions, tests the new version against the fixed test set, and moves to it only when it scores at least as well. Without the weekly sample, hundreds of off-brand descriptions would have gone live.

## 10. Matching tools to sales and marketing jobs

The categories in Section 2 map onto the everyday jobs of revenue teams. The table below is a starting point for building a stack around real work rather than around products.

| Job | Typical task types | Tool categories that usually fit |
|---|---|---|
| Research a prospect before a call | Retrieval, generation | General assistant; CRM AI features |
| Qualify and route inbound leads | Extraction, classification, action | Automation platform with AI steps; CRM |
| Draft first-touch and follow-up emails | Generation | CRM or email platform AI features; model API grounded in approved messaging |
| Summarise calls and log next steps | Extraction, generation, action | Meeting-notes tools integrated with the CRM |
| Forecast pipeline | Prediction | CRM forecasting features; analytics tools |
| Produce campaign content | Generation | General assistant; model API with brand guide grounding |
| Personalise web and email content | Classification, generation | Marketing automation platform with AI features |
| Answer product questions from customers | Retrieval, generation | Help-desk AI grounded in the knowledge base |
| Report on results | Retrieval, generation | Analytics tools; general assistant working from exported data |

Notice how often the CRM appears. The system of record is where AI in sales pays off most, because that is where the customer data lives. A team with messy CRM data gets poor results from every AI tool, however advanced. Cleaning the CRM is often the most valuable AI project a sales team can start with.

## 11. Reading vendor claims critically

AI marketing is full of claims that sound precise and mean little. A buyer who can question them saves money and avoids tools that fail in production.

### Common red flags

- **"No hallucinations" or "100% accurate."** No language-model product can guarantee this. A vendor who says so either misunderstands the technology or is overselling it. Better vendors describe how they reduce errors, such as grounding, citations and review steps, and how often errors still occur on realistic tests.
- **Accuracy figures without a test description.** "95% accurate" means nothing unless you know what was tested, on how many examples, how they were chosen and who judged the answers. Ask for the method, or better, test on your own data.
- **"Fully autonomous."** Autonomy is only valuable when it is controlled. Ask what the tool does when it is unsure, what limits can be set on its actions, and how every action is logged and reversed.
- **"Trained on your data."** This can mean the tool reads your documents when answering, which is usually what you want. It can also mean your data is used to train the vendor's models, which you may not want. Ask which one, and whether you can opt out.
- **Case studies with no numbers.** "Company X transformed its sales process" says nothing. Ask for the metric, the baseline, the time period and whether you can speak to the customer.
- **Pricing only for small teams.** If the public price stops at ten users, ask for the price at your real size and projected growth before investing time in a trial.

### Questions that separate strong vendors from weak ones

1. What happens when the tool does not know the answer?
2. Can we run a trial on our own data, scored by our own staff?
3. Where is our data processed and stored, and is it used to train any model?
4. Which model or models power the product, and how are model changes announced?
5. How do we export our data, configurations and history if we leave?

A vendor that answers these clearly and in writing is usually one worth testing further.

### Worked example 8: Decoding a sales pitch

A vendor tells a recruitment firm: "Our AI screening agent is 97% accurate, fully autonomous, and trained on your data, with no hallucinations."

The firm's operations lead asks the five questions and learns the following:

- The 97% figure came from 200 applications in another industry, judged by the vendor's own staff.
- "Fully autonomous" means it can reject applicants without review.
- "Trained on your data" means the firm's past hiring decisions would be used to fine-tune a model shared across customers.

Each answer raises a concern. Automated rejection of job applicants raises legal and fairness risks in many places. Fine-tuning on past decisions can copy past bias. Sharing that model across customers raises confidentiality questions. The firm asks for a trial on 300 of its own past applications, scored by its recruiters, with every rejection routed to a person. The vendor declines the review requirement, and the firm moves on to a vendor that accepts it.

## 12. A security review before connecting any tool

Connecting an AI tool to company systems gives it access to data and, often, the ability to act. A short security review before connection prevents most serious problems. It is the same review for a small automation as for a large platform, only shorter.

**Access and identity.** Can users sign in through the company's single sign-on, so access ends automatically when someone leaves? Can permissions be limited by role? Is there an administrator view of who has access?

**Data scope.** Which systems and records will the tool read, and which will it change? Grant access to the specific folders, pipelines or mailboxes it needs, not the whole account.

**Logging.** Does the tool record what it read and what it did, with times and user names, in a form you can export? Without logs, an incident cannot be investigated.

**Outside content.** Will the tool process content from outside the company, such as emails, web pages or uploaded files? If so, how does it prevent hidden instructions in that content from triggering actions (the prompt-injection risk from Chapter 1)?

**Vendor security.** Does the vendor publish security documentation, independent audit reports or certifications, and a contact for reporting problems? Larger buyers often require these; smaller ones should still ask.

**Kill switch.** Can the connection be switched off instantly, and do you know who can do it? Every AI tool that takes actions should have a documented way to stop it.

### Worked example 9: A fifteen-minute review

A small e-commerce business wants to connect an AI support agent to its help desk and order system. The owner reviews it:

| Check | Finding | Action |
|---|---|---|
| Access and identity | Single sign-on supported; two roles available | Give support staff "agent operator", owner "admin" |
| Data scope | Tool asks for full order-system access | Limit to read orders and create refund requests; no editing of customer records |
| Logging | Every reply and action logged, exportable | Export weekly to shared storage |
| Outside content | Reads customer emails | Confirm refund amounts come only from the order system, never from email text |
| Vendor security | Security page and audit report available | File the report with the contract |
| Kill switch | Toggle in admin settings | Owner and support lead named as the two people who may use it |

The review takes fifteen minutes and turns a broad, risky connection into a narrow, auditable one.

## 13. Configure or build: when a custom agent is worth it

Many teams reach a point where a general assistant is not enough, because the same instructions are pasted in every day, answers must come from company material, or work must flow into the CRM. The next step is usually a **configured agent**: an assistant with fixed instructions, a defined role, grounding in a specific knowledge source and a limited set of tools it may use. Most agent builders let non-developers set this up in an hour.

A configured agent is worth creating when three conditions hold:

1. **The task repeats.** The same kind of request comes in many times a week.
2. **The instructions are stable.** You can write down how the task should be done, including what to avoid.
3. **The knowledge is defined.** The agent can be pointed at a specific, maintained body of material.

A fully **custom-built agent**, with code, its own integrations and its own interface, is worth the extra effort only when a configured agent cannot reach the systems it needs, cannot meet the volume or cost targets, or must run inside the company's own infrastructure for data or contractual reasons. Build the configured version first; it teaches you what the custom version must do.

When you write an agent's instructions, include five things: its **role** ("you qualify inbound leads for a commercial cleaning company"), its **sources** ("answer only from the attached service and pricing pages"), its **boundaries** ("never quote a price not in the pricing page; never promise dates"), its **output format** ("reply in under 120 words, end with one question"), and its **handoff rule** ("if the request involves a complaint or a contract, say a team member will reply and stop").

### Worked example 10: Rewriting agent instructions

A commercial cleaning company sets up an agent to answer enquiries from its website. The first version of its instructions reads:

"You are a helpful assistant for our cleaning company. Answer customer questions and try to get them to book."

In testing against ten real enquiries, the agent performs poorly. It quotes prices the company does not offer, promises same-day service the company cannot provide, answers a complaint cheerfully as if it were a sales enquiry, and writes replies of 300 words or more. Scored on accuracy, completeness and tone, it earns 31 out of 60.

The owner rewrites the instructions using the five parts of good agent instructions:

- **Role:** "You answer enquiries for a commercial cleaning company serving offices, clinics and retail units in one metropolitan area. Your goal is to answer accurately and, when the enquiry is a fit, offer a free site visit."
- **Sources:** "Answer only from the attached service list, service-area list and pricing guide. If the answer is not in them, say a team member will confirm."
- **Boundaries:** "Never quote a price that is not in the pricing guide. Never promise a start date or same-day service. Do not discuss competitors."
- **Output format:** "Reply in under 120 words. Use plain language. End with one question that moves the conversation forward, such as asking for the property size or a convenient time for a site visit."
- **Handoff rule:** "If the message is a complaint, mentions an existing contract, or asks for anything outside the sources, reply that a team member will respond within one business day, and stop."

On the same ten enquiries, the rewritten agent scores 52 out of 60. Its remaining errors involve two enquiries from just outside the service area, where the service-area list was unclear. Adding a line to the list fixes both. As in earlier examples, the biggest gains came from clear instructions and good source material, not from a more powerful model.

## SKA Field Case Study: The tool stack behind Sales King Academy

This case describes the tools that run Sales King Academy, the platform on which you are taking this course, and the decisions behind them.

### The stack

Sales King Academy is built and operated by one founder. Its stack is deliberately small:

- **Hosting and compute:** a single serverless program on Cloudflare's network, with two small databases, several key-value stores for fast lookups and settings, and Cloudflare's hosted AI models. Everything runs in one account under one bill.
- **Language models:** chat replies are produced by open-weight models hosted on Cloudflare, with a second model family as a fallback. Where a question can be answered from stored course material or exact records, the platform answers from those directly and marks the reply's source.
- **Vision:** when a buyer uploads a payment receipt screenshot, a vision model from one provider reads it first; if that fails, a vision model hosted on Cloudflare reads it instead.
- **Email:** a transactional email service sends outreach and notifications from the company's own domain, at roughly 95 emails a day, and an inbound handler captures replies.
- **Payments:** a card payment link is used for one purpose only, buying Beats, the platform's prepaid credits. Everything else on the platform is priced in Beats.
- **Code and deployment:** the platform's code lives in a private repository. Every change pushed to the main branch triggers an automated deployment. The course material lives in a separate repository, where free automated jobs rebuild study packs and training data every week.
- **Tool protocol:** the platform runs its own MCP server, so MCP-capable assistants can use functions such as giving an SKA agent a goal, looking up course material, and searching the connected CRM.
- **Customer-owned deployment:** customers can run agents they build on their own Cloudflare accounts. Their credentials are stored encrypted in a personal vault and used only for their own deployments, so the compute bill is theirs, not the platform's.

### Decisions that shaped it

**Fallbacks at every AI step.** Each AI function has a second option: a second chat model, a second vision model, and for receipts a final human review. When a provider fails, the task degrades to the next option instead of stopping.

**Verification ladder for payments.** Receipt approval runs strongest-first. The payment processor's own records are checked where available; if not, an AI read of the receipt is accepted only for small amounts within a daily limit; everything else waits for the founder. Every receipt is recorded once, with unique receipt numbers and image fingerprints, so the same payment can never be credited twice.

**Signed webhooks, failing closed.** An early version of the payment webhook accepted messages when no signing secret was configured, which meant anyone who knew the address could have sent a fake "payment completed" event and received credits. It was changed to reject every message unless the signature is present and correct. This is Section 4's "verify what comes in" rule, learned the hard way.

**One system of record for money.** Purchases once updated an older balance field while charges came from a newer ledger, so a buyer could pay and not see their credits arrive. Both were moved onto the ledger, and the balance screen now reads only from it.

### The credential lesson

In July 2026, the credential that allowed the automated pipeline to deploy code expired. Deployments stopped, but nothing announced the failure clearly: the code repository kept accepting changes, and the site kept running the old version. It took about two weeks to discover that nothing new had shipped. The same credential was stored in three places — two secrets in the code repository and one in the platform itself — and all three had to be replaced for deployments to resume.

The fix combined two practices from Section 7: record every place a credential is used, and watch for expiry. It also added a habit that goes beyond this chapter's list: after every deployment, check the live site itself, not just the pipeline's success badge, because the badge and the reality can disagree.

### What remains open

The platform runs on a free hosting plan with a strict processing limit per request, which affects some AI features, as Chapter 1's field case describes. The payment processor's automatic confirmation also depends on credentials not yet configured, so receipts currently rely on the AI read and founder review.

Results for the founder to add: [FOUNDER TO ADD: monthly cost of each tool in the stack] [FOUNDER TO ADD: outreach reply rate from the 95 emails a day] [FOUNDER TO ADD: number of receipts approved automatically versus by review].

### Discussion questions

1. Which single tool in this stack would cause the most damage if it failed without a fallback, and what fallback would you add?
2. Why does sending customers' agents to their own Cloudflare accounts change the platform's cost structure?
3. What check would have caught the expired deployment credential within a day instead of two weeks?

## SKA Lab: Build and test your own agent

In this lab you configure a custom agent on the Sales King Academy platform and test it against a small test set, applying Sections 5 and 13. You need a signed-in account. Check any price shown on screen before confirming an action.

### Steps

1. **Choose a job.** Pick one repeating task from your own work, such as answering questions about your services, qualifying leads, or drafting follow-up emails.
2. **Write a test set.** Before building anything, write five realistic requests the agent will receive, including one vague request and one it should refuse or hand off. Write the answer you would consider correct for each.
3. **Open Build an Agent** from the menu. Choose the base agent closest to your job, such as a sales or marketing specialist.
4. **Configure it** using the five parts from Section 13: role, sources, boundaries, output format and handoff rule. Give it a name and greeting.
5. **Test it.** Open a chat with your agent and send your five test requests, one at a time. Score each reply 0 to 2 on accuracy, completeness and tone, and note whether it followed the handoff rule.
6. **Improve and re-test.** Change the instructions to fix the weakest answer, then re-run all five requests. Record whether the total score improved and whether any other answer got worse.
7. **Explore connections (optional).** Open Connections & API and read the "where to find this key" guidance for one service your business uses. Notice where credentials are stored and that they are never shown back to you. If you have your own Cloudflare account, you can use "Run on my Cloudflare" on your agent to deploy it there.

### Record your results

| Test request | Expected answer (short) | Score, first version (0-6) | Score, improved version (0-6) | Notes |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 (vague) | | | | |
| 5 (refuse or hand off) | | | | |
| **Total** | | | | |

### Reflect

In three to five sentences: Which instruction change made the biggest difference, and why? Would you trust this agent with real customers today? If not, what would it need first?

## Summary

AI tools come in three layers: models that do the work, platforms that run them, and applications that people use. Seven categories cover most of the market: general assistants, model APIs, cloud AI platforms, AI inside business applications, automation platforms, knowledge and search tools, and agents. Closed models offer capability and simplicity, while open-weight models offer control, subject to their licences. Output terms also matter whenever generated text will be reused, including for training.

Tools create value when connected to business systems through APIs, signed webhooks, automation platforms and tool protocols such as MCP, following four rules: expect failure, make actions idempotent, verify what comes in, and grant least access. A weighted scorecard tested on your own data and priced at real volume keeps choices honest. A small stack built around the CRM, with fallbacks and one maintained knowledge source, beats a large collection of overlapping tools. Credentials need a secrets manager, least permission, a record of where each is used, rotation, and expiry checks.

Costs include seats, usage, add-ons and — usually the largest — staff time, so budgets, caps and regular reviews matter, as do contract terms on data, outputs and exit. Tools must be run over time with pinned versions, monitoring, a named owner and planned retirement. The Sales King Academy field case showed these ideas in a real stack: fallbacks at every AI step, a verification ladder for payments, webhooks that fail closed, and a costly lesson about an expired credential.

## Key terms

- **Model**: a trained system that performs a task such as writing text or reading images.
- **Platform**: infrastructure that runs models and lets developers build with them.
- **Application**: a finished product people use, built on models and platforms.
- **Closed model**: a model available only through its maker's services.
- **Open-weight model**: a model whose parameters are published and can be run by others under a licence.
- **Permissive licence**: a licence, such as Apache 2.0, allowing commercial use and modification with few conditions.
- **API (application programming interface)**: a defined way for one program to request data or actions from another.
- **Webhook**: a message a system sends to another the moment an event happens.
- **Signature (webhook)**: a code computed from a shared secret that proves a webhook came from the real sender.
- **Automation platform**: a tool that connects applications through triggers and actions.
- **Model Context Protocol (MCP)**: an open standard letting AI assistants discover and use tools in other systems.
- **Idempotent**: having the same effect whether performed once or several times.
- **Least access**: giving each connection only the permissions its job requires.
- **Stack**: the set of tools a business uses together.
- **Fallback**: a second option that takes over when the primary tool fails.
- **Credential**: a key, token, password or secret that authorises a connection.
- **Lock-in**: the cost and difficulty of leaving a tool.
- **Configured agent**: an assistant set up with fixed instructions, sources, boundaries and tools.

## Review questions

1. What is the difference between a model, a platform and an application?
2. What are the seven categories of AI tools described in this chapter?
3. What are two advantages and two costs of using an open-weight model?
4. Why must a webhook handler check a signature before acting?
5. What does it mean for an action to be idempotent, and why does it matter for retries?
6. What six criteria make up the tool evaluation scorecard?
7. Why is the CRM called the system of record in a sales stack?
8. What five practices prevent most credential problems?
9. In Worked example 6, what was the largest monthly cost, and what does that suggest?
10. What five things should a configured agent's instructions include?

## Answer key

1. A model does the work, a platform runs models and provides developer access, and an application is the finished product people use.
2. General assistants, model APIs, cloud AI platforms, AI inside business applications, automation and integration platforms, knowledge and search tools, and agents and agent builders.
3. Advantages: data can stay on your own infrastructure, and there are no per-token fees at high volume. Costs: hardware and engineering time, and responsibility for security and updates. Its licence must also permit your use.
4. Without it, anyone who learns the address could send fake events, such as a false payment, and the system would act on them.
5. It has the same effect whether it runs once or many times. This lets failed calls be retried without creating duplicates such as double invoices.
6. Fit, quality, cost, data handling, integration and lock-in.
7. It holds the authoritative customer, company and deal data, and every other tool reads from and writes to it.
8. Use a secrets manager, grant least permission with a separate key per integration, record where each key is used, rotate keys regularly and after exposure, and watch for expiry.
9. Staff time reviewing AI output, at $1,200. Review processes deserve careful design, because people usually cost more than software.
10. Role, sources, boundaries, output format and handoff rule.
