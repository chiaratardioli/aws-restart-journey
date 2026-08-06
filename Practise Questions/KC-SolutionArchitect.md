# Questions for AWS Solution Architect exam

## Question #1

A solutions architect is comparing Disaster Recovery (DR) strategies for an application with an **RPO of 15 minutes** and an **RTO of 1 hour**.

Which **TWO** AWS services are **MOST** relevant for achieving **continuous data replication** to meet the **15-minute RPO**?

A. AWS Backup with daily backup windows  
B. Amazon S3 Cross-Region Replication (CRR)  
C. Amazon Glacier for long-term archival storage  
D. Amazon EC2 AMI snapshots taken weekly  
E. Amazon RDS with Multi-AZ and cross-region Read Replicas  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answers: B. Amazon S3 Cross-Region Replication (CRR) and E. Amazon RDS with Multi-AZ and cross-region Read Replicas**

**Explanation:**  
A **Recovery Point Objective (RPO)** of **15 minutes** means the application can lose **no more than 15 minutes of data**. This requires **continuous or near-continuous data replication**, rather than periodic backups.

- **B. Amazon S3 Cross-Region Replication (CRR)** continuously replicates objects from one S3 bucket to another bucket in a different AWS Region, helping achieve a low RPO for S3 data.
- **E. Amazon RDS with Multi-AZ and cross-region Read Replicas** provides database replication. While **Multi-AZ** offers high availability within a Region, **cross-region Read Replicas** continuously replicate data to another Region, supporting disaster recovery with a low RPO.

**Why not the others:**
- **A. AWS Backup with daily backup windows** – Daily backups could result in up to **24 hours of data loss**, far exceeding the 15-minute RPO.
- **C. Amazon Glacier for long-term archival storage** – Designed for archival and compliance, not continuous replication or rapid disaster recovery.
- **D. Amazon EC2 AMI snapshots taken weekly** – Weekly snapshots could result in up to **one week of data loss**, making them unsuitable for a 15-minute RPO.

**Exam Tip:**  
- **RPO (Recovery Point Objective)** = Maximum acceptable **data loss** → Low RPO requires **replication**.
- **RTO (Recovery Time Objective)** = Maximum acceptable **recovery time** → Low RTO requires architectures that can be restored or failed over quickly.

</details>

## Question #2

A company's application sends messages to an Amazon SQS queue. Some messages are occasionally failing processing and causing the consumer to retry continuously, impacting performance.

What should the solutions architect configure to handle **poison-pill messages** **WITHOUT** losing them?

A. Increase the SQS message visibility timeout to prevent reprocessing  
B. Enable SQS long polling to reduce empty receives  
C. Configure a Dead Letter Queue (DLQ) with a `maxReceiveCount` threshold  
D. Switch to a FIFO queue to process messages in order  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Configure a Dead Letter Queue (DLQ) with a `maxReceiveCount` threshold**

**Explanation:**  
A **poison-pill message** is a message that repeatedly fails processing due to malformed data, invalid content, or an application error. If the message remains in the queue, consumers will continue retrying it, wasting resources and reducing overall throughput.

A **Dead Letter Queue (DLQ)** allows Amazon SQS to automatically move a message to a separate queue after it has been received a specified number of times (`maxReceiveCount`). This prevents endless retries while preserving the failed message for later inspection, troubleshooting, or reprocessing.

**Why not the others:**
- **A. Increase the SQS message visibility timeout** – This only delays when the message becomes visible again. It does not solve repeated processing failures.
- **B. Enable SQS long polling** – Long polling reduces empty responses and API calls but has no effect on poison-pill messages.
- **D. Switch to a FIFO queue** – FIFO queues guarantee message ordering and exactly-once processing, but they do not automatically handle messages that continually fail processing.

**Exam Tip:**  
- Use a **Dead Letter Queue (DLQ)** to isolate messages that cannot be processed successfully after multiple attempts.
- Configure the **`maxReceiveCount`** to control how many retries occur before the message is moved to the DLQ.
- DLQs improve application reliability by preventing failed messages from blocking or slowing down normal message processing.

</details>

## Question #3

A solutions architect is configuring an Auto Scaling Group (ASG) for a stateless web application behind an Application Load Balancer (ALB).

Which **TWO** configurations are essential to ensure that **only healthy instances receive traffic**?

A. Configure health check grace period to allow instance initialization before health checking begins  
B. Set the minimum capacity to 0 to allow full scale-in  
C. Enable ELB health checks on the Auto Scaling Group  
D. Disable termination policies to prevent accidental instance removal  
E. Attach an Elastic IP to each instance in the ASG  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answers: A. Configure health check grace period to allow instance initialization before health checking begins**  
**C. Enable ELB health checks on the Auto Scaling Group**

**Explanation:**  
To ensure that only healthy instances receive traffic, the Auto Scaling Group should work together with the Application Load Balancer.

- **A. Configure a health check grace period** – The grace period gives newly launched instances time to boot, install software, and start the application before health checks begin. Without it, instances may be marked unhealthy prematurely and terminated before they are ready.
- **C. Enable ELB health checks on the Auto Scaling Group** – This allows the ASG to use the ALB's health check results. If an instance fails the ALB health checks, the ASG automatically replaces it with a healthy instance, ensuring traffic is directed only to healthy targets.

**Why not the others:**
- **B. Set the minimum capacity to 0** – This controls scaling behavior but does not determine whether traffic is routed only to healthy instances.
- **D. Disable termination policies** – Termination policies control which instances are removed during scale-in events. Disabling them does not improve health checking or traffic routing.
- **E. Attach an Elastic IP to each instance** – Instances behind an ALB typically do not require Elastic IP addresses. The ALB handles incoming traffic and distributes it to the instances.

**Exam Tip:**  
- For Auto Scaling Groups behind an **Application Load Balancer**, always:
  - Enable **ELB health checks** on the ASG.
  - Configure an appropriate **health check grace period**.
- The ALB determines whether instances are healthy enough to receive traffic, while the ASG replaces unhealthy instances automatically.

</details>

## Question #4

A solutions architect is selecting an EC2 instance type for a high-performance relational database that requires **maximum RAM** and **low-latency access to data**.

Which EC2 instance family is **MOST** appropriate?

A. General Purpose (T-family, e.g., t3, t4g)  
B. Compute Optimized (C-family, e.g., c6i, c7g)  
C. Memory Optimized (R-family, e.g., r6g, r7i)  
D. Storage Optimized (I-family, e.g., i3, i4i)  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Memory Optimized (R-family, e.g., r6g, r7i)**

**Explanation:**  
**Memory Optimized** instances are designed for workloads that require **large amounts of RAM** and fast access to data stored in memory. High-performance relational databases, such as SAP HANA, MySQL, PostgreSQL, Oracle, and Microsoft SQL Server, often benefit from large memory capacity because more data can be cached in memory, reducing disk I/O and improving query performance.

The **R-family** provides a high memory-to-vCPU ratio, making it the best choice for memory-intensive database workloads.

**Why not the others:**
- **A. General Purpose (T-family)** – Designed for burstable workloads and balanced CPU, memory, and networking. Not suitable for demanding production databases.
- **B. Compute Optimized (C-family)** – Optimized for CPU-intensive applications such as web servers, scientific computing, and batch processing, rather than memory-intensive databases.
- **D. Storage Optimized (I-family)** – Provides high-speed local NVMe SSD storage for workloads requiring very high IOPS and low-latency local storage. While useful for some databases, the question specifically emphasizes **maximum RAM**, making the **R-family** the better choice.

**Exam Tip:**  
Remember the common EC2 instance families:

- **T** = Burstable, General Purpose
- **M** = Balanced, General Purpose
- **C** = Compute Optimized (CPU-intensive)
- **R/X/U** = Memory Optimized (large in-memory workloads)
- **I/D/H** = Storage Optimized (high IOPS and local SSD/HDD storage)
- **P/G/Trn/Inf** = Accelerated Computing (GPU/ML)

When an exam question emphasizes **large memory**, **in-memory databases**, or **caching**, the answer is usually a **Memory Optimized (R-family)** instance.

</details>

## Question #5

A company runs a **stateful gaming application** where **session data must persist across requests** and be **shared among multiple EC2 instances** in an Auto Scaling Group.

Which AWS service should store this shared session state?

A. EC2 Instance Store  
B. Amazon ElastiCache for Redis  
C. Amazon EFS (Elastic File System)  
D. Amazon DynamoDB with DAX  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: B. Amazon ElastiCache for Redis**

**Explanation:**  
**Amazon ElastiCache for Redis** is the preferred solution for storing **shared session state** in distributed applications. Redis is an in-memory data store that provides **very low latency**, making it ideal for session management, gaming leaderboards, caching, and real-time applications.

Because all EC2 instances in the Auto Scaling Group can access the same Redis cluster, users can be routed to any instance without losing their session data.

**Why not the others:**
- **A. EC2 Instance Store** – Instance store is local to a single EC2 instance and is **ephemeral**. Data is lost if the instance stops or terminates, and it cannot be shared across instances.
- **C. Amazon EFS (Elastic File System)** – EFS provides a shared file system, but it is designed for file storage rather than high-performance session management. It has higher latency than Redis.
- **D. Amazon DynamoDB with DAX** – DynamoDB is a NoSQL database, and DAX is an in-memory cache for DynamoDB. While it can store session data, it is generally not the preferred solution for fast, transient session storage compared to Redis.

**Exam Tip:**  
Choose **Amazon ElastiCache for Redis** when you see requirements such as:
- Shared user sessions
- Session persistence across multiple web or application servers
- Low-latency reads and writes
- Gaming sessions, shopping carts, or user authentication state

A common architecture is:

```text
Client
   │
Application Load Balancer
   │
Auto Scaling Group (EC2)
   │
Amazon ElastiCache for Redis
      ↑
Shared session state
```

This allows users to be served by any healthy EC2 instance without losing their session.

</details>

## Question #6

A media company wants to serve **static content globally** with the **lowest possible latency**.

Which AWS service leverages **Edge Locations** to achieve this?

A. AWS Direct Connect  
B. Amazon S3 Transfer Acceleration  
C. Amazon CloudFront  
D. AWS Global Accelerator  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. Amazon CloudFront**

**Explanation:**  
**Amazon CloudFront** is AWS's **Content Delivery Network (CDN)**. It caches content at **Edge Locations** around the world, allowing users to retrieve static content such as images, videos, JavaScript, CSS, and HTML from the location closest to them.

By serving cached content from nearby Edge Locations instead of the origin server, CloudFront reduces latency, improves performance, and decreases the load on the origin.

**Why not the others:**
- **A. AWS Direct Connect** – Provides a dedicated private network connection between an on-premises data center and AWS. It is not used for global content delivery.
- **B. Amazon S3 Transfer Acceleration** – Speeds up uploads and downloads to and from Amazon S3 by using the AWS global network, but it is designed for accelerating file transfers, not for caching and serving web content.
- **D. AWS Global Accelerator** – Improves the performance and availability of applications by routing traffic over the AWS global network to optimal endpoints. It does **not cache content** at Edge Locations like CloudFront.

**Exam Tip:**  
Remember these AWS networking services:

- **Amazon CloudFront** → **Content Delivery Network (CDN)** that caches content at **Edge Locations**.
- **AWS Global Accelerator** → Routes application traffic over the AWS global network for lower latency and higher availability.
- **Amazon S3 Transfer Acceleration** → Accelerates transfers to and from S3 using the AWS edge network.
- **AWS Direct Connect** → Dedicated private connection from on-premises to AWS.

**Keyword to remember:**  
If the question mentions **static content**, **global users**, **content caching**, or **Edge Locations**, the answer is almost always **Amazon CloudFront**.

</details>

## Question #7

A healthcare company requires a disaster recovery (DR) strategy where the **core database is always kept synchronized** with the production environment, but the **application servers in the DR site are turned off** to save costs. In a disaster, the application servers are quickly launched and scaled.

Which DR strategy does this describe?

A. Backup and Restore  
B. Warm Standby  
C. Multi-Site Active-Active  
D. Pilot Light  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: D. Pilot Light**

**Explanation:**  
A **Pilot Light** disaster recovery strategy keeps only the **critical core components**, such as the database, continuously running and synchronized in the disaster recovery (DR) Region. Other infrastructure, such as application servers, is kept **powered off or minimally provisioned** to reduce costs.

If a disaster occurs:
- The synchronized database is already available.
- Application servers are launched from templates (for example, using Auto Scaling Groups and launch templates).
- The environment is scaled up to handle production traffic.

This approach provides a good balance between **cost** and **recovery time**.

**Why not the others:**
- **A. Backup and Restore** – Only backups are maintained. Infrastructure and databases must be restored from backups during a disaster, resulting in the longest recovery times.
- **B. Warm Standby** – A complete but **scaled-down** version of the application is always running in the DR Region. Application servers are already running, unlike in a Pilot Light strategy.
- **C. Multi-Site Active-Active** – Full production environments run simultaneously in multiple Regions and actively serve traffic. This provides the fastest recovery but is the most expensive option.

**Exam Tip:**  

Know the four common AWS disaster recovery strategies:

| Strategy | Infrastructure Running? | Cost | Recovery Time |
|----------|--------------------------|------|---------------|
| **Backup & Restore** | No | Lowest | Slowest |
| **Pilot Light** | Only critical components (e.g., database) | Low | Moderate |
| **Warm Standby** | Fully functional but scaled-down environment | Medium | Fast |
| **Multi-Site Active-Active** | Full production environments in multiple Regions | Highest | Fastest |

**Memory Trick:**
- **Backup & Restore** → Save backups only.
- **Pilot Light** → Keep the **core ("pilot light")** running.
- **Warm Standby** → Keep a **small version** of the application running.
- **Active-Active** → Everything is running in multiple Regions all the time.

</details>

## Question #8

A development team wants to deploy a web application to AWS without managing the underlying infrastructure (EC2, load balancers, Auto Scaling).

They need a **fully managed Platform-as-a-Service (PaaS)** solution.

Which AWS service should they use?

A. AWS Elastic Beanstalk  
B. Amazon ECS with Fargate  
C. AWS CloudFormation  
D. AWS CodeDeploy  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. AWS Elastic Beanstalk**

**Explanation:**  
**AWS Elastic Beanstalk** is a **Platform-as-a-Service (PaaS)** offering that allows developers to deploy web applications without manually managing the underlying infrastructure.

Elastic Beanstalk automatically handles:
- EC2 instance provisioning
- Load balancer configuration
- Auto Scaling setup
- Application health monitoring
- Platform updates

Developers only need to upload their application code, and Elastic Beanstalk manages the AWS resources required to run it.

**Why not the others:**
- **B. Amazon ECS with Fargate** – Provides serverless container execution without managing EC2 instances, but it is a **container orchestration solution**, not a traditional PaaS where developers simply deploy application code.
- **C. AWS CloudFormation** – An Infrastructure as Code (IaC) service used to create and manage AWS resources through templates. It requires users to define and manage infrastructure.
- **D. AWS CodeDeploy** – A deployment automation service that helps deploy applications to EC2, Lambda, or on-premises servers. It does not provide a managed application platform.

**Exam Tip:**  

Remember AWS service categories:

- **AWS Elastic Beanstalk** → PaaS; deploy applications without managing infrastructure.
- **Amazon ECS/Fargate** → Run containers without managing servers.
- **AWS CloudFormation** → Define and provision infrastructure as code.
- **AWS CodeDeploy** → Automate application deployments.

**Keyword to remember:**  
If a question says **"developers deploy an application without managing servers, load balancers, or scaling"**, the answer is usually **AWS Elastic Beanstalk**.

</details>

## Question #9

Praesignis creates an S3 Access Point with a policy granting full read and write access to a specific application team. The underlying bucket policy, however, only grants that same team read-only access.

What level of access does the application team actually have through this access point?

A. Read-only access, since an access point policy cannot grant more access than the underlying bucket policy already allows.  
B. Full read and write access, since the access point's policy takes precedence over the bucket policy.  
C. No access at all, since access points and bucket policies must be identical to function.  
D. It depends entirely on which VPC the request originates from.  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. Read-only access, since an access point policy cannot grant more access than the underlying bucket policy already allows.**

**Explanation:**
An **Amazon S3 Access Point** provides a dedicated access path to an S3 bucket with its own resource policy. However, an access point **cannot grant permissions beyond what the underlying bucket policy allows**.

When a request is made through an access point, AWS evaluates **both**:

* The **Access Point policy**
* The **Underlying S3 bucket policy**

The effective permissions are the **intersection** of the permissions granted by both policies. Since the bucket policy only allows **read** access, write operations are denied even though the access point policy allows them.

**Why not the others:**

* **B. Full read and write access** – Incorrect. An access point policy does **not** override or take precedence over the bucket policy. Both policies must allow the requested action.
* **C. No access at all** – Incorrect. The policies do not need to be identical. The team still receives the permissions that are allowed by both policies—in this case, read-only access.
* **D. It depends entirely on which VPC the request originates from** – Incorrect. While an access point can be restricted to a VPC, VPC origin does not allow it to bypass the permissions defined by the bucket policy.

**Exam Tip:**

Remember how Amazon S3 authorization works:

* **Access Point Policy** → Provides an additional access control layer for a bucket.
* **Bucket Policy** → Defines the maximum permissions available through the bucket.
* **Effective Permissions** → Only the permissions that are allowed by **both** the Access Point policy and the bucket policy.

**Keyword to remember:**
If a question says an **S3 Access Point grants more permissions than the bucket policy**, the answer is that the user **only receives the permissions allowed by the bucket policy**. Access point policies **cannot expand** access beyond the underlying bucket.

</details>


## Question #10

A Praesignis partner integration for supply-chain document exchange specifically requires **EDI (Electronic Data Interchange)** support.

Which AWS Transfer Family protocol should be configured?

A. SFTP  
B. FTPS  
C. AS2  
D. FTP  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. AS2**

**Explanation:**
**AS2 (Applicability Statement 2)** is the AWS Transfer Family protocol specifically designed for **Electronic Data Interchange (EDI)** over the internet. It enables organizations to securely exchange business documents, such as purchase orders, invoices, and shipping notices, using encryption, digital signatures, and message acknowledgments (MDNs).

AWS Transfer Family supports AS2 to help organizations modernize B2B integrations while meeting common EDI requirements.

**Why not the others:**

* **A. SFTP** – Securely transfers files over SSH, but it does not provide the EDI-specific messaging, encryption, signing, and acknowledgment capabilities of AS2.
* **B. FTPS** – Uses SSL/TLS to secure file transfers but is a general-purpose file transfer protocol, not an EDI protocol.
* **D. FTP** – Provides basic file transfer without encryption and is not suitable for secure EDI communications.

**Exam Tip:**

Remember the AWS Transfer Family protocols:

* **AS2** → Secure **EDI/B2B** document exchange.
* **SFTP** → Secure file transfer over SSH.
* **FTPS** → Secure file transfer over SSL/TLS.
* **FTP** → Unencrypted legacy file transfer.

**Keyword to remember:**
If a question mentions **"EDI," "B2B integration," "purchase orders," "invoices,"** or **"supply-chain document exchange,"** the answer is usually **AS2**.

</details>


## Question #11

A Praesignis bucket policy explicitly grants public read access to all objects, and **Block Public Access** is fully disabled at both the account and bucket level. An external, anonymous user still cannot read a specific object.

Which layer of the access control model is the **MOST LIKELY** cause, given the other layers appear correctly configured for public access?

A. Block Public Access, since it always overrides bucket policies regardless of its configured state.  
B. The IAM policy of the anonymous user, since anonymous users always have an implicit IAM policy blocking access.  
C. An S3 Access Point policy that does not grant this specific access, since an access point policy can only narrow, never expand, what the underlying bucket policy allows.  
D. The object's storage class, since Glacier-class objects can never be made public.  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: C. An S3 Access Point policy that does not grant this specific access, since an access point policy can only narrow, never expand, what the underlying bucket policy allows.**

**Explanation:**
When accessing an object through an **Amazon S3 Access Point**, AWS evaluates both the **Access Point policy** and the **underlying bucket policy**. Even if the bucket policy allows public read access and **Block Public Access** is disabled, the request must also be permitted by the Access Point policy.

An Access Point policy can **further restrict** access but **cannot grant permissions beyond what the bucket policy allows**. Therefore, if the Access Point policy does not allow anonymous read access, the request is denied.

**Why not the others:**

* **A. Block Public Access** – Incorrect. The question explicitly states that Block Public Access is fully disabled at both the account and bucket level, so it is not preventing access.
* **B. The IAM policy of the anonymous user** – Incorrect. Anonymous users do not authenticate with IAM identities, so there is no IAM policy attached to them.
* **D. The object's storage class** – Incorrect. Storage classes such as S3 Glacier Flexible Retrieval or S3 Glacier Deep Archive do not determine whether an object can be public. Public access is controlled by S3 authorization policies, although archived objects must first be restored before they can be retrieved.

**Exam Tip:**

Remember the S3 authorization layers:

* **Block Public Access** → Can block public access regardless of policies (when enabled).
* **Bucket Policy** → Defines permissions for the bucket and its objects.
* **Access Point Policy** → Applies additional restrictions for requests through an access point.
* **Effective permissions** → A request must be allowed by **all applicable authorization layers**.

**Keyword to remember:**
If a question states that **Block Public Access is disabled** and the **bucket policy already allows public access**, but access through an **S3 Access Point** still fails, the cause is usually the **Access Point policy**, which can **restrict** but never **expand** permissions.

</details>


## Question #12

Which **TWO** of the following statements about AWS hybrid storage services are correct?

A. Tape Gateway requires backup software to be reconfigured to use a new, AWS-specific API instead of standard tape commands.  
B. DataSync can perform AWS-to-AWS transfers, such as syncing data from Amazon S3 to Amazon EFS or replicating between AWS Regions, not just on-premises-to-AWS transfers.  
C. Volume Gateway Cached Mode keeps the entire dataset locally with only an asynchronous backup to Amazon S3.  
D. S3 File Gateway translates NFS/SMB writes into native Amazon S3 API calls, and the resulting data is stored as genuine S3 objects, not a proprietary format.  
E. FSx File Gateway presents an NFS interface backed by Amazon FSx for Lustre.  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answers: B and D**

**Explanation:**

**B. DataSync can perform AWS-to-AWS transfers** – **Correct.**
AWS DataSync is not limited to migrating data from on-premises environments to AWS. It can also transfer data **between AWS storage services**, such as Amazon S3, Amazon EFS, Amazon FSx, and even across AWS Regions or AWS accounts.

**D. S3 File Gateway stores data as native S3 objects** – **Correct.**
Amazon S3 File Gateway presents standard **NFS or SMB file shares** to clients. Files written to the gateway are translated into **native Amazon S3 objects**, allowing direct access using S3 APIs and integration with other AWS services.

**Why not the others:**

* **A. Tape Gateway** – Incorrect. Tape Gateway exposes a **Virtual Tape Library (VTL)** using standard iSCSI interfaces, allowing existing backup software to continue using standard tape operations without modification.
* **C. Volume Gateway Cached Mode** – Incorrect. Cached Mode stores the **primary copy of data in Amazon S3**, while only **frequently accessed data is cached locally**. Keeping the entire dataset locally describes **Stored Mode**, not Cached Mode.
* **E. FSx File Gateway** – Incorrect. Amazon FSx File Gateway provides access to **Amazon FSx for Windows File Server** using the **SMB protocol**. It does **not** present an NFS interface and is not backed by Amazon FSx for Lustre.

**Exam Tip:**

Remember the AWS hybrid storage services:

* **AWS DataSync** → High-speed data transfers between on-premises storage and AWS, **and between AWS storage services**.
* **S3 File Gateway** → NFS/SMB access to **native Amazon S3 objects**.
* **Volume Gateway Cached Mode** → Primary data in S3, frequently accessed data cached locally.
* **Volume Gateway Stored Mode** → Primary data stored locally with asynchronous backups to S3.
* **Tape Gateway** → Virtual Tape Library (VTL) compatible with existing backup software.

**Keyword to remember:**
If a question mentions **AWS-to-AWS data transfers**, think **AWS DataSync**. If it mentions **NFS/SMB access to Amazon S3**, think **S3 File Gateway** storing **native S3 objects**.

</details>


## Question #13

A Praesignis mission-critical financial database requires **up to 200,000 IOPS** and **consistent, provisioned performance**, with the ability to attach the **same Amazon EBS volume to multiple EC2 instances** in an **active-active cluster configuration** within a single Availability Zone.

Which Amazon EBS volume type satisfies **BOTH** requirements?

A. io2 Block Express  
B. io1  
C. gp3  
D. st1  

### Answer

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct Answer: A. io2 Block Express**

**Explanation:**
**Amazon EBS io2 Block Express** is the highest-performance EBS volume type, designed for mission-critical applications such as large relational databases. It supports:

* Up to **256,000 IOPS** (depending on instance type)
* Consistent, low-latency performance
* High durability (99.999%)
* **Multi-Attach**, allowing the same volume to be attached to multiple EC2 instances simultaneously within the same Availability Zone

These capabilities make **io2 Block Express** the ideal choice for clustered applications requiring shared block storage and extremely high I/O performance.

**Why not the others:**

* **B. io1** – Provides provisioned IOPS and supports Multi-Attach, but it does **not** support the performance levels of **io2 Block Express**, making it unsuitable for workloads requiring up to 200,000 IOPS.
* **C. gp3** – A general-purpose SSD volume that offers up to **80,000 IOPS**, but it does **not** support Multi-Attach.
* **D. st1** – A throughput-optimized HDD volume intended for large, sequential workloads. It is not designed for high IOPS, low latency, or Multi-Attach.

**Exam Tip:**

Remember the key Amazon EBS volume types:

* **io2 Block Express** → Highest performance, lowest latency, **Multi-Attach**, mission-critical databases.
* **io1** → Provisioned IOPS SSD with lower maximum performance than io2 Block Express.
* **gp3** → General-purpose SSD with independent IOPS and throughput provisioning.
* **st1** → Throughput-optimized HDD for large sequential workloads.

**Keyword to remember:**
If a question mentions **200,000+ IOPS**, **consistent provisioned performance**, or **Multi-Attach for clustered applications**, the answer is almost always **io2 Block Express**.

</details>
