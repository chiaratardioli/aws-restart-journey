# AWS Practice Questions (1–44) – Formatted Answers

---

## Question #1
Which design principle aligns with performance efficiency pillar of the AWS Well-Architected Framework?

A. Using serverless architectures  
B. Scaling horizontally  
C. Measuring the cost of workloads  
D. Using managed services  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Scaling horizontally**

**Explanation:**  
The **performance efficiency pillar** of the AWS Well-Architected Framework focuses on using computing resources efficiently to meet system requirements and maintain performance as demand changes. A key design principle here is **scaling horizontally**, which means adding more instances or resources to handle increased load instead of relying on a single larger instance.

**Why not the others:**
- **A. Using serverless architectures** – Improves efficiency, but is more about abstracting infrastructure management rather than a core design principle of performance efficiency.  
- **C. Measuring the cost of workloads** – Belongs to the **cost optimization** pillar.  
- **D. Using managed services** – General optimization, not the core principle asked.

</details>

---

## Question #2
A company migrated to the AWS Cloud. Now the company pays for services on an as-needed basis. Which advantage of cloud computing is the company benefiting from?

A. Stop spending money running and maintaining data centers  
B. Increase speed and agility  
C. Go global in minutes  
D. Trade fixed expense for variable expense  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. Trade fixed expense for variable expense**

**Explanation:**  
Cloud computing shifts costs from upfront capital expenses (CapEx) to variable operational expenses (OpEx), allowing companies to pay only for what they use.

**Why not the others:**
- **A.** Describes cost reduction but not the core financial model shift.  
- **B.** Refers to agility, not pricing model.  
- **C.** Refers to global deployment capability.  
- **D.** Correct financial benefit of cloud adoption.

</details>

---

## Question #3
Which AWS service helps set spending limits and send notifications when exceeded?

A. AWS Cost and Usage Reports  
B. AWS Budgets  
C. AWS Organizations consolidated billing  
D. Cost Explorer  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. AWS Budgets**

**Explanation:**  
AWS Budgets allows you to set custom cost and usage thresholds and receive alerts when limits are exceeded.

**Why not the others:**
- **A.** Reporting only, no alerts.  
- **C.** Billing consolidation, not monitoring.  
- **D.** Visualization tool, not alerting system.

</details>

---

## Question #4
Which service deploys infrastructure using templates?

A. AWS CloudFormation  
B. AWS Directory Service  
C. Amazon Lightsail  
D. AWS CodeDeploy  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS CloudFormation**

**Explanation:**  
AWS CloudFormation allows infrastructure as code using templates to deploy resources consistently.

**Why not the others:**
- **B.** Directory management  
- **C.** Simple VM hosting  
- **D.** Application deployment, not infrastructure provisioning

</details>

---

## Question #5
Which credentials are required for AWS CLI access? (Select TWO)

A. Public key  
B. Secret access key  
C. IAM role  
D. Access key ID  
E. Private key  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B and D**

**Explanation:**  
AWS CLI uses Access Key ID and Secret Access Key for authentication.

**Why not the others:**
- **A.** Not used for AWS CLI authentication  
- **C.** Roles are used differently (temporary credentials)  
- **E.** Not used in AWS IAM authentication model

</details>

---

## Question #6
Which service triggers Step Functions on EC2 state change?

A. SageMaker  
B. Connect  
C. EventBridge  
D. Fargate  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Amazon EventBridge**

**Explanation:**  
EventBridge captures AWS service events and triggers workflows like Step Functions.

**Why not the others:**
- Not event routing services.

</details>

---

## Question #7
Which service provides low-latency access to AWS data from on-premises?

A. CloudFront  
B. Storage Gateway  
C. Backup  
D. DataSync  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. AWS Storage Gateway**

**Explanation:**  
Provides hybrid access between on-prem and AWS storage.

**Why not the others:**
- CloudFront = CDN  
- DataSync = transfer tool  
- Backup = backup service

</details>

---

## Question #8
Which service migrates databases with minimal downtime?

A. AWS DMS  
B. Snow Family  
C. DataSync  
D. Mainframe Modernization  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS DMS**

**Explanation:**  
AWS Database Migration Service enables live database replication with minimal downtime.

**Why not the others:**
- Not database replication services.

</details>

---

## Question #9
Which provides consistent low-latency connectivity to AWS?

A. Direct Connect  
B. Internet  
C. VPN  
D. Amazon Connect  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS Direct Connect**

**Explanation:**  
Provides dedicated private network connection to AWS.

**Why not the others:**
- Internet/VPN = variable latency  
- Amazon Connect = contact center service

</details>

---

## Question #10
Which service tracks migration inventory?

A. CloudWatch  
B. DataSync  
C. Migration Hub  
D. Application Migration Service  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. AWS Migration Hub**

**Explanation:**  
Centralized tracking of application migration progress.

</details>


## Question #11
An ecommerce company plans to move its data center workload to the AWS Cloud to support highly dynamic usage patterns. Which benefits make the AWS Cloud cost-effective for this type of workload? (Select TWO.)

A. Reliability  
B. Security  
C. Elasticity  
D. Pay-as-you-go resource pricing  
E. High availability  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C and D**

**Explanation:**  
Highly dynamic workloads benefit from the ability to scale resources automatically (**elasticity**) and only pay for what is used (**pay-as-you-go pricing**), avoiding overprovisioning.

**Why not the others:**
- **A. Reliability** – important, but not directly cost-related  
- **B. Security** – unrelated to cost model  
- **E. High availability** – availability feature, not cost optimization driver  

</details>

---

## Question #12
Which benefit describes scaling compute resources as needed?

A. Global deployment in minutes  
B. Cost savings  
C. Agility  
D. Elasticity  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. Elasticity**

**Explanation:**  
Elasticity is the ability to automatically increase or decrease resources based on demand.

**Why not the others:**
- **A.** Geographic benefit  
- **B.** Financial benefit  
- **C.** Broad capability, not specific scaling behavior  

</details>

---

## Question #13
Which service provides repeatable infrastructure deployment?

A. AWS CloudFormation  
B. AWS CodeDeploy  
C. AWS CodeBuild  
D. AWS Systems Manager  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS CloudFormation**

**Explanation:**  
CloudFormation enables Infrastructure as Code for consistent deployments.

</details>

---

## Question #14
Which actions allow programmatic-only access with least privilege? (Select TWO)

A. Console access only user  
B. Programmatic access only user  
C. IAM role with console access  
D. Admin policy  
E. RDS access policy  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B and E**

**Explanation:**  
Programmatic access is required for CLI/SDK usage, and permissions should be limited to RDS only.

**Why not the others:**
- Console access contradicts requirement  
- Admin access violates least privilege  

</details>

---

## Question #15
Which service automatically patches EC2 Windows instances?

A. AWS Systems Manager  
B. AWS Organizations  
C. AWS Control Tower  
D. ELB  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS Systems Manager**

**Explanation:**  
Systems Manager Patch Manager automates OS patching.

</details>

---

## Question #16
Which AWS support plan provides architecture guidance + event support?

A. Trusted Advisor  
B. APN  
C. Enterprise Support  
D. Professional Services  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. AWS Enterprise Support**

**Explanation:**  
Includes Technical Account Manager (TAM), architecture reviews, and event support.

</details>

---

## Question #17
Which AWS CAF perspective organizes data catalog inventory?

A. Operations  
B. Governance  
C. Business  
D. Platform  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Governance**

**Explanation:**  
Governance ensures data management, compliance, and cataloging.

</details>

---

## Question #18
When are EC2 On-Demand instances most cost-effective?

A. Restartable workloads  
B. 1-month QA testing  
C. 1-year web server  
D. 3-year database  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. An instance in continual use for 1 month**

**Explanation:**  
On-Demand is best for short-term or unpredictable workloads.

</details>

---

## Question #19
Which service hosts domain names in AWS?

A. Lambda  
B. Route 53  
C. CloudFront  
D. Direct Connect  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Amazon Route 53**

**Explanation:**  
Route 53 is AWS DNS and domain registration service.

</details>

---

## Question #20
Which AWS principle supports testing applications?

A. Long-term commitment  
B. Scale up/down without commitment  
C. Full infrastructure control  
D. Manual maintenance  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B**

**Explanation:**  
Cloud enables elasticity and experimentation without long-term commitment.

</details>

---

## Question #21
Which provides graphical AWS management interface?

A. Copilot  
B. CLI  
C. Management Console  
D. SDKs  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. AWS Management Console**

**Explanation:**  
Web-based UI for managing AWS services.

</details>

---

## Question #22
Best service for managed MariaDB with low overhead?

A. RDS  
B. Neptune  
C. S3  
D. DynamoDB  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. Amazon RDS**

**Explanation:**  
Fully managed relational database service.

</details>

---

## Question #23
Which provides multi-language SDKs?

A. CodePipeline  
B. AWS SDKs  
C. CloudWatch  
D. CodeDeploy  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. AWS SDKs**

**Explanation:**  
SDKs provide APIs for multiple programming languages.

</details>

---

## Question #24
Which service builds chatbots?

A. Amazon Lex  
B. Amplify  
C. Comprehend  
D. Polly  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. Amazon Lex**

**Explanation:**  
Lex provides conversational AI and chatbot functionality.

</details>

---

## Question #25
Where to find AWS architecture examples?

A. Marketplace  
B. Service Catalog  
C. Architecture Center  
D. Trusted Advisor  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. AWS Architecture Center**

**Explanation:**  
Provides reference architectures and best practices.

</details>


## Question #26
A company purchased Amazon EC2 Standard Reserved Instances (RIs) and now needs to move workloads to a different instance family. What should they do with unused RIs?

A. Contact AWS Support to sell them  
B. Sell them on the Reserved Instance Marketplace  
C. Sell them on AWS Marketplace  
D. Convert to Savings Plans  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Sell the Standard RIs on the Amazon EC2 Reserved Instance Marketplace**

**Explanation:**  
Standard Reserved Instances can be resold in the EC2 Reserved Instance Marketplace.

**Why not the others:**
- AWS Support does not resell RIs  
- AWS Marketplace is for software, not RIs  
- Conversion to Savings Plans is not supported directly  

</details>

---

## Question #27
How can a company access S3 from EC2 without using the internet?

A. VPN connection  
B. Internet gateway  
C. VPC endpoint  
D. NAT gateway  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. VPC endpoint**

**Explanation:**  
A VPC endpoint enables private connectivity between VPC resources and AWS services like S3.

</details>

---

## Question #28
Which service enables consolidated billing?

A. Billing and Cost Management console  
B. AWS Organizations  
C. Cost and Usage Report  
D. Systems Manager  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. AWS Organizations**

**Explanation:**  
AWS Organizations centralizes billing across multiple accounts.

</details>

---

## Question #29
Which is a reliability design principle?

A. Test recovery procedures  
B. Experiment more often  
C. Go global in minutes  
D. Attribute expenditure  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. Test recovery procedures**

**Explanation:**  
Reliability focuses on recovering from failures effectively.

</details>

---

## Question #30
Which service supports low-latency access to on-premises systems with data residency requirements?

A. Wavelength  
B. Transit Gateway  
C. Ground Station  
D. Outposts  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. AWS Outposts**

**Explanation:**  
Outposts extends AWS infrastructure on-premises.

</details>

---

## Question #31
Most cost-effective EC2 pricing for intermittent workloads?

A. Standard RIs  
B. Convertible RIs  
C. Capacity Reservations  
D. On-Demand Instances  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. On-Demand Instances**

**Explanation:**  
Best for short, infrequent workloads with no commitment.

</details>

---

## Question #32
Which AWS Well-Architected pillar focuses on minimizing cost?

A. Security  
B. Reliability  
C. Sustainability  
D. Cost optimization  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. Cost optimization**

**Explanation:**  
This pillar focuses on reducing unnecessary spending and improving efficiency.

</details>

---

## Question #33
Which service deploys and manages applications?

A. CodeGuru  
B. Fargate  
C. CodeCommit  
D. Elastic Beanstalk  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. AWS Elastic Beanstalk**

**Explanation:**  
Elastic Beanstalk handles deployment, scaling, and management.

</details>

---

## Question #34
Which EC2 responsibilities belong to the customer? (Select TWO)

A. Hypervisor patching  
B. OS patching  
C. Encrypt data at rest  
D. Physical hardware  
E. Data center security  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B and C**

**Explanation:**  
Customers manage the guest OS and data encryption.

**AWS handles:**
- Hardware  
- Hypervisor  
- Physical security  

</details>

---

## Question #35
Which service manages SSL/TLS certificates?

A. WAF  
B. Shield  
C. VPC  
D. ACM  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. AWS Certificate Manager (ACM)**

**Explanation:**  
ACM provisions and manages TLS certificates.

</details>

---

## Question #36
Which report shows MFA device status?

A. Cost and Usage Report  
B. IAM credential report  
C. Billing report  
D. Cost Explorer  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. IAM credential report**

**Explanation:**  
Lists users, credentials, and MFA status.

</details>

---

## Question #37
Which service provides dedicated low-latency connectivity?

A. Direct Connect  
B. VPN  
C. Directory Service  
D. Transit Gateway  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS Direct Connect**

**Explanation:**  
Private dedicated network connection to AWS.

</details>

---

## Question #38
Which can IAM users do without root access?

A. Change support plan  
B. Close account  
C. View billing console  
D. Activate billing access  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. View the AWS Billing console**

**Explanation:**  
With permissions enabled, IAM users can view billing info.

</details>

---

## Question #39
Which acts as subnet-level firewall?

A. Security group  
B. Network ACL  
C. Traffic Mirroring  
D. Internet gateway  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Network ACL**

**Explanation:**  
NACLs operate at subnet level and are stateless.

</details>

---

## Question #40
Benefit of Elastic Load Balancing?

A. Auto scale resources  
B. Distribute traffic across resources  
C. Span multiple regions  
D. Balance internet gateways  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Balance traffic across multiple compute resources**

**Explanation:**  
ELB distributes incoming traffic across targets.

</details>

---

## Question #41
Which service creates private scalable network environments?

A. ECS  
B. S3  
C. VPC  
D. Route tables  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Amazon VPC**

**Explanation:**  
VPC provides isolated virtual networks.

</details>

---

## Question #42
Fully managed NoSQL database?

A. RDS  
B. Redshift  
C. DynamoDB  
D. Aurora  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Amazon DynamoDB**

**Explanation:**  
Serverless NoSQL key-value/document database.

</details>

---

## Question #43
Scalable data warehouse service?

A. S3  
B. DynamoDB  
C. Kinesis  
D. Redshift  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. Amazon Redshift**

**Explanation:**  
Fully managed cloud data warehouse.

</details>

---

## Question #44
Features of Network ACLs (Select TWO)

A. Stateless  
B. Stateful  
C. Evaluate all rules before allowing traffic  
D. Process rules in order  
E. Instance-level firewall  

### Answer
<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A and D**

**Explanation:**  
NACLs are stateless and evaluate rules in order.

**Why not others:**
- Stateful applies to Security Groups  
- Instance-level applies to Security Groups  
- NACLs do NOT evaluate all rules before decision  

</details>
