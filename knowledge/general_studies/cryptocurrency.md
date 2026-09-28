---
key: cryptocurrency
title: "Cryptocurrency"
program: general_studies
course_level: 6
dna16: "0701201818479643"
l4_address: "S6:P1935839186"
chain256_anchor: "0678203222627643007186123547577315386131581757730010703746449679113669509025844705009663519157730521097233515773064532639674003709998741337914570786007785345773085304241730577314894772713160211093267281333018156345794517577310780037616657730296159988757945"
updated_at: "2026-09-07T03:25:57.737Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Cryptocurrency

> The course assumes significant prior knowledge of computer science, cryptography, and programming concepts.

## Foundations

Cryptocurrency is a decentralized digital asset designed to function as a medium of exchange, secured by cryptographic protocols and underpinned by distributed ledger technology (DLT), primarily blockchain. Unlike fiat currencies issued by sovereign states, cryptocurrencies operate without centralized intermediaries, relying on consensus algorithms to validate and record transactions. The foundational principles include immutability, pseudonymity, scarcity (often via capped supply), and programmability through smart contracts. The seminal implementation, Bitcoin (Nakamoto, 2008), introduced the Proof-of-Work (PoW) consensus mechanism and a decentralized timestamping server to prevent double-spending without trusted third parties.

In the context of economics and finance, a cryptocurrency is a digital or virtual currency that uses cryptography for security and is decentralized, meaning it is not controlled by any government or financial institution. The core definition of cryptocurrency is based on a peer-to-peer network, where transactions are recorded on a public ledger called a blockchain. A blockchain is a distributed ledger technology that allows for secure, transparent, and tamper-proof recording of transactions.

Key vocabulary includes: 
- **Token**: a digital asset issued on a blockchain, which can represent a currency, commodity, or other type of asset. 
- **Coin**: a type of token that is used as a medium of exchange, such as Bitcoin or Ethereum. 
- **Blockchain**: a decentralized, digital ledger that records transactions across a network of computers. 
- **Mining**: the process of verifying transactions and adding them to the blockchain, typically rewarded with newly minted tokens. 
- **Wallet**: a software program that allows users to store, send, and receive cryptocurrencies. 
- **Private key**: a unique code used to access and manage a user's cryptocurrency holdings. 
- **Public key**: a publicly available code that allows users to receive cryptocurrencies.

First principles of cryptocurrency include the concept of **decentralization**, where control is distributed among a network of users, rather than a central authority. Another key principle is **consensus mechanism**, which refers to the process by which transactions are verified and added to the blockchain, such as proof-of-work or proof-of-stake. Understanding these core definitions, vocabulary, and principles is essential for practitioners in the field of economics and finance to navigate the complex world of cryptocurrency.

## Section 1

CONSENSUS MECHANISMS – Proof-of-Work (PoW) vs. Proof-of-Stake (PoS)  
Framework: Consensus algorithms ensure network agreement on ledger state. PoW (Bitcoin, SHA-256 hashing) requires miners to solve computational puzzles, expending energy to find a nonce such that:  
`SHA256(SHA256(Block_Header + Nonce)) < Target`  
where Target adjusts every 2016 blocks (~2 weeks) to maintain ~10-minute block intervals. PoS (Ethereum 2.0’s Casper FFG) replaces energy expenditure with stake-weighted voting, where validators lock tokens as collateral and are randomly selected to propose/validate blocks. Slashing conditions penalize malicious behavior by forfeiting staked funds. PoS reduces energy consumption by >99% compared to PoW.

## Section 2

CRYPTOGRAPHIC PRIMITIVES – Hash Functions and Digital Signatures  
Framework: Cryptographic hash functions (SHA-256, Keccak-256) provide collision resistance and preimage resistance, enabling transaction integrity and block linking. Digital signatures (ECDSA on secp256k1 curve for Bitcoin, Ed25519 for newer chains) authenticate transaction originators. Transaction verification involves:  
1. Hashing transaction data to create a message digest.  
2. Verifying signature `S` against public key `K` and message digest `m` via elliptic curve operations.  
This ensures non-repudiation and prevents unauthorized fund transfers.

## Section 3

TOKEN ECONOMICS – Supply Models and Inflation Schedules  
Framework: Tokenomics defines scarcity and incentive alignment. Bitcoin’s supply cap is 21 million BTC, with a halving event every 210,000 blocks (~4 years) reducing block rewards from 50 BTC (2009) to 6.25 BTC (2020), enforcing a disinflationary issuance curve approximating a geometric series:  
`R_n = R_0 * (1/2)^n`  
where `R_n` is reward after n halvings. Ethereum initially had no fixed cap but transitioned to deflationary issuance post-EIP-1559, burning base fees and targeting net issuance near zero.

## Section 4

SMART CONTRACTS AND Turing-Completeness  
Framework: Smart contracts are self-executing code deployed on blockchain virtual machines (EVM for Ethereum). Contracts are written in languages like Solidity or Vyper, compiled to bytecode. Gas metering quantifies computational steps, with each opcode assigned a gas cost (e.g., ADD = 3 gas, SSTORE = 20,000 gas). Execution halts if gas is exhausted, preventing infinite loops. Formal verification tools (e.g., CertiK, MythX) analyze contract logic to mitigate vulnerabilities such as reentrancy (DAO hack, 2016).

## Section 5

LAYER 2 SCALABILITY SOLUTIONS – State Channels and Rollups  
Framework: To overcome base-layer throughput limits (~7 TPS for Bitcoin, ~15 TPS for Ethereum), Layer 2 solutions offload transactions. State channels (Lightning Network) enable off-chain micropayments by locking funds in multisignature contracts and exchanging signed transactions off-chain, settling net results on-chain. Rollups (Optimistic and ZK-Rollups) batch multiple transactions into a single proof submitted on-chain:  
- Optimistic Rollups assume correctness, with fraud proofs enabling challenge windows (~1 week).  
- ZK-Rollups generate succinct zero-knowledge proofs (SNARKs) that verify batch validity instantly.  
These increase throughput to thousands of TPS while maintaining security via on-chain data availability.

## Section 6

SECURITY MODELS – Sybil Resistance and 51% Attacks  
Framework: Sybil resistance prevents adversaries from gaining disproportionate influence by creating multiple identities. PoW achieves this via computational cost; PoS via economic stake. A 51% attack occurs if an entity controls majority hashing power or stake, enabling double-spends or censorship. Mitigation includes checkpointing (Ethereum’s Casper finality gadget), decentralized node distribution, and hybrid consensus models (e.g., Tendermint’s BFT + PoS). Attack cost estimation: For Bitcoin, controlling >50% hash rate requires investment exceeding $1 billion in ASIC hardware and electricity (as of 2024).

## Section 7

REGULATORY AND COMPLIANCE FRAMEWORKS – KYC/AML and On-Chain Analytics  
Framework: Regulatory compliance integrates Know Your Customer (KYC) and Anti-Money Laundering (AML) protocols with blockchain’s pseudonymous nature. Exchanges implement KYC via identity verification (e.g., government IDs, biometric checks). On-chain analytics firms (Chainalysis, Elliptic) utilize clustering heuristics and transaction graph analysis to identify illicit activity. Compliance frameworks increasingly incorporate Travel Rule adherence, requiring VASPs to share sender/recipient information for transfers exceeding thresholds (e.g., $1,000 USD).

## Mastery Levels

L1: Define cryptocurrency as digital money secured by cryptography and decentralized consensus.  
L2: Explain Bitcoin’s PoW puzzle and block reward halving mechanism.  
L3: Distinguish ECDSA from Ed25519 signatures and their blockchain applications.  
L4: Calculate gas costs for a typical Ethereum smart contract deployment.  
L5: Compare security trade-offs between PoW and PoS consensus algorithms.  
L6: Design a state channel protocol ensuring off-chain transaction finality.  
L7: Analyze the economic feasibility of a 51% attack on a given PoW network.  
L8: Architect a cross-chain interoperability protocol integrating Layer 2 rollups with regulatory compliance.

## Mechanisms

The cryptocurrency mechanism involves a decentralized network of computers that record transactions on a public ledger called a blockchain. The process begins with a user initiating a transaction, such as sending a certain amount of cryptocurrency to another user. This transaction is broadcast to the network of computers, known as nodes, which verify the transaction using complex algorithms. The verification process involves checking the user's digital signature, which is a unique code that confirms the user's identity, and ensuring that the user has the necessary funds to complete the transaction. Once verified, the transaction is combined with other transactions in a batch called a block. Each block is given a unique code, known as a hash, that connects it to the previous block, creating a chain of blocks, hence the term blockchain. The blockchain is maintained by a network of nodes, which continuously update and validate the ledger to ensure its integrity. The nodes are incentivized to participate in the network through a reward system, such as the release of new cryptocurrency units or transaction fees. The decentralized nature of the network allows for peer-to-peer transactions without the need for intermediaries, such as banks, and the use of advanced cryptography ensures the security and transparency of the transactions. The blockchain technology also enables the use of smart contracts, which are self-executing contracts with the terms of the agreement written directly into lines of code. This allows for automated enforcement and execution of contracts, further increasing the efficiency and security of transactions.

## Methods And Frameworks

In the context of cryptocurrency, several methods and frameworks are employed to analyze and understand market trends, risks, and potential returns. The Capital Asset Pricing Model (CAPM) is used to estimate the expected return of a cryptocurrency based on its beta, which measures its volatility relative to the overall market. The Arbitrage Pricing Theory (APT) is applied to identify mispricings in the market by analyzing the relationship between cryptocurrencies and other assets. The Efficient Market Hypothesis (EMH) is used to assess the degree to which cryptocurrency markets reflect all available information, with implications for investment strategies. The Black-Scholes model is adapted to price cryptocurrency options, taking into account the unique characteristics of these assets. The Gordon Growth Model is used to estimate the intrinsic value of a cryptocurrency, based on its expected growth rate and dividend yield. Each of these methods has its failure mode, such as CAPM's assumption of a normal distribution of returns, APT's reliance on historical data, EMH's neglect of market imperfections, Black-Scholes' oversimplification of volatility, and Gordon Growth Model's sensitivity to growth rate estimates. Understanding these limitations is crucial for applying these frameworks effectively in cryptocurrency analysis.

## Worked Examples

To illustrate key concepts in cryptocurrency, consider the following examples. 
1. **Calculating Bitcoin Volatility**: Suppose the price of Bitcoin was $40,000 on January 1 and $45,000 on January 31. To calculate the monthly return, we use the formula: ((End Value - Start Value) / Start Value) * 100. This gives ((45,000 - 40,000) / 40,000) * 100 = 12.5%. 
2. **Evaluating Mining Profitability**: A cryptocurrency miner spends $1,500 on a mining rig and $100 per month on electricity. If they mine 0.1 Bitcoins per month and the price of Bitcoin is $50,000, their monthly revenue is 0.1 * $50,000 = $5,000. Their monthly profit is $5,000 - $100 = $4,900. 
3. **Assessing Investment Risk**: An investor buys $10,000 worth of Ethereum at $3,000 per unit, receiving 3.33 units. If the price falls to $2,500, the new value of their investment is 3.33 * $2,500 = $8,325, representing a loss of $1,675 or 16.75%. This example demonstrates how price volatility can impact investment value.

## Applications

In economics and finance, cryptocurrencies have several practical applications. One of the primary uses is as a medium of exchange for online transactions, allowing for peer-to-peer transfers without the need for intermediaries like banks. This is particularly useful for cross-border transactions, as it eliminates the need for currency conversion and reduces transaction fees. Cryptocurrencies like Bitcoin are also used as a store of value, with some investors viewing them as a hedge against inflation or market volatility. Additionally, cryptocurrencies are used in decentralized finance (DeFi) applications, such as lending, borrowing, and trading, which operate on blockchain technology and smart contracts. The use of cryptocurrencies also enables micropayments, which are small transactions that are not feasible with traditional payment systems due to high transaction fees. Furthermore, cryptocurrencies are used in initial coin offerings (ICOs), which allow startups to raise capital by issuing their own digital tokens. The applications of cryptocurrencies are expanding into various industries, including supply chain management, where they can be used to track the movement of goods and verify authenticity. Overall, the use of cryptocurrencies in practice is driven by their potential to increase efficiency, reduce costs, and provide greater financial inclusion.

## Common Errors

In the context of economics and finance, practitioners often make mistakes when dealing with cryptocurrencies. One common error is treating cryptocurrencies as traditional fiat currencies, ignoring their unique characteristics such as decentralization, limited supply, and the lack of a central authority. This oversight can lead to incorrect assumptions about their value, volatility, and potential correlations with other assets. Another mistake is failing to account for the differences between various cryptocurrencies, such as their distinct consensus mechanisms, block sizes, and use cases. For instance, Bitcoin and Ethereum have different underlying technologies and purposes, which affect their market behavior and investment potential. Additionally, some practitioners incorrectly assume that the price of a cryptocurrency is solely determined by its supply and demand, neglecting the impact of external factors like regulatory changes, security concerns, and global economic trends. Furthermore, the lack of understanding of the concept of market capitalization and its implications for cryptocurrency valuation can also lead to errors in investment decisions. It is essential for practitioners to recognize these mistakes and develop a nuanced understanding of the economics and finance of cryptocurrencies to make informed decisions.

## Advanced

In the realm of economics finance, advanced studies on cryptocurrency delve into the intricacies of its impact on traditional financial systems, monetary policy, and the global economy. Graduate-level research explores the implications of cryptocurrency on the effectiveness of monetary policy tools, such as interest rates and quantitative easing. The concept of decentralized finance (DeFi) and its potential to disrupt traditional financial intermediaries is also a key area of study. Open questions in the field include the optimal regulatory framework for cryptocurrencies, the potential for central bank-issued digital currencies, and the impact of cryptocurrency on financial inclusion and stability. Furthermore, the integration of blockchain technology with other emerging technologies, such as artificial intelligence and the Internet of Things (IoT), is expected to shape the future of cryptocurrency and its applications in finance. Researchers are also investigating the use of cryptocurrency in cross-border payments, supply chain finance, and other areas where traditional financial systems are inefficient. The field is moving towards a deeper understanding of the economic and financial implications of cryptocurrency, with a focus on developing new theoretical models and empirical methods to analyze its impact on the global economy.
