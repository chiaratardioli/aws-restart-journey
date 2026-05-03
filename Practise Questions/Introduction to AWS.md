## Introduction to AWS – Practice Questions

### Question 1
Which design principle aligns with performance efficiency pillar of the AWS Well-Architected Framework?  

A. Using serverless architectures  
B. Scaling horizontally  
C. Measuring the cost of workloads  
D. Using managed services  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. Scaling horizontally**

**Explanation:**  
The **performance efficiency pillar** focuses on efficiently using computing resources and adapting to changing demand. **Horizontal scaling** allows systems to handle increased load by adding more instances instead of relying on a single larger one.

**Why not the others:**
- **A. Using serverless architectures** – Helps efficiency but is not the core principle here.  
- **C. Measuring the cost of workloads** – Belongs to **cost optimization**.  
- **D. Using managed services** – General best practice, not the key principle asked.

</details>

---

### Question 2
A company migrated to the AWS Cloud. Now the company pays for services on an as-needed basis. Which advantage of cloud computing is the company benefiting from?  

A. Stop spending money running and maintaining data centers  
B. Increase speed and agility  
C. Go global in minutes  
D. Trade fixed expense for variable expense  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: D. Trade fixed expense for variable expense**

**Explanation:**  
Cloud computing allows companies to shift from **capital expenditure (fixed costs)** to **operational expenditure (pay-as-you-go)**, meaning they only pay for what they use.

**Why not the others:**
- **A. Stop spending money on data centers** – True benefit, but not what is described.  
- **B. Increase speed and agility** – Not related to billing model.  
- **C. Go global in minutes** – Refers to global infrastructure.

</details>

---

### Question 3
A company is moving some of its on-premises IT services to the AWS Cloud. The finance department wants to see the entire bill and receive notifications if limits are exceeded. Which AWS service should the company use?  

A. AWS Cost and Usage Reports  
B. AWS Budgets  
C. AWS Organizations consolidated billing  
D. Cost Explorer  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. AWS Budgets**

**Explanation:**  
**AWS Budgets** allows organizations to **set spending thresholds** and receive alerts when costs exceed predefined limits.

**Why not the others:**
- **A. Cost and Usage Reports** – Detailed reporting, no alerting.  
- **C. Consolidated billing** – Aggregates accounts, not alerts.  
- **D. Cost Explorer** – Visualization tool, not proactive alerts.

</details>

---

### Question 4
An ecommerce company plans to move its workload to AWS to support dynamic usage patterns. Which benefits make AWS cost-effective? (Select TWO.)  

A. Reliability  
B. Security  
C. Elasticity  
D. Pay-as-you-go pricing  
E. High availability  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: C and D**

**Explanation:**  
Dynamic workloads benefit from **elasticity** (scale resources up/down) and **pay-as-you-go pricing**, ensuring cost efficiency.

**Why not the others:**
- **A. Reliability** – Important but not cost-related.  
- **B. Security** – Not directly tied to cost savings.  
- **E. High availability** – Improves uptime, not cost efficiency.

</details>

---

### Question 5
A company wants to scale compute resources based on changing demand. Which AWS benefit is this?  

A. Global deployment in minutes  
B. Cost savings  
C. Agility  
D. Elasticity  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: D. Elasticity**

**Explanation:**  
**Elasticity** is the ability to automatically scale resources up or down based on demand.

**Why not the others:**
- **A. Global deployment** – Refers to geographic expansion.  
- **B. Cost savings** – Outcome, not the mechanism.  
- **C. Agility** – Faster innovation, not scaling.

</details>

---

### Question 6
A company is releasing a business-critical application and needs planning plus real-time support. What should they do?  

A. AWS Trusted Advisor  
B. AWS Partner Network  
C. AWS Enterprise Support  
D. AWS Professional Services  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: C. AWS Enterprise Support**

**Explanation:**  
**Enterprise Support** provides **proactive guidance, infrastructure event management, and 24/7 support** for critical workloads.

**Why not the others:**
- **A. Trusted Advisor** – Recommendations only.  
- **B. APN** – Partner ecosystem, not direct support.  
- **D. Professional Services** – Project-based, not real-time support.

</details>

---

### Question 7
Which AWS CAF perspective focuses on data catalog and governance?  

A. Operations  
B. Governance  
C. Business  
D. Platform  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. Governance**

**Explanation:**  
The **Governance perspective** ensures **data management, compliance, and cataloging** across the organization.

**Why not the others:**
- **A. Operations** – Focuses on running workloads.  
- **C. Business** – Strategy and outcomes.  
- **D. Platform** – Infrastructure and architecture.

</details>

---

### Question 8
For which use case are On-Demand Instances MOST cost-effective?  

A. Interruptible workloads  
B. Short-term testing (1 month)  
C. 1-year workload  
D. 3-year workload  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. Short-term testing**

**Explanation:**  
On-Demand is best for **short-term, unpredictable workloads** without long-term commitments.

**Why not the others:**
- **A. Interruptible workloads** – Spot Instances better.  
- **C & D. Long-term workloads** – Reserved Instances cheaper.

</details>

---

### Question 9
Which AWS principle helps test applications easily?  

A. Long-term commitments  
B. Scale without commitments  
C. Full infrastructure control  
D. Manage all maintenance  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. Scale without commitments**

**Explanation:**  
Cloud allows **rapid provisioning and deprovisioning**, enabling easy testing without long-term cost.

**Why not the others:**
- **A. Long-term commitments** – Opposite of flexibility.  
- **C. Full control** – Not required for testing.  
- **D. Manage maintenance** – AWS handles infrastructure.

</details>

---

### Question 10
Which AWS tool provides a graphical interface?  

A. AWS Copilot  
B. AWS CLI  
C. AWS Management Console  
D. AWS SDKs  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: C. AWS Management Console**

**Explanation:**  
The **AWS Management Console** is a web-based GUI for managing AWS resources.

**Why not the others:**
- **A. Copilot** – CLI-based tool.  
- **B. CLI** – Command line only.  
- **D. SDKs** – Used in code.

</details>

---

### Question 11
Where can users find AWS solution design examples?  

A. AWS Marketplace  
B. AWS Service Catalog  
C. AWS Architecture Center  
D. AWS Trusted Advisor  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: C. AWS Architecture Center**

**Explanation:**  
The **Architecture Center** provides **reference architectures and best practices**.

**Why not the others:**
- **A. Marketplace** – Software listings.  
- **B. Service Catalog** – Approved resources.  
- **D. Trusted Advisor** – Recommendations.

</details>

---

### Question 12
How can a company resell unused Reserved Instances?  

A. Contact support  
B. Sell on RI Marketplace  
C. AWS Marketplace  
D. Convert to Savings Plans  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. Sell on RI Marketplace**

**Explanation:**  
AWS allows selling unused Standard RIs on the **Reserved Instance Marketplace**.

**Why not the others:**
- **A. Support** – Cannot sell for you.  
- **C. AWS Marketplace** – Different service.  
- **D. Cannot convert Standard RIs.**

</details>

---

### Question 13
Which service enables consolidated billing?  

A. Billing Console  
B. AWS Organizations  
C. Cost Reports  
D. Systems Manager  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. AWS Organizations**

**Explanation:**  
**AWS Organizations** enables **centralized billing and account management**.

**Why not the others:**
- **A. Billing console** – View only.  
- **C. Reports** – Data only.  
- **D. Systems Manager** – Operations tool.

</details>

---

### Question 14
Which principle relates to reliability?  

A. Test recovery procedures  
B. Experiment more  
C. Go global  
D. Analyze costs  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: A. Test recovery procedures**

**Explanation:**  
Reliability includes **testing disaster recovery and failover mechanisms**.

**Why not the others:**
- **B. Experiment** – Innovation.  
- **C. Global** – Scalability.  
- **D. Costs** – Cost optimization.

</details>

---

### Question 15
Which pillar focuses on minimizing costs?  

A. Security  
B. Reliability  
C. Sustainability  
D. Cost optimization  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: D. Cost optimization**

**Explanation:**  
This pillar ensures **efficient resource usage and minimal cost**.

</details>

---

### Question 16
Which EC2 tasks are customer responsibilities? (Select TWO.)  

A. Hypervisor patching  
B. OS patching  
C. Data encryption  
D. Hardware setup  
E. Physical security  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B and C**

**Explanation:**  
Customers manage the **guest OS and data**, including patching and encryption.

**Why not the others:**
- **A, D, E** – AWS responsibilities.

</details>

---

### Question 17
Which report shows MFA status?  

A. Cost reports  
B. IAM credential report  
C. Billing report  
D. Cost Explorer  

### Answer
<details>
<summary><strong>Show answer</strong></summary>

**Correct Answer: B. IAM credential report**

**Explanation:**  
This report provides **security details including MFA status**.

</details>
