---
key: crypto_compliance_and_risk
title: "Crypto Compliance And Risk"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-10-08"
chapter: "Sales King Academy, Volume 2, Chapter 6"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# Crypto Compliance and Risk

This chapter explains the legal and operational risks a business takes on when it handles digital assets, and the controls that professionals use to manage them. Chapter 5 showed how blockchains work: public, permanent, pseudonymous records in which whoever holds a private key controls the assets. Those same properties shape the compliance problem. Payments are fast and final, they cross borders without friction, and the identity behind an address is not shown on the ledger. Regulators therefore expect businesses that touch digital assets to know who they are dealing with, to watch for criminal funds, to avoid sanctioned parties, to keep records that support accurate tax reporting, and to treat consumers fairly. You will learn each of these duties by principle, so that you can recognise them under whatever name a particular country's law gives them, and you will learn to build a risk register and a compliance programme in proportion to a business's real exposure.

This chapter is educational and is not legal, tax or financial advice. Laws differ between countries, and rules for digital assets have changed often in recent years and continue to change. Where the chapter names a specific law or authority, it does so to illustrate a principle. Before acting, a business should confirm the current rules that apply to it with qualified counsel and a qualified tax adviser in each place it operates.

## Learning objectives

By the end of this chapter you will be able to:

1. Explain why most existing financial, tax and consumer laws apply to digital asset activity, and describe the risk-based approach to compliance.
2. Describe the stages of know-your-customer and customer due diligence, including enhanced due diligence and beneficial ownership.
3. Explain how money laundering works in three stages, list common digital asset typologies, and describe transaction monitoring and suspicious activity reporting.
4. Explain sanctions screening for people, entities, places and blockchain addresses, and why sanctions breaches are treated so seriously.
5. Describe the purpose of the travel rule and the practical problems of applying it to digital asset transfers.
6. Recognise the activities that commonly trigger licensing or registration, and the main tests used to decide whether a token is a security.
7. Calculate income, cost basis and gain or loss for digital asset transactions, and compare the effect of lot-selection methods.
8. Identify consumer protection duties and operational risks such as key custody, third-party failure and record integrity.
9. Build a scored risk register and outline a proportionate compliance programme.
10. Use the Sales King Academy platform to test how grounded and reasoned answers to compliance questions differ, and to check what personal data the platform shows you.

## 1. Why compliance applies to digital assets

A common early belief about cryptocurrency was that it sat outside the law: no bank, no government, no rules. That belief has caused serious harm to businesses that acted on it. In practice, most countries apply their existing laws to digital asset activity according to what the activity does, not what technology it uses. If a business transfers value for other people, rules for money transmission may apply. If it offers an investment that people buy in the hope of profit from its efforts, securities rules may apply. If it earns income in digital assets, tax rules apply. If it sells to consumers, consumer protection rules apply. Many countries have also passed laws written specifically for digital assets, which add to these duties rather than replace them.

This principle, sometimes summed up as "same activity, same risk, same rules", is the single most useful idea in this chapter. When a business considers a new digital asset feature, the first compliance question is not "is crypto regulated here?" but "what is this feature actually doing, and which laws cover that activity?"

### The risk-based approach

International standards for fighting money laundering and terrorist financing are set by the **Financial Action Task Force** (FATF), an intergovernmental body whose recommendations most countries have committed to implement. Since amendments adopted in 2018 and 2019, FATF's standards have explicitly covered **virtual asset service providers** (VASPs): businesses that exchange, transfer, hold or administer digital assets for others. Countries implement the standards in their own laws, so details vary, but the core structure is shared widely.

At the centre of that structure is the **risk-based approach**. A business is expected to understand the specific ways it could be used for crime, assess how likely and how harmful each is, and put stronger controls where risk is higher. A small merchant taking occasional payments for its own goods faces a different risk from an exchange that lets anonymous users move large sums across borders, and the controls expected of each differ accordingly. The approach rewards honest analysis. A regulator is usually far more forgiving of a business that identified a risk, controlled it reasonably and still suffered an incident than of one that never looked.

### Who is responsible

Compliance cannot be delegated away entirely. A business may use vendors for identity checks, sanctions screening or blockchain analytics, and may use a payment processor that takes on many duties itself. But the business remains responsible for understanding what its vendors do, for its own policies and for its own decisions. Most compliance frameworks expect a named person, often called a compliance officer or money laundering reporting officer, to own the programme, with enough authority and independence to say no to the business when necessary.

## 2. Knowing your customer

**Know your customer** (KYC) is the process of establishing who a customer is before and during a business relationship. It is part of a wider duty usually called **customer due diligence** (CDD). Where a business falls within anti-money-laundering law, CDD is typically a legal requirement; where it does not, a lighter version is still good practice for preventing fraud.

### The stages of due diligence

Customer due diligence usually has four parts.

**Identification and verification.** The business collects identifying information, such as a person's full name, date of birth and address, or a company's legal name, registration number and registered office, and then verifies it against reliable sources. Verification may involve checking an identity document, comparing a live photo or video with the document, checking databases or confirming a company's registration with the official registry. Identification is what the customer tells you; verification is how you confirm it.

**Beneficial ownership.** For a company or other legal entity, the business must identify the natural persons who ultimately own or control it, called **beneficial owners**. Criminals often hide behind chains of companies. Many regimes set an ownership percentage above which an owner must be identified, and also require identifying whoever exercises control by other means.

**Purpose and nature of the relationship.** The business records what the customer intends to do: for example, a retailer paying suppliers monthly, or an individual buying small amounts occasionally. This creates an expected pattern against which later activity can be compared.

**Ongoing monitoring.** Due diligence is not a one-time event. The business keeps customer information current and watches whether actual activity fits the expected pattern.

### Enhanced and simplified due diligence

Under a risk-based approach, the depth of checks varies. **Enhanced due diligence** (EDD) applies to higher-risk customers and may include confirming the source of the customer's funds and wealth, obtaining senior management approval to accept the customer, and monitoring more frequently. Typical triggers include very large or unusual transactions, connections to countries with weak controls, complex ownership structures that have no clear business reason, and **politically exposed persons** (PEPs): people who hold or have held prominent public positions, together with their close family and associates, whose position could expose them to bribery or corruption. Being a PEP is not wrongdoing; it is a reason for closer attention.

Some regimes allow **simplified due diligence** for demonstrably low-risk situations, such as small, capped products, but the business must be able to justify the decision.

### The digital asset twist

Digital assets add two complications. First, many relationships are entirely online, so identity verification depends on remote document and liveness checks, which fraudsters try to defeat with stolen documents and increasingly with synthetic images. Second, a verified customer may send and receive funds from addresses that belong to someone else entirely. KYC on the customer is therefore only half the picture; the business also needs to understand the addresses its customers deal with. Blockchain analytics, covered in Section 3, help with this second half.

### Data protection

Identity documents and verification records are highly sensitive personal data. Collecting them creates a duty to protect them. A business should collect only what it needs, store it securely with access limited to those who need it, keep it for the period the law requires and no longer, and choose verification vendors with strong security. A leak of customers' identity documents is both a legal problem and a severe breach of trust.

## 3. Anti-money laundering

**Money laundering** is the process of making the proceeds of crime appear to come from legitimate sources. **Anti-money-laundering** (AML) rules require certain businesses to put controls in place to prevent, detect and report it. The same controls usually cover **terrorist financing**, which differs in that the funds may be legitimate in origin but are destined for harmful use.

### Three stages

Laundering is classically described in three stages.

**Placement** introduces criminal proceeds into the financial system, for example by depositing cash or buying digital assets with it.

**Layering** moves the funds through many transactions to obscure their origin, for example by passing them through many addresses, exchanging them for other assets, or moving them between platforms and countries.

**Integration** brings the funds back as apparently clean money, for example by withdrawing to a bank account as if they were trading profits or paying for goods and property.

Digital assets can make layering fast and cheap, because funds can be moved across many addresses and networks in minutes. At the same time, public ledgers keep a permanent record of every movement, which investigators can analyse long afterwards. The technology helps both sides.

### Digital asset typologies

A **typology** is a recognised pattern of criminal behaviour. Common digital asset typologies include:

- **Mixing and tumbling**: services that pool funds from many users and pay out different coins, breaking the visible link between sender and receiver.
- **Chain hopping**: converting funds rapidly across different assets and networks, often through bridges, to make tracing harder.
- **Structuring**: splitting a large amount into many smaller transactions to stay below thresholds that would trigger checks or reports.
- **Money mules**: using accounts opened by other people, sometimes recruited with job offers and sometimes unaware of what they are doing, to move funds.
- **Scam proceeds**: funds obtained from investment fraud, romance scams or fake platforms, which victims are often coached to send in digital assets.
- **Ransomware and hacking proceeds**: payments extorted from victims or assets stolen from platforms, typically moved quickly through many addresses.
- **Darknet market activity**: payments for illegal goods on hidden marketplaces.

Knowing typologies lets a business write monitoring rules and train staff to recognise suspicious behaviour.

### Transaction monitoring and blockchain analytics

**Transaction monitoring** compares customer activity with expected behaviour and with known typologies, and flags exceptions for review. Rules might flag a sudden jump in volume, many transfers just below a review threshold, funds that arrive and leave within minutes, or activity inconsistent with what the customer said they would do.

For digital assets, monitoring is supported by **blockchain analytics**: tools that analyse public ledgers to group addresses that are likely controlled by the same party and to label clusters associated with exchanges, mixers, scams, sanctioned parties and other categories. A business can screen an incoming deposit's history and see, for example, that a large share of the funds passed through a mixer two transactions earlier. Analytics are powerful but not infallible: labels are inferences, can be wrong or out of date, and can be evaded. They support human judgement; they do not replace it.

### Worked example 1: Tuning an alert rule

A payment business screens about 20,000 incoming transactions a month. Its first monitoring rule flags 0.6 percent of them for review. Each review takes an analyst about 12 minutes.

- Alerts per month: 20,000 × 0.006 = 120.
- Analyst time: 120 × 12 = 1,440 minutes, which is 24 hours a month.

Over a quarter, the team finds that, on average, only 2 alerts a month turn out to be genuinely suspicious. The rule's precision, the share of alerts that matter, is 2 ÷ 120, about 1.7 percent. Analysts spend 98 percent of their review time on false alarms, and fatigue starts to make reviews careless.

The team refines the rule, adding conditions based on its typology analysis, so that it flags 0.2 percent of transactions:

- Alerts per month: 20,000 × 0.002 = 40.
- Analyst time: 40 × 12 = 480 minutes, which is 8 hours a month.
- If the same 2 genuine cases are still caught, precision rises to 2 ÷ 40 = 5 percent.

The crucial word is "if". A rule that generates fewer alerts is only better if it still catches the cases that matter. Before adopting the refined rule, the team runs it against the previous six months of data and confirms that it would have flagged every case that was actually reported. It also keeps a written record of why the rule changed and what testing showed, because a regulator reviewing the programme will ask. Tuning is a balance between missing real cases and drowning analysts in noise, and it must be documented and tested, not done by instinct.

### Worked example 2: Spotting structuring

A business has set an internal rule that any single customer payment of 3,000 dollars or more receives an extra source-of-funds check. This is the business's own threshold, not a figure from any law. Over five days, a newly onboarded customer makes four payments: 2,900, 2,950, 2,980 and 2,900 dollars.

Each payment, taken alone, is under 3,000 dollars and passes the single-payment rule. Together they total 2,900 + 2,950 + 2,980 + 2,900 = 11,730 dollars in five days, nearly four times the threshold. All four sit within 100 dollars of it. The customer said at onboarding that they expected to make occasional purchases of a few hundred dollars.

This is a classic structuring pattern, and it shows why monitoring must look at aggregates over time, not only individual transactions. A good rule would also flag repeated payments within a narrow band below any threshold. The pattern does not prove wrongdoing. The customer may have a simple explanation. But it justifies a review, a request for information about the source of funds and, if the explanation is unsatisfactory, the reporting step described next.

### Suspicious activity reporting

Where a business is covered by AML law and its review leaves a suspicion of money laundering or terrorist financing, it is usually required to file a report with the national **financial intelligence unit**. Names differ: in the United States the filing is a suspicious activity report submitted to FinCEN; other countries use other names. The report goes to the authorities, not to the customer.

Most regimes forbid **tipping off**: telling the customer, directly or indirectly, that a report has been made or that an investigation is under way. Staff must be trained to handle these situations without revealing the report, which can be difficult when a customer asks why their withdrawal has been delayed. A business should have a scripted, neutral response approved by its compliance officer.

Reporting is an obligation based on suspicion, not proof. Staff do not need to establish that a crime occurred, and they should not investigate in ways that alert the customer. They need to escalate honestly and promptly.

## 4. Sanctions screening

**Sanctions** are legal restrictions that governments and international bodies impose on dealings with specified countries, regions, governments, organisations and individuals, usually for reasons of national security or foreign policy. They can prohibit any transfer of funds or assets to a listed party, require assets of listed parties to be frozen, and restrict trade with whole regions.

Sanctions are among the strictest obligations a business faces. In many regimes, liability does not depend on intent: a business that sends funds to a sanctioned party may be in breach even if it did not know. Penalties can be severe, and reputational damage follows. A business must therefore screen before it acts, not after.

### What to screen

**People and entities.** Customers, their beneficial owners and, where known, counterparties are checked against the sanctions lists that apply to the business. Many businesses check several lists, because their activities may fall under more than one country's regime. In the United States, the Office of Foreign Assets Control (OFAC) maintains the main list, often called the SDN list. Some regimes extend restrictions to entities owned or controlled by listed parties even if those entities are not listed themselves, so ownership information matters.

**Places.** Some sanctions apply to entire countries or regions. Businesses commonly block access from those places using the customer's verified address, and often also the location suggested by the customer's internet connection, while recognising that tools for hiding location exist.

**Addresses.** Some authorities have added specific blockchain addresses to their sanctions listings, alongside the names of the people or groups that control them. OFAC first included digital currency addresses in a listing in 2018. Screening a counterparty's address against these listings, and using analytics to see whether funds have passed through listed addresses, is now a standard control for businesses that handle digital assets.

### Matching and false positives

Name screening is imperfect. Names are spelled in different ways, transliterated from other alphabets, and shared by many unrelated people. Screening tools use fuzzy matching, which catches near matches but also produces many false positives. Each potential match must be reviewed and either cleared, with a recorded reason, or escalated. Screening that blocks too little is dangerous; screening that blocks too much harms legitimate customers. As with transaction monitoring, settings must be tested and documented.

### When a match is real

If a business identifies a genuine match, it typically must stop the transaction, freeze any assets as the law requires, and report to the relevant authority within a set period. It should not return funds to a sanctioned sender, because returning them is itself a transfer. These steps are time-sensitive and legally technical, which is why every business that handles payments should have a written procedure and a named person to call before it ever needs them.

## 5. The travel rule

In traditional banking, wire transfers carry information about who is sending the money and who is receiving it, and banks pass this information along the chain. This lets each bank screen both parties and lets investigators follow funds. FATF's Recommendation 16 sets this standard, and in 2019 FATF extended it to digital asset transfers between VASPs. The obligation is widely called the **travel rule**, because the information must travel with the transfer.

### What the rule requires

In broad terms, when one VASP sends digital assets on behalf of a customer to another VASP, the sending VASP must collect and pass on information identifying the originator (such as name and account or address, and in some cases further details) and the beneficiary (such as name and address or account). The receiving VASP must obtain this information, check it and use it for screening. FATF's standard allows countries to exempt transfers below a de minimis threshold of 1,000 US dollars or euros, with lighter information requirements; some jurisdictions have chosen to apply the rule to transfers of any size. Thresholds and exact data requirements are set by each country's law and should be confirmed locally.

### Practical problems

The travel rule was designed for a world of banks that know each other. Digital assets raise new difficulties.

**Identifying the counterparty.** A blockchain address does not say whether it belongs to another VASP, and if so which one, or to an individual's own wallet. Businesses use analytics, directories and direct confirmation to find out.

**Transmitting the data.** The blockchain itself does not carry the customer information, and putting personal data on a public chain would be a serious privacy failure. The data must be sent separately, through messaging protocols that VASPs have built for this purpose. Different protocols do not always talk to each other, so a VASP may need to support several or use an intermediary that bridges them.

**Unhosted wallets.** When a customer sends to, or receives from, a wallet they control themselves rather than one held at a VASP, there is no counterparty institution to exchange data with. Rules for these transfers differ between jurisdictions. Common measures include collecting the counterparty's details from the customer, and for larger amounts asking the customer to prove control of the wallet, for example by signing a message with its key.

**The sunrise problem.** Countries have implemented the rule at different times. A VASP in a country that enforces it may need to send to one in a country that does not yet, and must decide how to handle such transfers under a risk-based approach.

For a merchant that simply accepts payments through a licensed payment processor, the processor usually handles travel rule obligations. A business that itself transfers assets on behalf of customers needs to understand them directly.

## 6. Licensing, registration and the regulatory perimeter

The **regulatory perimeter** is the boundary between activities that require a licence, registration or authorisation and those that do not. Crossing it without the necessary permission is one of the most serious compliance failures, because it can make the whole business unlawful rather than just one transaction.

### Activities that commonly need permission

Across many jurisdictions, the following activities commonly require some form of licence, registration or authorisation when done for others as a business:

- exchanging digital assets for money or for other digital assets;
- transferring digital assets on behalf of customers;
- holding or safeguarding digital assets or their keys for customers (custody);
- operating a trading platform;
- issuing stablecoins or other tokens offered to the public;
- giving advice on, or managing, investments in digital assets.

Examples illustrate the pattern. In the United States, a business that transmits value on behalf of others may be a money services business that must register with FinCEN, and many states separately require money transmitter licences. In the European Union, the Markets in Crypto-Assets Regulation (MiCA) set up an authorisation regime for crypto-asset service providers and rules for issuers of certain tokens, including stablecoins. In 2025 the United States enacted a federal framework for payment stablecoins. Other countries have their own regimes, from registration schemes to full licensing to outright restrictions.

A business that accepts digital assets as payment for its own goods or services is, in many places, treated differently from one that moves value for others. That difference is often decisive, but it depends on the exact facts. A business that also holds customer balances, pays out to third parties, or converts funds for others may cross into regulated territory. Specific facts should be checked with counsel.

### When is a token a security?

Securities laws protect investors by requiring disclosure, registration and fair dealing when investments are offered to the public. Whether a token counts as a security matters enormously, because selling an unregistered security can bring heavy penalties and an obligation to refund buyers.

In the United States, the key test comes from a 1946 Supreme Court case, *SEC v. W. J. Howey Co.*, and is known as the **Howey test**. An arrangement is an investment contract, and therefore a security, if it involves an investment of money in a common enterprise with an expectation of profits that come from the efforts of others. Courts look at the economic reality, not the label. A token sold to raise money for a project, marketed with promises that the team's work will make it rise in value, has the features the test looks for. A token that only gives access to a service, sold at a fixed price to people who use it, generally has fewer of them, though the analysis can be complex and has been argued over in court for years.

Other countries use their own definitions, and the same token may be treated differently in different places. A business that creates, sells or promotes any token should obtain specialist legal advice before doing so.

### Regulatory change

Rules for digital assets have changed frequently and are likely to keep changing. A compliance programme therefore needs a process for regulatory change: someone responsible for tracking new laws, guidance and enforcement actions in each relevant jurisdiction, assessing their effect, and updating policies. Relying on a vendor's newsletter or a news headline is not enough; changes need to be read in the original and assessed against the business's actual activities.

## 7. Tax and record-keeping

Tax rules for digital assets differ between countries, but most share a common structure. Many treat digital assets as a form of property or asset rather than as currency. In the United States, for example, the IRS treats them as property. Under property treatment, receiving digital assets as payment is generally income measured at their fair market value when received, and selling, exchanging or spending them later is generally a disposal on which a gain or loss arises.

### Core concepts

**Fair market value** is the price at which the asset could be sold in an open market at the relevant moment, usually taken from a reliable exchange price in the business's reporting currency.

**Cost basis** is the amount treated as having been paid for an asset, used to calculate gain or loss when it is disposed of. For assets received as payment, the basis is generally the value counted as income at receipt. For purchased assets, it is generally the purchase price, and many tax systems allow certain acquisition fees to be added.

**Gain or loss** on a disposal is generally the proceeds (often reduced by selling fees) minus the cost basis.

**Lot** means a specific acquisition of an asset at a particular time and price. A business that acquires the same asset several times holds several lots with different bases.

### Worked example 3: Income, basis and a loss

A design studio completes a project and is paid 0.05 bitcoin. At the moment of receipt, the market price is 60,000 dollars per bitcoin. (All prices here are illustrations.)

- Income recognised at receipt: 0.05 × 60,000 = 3,000 dollars.
- Cost basis of the 0.05 bitcoin: 3,000 dollars.

Three weeks later, the studio sells the 0.05 bitcoin when the price is 54,000 dollars, paying a 15-dollar selling fee.

- Gross proceeds: 0.05 × 54,000 = 2,700 dollars.
- Net proceeds: 2,700 − 15 = 2,685 dollars.
- Gain or loss: 2,685 − 3,000 = −315 dollars, a loss of 315 dollars.

Under property-style rules, the studio typically reports 3,000 dollars of business income and, separately, a 315-dollar loss on disposal. The studio does not simply report 2,685 dollars of income; the two events are distinct. How the loss may be used depends on the tax system and the type of taxpayer. The example shows why the price at the moment of receipt must be recorded: without it, neither the income nor the basis can be calculated.

### Worked example 4: Which lot was sold?

A business acquired the same digital asset in three lots:

| Lot | Acquired | Quantity | Cost basis |
|---|---|---|---|
| 1 | January | 1.0 | 2,000 dollars |
| 2 | March | 1.0 | 2,600 dollars |
| 3 | May | 1.0 | 2,300 dollars |

In June it sells 1.5 units at 2,500 dollars each, for proceeds of 1.5 × 2,500 = 3,750 dollars (ignore fees for simplicity). The gain depends on which units are treated as sold.

- **First in, first out (FIFO)**: all of lot 1 and half of lot 2. Basis = 2,000 + 0.5 × 2,600 = 3,300. Gain = 3,750 − 3,300 = 450 dollars.
- **Specific identification, highest cost first**: all of lot 2 and half of lot 3. Basis = 2,600 + 0.5 × 2,300 = 3,750. Gain = 0.
- **Most recent first**: all of lot 3 and half of lot 2. Basis = 2,300 + 1,300 = 3,600. Gain = 150 dollars.
- **Average cost**: average basis per unit = (2,000 + 2,600 + 2,300) ÷ 3 = 2,300. Basis = 1.5 × 2,300 = 3,450. Gain = 300 dollars.

The same sale produces a reported gain anywhere from 0 to 450 dollars depending on the method. That is why tax systems regulate which methods are allowed. Some permit specific identification only if the business keeps records showing exactly which units were sold at the time of sale, and apply a default such as FIFO otherwise; some require an averaging or pooling method. A business cannot choose whichever method gives the best answer after the fact. It must follow the method its tax system permits, apply it consistently, and keep the records that support it.

### What records to keep

For every digital asset transaction, a business should record:

- the date and time;
- the asset and quantity;
- the fair market value in the reporting currency at that moment, and the source of the price;
- the counterparty or purpose (customer payment, supplier payment, transfer between own wallets, sale on an exchange);
- fees paid and in which asset;
- the transaction identifier on the blockchain, and the addresses involved;
- the lot or lots affected, and the method used to select them.

Transfers between a business's own wallets are not usually taxable disposals, but they must be recorded so that the business can show the units are the same ones it already held. Without that record, a transfer can look like an unexplained receipt.

Exchanges and brokers in many jurisdictions are now subject to information-reporting rules that send transaction data to tax authorities. A business should expect its records to be compared with third-party reports, and gaps between them will raise questions.

## 8. Consumer protection and fair dealing

Businesses that offer digital asset products or payments to consumers owe them the same basic duties as any other seller, and in many places additional ones. The principles below are widely shared, though the specific rules vary.

**Clear, fair and not misleading communication.** Marketing must not overstate benefits, hide risks or imply guarantees that do not exist. Statements such as "safe", "guaranteed returns" or "as good as cash" invite enforcement if they are not true. Risks such as price volatility, irreversibility and the possibility of losing access to assets should be stated plainly and prominently, not buried in terms and conditions.

**Disclosure of fees and terms.** Customers should see the full cost of a transaction, including exchange rate spreads and network fees, before they commit. If a price quote expires after a set time, the customer must be told.

**Handling of customer assets.** Where a business holds assets for customers, many regimes require them to be kept separate from the business's own assets and protected if the business fails. Several high-profile collapses showed what happens when customer assets are mixed with company funds: customers become unsecured creditors in a long insolvency process.

**Complaints and redress.** Customers should have a clear way to complain, and the business should respond within a stated time. Because blockchain transactions are usually irreversible, refund and dispute policies must be designed by the business itself; Chapter 7 covers this in detail.

**Scam prevention.** Consumers are frequently targeted by fraudsters who persuade them to send digital assets. A business that sees a customer about to send funds to an address associated with fraud, or showing signs of being coached, may have a duty, and certainly has a strong reason, to warn and delay. Clear warnings at the point of payment ("We will never ask you to move funds to a 'safe' wallet") reduce losses.

**Vulnerable customers.** Some customers are more exposed to harm because of age, illness, financial difficulty or limited understanding. Staff should be trained to recognise signs of vulnerability and respond with care.

## 9. Operational risk

Legal risk is only part of the picture. Many of the largest losses involving digital assets came from operational failures: stolen keys, insider theft, failed vendors, and records that could not be trusted.

**Key custody.** Chapter 5 showed that whoever holds the private keys controls the assets. A compliance programme should therefore cover how keys are generated, stored, backed up and used. Good practice includes keeping most assets in cold storage with only an operating float in hot wallets; requiring several approvals for large transfers through multisig or multi-party computation; separating duties so no single person can both initiate and approve a transfer; recording key-generation ceremonies; and test-restoring backups on a schedule.

**Address allow-lists and transfer limits.** Restricting outgoing transfers to pre-approved addresses, with a waiting period before a new address can be used, protects against both outside attackers and tricked employees. Daily limits cap the damage from any single failure.

**Third-party risk.** Custodians, processors, exchanges, analytics providers and identity vendors are all points of failure. A business should assess each before relying on it (its regulation, security, financial strength and how customer assets are held) and plan for what happens if it fails or stops serving the business.

**Record integrity and retention.** Compliance depends on records: identity checks, screening results, alerts and decisions, reports, transaction histories and tax data. Most regimes require them to be kept for a set number of years. The records must be complete, protected against alteration and restorable. A backup that cannot be restored, or a database that silently loses rows, can turn a compliant business into one that cannot prove it was compliant.

**Privacy at the point of output.** Systems often hold more data than any one user should see. Customer-facing screens, statements and support tools should show each customer only their own information, and internal identifiers and other customers' data should never reach them. The most reliable design applies a single filter at the point where data leaves the system, so that no individual screen can forget to apply it.

**Incident response.** When something goes wrong (a hack, a sanctions hit, a data leak, a lost key) the first hours matter. A written plan should say who decides, who is told (including regulators, banks and customers where required), how evidence is preserved and how communications are approved.

## 10. Building a proportionate compliance programme

A compliance programme pulls the elements of this chapter together. Its components are broadly the same everywhere:

1. **A business-wide risk assessment** covering customers, products, delivery channels, geographies and transaction types.
2. **Written policies and procedures** for due diligence, screening, monitoring, reporting, record-keeping, custody and incident response.
3. **A responsible officer** with authority, independence and resources.
4. **Training** for all staff, with deeper training for those in high-risk roles.
5. **Independent testing**, by internal audit or an outside reviewer, of whether the programme works in practice.
6. **Regulatory change management** to keep all of the above current.

Many organisations describe responsibility in **three lines**: the business teams that own and manage risk day to day, the compliance and risk functions that set policy and oversee it, and an independent audit function that checks both.

### The risk register

A **risk register** lists each identified risk, scores it, records the controls in place and names an owner. A simple scoring method rates likelihood and impact each from 1 (low) to 5 (high) and multiplies them. The score ranks risks; it is not a precise measurement, and its value lies in forcing an honest discussion.

### Worked example 5: Scoring a risk register

A small online retailer plans to accept stablecoin payments directly, without a processor. Its team rates six risks before controls:

| Risk | Likelihood (1-5) | Impact (1-5) | Score |
|---|---|---|---|
| Incomplete tax lot records | 4 | 3 | 12 |
| Payment received from a sanctioned address | 2 | 5 | 10 |
| Theft of hot wallet keys | 2 | 5 | 10 |
| Customer complaints arising from scams | 3 | 3 | 9 |
| Operating without a licence that is needed | 2 | 4 | 8 |
| Customers paying on the wrong network | 3 | 2 | 6 |

The ranking surprises the team: the least dramatic risk, poor records, scores highest, because without a system it is almost certain to happen and it affects every transaction. They assign controls and owners:

- Tax records: integrate the wallet with accounting software that captures price, lot and transaction identifier for each payment; owner, finance lead. Likelihood falls from 4 to 2, giving a residual score of 2 × 3 = 6.
- Sanctions: screen every paying address with an analytics service before the order ships and hold flagged payments for review; owner, compliance lead. Likelihood falls from 2 to 1; residual 1 × 5 = 5.
- Key theft: keep only one week's receipts in the hot wallet and sweep the rest to a two-of-three multisig; owner, operations lead. Likelihood falls from 2 to 1; residual 1 × 5 = 5.

Two items cannot be scored away by the team alone. The licensing question needs counsel's written view on whether direct acceptance for the retailer's own goods falls outside the local licensing rules. The impact of a sanctions breach stays at 5 whatever the controls, which is why its residual score remains significant and the item stays on the board's quarterly agenda. The register is not a box-ticking exercise; it is where the business decides, in writing, which risks it accepts.

### Case study: Lumen Craft Supply chooses a processor

Lumen Craft Supply is a fictional company invented for this chapter. It sells art materials online to customers in many countries, and a growing number of overseas customers ask to pay in stablecoins because card payments from their countries often fail.

The founder's first plan is to publish a wallet address at checkout and ship when funds arrive. The operations manager builds a risk register like the one in Worked example 5 and finds four problems with the plan. First, the business would need to screen every paying address against sanctions lists and analytics, which means a subscription to an analytics tool and a trained reviewer. Second, overseas customers would sometimes pay from accounts at exchanges in other countries, and the team does not know which travel rule obligations, if any, would fall on it. Third, the finance team would need to record fair market value and lot data for every receipt. Fourth, nobody on staff has experience with secure key custody.

The team then evaluates licensed payment processors. A processor would provide a payment page with the network and amount fixed, screen incoming funds, handle travel rule messaging with exchanges, and convert receipts to the business's bank currency the same day, so that Lumen never holds the stablecoins itself and has no tax lots to track beyond the conversion. The costs are a processing fee and dependence on the processor. The team performs due diligence on two processors: their licensing in the countries where Lumen sells, how they hold funds in transit, their screening practices, what happens to pending payments if they fail, and whether they will share screening results when Lumen asks.

Lumen chooses the processor that can show current licences in its main markets and that converts funds on the same day. Its board approves a written policy: the business will accept stablecoins only through the processor, will not hold digital assets on its balance sheet, will display a plain-language notice at checkout explaining that blockchain payments cannot be reversed and that refunds are paid in the store's currency, and will review the arrangement every six months. The founder's original plan would have taken a day to set up and created risks the business could not manage. The chosen plan took six weeks and matched the business's capacity.

The case illustrates proportionality. The right compliance answer for a small retailer is often to keep risky activities with a specialist that is equipped and licensed to handle them, and to keep its own exposure small.

## SKA Field Case Study: One filter for what users can see

This case comes from the operation of Sales King Academy itself, the platform on which you are taking this course. It concerns two controls that every compliance programme depends on: protecting what customers can see, and keeping records that can be restored.

### The situation

Sales King Academy runs 26 specialist AI agents, a curriculum of 1,119 subjects, a CRM, automations and a prepaid credit system called Beats (1 Beat equals 1 US dollar, with a minimum purchase of 10 Beats). Beats are a prepaid platform credit, not a cryptocurrency or an investment. Internally, the platform links its records with identifiers and internal chain numbers that help it organise data. Its stated privacy rule is that a user sees only their own DNA-16 identifier, their usage and their Beats balance, and nothing else from the internal structure.

### The problems it caused

On 7 October 2026, an audit found that internal chain numbers were appearing in API responses and on screens that users could see. The rule existed, but it was not being enforced everywhere data left the system. Each screen and each response had been built separately, and some of them passed internal values through.

This is a common pattern in compliance failures. A policy is written, and enforcement is left to many separate places, each of which must remember to apply it. Every new feature becomes another chance to forget. A month earlier, on 7 September, the platform had also lost a large share of its deterministic knowledge rows and had to recover them from nightly database backups kept in a separate, access-controlled backup location. Taken together, the two incidents tested both halves of record governance: controlling what leaves the system, and being able to rebuild what is inside it.

### What was done

The privacy fix did not patch each screen one at a time. Instead, a single outgoing filter was put in place that strips internal chain numbers from everything leaving the platform, so users see only their DNA-16, their usage and their Beats. Because every response passes through that one point, a new screen or response is covered automatically.

For the data loss, recovery used the nightly backups stored outside the main database. Because they were taken every night and kept in a separate place, the platform could restore from a recent copy rather than rebuilding from nothing.

### What it shows

1. **Enforce rules at a choke point.** Section 9 recommended applying privacy controls where data leaves a system. The same logic applies to sanctions screening (one screening step that every outgoing payment must pass) and to approvals (one signing service that every transfer must use). A single point of enforcement is easier to test, audit and trust than many scattered ones.
2. **Audit what users actually see.** The policy was correct; the outputs did not match it. Compliance testing has to examine real outputs, not only written policies.
3. **Records must be restorable, not just stored.** A compliance programme that cannot produce its records after a failure cannot demonstrate compliance. Off-site, regular backups are the minimum; tested restores and integrity checks make them reliable.
4. **Data minimisation reduces risk.** Showing users only what they need limits the damage of any leak and keeps the platform's internal structure out of view.

### What remains open

- How long internal chain numbers had been visible before the 7 October audit: **[founder figure: exposure period]**
- How many responses or screens were affected: **[founder figure: number of affected endpoints]**
- Whether an automated test now checks every response for internal numbers on each release: **[founder figure: automated output test in place]**
- The share of knowledge rows lost and recovered in September: **[founder figure: rows lost and recovered]**

A remaining design question is how to prove the filter keeps working as the platform grows. The general answer is a recurring automated test that sends sample requests and fails the release if any internal value appears in the output.

### Discussion questions

1. Why is a single outgoing filter more reliable than fixing each screen separately?
2. How would you apply the choke-point principle to sanctions screening in a business that sends payments from several different systems?
3. What evidence would you want to see before telling a regulator, or a customer, that the privacy problem is fixed?

## SKA Lab: Test grounded and reasoned answers to compliance questions

In this lab you use the live Sales King Academy platform to ask compliance questions, compare how answers are produced, and check the platform's own privacy rule. You need a free account and text chat only.

### Steps

1. **Sign in** at saleskingacademy.com and open the chat with Statute, the legal agent.
2. **Ask a principle question in Deterministic mode.** Choose Deterministic in the chat settings and ask: "What are the stages of customer due diligence?" Record the source badge and compare the answer with Section 2.
3. **Ask the same question in Auto and Natural modes.** Note the badge, wording and length each time, and check that key terms match across modes.
4. **Test the logic lane with a certain premise.** In Natural or Auto mode, ask: "If a business transfers value on behalf of others, it needs to check whether it must register. Our business transfers value on behalf of others. Does it follow that we need to check whether we must register?" Record whether the answer says the conclusion follows.
5. **Test it with a hedged premise.** Ask: "Businesses that hold customer funds usually need a licence. Our business holds customer funds. Do we need a licence?" Record whether the answer presents the conclusion as certain or as "most likely", and whether it advises confirming with counsel.
6. **Ask Ledger a tax calculation.** Open the Ledger agent and ask: "We received 0.05 bitcoin worth 60,000 dollars per bitcoin and later sold it at 54,000 dollars with a 15-dollar fee. What were the income and the gain or loss?" Compare the result with Worked example 3.
7. **Ask a live question.** Ask Statute: "What recent news is there about crypto travel rule enforcement?" Record the source badge and any sources named, and note how you would check them.
8. **Check what the platform shows you.** Open your account or wallet view. List the identifiers and figures shown about you. Compare them with the platform's rule that a user sees only their DNA-16, usage and Beats.

### Record your results

| Step | Agent and mode | Question (short form) | Source badge | Certain, "most likely", or other? | Matches the chapter? | Notes |
|---|---|---|---|---|---|---|
| 2 | | | | | | |
| 3 Auto | | | | | | |
| 3 Natural | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |

### Reflect

Write three to five sentences answering: How did the answer to the hedged premise in step 5 differ from step 4, and why does that difference matter for compliance advice? Which answers would you treat as a starting point for a conversation with counsel, and which, if any, would you rely on directly?

## Summary

Most existing laws on money, securities, tax and consumer protection apply to digital asset activity according to what the activity does. International standards set by FATF cover virtual asset service providers, and countries implement them in their own laws under a risk-based approach that puts stronger controls where risk is higher.

Customer due diligence identifies and verifies customers and beneficial owners, records the purpose of the relationship and monitors it over time, with enhanced checks for higher-risk customers such as politically exposed persons. Anti-money-laundering controls address placement, layering and integration, use typologies and blockchain analytics to monitor activity, and lead to suspicious activity reports without tipping off the customer. Monitoring rules must be tuned and tested, balancing missed cases against false alarms.

Sanctions screening covers people, entities, places and blockchain addresses, and is strict because liability often does not depend on intent. The travel rule requires originator and beneficiary information to accompany transfers between service providers, which raises practical problems with counterparty identification, data transmission and unhosted wallets.

Licensing questions turn on activities such as exchange, transfer, custody, issuance and advice. Securities law may apply to tokens; in the United States the Howey test asks whether there is an investment of money in a common enterprise with an expectation of profit from the efforts of others. Tax rules in many places treat digital assets as property, so receipts create income at fair market value and later disposals create gains or losses that depend on cost basis and the lot-selection method allowed.

Consumer protection requires clear communication of risks and fees, protection of customer assets and fair complaint handling. Operational risk, especially key custody, third-party failure, record integrity and privacy, causes many of the largest losses. A proportionate programme combines a risk assessment, policies, an accountable officer, training, independent testing and regulatory change management, recorded in a risk register that states which risks the business accepts.

## Key terms

- **Same activity, same risk, same rules**: the principle that laws apply according to what an activity does, not the technology used.
- **Financial Action Task Force (FATF)**: the intergovernmental body that sets international anti-money-laundering standards.
- **Virtual asset service provider (VASP)**: a business that exchanges, transfers, holds or administers digital assets for others.
- **Risk-based approach**: assessing risks and applying stronger controls where risk is higher.
- **Know your customer (KYC)**: establishing and verifying who a customer is.
- **Customer due diligence (CDD)**: identification, verification, beneficial ownership, purpose and ongoing monitoring of a customer relationship.
- **Enhanced due diligence (EDD)**: deeper checks for higher-risk customers, such as source of funds and senior approval.
- **Beneficial owner**: a natural person who ultimately owns or controls a legal entity.
- **Politically exposed person (PEP)**: someone who holds or held a prominent public role, or a close family member or associate.
- **Money laundering**: making criminal proceeds appear legitimate, through placement, layering and integration.
- **Typology**: a recognised pattern of criminal behaviour used to design controls.
- **Structuring**: splitting transactions to stay below thresholds that would trigger checks or reports.
- **Transaction monitoring**: comparing activity with expected behaviour and typologies to flag exceptions.
- **Blockchain analytics**: tools that cluster and label addresses on public ledgers to trace the history of funds.
- **Suspicious activity report**: a report of suspected money laundering or terrorist financing to a financial intelligence unit.
- **Tipping off**: improperly alerting a customer that a report or investigation exists.
- **Sanctions**: legal restrictions on dealings with listed countries, entities and people.
- **Travel rule**: the requirement that originator and beneficiary information accompany transfers between service providers.
- **Unhosted wallet**: a wallet controlled directly by its user rather than held at a service provider.
- **Regulatory perimeter**: the boundary between activities that need a licence or registration and those that do not.
- **Howey test**: the US test for an investment contract: investment of money, common enterprise, expectation of profit from others' efforts.
- **Fair market value**: the open-market price of an asset at a given moment.
- **Cost basis**: the amount treated as paid for an asset, used to compute gain or loss.
- **Lot**: a specific acquisition of an asset at a particular time and cost.
- **Risk register**: a list of risks with scores, controls and owners.
- **Three lines**: the division of risk responsibilities between business teams, oversight functions and independent audit.

## Review questions

1. What does the principle "same activity, same risk, same rules" mean for a business planning a new digital asset feature?
2. What are the four parts of customer due diligence?
3. Why is a politically exposed person subject to enhanced due diligence, even though being one is not wrongdoing?
4. What happens in each of the three stages of money laundering?
5. In Worked example 1, why is reducing alerts from 120 to 40 only an improvement if it is tested against past cases?
6. Why does the series of payments in Worked example 2 justify a review even though no single payment crossed the threshold?
7. What is tipping off, and why must staff avoid it?
8. Why should a business not return funds to a sender it has identified as sanctioned?
9. What practical problems arise in applying the travel rule to digital asset transfers?
10. What are the four elements of the Howey test?
11. A business is paid 0.05 bitcoin when the price is 60,000 dollars and sells it at 54,000 dollars with a 15-dollar fee. What are its income and its gain or loss?
12. Why can the choice of lot-selection method change the reported gain on the same sale, and why can a business not choose freely after the fact?
13. What custody controls reduce the risk of key theft by an outsider or an insider?
14. In Worked example 5, why did incomplete tax records score higher than a sanctions breach?
15. In the SKA field case, why was a single outgoing filter chosen instead of fixing each screen?

## Answer key

1. The business should ask what the feature actually does (transfer value, offer an investment, earn income, sell to consumers) and identify the laws covering that activity, rather than asking whether crypto as such is regulated.
2. Identification and verification; identifying beneficial owners; understanding the purpose and nature of the relationship; and ongoing monitoring.
3. Their public role could expose them to bribery or corruption, so the risk that funds are proceeds of crime is higher, which calls for closer checks such as source of wealth and senior approval.
4. Placement introduces criminal proceeds into the financial system; layering moves them through many transactions to hide their origin; integration brings them back as apparently legitimate funds.
5. Fewer alerts save analyst time only if the rule still catches the genuinely suspicious cases. Testing against past data confirms it would have flagged every case that was actually reported.
6. Together the payments total 11,730 dollars in five days, all just below the 3,000-dollar threshold, and far above the customer's stated expected activity. That pattern matches structuring, so it warrants review.
7. Telling a customer, directly or indirectly, that a suspicious activity report has been made or an investigation is under way. It can let criminals move funds or destroy evidence, and it is prohibited in most regimes.
8. Returning funds is itself a transfer to a sanctioned party, which may be prohibited. The business should freeze or hold the funds as the law requires and report.
9. Identifying whether an address belongs to a service provider and which one; transmitting customer data separately from the public chain, across protocols that may not interoperate; handling unhosted wallets; and dealing with countries that have not yet implemented the rule.
10. An investment of money, in a common enterprise, with an expectation of profits, coming from the efforts of others.
11. Income of 0.05 × 60,000 = 3,000 dollars. Net proceeds are 0.05 × 54,000 − 15 = 2,685 dollars, so there is a loss of 2,685 − 3,000 = −315 dollars.
12. Different lots have different cost bases, so selecting different units changes the basis subtracted from the same proceeds. Tax systems regulate the permitted methods and require records made at the time, so a business must apply its permitted method consistently.
13. Keeping most assets in cold storage, requiring several approvals through multisig or multi-party computation, separating duties, using address allow-lists and transfer limits, and recording and testing key procedures.
14. Without a system, incomplete records were almost certain to occur and affect every transaction (likelihood 4, impact 3, score 12), whereas a sanctions breach was less likely (likelihood 2) despite its maximum impact (score 10).
15. A single point that every response passes through covers every existing and future screen automatically, is easier to test, and does not depend on each separate feature remembering to apply the rule.

## Further reading

- Financial Action Task Force (2021). *Updated Guidance for a Risk-Based Approach to Virtual Assets and Virtual Asset Service Providers*. FATF, Paris.
- Financial Action Task Force. *The FATF Recommendations*. FATF, Paris (regularly updated).
- Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller and Steven Goldfeder (2016). *Bitcoin and Cryptocurrency Technologies*. Princeton University Press.
- Satoshi Nakamoto (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System."
