---
key: crypto_payments_integration
title: "Crypto Payments Integration"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-10-08"
chapter: "Sales King Academy, Volume 2, Chapter 7"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# Crypto Payments Integration

This chapter teaches how a business can accept and send payments in digital assets, especially stablecoins, and what changes when it does. Chapter 5 explained how blockchains record transfers and why they are final. Chapter 6 explained the compliance duties that come with handling digital assets. This chapter puts both to work at the checkout and in the back office. You will learn the anatomy of a blockchain payment, the difference between accepting payments directly and through a custodial processor, how stablecoins hold their value and what can go wrong with them, how price movements change what a business actually receives, and how to handle the cases that cause most support problems: underpayments, late payments, wrong networks and refunds. You will also learn to record crypto payments in the accounts and reconcile them with orders.

The chapter is educational. It is not investment, tax or legal advice, and it does not recommend holding any digital asset. All prices, fees and rates in the worked examples are illustrations chosen to make the arithmetic clear; real figures change constantly and must be checked at the time.

## Learning objectives

By the end of this chapter you will be able to:

1. Explain how blockchain payments differ from card and bank payments in direction, timing, finality and cost.
2. Describe the parts of a crypto payment request and the steps from checkout to confirmed payment.
3. Compare direct on-chain acceptance with custodial processors and hybrid models, and carry out due diligence on a processor.
4. Explain how stablecoins aim to hold a fixed value, and identify issuer, reserve, network and redemption risks.
5. Calculate the settlement value of a payment under price movements, quote windows and conversion fees.
6. Compare the total cost of accepting crypto with card acceptance, including the effect of adoption rates.
7. Design rules for underpayments, overpayments, late payments, wrong-network payments and refunds.
8. Record crypto payments in the accounts and reconcile them with orders using transaction identifiers and signed notifications.
9. Explain the design of a prepaid, metered credit system and how it differs from a cryptocurrency, using the Sales King Academy Beats system as an example.

## 1. How blockchain payments differ

Most people's experience of digital payment is a card. When a customer pays by card, they hand the merchant their card details, and the merchant, through its payment provider, pulls the money from the customer's account. The card network authorises the payment within seconds, but the money settles to the merchant days later, and the customer can dispute the charge for weeks or months afterwards through a chargeback. The merchant pays a fee, usually a percentage of the sale plus a small fixed amount.

A blockchain payment works the other way round, and that changes almost everything.

**It is a push payment.** The customer's wallet signs a transaction and sends funds to an address the merchant provides. The merchant never receives any details it could use to take money. This removes a whole class of risk: there is no card number to steal from the merchant's systems.

**It settles on the ledger.** Once the transaction is confirmed to the business's chosen depth, the funds are under the control of whoever holds the receiving address's key. There is no separate settlement step days later, though converting the funds to a bank currency may add one.

**It is final.** As Chapter 5 explained, confirmed transactions cannot be reversed by the network. There is no chargeback. This protects merchants from a common type of fraud, in which a customer receives goods and then disputes the charge. It also removes a protection customers rely on, so the merchant must offer its own fair refund process.

**It runs at all hours and across borders.** Blockchains do not close at weekends or on public holidays, and a payment from another country moves the same way as a local one.

**Fees are per transaction, not per value.** On most networks, the network fee depends on how busy the network is and how much data or computation the transaction uses, not on its value. It is usually paid by the sender. A processor, if one is used, adds its own fee, which is often a percentage.

**The customer must choose correctly.** The customer has to send the right asset, on the right network, to the right address, for the right amount, before a quote expires. Each of these is a chance for error, and errors can be costly because the transfer cannot simply be cancelled.

These differences explain the design choices in the rest of the chapter. A business that integrates crypto payments well is mostly a business that has thought hard about finality and about helping customers avoid mistakes.

## 2. The anatomy of a crypto payment

A crypto payment at an online checkout typically passes through six steps.

**1. The order is priced.** The business sets its prices in its own currency, say US dollars. The customer chooses to pay in a particular asset on a particular network, for example a dollar stablecoin on a named network.

**2. A payment request is created.** The business, or its processor, creates a request that specifies:

- the **asset** (which coin or token);
- the **network** (which blockchain it must be sent on, since many tokens exist on several networks);
- the **amount** in that asset, converted from the order price at a quoted rate;
- the **receiving address**, ideally unique to this order so the payment can be matched automatically;
- the **expiry time** of the quote, after which the amount may be recalculated.

The request is shown to the customer as text and as a QR code, a square barcode that a phone wallet can scan to fill in the address and amount without typing. Many processors use a standard payment link format so that the wallet picks up the asset, network and amount together.

**3. The customer's wallet signs and broadcasts.** The customer approves the payment in their wallet. The wallet signs the transaction with the customer's private key and broadcasts it to the network.

**4. The transaction is seen.** Nodes receive the transaction and hold it in a waiting area of unconfirmed transactions, often called the mempool on networks that have one. The business's system, or its processor, sees the transaction arrive and can show the customer "payment detected". It is not yet confirmed.

**5. The transaction is confirmed.** The transaction is included in a block, then further blocks are added. When it reaches the depth the business requires, the payment is treated as complete. On some networks this takes seconds; on others it takes many minutes, and as Chapter 5 showed, the time varies.

**6. The business is notified and fulfils the order.** The processor sends the business's systems a notification, usually a **webhook**: an automatic message sent to a web address the business has set up, saying that payment for order 1234 is confirmed. The business's order system marks the order paid and releases the goods or service.

### Choosing a confirmation rule

The business must decide how many confirmations to wait for. The decision is a trade-off between speed and the small risk that an unconfirmed or shallowly confirmed transaction is dropped. A sensible rule scales with value: a low-value digital download might be released as soon as the payment is detected on a fast network, while a high-value order on a network with probabilistic finality might wait for several confirmations. Networks with fast, deterministic finality make this decision much simpler. Whatever the rule, it should be written down, built into the system and explained to customers, so that support staff are not asked to make judgement calls on every order.

## 3. Integration models

A business can accept crypto payments in three broad ways.

### Direct on-chain acceptance

In **direct acceptance**, the business generates its own receiving addresses from wallets it controls, watches the blockchain itself (or through a data service) for incoming payments, and holds the funds it receives. This gives the business full control and avoids processor fees. It also gives the business every responsibility at once: secure key custody, generating a fresh address per order, watching several networks, converting prices, screening incoming funds against sanctions and analytics (Chapter 6), keeping tax records for every receipt, and, if it wants bank currency, selling the assets through an exchange account. For most businesses that are not already specialists, direct acceptance concentrates a great deal of technical and compliance risk in a small team.

### Custodial payment processors

A **custodial processor** handles the payment on the business's behalf. It provides the checkout page or programming interface, generates addresses it controls, watches for payment, screens incoming funds, handles exchange rates and, typically, converts the receipts into the business's own currency and pays them to its bank account on a schedule. The business never needs to hold digital assets or keys. In return, it pays a fee and depends on the processor.

A processor with **automatic conversion** turns crypto receipts into bank currency at once, so the business's exposure to price movements is limited to the short window between quote and conversion. A processor that **settles in crypto** passes the assets to the business's wallet or account, leaving the business to decide whether and when to convert.

### Hybrid models

Many businesses use a **hybrid**: a processor handles customer checkout and screening, and pays out some or all of the receipts in stablecoins to a wallet the business controls, perhaps because the business pays overseas suppliers in stablecoins. The business then carries some custody and record-keeping duties, but not the checkout and screening work.

### Comparing the models

| Factor | Direct acceptance | Custodial processor with conversion | Hybrid |
|---|---|---|---|
| Who holds keys | The business | The processor | Both, at different stages |
| Price exposure | Until the business sells | Only during the quote window | Depends on how much is held |
| Screening and travel rule | The business | Usually the processor | Mostly the processor |
| Tax records per receipt | Full lot records | Simpler, around conversion | Full records for held assets |
| Fees | Network fees only | Processor fee plus spread | Processor fee plus network fees |
| Main dependency | Own staff and systems | Processor's security and solvency | Both |

### Due diligence on a processor

Because a custodial processor holds funds in transit, the business takes on its risks. Before signing up, a business should establish:

- which licences or registrations the processor holds in the places where the business sells and where it is based;
- how funds in transit are held, and whether they are kept separate from the processor's own funds;
- what happens to pending payments and unpaid balances if the processor fails or suspends service;
- how it screens funds, what it does with flagged payments, and what information it shares with the business;
- how quickly it pays out, in what currency, and with what fees, spreads and minimums;
- how it handles underpayments, late payments and refunds;
- how its webhooks are signed and how outages are communicated;
- which assets and networks it supports, and how it handles payments sent on unsupported networks.

A processor that cannot answer these questions clearly in writing is a processor to avoid.

## 4. Stablecoins

A **stablecoin** is a token designed to hold a steady value relative to a reference, most often one US dollar. Stablecoins are the form of digital asset most used for business payments, because they give the speed and reach of blockchain transfers without most of the price swings of native coins.

### How stablecoins aim to hold their value

Stablecoins use different mechanisms, with very different risks.

**Fiat-reserved stablecoins** are issued by a company that holds reserves, such as bank deposits and short-term government securities, intended to equal at least the value of the tokens in circulation. The issuer promises to redeem tokens for currency, usually for approved customers who meet its requirements. Their stability depends on the quality and availability of the reserves and on the issuer's ability and willingness to redeem. Reputable issuers publish regular reports on their reserves, often with independent attestation; the business should read what kind of assurance a report actually provides.

**Crypto-collateralised stablecoins** are backed by other digital assets locked in smart contracts, usually worth more than the stablecoins issued so that a fall in collateral value can be absorbed. Their stability depends on the collateral, the smart contract code and the price oracles that tell the contracts what the collateral is worth.

**Algorithmic stablecoins** try to hold their value through automatic rules that expand or shrink supply, sometimes with little or no reserve. Some have failed dramatically, losing nearly all their value within days when confidence broke. A business should treat any stablecoin without clear, high-quality reserves as a volatile asset, not as a currency.

### Risks a business should weigh

**Depeg risk.** A stablecoin's market price can drift below its target, temporarily or permanently, if holders doubt the reserves, if a reserve bank fails, or if redemptions cannot keep up with demand. A business holding the token during a depeg receives less than it expected.

**Issuer and redemption risk.** The business relies on the issuer to honour redemptions and to stay solvent. Many businesses do not redeem directly with the issuer but sell on an exchange or through their processor, so they also rely on that market functioning.

**Freezing.** Many fiat-reserved stablecoins are issued by smart contracts that let the issuer freeze tokens at specific addresses, for example in response to theft or a legal order. This is a useful protection against crime, and it also means tokens received from a tainted source could be frozen in the business's hands. Screening incoming funds (Chapter 6) addresses this.

**Network risk.** The same stablecoin may be issued on several blockchains. A token on one network is not automatically usable on another. Each network has its own fees, confirmation times and failure modes. Moving tokens between networks through a bridge introduces the bridge's risks. A business should accept a stablecoin only on networks it and its processor support, and say so clearly at checkout.

**Regulatory change.** Stablecoins have attracted specific regulation in recent years, including the European Union's Markets in Crypto-Assets Regulation and a federal framework for payment stablecoins enacted in the United States in 2025. Rules on which stablecoins may be offered, by whom, and with what reserves, continue to evolve and differ by country. A business should confirm with counsel and its processor which stablecoins it can accept in each market.

## 5. Volatility, quotes and settlement value

When an order is priced in dollars and paid in an asset whose price moves, the amount the business ends up with depends on three things: the rate at which the dollar price was converted into the asset, the price at which the asset is eventually sold, and the fees taken along the way.

### Quote windows

A processor converting a dollar price into an asset amount quotes a rate valid for a short **quote window**, often a matter of minutes. If the customer pays within the window, the processor honours the quoted amount. If the processor guarantees the rate, it bears the price risk during the window; if it does not, the business bears it until conversion.

### Worked example 1: What does the business actually receive?

An online store sells a piece of equipment for 1,200 dollars. A customer chooses to pay in bitcoin. The processor quotes an illustrative price of 60,000 dollars per bitcoin, so the payment request is for 1,200 ÷ 60,000 = 0.02 bitcoin, valid for 15 minutes. The processor charges a fee of 1 percent of the converted amount.

**Case A: the processor guarantees the quote and converts at once.** The customer pays 0.02 bitcoin within the window. The processor credits the business at the quoted 1,200 dollars and deducts its 1 percent fee: 1,200 × 0.99 = 1,188 dollars. The business receives 1,188 dollars whatever the price does next.

**Case B: no guarantee, conversion when confirmed.** The customer pays within the window, but by the time the payment is confirmed and converted, the price has fallen 1 percent to 59,400 dollars. The 0.02 bitcoin converts to 0.02 × 59,400 = 1,188 dollars. The 1 percent fee is 11.88 dollars, leaving 1,176.12 dollars. The 1 percent price movement cost the business another 11.88 dollars.

**Case C: the business holds the bitcoin.** The business chooses to keep the 0.02 bitcoin rather than convert it. A month later the price has fallen 15 percent, to 51,000 dollars. The holding is now worth 0.02 × 51,000 = 1,020 dollars, 180 dollars less than the sale price, before any fees. The price could equally have risen; the point is that by holding, the business turned a sale of equipment into a sale of equipment plus an investment position it did not set out to take.

**Case D: the customer pays late.** The customer pays the 0.02 bitcoin an hour after the quote expired, by which time the price has risen to 63,000 dollars. The payment is now worth 0.02 × 63,000 = 1,260 dollars, more than the order price. Whether the business refunds the excess, credits it, or treats the late payment under its normal policy depends on the rules it has published (see Section 7).

The four cases show why most businesses that accept volatile assets use guaranteed quotes and immediate conversion. A payment policy should state plainly whether the business converts, when, and who bears price risk during the window.

### Stablecoins and volatility

Paying in a dollar stablecoin removes almost all of this complexity for a dollar-priced business: a 1,200-dollar order is 1,200 tokens, give or take a processor fee, as long as the stablecoin holds its value. The business still faces the small risk of a depeg while it holds the tokens, which is one reason to convert promptly or to hold stablecoins only in amounts it needs for operations such as paying suppliers.

## 6. Fees and the business case

Accepting crypto costs money and staff time. The business case depends on what it replaces and how many customers will use it.

### Worked example 2: Is crypto acceptance cheaper?

An online shop's average order is 250 dollars, and it processes 800 orders a month. Use illustrative rates: card processing at 2.9 percent plus 30 cents per transaction, and a crypto processor at 1 percent per transaction with no fixed fee.

Per order:

- Card: 250 × 0.029 + 0.30 = 7.25 + 0.30 = 7.55 dollars.
- Crypto processor: 250 × 0.01 = 2.50 dollars.

If every order moved from card to crypto, monthly fees would fall from 800 × 7.55 = 6,040 dollars to 800 × 2.50 = 2,000 dollars. That headline saving of 4,040 dollars a month is the figure vendors tend to quote.

But customers choose how they pay. Suppose only 5 percent of orders, 40 a month, are paid in crypto. Those 40 orders would have cost 40 × 7.55 = 302 dollars by card and cost 40 × 2.50 = 100 dollars in crypto, a saving of 202 dollars a month. If setting up and supporting crypto payments takes a few hours of staff time each month, plus time to answer customer questions about networks and refunds, the saving may be smaller than the cost.

The real business case is usually elsewhere: reaching customers whose cards are declined or unavailable, accepting cross-border payments that would otherwise fail, avoiding chargeback fraud on high-risk goods, or paying overseas suppliers quickly. A business should estimate realistic adoption, include staff and support costs, and weigh the strategic benefits, rather than relying on the per-transaction fee difference alone.

### Hidden costs

Several costs are easy to miss:

- **Spread**: the difference between the market rate and the rate a processor or exchange actually offers. A "1 percent fee" with a 0.5 percent spread costs about 1.5 percent.
- **Payout fees**: charges for paying out to a bank account, especially across currencies.
- **Network fees on refunds and payouts**: when the business sends funds, it pays the network fee.
- **Support time**: customers who sent the wrong asset or network, or who misunderstand confirmation times, generate support work.
- **Compliance costs**: screening, record-keeping and advice, as covered in Chapter 6.

## 7. Payment edge cases

Most crypto payments go smoothly. The ones that do not are where a business either protects its reputation or damages it. Each case below needs a written rule, built into the system so that staff do not improvise.

**Underpayment.** The customer sends less than the requested amount. This often happens because the customer paid from an exchange account that deducted a withdrawal fee from the amount sent, or because they typed the amount wrongly. Common rules accept small shortfalls within a stated tolerance, ask the customer to send the difference for larger ones, and refund (minus network costs) if the difference is not paid within a set time.

**Overpayment.** The customer sends more than requested. The usual rule is to refund the excess, perhaps above a minimum below which refunding would cost more in network fees than the amount returned, in which case the excess may be credited to the customer's account.

**Late payment.** The customer pays after the quote has expired. For stablecoins this matters little. For volatile assets, the business may recalculate the payment's value at the current rate and then treat it as an underpayment or overpayment, as Worked example 1 Case D showed.

**Wrong asset or wrong network.** The customer sends a different token, or the right token on the wrong network. Whether the funds can be recovered depends on whether the business or processor controls the receiving address's key on that network and is willing to perform a manual recovery, which may be slow and costly. Many processors state that such payments may be unrecoverable. The best defence is a clear checkout that shows the network name prominently, warns about mismatches, and, where possible, uses payment links that set the network automatically.

**Duplicate payment.** The customer pays twice, perhaps after thinking the first payment had failed. Unique addresses per order make duplicates easy to spot; the excess is treated as an overpayment.

**Payment from a flagged source.** Screening (Chapter 6) flags the incoming funds. The business must follow its compliance procedure, which may require holding the funds and reporting rather than either fulfilling the order or returning the funds.

### Worked example 3: Applying an underpayment tolerance

A business accepts a dollar stablecoin and has published this rule: shortfalls of up to 0.50 tokens are accepted as payment in full; larger shortfalls must be topped up within 24 hours, or the amount received will be refunded minus the network fee.

An invoice is for 100.00 tokens. The customer pays from an exchange account, and 99.40 tokens arrive.

- Shortfall: 100.00 − 99.40 = 0.60 tokens.
- 0.60 is greater than the 0.50 tolerance, so the order is not treated as paid in full.

The system automatically emails the customer, explaining that 0.60 tokens are outstanding, giving the same address for the top-up, and stating the 24-hour deadline. Had 99.60 tokens arrived, the shortfall of 0.40 would have been within tolerance and the order would have been released automatically, with the 0.40 recorded as a payment discount in the accounts.

The tolerance is a business decision. It should be small enough not to cost much and large enough to absorb the typical exchange withdrawal fee, so that ordinary customers are not caught by it. Writing the rule down, applying it automatically and recording the discount in the accounts are what keep it fair and auditable.

## 8. Refunds

Because blockchain transactions cannot be reversed, a refund is a new payment from the business to the customer. The refund policy must answer four questions, and the answers must be published before the customer pays.

1. **In what value is the refund calculated?** Most businesses refund the original price in their own currency (the "fiat-equivalent" method), not the original quantity of the asset.
2. **In what asset, and on what network, is it paid?** Usually the same asset the customer paid with, though some businesses refund stablecoins or bank currency only.
3. **To what address?** A refund should not automatically go back to the sending address, because the customer may have paid from an exchange account that cannot receive returns to that address. The customer should supply a refund address, which the business should screen and confirm.
4. **Who pays the network fee?** Typically the business absorbs it for faulty goods and may deduct it for change-of-mind returns, if the policy says so in advance.

### Worked example 4: Refunding when the price has moved

A customer paid 0.5 units of a volatile asset for a 1,500-dollar item, when the asset's illustrative price was 3,000 dollars (0.5 × 3,000 = 1,500). A month later the customer returns the item under the store's 30-day policy.

**If the price has risen to 3,600 dollars:**

- Fiat-equivalent refund: 1,500 ÷ 3,600 ≈ 0.4167 units (exactly 0.416666...), worth 1,500 dollars.
- Same-quantity refund: 0.5 units, worth 0.5 × 3,600 = 1,800 dollars. The business would pay 300 dollars more than the sale price.

**If the price has fallen to 2,400 dollars:**

- Fiat-equivalent refund: 1,500 ÷ 2,400 = 0.625 units, worth 1,500 dollars.
- Same-quantity refund: 0.5 units, worth 0.5 × 2,400 = 1,200 dollars. The customer would receive 300 dollars less than they paid.

A same-quantity policy turns every refund into a bet on the asset's price, won by the business or the customer depending on the direction. The fiat-equivalent method keeps both parties where they started in money terms, which is why most businesses that price in their own currency use it. Whichever method the business chooses, customers must be told at checkout. A customer who learns the method only when asking for a refund will feel cheated, whatever the arithmetic says.

For stablecoin payments, the two methods give nearly the same result, which is another practical advantage of stablecoins for commerce.

## 9. Accounting and reconciliation

A crypto payment must end up correctly in the business's books, matched to the right order, at the right value, with a record that an auditor or tax authority can follow. The accounting standards and tax rules that apply depend on the business's country, and a qualified accountant should confirm the treatment. The principles below are common.

### Recording receipts

When a business receives digital assets as payment for goods or services, it generally recognises revenue at the fair value of what it received, measured in its reporting currency at the time of the transaction. If the processor converts immediately, the accounting looks much like any other payment method with a fee. If the business holds the assets, they become an asset on its balance sheet, and later sale or use creates a gain or loss against their recorded value, as Chapter 6 explained for tax. How held digital assets are measured on the balance sheet at the end of each period differs between accounting frameworks and has changed in some of them in recent years, which is a question for the business's accountant.

### Worked example 5: Journal entries for a stablecoin sale

A business invoices a customer 1,000 dollars and the customer pays 1,000 dollar-stablecoin tokens, each worth 1 dollar at the time.

**If the processor converts immediately**, charging 0.5 percent, the processor's fee is 1,000 × 0.005 = 5 dollars, and 995 dollars reaches the bank. The entry is:

| Account | Debit | Credit |
|---|---|---|
| Bank | 995 | |
| Payment processing fees | 5 | |
| Sales revenue | | 1,000 |

**If the business holds the tokens** for two weeks and then sells them when they trade at 0.998 dollars each, the entries are:

At receipt:

| Account | Debit | Credit |
|---|---|---|
| Digital assets (stablecoin) | 1,000 | |
| Sales revenue | | 1,000 |

At sale, for 1,000 × 0.998 = 998 dollars:

| Account | Debit | Credit |
|---|---|---|
| Bank | 998 | |
| Loss on disposal of digital assets | 2 | |
| Digital assets (stablecoin) | | 1,000 |

In both cases the revenue is 1,000 dollars, because that is the value of what the customer paid for the goods. The difference between the two approaches appears separately as a fee in the first case and as a loss on disposal in the second. Keeping these items separate in the accounts makes it clear how much the business earned from selling goods and how much it gained or lost from holding digital assets.

### Reconciliation

**Reconciliation** is the regular check that three records agree: the business's order system, the processor's or wallet's transaction records, and the accounting ledger. For crypto payments, the key matching field is the **transaction identifier** (often called a transaction hash), the unique reference of each transfer on the blockchain. Every order paid in crypto should store the transaction identifier, the asset, the network, the amount received, the rate used and the processor's payment reference.

A daily reconciliation should answer:

- Is every confirmed payment matched to exactly one order?
- Is every order marked paid backed by a confirmed payment?
- Do the processor's payout reports equal the sum of payments minus fees for the period?
- Are underpayments, overpayments and refunds recorded and explained?

Because blockchain records are public and permanent, a business can always check a disputed payment against the chain itself. That is a real advantage over many traditional payment methods, but only if the business stored the transaction identifier in the first place.

### Webhooks done properly

Order systems usually learn about payments through webhooks, which makes their security and reliability part of the accounting control.

- **Verify signatures.** Processors sign webhook messages with a secret key. The business must check the signature on every message, otherwise anyone who discovers the web address can send a fake "payment confirmed" message and receive free goods.
- **Make handling idempotent.** Webhooks are often delivered more than once, for example after a network timeout. Processing must be **idempotent**: handling the same message twice must have the same effect as handling it once. The usual method is to record the processor's event identifier and ignore any event already processed.
- **Do not trust the webhook alone for large orders.** For high-value orders, the system can confirm the payment status with the processor's interface, or check the blockchain directly, before releasing goods.
- **Handle missed messages.** If the business's system is down when a webhook arrives, it may never learn of the payment. A scheduled job that asks the processor for recent payments catches what was missed.

## 10. Security and operations

**Address substitution.** Some malware watches a computer's clipboard and replaces any copied crypto address with the attacker's address. A business that pays suppliers should verify the full address on a separate channel, use allow-lists of approved addresses, and send a small test payment before a large one to a new address.

**Payment page integrity.** If an attacker can alter the checkout page, they can replace the receiving address with their own. Pages should be served securely, scripts from third parties should be limited, and the business should monitor that the addresses shown match those its processor generated.

**Hot wallet limits and sweeps.** A business that holds received funds should keep only an operating amount in hot wallets and move the rest regularly to cold storage or multisig custody, as Chapter 6 described.

**Customer communication.** Clear wording at checkout prevents most support problems. It should name the asset and network in large type, state the amount precisely, show the quote expiry, explain how long confirmation takes, state that blockchain payments cannot be reversed, and summarise the refund method. Support staff should have approved answers for the common edge cases.

**Monitoring.** The business should be alerted when payments stop arriving (which may mean the integration is broken), when an unusual number of underpayments or wrong-network payments occur (which may mean the checkout is confusing), or when the processor's payouts fall behind.

### Case study: Ridgeline Outdoor Co. adds stablecoin checkout

Ridgeline Outdoor Co. is a fictional company invented for this chapter. It sells camping equipment online, mostly within its own country, with a growing number of customers abroad whose card payments often fail.

Ridgeline's goal is to accept dollar stablecoins from overseas customers without holding digital assets itself. After due diligence on three processors (Section 3), it chooses one that is licensed in its home market and its two largest overseas markets, converts receipts to dollars the same day and supports the stablecoin on two networks. Ridgeline decides to offer only one network at launch, to keep the checkout simple.

The project team writes a payment policy before writing any code:

- Payments are accepted in one dollar stablecoin on one named network. The network name is shown in large type next to the QR code.
- Each order gets a unique address. Quotes are valid for 30 minutes.
- Orders are released when the processor confirms the payment.
- Shortfalls up to 0.50 tokens are accepted; larger shortfalls must be topped up within 24 hours or are refunded minus the network fee.
- Overpayments above 2 tokens are refunded; smaller ones are credited as store credit.
- Refunds are calculated in dollars and paid in the same stablecoin to an address the customer supplies, which is screened before payment.
- Wrong-network payments are referred to the processor, and the customer is told in advance that recovery is not guaranteed.

The developers build the integration with signed, idempotent webhooks and a nightly reconciliation job that compares orders, processor payments and payouts and emails any mismatch to the finance team. Each paid order stores the transaction identifier.

In the first month, the reconciliation job finds three orders where the webhook had failed during a brief outage on Ridgeline's side; the scheduled check had caught the payments and released the orders a few hours late, and the finance team confirmed all three against the processor's records. Support tickets reveal that most underpayments come from customers paying from one particular exchange that deducts its withdrawal fee from the amount sent; Ridgeline adds a line to the checkout warning customers to send the full amount after fees.

The case shows that the code is the smaller part of crypto payments integration. The larger part is policy, written before launch, and the controls that make the policy work automatically.

## SKA Field Case Study: Designing a prepaid, metered credit

This case comes from the operation of Sales King Academy itself, the platform on which you are taking this course. It is about a payment design that is deliberately not a cryptocurrency, and why that choice matters.

### The situation

Sales King Academy charges for usage of its AI features through **Beats**, its platform currency. One Beat equals one US dollar, and the minimum purchase is 10 Beats. Beats are a prepaid credit for using the platform's services. They are not a cryptocurrency, token, coin or investment, and they are not traded on any blockchain. Usage is metered by seconds of compute, and only full seconds are charged. Each user can see their own Beats balance and usage, along with their own DNA-16 identifier, and nothing about the platform's internal records.

The platform runs 26 specialist AI agents. The cost of answering a question depends heavily on which AI model answers it: large models cost much more to run than small ones.

### The problems it caused

An audit on 7 October 2026 found that unpaid users had been served by the most expensive model. Every free question was being answered at the highest cost the platform could incur, with no revenue to cover it. For a metered, prepaid system, this is the worst possible mismatch between who pays and what is consumed: the users who paid nothing used the most expensive resource.

The same audit period found a second, related issue: internal chain numbers were appearing in API responses and on screens. For a system in which users should see only their own balance, usage and identifier, that was a privacy failure in the place where users check their spending.

### What was done

Routing was changed so that free and explorer tiers use a small, free model, and paid tiers get the large models. The expensive resource is now consumed by the users whose prepaid Beats pay for it.

A single outgoing filter was put in place to strip internal chain numbers from everything leaving the platform, so the account and usage views show users only their DNA-16, their usage and their Beats.

### What it shows

1. **Prepaid credit separates payment from consumption.** A customer buys Beats once, at a minimum of 10, and spends them in small amounts as they use the service. This avoids a separate payment for every question, much as the processor payouts in Section 3 batch many customer payments into one bank transfer.
2. **Metering rules must be stated precisely.** Charging only full seconds means a fraction of a second is not billed. For example, three tasks lasting 2.4, 7.9 and 0.6 seconds of compute total 10.9 seconds, but the billed seconds are 2 + 7 + 0 = 9. The customer is never charged for time not fully used, and the cost of those tasks in Beats is 9 × **[founder figure: Beats charged per second of compute]**. A rule like this, published and applied by the system, is the metering equivalent of the underpayment tolerance in Worked example 3: small, fair and automatic.
3. **Unit economics decide routing.** The cost of serving a request must be matched to what is paid for it. Sending free users to the most expensive model inverted that match; the routing change restored it.
4. **Not everything that holds value needs a blockchain.** Beats are sold and spent with one party, the platform, which keeps the record. Under the decision test in Chapter 5, a single-issuer prepaid credit fits an ordinary ledger kept by that party better than a blockchain token: it is simpler, cheaper, easier to correct, and avoids the custody, volatility and regulatory questions this chapter has described.
5. **Show customers their own money, and only that.** Users need to see their balance and usage to trust a metered system. They do not need, and should not see, internal records.

### What remains open

- The model costs per tier before and after the routing change: **[founder figure: model cost per tier before and after 7 October]**
- The share of free versus paid usage: **[founder figure: free and paid share of usage]**
- Monthly Beats sales: **[founder figure: monthly Beats revenue]**
- How usage data is reconciled with Beats balances, and how often: **[founder figure: reconciliation method and frequency]**

A further open design question for any prepaid system is how to present usage so that customers can predict their spending before they act, for example by showing an estimated cost before a long task begins.

### Discussion questions

1. Why is a prepaid credit issued by one platform better run as a database ledger than as a blockchain token?
2. What are the advantages to the customer of charging only full seconds of compute? Is there any disadvantage to the platform?
3. How would you design a daily reconciliation between usage records and Beats balances, using the principles in Section 9?

## SKA Lab: Price, record and reconcile with SKA agents

In this lab you use the live Sales King Academy platform to test the calculations and policies in this chapter, and to inspect a real metered, prepaid credit system. You need a free account and text chat only; you do not need to buy Beats to complete the lab.

### Steps

1. **Sign in** at saleskingacademy.com and open your account or wallet view. Record your Beats balance and the usage information shown. Note which identifiers appear, and compare them with the rule that a user sees only their DNA-16, usage and Beats.
2. **Ask Monetize a pricing question in Deterministic mode.** Open the Monetize agent, choose Deterministic, and ask: "What should a refund policy for crypto payments specify?" Record the source badge and compare the answer with Section 8.
3. **Ask the same question in Natural mode.** Switch to Natural and repeat the question. Compare wording, length and badge, and check that the key terms match.
4. **Test exact arithmetic.** Ask Monetize: "An order costs 1,200 dollars. The quote is 60,000 dollars per bitcoin. The price falls to 59,400 dollars before conversion and the processor charges 1 percent. What does the business receive?" Compare the result with Worked example 1 Case B (1,176.12 dollars).
5. **Ask Ledger for journal entries.** Open the Ledger agent and ask: "Record a 1,000-dollar sale paid in a dollar stablecoin, converted immediately with a 0.5 percent fee." Compare the entries with Worked example 5.
6. **Ask a live question.** Ask Ledger: "What is today's euro to US dollar reference exchange rate?" Record the source badge and the source named. Then ask the same question again and note whether the answer is the same.
7. **Draft a policy agent.** Open Agent Builder and start a new agent on top of the Monetize base agent. Give it instructions to answer customer questions about your own (real or imagined) business's crypto refund and underpayment policy, using the rules you write from Sections 7 and 8. Ask it two test questions. You do not need to publish it.

### Record your results

| Step | Agent and mode | Question (short form) | Source badge | Result correct? (yes / no / partly) | Notes |
|---|---|---|---|---|---|
| 1 | Account view | Balance and usage | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

### Reflect

Write three to five sentences answering: Which of the platform's answers would you use directly in a customer-facing payment policy, and which would you have checked by an accountant or lawyer first? What did inspecting your own Beats balance and usage teach you about what customers of a metered system need to see?

## Summary

Blockchain payments are push payments: the customer sends funds to an address the business supplies. Once confirmed they are final, with no chargebacks, they run at all hours and across borders, and their network fees depend on network conditions rather than value. The customer must send the right asset, on the right network, for the right amount, before the quote expires.

A payment request specifies asset, network, amount, receiving address and expiry. The business sets a confirmation rule that scales with value and is notified through webhooks. Businesses can accept payments directly, through a custodial processor, or through a hybrid; processors reduce custody, screening and record-keeping burdens in exchange for fees and dependence, so due diligence on them is essential.

Stablecoins aim to hold a fixed value through reserves, crypto collateral or algorithms, and carry depeg, issuer, freezing, network and regulatory risks. With volatile assets, the value a business receives depends on the quoted rate, the conversion price and fees; guaranteed quotes and immediate conversion limit exposure. The business case for crypto acceptance depends on realistic adoption and on strategic benefits, not only per-transaction fees.

Edge cases such as underpayment, overpayment, late payment, wrong networks, duplicates and flagged funds need written rules applied automatically. Refunds are new payments, and a fiat-equivalent method keeps both parties whole. Accounting records revenue at the value received and separates fees and holding gains or losses; reconciliation matches orders, payments and payouts using transaction identifiers, with signed and idempotent webhooks. The Sales King Academy field case showed a prepaid, metered credit designed as a database ledger rather than a token, with full-second metering, routing matched to payment, and a privacy filter on what users see.

## Key terms

- **Push payment**: a payment initiated by the payer sending funds, rather than pulled by the payee.
- **Chargeback**: a card payment reversal initiated through the card network after a customer dispute; not available for blockchain payments.
- **Payment request**: the asset, network, amount, receiving address and expiry presented to a customer.
- **Quote window**: the period during which a quoted exchange rate is honoured.
- **Mempool**: the pool of broadcast but unconfirmed transactions on networks that use one.
- **Confirmation rule**: the business's written rule for how many confirmations a payment needs before fulfilment.
- **Webhook**: an automatic message from a processor to the business's system reporting an event such as a confirmed payment.
- **Direct acceptance**: receiving crypto payments into wallets the business controls, without a processor.
- **Custodial processor**: a service that accepts crypto payments on the business's behalf, holding the keys.
- **Automatic conversion**: immediate conversion of crypto receipts into the business's own currency.
- **Stablecoin**: a token designed to hold a fixed value relative to a reference such as one US dollar.
- **Fiat-reserved stablecoin**: a stablecoin backed by reserves of conventional assets held by an issuer.
- **Depeg**: a stablecoin's market price moving away from its target value.
- **Redemption**: exchanging a stablecoin with its issuer for the reference currency.
- **Spread**: the difference between the market rate and the rate actually offered.
- **Underpayment tolerance**: a published shortfall below which a payment is accepted as full.
- **Fiat-equivalent refund**: a refund calculated in the business's own currency at the original price.
- **Transaction identifier (transaction hash)**: the unique reference of a transfer on a blockchain.
- **Reconciliation**: regular checking that orders, payment records and accounting entries agree.
- **Idempotent**: producing the same result whether an operation is performed once or several times.
- **Address substitution**: malware that replaces a copied crypto address with an attacker's address.
- **Prepaid credit**: value bought in advance from a provider and spent on its services, such as Beats on Sales King Academy; not a cryptocurrency.
- **Metering**: measuring usage in defined units, such as full seconds of compute, to charge for it.

## Review questions

1. Why does a push payment remove the risk of a merchant's systems leaking card details?
2. What five pieces of information should a crypto payment request contain?
3. Why should a confirmation rule scale with the value of the order?
4. What are the main trade-offs between direct acceptance and a custodial processor with automatic conversion?
5. What risks does a business take on when it holds a fiat-reserved stablecoin?
6. In Worked example 1 Case B, what does the business receive, and why is it less than in Case A?
7. Why did the fee saving in Worked example 2 fall from 4,040 dollars to 202 dollars a month?
8. Under the tolerance rule in Worked example 3, what happens if 99.60 tokens arrive for a 100.00-token invoice?
9. Why should a refund not automatically be sent back to the address the customer paid from?
10. If a customer paid 0.5 units at 3,000 dollars each and the price is now 3,600 dollars, how many units does a fiat-equivalent refund return?
11. In Worked example 5, why is sales revenue 1,000 dollars in both the conversion and holding cases?
12. What does it mean for webhook handling to be idempotent, and why is it necessary?
13. What controls protect against address substitution when paying suppliers?
14. In the SKA field case, how many seconds are billed for tasks of 2.4, 7.9 and 0.6 seconds, and why?
15. Why does the chapter argue that Beats are better run as a database ledger than as a blockchain token?

## Answer key

1. The customer sends funds from their own wallet to an address the merchant provides, so the merchant never receives any credentials that could be used to take money.
2. The asset, the network, the amount in that asset, the receiving address (ideally unique to the order), and the quote's expiry time.
3. A higher-value order is more worth protecting against the small chance that a shallowly confirmed transaction is dropped, while a low-value order is better served by fast release.
4. Direct acceptance gives full control and avoids processor fees, but the business takes on custody, screening, monitoring, conversion and full tax records. A processor with conversion removes most of those burdens and limits price exposure to the quote window, at the cost of fees and dependence on the processor's security, licensing and solvency.
5. Depeg risk, issuer and redemption risk, the risk that tokens are frozen by the issuer, network risk, and the risk of regulatory change affecting which stablecoins may be used.
6. 0.02 × 59,400 = 1,188 dollars before fees, minus the 1 percent fee of 11.88 dollars, leaving 1,176.12 dollars. It is less than Case A's 1,188 dollars because the business, not the processor, bore the 1 percent price fall before conversion.
7. The 4,040-dollar figure assumed every order moved to crypto. With only 5 percent of orders, 40 a month, paid in crypto, the saving is 40 × (7.55 − 2.50) = 202 dollars.
8. The shortfall is 0.40 tokens, within the 0.50 tolerance, so the order is released automatically and the 0.40 is recorded as a payment discount.
9. The customer may have paid from an exchange account whose sending address cannot receive returns, so funds could be lost. The customer should supply a refund address, which the business screens and confirms.
10. 1,500 ÷ 3,600 ≈ 0.4167 units, worth 1,500 dollars.
11. Revenue is the value of what the customer paid for the goods at the time of the sale. The processor fee and the later loss on disposal are separate items, recorded as an expense and a loss respectively.
12. Processing the same message more than once has the same effect as processing it once. Webhooks may be delivered several times, so without idempotency an order could be marked paid twice or a refund issued twice.
13. Verifying the full address on a separate channel, using allow-lists of approved addresses, and sending a small test payment before a large payment to a new address.
14. 2 + 7 + 0 = 9 seconds, because only full seconds of compute are charged and fractions of a second are not billed.
15. Beats are issued and spent with one party, the platform, which keeps the record. Under the decision test in Chapter 5 a blockchain adds no benefit when one party writes the record, while a database ledger is simpler, cheaper, easier to correct and avoids custody, volatility and regulatory issues.

## Further reading

- Satoshi Nakamoto (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System."
- Andreas M. Antonopoulos. *Mastering Bitcoin*. O'Reilly Media.
- Andreas M. Antonopoulos and Gavin Wood (2018). *Mastering Ethereum*. O'Reilly Media.
- Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller and Steven Goldfeder (2016). *Bitcoin and Cryptocurrency Technologies*. Princeton University Press.
