---
key: devops
title: "Devops"
program: computer_science
course_level: 3
dna16: "0701201818790554"
l4_address: "S6:P1335150979"
chain256_anchor: "1340475039756989068498338554583417117810473458341738959502205129096541298508692302167107079558340125980161055834064472109249404911410939994032600695158775075834078789730912583409747924368200051038381304773746000381784169583405932541769758341030014627945574"
updated_at: "2026-09-07T12:07:58.341Z"
license: CC-BY-SA-4.0
source: Sales King Academy knowledge base (ska_knowledge)
---

# Devops

> The course applies DevOps principles to real situations and methods, assuming foundational knowledge of software development and IT operations.

## Foundations

DevOps is a multidisciplinary paradigm integrating software development (Dev) and IT operations (Ops) to accelerate delivery, improve quality, and enhance reliability through automation, collaboration, and continuous feedback. Rooted in Lean manufacturing and Agile methodologies, DevOps dismantles traditional silos by unifying development, QA, and operations teams under shared goals and metrics. Its first principles include continuous integration, continuous delivery/deployment (CI/CD), infrastructure as code (IaC), monitoring and observability, and a culture of shared responsibility. The objective is to enable rapid, repeatable, and reliable software releases while minimizing risk and maximizing customer value. DevOps is not a toolset but a systemic transformation encompassing people, processes, and technology.

In the context of computer science, DevOps refers to a set of practices that combines software development (Dev) and IT operations (Ops) to improve the speed, quality, and reliability of software releases and deployments. **Software development** encompasses the processes of designing, coding, testing, and maintaining software systems. **IT operations**, on the other hand, involves the management of the infrastructure, networks, and systems that support software applications. The core principle of DevOps is to bridge the gap between these two traditionally separate disciplines by fostering a culture of collaboration, automation, and continuous improvement. Key vocabulary includes **continuous integration** (the practice of frequently integrating code changes into a central repository), **continuous delivery** (the ability to rapidly and reliably release software changes to production), and **continuous monitoring** (the ongoing process of tracking and analyzing system performance and user feedback). Other essential terms include **agile development** (an iterative and incremental approach to software development), **infrastructure as code** (the practice of managing infrastructure through code and version control systems), and **version control systems** (tools such as Git that manage changes to code, documents, or other digital content). Understanding these concepts and their interrelationships is crucial for a DevOps practitioner to design, implement, and maintain efficient and reliable software systems.

## Section

CONTINUOUS INTEGRATION (CI)  
Framework: The CI pipeline, as popularized by Jez Humble and David Farley in *Continuous Delivery* (2010), mandates that developers integrate code into a shared repository multiple times daily. Each commit triggers an automated build and test cycle. Key tools include Jenkins, Travis CI, GitLab CI, and CircleCI.  
Specifics:  
- Commit frequency: ≥5 times per developer per day  
- Build duration target: ≤10 minutes to maintain rapid feedback  
- Test coverage threshold: ≥80% automated unit and integration tests  
- Gate criteria: All tests must pass before merge; static code analysis (e.g., SonarQube) enforces quality gates  
- Artifact versioning: Semantic Versioning (SemVer) 2.0.0 for traceability  
Steps: Commit → Automated build → Automated tests → Static analysis → Artifact creation → Feedback to developer

CONTINUOUS DELIVERY & DEPLOYMENT (CD)  
Framework: The CD pipeline extends CI by automating release to staging and production environments. Jez Humble’s CD maturity model defines stages from manual deployment to fully automated, zero-downtime deployments.  
Specifics:  
- Deployment frequency: High-performing teams deploy 208 times/year (DORA 2021)  
- Lead time for changes: <1 day from commit to production  
- Deployment automation tools: Spinnaker, ArgoCD, Octopus Deploy  
- Deployment strategies: Blue-Green, Canary Releases, Feature Toggles (LaunchDarkly)  
- Rollback mechanisms: Automated rollback within 5 minutes upon failure detection  
Steps: Build artifact → Deploy to staging → Automated acceptance tests → Deploy to production → Monitor → Rollback if needed

INFRASTRUCTURE AS CODE (IaC)  
Framework: IaC codifies infrastructure provisioning and configuration management, enabling version-controlled, repeatable environments. Tools include Terraform (HashiCorp Configuration Language), AWS CloudFormation, Ansible, Puppet, and Chef.  
Specifics:  
- Desired State Configuration: Declarative syntax specifying target infrastructure  
- Idempotency: Reapplying code yields consistent environment without drift  
- Modularization: Reusable modules for VPCs, subnets, security groups  
- State management: Remote state backends (e.g., S3 with DynamoDB locking)  
- Testing: Unit tests with Terratest; policy-as-code with Open Policy Agent (OPA)  
Steps: Write IaC → Validate syntax → Plan changes → Apply changes → Verify state → Commit to VCS

MONITORING & OBSERVABILITY  
Framework: Observability, per Charity Majors, is the ability to infer internal system states from external outputs. It encompasses metrics, logs, and traces (the “three pillars”). Tools: Prometheus (metrics), ELK Stack (logs), Jaeger/Zipkin (traces).  
Specifics:  
- SLOs/SLA definition: e.g., 99.9% uptime monthly (43.2 min downtime)  
- Alerting thresholds: Error rate >1% for 5 minutes triggers PagerDuty alerts  
- Distributed tracing: Trace requests across microservices with <1ms overhead  
- Metrics retention: 15 months for trend analysis (Prometheus TSDB)  
- Dashboarding: Grafana with real-time visualizations, anomaly detection  
Steps: Instrument code → Collect telemetry → Store and query → Alert → Analyze → Remediate

CULTURE & COLLABORATION  
Framework: DevOps culture is grounded in Westrum’s organizational typologies and the CALMS model (Culture, Automation, Lean, Measurement, Sharing). Key practices include blameless postmortems, cross-functional teams, and continuous learning.  
Specifics:  
- Team structure: Small, cross-functional teams of 7±2 members  
- Communication cadence: Daily standups, biweekly retrospectives  
- Postmortem process: Document incident within 24h; share learnings publicly  
- Psychological safety: Measured via surveys (e.g., Google’s Project Aristotle)  
- Knowledge sharing: Internal wikis, brown bag sessions, and communities of practice  
Steps: Establish shared goals → Implement feedback loops → Foster transparency → Enable autonomy → Reward collaboration

SECURITY INTEGRATION (DevSecOps)  
Framework: Embedding security into DevOps pipelines ensures compliance and reduces vulnerabilities early. The DevSecOps model integrates automated security testing and policy enforcement into CI/CD.  
Specifics:  
- Static Application Security Testing (SAST): Tools like SonarQube, Checkmarx run on every commit  
- Dynamic Application Security Testing (DAST): OWASP ZAP scans pre-production environments  
- Dependency scanning: Snyk or Dependabot to detect vulnerable libraries  
- Secrets management: Vault (HashiCorp) or AWS Secrets Manager with rotation policies  
- Compliance as code: CIS benchmarks automated checks during provisioning  
Steps: Integrate security tools → Automate scans → Fail builds on critical issues → Remediate → Audit and report

SCALABILITY & RESILIENCE ENGINEERING  
Framework: Applying principles from Site Reliability Engineering (SRE) by Google, DevOps teams engineer systems for fault tolerance and scalability. Key metrics include error budgets and capacity planning.  
Specifics:  
- Error budget: 0.1% downtime/month allows for controlled risk-taking  
- Load testing: Use tools like Locust or JMeter to simulate 10x peak traffic  
- Chaos engineering: Netflix’s Chaos Monkey to induce failures and validate recovery  
- Auto-scaling: Kubernetes Horizontal Pod Autoscaler with CPU utilization target 60-70%  
- Recovery time objective (RTO): <5 minutes; Recovery point objective (RPO): <1 minute  
Steps: Define SLOs → Measure SLIs → Allocate error budgets → Conduct failure injection → Optimize system design

## Mastery Levels

L1: Understand DevOps as bridging development and operations for faster releases.  
L2: Implement basic CI pipelines with automated builds and tests.  
L3: Deploy applications using automated CD pipelines with rollback capabilities.  
L4: Manage infrastructure declaratively via Terraform or CloudFormation.  
L5: Instrument systems for observability using Prometheus and distributed tracing.  
L6: Foster a blameless culture and implement continuous feedback loops.  
L7: Integrate security testing into CI/CD pipelines, achieving DevSecOps maturity.  
L8: Architect resilient, scalable systems with SRE principles and chaos engineering at scale.

## Mechanisms

In the context of DevOps, several key mechanisms facilitate the integration of development and operations teams, enabling the rapid and reliable delivery of software systems. The mechanism begins with **Version Control Systems (VCS)**, such as Git, which track changes to code, allowing multiple developers to collaborate and maintain a record of updates. This leads to **Continuous Integration (CI)**, where automated tools, like Jenkins, compile and test code changes, ensuring that the software remains stable and functional. Upon successful integration, **Continuous Deployment (CD)** mechanisms, such as Docker, package the software into deployable artifacts, which are then released to production environments through **Automated Deployment Scripts**. These scripts, often written in languages like Python or Ruby, utilize **Infrastructure as Code (IaC)** tools, such as Ansible or Terraform, to manage and provision the underlying infrastructure, ensuring consistency and reproducibility. The **Monitoring and Feedback** mechanism, involving tools like Prometheus and Grafana, collects performance and usage data, providing insights that inform future development and optimization efforts, thus completing the DevOps cycle. This causal chain enables the rapid, reliable, and continuous delivery of software systems, fostering collaboration and improving overall quality.

## Methods And Frameworks

In DevOps, several methods and frameworks are employed to facilitate collaboration, automation, and continuous improvement. The Agile methodology is often used in conjunction with DevOps, emphasizing iterative development, continuous testing, and rapid deployment. 
The DevOps Infinity Loop model illustrates the cyclical nature of DevOps, comprising plan, develop, deliver, and operate phases. 
The Three Ways framework, introduced by Gene Kim, focuses on the principles of flow, feedback, and continuous learning. 
The CALMS model (Culture, Automation, Lean, Measurement, Sharing) provides a structured approach to implementing DevOps practices. 
When to use: Agile and DevOps Infinity Loop are suitable for projects requiring rapid iteration and deployment, while the Three Ways and CALMS models are useful for organizations seeking to adopt a holistic DevOps approach. 
Failure modes: Inadequate cultural transformation can hinder Agile and DevOps adoption, while insufficient automation and measurement can limit the effectiveness of the Three Ways and CALMS models. 
Additionally, formulas such as Little's Law (Lead Time = Work in Progress / Average Completion Rate) can be applied to optimize workflow and reduce lead times. 
Understanding these methods, models, and formulas enables DevOps practitioners to select the most suitable approaches for their organizations and mitigate potential failure modes.

## Worked Examples

Consider a web application with 1000 users, where each user makes 5 requests per minute. The application has a response time requirement of 200ms. To meet this requirement, the development team implements a load balancer and 5 identical servers, each capable of handling 200 requests per second.

In the first example, if each server has a utilization of 70%, what is the maximum response time? Assuming a linear relationship between utilization and response time, with a response time of 100ms at 0% utilization and 500ms at 100% utilization, we can calculate the response time as follows: Response Time = (500-100) * (0.7) + 100 = 250 + 100 = 350ms, which is within the requirement.

In the second example, suppose the development team wants to reduce the response time by 20% by adding more servers. If each server costs $100 per hour to run, and the team has a budget of $500 per hour, how many servers can they add? With a budget of $500 per hour, the team can add 5 new servers ($500 / $100 per server), making a total of 10 servers.

In the third example, if the application has a deployment frequency of 10 times per day, and each deployment takes 10 minutes to complete, what is the total downtime per day? Assuming a rolling deployment strategy where only one server is taken down at a time, the total downtime per day can be calculated as: Total Downtime = 10 deployments * 10 minutes * (1/10) = 10 minutes, since only one server is taken down at a time, and there are 10 servers in total.

## Applications

In computer science, DevOps is applied in various domains to bridge the gap between software development and operations teams, ensuring faster time-to-market, improved quality, and increased efficiency. In web development, DevOps practices such as continuous integration and continuous deployment (CI/CD) enable rapid deployment of updates and features, as seen in companies like Amazon and Google. In cloud computing, DevOps is used to manage and monitor cloud infrastructure, leveraging tools like AWS CloudFormation and Azure DevOps to automate provisioning and scaling. In mobile app development, DevOps helps teams manage the complex lifecycle of mobile apps, from development to deployment, using tools like Jenkins and GitLab CI/CD. Additionally, DevOps is applied in enterprise software development, where it helps teams manage complex software systems, ensure compliance, and maintain security, as seen in companies like Microsoft and IBM. The use of DevOps in these domains is characterized by the adoption of agile methodologies, automation of testing and deployment, and the use of metrics and monitoring to inform decision-making. By applying DevOps principles, organizations can improve collaboration, reduce errors, and increase the speed and reliability of software releases.

## Common Errors

In DevOps, common mistakes include inadequate testing, insufficient monitoring, and poor communication between development and operations teams. One error is neglecting to automate testing, leading to manual testing bottlenecks and potential human error. Another mistake is not implementing continuous integration and continuous deployment (CI/CD) pipelines, resulting in delayed feedback and longer time-to-market. Insufficient monitoring and logging can also lead to undetected issues and prolonged downtime. Furthermore, not adopting infrastructure as code (IaC) practices can cause configuration drift and make it difficult to reproduce environments. Additionally, ignoring security and compliance in the development process can lead to vulnerabilities and non-compliance issues. Poor communication and lack of collaboration between teams can cause misunderstandings, misaligned goals, and inefficient workflows. These errors often stem from a lack of understanding of DevOps principles, inadequate training, or insufficient investment in automation and tooling. By recognizing these common errors, practitioners can take steps to avoid them and implement more effective DevOps practices.

## Advanced

In computer science, DevOps encompasses a range of advanced topics that build upon the foundational principles of development, operations, and quality assurance. At the graduate level, students delve into the intricacies of continuous integration and delivery, exploring the application of containerization using Docker, and orchestration with Kubernetes. The use of infrastructure as code (IaC) tools like Terraform and AWS CloudFormation enables the management of complex systems through version-controlled configuration files. Advanced monitoring and logging techniques, including the ELK Stack (Elasticsearch, Logstash, Kibana) and Prometheus, provide insights into system performance and facilitate proactive maintenance. Open questions in the field include the integration of artificial intelligence and machine learning into DevOps pipelines, as well as the development of more sophisticated security and compliance frameworks. The field is moving towards greater emphasis on serverless computing, edge computing, and the application of DevOps principles to emerging technologies like the Internet of Things (IoT) and cloud-native applications. Researchers are also exploring the human factors and organizational aspects of DevOps, recognizing that successful implementation requires not only technical expertise but also cultural and process changes within organizations.
