---
key: conversion_rate_optimization
title: "Conversion Rate Optimization"
program: marketing_sales
course_level: 3
dna16: ""
l4_address: "S6:P40374397"
chain256_anchor: "0967107337367035168996570182266709123002581226671831789663143782019876851667905004291384915926670271007876342667087782123394906904621931160810020589292866902667014550198956266704436439091288530949005017986672001050074125266702313154415526671498409956411645"
updated_at: "2026-10-08"
generated_by: "Sales King Academy knowledge base, expanded by Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Conversion Rate Optimization

Every business that sells online pays to bring people to a page and then hopes they do something useful once they arrive. Conversion rate optimization (CRO) is the discipline that replaces that hope with a method. It studies why visitors do or do not act, forms testable explanations, runs controlled experiments, and keeps the changes that measurably improve outcomes. Because CRO works on traffic a company has already paid for, a modest improvement in the share of visitors who convert often produces more profit than the same effort spent buying more traffic. This chapter teaches CRO as an applied practice for the funnel specialist: the vocabulary, the causal mechanism, the research methods, the statistics behind a trustworthy test, the frameworks for deciding what to test first, and the organizational habits that turn isolated tests into a durable program. It assumes you already know basic marketing and sales concepts such as funnels, traffic sources and customer value.

## Learning objectives

1. Define conversion, conversion rate, micro- and macro-conversions, and revenue per visitor, and calculate each from raw funnel data.
2. Explain the causal chain of a CRO program from data collection through hypothesis, experiment, decision and implementation.
3. Select appropriate quantitative and qualitative research methods to locate and explain conversion problems.
4. Apply and compare the main diagnostic frameworks used in CRO, including the Fogg Behavior Model, the LIFT model and heuristic evaluation.
5. Prioritize a backlog of test ideas using PIE, ICE, PXL or value-at-stake scoring, and justify the choice of framework.
6. Design an A/B test with a stated hypothesis, primary metric, guardrail metrics, minimum detectable effect and required sample size.
7. Interpret test results correctly, including p-values, confidence intervals, statistical power and the dangers of peeking.
8. Diagnose common page-level conversion barriers on landing pages, forms, checkouts and mobile experiences.
9. Recognize ethical, privacy and legal limits on persuasion, data collection and experimentation.
10. Plan the people, cadence and documentation needed to run CRO as a continuous program rather than a one-off project.

## Overview

Conversion rate optimization is a professional discipline for the funnel specialist and an applied practice used to generate revenue. It sits between marketing, product design, analytics and sales. Marketing brings visitors; product and design shape what they experience; analytics measures what happens; sales and customer success depend on the quality of the leads and customers that result. CRO borrows from all four and adds one distinctive habit: it treats every belief about what customers want as a hypothesis until a controlled test or strong evidence supports it.

Three ideas run through the whole chapter. First, conversion is a behavior, so the tools that explain behavior (motivation, ability, friction, trust, timing) explain conversion. Second, a conversion rate is a ratio of two noisy counts, so judging whether it has really changed requires statistics, not eyeballing. Third, the goal is not a higher conversion rate for its own sake but more value per visitor over the customer's lifetime, achieved honestly. A change that lifts sign-ups while filling the pipeline with poor-fit leads, or that tricks people into purchases they later refund, is not an optimization.

## Foundations

Conversion rate optimization (CRO) is the systematic process of increasing the percentage of website or app visitors who complete a desired action, known as a conversion. A conversion is a specific, measurable action taken by a visitor, such as filling out a form, making a purchase or subscribing to a newsletter. The conversion rate is calculated by dividing the number of conversions by the number of visitors (or sessions) in the same period, typically expressed as a percentage. A practitioner of CRO must understand key terms, including:

- **Landing page**: a standalone web page designed to convert visitors, often used as the destination for paid advertising or email campaigns.
- **Call-to-action (CTA)**: a prompt or instruction that encourages visitors to take a specific action, such as "Start free trial" or "Buy now."
- **Funnel**: the series of steps a visitor takes to complete a conversion, from first arrival to final action.
- **A/B testing**: a method of comparing two versions of a web page or element, shown at random to comparable visitors, to determine which performs better.
- **Segmentation**: dividing visitors into distinct groups based on characteristics such as traffic source, device, location or behavior, to understand differences and tailor experiences.
- **User experience (UX)**: the overall perception and interaction a visitor has with a website or application, which shapes their likelihood of converting.
- **Heuristic evaluation**: assessing a website's usability and conversion potential by checking it against established principles, known as heuristics.

UX covers usability, accessibility and user interface (UI) design. UI design focuses on the visual elements and interactions of a page, aiming to create an intuitive environment in which the next step is obvious. The word heuristic is used in two related senses in CRO, and it helps to keep them apart. A design heuristic is a rule of thumb an expert uses to evaluate a page ("the primary action should be visually dominant"). A cognitive heuristic is a mental shortcut a visitor uses to decide quickly ("many other people bought this, so it is probably fine"). Persuasion principles such as reciprocity, scarcity and social proof describe cognitive heuristics; CRO practitioners use them, but must use them truthfully.

### Macro-conversions and micro-conversions

A macro-conversion is the primary outcome a page or site exists to produce: a purchase, a demo request, a paid subscription. A micro-conversion is a smaller step that tends to precede it: viewing a pricing page, adding to cart, starting a form, watching a product video, creating an account. Micro-conversions matter for two reasons. They locate where people drop out, and they occur more often, so they give faster feedback. Their weakness is that they can mislead: a change that increases add-to-cart clicks by hiding shipping costs may reduce completed purchases once the costs appear. The rule is to diagnose with micro-conversions and decide with macro-conversions or with a micro-conversion that has been shown to predict them.

### The unit of analysis

A conversion rate needs a denominator, and the choice changes the number. Sessions-based rates divide conversions by visits; one person visiting five times counts five times. User-based rates divide by unique visitors, which is closer to how people actually decide but depends on identifying returning users across devices, which is imperfect. Order-based metrics such as checkout completion divide by those who started checkout. None is wrong; the error is comparing numbers built on different denominators. Every CRO report should state its denominator, and experiments should randomize and analyze at the same unit (usually the user), because randomizing by session lets the same person see both versions.

### Why CRO is economically powerful

Revenue from a digital channel can be written as traffic multiplied by conversion rate multiplied by average order value. Growing traffic usually costs more money every month, because each additional visitor must be bought or earned. Improving conversion is a one-time investment in a better experience that then applies to all future traffic, including traffic that has not been bought yet. Conversion improvements also make paid acquisition cheaper per customer, which can let a company bid for traffic that was previously unprofitable. This compounding is why CRO, done well, is one of the highest-return activities available to a revenue team, and why it deserves rigorous methods rather than guesswork.

## Mechanisms

Conversion rate optimization operates through a series of interconnected steps that form a causal chain. It begins with data collection, where user interactions on a website or application are tracked and recorded. This data is analyzed to identify patterns, such as which pages have high exit rates, where visitors abandon forms, or which elements receive attention. Statistical reasoning separates real patterns from noise. Hypotheses are then formulated: specific, causal explanations of why a problem exists and what change would fix it, ranging from unclear calls-to-action to missing information or a confusing interface. These hypotheses are tested through controlled experiments, typically A/B tests or multivariate tests, in which different versions are shown at random to comparable groups of users. Outcomes are measured and compared. If a version shows a reliable improvement on the primary metric without harming guardrail metrics, it is implemented as the new standard.

The causal chain is: data informs analysis, analysis informs hypothesis, hypothesis informs testing, and testing informs implementation, in a cycle that drives ongoing optimization. Each cycle builds on the last, because every test, including a failed one, adds to the team's understanding of its customers. The key requirement throughout is accurate measurement of user behavior, so that decisions are driven by evidence rather than by intuition, seniority or the loudest opinion in the room.

### What actually changes when a visitor converts

Behind the cycle sits a model of the visitor. A person arrives with some level of motivation, created by a need and shaped by the ad or link that brought them. On the page they gather evidence about whether this offer meets the need, whether it is credible, and what it will cost in money, time, effort and risk. At each step they weigh perceived value against perceived cost and either continue, pause or leave. A conversion happens when, at the moment a clear prompt is present, perceived value exceeds perceived cost by enough to overcome inertia.

This gives CRO exactly four kinds of lever:

1. **Raise perceived value**: a clearer value proposition, better evidence of outcomes, a more relevant offer.
2. **Lower perceived cost**: fewer form fields, faster pages, simpler choices, transparent pricing.
3. **Reduce uncertainty and anxiety**: guarantees, reviews, security cues, clear policies, honest answers to objections.
4. **Improve the prompt**: a visible, specific, well-timed call-to-action that arrives when motivation is highest.

Every good test hypothesis names which lever it pulls and why the research suggests that lever is the constraint. A hypothesis that cannot name its lever is usually a design preference in disguise.

### Traffic quality and message match

A page does not convert in isolation; it converts the visitors it receives. Visitors from a search for the product's exact name arrive highly motivated; visitors from a broad social ad arrive curious at best. A drop in conversion rate after a marketing team broadens targeting may reflect a change in traffic mix rather than a worse page. For this reason CRO practitioners analyze by traffic source and check message match: the degree to which the page's headline, offer and imagery continue the promise of the ad, email or link that brought the visitor. Poor message match forces the visitor to re-orient, and many simply leave.

## Measuring Conversion: Metrics And Formulas

A CRO practitioner needs a small set of precisely defined metrics. Formulas are given here in words and symbols so they can be computed in any tool.

- **Conversion rate (CR)** = conversions / visitors. If 200 of 10,000 visitors buy, CR = 200 / 10,000 = 2.0%.
- **Step conversion rate** = visitors completing step k+1 / visitors completing step k. Multiplying all step rates gives the overall funnel rate.
- **Average order value (AOV)** = revenue / orders.
- **Revenue per visitor (RPV)** = revenue / visitors = CR x AOV. RPV is often the best single primary metric for e-commerce tests because it captures both whether people buy and how much.
- **Bounce rate**: the share of sessions that view one page and leave without a further interaction (definitions vary by analytics tool; check yours).
- **Exit rate** of a page: the share of page views that were the last in a session. Unlike bounce rate it applies to every page in a funnel.
- **Abandonment rate** of a step = 1 - step conversion rate. Cart abandonment is the share of carts not turned into orders.
- **Cost per acquisition (CPA)** = marketing spend / conversions. Holding spend constant, CPA falls in proportion as CR rises.
- **Relative lift** = (variant rate - control rate) / control rate. Moving from 3.0% to 3.5% is an absolute lift of 0.5 percentage points and a relative lift of 16.7%. Always say which you mean.
- **Lead-to-customer rate** and **lead quality**: for B2B, the share of form leads that become qualified opportunities and then customers. A form change that raises lead volume but lowers this rate may not create value.

### Choosing a primary metric and guardrails

Every experiment has one primary metric, chosen before the test starts, that decides the winner. It should be sensitive enough to move within a reasonable test duration and close enough to business value that moving it matters. Guardrail metrics are measures the test must not harm, such as refund rate, page load time, unsubscribe rate, or downstream lead quality. Secondary metrics help explain the result but do not decide it. Writing these down in advance prevents the common temptation to scan twenty metrics after a test and declare victory on whichever one happened to rise.

### Funnel arithmetic

Because overall conversion is the product of step rates, a relative improvement at any step produces the same relative improvement overall, holding the other steps constant. A 10% relative lift in add-to-cart rate and a 10% relative lift in checkout completion each raise final orders by 10%. What differs is how hard each is to achieve and how many visitors the step touches, which affects how quickly a test can detect the change. Worked example 1 below works through this.

## The CRO Research Toolkit

Good tests come from good research. Teams that test ideas from a brainstorm win far less often than teams that test ideas grounded in evidence about where and why visitors struggle. Research divides into quantitative methods, which show what is happening and where, and qualitative methods, which explain why.

### Quantitative methods

- **Web analytics**: funnel reports, landing-page reports, device and source segments, and exit pages identify where conversion is lost. Start every engagement by verifying tracking: duplicate events, missing purchase tags and broken cross-domain tracking are common and can invalidate everything downstream.
- **Funnel and path analysis**: maps the sequence of steps and the drop-off between each, showing which step leaks the most visitors.
- **Form analytics**: field-level data on which fields people hesitate over, correct repeatedly or abandon at.
- **Heatmaps and scroll maps**: aggregate click and scroll behavior. They show whether people see the key content and whether they click things that are not links. Interpret with care: a heatmap shows what people did, not what they intended.
- **Session recordings**: replays of individual sessions with personal data masked. Useful for spotting bugs and confusion, but slow to review; sample deliberately, for example sessions that reached checkout and left.
- **Site speed and error monitoring**: slow loading and JavaScript errors are frequent hidden causes of lost conversions, especially on mobile and older devices.

### Qualitative methods

- **On-site polls**: one short question shown at a meaningful moment, such as "What, if anything, is stopping you from starting your trial today?" on exit intent from a pricing page.
- **Customer surveys**: ask recent buyers what almost stopped them, what alternatives they considered and what convinced them. Their words become raw material for headlines and objection handling.
- **User testing**: watch five to eight target users attempt realistic tasks while thinking aloud. Small samples reliably reveal major usability problems, though not their frequency.
- **Customer interviews and sales or support transcripts**: the questions customers ask a salesperson or support agent are the questions the page fails to answer.
- **Heuristic evaluation**: an expert review against a checklist of usability and persuasion principles. Fast and cheap, but it produces hypotheses, not proof.

### Triangulation

The strongest hypotheses come from triangulation: the same problem visible in two or more independent sources. If analytics show a large drop at the shipping step, recordings show people pausing at the delivery options, and a poll returns "shipping too expensive" as the top answer, the team has a well-supported hypothesis about cost transparency at that step. A single source rarely justifies a test on its own; two or three agreeing sources justify a high priority.

## Methods And Frameworks

Conversion rate optimization employs several methods, models and formulas. Each suits a different job, and each has a characteristic way of failing.

**A/B testing** compares two versions of a page or element to determine which performs better. It is ideal for testing discrete, well-defined changes and is the workhorse method of CRO. It requires enough traffic to reach the needed sample size; low-traffic sites must test bolder changes or rely more on qualitative research. **A/B/n testing** extends this to several variants at once, at the cost of more traffic and a need to correct for multiple comparisons.

**Multivariate testing (MVT)** tests several elements at once, such as three headlines crossed with two images, to estimate each element's effect and their interactions. It suits complex pages with high traffic. Its failure mode is over-testing: the number of combinations grows multiplicatively, so each one receives little traffic and results take very long or never become reliable.

**Pareto analysis**, also known as the 80/20 rule, observes that a small share of causes often produces a large share of effects; for example, a few pages or a few traffic sources may account for most lost revenue. It helps focus effort. The 80/20 split is a heuristic, not a law; the failure mode is assuming the split rather than measuring it, and so misidentifying the key elements.

**The Six Thinking Hats**, a framework developed by Edward de Bono, structures team discussion by having participants consider a problem from distinct perspectives in turn: facts, feelings, risks, benefits, creative alternatives and process. In CRO it is useful for test-ideation workshops and post-test reviews, because it stops a single perspective (often the risk-averse one or the enthusiastic one) from dominating.

**The Fogg Behavior Model**, B = MAP, states that a behavior occurs when Motivation, Ability and a Prompt converge at the same moment. If motivation is high but the action is hard, people need simplification; if the action is easy but motivation is low, they need a stronger reason; if both are adequate but there is no clear prompt, nothing happens. The model is diagnostic: it tells the practitioner which of the three to work on. Its failure mode is misreading motivation, for example assuming visitors lack motivation when they are actually blocked by ability problems such as a broken form.

**The LIFT model**, developed by the agency WiderFunnel, analyzes a page against six conversion factors. The **value proposition** is the engine; it is what the visitor weighs against cost. Three factors can increase conversion: **relevance** (does the page match what the visitor expected), **clarity** (is the offer and next step easy to understand) and **urgency** (is there a genuine reason to act now). Two factors can decrease it: **anxiety** (doubts about trust, security or risk) and **distraction** (competing links, offers and visual noise that pull attention from the main action). The original knowledge base listed the factors inconsistently; the six above are the standard set.

**Pirate Metrics (AARRR)**, a framework introduced by investor Dave McClure, tracks users across Acquisition, Activation, Retention, Referral and Revenue. In CRO it widens the lens: a change to a sign-up page should be judged not only on acquisition but on whether the new users activate and stay. Its failure mode is treating each stage in isolation and ignoring external factors, such as seasonality or a competitor's promotion, that move several stages at once.

Failure modes common to all these methods include testing without a clear hypothesis, ignoring user feedback, confirmation bias in reading results, insufficient sample size, and over-reliance on a single metric. Understanding these methods and their limitations is crucial for effective CRO.

### Heuristic evaluation checklists

A practical heuristic review checks each key page for a short list of questions. Is it immediately clear what this page offers and for whom? Does the headline match the source that brought the visitor? Is there one primary action, visually dominant and specifically labeled? Does the page answer the main objections, such as price, effort, risk and fit, before asking for commitment? Is the evidence credible and specific? Are there unnecessary fields, steps or choices? Does it work well on a small screen with one thumb? Does it load quickly? Is it accessible to users with disabilities, for instance with readable contrast, labeled form fields and keyboard navigation? Each "no" becomes a candidate hypothesis, not an automatic change.

### Jobs to be done as a research lens

The jobs-to-be-done perspective asks what progress a customer is trying to make in a particular situation, rather than what demographic group they belong to. A visitor to a payroll software page is not "a small business owner aged 35-44"; they are someone who wants to stop spending Sunday evenings on payroll and never get a tax penalty again. Framing research around the job clarifies which value proposition to lead with and which anxieties to address, and it often reveals that the real competitor is not another vendor but a spreadsheet or doing nothing.

## Prioritization Frameworks Compared

Research typically produces more ideas than a team can test. A test slot is a scarce resource, limited by traffic and team capacity, so prioritization determines the program's return. Four frameworks are widely used.

**PIE** scores each idea from 1 to 10 on Potential (how much improvement is possible on this page), Importance (how valuable the page's traffic is) and Ease (how simple the test is to build and run), then averages the scores. It is quick and intuitive. Its weakness is subjectivity: two people can score the same idea very differently.

**ICE** scores Impact, Confidence and Ease, again typically 1 to 10. The Confidence term rewards ideas backed by evidence, which nudges teams toward research-led testing. It shares PIE's subjectivity.

**PXL**, a framework popularized by the CRO agency CXL, replaces most subjective scores with yes-or-no questions: Is the change above the fold? Is it noticeable within five seconds? Does it add or remove an element? Is it supported by user testing, by qualitative feedback, by analytics? Does it run on high-traffic pages? Points are summed, with an ease estimate. Binary questions make scores more consistent between people, at the cost of a longer checklist.

**Value-at-stake scoring** estimates the money each idea could plausibly add: page revenue (or the revenue flowing through it) multiplied by a realistic relative lift, adjusted by the probability the idea works and divided by the effort required. It forces quantitative thinking and is easy to explain to finance and leadership, but it gives a false sense of precision if the lift and probability estimates are guesses.

No framework is correct; each is a way of making assumptions explicit and consistent. Mature programs often combine one: a PXL-style evidence checklist to estimate confidence and a value-at-stake estimate to estimate size. The worst approach is no framework, which in practice means the highest-paid person's ideas get tested first.

## Experiment Design And Statistics

A test is only as good as its design. This section covers what a CRO practitioner needs to run trustworthy A/B tests; deeper treatment belongs to a dedicated experimentation course.

### Writing a hypothesis

A strong hypothesis has three parts: the observation, the change, and the predicted effect with its reason. For example: "Because exit polls and recordings show that visitors on the pricing page are unsure whether the trial requires a credit card, adding the line 'No card required' beside the trial button will increase trial starts, because it removes a specific anxiety at the moment of decision." This template forces the team to connect the test to research and to a lever, and it makes the result informative whichever way it goes: if it fails, the team learns that card anxiety was not the constraint.

### Randomization and the unit of assignment

Visitors must be assigned to versions at random so that, apart from the change, the groups are comparable. Assignment should be sticky, so a returning visitor sees the same version, and should be made at the level of analysis, usually the user. Check for **sample ratio mismatch (SRM)**: if a test was set to split traffic 50/50 but the counts are noticeably unequal, something in the assignment or tracking is broken, and the results should not be trusted until it is fixed. A chi-square test on the counts detects SRM.

### Significance, power and minimum detectable effect

Four quantities define a test's sensitivity:

- The **significance level** (alpha), commonly 0.05, is the false-positive rate the team accepts: the probability of declaring a difference when there is none.
- **Statistical power**, commonly 0.80, is the probability of detecting a real effect of a given size.
- The **minimum detectable effect (MDE)** is the smallest true lift the test is designed to detect reliably.
- The **baseline conversion rate** of the control.

For comparing two proportions, the sample size per variant is approximately:

n = [ z(1-alpha/2) x sqrt(2 x pbar x (1 - pbar)) + z(1-beta) x sqrt(p1(1-p1) + p2(1-p2)) ]^2 / (p2 - p1)^2

where p1 is the baseline rate, p2 is the rate under the MDE, pbar is their average, z(1-alpha/2) is 1.96 for a two-sided 5% test and z(1-beta) is 0.84 for 80% power. A useful rule of thumb is n is about 16 x p(1-p) / d^2, where d is the absolute difference to detect. Lower baselines and smaller effects demand far larger samples, which is why low-traffic sites cannot detect subtle changes.

### p-values and confidence intervals

The p-value is the probability of seeing a difference at least as large as the observed one if there were truly no difference. It is not the probability that the variant is better, nor the probability that the result is a fluke. A confidence interval for the difference is usually more informative: a 95% interval of +0.05 to +0.95 percentage points says the effect is probably positive but could be anywhere from trivial to large. Report both, and always report the effect size, not just "significant."

### Peeking and stopping rules

Classical tests assume the sample size is fixed in advance and the result is checked once. Checking daily and stopping the moment p falls below 0.05 dramatically inflates the false-positive rate, because random fluctuations will cross the threshold at some point surprisingly often. Teams should either fix the duration in advance and wait, or use a method designed for continuous monitoring, such as sequential testing or a Bayesian approach with a pre-agreed decision rule. Tests should also run for whole weeks, usually at least one and preferably two full business cycles, because behavior differs between weekdays and weekends.

### Threats to validity

- **Novelty and primacy effects**: returning users may react to a change simply because it is new, or resist it because it is unfamiliar. Segmenting new versus returning users helps.
- **Seasonality and external events**: a sale, holiday, outage or press story during a test can distort results; note them in the test log.
- **Multiple comparisons**: testing many variants or metrics raises the chance that one looks significant by luck. Correct for it or pre-register one primary comparison.
- **Instrumentation errors**: the variant's tracking code may fire differently from the control's. Run an A/A test (two identical versions) when setting up a new tool to confirm that it reports no difference.
- **Flicker**: client-side tools sometimes show the original page briefly before swapping in the variant, which itself changes behavior. Server-side testing avoids this.
- **Winner's curse**: the measured lift of tests that just cleared the threshold tends to overstate the true effect. Expect real-world gains to be smaller than test readouts, and validate large wins with a holdout or retest.

### Bayesian and bandit approaches

Bayesian analysis reports the probability that each variant is best and the expected loss from choosing it, which many business stakeholders find more intuitive than p-values. It still requires sensible priors and pre-agreed decision rules. Multi-armed bandit algorithms shift traffic toward better-performing variants during a test, which reduces the cost of showing losing versions. They suit short-lived decisions such as which promotional banner to show this week, but they make clean inference about effect sizes harder, so they are less suited to learning why something works.

## Page-Level Levers

Most CRO work concentrates on a few recurring page types. The following principles are widely applicable starting points for hypotheses, not rules to apply without testing.

### Landing pages

A landing page should make one promise to one audience and ask for one action. The headline should state the outcome the visitor wants in their terms and match the ad or link that brought them. Supporting content should, in roughly this order, clarify what the offer is, show evidence that it works, address the main objections and repeat the call-to-action. Removing site navigation from a campaign landing page often reduces distraction, though it should be tested, because some visitors need to explore before committing.

### Forms

Every field is a cost. Remove fields the business does not use, defer non-essential questions until after conversion (progressive profiling), and explain why sensitive information is requested. Use clear labels above fields rather than placeholder text that disappears, inline validation that flags errors as the user goes, and input types that bring up the right mobile keyboard. In B2B, there is a real trade-off: fewer fields usually increase volume, while qualifying fields help sales prioritize. The right answer depends on whether sales capacity or lead volume is the binding constraint, and the decision should be judged on pipeline created, not form submissions.

### Product pages

Visitors need enough information to judge fit: clear images from several angles, honest specifications, size or compatibility guidance, price including any mandatory extras, delivery time and returns policy. Reviews help most when they are numerous, recent, detailed and include some criticism; a wall of perfect scores can reduce credibility.

### Cart and checkout

Checkout is where motivation is highest and patience lowest. Common hypotheses include offering guest checkout, showing total cost including shipping and taxes as early as possible, reducing steps, offering familiar payment methods, displaying security and returns information near the payment fields, and preserving cart contents if the visitor leaves. Unexpected costs revealed late are among the most frequently reported reasons for abandonment in shopper surveys.

### Pricing pages

For subscription businesses, the pricing page is often the most important page after the home page. Clear plan names, a recommended plan, a comparison of what each tier includes, honest answers about contracts and cancellation, and a visible route to talk to sales for complex needs all reduce uncertainty. Annual versus monthly toggles, anchoring with a higher tier and the number of plans are all legitimate test subjects.

### Mobile and speed

Mobile visitors often convert at lower rates than desktop visitors, partly because of intent (browsing on the move) and partly because of friction (small screens, typing, slow connections). Test mobile experiences separately; a layout that wins on desktop can lose on mobile. Page speed affects both conversion and search visibility; improvements to image size, script loading and server response time are often among the most reliable gains available, and they help every visitor.

### Trust and credibility

Trust cues include recognizable customer logos used with permission, specific testimonials attributed to real customers, independent reviews, guarantees, clear contact details, security indicators near payment and plain-language policies. Specificity beats superlatives: "Set up in about 20 minutes, according to our onboarding data" is more persuasive than "Incredibly easy," provided the claim is true and supported.

## Worked Examples

The following worked examples use illustrative numbers. Every figure has been checked by calculation.

### Worked example 1: Diagnosing a funnel and choosing where to work

An online outdoor-gear store receives 40,000 sessions in a month. Its funnel is:

- 60% of sessions view a product page: 40,000 x 0.60 = 24,000 product views.
- 8% of product viewers add to cart: 24,000 x 0.08 = 1,920 carts.
- 55% of carts start checkout: 1,920 x 0.55 = 1,056 checkouts started.
- 60% of checkouts are completed: 1,056 x 0.60 = 633.6, which we round to about 634 orders.

Overall conversion rate = 633.6 / 40,000 = 1.584%, about 1.58%. With an average order value of $70, monthly revenue is 633.6 x $70 = $44,352, and revenue per visitor is $44,352 / 40,000 = $1.11.

The team has two candidate projects. Project A would raise add-to-cart from 8% to 9%, a 12.5% relative lift. Project B would raise checkout completion from 60% to 66%, a 10% relative lift. Because the overall rate is the product of step rates, Project A yields 40,000 x 0.60 x 0.09 x 0.55 x 0.60 = 712.8 orders, an extra 79.2 orders and $5,544 per month. Project B yields 40,000 x 0.60 x 0.08 x 0.55 x 0.66 = 696.96 orders, an extra 63.4 orders and $4,435 per month.

Project A is worth more if both are achievable. But a test of the add-to-cart step has 24,000 visitors per month exposed, while a checkout test has only 1,056, so a checkout test will take far longer to reach significance. The lesson: rank opportunities by value, then check whether the step has enough traffic to test; where it does not, consider making the change on strong qualitative evidence and monitoring the result.

### Worked example 2: Calculating the sample size for an A/B test

A software company's trial page converts 3.0% of visitors. The team wants to detect a 15% relative lift, which means a variant rate of 3.0% x 1.15 = 3.45%. It uses a two-sided significance level of 0.05 (z = 1.96) and power of 0.80 (z = 0.84).

The average rate pbar = (0.030 + 0.0345) / 2 = 0.03225. Applying the formula from the statistics section:

n = [1.96 x sqrt(2 x 0.03225 x 0.96775) + 0.84 x sqrt(0.03 x 0.97 + 0.0345 x 0.9655)]^2 / (0.0045)^2, which comes to about 24,193 visitors per variant.

The rule of thumb 16 x p(1-p) / d^2 = 16 x 0.03 x 0.97 / 0.0045^2 gives about 22,993, close enough for planning. The page receives 3,000 visitors per day, split between two variants, so the test needs about 2 x 24,193 / 3,000 = 16.1 days. The team rounds up to 21 days, three full weeks, so every weekday is represented equally. If the team had wanted to detect a 5% relative lift instead, the required sample would rise roughly ninefold, because sample size scales with the inverse square of the effect, which would make the test impractical at this traffic level.

### Worked example 3: Reading an A/B test result

After the planned duration, the results are:

- Control: 12,000 visitors, 360 conversions, CR = 3.00%.
- Variant: 12,000 visitors, 420 conversions, CR = 3.50%.

Absolute lift = 0.50 percentage points; relative lift = 0.50 / 3.00 = 16.7%. The pooled rate is 780 / 24,000 = 3.25%. The standard error of the difference under the null hypothesis is sqrt(0.0325 x 0.9675 x (1/12,000 + 1/12,000)) = 0.00229. The z-statistic is 0.005 / 0.00229 = 2.18, which corresponds to a two-sided p-value of about 0.029.

The 95% confidence interval for the difference, using the unpooled standard error of 0.00229, is 0.005 plus or minus 1.96 x 0.00229, which is about +0.05 to +0.95 percentage points. The result is statistically significant at the 5% level, and the interval excludes zero. But the interval is wide: the true lift could be as small as a 2% relative improvement or as large as about 32%. The team should ship the variant, assuming the guardrail metrics are healthy, but forecast its value using a conservative figure, not the 16.7% headline, because of the winner's curse.

### Worked example 4: Prioritizing by value at stake

A team compares three pages for its next test slot. It estimates monthly visitors and revenue per visitor flowing through each, and assumes a plausible 5% relative lift from a good test:

| Page | Monthly visitors | Revenue per visitor | Monthly revenue through page | Value of a 5% lift per month | Per year |
|---|---|---|---|---|---|
| Checkout | 9,000 | $32.00 | $288,000 | $14,400 | $172,800 |
| Product pages | 60,000 | $2.40 | $144,000 | $7,200 | $86,400 |
| Home page | 80,000 | $1.10 | $88,000 | $4,400 | $52,800 |

Although the home page has the most traffic, checkout carries the most revenue, so a 5% improvement there is worth more than three times a 5% improvement on the home page. If a checkout test would take twice as long to build, its value per unit of effort is still the highest. This table also helps explain the program to leadership: it ties each test to money.

### Worked example 5: Conversion rate versus revenue per visitor, and the original examples revisited

The original knowledge base offered three illustrations, which are kept here in one consistent version:

1. **E-commerce product page**: 10,000 monthly visitors convert at 2.0%, giving 200 sales. Simplifying the layout, improving images and streamlining checkout raises the rate to 2.5%, giving 250 sales, a 25% increase.
2. **Lead-generation landing page**: 10,000 monthly visitors convert at 5.0%, giving 500 leads. Clarifying the headline, simplifying the form and adding social proof raises the rate to 7.5%, giving 750 leads, a 50% increase.
3. **Pay-per-click campaign**: 10,000 clicks convert at 1.0%, giving 100 conversions. Improving ad relevance and aligning the landing page with the ad's message raises the rate to 1.5%, giving 150 conversions, a 50% increase from the same clicks. If the clicks cost $15,000, cost per acquisition falls from $150 to $100, which improves return on ad spend.

Now a caution. A retailer tests a discount banner. Control converts at 3.0% with AOV of $60, so RPV = $1.80. The variant converts at 3.3% with AOV of $52, so RPV = $1.716. The variant "wins" on conversion rate, a 10% relative lift, yet earns about 4.7% less revenue per visitor, before even counting the lower margin on discounted orders. Choosing RPV or profit per visitor as the primary metric would have prevented a costly mistake.

## Case Study

### Case study: Northfield Outdoor Supply (fictional company)

Northfield Outdoor Supply is a fictional online retailer of camping and hiking equipment, used here for teaching. All names and figures are illustrative.

**Problem.** Northfield received about 120,000 sessions per month and converted 1.8% of them, giving roughly 2,160 orders at an average order value of $85, or about $183,600 in monthly revenue. Paid traffic costs had risen for two consecutive quarters, and leadership's first instinct was to raise the advertising budget. The new e-commerce manager argued that the business should first find out why 98% of visitors left without buying.

**What was done.** The team spent four weeks on research before running any test. Analytics, after fixing a duplicate purchase tag that had been inflating mobile conversion, showed that mobile visitors converted at well under half the desktop rate and that the largest drop occurred between cart and the shipping step. Session recordings showed mobile users pinching and zooming on the shipping options and abandoning when the total updated. An exit poll on the cart page returned two dominant answers: "Shipping cost surprised me" and "Not sure if it will arrive before my trip." Ten customer interviews revealed that many shoppers were buying for a specific trip date, which made delivery timing as important as price.

The team wrote hypotheses that named their levers. Showing an estimated delivery date and the shipping cost on product pages would reduce anxiety and surprise (lowering perceived cost and uncertainty). A simplified single-page mobile checkout would increase ability. A free-shipping threshold set slightly above the median order value would raise perceived value and might increase order size. They prioritized with a value-at-stake estimate combined with an evidence checklist, and ran tests one at a time on the affected pages, each for three full weeks with RPV as the primary metric and refund rate and page speed as guardrails.

**Measured results.** The delivery-date and up-front shipping test produced a clear win on RPV. The single-page mobile checkout produced a smaller but significant win on mobile only, with no effect on desktop, so it was shipped for mobile. The free-shipping threshold raised average order value but lowered conversion slightly; net RPV was flat while margin fell, so it was rejected. After the two winners had been live for a full quarter, sitewide conversion settled at about 2.07%, a 15% relative improvement over 1.8%. On 120,000 sessions at $85 AOV, that is about 2,484 orders and $211,140 per month, an increase of roughly $27,540 per month or about $330,000 per year, with no increase in advertising spend. The measured post-launch gain was smaller than the sum of the two test readouts, as the winner's curse predicts.

**Lessons.** First, the most valuable finding came from research, not from a test: shoppers were buying for a deadline, which no one had considered. Second, fixing tracking came before everything else; the duplicate tag would have hidden the size of the mobile problem. Third, a rejected test (the shipping threshold) was still valuable, because it prevented a margin-reducing change that looked good on one metric. Fourth, segment results: the mobile checkout helped one segment and did nothing for another. Finally, forecasts based on test readouts should be discounted; the team now plans using half the measured lift.

## Applications

Conversion rate optimization is applied across many domains. In e-commerce it is used to optimize product pages, carts and checkout processes to increase sales and revenue per visitor; large retailers commonly run experimentation programs that test page layouts, product information and calls-to-action continuously. In digital marketing, CRO improves landing pages, email campaigns and paid advertising to raise lead generation and lower acquisition cost; marketers use heatmaps, click analysis and polls to find where a landing page fails to engage and then test data-driven changes.

In software and subscription businesses, CRO extends beyond the website into the product: sign-up flows, onboarding steps, the moment a free user meets a paywall, and in-product upgrade prompts. Here it overlaps with product-led growth, and the key metrics shift from sign-ups toward activation and paid conversion. In mobile apps, CRO applies to app store listings, onboarding screens, in-app purchases and permission requests such as push notifications. In B2B sales, it applies to demo-request forms, pricing pages, chat prompts and the hand-off from marketing to sales, where the metric that matters is pipeline and revenue rather than form fills.

CRO is also used in sectors such as finance, healthcare, education and the public sector to make applications, enrollments and service sign-ups easier to complete. In these settings the goal is often less about persuasion and more about removing friction for people who already want to complete a task, such as renewing a document or registering for a course, and accessibility and clarity carry extra weight.

In AI-assisted selling, which is central to Sales King Academy's curriculum, CRO principles apply to conversational interfaces. A chat assistant on a pricing page has a conversion funnel of its own: open rate, engaged conversations, qualified hand-offs and booked meetings. Each step can be measured and tested like a page, and the same rules about primary metrics, guardrails and honest persuasion apply.

## Building A CRO Program

Isolated tests produce isolated wins. A program produces compounding learning. Building one involves people, process, tools and documentation.

### Roles

Even a small program needs several capabilities, which one person may cover in a small company: a strategist or lead who owns the roadmap and the research; an analyst who validates tracking, sizes tests and reads results; a designer and copywriter who create variants; a developer who builds them reliably; and a stakeholder from each affected team, such as product, brand or legal, who agrees in advance what may be tested. The most common structural failure is a program that depends on borrowed developer time and stalls whenever other priorities arise.

### Cadence

A typical cycle runs research, ideation, prioritization, design and build, quality assurance, launch, analysis and documentation. Programs should track their **testing velocity** (tests launched per month), **win rate** (share of tests producing a reliable improvement) and **impact** (estimated value of implemented wins). Win rates vary widely; in mature programs a large share of tests do not beat the control, which is normal and still informative. A program whose win rate is very high is often testing timid changes or reading results too generously.

### Quality assurance

Before launch, every variant should be checked on the main browsers and devices, with tracking verified for both control and variant, and with the assignment working as intended. A broken variant does not just waste a test slot; it can lose revenue and produce misleading conclusions.

### Documentation and the learning repository

Each test should be logged with its hypothesis, research evidence, screenshots, dates, sample sizes, results, decision and the lesson learned. Over time this repository becomes one of the company's most valuable assets: a record of what customers actually respond to. It prevents re-testing settled questions, helps onboard new team members and turns individual tests into a theory of the customer.

### Tools

The tool landscape changes often, so this chapter teaches categories rather than vendors: analytics platforms; tag management; experimentation platforms (client-side or server-side, with feature flags for product tests); heatmap and session recording tools; survey and polling tools; user-testing services; and statistics tools or notebooks for analysis. Choose tools that integrate with each other, that respect privacy settings and consent, and that the team can operate without external help.

## Ethics, Privacy And Law

Persuasion is part of commerce, but CRO practitioners have unusual power to influence behavior at scale and must use it responsibly.

### Dark patterns

A dark pattern is an interface design that steers people into choices they would not make if fully informed. Examples include hiding mandatory fees until the last step, pre-ticking boxes that add products or consent, making cancellation far harder than sign-up, using fake countdown timers or false low-stock warnings, disguising ads as content, and "confirm-shaming" (labeling the decline option with a guilt-inducing phrase). Dark patterns may lift a short-term metric, but they increase refunds, chargebacks, complaints and churn, damage brand trust and attract regulatory attention. Consumer protection authorities in several jurisdictions, including the United States Federal Trade Commission and regulators in the European Union and United Kingdom, have published guidance and taken enforcement action against deceptive design. A useful test: would the change still work if the visitor fully understood what it was doing? If not, do not ship it.

### Honest urgency and scarcity

Urgency and scarcity are legitimate when real: a sale that genuinely ends on a stated date, limited seats in a live cohort, stock that is genuinely low. They are deceptive when manufactured. The LIFT model's urgency factor should be built from true reasons to act now, such as a deadline the customer cares about, not from invented pressure.

### Privacy and consent

CRO depends on behavioral data, and much of that data is personal. Privacy laws such as the European Union's General Data Protection Regulation (GDPR) and California's consumer privacy law (the CCPA, as amended) give people rights over their data, and many jurisdictions require consent before non-essential tracking cookies are set. Practical consequences for CRO include configuring analytics and testing tools to respect consent choices; masking personal data in session recordings; collecting only the data the analysis needs; and accepting that consent requirements will reduce the share of visitors who can be measured. The specific rules vary by jurisdiction and change over time, so programs should involve their legal or privacy function when choosing tools and settings. This chapter is not legal advice.

### Experiment ethics

Routine A/B tests of layout and copy are a normal part of improving a product. Tests that manipulate emotions, vary prices for the same product in ways customers would consider unfair, or affect vulnerable users raise harder ethical questions and deserve review before launch. Many companies maintain an internal review step for experiments touching pricing, health, finance or minors.

### Accessibility

Accessibility is both an ethical obligation and, in many places, a legal one. The Web Content Accessibility Guidelines (WCAG), published by the World Wide Web Consortium, are the widely used technical standard. Accessible pages, with sufficient contrast, labeled form fields, keyboard navigation and descriptive buttons, usually convert better for everyone, and a variant should never win by making the experience worse for users of assistive technology.

## Common Errors

A common error is misinterpreting statistical significance in A/B testing, where practitioners fail to calculate the minimum sample size required for reliable results, or stop tests early when results look good. This leads to false positives or false negatives and incorrect conclusions about a variation's effectiveness. Another mistake is changing many things at once without a plan, then being unable to say which change caused the effect; bundling changes is acceptable when the goal is to beat the control quickly, but the team must accept that it learns less about why. Practitioners also overlook segmentation, failing to account for differences in behavior among user groups, which can produce an experience optimized for one segment at the expense of another. Over-reliance on "best practices" and expert opinions without validating them through testing can lead to suboptimal solutions, because what worked on someone else's site, for someone else's audience, may not work on yours. Ignoring external factors such as seasonality, user fatigue and technical issues compromises the validity of results.

Other frequent errors include:

- **No clear, measurable goals.** Without a defined primary metric tied to business value, the program has no direction and no way to show progress.
- **Skipping user research.** Relying on assumptions about user behavior produces misguided tests and low win rates.
- **Optimizing elements in isolation.** Focusing only on buttons or headlines while ignoring the broader experience, and how elements interact, limits impact.
- **No prioritization.** Without weighing impact against effort, teams waste scarce test slots on low-value changes.
- **Optimizing the wrong metric.** Lifting conversion while lowering revenue per visitor, margin or lead quality, as Worked example 5 shows.
- **Broken tracking.** Trusting analytics that have not been audited; one duplicate tag can invalidate months of conclusions.
- **Treating CRO as a project.** Running a burst of tests and stopping, rather than maintaining a culture of continuous testing and learning, leads to stagnation.
- **Not documenting.** Failing to record tests means the organization forgets what it learned and repeats past mistakes.

These errors can be avoided by adopting a rigorous, evidence-driven approach, respecting the complexity of user behavior, and continually testing and refining hypotheses.

## Advanced

Conversion rate optimization is evolving to incorporate more advanced methods and technologies. One key area is the integration of machine learning and artificial intelligence for personalization and prediction. Instead of finding one best page for everyone, personalization systems try to choose the best experience for each visitor or segment, using signals such as traffic source, location, device and past behavior. Contextual bandits extend multi-armed bandits by conditioning choices on those signals. The challenge is evaluation: personalized systems still need holdout groups that receive a non-personalized experience, or the team cannot tell whether personalization adds value. Bayesian optimization is used to tune continuous parameters, such as the threshold for a free-shipping offer, more efficiently than testing fixed values one at a time.

Natural language processing and sentiment analysis can summarize thousands of survey responses, reviews, support tickets and chat transcripts into themes, which speeds up the qualitative side of research. Generative AI tools can draft many headline and copy variants quickly. The bottleneck then moves from generating ideas to having enough traffic to test them, which makes rigorous prioritization and research more important, not less. AI-generated variants also need human review for accuracy, brand voice and honesty.

Behavioral economics and cognitive psychology continue to inform persuasion strategy, through concepts such as loss aversion, defaults, anchoring and choice overload. Practitioners should treat individual findings as hypotheses to test in their own context, because many effects vary with audience and setting, and some widely repeated findings have not replicated well.

Measurement itself is changing. Browser restrictions on third-party cookies, consent requirements and privacy regulations such as GDPR and CCPA reduce the share of behavior that can be observed directly. CRO practitioners are adapting with server-side tracking that respects consent, first-party data strategies, aggregated and modeled measurement, and more weight on experiments, which can be analyzed reliably even when individual-level tracking is limited.

Several open questions remain. How should programs measure long-term effects, such as whether a change that increases sign-ups today affects retention a year later? Long-running holdout groups help, but they are expensive. How should CRO be integrated with other disciplines, such as search engine optimization, brand marketing and social media, whose effects are slower and harder to test? What is the right balance between human judgment and automated, data-driven decisions, given the potential biases and blind spots of both? And what are the ethical limits of increasingly personalized persuasion? As the field matures, the emphasis is shifting from conversions alone to long-term customer value and loyalty. Emerging interfaces, including voice, conversational agents and immersive environments such as augmented and virtual reality, will require new ways of defining and measuring conversion, though the underlying method of research, hypothesis, controlled test and learning will remain the same. CRO is becoming more tightly intertwined with user experience design, data science and marketing strategy.

## Summary

Conversion rate optimization is the systematic practice of increasing the share of visitors who take a valuable action, through research, hypotheses, controlled experiments and implementation. Conversion is a behavior driven by perceived value, perceived cost, uncertainty and the presence of a clear prompt, which gives the practitioner four levers to work with. Precise metrics, especially conversion rate, revenue per visitor and step conversion rates, show where value is lost; quantitative research shows where problems occur and qualitative research explains why, with the strongest hypotheses supported by several sources. Frameworks such as the Fogg Behavior Model, the LIFT model and heuristic evaluation structure diagnosis, while PIE, ICE, PXL and value-at-stake scoring structure prioritization. Trustworthy tests require a written hypothesis, a primary metric and guardrails, a sample size calculated from the baseline and minimum detectable effect, randomization checks, a fixed or sequential stopping rule and honest interpretation of p-values and confidence intervals. Common page-level levers include message match, simpler forms, transparent costs, credible evidence, mobile usability and speed. A durable program depends on clear roles, a regular cadence, quality assurance and a documented learning repository. Throughout, CRO must respect ethical, privacy and accessibility obligations: the aim is more value for both the business and the customer, not short-term gains won through deception.

## Key terms

- **Conversion**: a specific, measurable action a visitor takes that the business values, such as a purchase or sign-up.
- **Conversion rate**: conversions divided by visitors (or sessions) in the same period.
- **Micro-conversion**: a smaller step that tends to precede the main conversion, such as adding to cart.
- **Revenue per visitor (RPV)**: total revenue divided by visitors; equal to conversion rate multiplied by average order value.
- **Funnel**: the sequence of steps from arrival to conversion, each with its own step conversion rate.
- **Message match**: the consistency between a page and the ad, email or link that brought the visitor.
- **A/B test**: a controlled experiment in which visitors are randomly assigned to a control or a variant.
- **Multivariate test**: an experiment that varies several elements at once to estimate their individual and combined effects.
- **Hypothesis**: a testable causal statement linking an observation, a change and a predicted effect.
- **Primary metric**: the single, pre-chosen metric that decides an experiment's outcome.
- **Guardrail metric**: a metric that a test must not harm, such as refund rate or page speed.
- **Minimum detectable effect (MDE)**: the smallest true effect a test is designed to detect reliably.
- **Statistical power**: the probability that a test detects a true effect of a given size.
- **p-value**: the probability of a result at least as extreme as the one observed if there were no true difference.
- **Sample ratio mismatch (SRM)**: an unexpected imbalance in the number of users assigned to each variant, signaling a technical fault.
- **Fogg Behavior Model**: the model B = MAP, in which behavior occurs when motivation, ability and a prompt converge.
- **LIFT model**: a diagnostic framework assessing value proposition, relevance, clarity, urgency, anxiety and distraction.
- **PXL**: a prioritization framework that scores test ideas with mostly yes-or-no evidence questions.
- **Dark pattern**: a deceptive interface design that steers users into choices they would not make if fully informed.
- **Winner's curse**: the tendency for measured lifts of winning tests to overstate the true effect.

## Review questions

1. What is the difference between a macro-conversion and a micro-conversion, and why should decisions rest mainly on the former?
2. How do revenue per visitor, conversion rate and average order value relate to one another?
3. What are the four levers a CRO practitioner can pull to influence whether a visitor converts?
4. Why does a change in traffic mix complicate the interpretation of a falling conversion rate?
5. Which three research sources might you triangulate to support a hypothesis about checkout abandonment?
6. What are the six factors of the LIFT model, and which of them can decrease conversion?
7. According to the Fogg Behavior Model, what should you change if visitors are motivated but the action is difficult?
8. How does PXL try to reduce the subjectivity found in PIE and ICE scoring?
9. If baseline conversion is 4% and you want to detect a smaller lift, what happens to the required sample size?
10. Why does checking a test daily and stopping at the first significant result inflate false positives?
11. What does a sample ratio mismatch indicate, and what should you do about it?
12. In Worked example 5, why did the discount banner lose despite raising the conversion rate?
13. What makes an urgency message ethical rather than a dark pattern?
14. Why should a CRO program keep a documented learning repository?

## Answer key

1. A macro-conversion is the primary outcome a page exists to produce, such as a purchase, while a micro-conversion is a preceding step such as adding to cart; decisions should rest on macro-conversions, or on micro-conversions proven to predict them, because micro-conversions can rise while final outcomes fall.
2. Revenue per visitor equals conversion rate multiplied by average order value, so it captures both whether visitors buy and how much they spend.
3. Raise perceived value, lower perceived cost, reduce uncertainty and anxiety, and improve the prompt.
4. Different sources bring visitors with different motivation, so the rate can fall because less-motivated visitors arrived, not because the page got worse; analyzing by source separates the two.
5. Funnel analytics showing where drop-off occurs, session recordings showing behavior at that step, and an exit poll or survey giving visitors' stated reasons; user tests and support transcripts are also valid sources.
6. Value proposition, relevance, clarity, urgency, anxiety and distraction; anxiety and distraction decrease conversion.
7. Increase ability by simplifying the action, for example by removing steps or fields, rather than adding more persuasion.
8. It replaces most subjective 1-10 ratings with yes-or-no questions about visibility, evidence and traffic, which different people answer more consistently.
9. It increases sharply, roughly with the inverse square of the absolute difference, so halving the detectable lift roughly quadruples the sample needed.
10. Random fluctuations will cross the significance threshold at some point surprisingly often, so repeated checks with early stopping give many more chances to declare a false winner than the nominal 5%.
11. It indicates a fault in assignment, redirects or tracking; stop trusting the results, find and fix the cause, and rerun the test.
12. Its lower average order value more than offset its higher conversion rate, so revenue per visitor fell from $1.80 to about $1.72, before even counting reduced margin.
13. It is ethical when the reason to act now is true and accurately stated, such as a genuine deadline or real limited capacity; it becomes a dark pattern when the urgency is invented or exaggerated.
14. It preserves what tests revealed about customers, prevents re-testing settled questions, speeds onboarding and turns individual results into a cumulative understanding of the customer.

## Further reading

- Ron Kohavi, Diane Tang and Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing*.
- Steve Krug, *Don't Make Me Think: A Common Sense Approach to Web Usability*.
- Avinash Kaushik, *Web Analytics 2.0*.
- Alistair Croll and Benjamin Yoskovitz, *Lean Analytics*.
- BJ Fogg, *Tiny Habits: The Small Changes That Change Everything*.
- Robert B. Cialdini, *Influence: The Psychology of Persuasion*.
- Daniel Kahneman, *Thinking, Fast and Slow*.
- Richard H. Thaler and Cass R. Sunstein, *Nudge*.
- World Wide Web Consortium (W3C), *Web Content Accessibility Guidelines (WCAG)*.
