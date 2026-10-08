---
key: ai_business_process_automation
title: "AI Business Process Automation"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-10-08"
chapter: "Sales King Academy, Volume 1, Chapter 1"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# AI Business Process Automation

This chapter teaches you how to find, measure, redesign and automate the repeatable processes that run a company: taking in orders, entering invoices, approving spending, onboarding customers, producing reports and answering routine requests. You will learn to tell the steps that need simple rules from the steps that need AI to read or judge text, to set confidence thresholds that send uncertain cases to people, to build an automation in safe stages, and to prove its value with numbers instead of impressions. The chapter closes with a field case from the operation of the Sales King Academy platform and a lab on the live site, so the methods are tied to systems you can see and use.

## Learning objectives

By the end of this chapter you will be able to:

1. Define a business process in terms of its trigger, inputs, steps, outputs, owner and measures, and explain what automating it means.
2. Distinguish rule-based automation, robotic process automation, workflow and integration platforms, and AI-driven steps, and choose the right one for each step of a process.
3. Rank candidate processes for automation using a weighted scoring method based on volume, effort, stability, data readiness and risk.
4. Map a process and measure its baseline, including touch time, cycle time, process cycle efficiency, error rate, cost per item and work in progress.
5. Redesign a process before automating it, removing and simplifying steps so that automation does not lock in waste.
6. Design exception handling, including confidence thresholds chosen by comparing the cost of errors with the cost of human review.
7. Plan a staged rollout from suggestion to supervised action to monitored autonomy, with audit trails, limits and rollback.
8. Build a business case with monthly savings, payback period and first-year return, and identify the legal, ethical and workforce questions an automation raises.

## 1. What a business process is, and what automating it means

A **business process** is a repeatable sequence of work that turns an input into an output of value to someone. A supplier's invoice arrives and, some days later, the supplier is paid and the books are correct. A prospect fills in a form and, some time later, a salesperson has a qualified conversation with them. A new customer signs a contract and, some weeks later, they are using the product. Each of these is a process, whether or not anyone has ever written it down.

Every process can be described with six elements:

- **Trigger**: the event that starts it. An email arrives, a form is submitted, a date is reached, a record changes status.
- **Inputs**: the material the process works on. An invoice PDF, a form's fields, a contract, a spreadsheet.
- **Steps**: the individual pieces of work, each done by a person or a system. Read, check, enter, decide, approve, send, file.
- **Outputs**: what the process produces. A payment, a CRM record, a welcome email, a report.
- **Owner**: the one person accountable for how well the process performs. Not everyone who touches it, but the one who answers for it.
- **Measures**: the numbers that say whether it is working. How long it takes, how much it costs, how often it goes wrong.

Writing these six elements down for a process is the first discipline of automation. Many businesses discover at this point that a process they thought was simple has no clear trigger (people start it whenever they remember), no owner (three people each think someone else is responsible) and no measures at all. Automation cannot fix that confusion. It can only make it faster.

**Automation** means a system performs some or all of the steps without a person doing them. It is useful to think of automation as a spectrum, not a switch:

1. **Manual**: people do every step.
2. **Assisted**: software helps a person do a step faster, such as a template, a pre-filled form or an AI draft.
3. **Partial**: software does some steps on its own, and people do the rest, usually the decisions.
4. **Supervised**: software does the whole process, but a person reviews and approves before anything final happens.
5. **Monitored**: software does the whole process and acts on its own for ordinary cases; people handle exceptions and check samples.

Most well-run automations live at levels 3 to 5, and different steps of the same process often sit at different levels. A process that runs entirely at level 5, with nobody looking, is rarely a sign of maturity. It is usually a sign that nobody is checking.

### Why processes are worth automating at all

The case for automation rests on four kinds of gain:

- **Capacity.** Work that took staff hours is done in seconds, so the same team handles more volume. A business whose core processes are automated can grow revenue faster than it grows headcount.
- **Speed.** A customer who receives a quote in five minutes instead of two days is more likely to buy. Speed often matters more to revenue than the labour saved.
- **Consistency.** Software applies the same rule the same way every time. Two staff members applying a discount policy will drift apart; a well-built rule will not.
- **Visibility.** An automated process records what happened at every step, so the business can measure it and find problems. A manual process often leaves no trace except the final output.

There is also a cost side that business cases often miss: automations must be designed, built, tested, monitored and maintained, and they fail in ways manual work does not. A person who sees something odd usually stops and asks. A badly designed automation keeps going.

## 2. The automation toolbox: rules, robots, workflows and AI

Not every step of a process needs AI, and using AI where a simple rule would do makes a process slower, more expensive and harder to audit. Before you choose tools, learn the main families.

### Rule-based automation

**Rule-based automation** follows explicit instructions a person wrote: if a form's country field is Canada, assign the lead to the Toronto team; if an invoice total is above a limit, send it for approval; every Monday at 8:00, email the sales report. Rules are cheap, fast, predictable and easy to audit. Their weakness is that they handle only the situations their author anticipated. A rule that looks for the word "invoice" in an email subject misses every email that says "bill", "statement" or nothing at all.

### Robotic process automation

**Robotic process automation (RPA)** is software that operates other software the way a person does: it clicks buttons, types into fields and copies data from one screen to another. RPA is useful when an old system has no proper way to connect to it, so the only route in is through its screens. It is fragile, because a change to a screen layout can break the robot, and it should be treated as a bridge to a better integration rather than a permanent design.

### Workflow and integration platforms

A **workflow engine** coordinates the steps of a process: it knows which step comes next, who is responsible, what is waiting for approval and what has timed out. An **integration platform** connects systems through their **APIs** (application programming interfaces, the defined ways one program can ask another to read or write data) so that, for example, a new row in a form tool creates a contact in a CRM. Many modern tools combine both functions. They are the backbone of most automations: the AI steps plug into a workflow, not the other way round.

A related idea is the **webhook**: a message one system sends to another the moment something happens, such as "this deal just changed stage". Webhooks let processes react to events immediately instead of checking for changes on a schedule.

### AI steps

AI is the right tool for steps that require reading, interpreting or producing language or other unstructured input. In process automation, AI steps usually fall into five types:

- **Classification**: deciding what category something belongs to. Is this email a complaint, an order or a question? Is this expense travel, meals or software?
- **Extraction**: pulling structured fields out of unstructured material. The total, date, supplier and line items from an invoice; the renewal date from a contract; the budget mentioned in a call transcript.
- **Summarization**: condensing a long input into the points a person needs. A ten-page tender reduced to its requirements and deadlines.
- **Generation**: producing a draft. A reply to a customer, a product description, a handoff note.
- **Judgment support**: comparing an input against a policy and flagging problems, such as a contract clause that differs from the company's standard terms.

The combination of extraction and classification applied to documents is often called **document understanding** or intelligent document processing. It is the single most common AI step in back-office automation, because so much business information still arrives as PDFs, scans and emails.

### Choosing the right tool for each step

A practical rule: **use the simplest tool that handles the real variety of the input.** If the input is already structured, such as a form with fixed fields, a rule is enough. If the input varies in wording and format, AI earns its place. If the decision carries money or legal weight, the decision itself should be a rule applied to the facts the AI extracted, not a judgment the AI makes freely.

| Step | Input variety | Stakes | Best tool |
|---|---|---|---|
| Route a web form by its "department" drop-down | None, fixed values | Low | Rule |
| Route a free-text email to the right team | High | Low to medium | AI classification with a fallback to a person |
| Read totals and dates from supplier invoices | High (many layouts) | Medium | AI extraction, checked against purchase orders |
| Decide whether an invoice needs approval | None once fields are extracted | High | Rule on the extracted total and supplier |
| Draft a reply to a delivery complaint | High | Medium | AI generation, grounded in the order record, reviewed |
| Copy data into an old system with no API | None | Low | RPA, as a temporary bridge |

Notice the pattern in the invoice rows. AI reads the document, but the approval decision is a rule applied to what it read. This division, AI for reading and rules for deciding, is the most reliable design pattern in business automation.

## 3. Choosing which processes to automate

Most businesses have far more candidate processes than they can automate at once. Choosing badly wastes months: the first project is too hard, it stalls, and the organization concludes that automation does not work. Choosing well produces an early success that funds and justifies the next project.

### The selection criteria

Five criteria predict whether a process is a good candidate:

- **Volume**: how often it runs. A process that runs 2,000 times a month repays design effort far faster than one that runs twice a month.
- **Effort per item**: how much staff time each run takes. High volume with very low effort (a ten-second task) may not be worth automating; moderate volume with high effort may be.
- **Stability**: how often the process and its inputs change. A process that is rewritten every quarter will break its automation every quarter.
- **Data readiness**: whether the inputs are digital, accessible and reasonably consistent, and whether the systems involved can be connected.
- **Risk**: what a mistake costs. Lower risk makes a better first candidate, because it allows the team to learn without serious consequences.

Some practitioners add a sixth criterion, **strategic value**: whether speeding the process up changes something customers notice, such as quote turnaround or onboarding time. A process that customers feel directly may be worth automating even when the labour savings alone would not justify it.

### Worked example 1: Scoring three candidates

A wholesale distributor with 40 staff wants to choose its first automation project. The operations manager lists three candidates and scores each criterion from 1 (poor candidate) to 5 (strong candidate). For risk, a high score means low risk. The weights reflect what the business cares about most: volume 30 percent, effort per item 20 percent, stability 20 percent, data readiness 15 percent and risk 15 percent.

| Process | Volume (0.30) | Effort (0.20) | Stability (0.20) | Data readiness (0.15) | Risk (0.15) |
|---|---|---|---|---|---|
| Supplier invoice entry | 5 | 4 | 4 | 4 | 4 |
| Quote follow-up emails | 4 | 2 | 3 | 3 | 5 |
| Customer contract review | 2 | 5 | 2 | 2 | 1 |

The weighted score is each score multiplied by its weight, then added up.

- Supplier invoice entry: 5 × 0.30 + 4 × 0.20 + 4 × 0.20 + 4 × 0.15 + 4 × 0.15 = 1.50 + 0.80 + 0.80 + 0.60 + 0.60 = **4.30**
- Quote follow-up emails: 4 × 0.30 + 2 × 0.20 + 3 × 0.20 + 3 × 0.15 + 5 × 0.15 = 1.20 + 0.40 + 0.60 + 0.45 + 0.75 = **3.40**
- Customer contract review: 2 × 0.30 + 5 × 0.20 + 2 × 0.20 + 2 × 0.15 + 1 × 0.15 = 0.60 + 1.00 + 0.40 + 0.30 + 0.15 = **2.45**

Invoice entry wins clearly. Contract review scores high on effort, because each contract takes a lawyer a long time, but its low volume, poor stability and high risk make it a poor first project. That does not mean it should never be automated; it means it should come later, once the team has experience, and probably at the "assisted" level, where AI flags unusual clauses for a lawyer rather than approving anything itself.

The scoring method is simple on purpose. Its value is not precision but discipline: it forces the team to state its reasons and compare candidates on the same terms, instead of automating whatever the most senior person happens to find annoying.

### Building an automation portfolio

Once the first project succeeds, treat automation as a **portfolio**: a ranked list of all candidates, reviewed every quarter, with each project funded in order of value and readiness. Portfolio thinking prevents two common failures. The first is the scattered pilot problem, where many departments each start a small experiment and none reaches production. The second is the stranded project, where an automation is built and then abandoned because nobody budgeted for its maintenance. A portfolio includes the running cost and owner of every automation already live, not just the new ideas.

## 4. Mapping and measuring the current process

You cannot improve what you have not described, and you cannot prove an improvement you did not measure beforehand. Mapping and measuring the current process, the "as-is" state, comes before any design work.

### Mapping methods

Three mapping methods cover most needs.

**SIPOC** is a one-page summary listing the Suppliers, Inputs, Process (in five to seven high-level steps), Outputs and Customers of a process. It is a quick way to agree on where a process starts and ends before going into detail.

A **swimlane diagram** draws each step as a box in a horizontal lane belonging to the person, team or system that does it. Arrows show the flow. Whenever an arrow crosses from one lane to another, there is a **handoff**, and handoffs are where most delays and errors live: work waits in an inbox, information is lost, or each side assumes the other has done a check.

A **value stream map**, a method that comes from lean manufacturing, adds time to the picture. For each step it records the **touch time** (the time someone actually works on the item) and the **wait time** (the time the item sits between steps). The usual finding is startling: an item that takes six days to get through a process may receive only a few minutes of actual work.

Process maps can also be drawn in a formal notation. **BPMN** (Business Process Model and Notation), a standard maintained by the Object Management Group, defines shapes for events, tasks, decisions and flows so that maps can be read the same way by different teams and loaded into some workflow tools. For a small business, a clear swimlane drawn on a whiteboard is usually enough; the notation matters less than the honesty of the map.

### How to gather the facts

Maps drawn in a meeting room describe how people believe the process works. Maps drawn from evidence describe how it actually works. Four sources of evidence are worth using:

- **Walk the process.** Sit with the people who do each step and watch real items go through. Ask what they do when something is missing or wrong; the exceptions are where the real process hides.
- **Sample the records.** Take 30 to 50 recent items and trace each one through emails, system timestamps and files. Note how long each step took and how often items went backwards.
- **Count the volume.** Pull monthly counts from the systems involved, including seasonal peaks.
- **Use system logs where they exist.** Many systems record when a record was created and changed. The technique of reconstructing a process from these event records is called **process mining**, and specialized tools exist for it in larger organizations.

### The baseline measures

Six measures make up a useful baseline:

- **Volume**: items per period.
- **Touch time**: total working minutes per item, added across all steps.
- **Cycle time**: elapsed time from trigger to output, including all waiting.
- **Process cycle efficiency (PCE)**: touch time divided by cycle time. It shows what share of the elapsed time is spent actually working on the item.
- **First-pass yield**: the share of items that go through without any rework or correction. Its opposite is the **error rate** or rework rate.
- **Cost per item**: touch time multiplied by the loaded hourly cost of the people involved, plus any rework, plus system costs.

A seventh measure, **work in progress (WIP)**, is the number of items inside the process at any moment. A useful relationship from queueing theory, known as **Little's Law**, ties three of these measures together for a stable process: average work in progress equals the average arrival rate multiplied by the average cycle time. If you know two of the numbers, you can calculate the third, and a large WIP is a visible sign of a slow process.

### Worked example 2: Measuring the invoice process

The distributor from Worked example 1 maps its supplier invoice process. It receives 1,200 invoices a month, over 20 working days. The value stream map records these touch times per invoice:

| Step | Who | Touch time (minutes) |
|---|---|---|
| Open email, save PDF, log receipt | Accounts assistant | 1 |
| Key invoice into the accounting system | Accounts assistant | 4 |
| Match to purchase order and delivery note | Accounts assistant | 3 |
| Approval by budget holder | Department manager | 2 |
| Schedule payment | Finance lead | 1 |
| **Total touch time** | | **11** |

Sampling 40 recent invoices shows that the average invoice takes 6 working days from arrival to scheduled payment, and that 4 percent need correction (wrong amount keyed, wrong supplier, missing purchase order), each taking about 20 minutes of rework. The loaded cost of staff time, including wages, taxes and benefits, averages $32 an hour.

**Process cycle efficiency.** A working day is 8 hours, or 480 minutes, so 6 working days is 6 × 480 = 2,880 minutes. PCE = 11 ÷ 2,880 = 0.0038, or about **0.38 percent**. Less than half of one percent of the elapsed time is spent working on the invoice; the rest is waiting.

**Labour cost.** Each invoice takes 11 minutes, which costs 11 ÷ 60 × $32 = about **$5.87**. For 1,200 invoices a month: 1,200 × 11 ÷ 60 × $32 = **$7,040**.

**Rework cost.** 4 percent of 1,200 is 48 invoices. 48 × 20 minutes = 960 minutes, or 16 hours, which at $32 an hour is **$512** a month.

**Total monthly baseline cost:** $7,040 + $512 = **$7,552**.

**Work in progress.** Invoices arrive at 1,200 ÷ 20 = 60 per working day. By Little's Law, average WIP = 60 per day × 6 days = **360 invoices** in the process at any time. That number explains why suppliers phone to ask about payments and why staff spend time searching inboxes for invoices "somewhere in approval".

The baseline tells the team three things before any technology is chosen. First, the largest single block of touch time is keying (4 minutes), which is a strong candidate for AI extraction. Second, the long cycle time comes from waiting, mostly for approval, which automation of data entry alone will not fix. Third, the business now has numbers against which any change can be judged.

## 5. Redesign before you automate

The most expensive mistake in process automation is automating a process exactly as it is. Every unnecessary step, duplicate check and pointless handoff becomes code that must be built, tested and maintained, and the waste is now harder to see because a machine is doing it. Redesign comes first.

### The four questions

A long-standing improvement method asks four questions of every step, in this order, often remembered by the letters **ECRS**:

1. **Eliminate**: does this step need to exist at all? Many steps survive because "we have always done it", or because they once caught a problem that no longer occurs.
2. **Combine**: can this step be merged with another, so that one person or system does both in one pass and a handoff disappears?
3. **Rearrange**: would a different order remove waiting or rework? Checking that a purchase order exists before keying an invoice, rather than after, avoids keying invoices that will be rejected.
4. **Simplify**: can the step be made easier, with a standard form, a clearer rule or fewer options?

Only after these questions have been asked should the team decide what to automate. The order matters: automation is the last tool, not the first.

### Common redesign moves

- **Standardize the input.** If suppliers send invoices in fifty formats to twelve email addresses, set up one address for invoices. Ask large suppliers to send structured electronic invoices if they can. Every reduction in input variety makes automation cheaper and more accurate.
- **Move checks to the start.** Validate an order, a form or an invoice when it arrives, while the sender is still easy to reach, instead of discovering the problem days later.
- **Replace approvals with rules where the risk allows.** Many approvals exist only because no one wrote down the conditions under which approval is automatic. "Invoices under $500 that match an approved purchase order are approved automatically" removes thousands of approval clicks a year without adding risk, because the purchase order was already approved.
- **Set time limits on waiting.** If an approval has not happened in two days, remind; after four, escalate. Waiting without limits is how cycle times grow.
- **Remove duplicate data entry.** If the same customer details are typed into three systems, connect the systems so the details are entered once.

### Designing the "to-be" process

The redesigned process, the "to-be" state, should be drawn as a new map with the same rigour as the old one, and each step should be labelled with its intended level of automation and its tool. For the invoice process, a redesign might look like this:

| Step | Before | After redesign |
|---|---|---|
| Receive | Twelve inboxes, manual saving | One invoice address; system saves and logs automatically |
| Key data | Manual, 4 minutes | AI extraction of supplier, date, total, tax and line items |
| Match | Manual, 3 minutes | Rule-based match to purchase order and delivery records |
| Approve | Every invoice to a manager | Rule: matched invoices under $500 approved automatically; others to the manager with a two-day reminder |
| Exceptions | Discovered late, ad hoc | Unmatched or low-confidence invoices go to a review queue with the reason shown |
| Schedule payment | Manual | Automatic on approval, with a weekly payment run reviewed by the finance lead |

The redesign does more than add AI. It removes inboxes, changes an approval policy and adds a reminder. Those non-technical changes may cut the cycle time more than the AI step does.

## 6. How AI steps work inside a process

An AI step inside an automation behaves differently from a person and differently from a rule. Understanding those differences lets you design around them.

### Inputs and preparation

AI models work on text, images or audio. A scanned invoice is first converted into text by **optical character recognition (OCR)**, which turns an image of characters into machine-readable characters; many modern models can read the image directly. Either way, quality of input drives quality of output. A blurry phone photo of a crumpled receipt will produce more errors than a clean PDF, and no model choice fixes that. Part of good design is improving inputs at the source.

### Structured outputs

For an AI step to feed a workflow, its output must be structured: named fields with defined types, not free prose. The instructions to the model specify the exact fields (supplier name, invoice number, invoice date, currency, total, tax), the format of each (a date as year-month-day, a total as a number with two decimals) and what to return when a field is not present (an empty value, not a guess). The workflow then checks the output: is the date a real date, is the total a number, do the line items add up to the subtotal? These **validation checks** catch many model errors before anything happens downstream.

### Confidence

Many AI tools return a **confidence score** with each output: a number, often between 0 and 1, expressing how sure the system is. Confidence scores are useful but must be treated with care. A score of 0.92 does not necessarily mean the answer is right 92 percent of the time; the relationship between a tool's scores and its real accuracy has to be measured on your own data. A tool whose scores match its real accuracy is said to be **calibrated**. You can also build your own confidence signals: agreement between two independent methods (the model's total matches the sum of the line items), agreement with a system of record (the supplier exists and the purchase order matches), and the presence of every required field.

### Determinism and repeatability

A rule gives the same output for the same input every time. An AI model may not, especially at higher temperature settings. For process automation, set the model to its most consistent behaviour, keep the instructions fixed and versioned, and where the same input may be processed more than once, store the first result and reuse it rather than asking again. Consistency is a feature: an invoice that is classified one way on Monday and another way on Tuesday will confuse staff and auditors alike.

### Safe repetition and failures

Automated steps fail: a system is briefly unavailable, a request times out, a quota is reached. A good design distinguishes two kinds of step. A step that only reads, such as looking up a supplier, can safely be **retried**. A step that changes something, such as scheduling a payment, must be **idempotent**, meaning that repeating it has the same effect as doing it once, usually because each action carries a unique identifier and the receiving system ignores duplicates. Without idempotency, a retried payment step can pay a supplier twice. This principle appears again in the Sales King Academy field case later in this chapter, where repeatable restores mattered as much as the backups themselves.

## 7. Exception handling and confidence thresholds

Every automation meets cases it cannot handle: a missing field, an unknown supplier, a document in an unexpected language, a model output that fails validation. **Exception handling** is the design of what happens to those cases. It is not an afterthought; in many processes it is where most of the design effort should go, because exceptions are where errors and customer frustration concentrate.

### The parts of an exception path

A complete exception path has five parts:

1. **Detection**: a defined condition that marks an item as an exception, such as a confidence score below a threshold, a failed validation check, or a mismatch with a system of record.
2. **Routing**: a queue owned by a named person or team, not a general inbox.
3. **Context**: the item arrives with the reason it was flagged, what the automation extracted and what it was unsure of, so the reviewer does not start from scratch.
4. **Resolution**: the reviewer corrects and completes the item, and the process continues from that point automatically.
5. **Learning**: corrections are recorded, so the team can see which kinds of exception are common and fix their causes, whether by improving instructions, adding a rule or asking a supplier to change a format.

A process with no exception path does not have fewer exceptions. It has hidden ones: items that silently fail, sit in an error log nobody reads, or go through with wrong data.

### Choosing a confidence threshold

The **confidence threshold** is the score above which the automation acts on its own and below which it routes the item to a person. Setting it is a business decision, not a technical one, because it trades two costs against each other. A low threshold sends fewer items to people, saving review time, but lets more errors through. A high threshold catches more errors but sends more work to people. The right threshold is the one with the lowest total cost, and you find it by testing on real items with known answers.

### Worked example 3: Setting the threshold for invoice extraction

The distributor runs its chosen AI extraction tool on a test set of 1,000 past invoices whose correct values are already known. For three candidate thresholds, it counts how many invoices would have been processed automatically and how many of those automatic results contained an error.

The business estimates that an error that slips through costs about $40 to find and fix later (staff time, supplier calls, sometimes a duplicate or wrong payment to reverse). A human review of a flagged invoice takes about 5 minutes; at a loaded cost of $30 an hour for the reviewer, that is $2.50 per review. For simplicity, the example assumes reviewed invoices are corrected and leave no further errors.

| Threshold | Processed automatically | Errors among automatic | Error rate among automatic | Sent to review | Cost of errors | Cost of reviews | Total cost |
|---|---|---|---|---|---|---|---|
| 0.80 | 850 | 25 | 2.94% | 150 | $1,000 | $375 | $1,375 |
| 0.90 | 720 | 9 | 1.25% | 280 | $360 | $700 | $1,060 |
| 0.95 | 560 | 3 | 0.54% | 440 | $120 | $1,100 | $1,220 |

The calculations for the 0.90 row: errors cost 9 × $40 = $360; reviews cost 280 × $2.50 = $700; total $1,060. The same method gives the other rows.

The 0.90 threshold has the lowest total cost, **$1,060 per 1,000 invoices**. Dropping to 0.80 saves review time but lets far more errors through; rising to 0.95 catches a few more errors at the price of many more reviews. Two points matter beyond the arithmetic. First, the answer depends on the business's own costs: if an error were much more expensive, perhaps because it caused a payment to the wrong bank account, the higher threshold would win, and some errors, such as changed bank details, should always go to a person regardless of confidence. Second, the test must be re-run when the tool, its instructions or the mix of suppliers changes, because the error counts will change too.

### Exceptions that should never be automated

Some conditions should always route to a person, whatever the confidence score, because the cost of a single error is too high or because the situation is a known pattern of fraud. In accounts payable, a classic example is a request to change a supplier's bank details, a common route for invoice fraud: the change should be confirmed through a separately known contact, never through the email that requested it. Every process has its own list of such conditions, and writing it down is part of the design.

## 8. Rolling out in stages, with controls

An automation should earn trust step by step, not receive it on the first day. A staged rollout reduces risk and produces the evidence needed to justify each step up.

### Stage 1: Shadow mode

The automation runs alongside the existing manual process but takes no action. Its outputs are recorded and compared with what staff actually did. Shadow mode costs almost nothing in risk and quickly reveals where the automation disagrees with people, and sometimes where people were inconsistent with each other.

### Stage 2: Suggest and approve

The automation prepares each item, such as an extracted invoice ready to post, and a person approves, corrects or rejects it with one action. This stage already saves time, because checking is faster than keying, and every correction becomes evidence about where the automation is weak. Track the **acceptance rate** (the share of suggestions approved without change) by field and by type of item.

### Stage 3: Act on high-confidence cases

Items above the chosen threshold, and passing every validation check, go through automatically. The rest go to the exception queue. Introduce this stage gradually: one supplier group, one region or one category first.

### Stage 4: Monitored operation

The automation runs as the normal process. People handle exceptions and check a regular **sample** of automatic items, for example 20 a week chosen at random, so that a slow drift in quality is caught before it becomes expensive. The monitoring dashboard shows volume, share automated, exception rate, error rate found in samples, cycle time and cost.

### Controls that apply at every stage

- **Audit trail.** For every automated action, record the input, the version of the instructions and model used, the output, the confidence, the decision taken and the time. An audit trail lets errors be found, explained and reversed, and it is often required by auditors and regulators.
- **Limits.** Set hard caps that a fault cannot exceed: maximum value of automatic approvals per day, maximum number of emails sent per hour, maximum spend on model usage per day. When a limit is reached, the automation pauses and alerts the owner.
- **Segregation of duties.** The same automation, or the same person, should not be able both to create a supplier and to pay it. This long-standing financial control applies to software as much as to staff.
- **Kill switch and rollback.** The owner must be able to stop the automation at once and return to the manual process. Test this before go-live, not during an incident.
- **Change control.** Treat instructions, thresholds and rules as versioned configuration. Any change is tested against the test set before it goes live, and the previous version can be restored.
- **Backups that are tested.** Automations create and change records at speed, so a fault can damage data at speed. Regular backups, and regular practice at restoring them, are part of the design, not an IT afterthought.

### Case study: Northgate Freight Brokers onboards carriers faster

*This case uses a fictional company to illustrate the methods in this chapter. Northgate Freight Brokers is not a real business, and its figures are invented for teaching.*

Northgate is a freight broker that matches shippers with independent trucking companies, called carriers. Before a carrier can haul a load, Northgate must collect and check its documents: operating authority, insurance certificate, tax form, bank details for payment and a signed carrier agreement. Northgate onboards about 300 new carriers a month, and each onboarding took an average of 45 minutes of staff time spread over three days, or 300 × 45 ÷ 60 = 225 staff hours a month. Loads were lost to competitors because a carrier was not yet approved when a shipment needed to move.

**Mapping.** A swimlane map showed four handoffs between the sales desk, the compliance team and accounts. Documents arrived by email, text message and fax-to-email, in every format imaginable. The longest waits came from missing documents discovered only after the first review, and from insurance certificates that had to be confirmed with the insurer.

**Redesign first.** Before any AI, Northgate replaced scattered email with a single upload page that asked for each document by name and refused to submit until all were present. It moved the bank-detail step to the end, after all other checks, and made any change to bank details require a phone call to a number already on file. It also merged two review steps that checked the same insurance dates.

**AI steps.** AI extraction then read each uploaded document: the authority number, insurance limits and expiry dates, and the carrier's legal name. Rules compared the extracted values with Northgate's requirements (minimum insurance limits, name matching across documents, expiry at least 30 days away). Any mismatch, missing field or low-confidence result went to a compliance reviewer with the reason shown.

**Rollout.** Northgate ran two weeks in shadow mode, then four weeks of suggest-and-approve, during which reviewers accepted most extractions unchanged but corrected insurance expiry dates often enough that the team added a rule to double-check that field. Only then did it allow automatic approval of carriers whose documents passed every check.

**Results.** Average staff time per onboarding fell to 18 minutes, so 300 onboardings took 300 × 18 ÷ 60 = 90 hours a month instead of 225, a 60 percent reduction. More important to the business, most carriers were approved the same day. Northgate kept a weekly sample of 15 automatic approvals for human review and kept bank-detail changes as a permanently manual step.

**Questions to consider.** Which part of the improvement came from redesign and which from AI? Why did Northgate deliberately leave bank-detail changes outside the automation? What would you monitor to detect if the automation began approving carriers it should not?

## 9. Proving value: the business case

An automation should be justified with numbers before it is built and judged with numbers after it goes live. The business case compares the cost of the process before and after, and sets that difference against the one-time cost of building the automation.

### The parts of a business case

- **Baseline cost**: the monthly cost of the current process, from the measurements in Section 4, including rework.
- **Future running cost**: staff time for reviews, exceptions and sampling; the cost of remaining errors; software, model usage and infrastructure; and the owner's time for monitoring and maintenance.
- **One-time cost**: design, build, testing, training, data cleanup and the productivity dip during rollout.
- **Monthly saving**: baseline cost minus future running cost.
- **Payback period**: one-time cost divided by monthly saving, in months.
- **Return on investment (ROI)** over a period: total savings in the period minus the one-time cost, divided by the one-time cost.

Add benefits that are real but harder to price, such as faster supplier payments that earn early-payment discounts, faster quotes that win more sales, or fewer customer complaints. List them separately rather than mixing estimates of uncertain value into the hard numbers, so readers can judge each kind of benefit on its merits.

### Worked example 4: The invoice automation business case

The distributor uses its measurements to build a business case for the redesigned invoice process with AI extraction at the 0.90 threshold from Worked example 3.

**Baseline**, from Worked example 2: **$7,552** a month.

**Future running cost**, per month, for 1,200 invoices:

- At the 0.90 threshold, 72 percent are processed automatically: 0.72 × 1,200 = 864 invoices. The other 336 go to review.
- Review time: 336 × 5 minutes = 1,680 minutes = 28 hours. The team adds 10 hours a month for sampling, monitoring and maintenance, for 38 hours. At $32 an hour: 38 × $32 = **$1,216**.
- Remaining errors: the test set showed 9 errors per 1,000 invoices, so 1,200 invoices produce about 9 ÷ 1,000 × 1,200 = 10.8 errors a month. At $40 each: **$432**.
- Software, model usage and integration platform fees, as quoted for this example: **$600**.
- Total future running cost: $1,216 + $432 + $600 = **$2,248**.

**Monthly saving**: $7,552 − $2,248 = **$5,304**.

**One-time cost**: design, build, testing and training, quoted at **$24,000**.

**Payback period**: $24,000 ÷ $5,304 = **4.5 months** (4.52 to two decimal places).

**First-year ROI**: twelve months of savings is 12 × $5,304 = $63,648. ROI = ($63,648 − $24,000) ÷ $24,000 = 1.652, or **165.2 percent**.

The case is strong, but a careful reader would check three things. First, the review time per invoice: if reviews take 8 minutes rather than 5, the saving falls. Running the numbers again with pessimistic assumptions, called a **sensitivity analysis**, shows how much the case depends on each estimate. Second, the error cost: if it is underestimated, the threshold choice and the saving both change. Third, the saved staff time: a saving is real only if the time is used for something valuable, such as handling more volume without hiring, or moving staff to supplier negotiations. If the hours simply disappear into idle time, the business has paid for an automation without capturing its value.

### Measuring after go-live

The same measures used for the baseline are tracked after go-live: volume, touch time, cycle time, error rate found in samples, cost per item and work in progress. Compare them with the business case at one, three and six months. A business case that is never checked teaches nothing; one that is checked improves the next estimate.

## 10. Governance, law, ethics and people

Automation raises questions beyond cost and speed. A business that ignores them takes on risks its business case does not show.

### Data protection

Automations move data between systems and often send it to outside AI providers. Before going live, check four things:

- **Purpose**: is the data being used for a purpose the customer or employee would expect, and that your privacy notice describes?
- **Minimization**: does each step receive only the fields it needs? An invoice extractor does not need the supplier's full contact history.
- **Provider terms**: what does the AI provider do with the data you send? Check its terms on retention and on whether your data may be used to train its models, and choose settings or contracts that match your obligations.
- **Location and transfer**: some laws restrict sending personal data across borders. If you operate in such markets, check where your providers process data.

In the European Union and the United Kingdom, the General Data Protection Regulation (GDPR) gives people rights concerning decisions based solely on automated processing that have legal or similarly significant effects on them, such as some credit or employment decisions. Other jurisdictions have their own rules, and the rules are changing as governments respond to AI. A business should check the requirements that apply in its markets, and should design processes that make decisions about people so that a human can review them and the person affected can ask for an explanation.

### Fairness

When an automation makes or shapes decisions about people, such as screening job applicants, setting credit terms or prioritizing customer complaints, test its outcomes across groups. An AI step can reproduce patterns in the historical data it learned from, including unfair ones. Keep a person accountable for decisions with significant effects, record the reasons for decisions, and review outcomes regularly.

### Security

An automation that reads outside content, such as emails and uploaded documents, can be attacked through that content. Text hidden in a document may try to instruct an AI step to change its behaviour, a technique called prompt injection. Design so that outside content can never set the important values of an action: an invoice's payee comes from the supplier record, not from text in the invoice. Give each automation only the permissions it needs, store credentials in a secrets manager rather than in instructions or logs, and log every action.

### Records and accountability

Many industries require records to be kept for set periods, and many audits require evidence of who approved what. Automated approvals must leave the same quality of evidence as manual ones: which rule approved the item, what values it saw, which version of the rule applied. "The system did it" is not an acceptable answer to an auditor or a customer.

### People and jobs

Automation changes people's work, and how a business handles that change decides whether the automation succeeds. Staff who fear for their jobs have every reason to make an automation look bad. Staff who helped design it, understand what it does and see their own work become more interesting tend to improve it. Good practice includes involving the people who do the work in mapping and redesign, being honest about how roles will change, investing in training for the new tasks (exception handling, monitoring, supplier relationships), and giving each automation a named owner whose job includes its quality. Automation that frees experienced staff to handle the difficult cases is usually worth more than automation that simply removes them, because the difficult cases are where the business's reputation is made.

## 11. Running and improving automations over time

An automation is not a project that ends at go-live. It is a running system that degrades unless someone looks after it.

### Why automations decay

- **Inputs change.** A large supplier changes its invoice layout; customers start writing in a new language; a form gains a field.
- **Business rules change.** Prices, approval limits and policies change, and the automation keeps applying the old ones until someone updates it.
- **Models change.** Rented AI models are updated or retired by their providers, sometimes with changes in behaviour.
- **Connected systems change.** An API version is retired, a password expires, a quota is reduced.
- **Platforms change.** The hosting plan, storage options or limits under an automation can change, sometimes at short notice, and an automation designed for one set of limits may fail under another.

Each of these produces **drift**: a slow or sudden fall in quality or reliability. Drift is dangerous precisely because automations usually keep running while it happens.

### The operating routine

A simple routine keeps automations healthy:

- **Daily**: the owner checks the exception queue and any alerts for failures or limits reached.
- **Weekly**: review the random sample of automatic items, the error rate found in it and the volume trend.
- **Monthly**: review cost against the business case, the most common exception reasons and any planned changes to connected systems.
- **On any change**: re-run the test set before the change goes live, and keep the previous version ready to restore.
- **Quarterly**: review the whole automation portfolio, retire automations that no longer pay their way, and choose the next candidates.

### Continuous improvement

The exception queue is the best source of improvement ideas. If 30 percent of exceptions come from one supplier's format, ask that supplier to send structured invoices. If many come from a missing purchase order, fix the purchasing process upstream. Each fix removes a class of exception permanently, which raises the share of items processed automatically without lowering the threshold or accepting more errors. Over time, the best automations improve not because the AI gets cleverer but because the process around it gets cleaner.

## SKA Field Case Study: Recovering lost knowledge from automated backups

This case comes from the operation of Sales King Academy itself, the platform on which you are taking this course. It concerns one of the least glamorous automated processes any business runs, the nightly backup, and shows why an automation is only as good as the process that tests it.

### The situation

Sales King Academy runs its website, its 26 specialist AI agents, its course catalogue, its CRM, its Automations hub and its Beats wallet on Cloudflare's serverless platform, operated by a single founder. A central asset is its store of **deterministic knowledge**: verified question-and-answer records that the platform's Deterministic answer mode draws on, so that the same question receives the same verified answer every time. In Auto mode, too, verified knowledge is used first. When a student asks a question that the stored knowledge covers, the chat shows a source badge saying the answer came from deterministic recall or verified knowledge rather than from a generated reply.

Alongside the live database, an automated process ran every night: it exported the database and stored the backup in a separate, access-controlled location. Like most backups, it ran quietly and nobody needed it, until they did.

### The problems it caused

On 7 September 2026, a large share of the deterministic knowledge rows was lost. The exact count is a figure only the founder holds: **[founder figure: number and share of knowledge rows lost]**.

The loss struck at the platform's most trusted layer. With knowledge rows missing, questions that should have been answered word for word from verified material would instead fall through to other answer paths, or would have nothing verified to draw on. For a platform that sells consistency and visible sourcing, losing that layer is a direct hit on what customers are paying for.

A few days later a second, separate pressure arrived. On 10 September the platform moved to Cloudflare's free plan, which disabled R2 file storage and tightened database limits. Operating inside tighter limits is the background against which recovery and normal running had to work, until the platform returned to the Workers paid plan, at $5 a month, on 6 October.

### What was done

Recovery used the nightly database backups kept in a separate, access-controlled backup location. Because the backup process had been automated and its output stored outside the live database, there was something to restore from. The time taken to restore, and the share of rows recovered, are founder figures: **[founder figure: time from discovery to restored service]**, **[founder figure: share of lost rows recovered from backups]**.

The tightening of limits on the free plan was handled separately: the platform had to fit its work within the plan's limits for nearly a month, and the decision to return to the paid plan on 6 October is itself a business-case decision of the kind taught in Section 9, setting a modest fixed monthly cost against the risk and effort of operating inside hard limits.

### What it shows

The case illustrates five points from this chapter:

1. **Automate the dull safeguards.** The nightly backup is a textbook automation candidate: high frequency, fully defined, no judgment needed, and catastrophic if forgotten. It is exactly the kind of process a person will skip on a busy day and a schedule will not.
2. **Store the safeguard away from what it protects.** The backups lived in a separate, access-controlled backup location, so the event that damaged the database did not damage them. A backup in the same place as the original protects against much less.
3. **A backup is only as good as a tested restore.** The lesson the platform drew from this event was about backups you can actually restore, and verifying them. A backup that has never been restored is a hope, not a control. Section 8 lists tested backups among the controls every automation needs, because automations change data at speed.
4. **Platform limits shape operations.** The move to the free plan removed a storage service and tightened database limits. Any automation designed for one set of limits must be checked against new ones, as Section 11 describes under drift.
5. **Measures make the story complete.** The founder blanks above are not a gap in the lesson; they are the lesson. Without measured recovery time and recovery share, a business cannot say how good its backup process really is.

### What remains open

Several questions remain for the platform and are good practice for any business. How often should a restore be rehearsed, and who checks that the restored data is complete and correct, not merely present? Should the backup process verify each night's export automatically, for example by restoring it to a scratch database and counting rows against the live one? How long can the business tolerate between the last good backup and a loss, a measure usually called the **recovery point objective**, and how long can it tolerate before service is restored, the **recovery time objective**? Results for the founder to add: **[founder figure: recovery point objective set after the event]**, **[founder figure: restore rehearsals run since the event]**.

### Discussion questions

1. Using the five selection criteria from Section 3, score the nightly backup as an automation candidate. Why does it score so highly even though it saves very little staff time?
2. What automatic check would turn "a backup exists" into "a backup has been shown to restore correctly"?
3. Why is it important that the backups were stored outside the database they protected?
4. How would you build a business case, in the style of Worked example 4, for staying on a paid hosting plan rather than a free one?

## SKA Lab: Design, build and test an automation on the live platform

In this lab you apply the chapter's method to a small process of your own, using the live Sales King Academy platform at saleskingacademy.com. You will map the process, use an agent to help redesign it, build what you can in the platform's Automations hub and CRM, and test an agent built in Agent Builder against a small test set. On the free and explorer tiers, chat is served by a small free model; if you use features that draw on Beats, note the usage as described in step 9.

### Steps

1. **Choose a process.** Pick one repeatable process from your own work or business that involves contacts or customers, such as following up with new enquiries, sending a reminder before a renewal, or sorting incoming requests. Write its six elements from Section 1: trigger, inputs, steps, outputs, owner and measures.
2. **Map and measure.** List each step with an estimated touch time and the wait between steps. Calculate total touch time, cycle time and process cycle efficiency, as in Worked example 2.
3. **Ask for a redesign.** Sign in and open a chat with Sovereign, the executive agent, or Mentor, the education agent. Paste your step list and ask the agent to apply the ECRS questions (eliminate, combine, rearrange, simplify) before suggesting any automation. Note the source badge on the reply, which shows whether the answer came from deterministic recall, verified knowledge, the web or AI generation.
4. **Check the method in Deterministic mode.** Switch the chat to Deterministic mode and ask, "What is process cycle efficiency?" Then switch to Natural mode and ask again. Compare the two answers: in Natural mode the wording may differ, but numbers and key terms should match the stored answer. Record whether they did.
5. **Set up the records.** Open the CRM and add two or three test contacts (use invented names and addresses, not real people), placing them in your pipeline at the stage where your process begins.
6. **Build the automation.** Open the Automations hub. Review the triggers and actions it offers and record them in your results table; do not assume any option exists until you have seen it. Build the closest automation the hub supports to one step of your redesigned process, such as a follow-up for contacts at a given pipeline stage. Run it against your test contacts only.
7. **Build an AI step with Agent Builder.** Open Agent Builder and create an agent on top of a suitable base agent, for example Closer for sales follow-ups or Ledger for invoice and finance questions. Give it short, specific instructions for one AI step in your process, such as classifying an incoming request into one of four named categories and replying "unsure" when none fits.
8. **Test it like a professional.** Write a test set of ten realistic inputs with the correct category for each, written before you run the agent. Include at least three messy or ambiguous cases. Run all ten and score how many it got right and how many times it correctly said "unsure".
9. **Note the cost.** If your session used Beats, check your usage on your account. Usage is metered by seconds of compute, and only full seconds are charged; 1 Beat equals 1 US dollar. Record what the test run cost, or record that it used only free allowance.

### Record your results

| Item | Your result |
|---|---|
| Process chosen and its owner | |
| Total touch time / cycle time / PCE (before) | |
| Steps removed or combined by redesign | |
| Source badge on the redesign answer (step 3) | |
| Deterministic vs Natural answers matched on terms? (step 4) | |
| Triggers and actions available in the Automations hub | |
| Automation built and what happened on the test contacts | |
| Agent test set: correct / unsure / wrong (out of 10) | |
| Beats used, or free allowance only | |

### Reflect

Write five to eight sentences answering: Which steps of your process did the redesign remove before any automation was built? Based on your ten-item test, would you let your agent act on its own, suggest to a person, or stay in shadow mode, and what threshold of results would you need before moving up a stage? What would your exception path look like, and who would own it?

## Summary

A business process is a repeatable sequence of work with a trigger, inputs, steps, outputs, an owner and measures. Automation moves steps from people to software along a spectrum from assisted to monitored operation, and most good automations combine levels. The toolbox includes rules, robotic process automation, workflow and integration platforms, and AI steps; the most reliable pattern uses AI to read and interpret unstructured input and rules to make the decisions that carry money or legal weight.

Candidates are chosen by scoring volume, effort, stability, data readiness and risk, and managed as a portfolio. Before anything is designed, the current process is mapped and measured: touch time, cycle time, process cycle efficiency, first-pass yield, cost per item and work in progress, which Little's Law ties to arrival rate and cycle time. Redesign comes before automation, using the eliminate, combine, rearrange and simplify questions, so that automation does not lock in waste.

AI steps need structured outputs, validation checks, calibrated confidence and consistent settings, and actions must be safe to repeat. Exception handling routes uncertain cases to a named owner with context, and the confidence threshold is chosen by comparing the cost of errors with the cost of review on a real test set. Rollout proceeds from shadow mode to suggest-and-approve to high-confidence action to monitored operation, under controls including audit trails, limits, segregation of duties, a kill switch, change control and tested backups.

Value is proved with a business case of monthly saving, payback and return, tested with sensitivity analysis and checked after go-live. Data protection, fairness, security, record-keeping and the effect on people are part of the design. Automations decay through drift and need a regular operating routine. The Sales King Academy field case showed an automated nightly backup, stored outside the system it protected, making recovery possible after a serious data loss, and showed why a restore that has been tested is the real control.

## Key terms

- **Business process**: a repeatable sequence of work that turns an input into an output of value.
- **Trigger**: the event that starts a process.
- **Process owner**: the one person accountable for a process's performance.
- **Automation**: software performing process steps without a person doing them.
- **Rule-based automation**: automation that follows explicit instructions written by a person.
- **Robotic process automation (RPA)**: software that operates other applications through their screens, as a person would.
- **Workflow engine**: software that coordinates the order, ownership and status of process steps.
- **API (application programming interface)**: a defined way for one program to read or write data in another.
- **Webhook**: a message one system sends to another when an event occurs.
- **Document understanding**: AI extraction and classification applied to documents such as invoices and contracts.
- **SIPOC**: a one-page summary of a process's suppliers, inputs, steps, outputs and customers.
- **Swimlane diagram**: a process map with a lane for each person, team or system.
- **Handoff**: a point where work passes from one person, team or system to another.
- **Value stream map**: a process map that records touch time and wait time for each step.
- **Touch time**: the working time actually spent on an item.
- **Cycle time**: the elapsed time from a process's trigger to its output.
- **Process cycle efficiency (PCE)**: touch time divided by cycle time.
- **First-pass yield**: the share of items completed without rework.
- **Work in progress (WIP)**: the number of items inside a process at a given time.
- **Little's Law**: in a stable process, average work in progress equals arrival rate multiplied by average cycle time.
- **ECRS**: the redesign questions eliminate, combine, rearrange and simplify.
- **Process mining**: reconstructing how a process actually runs from system event records.
- **Confidence score**: a system's estimate of how sure it is of an output.
- **Calibration**: the match between a tool's confidence scores and its real accuracy.
- **Confidence threshold**: the score above which an automation acts on its own.
- **Exception handling**: the design of what happens to items an automation cannot complete.
- **Idempotent action**: an action that has the same effect whether performed once or several times.
- **Shadow mode**: running an automation alongside the manual process without letting it act.
- **Acceptance rate**: the share of automated suggestions approved without change.
- **Audit trail**: a record of every automated action with its inputs, decision and output.
- **Segregation of duties**: a control that prevents one person or system from completing a sensitive transaction alone.
- **Payback period**: one-time cost divided by monthly saving.
- **Sensitivity analysis**: re-running a business case with different assumptions to see how much it depends on each.
- **Drift**: a fall in an automation's quality or reliability as its inputs, rules or environment change.
- **Recovery point objective**: the longest period of data a business can afford to lose.
- **Recovery time objective**: the longest time a business can afford to wait for service to be restored.

## Review questions

1. What are the six elements that describe a business process?
2. Why does the chapter recommend using AI to read documents but rules to make approval decisions?
3. When is robotic process automation the right tool, and why should it be treated as temporary?
4. Which five criteria are used to score automation candidates, and why might a high-effort process still be a poor first project?
5. An invoice process has 15 minutes of touch time and an average cycle time of 5 working days of 8 hours. What is its process cycle efficiency?
6. A process receives 40 items a day and has an average cycle time of 3 days. Using Little's Law, how many items are in progress on average?
7. What do the letters ECRS stand for, and why should they be applied before automating?
8. What is an idempotent action, and why does it matter when an automation retries a failed step?
9. What five parts make up a complete exception path?
10. How should a business choose its confidence threshold?
11. What happens in shadow mode, and what does it reveal?
12. An automation costs $18,000 to build and saves $3,000 a month. What is its payback period, and what is its first-year ROI?
13. Why must a request to change a supplier's bank details always go to a person?
14. Name three causes of drift in a running automation.
15. In the SKA field case, why did it matter that the nightly backups were kept in a separate, access-controlled backup location rather than in the live database?

## Answer key

1. Trigger, inputs, steps, outputs, owner and measures.
2. Reading varied, unstructured documents needs AI's flexibility, while decisions with money or legal weight need the exactness, consistency and auditability of a rule applied to the extracted facts.
3. When an old system has no API or other proper connection, so the only way in is through its screens. It is fragile because screen changes break it, so it should bridge to a proper integration.
4. Volume, effort per item, stability, data readiness and risk. A high-effort process can still be a poor first project if it has low volume, changes often, has poor data or carries high risk, as contract review did in Worked example 1.
5. Cycle time is 5 × 480 = 2,400 minutes, so PCE = 15 ÷ 2,400 = 0.00625, or 0.625 percent.
6. 40 × 3 = 120 items.
7. Eliminate, combine, rearrange and simplify. Applying them first removes waste so that it is not built into code, where it is costly to maintain and harder to see.
8. An action that has the same effect whether done once or several times, usually because it carries a unique identifier that the receiving system uses to ignore duplicates. Without it, a retried step such as a payment could happen twice.
9. Detection, routing to an owned queue, context showing why the item was flagged, resolution that lets the process continue, and learning from recorded corrections.
10. By testing candidate thresholds on a set of real items with known answers, calculating the cost of errors that slip through and the cost of human reviews at each threshold, and choosing the threshold with the lowest total cost, while always routing certain high-risk conditions to people.
11. The automation runs alongside the manual process without acting, and its outputs are compared with what staff did. It reveals where the automation disagrees with people, and sometimes where people disagree with each other, at almost no risk.
12. Payback is $18,000 ÷ $3,000 = 6 months. First-year savings are 12 × $3,000 = $36,000, so ROI = ($36,000 − $18,000) ÷ $18,000 = 1.0, or 100 percent.
13. Changed bank details are a common route for invoice fraud, and a single error can send a large payment to a criminal, so the change must be confirmed through a separately known contact.
14. Any three of: changing inputs, changing business rules, updated or retired AI models, changes in connected systems such as retired APIs or expired credentials, and changes in platform plans or limits.
15. Because the backups were separate from the database that suffered the loss, the event that damaged the live data did not damage the backups, so there was something to restore from.

## Further reading

- Eliyahu M. Goldratt and Jeff Cox, *The Goal: A Process of Ongoing Improvement*.
- Mike Rother and John Shook, *Learning to See: Value Stream Mapping to Add Value and Eliminate Muda*.
- Marlon Dumas, Marcello La Rosa, Jan Mendling and Hajo A. Reijers, *Fundamentals of Business Process Management*.
- Mathias Weske, *Business Process Management: Concepts, Languages, Architectures*.
- Object Management Group, *Business Process Model and Notation (BPMN), Version 2.0*.
- Ajay Agrawal, Joshua Gans and Avi Goldfarb, *Prediction Machines: The Simple Economics of Artificial Intelligence*.
- Paul R. Daugherty and H. James Wilson, *Human + Machine: Reimagining Work in the Age of AI*.
