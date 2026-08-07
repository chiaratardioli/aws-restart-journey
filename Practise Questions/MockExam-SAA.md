# Mock Exam: Amazon Solution Architect Associate

## Question #1

Praesignis is planning their VPC architecture for a new project. They need to accommodate 1,000 EC2 instances in the production subnet, with room to grow to 2,000. The VPC CIDR is **10.0.0.0/16**. The Solutions Architect must choose an appropriate subnet CIDR block for the production subnet.

Which subnet CIDR block provides enough IP addresses while minimising waste?

A. 10.0.0.0/22 (1,019 usable IP addresses)  
B. 10.0.0.0/24 (251 usable IP addresses)  
C. 10.0.0.0/16 (65,531 usable IP addresses)  
D. 10.0.0.0/21 (2,046 usable IP addresses)

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: D. 10.0.0.0/21 (2,046 usable IP addresses)**

**Explanation:**

A **/21 subnet** provides **2,048 total IP addresses**, with **2,043 usable** in standard networking. In AWS, **5 IP addresses are reserved** in every subnet, leaving **2,043 usable IP addresses** (commonly rounded to about **2,046** in exam questions). This is sufficient to support the current requirement of **1,000 EC2 instances** while allowing growth to **2,000 instances**, with minimal unused address space.

- **10.0.0.0/22** provides approximately **1,019 usable IP addresses**, which is enough for the current deployment but does not support the planned growth to 2,000 instances.
- **10.0.0.0/24** provides only **251 usable IP addresses**, making it far too small.
- **10.0.0.0/16** provides over **65,000 usable IP addresses**, which is far more than required and wastes a large portion of the VPC address space.

</details>


## Question #2

Praesignis must comply with a regulatory requirement that all data stored in Amazon S3 must be encrypted, and the encryption keys must be managed and rotated exclusively by the Praesignis security team using their own key material. The solution must integrate with AWS services and provide audit trails of all key usage.

Which S3 encryption option satisfies these requirements?

A. SSE-C (Server-Side Encryption with Customer-Provided Keys)  
B. Client-Side Encryption using a self-managed library before uploading to S3  
C. SSE-S3 (Server-Side Encryption with Amazon S3 Managed Keys)  
D. SSE-KMS using Customer Managed Keys (CMKs) in AWS KMS

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: D. SSE-KMS using Customer Managed Keys (CMKs) in AWS KMS**

**Explanation:**

The **SSE-KMS using Customer Managed Keys (CMKs)** option best satisfies the requirements because it allows Praesignis to manage encryption keys while integrating seamlessly with AWS services. Customer Managed Keys support key rotation, fine-grained access control through IAM and key policies, and comprehensive audit trails of key usage through **AWS CloudTrail**. Additionally, AWS KMS supports importing customer-provided key material (BYOK), allowing the Praesignis security team to use their own cryptographic material while benefiting from KMS integration.

- **SSE-C (Server-Side Encryption with Customer-Provided Keys)** requires customers to provide the encryption key with every request. Although the customer controls the keys, it lacks the centralized key management, AWS service integration, and auditing capabilities required.
- **Client-Side Encryption** provides full control over encryption and keys but requires the application to manage encryption, decryption, and key lifecycle, making integration and auditing more complex.
- **SSE-S3 (Server-Side Encryption with Amazon S3 Managed Keys)** uses AWS-managed keys, so the customer cannot exclusively manage or rotate the encryption keys, making it unsuitable for the stated regulatory requirements.

</details>


## Question #11

Praesignis is deploying a distributed big data processing cluster using Apache Kafka across **48 EC2 broker instances**. The architecture must ensure that no two broker instances share the same underlying physical server, so that a hardware failure impacts the fewest brokers possible. The cluster must be able to span multiple Availability Zones.

Which EC2 Placement Group strategy should the Solutions Architect choose?

A. Spread Placement Group  
B. Cluster Placement Group  
C. Partition Placement Group  
D. Dedicated Host with affinity rules

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. Partition Placement Group**

**Explanation:**

A **Partition Placement Group** is designed for large distributed and replicated workloads such as **Apache Kafka**, **Hadoop**, **Cassandra**, and **HDFS**. It places instances into **logical partitions**, ensuring that each partition does not share the same underlying hardware. If a rack or hardware failure occurs, only the instances in the affected partition are impacted. Partition placement groups can also **span multiple Availability Zones**, making them ideal for highly available distributed systems.

- **Spread Placement Group** ensures that each instance runs on distinct hardware, but it is intended for **small numbers of critical instances** (up to seven per Availability Zone) and is not suitable for a 48-instance Kafka cluster.
- **Cluster Placement Group** places instances close together on the same hardware to provide **low latency and high network throughput**, but this increases the risk that a hardware failure affects many instances.
- **Dedicated Host with affinity rules** provides dedicated physical servers for licensing and compliance purposes but does not distribute instances across separate hardware to minimise the impact of hardware failures.

</details>


## Question #15

Praesignis's project dashboard performs repeated identical database queries for project summaries that change infrequently (updated once per hour). These queries are slow (2–3 seconds each) and are executed thousands of times per minute, causing significant load on the RDS database. The team wants to add caching to eliminate redundant database calls.

Which **TWO** caching strategies and AWS services should the Solutions Architect recommend? (Select TWO.)

A. Migrate the RDS database to DynamoDB with DAX for automatic microsecond caching  
B. Implement a Lazy Loading (Cache-Aside) strategy using Amazon ElastiCache for Redis  
C. Set an appropriate TTL (Time-to-Live) of 1 hour on cached query results to match the data update frequency  
D. Enable RDS Query Cache for automatic query result caching at the database level  
E. Use Write-Through caching to update the cache every time the database is written to

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answers: B. Implement a Lazy Loading (Cache-Aside) strategy using Amazon ElastiCache for Redis**  
**and**  
**C. Set an appropriate TTL (Time-to-Live) of 1 hour on cached query results to match the data update frequency**

**Explanation:**

A **Lazy Loading (Cache-Aside)** strategy with **Amazon ElastiCache for Redis** is the most common caching pattern for read-heavy applications. When a request is made, the application first checks Redis. If the data is not in the cache (a cache miss), it retrieves the data from Amazon RDS and stores it in Redis for future requests. This significantly reduces database load and improves response times.

Since the project summaries are updated only **once per hour**, configuring a **TTL (Time-to-Live) of one hour** ensures that cached data remains fresh while minimizing unnecessary database queries. When the TTL expires, the next request automatically refreshes the cache.

- **A. DynamoDB with DAX** is designed specifically for **DynamoDB**, not Amazon RDS, and migrating databases solely for caching is unnecessary.
- **D. RDS Query Cache** is not a feature available across Amazon RDS engines, and modern database engines such as MySQL 8 have removed query caching entirely.
- **E. Write-Through caching** is useful when data is updated frequently and the cache must always remain current. In this scenario, where data changes only once per hour and the workload is primarily read-heavy, **Cache-Aside with an appropriate TTL** is the simpler and more efficient solution.

</details>


## Question #16

Praesignis is expanding globally and needs their Aurora MySQL database to be available for reads in **us-east-1**, **eu-west-1**, and **ap-southeast-1** with **sub-second replication lag**. In the event of a regional disaster, the database must be promotable to a fully writable cluster in the affected Region within **1 minute**.

Which Aurora feature enables this global read capability with fast regional failover?

A. AWS Database Migration Service (DMS) with ongoing CDC replication across Regions  
B. Aurora cross-region Read Replicas  
C. Amazon Aurora Global Database  
D. DynamoDB Global Tables with a DynamoDB-Aurora proxy

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. Amazon Aurora Global Database**

**Explanation:**

**Amazon Aurora Global Database** is specifically designed for globally distributed applications. It replicates data across multiple AWS Regions with **typical replication latency of less than one second**, allowing low-latency local reads worldwide. In the event of a regional outage, a secondary Region can be **promoted to a standalone read/write cluster in typically under one minute**, meeting the stated disaster recovery requirement.

- **AWS Database Migration Service (DMS)** is intended for database migration and continuous replication, but it is not designed to provide the low-latency global reads and rapid failover capabilities of Aurora Global Database.
- **Aurora cross-region Read Replicas** provide cross-Region replication but generally have higher replication lag and slower failover than Aurora Global Database.
- **DynamoDB Global Tables** are a feature of Amazon DynamoDB and cannot be used to provide global replication for an Aurora MySQL database.

</details>


## Question #19

Praesignis's project reporting module runs complex read-heavy SQL queries that are consuming significant CPU on the primary RDS MySQL instance, causing slowness for write operations in the production application. The Solutions Architect must offload the reporting queries without affecting the production application.

Which solution should be implemented?

A. Enable Performance Insights on the primary RDS instance to optimise queries  
B. Create an RDS Read Replica and direct reporting queries to the Read Replica endpoint  
C. Enable RDS Multi-AZ and direct reporting queries to the standby instance  
D. Upgrade the primary RDS instance to a larger instance type

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. Create an RDS Read Replica and direct reporting queries to the Read Replica endpoint**

**Explanation:**

An **RDS Read Replica** is designed to offload **read-heavy workloads** from the primary database. Reporting and analytics queries can be directed to the Read Replica, reducing CPU utilization on the primary instance while allowing it to focus on handling production write operations. This improves application performance without impacting availability.

- **Performance Insights** helps identify and analyze database performance bottlenecks, but it does not offload reporting queries or reduce load on the primary database.
- **RDS Multi-AZ** provides high availability and automatic failover. The standby instance is **not accessible for read traffic** and cannot be used for reporting workloads.
- **Upgrading the primary instance** increases available resources but does not separate reporting traffic from production workloads and is a less efficient, more expensive solution than using a Read Replica.

</details>


## Question #26

Praesignis is migrating a Windows-based application to Amazon EC2 that currently uses a Windows file server with the **SMB protocol** for shared storage. The application requires **full NTFS compatibility**, **Active Directory (AD) integration** for access control, and support for Windows-specific features such as **Shadow Copies**.

Which AWS managed file storage service is **MOST appropriate**?

A. Amazon EFS (Elastic File System)  
B. Amazon FSx for Windows File Server  
C. Amazon FSx for Lustre  
D. AWS Storage Gateway, File Gateway with SMB enabled

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. Amazon FSx for Windows File Server**

**Explanation:**

**Amazon FSx for Windows File Server** is a fully managed Windows-native file system that supports the **SMB protocol**, **NTFS permissions**, **Active Directory integration**, **Distributed File System (DFS)**, and **Volume Shadow Copy Service (VSS)**. It is specifically designed for Windows applications that require full compatibility with traditional Windows file servers.

- **Amazon EFS** is a managed **NFS** file system intended primarily for Linux workloads and does not provide native SMB, NTFS, or Windows-specific features.
- **Amazon FSx for Lustre** is a high-performance file system optimized for HPC, machine learning, and analytics workloads, not Windows file sharing.
- **AWS Storage Gateway File Gateway** provides hybrid access to Amazon S3 using SMB or NFS but is intended for hybrid storage scenarios rather than replacing a Windows file server with full NTFS and Active Directory capabilities.

</details>


## Question #28

Praesignis has an on-premises engineering archive that stores **50 TB of CAD files** on a local NAS server. The team rarely accesses files older than **6 months** but needs them available on demand. They want to extend this storage to **Amazon S3** while maintaining on-premises access using their existing **file-sharing protocols (NFS/SMB)**, with frequently accessed files cached locally.

Which AWS Storage Gateway configuration addresses this use case?

A. AWS Storage Gateway: Volume Gateway (Stored mode)  
B. AWS Storage Gateway: File Gateway  
C. AWS DataSync with a daily schedule to synchronise the NAS to S3  
D. AWS Storage Gateway: Tape Gateway

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. AWS Storage Gateway: File Gateway**

**Explanation:**

**AWS Storage Gateway File Gateway** is designed for hybrid file storage scenarios where on-premises applications need access to files using standard **NFS and SMB protocols** while storing the underlying data in **Amazon S3**. It provides a local cache for frequently accessed files, while less frequently accessed files remain stored cost-effectively in S3 and can be retrieved when needed.

- **Volume Gateway (Stored mode)** provides block storage using iSCSI and is designed for applications that require block-level volumes, not file-based access through NFS/SMB.
- **AWS DataSync** is used for automated data transfer and migration between storage systems, but it does not provide a continuously mounted file share with local caching.
- **Tape Gateway** is intended for virtual tape library (VTL) workloads and backup/archive use cases, not active file sharing with SMB/NFS access.

</details>


## Question #35

Praesignis is deploying a content management system where thousands of EC2 instances access a shared Amazon EFS file system simultaneously. The workload involves a very large number of small file operations (metadata operations), and latency is highly sensitive. The team notices that EFS performance degrades under high concurrency.

Which EFS performance mode should be selected?

A. Provisioned Throughput Mode  
B. Max I/O Performance Mode  
C. General Purpose Performance Mode  
D. Bursting Throughput Mode

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. Max I/O Performance Mode**

**Explanation:**

**Max I/O Performance Mode** is designed for workloads that require **very high levels of concurrent access** from thousands of clients. It optimizes Amazon EFS for applications with high aggregate throughput and large numbers of file operations, making it suitable for distributed workloads where scalability is more important than the lowest possible latency.

- **Provisioned Throughput Mode** allows customers to configure throughput independently from the amount of data stored, but it does not address high-concurrency metadata operation performance.
- **General Purpose Performance Mode** provides the lowest latency and is recommended for most workloads, but it has concurrency limits that make it less suitable for thousands of simultaneous clients performing intensive file operations.
- **Bursting Throughput Mode** controls throughput based on the amount of data stored and does not change the EFS performance mode used to handle high-concurrency access.

</details>


## Question #51

Praesignis must comply with a financial regulation requiring that audit log files stored in S3 cannot be modified or deleted by anyone, including AWS account administrators, for a minimum of **7 years**.

Which S3 feature enforces this immutability requirement?

A. S3 Versioning with MFA Delete enabled  
B. S3 Bucket Policy with a deny statement for `s3:DeleteObject` for all principals  
C. S3 Object Lock in Compliance mode with a 7-year retention period  
D. S3 Object Lock in Governance mode with a 7-year retention period

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: C. S3 Object Lock in Compliance mode with a 7-year retention period**

**Explanation:**

**Amazon S3 Object Lock in Compliance mode** provides **WORM (Write Once, Read Many)** protection, ensuring that objects cannot be deleted or modified during the configured retention period. In Compliance mode, **no user, including the AWS account root user or administrators, can override or remove the retention settings**, making it suitable for strict regulatory requirements such as financial audit retention rules.

- **S3 Versioning with MFA Delete enabled** protects against accidental deletion of object versions but does not provide the required regulatory-grade immutability because authorized users can still manage versions.
- **S3 Bucket Policy with a deny statement for `s3:DeleteObject`** can prevent deletion attempts but administrators with sufficient permissions may modify the policy and bypass the restriction.
- **S3 Object Lock in Governance mode** provides retention protection but allows users with special permissions (`s3:BypassGovernanceRetention`) to override the retention settings, making it unsuitable when even administrators must be prevented from deleting objects.

</details>


## Question #59

Praesignis's IoT-enabled construction sites generate **millions of sensor readings per minute** (temperature, vibration, pressure). The team needs a database that can ingest this **time-series data at high speed**, automatically expire old data based on time, and run **time-series-specific analytical queries efficiently**. The solution must be **fully managed and serverless**.

Which AWS database service is purpose-built for this workload?

A. Amazon Timestream  
B. Amazon RDS PostgreSQL with the TimescaleDB extension  
C. Amazon Redshift with time-based partitioning  
D. Amazon DynamoDB with TTL (Time-to-Life) configured

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: A. Amazon Timestream**

**Explanation:**

**Amazon Timestream** is a purpose-built, fully managed **serverless time-series database** designed for high-volume IoT and operational workloads. It can ingest millions of time-series events per minute, automatically manages data lifecycle policies through memory and magnetic storage tiers, supports automatic data expiration, and provides built-in functions optimized for time-series analysis.

- **Amazon RDS PostgreSQL with TimescaleDB** can support time-series workloads, but it requires database management and scaling decisions. It is not a fully managed serverless time-series solution.
- **Amazon Redshift with time-based partitioning** is optimized for large-scale analytics and data warehousing, not high-frequency time-series ingestion from IoT devices.
- **Amazon DynamoDB with TTL** can automatically remove expired items, but it is a key-value database and does not provide native time-series analytical capabilities.

</details>


## Question #61

Praesignis runs a data analytics platform on EC2. When instances in their Auto Scaling Group are set to terminate (during scale-in), the team needs to ensure that any **in-flight data processing jobs are completed** and results are uploaded to **Amazon S3** before the instance is actually terminated. The completion time varies between **5 and 20 minutes**.

Which Auto Scaling feature enables this graceful shutdown behaviour?

A. Enable Instance Protection on all instances in the group  
B. Auto Scaling Lifecycle Hooks with a Terminating:Wait state  
C. Configure the Auto Scaling Group cooldown period to 20 minutes  
D. Increase the health check grace period to 20 minutes

<details>
<summary><strong>Click to reveal answer</strong></summary>

**Correct answer: B. Auto Scaling Lifecycle Hooks with a Terminating:Wait state**

**Explanation:**

**Amazon EC2 Auto Scaling Lifecycle Hooks** allow instances to pause during scaling activities so applications can perform custom actions before the instance enters its final state. A **Terminating:Wait** lifecycle hook places an instance into a waiting state during scale-in, giving running processes time to complete tasks such as finishing data processing jobs, saving results, and uploading files to Amazon S3 before termination.

- **Instance Protection** prevents selected instances from being terminated during scale-in, but it does not provide a mechanism for completing in-progress tasks before eventual termination.
- **Auto Scaling cooldown periods** control how frequently scaling activities can occur after a scaling event. They do not delay instance termination or allow applications to perform shutdown tasks.
- **Health check grace periods** provide time for newly launched instances to become healthy before health checks begin. They do not apply to terminating instances or graceful shutdown workflows.

</details>
