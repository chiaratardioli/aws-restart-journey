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

---

## Question #12

A company wants objects older than 365 days moved to Glacier Deep Archive automatically. Which S3 feature should they configure?

A. S3 Lifecycle rule to transition objects to Glacier Deep Archive  
B. Cross-region replication only  
C. Versioning with MFA delete only  
D. Bucket policy with deny action  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. S3 Lifecycle rule to transition objects to Glacier Deep Archive**

**Explanation:**
Amazon S3 Lifecycle rules allow you to automatically transition objects between storage classes based on their age. In this case, a lifecycle policy can be configured to move objects older than 365 days to **S3 Glacier Deep Archive**, which is designed for long-term, low-cost storage.

* **Cross-region replication** is used to replicate objects across AWS regions, not to manage storage class transitions.
* **Versioning with MFA delete** is used for protecting against accidental deletion, not lifecycle transitions.
* **Bucket policy with deny action** is used for access control, not for storage automation.

</details>

## Question #13

A team wants to run containerized microservices. They prefer AWS-managed orchestration and minimal operational overhead. Which TWO services are appropriate?

A. AWS App Runner  
B. Amazon RDS  
C. Amazon ECS with Fargate  
D. Amazon EMR  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answers: A. AWS App Runner and C. Amazon ECS with Fargate**

**Explanation:**
Both AWS App Runner and Amazon ECS with AWS Fargate provide managed, serverless-style options for running containerized applications with minimal infrastructure management.

* **AWS App Runner** is a fully managed service that automatically builds, deploys, and scales containerized web applications and APIs without requiring infrastructure management.
* **Amazon ECS with AWS Fargate** allows you to run containers without managing servers, as Fargate handles the underlying compute infrastructure.

Why the others are incorrect:

* **Amazon RDS** is a managed relational database service, not for running containers.
* **Amazon EMR** is used for big data processing (Hadoop/Spark workloads), not microservices hosting.

</details>

## Question #14

A company needs to transfer terabytes of files from on-premises NAS into S3 on a recurring schedule with high performance. Which service is designed for this?

A. Amazon S3 replication for first import  
B. AWS Lambda for file transfer  
C. AWS Transfer Family only  
D. AWS DataSync  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: D. AWS DataSync**

**Explanation:**
AWS DataSync is designed for high-speed, automated, and recurring data transfers between on-premises storage (such as NAS) and AWS services like Amazon S3. It efficiently transfers large datasets and can be scheduled for regular sync operations.

* **Amazon S3 replication** is used to replicate objects between S3 buckets, not from on-premises NAS.
* **AWS Lambda** is not suitable for large-scale or high-throughput file transfers.
* **AWS Transfer Family** is used for file transfer protocols (SFTP, FTPS, FTP) into S3 or EFS, but it is not optimized for large-scale NAS migration or high-performance recurring sync workloads like DataSync.

</details>

## Question #15

A read-heavy relational database needs better read scaling. Which approach is recommended?

A. Add read replicas (RDS Read Replicas) or use read-replica features of Aurora  
B. Store queries in S3 lifecycle  
C. Switch to a single larger instance with no replication  
D. Use CloudFront to cache RDS responses  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. Add read replicas (RDS Read Replicas) or use read-replica features of Aurora**

**Explanation:**
For read-heavy workloads on a relational database, the standard AWS approach is to scale read traffic horizontally using read replicas. Amazon RDS supports read replicas, and Amazon Aurora provides built-in, highly efficient replication to multiple read replicas for improved read scalability and performance.

* **B. Store queries in S3 lifecycle** – S3 is object storage and not used for database query handling.
* **C. Switch to a single larger instance** – This is vertical scaling and does not solve read scaling limitations effectively.
* **D. Use CloudFront to cache RDS responses** – CloudFront is for caching web content, not direct database query results.

</details>

## Question #16

A web application needs to allow a user to upload file directly to S3 without exposing AWS credentials. Which mechanism is best?

A. Use pre-signed S3 URLs or POST policies to allow direct uploads  
B. Use EFS mount in the browser  
C. Make the S3 bucket public and accept uploads  
D. Embed root AWS credentials in the client  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. Use pre-signed S3 URLs or POST policies to allow direct uploads**

**Explanation:**
Pre-signed URLs (or pre-signed POST policies) allow clients to upload files directly to Amazon S3 securely without exposing AWS credentials. The server generates a temporary, time-limited URL that grants permission for a specific upload operation.

* **B. Use EFS mount in the browser** – Not applicable; Amazon EFS is for mounting file systems on compute instances, not web browsers.
* **C. Make the S3 bucket public** – This is insecure and exposes the bucket to unauthorized access.
* **D. Embed root AWS credentials in the client** – Extremely insecure and strongly discouraged.

</details>

## Question #17

A global enterprise wants both encryption for traffic across the internet and a low-latency private connection for bulk transfer. Which TWO options describe a hybrid connectivity solution?

A. Use AWS Direct Connect for dedicated private connectivity  
B. Use Route 53 to encrypt traffic  
C. Use a VPN connection (IPSec) over the internet for encrypted backup/failover  
D. Use CloudFront to replace Direct Connect  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answers: A. Use AWS Direct Connect for dedicated private connectivity and C. Use a VPN connection (IPSec) over the internet for encrypted backup/failover**

**Explanation:**
A hybrid connectivity solution commonly combines multiple AWS networking services:

* **AWS Direct Connect** provides a dedicated private network connection between on-premises environments and AWS, ideal for high-throughput, low-latency bulk data transfer.
* **AWS Site-to-Site VPN (IPSec over the internet)** provides encrypted connectivity over the public internet and is often used as a secure backup or failover option when Direct Connect is unavailable.

Why the others are incorrect:

* **Route 53** is a DNS service and does not provide encryption or network connectivity.
* **CloudFront** is a content delivery network and does not replace Direct Connect for hybrid connectivity.

</details>

## Question #18

A serverless API using Lambda occasionally experiences increased latency on first request after idle. What is the likely cause?

A. S3 consistency issue  
B. CloudFront misconfiguration  
C. Lambda cold start (initialization overhead)  
D. Route 53 propagation delay  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. Lambda cold start (initialization overhead)**

**Explanation:**
When an AWS Lambda function has not been invoked for a period of time, AWS may need to initialize a new execution environment before handling a request. This is known as a **cold start**, and it can introduce additional latency on the first request after idle time.

* **S3 consistency issue** – Not applicable; S3 provides strong read-after-write consistency for most operations.
* **CloudFront misconfiguration** – Would affect caching and content delivery, not Lambda initialization latency.
* **Route 53 propagation delay** – Relates to DNS changes, not per-request latency in Lambda execution.

</details>

---



