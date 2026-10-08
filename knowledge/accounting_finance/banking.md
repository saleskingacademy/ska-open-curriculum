---
key: banking
title: "Banking"
program: accounting_finance
course_level: 5
dna16: "0701201811515067"
l4_address: "S6:P337045466"
chain256_anchor: "0413729454767619079330196167128504847024351212850097803422906394147682001773561913779625735212850038639564121285072627025237644316051290101290690792410004961285184427910303128501847604467420601377509578170891167590813099128507730546688812850105414548060887"
updated_at: "2026-10-01T20:00:00.000Z"
license: All-Rights-Reserved (Sales King Academy LLC)
source: Sales King Academy knowledge base (ska_knowledge)
---

# Banking

> The course assumes prior knowledge of financial concepts and delves into specialized topics like credit risk assessment and capital adequacy.

## Foundations

Banking is the intermediary financial institution activity that facilitates the flow of funds between surplus and deficit units, primarily through deposit-taking and credit extension. At its core, banking operates on the principle of maturity transformation—accepting short-term liabilities (deposits) and issuing longer-term assets (loans)—while managing liquidity, credit, and interest rate risks. The fundamental balance sheet identity governs banking operations: Assets = Liabilities + Equity, where assets include loans, securities, and reserves; liabilities primarily comprise customer deposits and wholesale funding. The bank’s profitability derives from net interest margin (NIM), the spread between interest earned on assets and interest paid on liabilities, adjusted for credit losses and operational costs. Regulatory frameworks (Basel Accords, Dodd-Frank, CRD IV) impose capital adequacy, liquidity coverage ratio (LCR), and leverage ratio requirements to ensure systemic stability.

In the business context, banking refers to the financial services provided by institutions that accept deposits, facilitate transactions, and provide credit to individuals, businesses, and organizations. A **bank** is a financial institution licensed to receive deposits, make loans, and provide other financial services. The core function of a bank is to act as a **financial intermediary**, connecting borrowers and lenders, and managing risk. **Deposits** are funds placed with a bank by customers, which can be withdrawn on demand or after a specified period. **Transactions** involve the transfer of funds between accounts, which can be facilitated through various payment systems, such as checks, credit cards, and electronic funds transfers. **Credit** refers to the provision of funds by a bank to a borrower, with the expectation of repayment, typically with interest. Key banking concepts include **liquidity**, which refers to the ability to meet short-term obligations, and **solvency**, which refers to the ability to meet long-term obligations. Banking operations are regulated by **central banks**, which oversee monetary policy, and **financial regulatory bodies**, which enforce banking laws and regulations to maintain stability and protect consumers. Understanding these core definitions and principles is essential for banking practitioners to navigate the complex financial landscape.

In the business context, banking refers to the acceptance and management of deposits, provision of credit, and facilitation of financial transactions. The **banking system** comprises commercial banks, central banks, and other financial institutions that facilitate the flow of money and credit. **Commercial banks** are institutions that accept deposits, provide checking and savings accounts, and make loans to individuals and businesses. A **central bank**, also known as a reserve bank, is responsible for regulating the banking system, managing the nation's monetary policy, and maintaining financial stability. **Capital** refers to the bank's ownership equity, while **reserves** are the portions of deposits set aside to meet withdrawal demands.

## Section 1

CREDIT RISK ASSESSMENT & LOAN PRICING  
Framework: Expected Loss (EL) Model  
EL = Probability of Default (PD) × Loss Given Default (LGD) × Exposure at Default (EAD)  
- PD: Estimated via credit scoring models (e.g., logistic regression, machine learning) or external ratings (S&P, Moody’s). For example, a BBB-rated corporate bond may have a 1.5% annual PD.  
- LGD: Typically 40% for unsecured loans, lower for secured loans (e.g., 20% for mortgages).  
- EAD: The outstanding loan amount at default, including undrawn commitments.  
Loan Pricing Formula:  
Loan Rate = Risk-Free Rate + Credit Spread + Operating Cost + Profit Margin  
Credit Spread is calibrated to cover EL and unexpected loss (UL), often derived from Value at Risk (VaR) or Credit VaR at 99.9% confidence over one year. For instance, a 5-year corporate loan might have a credit spread of 150 bps over LIBOR to cover EL and capital costs.

## Section 2

LIQUIDITY MANAGEMENT & LCR  
Framework: Basel III Liquidity Coverage Ratio (LCR)  
LCR = Stock of High-Quality Liquid Assets (HQLA) / Total Net Cash Outflows over 30 days ≥ 100%  
- HQLA categories: Level 1 (e.g., cash, central bank reserves, sovereign bonds with zero haircut), Level 2A (e.g., investment-grade corporate bonds, 15% haircut), Level 2B (lower-rated bonds, 50% haircut).  
- Net Cash Outflows: Estimated by applying run-off rates to various liabilities and drawdown rates to off-balance sheet commitments. For example, retail deposits have a 5% run-off rate, while unsecured wholesale funding may have 40%.  
Banks must maintain an LCR buffer to withstand acute liquidity stress, ensuring survival through a 30-day liquidity crisis.

## Section 3

CAPITAL ADEQUACY & RWA CALCULATION  
Framework: Basel III Risk-Weighted Assets (RWA)  
RWA = Σ (Exposure_i × Risk Weight_i)  
- Credit Risk Weights: Sovereign exposures (0%), residential mortgages (35%), corporate loans (100%), unrated SMEs (85%).  
- Operational Risk: Calculated via standardized approach (15% of average annual gross income over 3 years) or advanced measurement approach (AMA).  
- Market Risk: Calculated using standardized or internal models approach (IMA), including VaR and stressed VaR.  
Minimum Capital Requirement = 8% of RWA, with additional buffers (Capital Conservation Buffer 2.5%, Countercyclical Buffer up to 2.5%).  
Example: A bank with $1bn in corporate loans (100% RW), $500m in mortgages (35% RW), and $200m in sovereign bonds (0% RW) has RWA = (1bn×1) + (500m×0.35) + (200m×0) = $1.175bn; minimum capital = $94m.

## Section 4

INTEREST RATE RISK IN BANKING BOOK (IRRBB)  
Framework: Economic Value of Equity (EVE) Sensitivity  
EVE = PV(Assets) – PV(Liabilities)  
- Duration Gap Analysis: Duration Gap = Duration(Assets) – (Liabilities/Assets) × Duration(Liabilities)  
- A positive duration gap implies EVE decreases when rates rise; a negative gap implies the opposite.  
- Banks run stress tests with parallel and non-parallel yield curve shocks (e.g., +200 bps) to estimate EVE impact.  
Regulatory limits often restrict EVE sensitivity to a maximum of 15% of Tier 1 capital.

## Section 5

PAYMENT SYSTEMS & SETTLEMENT RISK  
Framework: Real-Time Gross Settlement (RTGS)  
- RTGS systems (e.g., Fedwire, TARGET2) settle payments individually and immediately, minimizing settlement risk.  
- Liquidity management within RTGS requires intraday liquidity forecasting and collateral optimization.  
- Payment finality is legally binding, reducing systemic risk.  
- Banks use queue management algorithms and liquidity-saving mechanisms (LSM) to optimize payment flows and reduce liquidity needs.

## Section 6

BANK PERFORMANCE METRICS  
Framework: Return on Risk-Adjusted Capital (RORAC)  
RORAC = Net Income / Economic Capital  
- Economic Capital is the capital required to cover unexpected losses at a high confidence level (e.g., 99.97% over one year), estimated via internal models.  
- RORAC facilitates comparison across business lines and supports risk-based pricing and capital allocation.  
- Example: A corporate lending unit with $10m net income and $50m economic capital has RORAC = 20%.  
Other metrics: Cost-to-Income Ratio (operating expenses/net income), NIM (net interest income/earning assets), Loan-to-Deposit Ratio (loans/deposits).

## Section 7

DIGITAL BANKING & FINTECH INTEGRATION  
Framework: API-Driven Open Banking  
- Open Banking mandates banks to expose customer data securely via APIs to third-party providers (TPPs), enabling services like account aggregation, payment initiation.  
- PSD2 regulation (EU) requires Strong Customer Authentication (SCA) to reduce fraud.  
- Banks leverage cloud-native infrastructure, microservices, and AI-driven credit underwriting to increase agility and reduce costs.  
- Example: A bank using AI-based credit scoring reduces default rates by 15% and loan processing time from 7 days to 24 hours.

## Mastery Levels

L1: Understand that banks accept deposits and make loans.  
L2: Calculate simple interest spreads and basic loan pricing.  
L3: Apply expected loss formula to assess credit risk.  
L4: Compute LCR and interpret liquidity buffers.  
L5: Calculate RWA and minimum capital requirements under Basel III.  
L6: Analyze duration gap and EVE sensitivity to interest rate changes.  
L7: Design risk-adjusted performance metrics like RORAC for capital allocation.  
L8: Architect integrated digital banking platforms with real-time risk analytics and open banking APIs.

## Mechanisms

In the banking system, the mechanism of banking operations involves a series of steps that facilitate the flow of funds between depositors, borrowers, and other financial institutions. The process begins with depositors placing their funds into a bank, which then acts as an intermediary to allocate these funds to borrowers. The causal chain can be broken down as follows: 
1. Deposit mobilization: Banks collect deposits from individuals and businesses, offering interest rates and other incentives to attract funds. 
2. Credit assessment: When a borrower applies for a loan, the bank conducts a credit assessment to evaluate the borrower's creditworthiness, considering factors such as credit history, income, and collateral. 
3. Loan disbursement: If the borrower is deemed creditworthy, the bank disburses the loan, which is then used by the borrower for various purposes such as consumption, investment, or debt repayment. 
4. Interest payment: The borrower repays the loan with interest, which is a percentage of the principal amount borrowed. 
5. Profit generation: The bank earns a profit from the difference between the interest rate it pays to depositors and the interest rate it charges to borrowers, known as the net interest margin. 
6. Risk management: Throughout the process, the bank engages in risk management activities, such as monitoring credit risk, liquidity risk, and operational risk, to minimize potential losses and ensure the stability of its operations. 
This mechanism highlights the critical role banks play in channeling funds from savers to investors, facilitating economic growth and development. The process begins with deposit mobilization, where banks collect funds from customers through various deposit accounts such as checking, savings, and time deposits. These deposits are then used to fund lending activities, including loans and credit facilities to individuals and businesses. The lending process involves credit assessment, where the bank evaluates the creditworthiness of the borrower, and loan disbursement, where the funds are disbursed to the borrower. The borrower is then required to repay the loan with interest, which is a critical component of the banking mechanism as it generates revenue for the bank. The interest earned on loans is a primary source of income for banks, and it is used to pay interest on deposits, cover operational expenses, and generate profits. The banking mechanism also involves risk management, where banks mitigate potential losses by diversifying their loan portfolios, maintaining adequate capital reserves, and implementing prudent lending practices. Additionally, banks engage in liquidity management, where they ensure that they have sufficient funds to meet customer withdrawals and other liquidity needs. The overall mechanism of banking is designed to facilitate financial intermediation, where banks act as intermediaries between savers and borrowers, and provide a range of financial services that support economic growth and development.

## Methods And Frameworks

In banking, several methods and frameworks are employed to assess creditworthiness, manage risk, and optimize investment decisions. The Altman Z-Score model is used to predict the likelihood of a company's bankruptcy, with a lower score indicating higher risk. It is applicable when evaluating the creditworthiness of potential borrowers. However, its failure mode lies in its sensitivity to accounting practices and industry-specific factors. The Capital Asset Pricing Model (CAPM) is used to estimate the expected return on an investment, taking into account its beta and the risk-free rate. It is suitable for evaluating investment opportunities, but its failure mode is the assumption of a constant beta over time. The Value-at-Risk (VaR) model is used to estimate the potential loss of a portfolio over a specific time horizon, with a given probability. It is applicable for managing market risk, but its failure mode is the inability to account for extreme events. The Gordon Growth Model is used to estimate the present value of a stock, based on its expected dividend payments and growth rate. It is suitable for evaluating equity investments, but its failure mode is the assumption of a constant growth rate. The Credit Migration Model is used to estimate the likelihood of a borrower's credit rating changing over time. It is applicable for managing credit risk, but its failure mode is the reliance on historical data and the inability to account for sudden changes in market conditions. The Credit Scoring Model is used to evaluate an individual's or business's creditworthiness, typically when deciding on loan applications. The Gordon Growth Model is applied to estimate the present value of future cash flows, often used in investment analysis and valuation of stocks. The Value-at-Risk (VaR) framework is employed to measure and manage market risk, commonly used by banks to estimate potential losses. Each of these methods has its failure mode, such as the Credit Scoring Model's reliance on historical data, which may not accurately predict future creditworthiness. The Gordon Growth Model assumes constant growth rates, which may not hold true in reality. The CAPM's failure mode lies in its assumption of efficient markets, which may not always be the case. VaR's failure mode is its inability to account for extreme events, also known as black swans. Understanding these methods, their applications, and limitations is crucial for effective banking and investment decisions.

## Worked Examples

To illustrate key banking concepts, consider the following examples. 
1. Calculating Interest on a Loan: A business borrows $100,000 from a bank at an annual interest rate of 8%. If the loan is for 5 years, the total interest paid can be calculated using the formula: Total Interest = Principal * Rate * Time. Thus, Total Interest = $100,000 * 8% * 5 = $40,000.
2. Determining Bank Charges: A company maintains an average balance of $50,000 in its checking account. The bank charges a monthly maintenance fee of $25 if the average balance falls below $75,000. Additionally, the bank charges $0.15 per transaction. If the company had 500 transactions in a month, the total bank charges would be $25 (maintenance fee) + $0.15 * 500 (transaction fees) = $25 + $75 = $100.
3. Evaluating Return on Investment (ROI) for a Bank Deposit: An investor deposits $200,000 into a 2-year term deposit with an annual interest rate of 4%. The interest is compounded annually. The future value of the deposit can be calculated using the formula: FV = PV * (1 + r)^n, where PV is the present value ($200,000), r is the annual interest rate (4% or 0.04), and n is the number of years (2). Thus, FV = $200,000 * (1 + 0.04)^2 = $200,000 * 1.0816 = $216,320. The ROI is then ($216,320 - $200,000) / $200,000 = 8.16%. Since $50,000 is less than $75,000, the company will be charged $25 per month. Over a year, this amounts to $25 * 12 = $300. 
3. The interest earned each year is $200,000 * 4% = $8,000. Over 2 years, the total interest is $8,000 * 2 = $16,000. This example demonstrates how to calculate the return on a bank deposit.

## Applications

In business, banking applications are diverse and critical to the functioning of economies. Banks provide financial services to individuals, businesses, and governments, facilitating transactions, managing risk, and allocating capital. Key applications include payment systems, such as checks, credit cards, and electronic funds transfers, which enable the efficient exchange of goods and services. Cash management services, including account reconciliation and treasury management, help businesses optimize their liquidity and minimize financial risk. Lending activities, such as commercial loans and mortgages, provide capital for investment and consumption, driving economic growth. Investment banking services, including mergers and acquisitions, initial public offerings, and securities underwriting, facilitate corporate finance and strategic transactions. Additionally, banks offer risk management products, such as derivatives and foreign exchange services, to help clients mitigate financial risks. Furthermore, banks play a crucial role in providing trade finance services, including letters of credit and factoring, which facilitate international trade and commerce. Overall, banking applications are essential to the functioning of modern economies, enabling the creation, allocation, and management of financial resources.

## Common Errors

In the banking sector, practitioners often make mistakes that can have significant consequences. One common error is the failure to properly assess credit risk, leading to lending to borrowers who are unlikely to repay. This can result from inadequate due diligence, reliance on incomplete or inaccurate financial information, or insufficient consideration of external factors such as market conditions. Another mistake is the mismanagement of liquidity risk, where banks fail to maintain sufficient liquid assets to meet deposit withdrawals or other short-term obligations. This can occur due to over-reliance on wholesale funding or failure to diversify funding sources. Additionally, banks may incorrectly calculate regulatory capital requirements, leading to insufficient capital buffers and increased risk of insolvency. These errors can be attributed to inadequate training, insufficient risk management frameworks, or poor governance practices. Furthermore, the failure to implement effective anti-money laundering (AML) and know-your-customer (KYC) procedures can lead to reputational damage and regulatory penalties. These mistakes highlight the importance of robust risk management, proper training, and effective governance in the banking sector. Additionally, banks may incorrectly calculate or misapply key financial metrics, such as the capital adequacy ratio or return on equity, which can lead to poor strategic decisions. Furthermore, non-compliance with regulatory requirements, such as anti-money laundering laws or data protection regulations, can result in significant fines and reputational damage. These errors often stem from inadequate training, insufficient risk management frameworks, or a lack of effective oversight and governance. By understanding these common errors, banking practitioners can take steps to mitigate them and ensure more effective and sustainable banking operations.

## Advanced

The graduate-level extensions of banking involve a deeper exploration of risk management, financial regulation, and the impact of technological advancements on the industry. One key area of study is the application of advanced statistical models and machine learning algorithms to predict credit risk, detect fraudulent activity, and optimize portfolio management. Another area of focus is the analysis of the Basel Accords and their implications for bank capital requirements, liquidity, and risk-weighted assets. The increasing importance of fintech and digital banking also raises questions about the future of traditional banking models and the potential for disintermediation. Furthermore, the growth of sustainable finance and environmental, social, and governance (ESG) considerations is leading to new areas of research and development in banking, such as green banking and impact investing. Open questions in the field include the optimal balance between regulation and innovation, the potential consequences of a cashless society, and the role of central banks in managing monetary policy in a rapidly changing financial landscape. As the field continues to evolve, graduate-level students of banking must be equipped to analyze complex data, evaluate emerging trends, and develop innovative solutions to the challenges facing the industry.

In advanced banking studies, graduate-level students delve into complex topics such as risk management, financial regulation, and international banking. They examine the implications of Basel Accords on bank capital requirements and liquidity standards. The impact of fintech and digital banking on traditional banking models is also explored, including the role of blockchain, cryptocurrencies, and mobile payments. Open questions in the field include the optimal level of bank regulation, the effectiveness of macroprudential policies, and the potential consequences of a cashless society. Current research focuses on the applications of artificial intelligence and machine learning in credit risk assessment, portfolio management, and customer segmentation. Furthermore, the integration of environmental, social, and governance (ESG) factors into banking practices and the development of sustainable banking models are emerging areas of study. The field is moving towards a more interdisciplinary approach, incorporating insights from economics, finance, law, and technology to address the complex challenges facing the banking industry.
