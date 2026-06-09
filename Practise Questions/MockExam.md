# Mock Exam

## Question #1

Which scaling type can forecast future application traffic to provision the right number of EC2 instances?

A. Predictive scaling  
B. Simple scaling  
C. Scheduled scaling  
D. Target tracking scaling  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. Predictive scaling**

**Explanation:**
Predictive scaling uses machine learning and historical workload data to forecast future application demand. It automatically adjusts the number of Amazon EC2 instances in advance of expected traffic changes, helping ensure that sufficient capacity is available when needed.

* **Simple scaling** responds to a single CloudWatch alarm and does not predict future demand.
* **Scheduled scaling** adjusts capacity based on predefined schedules that you configure manually.
* **Target tracking scaling** automatically adjusts capacity to maintain a target metric (such as CPU utilization) but does not forecast future traffic.

</details>

## Question #2

A company wants to connect its on-premises network to AWS so that employees can access resources in a secure, private environment without exposing them to the public internet.

Which AWS service should the company use?

A. AWS Virtual Private Network  
B. Amazon CloudFront  
C. AWS Connect  
D. Amazon Virtual Private Cloud  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. AWS Virtual Private Network**

**Explanation:**
AWS Virtual Private Network (AWS VPN) enables secure, encrypted connections between an on-premises network and AWS over the internet. It allows employees to access AWS resources privately and securely without exposing those resources directly to the public internet.

* **Amazon CloudFront** is a content delivery network (CDN) used to distribute content with low latency.
* **AWS Connect** is a cloud-based contact center service.
* **Amazon Virtual Private Cloud (VPC)** provides a logically isolated network within AWS, but by itself does not establish connectivity between an on-premises network and AWS. AWS VPN is commonly used to connect an on-premises network to a VPC.

</details>

## Question #3

Which service can connect a company's on-premises environment to a VPC without using the public internet?

A. VPC Endpoint  
B. Internet Gateway  
C. AWS Direct Connect  
D. AWS Site-to-Site VPN  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. AWS Direct Connect**

**Explanation:**
AWS Direct Connect provides a dedicated private network connection between an on-premises environment and AWS. Because the connection does not traverse the public internet, it can offer more consistent network performance, lower latency, and enhanced security.

* **VPC Endpoint** allows private access to supported AWS services from within a VPC but does not connect an on-premises environment to AWS.
* **Internet Gateway** enables communication between a VPC and the public internet.
* **AWS Site-to-Site VPN** provides an encrypted connection between an on-premises network and AWS, but it typically operates over the public internet.

</details>

## Question #4

A company wants to connect its on-premises office network to AWS quickly using the internet.

Which AWS service should the company use?

A. AWS Direct Connect  
B. AWS Site-to-Site VPN  
C. AWS Client VPN  
D. NAT Gateway  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. AWS Site-to-Site VPN**

**Explanation:**
AWS Site-to-Site VPN creates a secure, encrypted connection between an on-premises network and an AWS Virtual Private Cloud (VPC) over the internet. It is a quick and cost-effective way to establish connectivity without requiring dedicated physical network links.

* **AWS Direct Connect** provides a dedicated private connection to AWS but typically requires more setup time and coordination.
* **AWS Client VPN** is designed for individual users to securely access AWS resources and on-premises networks, not for connecting entire office networks.
* **NAT Gateway** allows instances in a private subnet to access the internet but does not provide connectivity between an on-premises network and AWS.

</details>

## Question #5

Which services enable secure private connectivity without public internet? (Select TWO)

A. Amazon Inspector  
B. Amazon Connect  
C. AWS Transit Gateway  
D. AWS Internet Gateway  
E. AWS PrivateLink  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answers: C. AWS Transit Gateway and E. AWS PrivateLink**

**Explanation:**
Both AWS Transit Gateway and AWS PrivateLink help provide private connectivity without exposing traffic to the public internet.

* **AWS Transit Gateway** acts as a central hub for connecting multiple VPCs, on-premises networks, and VPN connections, enabling private communication across connected networks.
* **AWS PrivateLink** allows private access to supported AWS services and customer-hosted services through private endpoints within a VPC, without traversing the public internet.

Why the others are incorrect:

* **Amazon Inspector** is a security assessment and vulnerability management service.
* **Amazon Connect** is a cloud contact center service.
* **AWS Internet Gateway** enables communication between a VPC and the public internet, which is the opposite of private connectivity.

</details>

## Question #6

Which framework can accelerate a company’s cloud-driven business transformation?

A. AWS Control Tower  
B. AWS Professional Services  
C. AWS Cloud Adoption Framework  
D. AWS Managed Services  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. AWS Cloud Adoption Framework**

**Explanation:**
The AWS Cloud Adoption Framework (AWS CAF) helps organizations plan and execute successful cloud transformations. It provides guidance, best practices, and a structured approach across business, people, governance, platform, security, and operations perspectives to accelerate cloud adoption and business transformation.

* **AWS Control Tower** helps set up and govern a secure multi-account AWS environment.
* **AWS Professional Services** provides expert consulting and implementation assistance but is not a framework.
* **AWS Managed Services** helps operate AWS infrastructure on behalf of customers but does not provide a cloud transformation framework.

</details>

## Question #7

Which tool is recommended for AWS disaster recovery for on-prem bare metal servers and SQL databases?

A. AWS Migration Hub  
B. AWS Database Migration Service  
C. AWS Application Migration Service  
D. AWS Elastic Disaster Recovery  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: D. AWS Elastic Disaster Recovery**

**Explanation:**
AWS Elastic Disaster Recovery (AWS DRS) is designed specifically for disaster recovery of on-premises and cloud workloads, including bare metal servers and databases such as SQL Server. It continuously replicates data into AWS and enables rapid recovery with minimal downtime.

* **AWS Migration Hub** helps track and manage application migrations but does not provide disaster recovery capabilities.
* **AWS Database Migration Service (DMS)** is used to migrate databases, not to provide full server-level disaster recovery.
* **AWS Application Migration Service (MGN)** is primarily used for lift-and-shift migration of servers to AWS, not ongoing disaster recovery operations.

</details>

## Question #8

A company needs to launch new features rapidly to respond to changing customer demands and market conditions.

Which AWS cloud characteristic does this demonstrate?

A. Scalability  
B. Elasticity  
C. Agility  
D. Reliability  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. Agility**

**Explanation:**
Agility refers to the ability to quickly develop, test, and deploy applications in response to changing business needs. AWS enables this by providing on-demand resources, automation, and managed services that reduce the time required to innovate and release new features.

* **Scalability** is the ability to increase or decrease resources to handle workload demand.
* **Elasticity** is the automatic adjustment of resources in response to changes in demand.
* **Reliability** is the ability of a system to recover from failures and continue operating correctly.

</details>

## Question #9

Which of the following can resolve the connection between on-premises VPN and an Amazon VPC? (Select TWO)

A. Virtual Private Gateway  
B. Amazon Route 53  
C. Egress-Only Internet Gateway  
D. NAT Gateway  
E. VPC Peering  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answers: A. Virtual Private Gateway and B. Amazon Route 53**

**Explanation:**
A **Virtual Private Gateway** is the AWS-side VPN endpoint attached to a VPC that enables secure VPN connectivity from an on-premises network into AWS.

**Amazon Route 53** can be used to resolve DNS names and route traffic appropriately between on-premises and AWS resources in hybrid architectures. In some scenarios, it supports name resolution and connectivity flows that help make VPN-based hybrid communication work correctly.

Why the others are incorrect:

* **Egress-Only Internet Gateway** is used for IPv6 outbound internet access from a VPC, not VPN connectivity.
* **NAT Gateway** allows instances in private subnets to access the internet, not on-premises connectivity.
* **VPC Peering** connects VPCs together and does not connect on-premises networks to AWS.

</details>

## Question #10

A company is launching an online multiplayer gaming application for users around the world. The application requires low latency and uses UDP to send real-time game data between players and AWS endpoints.

Which AWS service should the company use to improve global application availability and performance?

A. Network Load Balancer  
B. Amazon SNS  
C. AWS Global Accelerator  
D. Amazon CloudFront  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. AWS Global Accelerator**

**Explanation:**
AWS Global Accelerator improves global application availability and performance by routing user traffic through the AWS global network to the nearest healthy endpoint. It supports both TCP and UDP traffic, making it well-suited for real-time applications such as multiplayer gaming that require low latency and fast, reliable connectivity.

* **Network Load Balancer** operates within a region and does not provide global traffic optimization.
* **Amazon SNS** is a messaging and notification service and does not handle traffic routing.
* **Amazon CloudFront** is a content delivery network optimized for HTTP/HTTPS traffic and does not support UDP-based real-time game traffic.

</details>

## Question #11

A developer needs to collect and process large streams of data records in real-time. Which AWS service should be used for this task?

A. AWS CloudTrail  
B. Amazon Kinesis Data Firehose  
C. AWS Glue  
D. Amazon Kinesis Data Streams  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: D. Amazon Kinesis Data Streams**

**Explanation:**
Amazon Kinesis Data Streams is designed for real-time ingestion and processing of large streams of data records. It allows applications to process data continuously as it arrives, making it suitable for real-time analytics and streaming workloads.

* **AWS CloudTrail** records API activity for auditing and governance, not real-time data streaming.
* **Amazon Kinesis Data Firehose** is used for loading streaming data into destinations like S3 or Redshift, but it is not designed for custom real-time processing.
* **AWS Glue** is a serverless ETL service mainly used for batch data processing and data preparation.

</details>



