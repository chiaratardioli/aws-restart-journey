# AWS Storage Services

This summary provides an overview of the core AWS storage services as detailed in the architectural sources for the Solutions Architect Associate (SAA-C03) exam.

## 1. Amazon S3 (Simple Storage Service)
S3 is a foundational **object storage** service, not a file system. It stores data in buckets as a flat key-value store, where each object consists of a key (path), value (data up to 5 TB), metadata, and optional version ID.

### Storage Classes & Cost Optimisation
*   **S3 Standard:** The default for frequently accessed data.
*   **Intelligent-Tiering:** Automatically moves objects between tiers to save costs when access patterns are unknown or changing, with no retrieval fees or minimum duration penalties.
*   **Infrequent Access (Standard-IA/One Zone-IA):** Cheaper storage for rapid retrieval of infrequent data, but carries a **30-day minimum duration** charge and retrieval fees.
*   **S3 Glacier (Flexible Retrieval/Deep Archive):** Lowest-cost options for long-term archives (90 to 180-day minimums) with retrieval times ranging from minutes to 12 hours.
*   **Lifecycle Rules:** Automate cost management by defining **Transition Actions** (moving to cheaper classes) and **Expiration Actions** (permanent deletion) after set periods.

### Data Protection & Security
*   **Versioning:** Protects against accidental deletion by keeping multiple copies. A "delete" on a versioned bucket only adds a **delete marker**; previous versions remain intact and billable.
*   **MFA Delete:** Requires MFA from the root account to permanently delete versions or suspend versioning.
*   **Access Control:** Use **Bucket Policies** (resource-based) or **IAM Policies** (identity-based). An **explicit Deny always wins**.
*   **Block Public Access:** A top-level safety override that disables public permissions at the account or bucket level.

### Encryption Options
*   **SSE-S3:** Default encryption using AWS-managed keys.
*   **SSE-KMS:** Provides a full **audit trail** in CloudTrail. Cross-account access requires permissions on both the S3 bucket policy and the KMS key policy.
*   **SSE-C:** Customer-provided keys; AWS does not store the key, and HTTPS is mandatory.

## 2. Amazon EBS (Elastic Block Store)
EBS provides block-level storage for EC2 instances and is **AZ-locked**, meaning a volume and its instance must reside in the same Availability Zone.

### Volume Types
*   **gp3:** The modern default SSD; allows independent tuning of IOPS and throughput.
*   **io1/io2:** High-performance SSDs supporting **Multi-Attach** (up to 16 instances), which requires a **cluster-aware file system** to prevent data corruption.
*   **st1/sc1:** Low-cost HDD options for sequential workloads; these **cannot be used as boot volumes**.

### Backups & Migration
*   **Snapshots:** Incremental, point-in-time backups stored at the **Region level**.
*   **Migration Pattern:** To move an instance to another region: **Stop instance → Create AMI (includes snapshot) → Copy AMI → Launch**.
*   **DLM:** The **Data Lifecycle Manager** automates the creation and retention of snapshots at scale.

## 3. Shared File Systems
### Amazon EFS
A fully managed, elastic **NFS** file system for **Linux-only** workloads. It supports simultaneous access across multiple AZs and automatically scales capacity.

### Amazon FSx
A family of purpose-built managed file systems:
*   **FSx for Windows File Server:** Supports SMB protocol, Active Directory, and Windows-native features.
*   **FSx for Lustre:** High-performance parallel file system for HPC and ML, featuring native S3 integration.
*   **FSx for NetApp ONTAP:** Supports NFS, SMB, and iSCSI protocols simultaneously.
*   **FSx for OpenZFS:** Managed OpenZFS for migrations from on-premises ZFS infrastructure.

## 4. Migration & Hybrid Connectivity
*   **Snow Family:** Physical devices (Snowcone, Snowball Edge, Snowmobile) for **offline migration** when internet bandwidth makes online transfer impractical (>1 week).
*   **AWS Transfer Family:** Managed endpoints for **SFTP, FTPS, FTP, and AS2** that move files directly to S3 or EFS without changing client-side workflows.
*   **AWS DataSync:** An agent-based service for **automated bulk movement** or scheduled sync between on-premises and AWS (S3, EFS, FSx).
*   **AWS Storage Gateway:** Provides continuous hybrid access via virtual appliances:
    *   **S3 File Gateway:** NFS/SMB interface to S3.
    *   **Volume Gateway:** Presents iSCSI block volumes; **Stored Mode** keeps all data local with cloud backup, while **Cached Mode** keeps primary data in S3 with a local cache.
    *   **Tape Gateway:** Replaces physical tape libraries with a virtual library (VTL) backed by S3/Glacier.
