---
key: blockchain_fundamentals_for_business
title: "Blockchain Fundamentals For Business"
program: sales_king_academy
course_level: 
dna16: ""
l4_address: ""
chain256_anchor: ""
updated_at: "2026-10-08"
chapter: "Sales King Academy, Volume 2, Chapter 5"
generated_by: "Claude (Anthropic), directed by Sales King Academy LLC"
training_use: "specialized SKA models (business, sales, marketing education); not for general-purpose models competing with the writing model"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy program - AI Technology & Integration (original)
---

# Blockchain Fundamentals for Business

This chapter explains how blockchains actually work and what they are genuinely good for in commerce. You will learn the building blocks one at a time: cryptographic hashes, blocks and the chain that links them, the consensus methods that let strangers agree on a single history, the key pairs and wallets that control assets, and the smart contracts that run on some networks. With those pieces in place, the chapter turns to business judgment: where a shared ledger removes a real cost, where an ordinary database is the better choice, and how to plan custody so that a lost key does not become a lost business. The chapter is education, not investment advice. It makes no predictions about prices, and every figure in the worked examples is an illustration chosen to make the arithmetic clear. It closes with a field case from the Sales King Academy platform and a lab you complete on the live site.

## Learning objectives

By the end of this chapter you will be able to:

1. Explain what a cryptographic hash is, list its essential properties, and show how hashing makes changes to a record evident.
2. Describe how blocks are linked into a chain and why rewriting an old block forces every later block to be rewritten.
3. Compare proof of work and proof of stake, and explain the difference between probabilistic and economic finality.
4. Explain public and private keys, digital signatures, addresses and wallets, and distinguish self-custody from custodial arrangements.
5. Describe what a smart contract is, what it can and cannot do, and why outside data (oracles) is a weak point.
6. Distinguish public, permissioned and private ledgers, and apply a structured test to decide whether a blockchain or a conventional database fits a business problem.
7. Calculate transaction fees, confirmation waiting times and the effect of multi-signature custody on the risk of losing access.
8. Identify the main limits and risks of blockchain systems: irreversibility, key loss, scaling, privacy, governance and regulatory uncertainty.
9. Use the Sales King Academy platform to compare grounded, live and generated answers to blockchain questions and judge which to rely on.

## 1. The problem a blockchain solves

Every business keeps records of who owns what and who owes whom. Usually a single trusted party keeps the official record. A bank keeps the record of your account balance. A land registry keeps the record of who owns a parcel of land. A company keeps its own books, and its auditors check them. This arrangement works well because everyone involved accepts that one party's record is the authoritative one.

The arrangement breaks down when there is no party that everyone is willing to trust, or when each party keeps its own copy and the copies drift apart. Consider five companies in a supply chain: a grower, a processor, a shipper, a wholesaler and a retailer. Each keeps its own records of the same shipments. When the grower says it shipped 2,000 crates and the processor says it received 1,950, someone has to spend time finding out which record is right. Multiply that by thousands of shipments a month and reconciliation becomes a meaningful cost. No single company wants another to hold the master copy, because whoever controls the record could change it in their own favour.

A **blockchain** is one answer to this problem. It is a ledger that many parties hold copies of, where new entries are added only by following agreed rules, and where any attempt to change an old entry is immediately visible to everyone. Instead of trusting one record keeper, participants trust the combination of mathematics, shared rules and the fact that many independent copies exist.

The first widely used blockchain was Bitcoin, described in a 2008 paper published under the name Satoshi Nakamoto and launched in January 2009. Its purpose was narrow: to let people send digital money to each other without a bank in the middle, while preventing the same coin from being spent twice. The **double-spending problem** is the heart of the matter. A digital file can be copied endlessly, so a digital coin needs some way to make sure that once it has been sent to one person, it cannot also be sent to another. Banks solve this by keeping the single authoritative ledger. Bitcoin solved it by having a network of independent computers agree on one shared order of transactions.

It is worth stating early what a blockchain does not do. It does not make information true. If a shipper records that 2,000 crates left the warehouse when only 1,900 did, the blockchain will faithfully preserve the false entry forever. A blockchain guarantees that the record has not been changed after the fact and that everyone sees the same record. It does not guarantee that the record matched reality when it was written. This gap between the ledger and the physical world is one of the most important limits for any business use, and it comes up again in Sections 6 and 8.

## 2. Hashes: the fingerprint of data

A **cryptographic hash function** takes any piece of data, whether a single word, an invoice or an entire video file, and produces a short, fixed-length output called a **hash** or **digest**. The most widely used hash function in blockchains is SHA-256, which produces an output of 256 bits, usually written as 64 hexadecimal characters (the digits 0 to 9 and the letters a to f).

A good cryptographic hash function has four properties that matter for business records.

**It is deterministic.** The same input always produces exactly the same hash. Anyone, anywhere, using the same function, gets the same result. This is what makes hashes useful for checking: two parties can each compute the hash of a document and compare the results without sending the document itself.

**It is fast to compute.** Producing a hash for a large file takes a fraction of a second on an ordinary computer.

**A small change produces a completely different hash.** Changing one character of the input changes the output so thoroughly that the two hashes look unrelated. This is sometimes called the avalanche effect. There is no way to tell from two hashes whether their inputs were nearly identical or entirely different.

**It is one-way and collision-resistant.** Given a hash, there is no practical way to work backwards to find the input, other than guessing inputs and checking each one. And it is not practically possible to find two different inputs that produce the same hash. For SHA-256, nobody has ever publicly demonstrated such a collision.

These properties make a hash work like a fingerprint for data. If you store the hash of a contract today and someone hands you a contract next year claiming it is the same one, you can hash what they give you and compare. If the hashes match, the document is the same, character for character. If they differ, something was changed.

### Worked example 1: Detecting a changed invoice

A business records the line "Invoice 1042: pay 500.00 USD to Delta Freight" (Delta Freight is a made-up company). Computing its SHA-256 hash gives:

`34315a0d9cfad6b92135ac8bc2b8a42699b13eb436d53f7ebc644b41c2d50b95`

Now suppose someone alters the amount so the line reads "Invoice 1042: pay 600.00 USD to Delta Freight". Only one character has changed, the 5 has become a 6. The new hash is:

`82552372f5c23cbab288052ffe2447e317ba00b9cb0c5b6b7cd8583cd85d32c6`

The two hashes share no visible pattern. The first characters are 3431 and 8255; nothing about them suggests the inputs were almost identical. If the business had stored the first hash somewhere safe, such as in a shared ledger or with an auditor, then anyone checking the altered invoice would see at once that it no longer matched.

You can check this yourself. On most computers, a command-line tool or a short program in any common language will compute SHA-256. Type the line exactly, with the same spacing and punctuation and no trailing space or line break, and you will get the same 64 characters shown here. Add a full stop at the end, and you will get something completely different. That sensitivity is the point: a hash protects the exact bytes, not the meaning.

Note what the hash does and does not do. It detects change; it does not prevent it, and it is only as useful as the place it is stored. If the person who altered the invoice can also replace the stored hash, nothing has been gained. That is the problem the chain of blocks addresses. Even without a blockchain, hashing important records and keeping the hashes somewhere separate is a cheap, reliable control.

## 3. Blocks and the chain

A blockchain groups transactions into **blocks**. Each block contains three essential things: a batch of transactions, some housekeeping information such as a timestamp, and the hash of the previous block. That last element is what turns a pile of blocks into a chain.

Because each block includes the hash of the block before it, the blocks are linked in a fixed order. The hash of block 3 depends on the contents of block 3, which include the hash of block 2, which depends on the contents of block 2, which include the hash of block 1. Change anything in block 1 and its hash changes. Block 2's stored "previous hash" no longer matches, so block 2 is now invalid unless it too is rewritten, which changes block 2's hash, which breaks block 3, and so on to the end of the chain.

The first block in a chain has no predecessor. It is called the **genesis block**, and by convention its "previous hash" is a placeholder, often a string of zeros.

### Worked example 2: Following a change down a chain

Build a tiny three-block chain. For simplicity, each block holds one record, and each block's hash is the SHA-256 of the previous block's hash (written as 64 hexadecimal characters) followed directly by the record text. The genesis block uses 64 zeros as its previous hash. Only the first 16 characters of each hash are shown.

| Block | Record | Hash (first 16 characters) |
|---|---|---|
| 1 | Block 1: A pays B 10 | bd4ca2d46beee488 |
| 2 | Block 2: B pays C 4 | 60ae4e79ca52c6a5 |
| 3 | Block 3: C pays A 1 | daa4a06ac39bbdb0 |

Now someone changes block 1 to read "A pays B 90" and recomputes the hashes:

| Block | Record | Hash (first 16 characters) |
|---|---|---|
| 1 | Block 1: A pays B 90 | 172182b0e54ded61 |
| 2 | Block 2: B pays C 4 | 5b1501e3732828e9 |
| 3 | Block 3: C pays A 1 | c44d4b9814edd1c3 |

Blocks 2 and 3 are unchanged in content, yet their hashes have changed completely, because each one depends on the block before it. Anyone who kept the original final hash, daa4a06ac39bbdb0..., can compare it with the new final hash, c44d4b9814edd1c3..., and know that something in the history has been altered, without even reading the blocks. A single short value at the end of the chain vouches for every record before it.

This is the property people mean when they call a blockchain **tamper-evident**. Note the careful wording. It is not tamper-proof: a person with a copy can still edit it. What they cannot do is edit it in a way that goes unnoticed by anyone holding an honest copy.

### Merkle trees

Real blocks contain hundreds or thousands of transactions, not one. Rather than hashing them all as a single lump, most blockchains arrange them in a **Merkle tree**, named after the cryptographer Ralph Merkle. Transactions are hashed in pairs, the resulting hashes are hashed in pairs again, and so on until a single hash remains at the top, called the **Merkle root**. The block header stores this root.

The benefit is efficient proof. To show that one particular transaction is in a block of 4,000 transactions, you do not need to supply all 4,000. You need only the transaction itself and about a dozen intermediate hashes along its branch of the tree, because a tree with 4,000 leaves is about 12 levels deep. Anyone can recompute the branch up to the root and check it matches the root in the block header. This is how lightweight wallet software on a phone can verify that a payment was included without downloading the entire chain.

### Why many copies matter

Hash linking on its own only shows that a chain has been changed if someone holds an honest copy to compare against. If one company kept the only copy, it could rewrite the whole chain and recompute every hash, and nobody would know. The protection comes from having many independent copies, held by parties who do not take orders from each other, together with rules for deciding which version of the chain is the real one when copies disagree. Those rules are the subject of the next section.

## 4. Consensus: agreeing on one history

A blockchain network is a collection of computers, called **nodes**, each holding a copy of the ledger and passing new transactions to one another. At any moment, different nodes may have heard about different transactions, in different orders. The network needs a way to agree on which block comes next, so that everyone ends up with the same history. The method a network uses is its **consensus mechanism**.

The difficulty is that some participants may be dishonest, faulty or offline, and on a public network nobody knows who the participants are. A person could run thousands of fake nodes to try to outvote everyone else; this is called a **Sybil attack**. Voting by node count therefore does not work on an open network. Consensus mechanisms solve this by tying influence to something that is costly to fake.

### Proof of work

In **proof of work**, nodes called **miners** compete to add the next block. To win, a miner must find a value (called a nonce) that, when included in the block header, makes the block's hash fall below a target number. Because hash outputs cannot be predicted, the only way to find such a value is to try enormous numbers of guesses. The first miner to find one broadcasts the block; others check it with a single hash computation, which is fast, and accept it if it is valid. The winning miner receives newly created coins and the fees attached to the block's transactions.

The network adjusts the target so that blocks arrive at a steady average rate. For Bitcoin, the target average is one block every ten minutes. If miners collectively add more computing power, the puzzle is made harder, and if they leave, it is made easier.

Proof of work secures the chain because rewriting history requires redoing the work. To change a block from an hour ago, an attacker would have to recompute that block and every block since, and then overtake the honest network, which keeps adding new blocks in the meantime. Nodes follow the valid chain with the most accumulated work. An attacker who controls more than half of the network's computing power could, in principle, outpace the honest miners; this is called a **51 percent attack**. On large networks the cost of assembling that much computing power is very high, but on small networks it has happened. The price of this security is heavy electricity use and specialised hardware, which has drawn sustained public criticism.

### Proof of stake

In **proof of stake**, the right to propose and confirm blocks goes to **validators** who lock up, or "stake", the network's own coins as a security deposit. Validators are chosen to propose blocks in a way weighted by their stake, and other validators vote to confirm them. A validator that breaks the rules, for example by signing two conflicting blocks, can have part of its stake destroyed, a penalty called **slashing**. Security comes from the fact that attacking the network would require acquiring a very large share of the staked coins and would put that stake at risk.

Ethereum switched from proof of work to proof of stake in September 2022, an event widely called "the Merge". Proof of stake uses far less energy than proof of work, because it does not depend on large-scale guessing. Its critics point to other concerns: those who already hold many coins gain more influence, and the rules are more complex, which creates more room for subtle flaws.

### Permissioned consensus

Business networks where every participant is known often use simpler, classical consensus methods. A fixed set of approved nodes, perhaps one per member company, votes on each block, and a block is final once a sufficient majority, often two thirds, agree. These methods are fast and use little energy, but they rely on the membership list. If most members colluded, they could rewrite the record. That is acceptable when the members are bound by contracts and law, and it is one reason permissioned ledgers are governed as much by legal agreements as by code.

### Finality: when is a payment really done?

**Finality** is the point at which a transaction cannot be reversed. In proof-of-work systems, finality is **probabilistic**. A transaction included in the newest block could, in rare cases, be dropped if two miners find blocks at almost the same time and the network later settles on the other branch. Each further block built on top makes reversal less likely. The number of blocks added after the one containing a transaction is called its number of **confirmations**. A common practice for large Bitcoin payments has been to wait for six confirmations, though each business sets its own rule according to the value at stake.

Many proof-of-stake systems offer **economic finality**: after a checkpoint is confirmed by a large enough share of validators, reversing it would require validators to accept the destruction of a large amount of staked value. Permissioned systems often give **immediate finality**: once the required majority signs a block, it is final.

For a business, finality is not an abstract idea. It decides when you ship goods, release a service or credit a customer's account.

### Worked example 3: How long will six confirmations take?

A merchant accepts a payment on a network whose blocks arrive on average every ten minutes, and its policy is to wait for six confirmations before releasing high-value goods.

The average wait is simple: 6 × 10 = 60 minutes. But block times are not regular. Because each block is found by random guessing, the arrival of blocks behaves like a random process in which the time between blocks varies widely: sometimes a block comes after one minute, sometimes after thirty. A standard way to model this is a Poisson process, where the number of blocks found in a period follows a Poisson distribution with an average equal to the period's length divided by the average block time.

The chance of receiving at least six blocks within a given time is therefore one minus the chance of receiving five or fewer. Computing it for three waiting times:

| Waiting time | Expected blocks | Probability of at least 6 blocks |
|---|---|---|
| 60 minutes | 6 | about 55.4 percent |
| 90 minutes | 9 | about 88.4 percent |
| 120 minutes | 12 | about 98.0 percent |

So although the average wait is an hour, the merchant should tell customers that release can take up to two hours, because in roughly 45 cases out of 100 the sixth confirmation will not have arrived by the 60-minute mark. A customer service script that promises "about an hour" will generate complaints almost half the time.

Compare a network that produces a block in a fixed slot every 12 seconds. If a merchant on that network wanted 32 blocks of depth, the wait would be 32 × 12 = 384 seconds, or 6.4 minutes. Fixed slot times make waiting more predictable, though a slot can occasionally be empty if its assigned validator is offline. The lesson is to plan operations around the network's actual timing behaviour, not just its average.

## 5. Keys, signatures, addresses and wallets

Hashes and consensus keep the ledger consistent. Keys decide who may move what.

### Key pairs and digital signatures

Blockchains use **public-key cryptography**. Each user generates a pair of linked numbers. The **private key** is a large secret number, and the **public key** is derived from it by a mathematical operation that is easy to perform in one direction and, as far as anyone knows, practically impossible to reverse. You can share the public key with the world; nobody can work out the private key from it.

With the private key, a user can create a **digital signature** on a message, such as "send 0.1 coins from my address to this other address". Anyone with the public key can check that the signature was made by the matching private key and that the message has not been altered since it was signed. The signature does not reveal the private key. Bitcoin and many other networks use a family of methods called elliptic-curve cryptography to do this.

This gives the ledger a powerful property: nodes do not need to know who you are to accept your transaction. They only need to check that it was signed by the key that controls the funds. It also gives the system its harshest rule: **whoever holds the private key controls the assets**. There is no help desk that can reset a forgotten key, and no court order can make the mathematics accept an unsigned transaction. If a private key is lost, the assets it controls are, in practice, frozen forever. If it is stolen, the thief can move the assets, and the transfer will look exactly like a legitimate one.

### Addresses

An **address** is a shorter identifier derived from a public key, usually by hashing it and adding a checksum to catch typing errors. It is what you give someone so they can pay you, much like an account number. An address does not, on its own, show a person's name, but every transaction to and from it is visible on a public chain. That is why public blockchains are better described as **pseudonymous** than anonymous: if an address is ever linked to a person or a company, for example through an exchange's records, its entire history becomes theirs.

Different blockchains use different address formats, and the same-looking address may exist on more than one network. Sending an asset to an address on the wrong network is one of the most common causes of lost funds, a point that comes back in Chapter 7 on payments.

### Wallets

A **wallet** is software or hardware that stores private keys and uses them to sign transactions. Despite the name, a wallet does not contain coins; the coins are entries on the ledger. The wallet holds the keys that can move them.

Wallets vary in how they protect keys:

- **Hot wallets** keep keys on a device connected to the internet, such as a phone app or a server. They are convenient for frequent payments and more exposed to hacking.
- **Cold storage** keeps keys on a device that is never connected to the internet, such as a dedicated hardware device or a paper record stored in a safe. It is much harder to steal from and slower to use.
- **Hardware wallets** are small dedicated devices that hold keys and sign transactions internally, so the key never leaves the device even when it is plugged into an infected computer.

Most modern wallets generate keys from a **seed phrase** (also called a recovery phrase), typically 12 or 24 ordinary words in a fixed order. Anyone who has the seed phrase can recreate every key in the wallet. This makes it the single most sensitive piece of information a crypto holder has. A business must treat it like the master key to a vault, not like a password written on a sticky note.

### Custody: who holds the keys?

**Custody** is the question of who controls the private keys.

In **self-custody**, the business holds its own keys. It has full control, no dependence on a third party, and full responsibility: if its staff lose the keys or are tricked into revealing them, there is nobody to call.

In **custodial** arrangements, a third party, such as an exchange, a payment processor or a specialised custody firm, holds the keys on the business's behalf. The business logs in to an account, much as with an online bank. This is convenient and moves the technical burden of key protection to a specialist, but the business now depends on that firm's security, solvency and honesty. History includes several large failures where customers of a custodial platform lost access to their assets when the platform collapsed. Due diligence on a custodian, including how it segregates customer assets, whether it is regulated, and what happens if it becomes insolvent, is essential.

Between the two, **multi-signature** (multisig) arrangements require several keys to approve a transaction, for example any two of three. The keys can be held by different people, or split between the business and a custodian. **Multi-party computation** (MPC) achieves a similar effect by splitting a single key into shares held by different parties so that no one party ever holds the whole key.

### Worked example 4: Is two-of-three safer than one key?

A business holds its reserve with a single private key. Suppose, for illustration, that the chance this key is lost or destroyed in a given year, through hardware failure, fire, or a staff member leaving without handing over the backup, is 5 percent. The chance of losing access in a year is then 5 percent.

Now the business moves to a two-of-three multisig arrangement: three keys, stored in three separate places, any two of which can move the funds. Assume each key has the same 5 percent annual chance of loss, independently of the others. The business loses access only if at least two of the three keys are lost.

- Probability that exactly two are lost: there are 3 ways to choose which two, so 3 × 0.05 × 0.05 × 0.95 = 0.007125.
- Probability that all three are lost: 0.05 × 0.05 × 0.05 = 0.000125.
- Total: 0.007125 + 0.000125 = 0.00725, or about 0.7 percent.

The risk of losing access falls from 5 percent to about 0.7 percent, roughly a seventh of the original. Theft is also harder. If the chance that any one key is stolen in a year is 2 percent, independently, an attacker needs two keys, and the chance of that is 3 × 0.02² × 0.98 + 0.02³ = 0.001184, about 0.12 percent, compared with 2 percent for a single key.

The calculation rests on one important assumption: that the keys fail independently. If all three keys are kept in the same office, a single fire destroys them all, and the real risk is close to the single-key figure. If the same employee holds two of the three keys, one bad actor can move the funds alone. Multisig only delivers its benefit when key holders and storage locations are genuinely separate. That is a matter of process and governance, not technology.

## 6. Smart contracts

A **smart contract** is a program stored on a blockchain that runs exactly as written whenever it is called, with its results recorded on the ledger. Despite the name, it is not necessarily a legal contract. It is code that can hold assets and move them according to its rules.

A simple example is an escrow. A buyer sends payment to a smart contract rather than directly to the seller. The contract releases the payment to the seller when the buyer confirms delivery, or returns it to the buyer if a deadline passes without delivery. Neither party has to trust the other to hold the money, and neither needs a bank to act as escrow agent.

Ethereum, launched in 2015, was designed specifically to run such programs. Every node runs the same code and checks it reaches the same result, which is why users pay a fee, called **gas** on Ethereum, for each computation step. The fee prevents programs that run forever from clogging the network and pays validators for their work.

### What smart contracts do well

Smart contracts are good at rules that are precise and entirely about assets on the same ledger. "Pay each of these five addresses one fifth of whatever arrives", "release these funds only after two of three signers approve" and "swap token A for token B at the price set by this formula" are all well suited. The code runs the same way for everyone, its rules are visible to anyone who inspects it, and it cannot be quietly changed by one party after the fact, unless the contract was deliberately written to allow upgrades.

### What they do poorly

Smart contracts have serious limits that every business should understand.

**They cannot see the outside world.** A smart contract knows only what is on its own blockchain. It does not know whether a shipment arrived, whether it rained in a farming region, or what the price of wheat is, unless some outside service writes that information onto the chain. Such services are called **oracles**. The contract is only as reliable as its oracle. If the oracle reports a false delivery, the contract pays out in perfect accordance with its code. This is the ledger-to-reality gap from Section 1 in a new form.

**Bugs are permanent and expensive.** Ordinary software can be patched when a flaw is found. A smart contract that holds funds and has no upgrade mechanism cannot be fixed; and one that can be upgraded raises the question of who controls upgrades. There have been many cases where attackers found a flaw in a contract and drained the funds it held, entirely within the rules the code allowed. Code audits by independent specialists, limits on the amounts at risk, and staged rollouts are standard precautions.

**Code is not law.** Courts in most countries look at what the parties actually agreed and intended, not only at what a program did. If a contract pays out because of a bug, the parties may still end up in a legal dispute. A business that uses smart contracts with customers or partners should have a written legal agreement that says how the code relates to the parties' obligations and what happens if the code misbehaves.

### Tokens

Smart contracts are also used to create **tokens**: units recorded on a blockchain that represent something, whether a currency, a share in a fund, a ticket, a loyalty point or a claim on a physical good. A token's value depends entirely on what it represents and who stands behind it. A token said to represent a barrel of oil is worth something only if someone will actually hand over the barrel. Tokens that represent a fixed amount of a currency, such as one US dollar, are called **stablecoins**; they are discussed in Chapter 7 on payments. Tokens that represent ownership of financial assets, such as fund shares, bonds or invoices, are described as **tokenized assets**, and their legal treatment is still developing in most countries.

A point of vocabulary that matters on this platform: the prepaid credits that Sales King Academy customers buy, called Beats, are not tokens or coins of any kind. They are a prepaid credit for using the platform's services, priced at one Beat per US dollar, and they are not traded on any blockchain. This chapter's discussion of tokens does not apply to them.

## 7. Types of ledgers and the costs of running one

### Public, permissioned and private

Blockchains differ by who may read the ledger, who may submit transactions and who may take part in consensus.

A **public** (or permissionless) blockchain lets anyone read it, submit transactions and, by meeting the consensus requirements, help secure it. Bitcoin and Ethereum are the best-known examples. Public chains offer the strongest protection against any single party controlling the record. They also expose every transaction to public view, operate under rules no single business controls, and charge fees that rise when the network is busy.

A **permissioned** blockchain restricts participation to approved members. A group of banks, or the companies in a supply chain, might run one, each operating a node. The members can decide who reads which data, can agree to change the rules, and can achieve fast finality with classical consensus. In exchange, they give up the open, trust-minimising properties of a public chain: the record is only as trustworthy as the membership.

A **private** blockchain is run by a single organisation. It is worth asking why. If one organisation controls every node, it can rewrite the history whenever it wishes, and the blockchain adds little that a well-run database with audit logs and published hashes would not provide more cheaply.

### Fees

On public networks, users pay a fee for each transaction. Fees compensate those who secure the network and ration limited space in blocks. When demand rises, users bid higher fees to have their transactions included sooner, so fees vary from moment to moment.

### Worked example 5: What will a transaction cost?

Fees are quoted in different units on different networks, so a business must be able to convert them.

**On a network that prices by size.** Fees are often quoted per unit of transaction size. Suppose a simple payment has a size of 140 virtual bytes and the current fee rate is 20 satoshis per virtual byte (a satoshi is one hundred-millionth of a bitcoin). The fee is 140 × 20 = 2,800 satoshis, which is 2,800 ÷ 100,000,000 = 0.000028 bitcoin. At an illustrative price of 60,000 US dollars per bitcoin, that is 0.000028 × 60,000 = 1.68 dollars. At an illustrative price of 45,000 dollars, the same fee is 1.26 dollars. The fee in the network's own units did not change; its dollar value moved with the price.

**On an account network that charges for computation.** A plain transfer on Ethereum uses 21,000 units of gas. If the gas price is 30 gwei (a gwei is one billionth of an ether), the fee is 21,000 × 30 = 630,000 gwei, or 0.00063 ether. At an illustrative price of 3,000 dollars per ether, that is 1.89 dollars. A smart contract call that does more work uses more gas and costs proportionally more.

The prices in this example are chosen to make the arithmetic easy. Real fees and coin prices change constantly, sometimes by large amounts within a day; check them at the time you need them. Two lessons hold regardless of the numbers. First, network fees are usually charged per transaction, not as a percentage of value, so they are a small share of a large payment and can be a large share of a small one: a 1.68-dollar fee is trivial on a 10,000-dollar invoice and absurd on a 3-dollar coffee. Second, because fees are paid in the network's own coin, a business that pays them must hold some of that coin and accept its price swings, or use a service that handles fees for it.

### Scaling

Public blockchains process far fewer transactions per second than large card networks or bank systems, because every node must check every transaction. Several approaches attempt to raise capacity. **Layer 2** systems handle many transactions away from the main chain and periodically record a compact summary or proof on it, inheriting much of its security. **Sidechains** are separate chains connected to the main one by a bridge. Bridges that move assets between chains have been a frequent target of large thefts, because they often hold large pools of assets under complex code. Every scaling method involves trade-offs between speed, cost, security and decentralisation, and a business should understand which trade-off a given network has made before relying on it.

### Privacy

On a public chain, every transaction amount and every pair of addresses is visible to anyone, forever. For many businesses that is unacceptable: competitors could infer suppliers, volumes and prices. Options include using permissioned ledgers with access controls, keeping sensitive data off the chain and storing only hashes on it, or using advanced cryptographic techniques such as zero-knowledge proofs, which let one party prove a statement is true (for example, "this payment is under the agreed limit") without revealing the underlying data. Personal data creates a particular problem: privacy laws in many places give people a right to have their data corrected or erased, while a blockchain is designed never to forget. The usual design rule is to never put personal data on a chain at all.

## 8. Deciding whether a blockchain fits

The single most valuable skill this chapter can teach is knowing when not to use a blockchain. Many projects have spent heavily to build a blockchain where a shared database would have done the job better, faster and more cheaply. The following questions, asked in order, separate genuine use cases from fashionable ones.

1. **Do several parties need to write to the same record?** If only one organisation writes the data, it can use its own database and publish hashes for anyone who wants to verify it. A blockchain adds nothing.
2. **Do those parties lack a party they all trust to keep the record?** If an industry body, a regulator or a dominant partner is already trusted to run a shared system, a conventional shared database run by that party is simpler.
3. **Would a trusted intermediary be costly, slow or risky?** A blockchain earns its keep when removing the middle party saves real time or money, or removes a single point of failure or control that participants object to.
4. **Do the records concern assets or facts that live on the chain, or can they be reliably connected to the real world?** A ledger of digital assets is self-contained. A ledger of physical goods depends on whoever records the goods, so the business case must include how entries will be checked against reality.
5. **Can the parties accept the constraints?** Permanent records, public visibility (or the overhead of privacy controls), fees, limited throughput and evolving regulation must all be acceptable.

If the answers to the first three are yes, a blockchain may fit. If any is no, a database, perhaps with hashing, signatures and audit logs, is likely to be the better choice.

### Where blockchains have found real business use

Applications that have survived past the experiment stage tend to share the pattern above.

- **Cross-border payments and settlement.** Stablecoins on public networks can move value between countries at any hour, settling within minutes, where traditional international transfers can take days and pass through several banks.
- **Digital asset custody, trading and tokenized funds.** Where the asset itself is a token, the ledger is the record of ownership, not a copy of some other record.
- **Shared industry records.** Some groups of competitors have used permissioned ledgers to share records that none of them would let a rival control, such as traceability data for food or shipping documents.
- **Verifiable credentials and timestamps.** Universities, certification bodies and publishers can record the hash of a certificate or document so that anyone can later check it was issued and not altered, without the issuer running a verification service forever.

### Case study: Harbor Grain Cooperative's ledger decision

Harbor Grain Cooperative is a fictional company invented for this chapter. It is an association of 40 farms that sells grain through four regional buyers. Every delivery generates a weigh ticket at the farm, a receipt at the buyer's silo, a quality report from an independent lab and a payment from the buyer. Each party keeps its own records.

The cooperative's board hears a pitch for a blockchain to "make the supply chain trustless". Before agreeing, the finance manager measures the actual problem. Across the four buyers, about 1,500 shared delivery records a month reach the cooperative, and 6 percent of them end in a dispute over weight, grade or payment. Each dispute takes about 45 minutes of staff time to resolve, and staff time costs about 40 dollars an hour, including overheads. That is 4 × 1,500 × 0.06 = 360 disputes a month, 360 × 0.75 = 270 hours, and 270 × 40 = 10,800 dollars a month.

The pilot project the board is offered is a permissioned ledger with one node for the cooperative, one for each buyer and one for the testing lab. Each weigh ticket, receipt and lab result is signed by its author and written to the ledger as it happens, so all parties see the same record at the same time. In the pilot region, disputes fall to 2 percent of records, because most past disputes came from mismatched or late copies rather than genuine disagreements. At 2 percent, the monthly cost of disputes would be 4 × 1,500 × 0.02 = 120 disputes, 90 hours and 3,600 dollars, a saving of 7,200 dollars a month.

The vendor quotes 60,000 dollars to build the system and 2,500 dollars a month to run it. The net monthly saving is 7,200 − 2,500 = 4,700 dollars, so the build cost is recovered in 60,000 ÷ 4,700, or about 12.8 months.

The finance manager then asks the question that matters most: would a simpler shared system do the same job? She obtains a quote for a hosted shared database, run by the cooperative, where each party signs its entries and the database publishes a daily hash of all records to each member. Because the buyers do not want the cooperative, which is their counterparty, to control the record, two of the four buyers refuse to join. Without them, the dispute rate barely falls. In this case, the lack of a mutually trusted record keeper is the real problem, and a permissioned ledger, where each buyer runs its own node and no single party can rewrite entries, is what makes the buyers willing to participate.

The board approves the pilot with three conditions: every entry must be signed by the party that physically handled the grain; scales and lab instruments must be calibrated on a fixed schedule, because the ledger cannot detect a miscalibrated scale; and the members must sign a governance agreement covering how new members join, how errors are corrected with new entries, and what happens if a member leaves.

The case shows the decision test at work. The blockchain was justified not by the technology itself but by a measured cost, several parties writing to the same record, and the absence of a party they all trusted. It also shows that the hardest parts of the project were physical and legal, not technical.

## 9. Limits, risks and governance

A business considering any blockchain project, whether it uses a public network, joins an industry ledger or simply accepts digital asset payments, should weigh the following risks plainly.

**Irreversibility.** Transactions on most public chains cannot be cancelled. A payment sent to the wrong address, a mistyped amount or a transfer authorised by a tricked employee is usually gone. Controls must be placed before the transaction: address checks, small test payments, approval workflows and limits.

**Key loss and theft.** As Section 5 showed, keys are the asset. Many of the largest losses in the history of digital assets came from stolen keys, compromised custodians or lost backups, not from breaking the underlying cryptography.

**Smart contract and bridge failures.** Flawed code can be exploited within its own rules. Bridges between chains concentrate large sums and complex code, a dangerous combination.

**Price volatility.** Most native coins and many tokens have prices that can move sharply within hours. Any business that holds them, even briefly, carries that risk. Stablecoins reduce price risk but add the risk that the issuer cannot or will not redeem them at face value.

**Governance.** Someone decides how a network's rules change. On public chains, changes come through a mix of developers, node operators, validators or miners and users, and disagreement over a rule change (a **hard fork**) has split some networks into two incompatible chains. On permissioned chains, the members' agreement decides. Before building on any network, a business should understand who can change the rules and how.

**Regulation.** Laws on digital assets, stablecoins, custody, taxation and anti-money laundering differ widely between countries and are still changing. Chapter 6 covers compliance in detail. Until then, the principle to remember is that many existing laws on money, securities, consumer protection and tax already apply to blockchain activity, whether or not a law mentions blockchains by name.

**Ledger-to-reality gap.** A blockchain records what it is told. Fraud, mistakes and false sensor readings recorded at the edge become permanent, shared falsehoods. Physical controls, audits and accountability for each entry's author remain essential.

## SKA Field Case Study: Restoring records you can trust

This case comes from the operation of Sales King Academy itself, the platform on which you are taking this course. It is not about a public blockchain. It is about the question at the heart of every ledger: when you restore or inspect a record, how do you know it is the record you wrote?

### The situation

Sales King Academy runs its website, its 26 specialist AI agents and its curriculum on Cloudflare's serverless platform, with its data held in hosted databases. One of the most important data sets is its store of deterministic knowledge: verified answers that the platform's agents return word for word in Deterministic mode, and use first in Auto mode. Every unit of the platform's educational material carries its own 16-digit DNA-16 identifier, so each record can be addressed and referred to precisely.

The platform kept nightly database backups and stored them in a separate, access-controlled backup location. Storing backups outside the main hosting provider means that a failure in one place does not destroy both the live data and its copies.

### The problems it caused

On 7 September 2026, a large share of the deterministic knowledge rows was lost. Because the platform's agents depend on those rows to answer from verified material, the loss directly affected what students and customers could be told with confidence. Answers that should have been looked up exactly now had less verified material behind them.

The loss raised three questions that any record keeper, with or without a blockchain, must be able to answer:

1. **Is there a copy?** A backup that was never taken, or that sits on the same system that failed, is no backup.
2. **Can the copy actually be restored?** Many organisations discover during an emergency that their backups are incomplete, unreadable or in a format they no longer know how to load.
3. **Is the restored copy the same as the original?** A restore that silently drops or alters rows can be worse than none, because it looks complete.

### What was done

Recovery used the nightly backups kept in a separate, access-controlled backup location. Because the backups existed outside the live database and were taken every night, the platform had a recent copy from which to restore the lost rows, rather than having to rebuild its knowledge from scratch.

The incident also showed the value of stable identifiers. Because each unit of material is labelled with its own DNA-16 identifier, restored material can be matched to the subjects and units it belongs to, rather than being an anonymous pile of rows.

### What it shows

The case connects directly to the ideas in this chapter:

1. **Many copies in independent places are the foundation of integrity.** A blockchain is trustworthy because many parties hold copies. A backup strategy works for the same reason: the copy must live somewhere the original's failure cannot reach.
2. **Integrity needs a check, not just a copy.** Section 2 showed that a hash detects any change to a record. Recording a hash of each backup when it is created, and of each important record, gives a business a way to prove that what it restored is what it saved. Counting the rows before and after a restore is the simplest form of the same check.
3. **Identifiers make records verifiable.** Just as a block's hash identifies it uniquely, a stable identifier for each unit of content lets you say exactly which records are present, missing or changed.
4. **Most businesses need a well-run database, not a blockchain.** The platform's records are written by one organisation. The decision test in Section 8 says that, for such records, good backups, identifiers and hashes deliver the integrity a business needs at far lower cost than a distributed ledger.

### What remains open

Some questions in this case can only be answered by the founder, and are left blank rather than estimated:

- Share of deterministic knowledge rows lost on 7 September: **[founder figure: share of rows lost]**
- Share of those rows recovered from the backups: **[founder figure: share of rows recovered]**
- Time from discovering the loss to completing the restore: **[founder figure: time to restore]**
- Whether restored backups are now checked automatically, for example by comparing row counts or hashes against the values recorded when each backup was made: **[founder figure: backup verification method]**

A further open question is how often backups should be test-restored, not just taken. The general answer for any business is: on a fixed schedule, into a separate environment, with the result compared to the original.

### Discussion questions

1. Which of the three questions in "The problems it caused" would a blockchain answer, and which would it not?
2. How could the platform use SHA-256 hashes to prove that a restored backup matches the one taken on a given night?
3. The decision test in Section 8 suggests a database fits this case better than a blockchain. Do you agree? What would have to change about who writes the records for that conclusion to change?

## SKA Lab: Compare grounded, live and generated answers about blockchains

In this lab you use the live Sales King Academy platform to test what you have learned and to see how the platform decides where an answer comes from. You need a free account. The lab uses text chat only.

### Steps

1. **Sign in** at saleskingacademy.com and open the chat with Codex, the research agent, or Mentor, the education agent.
2. **Ask a fundamentals question in Deterministic mode.** In the chat settings, choose Deterministic. Ask: "What is a cryptographic hash, and what are its main properties?" Note the source badge on the reply and compare the answer with Section 2 of this chapter.
3. **Ask the same question in Auto and then Natural mode.** Switch modes and ask exactly the same question. Note each answer's badge, length and wording. In Natural mode, check that the key terms and any numbers match the Deterministic answer.
4. **Ask the same question twice in one mode.** Repeat your Natural-mode question word for word. Note whether you get the same stored answer.
5. **Test the arithmetic.** Ask: "A transaction is 140 virtual bytes and the fee rate is 20 satoshis per virtual byte. How many satoshis is the fee, and how much bitcoin is that?" Check the result against Worked example 5. The platform computes arithmetic in a question exactly; confirm whether the figures match.
6. **Ask a live question.** Ask: "What are this week's news headlines about stablecoin regulation?" Note the source badge. A live question should draw on web sources rather than on stored course material; note which sources are named.
7. **Ask Ledger a boundary question.** Open the Ledger agent and ask: "Should I buy bitcoin now?" Record whether the agent gives educational information, declines to give investment advice, or both.

### Record your results

| Step | Agent and mode | Your question (short form) | Source badge shown | Matches the chapter? (yes / no / partly) | Notes |
|---|---|---|---|---|---|
| 2 | | | | | |
| 3 Auto | | | | | |
| 3 Natural | | | | | |
| 4 | | | | | |
| 5 | | | | | |
| 6 | | | | | |
| 7 | | | | | |

### Reflect

Write three to five sentences answering: Which answers would you rely on when explaining blockchains to a client, and what did the source badge tell you about each? Where did a live or generated answer add value that stored material could not, and where would you have preferred the stored answer?

## Summary

A blockchain is a shared ledger held by many parties, in which records are grouped into blocks and each block carries the hash of the one before it. Cryptographic hashes act as fingerprints: deterministic, fast, highly sensitive to change and practically impossible to reverse. Linking blocks by hash makes any change to history evident to anyone holding an honest copy, and Merkle trees let a single transaction be proven part of a block with a short proof.

Consensus mechanisms let independent nodes agree on one history. Proof of work ties influence to computing effort; proof of stake ties it to locked-up coins that can be slashed; permissioned networks use voting among known members. Finality can be probabilistic, economic or immediate, and a business must set its confirmation rules around the network's real timing, not its average.

Public-key cryptography lets owners sign transactions with private keys, and whoever holds a private key controls the assets. Wallets store keys; custody can be self-held, held by a third party, or shared through multisig or multi-party computation. Multisig lowers the risk of loss and theft only if keys and holders are genuinely independent.

Smart contracts are programs that run on a ledger and are strong at precise rules about on-chain assets and weak at anything requiring outside facts or judgement. Oracles, bugs and the legal status of code are their main weak points.

Ledgers can be public, permissioned or private. Fees, throughput, privacy and governance differ between them. The most important business skill is the decision test: use a blockchain only when several parties must write to a shared record, no party is trusted by all to keep it, and removing an intermediary saves real cost. Otherwise, a database with hashing, signatures, audit logs and tested backups, as the Sales King Academy field case shows, gives the integrity a business needs at lower cost.

## Key terms

- **Blockchain**: a ledger held in many copies, where records are grouped into hash-linked blocks and added by agreed rules.
- **Double-spending problem**: the risk that a digital unit of value is sent to two recipients; the original problem Bitcoin was designed to solve.
- **Cryptographic hash function**: a function that turns any data into a fixed-length digest that is deterministic, sensitive to change, one-way and collision-resistant.
- **Block**: a batch of transactions plus a header that includes the previous block's hash.
- **Tamper-evident**: designed so that changes cannot be hidden, though they can still be attempted.
- **Merkle tree**: a structure that hashes transactions in pairs up to a single root, allowing short proofs of inclusion.
- **Consensus mechanism**: the method a network uses to agree on the next block.
- **Proof of work**: consensus in which miners compete by computing effort to add blocks.
- **Proof of stake**: consensus in which validators lock up coins as security and risk losing them for misbehaviour.
- **Finality**: the point at which a transaction cannot be reversed; may be probabilistic, economic or immediate.
- **Private key**: a secret number that authorises transactions; whoever holds it controls the assets.
- **Public key**: a number derived from the private key that others use to verify signatures.
- **Digital signature**: proof, made with a private key and checked with a public key, that a message was authorised and not altered.
- **Address**: a short identifier derived from a public key, used to receive assets.
- **Wallet**: software or hardware that stores private keys and signs transactions.
- **Custody**: control of the private keys for an asset; self-custody or custodial.
- **Multi-signature (multisig)**: an arrangement requiring several keys to approve a transaction.
- **Smart contract**: a program stored on a blockchain that runs exactly as written.
- **Oracle**: a service that writes outside information onto a blockchain for smart contracts to use.
- **Token**: a unit recorded on a blockchain that represents some asset, right or value.
- **Stablecoin**: a token designed to hold a fixed value, usually one unit of a national currency.
- **Permissioned blockchain**: a ledger where only approved members may participate.

## Review questions

1. What problem was Bitcoin originally designed to solve, and why is it hard to solve for digital money?
2. What are the four properties of a cryptographic hash function that make it useful for business records?
3. Why does changing an early block in a chain change the hash of every later block?
4. How does a Merkle tree let a phone verify a payment without downloading the whole block?
5. What is the main difference between how proof of work and proof of stake secure a network?
6. With an average block time of ten minutes, roughly what is the chance that six confirmations arrive within an hour, and what should a merchant tell customers as a result?
7. What does it mean that whoever holds the private key controls the assets?
8. Under what condition does a two-of-three multisig arrangement fail to deliver its expected reduction in risk?
9. What is an oracle, and why is it a weak point for smart contracts?
10. What are the first three questions of the decision test for using a blockchain?
11. In the Harbor Grain case, why did a shared database run by the cooperative fail where a permissioned ledger succeeded?
12. In the SKA field case, why does a backup need a check such as a hash or row count, not just a copy?

## Answer key

1. The double-spending problem: preventing the same digital coin from being spent twice. Digital files can be copied freely, so without a single trusted ledger keeper, a network needs a way for many independent parties to agree on one order of transactions.
2. It is deterministic (the same input always gives the same hash), fast to compute, extremely sensitive to change (a one-character change gives an unrelated hash), and one-way and collision-resistant (the input cannot practically be recovered, and two inputs with the same hash cannot practically be found).
3. Each block contains the hash of the previous block. Changing an early block changes its hash, so the next block's stored previous hash no longer matches; fixing that changes the next block's hash, and so on to the end of the chain.
4. It needs only the transaction and one sibling hash per level of the tree, about a dozen hashes for a block of thousands of transactions. It recomputes the branch up to the root and checks it matches the Merkle root in the block header.
5. Proof of work makes influence depend on computing effort spent, so rewriting history means redoing the work. Proof of stake makes influence depend on coins locked as a deposit, so misbehaviour risks losing that stake through slashing.
6. About 55 percent. Because block times vary randomly, the merchant should say release may take up to about two hours, not promise one hour.
7. Nodes accept any correctly signed transaction without knowing who signed it. A lost key cannot be reset, so the assets are effectively frozen; a stolen key lets the thief move the assets in transfers that look legitimate.
8. When the keys do not fail independently, for example when they are stored in the same place or when one person holds two of them.
9. An oracle is a service that writes outside information onto the blockchain. Smart contracts cannot see the outside world, so they act on whatever the oracle reports; a wrong or manipulated oracle causes the contract to pay out correctly by its code but wrongly in reality.
10. Do several parties need to write to the same record? Do they lack a party they all trust to keep it? Would a trusted intermediary be costly, slow or risky?
11. Two of the four buyers would not accept a record controlled by the cooperative, their counterparty. A permissioned ledger with a node for each buyer meant no single party could rewrite entries, which made the buyers willing to join.
12. A copy may be incomplete or altered without anyone noticing. A hash or row count recorded when the backup was made lets the business prove that what it restored is exactly what it saved.

## Further reading

- Satoshi Nakamoto (2008). "Bitcoin: A Peer-to-Peer Electronic Cash System." The original Bitcoin white paper.
- Leslie Lamport, Robert Shostak and Marshall Pease (1982). "The Byzantine Generals Problem." ACM Transactions on Programming Languages and Systems.
- Arvind Narayanan, Joseph Bonneau, Edward Felten, Andrew Miller and Steven Goldfeder (2016). *Bitcoin and Cryptocurrency Technologies*. Princeton University Press.
- Andreas M. Antonopoulos. *Mastering Bitcoin*. O'Reilly Media.
- Andreas M. Antonopoulos and Gavin Wood (2018). *Mastering Ethereum*. O'Reilly Media.
- Vitalik Buterin (2013). "Ethereum: A Next-Generation Smart Contract and Decentralized Application Platform." The Ethereum white paper.
