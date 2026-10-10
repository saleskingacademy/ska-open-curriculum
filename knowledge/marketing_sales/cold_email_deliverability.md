---
key: cold_email_deliverability
title: "Cold Email Deliverability"
program: marketing_sales
course_level: 3
dna16: ""
l4_address: "S6:P1455791645"
chain256_anchor: "0949828406214500041943396163300415528101920130041595195200041432034970061665495402664952797930041267087802973004175695180948391700175361779104661317845234613004167692417436300406586026996392770331625003328211168402566159300416888919290330041554982466415862"
updated_at: "2026-10-08"
generated_by: "Sales King Academy knowledge base, expanded by Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Cold Email Deliverability

A cold email that never reaches the inbox cannot start a conversation, no matter how well it is written. Deliverability is the set of technical, behavioral and legal conditions that decide whether a message from an unknown sender is accepted by the receiving server, placed in the inbox rather than the spam folder, and kept there over time. This chapter treats deliverability as an engineering and management discipline for the prospecting professional. It explains how mail actually travels and is judged, how sender identity is proven with SPF, DKIM and DMARC, how reputation is earned and lost, how to plan sending infrastructure and volume, how to keep lists clean, how to write messages that filters and people both accept, how to measure inbox placement honestly, and how to stay inside the law and the rules mailbox providers publish. The goal is not to trick filters. The goal is to send mail that deserves to be delivered and to prove it in every way the receiving systems check.

## Learning objectives

1. Describe the path of an email from the sending server to the recipient's inbox and name the checks applied at each stage.
2. Distinguish a sending platform, a mailbox provider and a mail transfer agent, and explain which of them controls each deliverability decision.
3. Configure and audit SPF, DKIM and DMARC records for a sending domain, including alignment and the SPF lookup limit.
4. Explain how domain and IP reputation are formed from bounces, complaints, spam-trap hits and engagement, and why reputation is the dominant factor for cold outreach.
5. Design a sending infrastructure and warm-up plan with defensible per-mailbox volume limits.
6. Calculate and interpret bounce rate, complaint rate, inbox placement rate and reply rate, and set alert thresholds for each.
7. Build a list-hygiene process covering sourcing, verification, suppression and decay.
8. Write cold messages whose structure, links and wording reduce filtering risk without resorting to evasion tricks.
9. Apply the main legal regimes and published mailbox-provider sender requirements to a cold email program, and recognize when to obtain legal advice.
10. Diagnose a deliverability decline using a structured troubleshooting sequence.

## Overview

> The course teaches applied practice of cold email deliverability, assuming foundational knowledge of email marketing and related concepts.

Professional discipline for the prospect specialist: cold email deliverability. Applied practice used to generate revenue.

Cold email differs from permission-based marketing email in one decisive way: the recipient did not ask for it. Mailbox providers know that unsolicited mail is where most abuse lives, so they judge a cold sender more strictly and with less benefit of the doubt. A newsletter sent to subscribers can absorb a few complaints because most recipients open and click. A cold sequence sent to strangers has weak positive engagement by nature, so every bounce and every "report spam" click weighs more heavily. The practical consequence is that cold email programs succeed by running small, precise, well-authenticated, low-complaint operations rather than large broadcasts. Throughout this chapter, the unit of thinking is the reputation of a sending domain, and the question to keep asking is: what evidence is this sending behavior giving the receiving system about whether people want this mail?

## Foundations

Cold email deliverability refers to the ability of an email to reach the recipient's inbox, rather than being blocked or filtered as spam. Email deliverability is influenced by the sender's reputation, defined as the sender's history of sending legitimate and engaging emails, which is evaluated by the organizations that receive mail on behalf of recipients. Key vocabulary includes spam trap, an email address used to detect senders with poor list practices, and bounce rate, the percentage of emails that are rejected by the recipient's server. Other crucial terms are IP address, a unique identifier assigned to a device on a network (here, the sending server), and domain, a unique name that identifies a website or email address. Understanding these first principles and definitions is essential for optimizing cold email deliverability.

A practitioner must use the actors' names precisely, because careless naming leads to fixing the wrong thing. An **Email Service Provider (ESP)** in deliverability language is the platform that sends mail for you: a sales engagement tool, a transactional email service or a marketing automation system. A **mailbox provider** (sometimes still called an ISP, for Internet Service Provider, from the era when access providers also hosted mailboxes) is the organization that hosts the recipient's mailbox and decides where your message lands; consumer webmail services and corporate email platforms are mailbox providers. The original term "ESP, such as Gmail or Outlook" mixes these roles: those services are mailbox providers when they receive your mail and only act as your sending service when you send from an account hosted there, which is common in cold email. A **Mail Transfer Agent (MTA)** is the software that routes and delivers email between servers using the Simple Mail Transfer Protocol (SMTP).

**SPF (Sender Policy Framework)**, **DKIM (DomainKeys Identified Mail)**, and **DMARC (Domain-based Message Authentication, Reporting, and Conformance)** are authentication protocols that let a receiver verify that a message really comes from the domain it claims. **Bounce rate** measures the percentage of emails rejected by the recipient's server, while **complaint rate** tracks the percentage of recipients who mark an email as spam.

Four further ideas complete the foundation:

- **Delivery versus deliverability.** Delivery means the receiving server accepted the message instead of rejecting it. Deliverability, or inbox placement, means it reached the inbox rather than the spam or junk folder. A sending tool that reports "98% delivered" says nothing about where those messages were placed. Many beginners confuse the two and conclude that their mail is fine when most of it sits in spam.
- **Reputation is attached to identifiers.** Receivers track reputation against the sending IP address, the domain in the visible From address, the domain that signs with DKIM, the domains of links in the body and, increasingly, the combination of these. Moving to a new IP does not escape a bad domain reputation, and a new domain does not escape bad content or bad targeting.
- **Filtering is probabilistic and personal.** There is no single score that passes or fails a message everywhere. Each mailbox provider uses its own models, and many personalize placement to the individual recipient based on how that person has treated similar mail. Two colleagues at the same company can receive the same message in different folders.
- **Engagement is evidence.** Replies, moving a message out of spam, adding the sender to contacts and reading without deleting are positive signals. Deleting unread, ignoring, and reporting spam are negative. Cold email cannot manufacture positive engagement, but it can avoid generating negative engagement by sending only relevant messages to people likely to care.

## Mechanisms

The process of cold email deliverability involves a series of steps that determine whether an email reaches the recipient's inbox. The original course summarized it as two overlapping causal chains; they are merged and corrected here into one accurate sequence.

1. **Submission.** The sender's mail client or sending platform submits the message to an outgoing MTA. In most cold email setups this is the outgoing server of the hosted mailbox (a workplace email account) rather than a bulk-sending server.
2. **Connection and SMTP conversation.** The outgoing MTA looks up the recipient domain's MX (mail exchanger) records in DNS and opens an SMTP connection to the receiving MTA. Before the message body is even transferred, the receiver can evaluate the connecting IP address against its own reputation data and against public and private blocklists (historically called blacklists). A badly listed IP can be refused at this stage.
3. **Envelope and authentication checks.** The receiver checks SPF against the envelope sender (the return-path domain), verifies any DKIM signatures against public keys published in DNS, and then evaluates DMARC, which asks whether at least one of those passing results is aligned with the domain in the visible From header. The DMARC policy published by the sender's domain tells the receiver what the domain owner wants done with failures.
4. **Content and link analysis.** The message is scanned for known malicious attachments, suspicious links, link domains with poor reputation, formatting associated with abuse, and language patterns that statistical classifiers (Bayesian filters and modern machine-learning models) associate with spam or phishing. Content rarely rescues a bad reputation, but poor content can push a borderline sender into spam.
5. **Reputation and engagement evaluation.** The receiver combines the evidence above with its history for the sending domain, IP and link domains, and with recipient-level history. This is the dominant step for cold senders.
6. **Placement.** The message is placed in the inbox, a secondary tab or category, the spam folder, or quarantine; or it is rejected with a bounce message, or occasionally accepted and silently discarded.
7. **Client-side and user-defined filtering.** Corporate security gateways, mail client rules and the recipient's own filters may move or hold the message after the provider's decision.
8. **Feedback.** The recipient's actions (reply, ignore, delete, report spam) feed back into reputation and affect the placement of the next message from the same sender. Some providers send complaint reports to registered senders through feedback loops; many large providers instead publish aggregate dashboards.

The causal chain is therefore: sending MTA → DNS and connection checks (IP reputation, blocklists) → authentication (SPF, DKIM, DMARC alignment) → content and link scanning → domain and recipient-level reputation → placement → local filtering → recipient behavior → updated reputation. The content filter examines the email's attachments, links, and images for malicious content. The IP reputation check assesses the sender's IP address to determine if it has been used to send spam in the past. If the email fails decisively, it may be rejected outright; if it is merely suspicious, it is usually routed to a spam folder, which the sender cannot see without testing.

Two corrections to common beliefs belong here. First, the receiver does not usually check content before authentication; authentication and connection-level reputation are evaluated early because they are cheap and decisive. Second, passing authentication does not earn inbox placement. Authentication proves who you are; reputation decides whether who you are is welcome.

## How Email Authentication Works

Authentication is the foundation of every deliverability program, and since the major mailbox providers began enforcing published sender requirements, unauthenticated mail from a business domain is increasingly rejected outright. A practitioner should be able to read and write each record.

### SPF

SPF lets a domain publish, in a DNS TXT record, the list of servers allowed to send mail using that domain in the envelope sender (the return-path, also called the bounce address or MAIL FROM). A simplified record looks like `v=spf1 include:mail.example-provider.net ip4:203.0.113.10 -all`. Each mechanism is evaluated left to right: `include` pulls in another domain's SPF policy, `ip4` and `ip6` list addresses, `a` and `mx` authorize the domain's own A or MX hosts, and the final `all` sets the default result for anything not matched. A hard fail qualifier (`-all`) asks receivers to treat unlisted senders as failing; a soft fail (`~all`) marks them as suspicious.

Three properties of SPF matter in practice. First, the specification limits evaluation to ten DNS-querying mechanisms (such as `include`, `a`, `mx`, `exists` and `redirect`) including those nested inside included records; exceeding the limit produces a permanent error, which receivers treat as an SPF failure. Organizations that add every new tool to their SPF record eventually break it. Second, a domain may have only one SPF record; publishing two produces an error. Third, SPF authenticates the envelope sender, not the visible From address, and it usually breaks when mail is forwarded, because the forwarding server is not in the original domain's list.

### DKIM

DKIM attaches a cryptographic signature to each message. The sending system signs selected headers and the body with a private key and adds a `DKIM-Signature` header naming the signing domain (`d=`) and a selector (`s=`). The receiver retrieves the public key from DNS at `selector._domainkey.domain` and verifies the signature. A valid signature proves that a server holding the domain's private key signed the message and that the signed parts were not altered in transit. The original course text stated that DKIM "encrypts emails"; that is incorrect. DKIM signs messages; it does not hide their content. Encryption in transit is a separate matter handled by TLS between servers.

Good DKIM practice includes using keys of adequate length (2048-bit RSA keys are the common recommendation), signing with your own domain rather than only your sending vendor's domain, rotating keys periodically, and keeping separate selectors for separate sending services so that one can be revoked without affecting the others. DKIM usually survives forwarding as long as the forwarder does not modify the signed content, which makes it the more robust of the two authentication results.

### DMARC

DMARC ties SPF and DKIM to the domain a human actually sees, the one in the From header. A message passes DMARC when SPF passes and the return-path domain aligns with the From domain, or when DKIM passes and the signing domain aligns with the From domain. Alignment can be relaxed (the organizational domains match, so `mail.example.com` aligns with `example.com`) or strict (exact match). The DMARC record is a TXT record at `_dmarc.domain`, for example `v=DMARC1; p=quarantine; rua=mailto:dmarc-reports@example.com; adkim=r; aspf=r`.

The `p` tag sets the policy: `none` (monitor only), `quarantine` (treat failures as suspicious, usually spam folder) or `reject` (refuse failures). The `rua` tag requests aggregate reports, which are XML summaries sent by receivers listing which IP addresses sent mail claiming your domain and whether it passed. A `pct` tag allows applying a policy to a percentage of failing mail during a rollout, and an `sp` tag sets the policy for subdomains.

The standard rollout path is to publish `p=none` with aggregate reporting, read the reports for several weeks to find every legitimate source of mail using the domain, fix authentication for each, and then move to `quarantine` and eventually `reject`. Moving straight to `reject` without this inventory risks blocking your own invoices, support tickets and calendar invitations. For cold email, DMARC matters in two ways: the major providers expect a DMARC record from senders, and a domain with an enforced policy is harder for criminals to spoof, which protects the reputation you are building.

### BIMI and other signals

BIMI (Brand Indicators for Message Identification) lets a domain publish a logo that participating mailbox providers can display next to authenticated messages. It requires DMARC at an enforcement policy (quarantine or reject), and some providers also require a mark certificate that verifies the organization's right to the logo. The original course described BIMI as a method that "improves deliverability"; more precisely, BIMI is a display feature that rewards strong authentication. It does not lift a poor reputation, and for most cold email programs it is a low priority compared with reputation and list quality. Related transport-security standards such as MTA-STS and TLS reporting protect mail in transit and are good hygiene for a domain, but they are not placement levers.

## Sender Reputation in Depth

Reputation is a running estimate, held separately by each mailbox provider, of how much recipients want mail from a given identifier. No provider publishes its formula, and none uses a single number that a sender can look up and game. What practitioners can know is which inputs consistently move reputation.

**Negative inputs.** Hard bounces to non-existent addresses show that the sender is mailing a stale or guessed list. Spam complaints are the strongest negative signal because they are explicit human judgments. Spam-trap hits reveal poor sourcing: a pristine trap is an address that was never used by a person and can only be on a list that was scraped or bought; a recycled trap is an abandoned address that a provider reactivated to catch senders who never remove inactive contacts; a typo trap catches lists with unverified, misspelled entries. Sudden volume spikes from a sender with no history look like a compromised or disposable account. Identical content sent to many recipients at once resembles a broadcast campaign rather than individual correspondence.

**Positive inputs.** Replies are the most valuable signal in cold email and the reason that sequences designed to start real conversations deliver better than sequences designed to push clicks. Recipients rescuing a message from spam, adding the sender to their contacts or forwarding the message internally also help. Consistent, predictable sending volume over months builds trust.

**Domain versus IP reputation.** In the era when most bulk mail came from dedicated IP addresses, IP reputation dominated. Today most cold email is sent through large hosted mailbox platforms whose outbound IP addresses are shared by millions of users; the receiving provider cannot rely on those IPs to judge an individual sender, so domain reputation carries most of the weight. This is why practitioners isolate cold outreach on separate domains: a reputation problem in outreach should not degrade the primary domain used for customer communication, invoices and executives' mail.

**Third-party reputation scores.** Commercial services publish reputation scores for IP addresses and domains derived from their own data networks. The original course referred to a "Sender Score Formula"; the widely used Sender Score is a proprietary 0 to 100 rating of IP reputation from a commercial vendor, and its exact formula is not public. Such scores are useful as one external indicator, especially for dedicated IPs. They do not represent what any particular mailbox provider thinks, and a sender should never treat any third-party score as the single measure of deliverability.

**Provider dashboards.** Large mailbox providers offer tools in which a verified domain owner can see aggregated data about mail the provider received from that domain, such as user-reported spam rate, authentication pass rates and a coarse reputation indicator. These dashboards generally show data only once a sender's daily volume to that provider is large enough, so very small cold programs may see little. When data is available, it is the closest view a sender gets of a provider's own judgment.

## Sending Infrastructure and Warm-up

### Domain strategy

The standard architecture for a professional cold email program separates three kinds of mail. The **primary domain** carries customer, partner, billing and internal mail and must be protected at all costs. **Outreach domains** are additional registered domains that are clearly related to the brand (for example, a variation of the company name) and that redirect their website to the main site so that a curious recipient finds a real company. **Marketing or transactional subdomains** carry newsletters and product notifications through bulk platforms. Each outreach domain gets its own SPF, DKIM and DMARC records, a functioning website or redirect, and a small number of real, monitored mailboxes with real people's names.

Using outreach domains is a risk-isolation practice, not a license to send more junk. Deceptive "lookalike" domains that impersonate another company, or a constant churn of disposable domains to stay ahead of blocks, are abusive practices that mailbox providers actively detect and that undermine any claim to legitimate business purpose.

### Mailbox and volume limits

Cold email delivers best when each mailbox behaves like a busy professional's mailbox rather than a mass-mailing engine. Practitioners commonly cap each mailbox at a few dozen new cold messages per day, spread through working hours with irregular gaps, with follow-ups counted against the same limit. The exact figure is a judgment, not a published rule, and conservative programs stay well below the platform's technical sending limits, which exist to stop abuse rather than to define good practice. Total program volume is then a function of the number of mailboxes, which is why capacity planning (Worked example 4) starts from the meeting target and works backward.

### Warm-up

A new domain or mailbox has no reputation. Sending hundreds of messages on its first day looks exactly like a compromised account. Warm-up is the practice of starting with low volume and increasing gradually while watching bounce and complaint signals, so that the receiving systems accumulate a history of normal behavior. A typical plan begins with a handful of messages per mailbox per day, sent first to known contacts and genuinely interested recipients who are likely to reply, and increases in modest steps over several weeks.

Many sending tools offer automated "warm-up networks" in which participating mailboxes exchange messages and automatically open, reply to and rescue each other's mail. Practitioners disagree about their value. Proponents argue they build early engagement history. Critics argue that providers can identify these networks' patterns, that the engagement is artificial, and that a program which needs artificial engagement indefinitely has a targeting problem that warm-up cannot fix. This chapter's position is that real, low-volume sending to well-chosen recipients is the most defensible warm-up, and that any automated network should be treated as a temporary supplement, never as a substitute for relevance.

### Tracking domains and links

Open and click tracking rewrites links through a tracking domain and inserts a tiny image. Shared tracking domains used by many customers of a sending platform carry the reputation of all those customers. A custom tracking domain on your own outreach domain isolates you from others' behavior. Many practitioners disable open tracking for first-touch cold messages entirely, because open data has become unreliable (some mail clients preload images automatically, recording "opens" that never happened, and others block them) and because tracking pixels and rewritten links add filtering risk. Reply rate is a better primary metric for cold email.

## List Quality and Hygiene

The single most controllable cause of poor cold email deliverability is a poor list. Hygiene begins with sourcing and continues for the life of the program.

**Sourcing.** Contacts should come from sources that give a reasonable basis to believe the person exists, holds the stated role and would plausibly find the message relevant: professional data providers with documented collection practices, company websites, event attendee lists shared with permission, and the seller's own research. Purchased bulk lists of unknown origin, scraped addresses and guessed address patterns carry high bounce and trap risk. The original text warned against purchased or rented lists; that warning stands, with the clarification that the problem is unknown provenance and irrelevance, not the act of paying a vendor.

**Verification.** Before first contact, every address should be checked by an email verification service, which tests syntax, domain existence, MX records and, where the receiving server allows it, mailbox existence. Results typically fall into valid, invalid, risky and unknown. Catch-all domains, which accept mail for any address, cannot be fully verified; addresses at catch-all domains should be sent in small numbers and watched closely, because some of them will bounce later or be silently discarded.

**Suppression.** A permanent suppression list must contain every hard-bounced address, every person who asked not to be contacted, every person who complained, existing customers being managed by another team, and any domains your organization has agreed not to prospect. Suppression must be enforced across every sending tool and every team member. A contact who opts out of one rep's sequence and receives another rep's sequence the next week will reasonably report spam.

**Decay.** Business contact data decays as people change jobs, companies rename domains and mailboxes are closed. A list that verified clean six months ago is not clean today. Reverify before each new campaign and remove addresses that have not been contacted or verified recently.

**Bounce handling.** A hard bounce (a permanent failure such as "user unknown" or "domain does not exist") must be suppressed immediately and never retried. A soft bounce (a temporary failure such as "mailbox full" or "try again later") may be retried a limited number of times; repeated soft bounces should be treated as hard. A block bounce, in which the receiver refuses mail because of the sender's reputation or a policy, is a signal about you rather than the address and calls for stopping and investigating, not retrying harder.

## Content That Filters and People Accept

Content contributes less to deliverability than reputation and list quality, but it is the part a writer controls in every message. The principles below aim at messages that look and read like a professional writing to one person.

1. **Plain text or light HTML.** Cold messages that resemble personal correspondence (short paragraphs, no heavy templates, no large images) are classified more like personal mail. Image-only messages and messages with large image-to-text ratios are a classic spam pattern.
2. **Few links, none shortened.** One link, or none in the first message, is typical. Public link shorteners hide the destination and are heavily abused. Every link domain should have a good reputation, because receivers judge the links as well as the sender.
3. **No attachments on first contact.** Unsolicited attachments are a leading malware vector and are filtered aggressively by corporate gateways.
4. **Honest, specific subject lines.** The original text warned against generic or misleading subject lines; this is both a filtering issue and, under several laws, a legal one. Subject lines should describe the message accurately. Fake "Re:" or "Fwd:" prefixes that imply an existing conversation are deceptive.
5. **Restrained formatting.** Using all caps or excessive punctuation in the email body can be perceived as spammy, as can heavy use of urgency language, currency symbols and claims of free money. These are not banned words; classifiers weigh them in context. Writing like a professional is the reliable defense.
6. **Real personalization, not merge-field variety.** Genuine relevance (a specific reason this person, at this company, now) improves replies, which improve reputation. "Spintax" that randomizes synonyms to make identical bulk messages look unique is an evasion technique; it does not make irrelevant mail relevant and should not be the basis of a program.
7. **A clear way to opt out.** Even where a law does not mandate a specific mechanism for the type of message, giving recipients an easy, respectful way to say "no thanks" converts would-be spam complaints into polite replies or unsubscribes. A complaint harms reputation; an opt-out does not.
8. **A real signature.** A full name, role, company and physical business address signals a real sender and, in several jurisdictions, satisfies a legal requirement.

## Measuring Deliverability

A deliverability program needs a small set of metrics with clear formulas and thresholds. All rates below should be computed per sending domain and per mailbox, not only for the whole program, because problems usually begin in one place.

- **Bounce rate** = bounced messages / sent messages. Track hard and soft bounces separately. **Hard bounce rate** = hard bounces / sent. For verified cold lists, a hard bounce rate that rises above roughly 2% is a widely used warning level, and many practitioners aim for under 1%; these are practitioner thresholds, not published provider rules.
- **Delivery rate** = (sent − bounced) / sent. It measures acceptance, not inbox placement.
- **Complaint rate** = spam complaints / delivered messages. For large providers that publish sender guidance, the user-reported spam rate shown in their dashboards should be kept well below 0.1% and must not reach 0.3%, the level at which they state that senders face enforcement. Cold senders rarely see complaint counts directly, which makes the provider dashboards and reply-based proxies (such as hostile replies) important.
- **Inbox placement rate** = messages placed in the inbox / messages delivered, estimated with seed testing (sending to a panel of test mailboxes across providers and checking where messages land). Seed tests are an estimate: seed mailboxes have no engagement history, so real recipients may see different placement.
- **Reply rate** = replies / delivered. **Positive reply rate** = interested replies / delivered. These are the true outcome metrics of cold email and also the strongest positive deliverability signal.
- **Authentication pass rate** = messages passing DMARC / total messages claiming the domain, from DMARC aggregate reports.

A well-run program reviews these weekly, sets automatic alerts on bounce and complaint thresholds, and pauses a mailbox or domain automatically when a threshold is crossed. Pausing early protects reputation; continuing to send while investigating compounds the damage.

## Laws and Mailbox Provider Requirements

Deliverability and legality overlap: mail that breaks the law tends to generate complaints, and mailbox providers increasingly codify legal and ethical expectations into technical requirements. This section explains principles; it is not legal advice, and a program sending across borders should be reviewed by qualified counsel.

**United States: CAN-SPAM.** The CAN-SPAM Act applies to commercial email, including business-to-business messages. It does not require prior consent; it is an opt-out regime. Its core requirements are: header information must not be false or misleading; subject lines must not be deceptive; commercial messages must be identifiable as such; the message must include the sender's valid physical postal address; it must give a clear way to opt out of future messages; opt-out requests must be honored within ten business days, and the opt-out mechanism must work for at least 30 days after the message is sent; and a company remains responsible for compliance when it hires another party to send for it. Penalties are assessed per violating message and adjusted over time, so the exposure from a large non-compliant campaign can be severe. The original course stated that non-compliance "can lead to blacklisting"; more precisely, non-compliance creates legal liability, while blocklisting results from the complaints and abusive patterns that non-compliant mail tends to cause.

**European Union and United Kingdom.** Under the GDPR, a business email address that identifies a person (such as firstname.lastname at a company) is personal data, so the sender needs a lawful basis for processing it. Cold B2B outreach typically relies on legitimate interests, which requires a documented balancing test, a clear connection between the offer and the person's professional role, transparency about where the data came from, and an easy way to object. Separate electronic-marketing rules (the ePrivacy framework in EU member states, implemented differently by each, and the UK's Privacy and Electronic Communications Regulations) govern unsolicited marketing email; under the UK rules, for example, emails to corporate subscribers are treated more permissively than emails to individual subscribers such as sole traders. Because national implementations differ, a single rule for "Europe" does not exist.

**Canada.** Canada's anti-spam legislation (CASL) is consent-based: commercial electronic messages generally require express or implied consent, with implied consent available in defined situations (for example, where a person has conspicuously published their business address without a statement refusing messages and the message relates to their business role). CASL also requires sender identification and an unsubscribe mechanism.

**Other jurisdictions.** Australia, Singapore and many other countries have their own rules, several of them consent-based. The safe operating principle is to determine, before launching, which countries the recipients are in and to apply the strictest applicable regime for each segment.

**Mailbox provider requirements.** Beginning in 2024, the largest consumer mailbox providers published and began enforcing requirements for senders, with the strictest rules applying to bulk senders (Google, for example, defines bulk senders as those sending roughly 5,000 or more messages a day to its users). The requirements include authenticating with SPF and DKIM, publishing a DMARC record with at least a monitoring policy and alignment for bulk senders, keeping user-reported spam rates low (below 0.3%, with lower targets recommended), supporting one-click unsubscribe for marketing and subscribed messages, and using valid forward and reverse DNS and TLS for sending servers. Microsoft has announced comparable requirements for its consumer mailboxes. Most individual cold email mailboxes send far below bulk thresholds, but providers apply the spirit of these rules to everyone, and a growing program can cross the threshold in aggregate across a domain. Treat these requirements as the minimum baseline for all outreach.

**Ethics.** Beyond the law, cold outreach is a privilege granted by a shared communication system. A practitioner who sends only to people with a plausible professional interest, says who they are, makes stopping easy and stops when asked is behaving in a way that preserves the channel for everyone, including future versions of their own program.

## Methods And Frameworks

The original course listed several methods twice with slightly different wording; the descriptions below merge each into one entry and add when to use it and how it fails.

**The Bounce Rate Method** involves tracking the percentage of emails that bounce back, and in particular the hard bounce rate, as an early indicator of list quality. Use it when launching any new list or campaign, because it is the first metric to move. Failure mode: over-reliance on bounce rates alone, neglecting spam-folder placement, which produces no bounce at all.

**Sender reputation scoring** (the original "Sender Score Formula") uses external reputation ratings and provider dashboards to estimate how receivers view the sender. Apply it for regular reputation checks. Failure mode: misinterpreting any single score as the sole indicator of deliverability, or ignoring other factors like content, list quality and recipient engagement.

**The CAN-SPAM Compliance Framework** ensures adherence to the US commercial email law: truthful headers and subject lines, identification, physical address, a working opt-out and timely honoring of opt-outs. Use it for all commercial emails sent to US recipients, alongside the rules of every other jurisdiction involved. Failure mode: incomplete or inaccurate implementation, such as opt-outs recorded in one tool but not suppressed in another, leading to legal exposure and complaints.

**The IP and Domain Warm-up Method** gradually increases email volume from a new IP address, domain or mailbox so that receivers accumulate a history of normal behavior. Use it when introducing any new sending identity. Failure mode: rushing the warm-up process, triggering spam filters, or relying indefinitely on artificial warm-up traffic instead of relevant sending.

**The Content Scoring Model** evaluates email content's spam likelihood based on keywords, links, and formatting, usually with a pre-send testing tool. Apply it when crafting templates. Failure mode: over-reliance on content scoring, neglecting the reputation and list factors that dominate placement, or "optimizing" toward evasion rather than clarity.

**The Domain Alignment Method** ensures that the From domain, the DKIM signing domain, the return-path domain and the link domains are consistent with each other and with the sender's identity. Use it when setting up new domains and whenever a new sending tool is added. Failure mode: inconsistent domain alignment that confuses recipients and spam filters and fails DMARC, or neglecting ongoing monitoring after setup.

**The Engagement-Based Method** prioritizes sending to recipients most likely to engage and stops sending to those who show no interest. Apply it when optimizing sequences. Failure mode: over-emphasizing a single engagement metric, particularly open rates that are distorted by privacy features.

**The authentication stack (SPF, DKIM, DMARC, BIMI).** SPF verifies which servers may send for the envelope domain; use it for every domain that sends mail, and keep it within the lookup limit. Its failure mode is outdated, duplicate or overlong records. DKIM signs messages so receivers can verify the signing domain and message integrity; use it for every sending service, with your own domain as signer. Its failure mode is incorrect key management, such as an expired or unpublished selector. DMARC aligns authentication with the visible From domain and tells receivers how to handle failures; use it on every domain, moving from monitoring to enforcement as reports confirm legitimate sources. Its failure mode is a misconfigured policy that blocks legitimate mail, or a monitoring policy left in place forever with nobody reading the reports. BIMI displays a verified logo once DMARC is enforced; it is worth adopting when brand recognition in the inbox matters. Its failure mode is incorrect DNS setup or a logo file that does not meet the required format.

**The Deliverability Triangle (SKA framework).** For diagnosis and planning, this course groups all of the above into three sides that must all be strong: **Identity** (authentication and alignment, domain setup, infrastructure), **Reputation** (history of bounces, complaints, traps and engagement, built by volume discipline) and **Relevance** (list quality, targeting and content). A weakness in any side limits the whole: perfect authentication cannot save an irrelevant list, and a perfect list cannot overcome a domain that fails DMARC. When placement drops, check the sides in that order, because identity problems are the fastest to find and fix.

## Diagnosing a Deliverability Problem

When replies fall or a seed test shows spam placement, a structured sequence prevents guesswork.

1. **Confirm the symptom.** Is the decline real and recent? Compare reply rate per mailbox and per domain over the last four weeks. Run a seed test and, if possible, ask a friendly contact at a large provider to check their spam folder.
2. **Localize it.** Is the problem on one mailbox, one domain, one provider, one campaign or everywhere? A single mailbox points to its own behavior or account status. A single provider points to that provider's view of your domain. Everywhere points to the domain, content shared across campaigns, or a link domain.
3. **Check identity.** Look up the SPF, DKIM and DMARC records, confirm the lookup count, confirm the DKIM selector is still published, and read recent DMARC aggregate reports for failures or unknown sources. A changed DNS setting or a newly added tool is a common cause.
4. **Check blocklists and dashboards.** Look up the sending domain and any dedicated IPs on major public blocklists, and review provider dashboards where available.
5. **Check list and behavior.** Review bounce rates, recent list sources, volume changes and any campaign launched just before the decline. A new list from an unverified source is the most common single cause.
6. **Check content and links.** Look for a new link domain, an added attachment, a tracking change or a template that changed format.
7. **Act and recover.** Pause or reduce volume on affected identities, fix the cause, remove risky segments, and resume slowly with the most engaged and most relevant recipients. Recovery takes weeks, because reputation is rebuilt by accumulated good behavior, not by a single fix. Request delisting from a blocklist only after the underlying cause is corrected.

## Worked Examples

To illustrate the principles of cold email deliverability, consider the following scenarios. The original course gave two versions of the warm-up and bounce examples with conflicting numbers; each has been reduced to one corrected version. All company names are fictional, and all numbers are illustrative and were checked by calculation.

### Worked example 1: Planning a domain warm-up

A fictional company, XYZ Inc., wants to send cold emails from a new outreach domain. It plans to start with 100 emails on day 1 across all its new mailboxes and increase the daily volume by 20% each day. The original example claimed that on day 7 it would reach 1,342 emails; that figure is wrong.

Volume on day *d* is 100 × 1.2^(d − 1).

- Day 7: 100 × 1.2^6 = 298.6, or about 299 emails.
- Total sent over days 1 to 7: 100 × (1.2^7 − 1) / 0.2 = 1,291.6, or about 1,292 emails.
- Day on which daily volume first exceeds 1,000: solve 1.2^(d − 1) ≥ 10, giving d − 1 ≥ ln 10 / ln 1.2 = 12.63, so d − 1 = 13 and d = 14. On day 14 the plan calls for 100 × 1.2^13 = 1,069.9, about 1,070 emails.

Interpretation: compound growth looks gentle at first and then becomes steep. A 20% daily increase multiplies volume by more than ten in two weeks, which is aggressive for brand-new identities. The plan should also respect a per-mailbox cap: reaching about 1,070 emails a day at no more than 30 per mailbox would require 36 mailboxes (1,070 / 30 = 35.7, rounded up), which is a sign that the target volume, not the warm-up curve, is the real problem. A better plan increases slowly, holds each level for several days while watching bounces and complaints, and sizes total volume from the meeting target (Worked example 4).

### Worked example 2: Bounce rate and complaint rate

A campaign is sent to 5,000 recipients and results in 250 hard bounces and 50 soft bounces. Six recipients report the message as spam (known here because the sending platform receives complaint feedback).

- Total bounce rate = (250 + 50) / 5,000 = 6.0%.
- Hard bounce rate = 250 / 5,000 = 5.0%. Soft bounce rate = 50 / 5,000 = 1.0%.
- Delivered = 5,000 − 300 = 4,700.
- Complaint rate = 6 / 4,700 = 0.128%.
- If a seed test estimates 80% inbox placement, about 4,700 × 0.80 = 3,760 messages reached inboxes.

Interpretation: the hard bounce rate of 5% is far above the roughly 2% warning level and shows that the list was not verified or has decayed. The complaint rate of about 0.13% is above the 0.1% level that large providers recommend staying under and well on the way to their 0.3% enforcement level. Both signals point to list sourcing and targeting, not to content. The right response is to stop the campaign, verify the remaining list, suppress all hard bounces permanently, and tighten targeting before resuming. The original example's second scenario (1,000 sent, 120 bounces, 12% bounce rate) is an even more severe version of the same problem: a 12% bounce rate means roughly one address in eight did not exist.

### Worked example 3: Fixing an SPF record that exceeds the lookup limit

ABC Corp., a fictional company, uses three sending services and its own servers. Its SPF record includes three vendors' policies plus the `a` and `mx` mechanisms. Counting DNS-querying mechanisms, including those nested inside each included policy, gives: vendor A, 3 lookups; vendor B, 4 lookups; vendor C, 2 lookups; `a`, 1; `mx`, 1. Total: 3 + 4 + 2 + 1 + 1 = 11.

Eleven exceeds the limit of ten, so receivers evaluating the record return a permanent error and treat SPF as failed for every message, including those from legitimate vendors. If DKIM is also misaligned for some service, DMARC fails for that mail.

The fix: ABC Corp. finds that its web server never sends mail and its MX hosts only receive mail, so it removes `a` and `mx`, bringing the total to 3 + 4 + 2 = 9. It also notes that vendor C sends only marketing mail and moves that service to a dedicated subdomain with its own SPF record, which keeps the main record well under the limit as new tools are added. Finally, it confirms that each vendor signs with DKIM using ABC Corp.'s own domain, so that DMARC passes through DKIM alignment even when SPF breaks during forwarding.

### Worked example 4: Sizing sending capacity from a meeting target

A sales team wants 20 booked meetings a month from cold email. From its own history, its positive reply rate is 1.5% of delivered messages and half of positive replies become booked meetings. Its delivery rate is 95%. The team works 22 sending days a month and caps each mailbox at 30 new cold messages a day.

- Positive replies needed = 20 / 0.5 = 40.
- Delivered messages needed = 40 / 0.015 = 2,667 (2,666.7 rounded up).
- Messages to send = 2,666.7 / 0.95 = 2,807.
- Messages per sending day = 2,807 / 22 = 127.6.
- Mailboxes needed = 127.6 / 30 = 4.25, rounded up to 5.

Interpretation: five mailboxes, spread across two or three outreach domains so that no domain carries all the volume, can meet the target at conservative per-mailbox volumes. The calculation also shows where leverage lies: if better targeting raised the positive reply rate from 1.5% to 3%, the team could reach the same 20 meetings with half the volume, which means fewer complaints, less reputation risk and less infrastructure. Deliverability and targeting quality reinforce each other.

### Worked example 5: Reading a DMARC aggregate report

After publishing `p=none`, a company's DMARC aggregate reports for one week show 10,000 messages claiming its domain: 9,200 passed with aligned DKIM and aligned SPF; 300 failed SPF (because they were forwarded) but passed aligned DKIM; and 500 came from IP addresses the company does not recognize and failed both.

- DMARC pass rate = (9,200 + 300) / 10,000 = 95%.
- Unrecognized, failing sources = 500 / 10,000 = 5%.

Interpretation: the forwarded messages pass DMARC because DKIM survived forwarding, which is why aligned DKIM matters more than SPF for robustness. The 500 unrecognized messages need investigation. If they come from a forgotten legitimate service (for example, an old survey tool), that service must be authenticated before enforcement, or its mail will be quarantined. If they are spoofing attempts, they are exactly what enforcement is designed to stop. Once every legitimate source is accounted for, the company can move to `p=quarantine` and later to `p=reject`.

### Additional scenario: setting up authentication with a third-party sender

A sender, ABC Corp., uses a third-party sending platform for cold emails. To authenticate their emails and improve deliverability, they set up SPF and DKIM records. With SPF, they specify the servers authorized to send emails on their behalf, reducing the risk of spoofing. With DKIM, they add a digital signature to their emails, verifying the signing domain and ensuring the signed content has not been tampered with during transmission. They then publish DMARC so that receivers can check alignment with the visible From domain. By implementing these authentication protocols, ABC Corp. meets the baseline every receiver now expects and makes its domain harder to impersonate; inbox placement then depends on the reputation it builds through list quality and relevance.

## Case Study

### Case study: Northgate Analytics rebuilds its outbound program

Northgate Analytics is a fictional business-intelligence software company used for teaching; the people, numbers and events are invented.

**Problem.** Northgate's three sales development representatives sent cold email directly from their primary-domain mailboxes using a purchased list of about 40,000 contacts. Each rep sent around 100 messages a day, so the team sent about 300 a day or 6,600 in a 22-day month. Hard bounces ran near 9%, so about 6,006 messages a month were delivered. The positive reply rate had fallen to 0.15% of delivered, producing about nine interested replies and roughly five booked meetings a month. Then the customer success team reported that renewal reminders and invoices from the same domain were landing in customers' spam folders. The domain had published SPF but no DKIM and no DMARC.

**What was done.** Over eight weeks the team:

1. Stopped all cold sending from the primary domain immediately and audited its authentication, adding DKIM signing with the company's own domain and a DMARC record at `p=none` with aggregate reporting.
2. Registered two outreach domains closely related to the brand, each redirecting to the main website, and created six mailboxes under real reps' names, each with SPF, DKIM and DMARC.
3. Discarded the purchased list, rebuilt a smaller list of companies matching their ideal customer profile from their own research and a reputable data provider, and verified every address before use.
4. Warmed the new mailboxes over four weeks, starting with a handful of messages a day to the most relevant contacts and holding at a cap of 25 new messages per mailbox per day, for a total of 150 a day, or 3,300 a month.
5. Rewrote templates as short plain-text messages with no links in the first touch, a specific reason for contacting each account, a full signature with a postal address, and a one-line opt-out offer. Open tracking was disabled.
6. Built a shared suppression list enforced across the sales engagement tool and the CRM, with automatic pausing of any mailbox whose hard bounce rate exceeded 2% in a week.
7. After six weeks of clean DMARC reports on the primary domain, moved it to `p=quarantine`.

**Measured results.** In the eighth week the hard bounce rate on the outreach domains was 0.8%, so about 3,274 of 3,300 monthly messages were delivered. The positive reply rate rose to 1.1% of delivered, producing about 36 interested replies and roughly 20 booked meetings a month at a 55% booking rate. Meetings per 1,000 messages sent rose from about 0.75 to about 6.0, an eightfold improvement while sending half the volume. Customer success reported that invoices and renewal reminders were again reaching inboxes.

**Lessons.**

- Sending less to the right people produced four times as many meetings. Volume was never the constraint; relevance and reputation were.
- Mixing cold outreach with customer mail on one domain put revenue already won at risk. Domain separation is a protection for customers, not a trick.
- Authentication was necessary but did not fix placement by itself; the improvement came when identity, reputation and relevance were all repaired together.
- Automated pausing at a bounce threshold turned a potential crisis into a routine alert.

## Applications

Cold email deliverability is crucial in sales, business development, recruiting, partnerships, fundraising and public relations: every function that must start conversations with people who do not yet know the sender. In B2B sales, cold email is used to initiate contact with potential clients, and high deliverability is essential to ensure that carefully researched messages reach the intended recipients. Sales teams typically send from hosted workplace mailboxes through sales engagement platforms, which add scheduling, sequencing, suppression and reply detection; marketing teams send permission-based campaigns through bulk platforms, which provide domain authentication, bounce handling and complaint processing. Keeping these two streams on separate domains or subdomains is the standard way to stop one from damaging the other.

Strictly speaking, onboarding and support messages sent to existing customers are not cold email; they are relationship mail and should travel on the protected primary domain or a dedicated transactional subdomain. The principles in this chapter still apply to them, especially authentication and list hygiene, and their health depends on keeping cold outreach separate.

Recruiters contacting passive candidates, founders seeking investors, and agencies prospecting for clients face the same mechanisms at smaller scale; for them, the most common failure is sending from a personal or primary domain at a sudden, unwarmed volume. Industries such as finance and healthcare add sector rules on top of general email law, and data protection regimes such as the GDPR and anti-spam laws such as CAN-SPAM and CASL shape who may be contacted and how. By applying cold email deliverability principles, businesses can increase the effectiveness of their outreach, improve conversion rates, and protect the reputation of the domains that carry their customer relationships.

Deliverability work also connects to revenue operations: the capacity model in Worked example 4 links infrastructure decisions directly to pipeline targets, and the metrics in this chapter belong on the same dashboard as meetings booked and pipeline created.

## Common Errors

Practitioners often make mistakes that negatively impact cold email deliverability. The errors below merge and extend the original list.

1. **Sending cold email from the primary domain.** A reputation problem then spreads to customer, billing and executive mail.
2. **Using generic or misleading subject lines,** which trigger filters, generate complaints and can violate law.
3. **Including too many links or attachments,** which raises red flags with filters and corporate security gateways.
4. **Using all caps or excessive punctuation,** which is perceived as spammy by classifiers and people alike.
5. **Failing to warm up new mailboxes and domains** by gradually increasing send volume, producing sudden spikes that look like a compromised account.
6. **Neglecting authentication.** Missing SPF, DKIM or DMARC, a duplicate SPF record, an SPF record over the lookup limit, or DKIM signed only with a vendor's domain all cause failures that are entirely avoidable.
7. **Using purchased or scraped lists of unknown origin** rather than researched, verified contacts, leading to bounces, spam-trap hits and blocklisting.
8. **Not cleaning and reverifying lists,** so that decay causes bounces and complaints.
9. **Neglecting a clear opt-out,** so recipients who want to stop press "report spam" instead.
10. **Treating "delivered" as "inboxed".** Sending-tool delivery rates do not show spam-folder placement.
11. **Relying on open rates,** which privacy features distort, instead of replies.
12. **Continuing to send during a problem.** Every additional message to a provider that is already filtering you deepens the reputation hole.
13. **Moving DMARC straight to reject** without reading reports, blocking legitimate mail from forgotten services.
14. **Fighting filters instead of earning placement.** Spintax, image tricks, hidden text and disposable domains may produce short-term gains but build no durable reputation and may breach provider policies.

These errors can be avoided by understanding how filters and mailbox providers work, and by prioritizing best practices for identity, list management and content.

## Advanced

Cold email deliverability is a dynamic field. Several developments are shaping current practice and remain open questions.

**Machine learning on both sides.** Mailbox providers use large-scale machine-learning models trained on billions of messages and user actions to classify mail, and those models increasingly evaluate patterns across many messages rather than single messages. At the same time, sending tools use artificial intelligence to personalize and time messages. The open question is whether AI-generated personalization at scale produces genuine relevance or simply more varied irrelevance; receiving models trained on user reactions will ultimately reward the former and punish the latter. Human review of targeting and messaging remains important in AI-assisted campaigns.

**Domain reputation over IP reputation.** As more mail is sent from shared infrastructure, and as IPv6 makes IP-based tracking harder, receivers continue to shift weight toward domain-level and organization-level reputation. This makes domain strategy and authentication alignment more important each year.

**Enforcement of sender requirements.** The published requirements of the largest providers turned long-standing best practices (authentication, low complaint rates, easy unsubscribe) into enforced rules. Further tightening, especially around DMARC enforcement and complaint thresholds, is a reasonable expectation. Programs built to the requirements' spirit rather than their minimum letter are best positioned.

**Multi-channel prospecting.** Cold email is increasingly combined with phone, professional social networks and events in coordinated sequences. Well-designed multi-channel outreach can reduce reliance on high email volume, because each touch carries more context, which in turn improves email engagement and reputation.

**Privacy regulation and consent.** Privacy-focused regulations such as the GDPR and California's privacy laws push toward more transparent data sourcing and easier objection. Data providers are under pressure to document provenance, and senders are expected to explain where they obtained contact data. A shift toward more consent-based and permission-based practices, especially for outreach to individuals rather than roles, is likely to continue.

**Measurement limits.** Inbox placement remains hard to observe directly. Seed testing, panel data and provider dashboards each offer a partial view. Researchers and practitioners are investigating better methods, including the use of natural language processing to classify replies (interested, not now, hostile, out of office) as a richer engagement signal than opens or clicks. Key open questions include how to balance deliverability with user privacy and security, how to measure placement without intrusive tracking, and how authentication standards will evolve to handle forwarding and mailing lists more gracefully.

## Summary

Cold email deliverability decides whether outreach reaches a human being. Mail passes through connection checks, authentication, content and link scanning, and reputation evaluation before being placed, and recipient behavior then feeds back into the sender's reputation. Authentication with SPF, DKIM and DMARC proves identity and is now a baseline requirement; SPF must stay within its ten-lookup limit, DKIM signs rather than encrypts, and DMARC requires alignment with the visible From domain and should progress from monitoring to enforcement. Reputation, attached mainly to domains in modern cold email, is built by low bounce and complaint rates, avoidance of spam traps, steady volume and genuine replies. Professional programs isolate outreach on related domains, cap per-mailbox volume, warm up gradually, verify and suppress rigorously, and write short, honest, plain messages with an easy opt-out. They measure bounce, complaint, inbox placement and reply rates per mailbox and domain, pause automatically at thresholds, and diagnose problems in a fixed order: identity, then reputation, then relevance. Legal regimes differ by country, from the opt-out model of CAN-SPAM to the consent-based models of CASL and many European rules, and the largest mailbox providers now enforce their own sender requirements. The durable strategy is to send mail that deserves the inbox and to prove it in every way the receiver checks.

## Key terms

- **Deliverability (inbox placement)**: the ability of a message to reach the recipient's inbox rather than the spam folder or rejection.
- **Delivery rate**: the share of sent messages accepted by receiving servers; it does not show folder placement.
- **Mailbox provider**: the organization hosting the recipient's mailbox and deciding message placement.
- **Email Service Provider (ESP)**: the platform or service that sends mail on the sender's behalf.
- **Mail Transfer Agent (MTA)**: software that routes and delivers email between servers using SMTP.
- **SPF (Sender Policy Framework)**: a DNS record listing servers allowed to send mail for a domain's envelope sender, limited to ten DNS-querying mechanisms.
- **DKIM (DomainKeys Identified Mail)**: a cryptographic signature that lets receivers verify the signing domain and that signed content was not altered.
- **DMARC**: a policy and reporting standard that requires SPF or DKIM to pass in alignment with the visible From domain and tells receivers how to treat failures.
- **Alignment**: the match between the From domain and the domain authenticated by SPF or DKIM, either relaxed (same organizational domain) or strict (exact).
- **BIMI**: a standard for displaying a verified brand logo beside authenticated mail at providers that support it; it requires DMARC enforcement.
- **Sender reputation**: a receiver's running estimate of how much recipients want mail from a sending domain, IP or link domain.
- **Spam trap**: an address used to identify senders with poor list practices; types include pristine, recycled and typo traps.
- **Hard bounce**: a permanent delivery failure, such as a non-existent address, that requires immediate suppression.
- **Soft bounce**: a temporary delivery failure that may be retried a limited number of times.
- **Complaint rate**: spam reports divided by delivered messages.
- **Seed test**: sending to a panel of test mailboxes to estimate inbox placement by provider.
- **Warm-up**: gradually increasing volume from a new sending identity to establish a normal history.
- **Suppression list**: a permanent list of addresses and domains that must never be contacted again by any sender in the organization.
- **Outreach domain**: a separate, brand-related domain used for cold email to isolate reputation risk from the primary domain.
- **Catch-all domain**: a domain whose server accepts mail for any address, making address verification inconclusive.

## Review questions

1. What is the difference between delivery and deliverability, and why does a high delivery rate not prove good inbox placement?
2. Which organization makes the final placement decision for a cold email, and how does it differ from the sender's ESP?
3. What does SPF authenticate, and what happens when an SPF record requires more than ten DNS lookups?
4. Why is the statement "DKIM encrypts emails" incorrect, and what does DKIM actually prove?
5. Under what conditions does a message pass DMARC?
6. Why should a domain begin DMARC at a monitoring policy before moving to quarantine or reject?
7. Why does domain reputation matter more than IP reputation for most modern cold email programs?
8. What are three types of spam trap, and what does hitting each one reveal about a sender's list?
9. Why do professional cold email programs send from outreach domains rather than the primary domain?
10. If a campaign has 250 hard bounces and 50 soft bounces out of 5,000 sends, what are its total and hard bounce rates, and what should the sender do?
11. Why is reply rate a better primary metric than open rate for cold email?
12. What are the main requirements of CAN-SPAM, and does it require prior consent?
13. How does Canada's CASL differ from CAN-SPAM in its basic approach to consent?
14. In what order should a practitioner check the three sides of the Deliverability Triangle when placement drops, and why?
15. Why does adding an easy opt-out to a cold email help deliverability rather than hurt it?

## Answer key

1. Delivery means the receiving server accepted the message; deliverability means it was placed in the inbox. Messages placed in the spam folder count as delivered, so a sending tool can report near-total delivery while most mail sits in spam.
2. The recipient's mailbox provider decides placement. The ESP or sending platform only transmits the sender's mail; it can affect reputation through its infrastructure and practices but does not decide where the mail lands.
3. SPF authenticates the envelope sender (return-path) domain by listing authorized sending servers. If evaluation needs more than ten DNS-querying mechanisms, including nested ones, the result is a permanent error, which receivers treat as an SPF failure.
4. DKIM does not hide content; it adds a cryptographic signature. A valid signature proves that a holder of the signing domain's private key signed the message and that the signed headers and body were not altered in transit.
5. A message passes DMARC when SPF passes with a return-path domain aligned to the From domain, or DKIM passes with a signing domain aligned to the From domain; one aligned pass is enough.
6. Monitoring with aggregate reports reveals every legitimate service sending mail as the domain. Enforcing before those services are authenticated would cause the domain's own legitimate mail to be quarantined or rejected.
7. Most cold email is sent from large shared mailbox platforms whose IP addresses carry mail for many users, so receivers cannot judge an individual sender by IP and rely mainly on the sending domain's history.
8. Pristine traps were never used by people and reveal scraped or bought lists; recycled traps are abandoned addresses that were reactivated and reveal failure to remove stale contacts; typo traps catch misspelled addresses and reveal lack of verification.
9. Outreach domains isolate the higher risk of cold email so that any reputation damage does not affect customer, billing and executive mail on the primary domain, while remaining clearly related to the brand.
10. Total bounce rate is 300 / 5,000 = 6%; hard bounce rate is 250 / 5,000 = 5%. The sender should stop the campaign, suppress all hard bounces permanently, verify the remaining list and improve sourcing before resuming.
11. Replies are real human actions and a strong positive reputation signal, whereas open tracking is distorted by mail clients that preload or block images, and tracking pixels can add filtering risk.
12. CAN-SPAM requires truthful headers and non-deceptive subject lines, identification of the message as commercial, a valid physical postal address, a clear opt-out, honoring opt-outs within ten business days with the mechanism working for at least 30 days, and responsibility for vendors sending on the company's behalf. It does not require prior consent.
13. CASL is consent-based: it generally requires express or implied consent before sending commercial messages, whereas CAN-SPAM permits sending without consent as long as recipients can opt out.
14. Check Identity first, then Reputation, then Relevance, because authentication and configuration problems are the fastest to find and fix and can masquerade as reputation problems, while reputation and relevance issues take longer to diagnose and repair.
15. A recipient who can easily say no will opt out or reply rather than click "report spam"; complaints damage reputation while opt-outs do not, so a clear opt-out converts harmful signals into harmless ones.

## Further reading

- *Email Marketing Rules* by Chad S. White.
- *Fanatical Prospecting* by Jeb Blount.
- *Predictable Revenue* by Aaron Ross and Marylou Tyler.
- RFC 5321, *Simple Mail Transfer Protocol*, Internet Engineering Task Force (J. Klensin).
- RFC 7208, *Sender Policy Framework (SPF) for Authorizing Use of Domains in Email, Version 1*, Internet Engineering Task Force (S. Kitterman).
- RFC 6376, *DomainKeys Identified Mail (DKIM) Signatures*, Internet Engineering Task Force (D. Crocker, T. Hansen, M. Kucherawy, editors).
- RFC 7489, *Domain-based Message Authentication, Reporting, and Conformance (DMARC)*, Internet Engineering Task Force (M. Kucherawy and E. Zwicky, editors).
- RFC 8058, *Signaling One-Click Functionality for List Email Headers*, Internet Engineering Task Force (J. Levine and T. Herkula).
- M3AAWG (Messaging, Malware and Mobile Anti-Abuse Working Group), *Sender Best Common Practices*.
