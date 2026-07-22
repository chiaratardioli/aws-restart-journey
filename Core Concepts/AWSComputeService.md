# EC2, Auto Scaling & Container Services

This section covers:

- **EC2 Advanced**
  - Amazon Machine Images (AMIs)
  - EC2 instance types
  - Placement groups
  - EC2 pricing models

- **Auto Scaling & Load Balancing**
  - Auto Scaling Groups (ASGs)
  - Scaling policies
  - Application, Network, and Gateway Load Balancers

- **Application Architecture**
  - Loosely coupled architectures
  - Microservices
  - Decoupling patterns

- **Disaster Recovery**
  - Backup and Restore
  - Pilot Light
  - Warm Standby
  - Multi-Site Active-Active

- **Multi-Account Strategy**
  - AWS Organizations
  - Service Control Policies (SCPs)
  - AWS Control Tower

- **Container & Managed Compute Services**
  - Amazon ECS
  - ECS Anywhere
  - Amazon EKS
  - AWS Fargate
  - Elastic Beanstalk
  - AWS Batch

---

# Part I. EC2 Advanced: AMIs, Instance Types & Placement Groups

## 1. Amazon Machine Images (AMIs)

An **AMI** is a blueprint used to launch EC2 instances.  
It contains:

- Operating system
- Installed software
- Configuration settings
- Storage volume information

<details>
<summary><strong>Key AMI Facts</strong></summary>

- AMIs are **Region-specific**.
- To use an AMI in another Region → **copy the AMI first**.
- A copied AMI receives a **new AMI ID**.
- Custom AMIs reduce EC2 launch time.
- Custom AMIs are useful with **Auto Scaling Groups** because new instances start faster.

</details>

**Exam keyword:**  
✅ Faster EC2 startup → **Custom AMI**

---

# 2. EC2 Instance Families

| Family | Purpose | Common Use Cases |
|---|---|---|
| **T** | Burstable, low-cost compute | Dev/test, small websites |
| **M** | Balanced CPU and memory | Web servers, applications |
| **C** | High CPU performance | Batch processing, HPC, gaming |
| **R / X** | Large memory capacity | SAP HANA, Redis, in-memory databases |
| **I** | High IOPS and low latency storage | NoSQL, OLTP databases |
| **P / G / Inf / Trn** | GPU and ML acceleration | AI, ML, video rendering |

<details>
<summary><strong>Instance Family Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| High CPU workload | **C family** |
| Batch processing | **C family** |
| In-memory database | **R / X family** |
| SAP HANA / Redis | **R / X family** |
| GPU / ML training | **P / G family** |
| High IOPS storage | **I family** |
| Variable CPU and low cost | **T family** |

</details>

---

# 3. EC2 Placement Groups

Placement Groups control how EC2 instances are physically placed in AWS infrastructure.

| Type | Goal | Best For |
|---|---|---|
| **Cluster** | Lowest latency | HPC, tightly coupled applications |
| **Spread** | Maximum fault isolation | Critical instances, databases |
| **Partition** | Large-scale isolation | Kafka, Hadoop, Cassandra |

<details>
<summary><strong>Placement Group Decision Guide</strong></summary>

### Cluster
- Instances are placed close together.
- Same Availability Zone.
- Lowest latency.
- No hardware fault isolation.

**Use for:**
- HPC
- Big data processing
- Fast inter-node communication

---

### Spread
- Each instance is placed on different hardware.
- Maximum protection from hardware failures.
- Maximum 7 instances per AZ.

**Use for:**
- Critical applications
- Primary databases
- ZooKeeper

---

### Partition
- Instances are separated into logical partitions.
- Supports hundreds of instances.
- Provides rack-level isolation.

**Use for:**
- Hadoop
- Kafka
- Cassandra
- HBase

</details>

**Exam keywords:**

- Lowest latency → **Cluster**
- Cannot share hardware failure → **Spread**
- Distributed big data at scale → **Partition**

---

# 4. EC2 Pricing Models

| Pricing Model | Best For |
|---|---|
| **On-Demand** | Short-term or unpredictable workloads |
| **Reserved Instances** | Stable workloads with long-term usage |
| **Spot Instances** | Fault-tolerant workloads |
| **Savings Plans** | Flexible long-term compute commitment |
| **Dedicated Host** | BYOL and compliance requirements |
| **Dedicated Instance** | Hardware isolation |

---

<details>
<summary><strong>Pricing Model Exam Rules</strong></summary>

### On-Demand
✅ Maximum flexibility  
❌ Highest price  

Use for:
- Testing
- Temporary workloads
- Unknown demand

---

### Reserved Instances
✅ Long-term discount  
✅ Predictable workloads  

Use for:
- Production servers running continuously

---

### Spot Instances
✅ Up to 90% discount  
❌ Can be interrupted  

Use for:
- Batch processing
- ML training
- Rendering
- CI/CD jobs

Never use for:
- Databases
- Stateful applications
- Critical live traffic

---

### Savings Plans
✅ Flexible discount model  
✅ Covers:
- EC2
- Lambda
- Fargate

---

### Dedicated Host
✅ Entire physical server dedicated to one customer  
✅ Required for BYOL licensing

Examples:
- Oracle
- Windows Server
- SQL Server

---

### Dedicated Instance
✅ Hardware isolation  
❌ No physical host control  
❌ Not designed for BYOL

</details>

---

# Final EC2 Exam Cheat Sheet

| Requirement | Correct Choice |
|---|---|
| Preconfigured EC2 template | **AMI** |
| Faster Auto Scaling launches | **Custom AMI** |
| CPU-intensive workload | **C family** |
| Memory-intensive workload | **R/X family** |
| GPU workload | **P/G family** |
| High IOPS storage | **I family** |
| Lowest network latency | **Cluster Placement Group** |
| Maximum hardware isolation | **Spread Placement Group** |
| Large distributed systems | **Partition Placement Group** |
| Cheapest interruptible compute | **Spot Instances** |
| Existing server licenses | **Dedicated Host** |



## Part II. Auto Scaling Groups & Load Balancers

# 1. Auto Scaling Groups (ASGs)

An **Auto Scaling Group (ASG)** manages a collection of EC2 instances.

It automatically:

- Launches new instances when demand increases.
- Terminates instances when demand decreases.
- Replaces unhealthy instances.
- Maintains the desired number of instances.

---

## ASG Core Concepts

| Component | Description |
|---|---|
| **Launch Template** | Blueprint containing AMI, instance type, security groups, and user data |
| **Minimum Capacity** | Lowest number of instances that must always run |
| **Desired Capacity** | Target number of instances ASG tries to maintain |
| **Maximum Capacity** | Highest number of instances allowed |

---

<details>
<summary><strong>ASG Important Rules</strong></summary>

- ASGs should span multiple Availability Zones.
- ASG automatically replaces unhealthy instances.
- During scale-out, ASG launches new instances.
- During scale-in, ASG removes instances.
- Load Balancers distribute traffic across ASG instances.

</details>

---

# Scaling Policies

Scaling policies define:

1. **When to scale**
2. **How much to scale**

| Policy | Purpose | Example |
|---|---|---|
| **Target Tracking** | Maintain a target metric | Keep CPU at 50% |
| **Step Scaling** | Different scaling actions based on alarm size | Add 2 instances at 70%, add 5 at 90% |
| **Scheduled Scaling** | Scale at predictable times | Add instances every Friday evening |
| **Predictive Scaling** | Uses ML forecasting | Scale before expected traffic |

---

<details>
<summary><strong>Scaling Policy Exam Keywords</strong></summary>

| Question Keyword | Answer |
|---|---|
| Maintain average CPU at 60% | **Target Tracking** |
| Increase capacity before known event | **Scheduled Scaling** |
| Scale aggressively based on load level | **Step Scaling** |
| Predict future demand | **Predictive Scaling** |

</details>

---

# 2. Elastic Load Balancing (ELB)

Load Balancers distribute incoming traffic across multiple targets.

They work together with ASGs:

```

Users
↓
Load Balancer
↓
Auto Scaling Group
↓
EC2 Instances

```

---

# Application Load Balancer (ALB)

## Layer 7 — HTTP/HTTPS

ALB makes routing decisions based on application information.

It supports:

- URL paths
- Host headers
- Query strings
- HTTP methods

Targets:

- EC2
- ECS containers
- EKS
- Lambda
- IP addresses

Best for:

- Web applications
- REST APIs
- Microservices
- Container workloads

**Keyword:**

> HTTP routing / microservices → ALB

---

# Network Load Balancer (NLB)

## Layer 4 — TCP/UDP/TLS

NLB is designed for:

- Extremely high performance.
- Millions of requests per second.
- Ultra-low latency.

Features:

- Static IP addresses.
- Elastic IP support.
- Preserves client source IP.

Best for:

- Gaming
- Financial applications
- IoT
- TCP workloads

**Keyword:**

> Static IP + ultra-low latency → NLB

---

# Gateway Load Balancer (GWLB)

## Layer 3 — Security Appliances

GWLB routes traffic through third-party network appliances.

Examples:

- Firewalls
- IDS/IPS systems
- Security inspection tools

Uses:

- GENEVE protocol

**Keyword:**

> Insert firewall/security inspection → GWLB

---

# Load Balancer Decision Guide

| Requirement | Answer |
|---|---|
| HTTP/HTTPS routing | **ALB** |
| Microservices | **ALB** |
| Containers | **ALB** |
| TCP/UDP traffic | **NLB** |
| Static IP requirement | **NLB** |
| Lowest latency networking | **NLB** |
| Firewall inspection | **GWLB** |

---

# Final Exam Memory

| Requirement | Solution |
|---|---|
| Automatically add/remove EC2 instances | **Auto Scaling Group** |
| Keep CPU at a target value | **Target Tracking** |
| Predictable traffic spike | **Scheduled Scaling** |
| HTTP path-based routing | **ALB** |
| TCP high performance | **NLB** |
| Security appliance insertion | **GWLB** |


# Part III. Loosely Coupled Architectures & Decoupling

# 1. Microservices Architecture

A **microservices architecture** breaks a large application into smaller, independent services.

Each service:

- Has a specific business responsibility.
- Can be deployed independently.
- Can scale independently.
- Communicates through APIs or messaging.

---

## Monolith vs Microservices

| Monolithic Application | Microservices |
|---|---|
| Single codebase | Multiple independent services |
| One failure can impact the whole application | Failures are isolated |
| Harder to scale individual components | Each service scales independently |
| Large deployments | Smaller independent deployments |

---

<details>
<summary><strong>Microservices Communication Patterns</strong></summary>

## Synchronous Communication

A service calls another service and waits for a response.

Examples:

- API Gateway
- Application Load Balancer
- Lambda

Use when:

- Immediate response is required.

Example:

```

Frontend
↓
Payment Service
↓
Response

```

---

## Asynchronous Communication

A service sends a message and continues without waiting.

Examples:

- Amazon SQS
- Amazon SNS
- Amazon EventBridge

Use when:

- Services should operate independently.
- Temporary failures should not block processing.

Example:

```

Order Service
↓
SQS
↓
Worker Service

```

</details>

---

# 2. Decoupling Patterns

A tightly coupled system has components that depend heavily on each other.

If one component becomes slow or unavailable, other components are affected.

A decoupled architecture introduces buffers and independent communication channels.

---

# Amazon SQS (Simple Queue Service)

## Message Queue Service

SQS stores messages until a consumer processes them.

Benefits:

- Absorbs traffic spikes.
- Prevents message loss.
- Allows services to process independently.

Example:

```

Website
↓
SQS Queue
↓
Processing Workers

```

---

## SQS Queue Types

| Queue Type | Feature |
|---|---|
| **Standard Queue** | High throughput, at-least-once delivery |
| **FIFO Queue** | Ordered processing, exactly-once processing |

---

<details>
<summary><strong>SQS Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| Decouple application components | **SQS** |
| Backend slower than frontend | **SQS** |
| Buffer messages | **SQS** |
| Preserve order | **FIFO Queue** |
| Process messages asynchronously | **SQS** |

</details>

---

# Amazon SNS (Simple Notification Service)

## Publish / Subscribe Messaging

SNS sends one message to multiple subscribers.

Common use:

- Fan-out architecture.
- Notifications.
- Event distribution.

---

# SNS + SQS Fan-Out Pattern

This is one of the most common AWS architecture patterns.

Advantages:

- Multiple systems receive the same event.
- Each system processes independently.
- One consumer failure does not affect others.

---

<details>
<summary><strong>SNS Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| Send one event to many systems | **SNS** |
| Publish/subscribe model | **SNS** |
| Fan-out architecture | **SNS + SQS** |

</details>

---

# Amazon EventBridge

## Event Routing Service

EventBridge receives events and routes them based on rules.

Sources:

- AWS services
- SaaS applications
- Custom applications

Features:

- Advanced event filtering.
- Event routing.
- Scheduled events.

Example:

```

AWS Service Event
↓
EventBridge Rule
↓
Lambda / SQS / Step Functions

```

---

# SQS vs SNS vs EventBridge

| Service | Main Purpose |
|---|---|
| **SQS** | Queue messages and decouple workloads |
| **SNS** | Broadcast messages to multiple subscribers |
| **EventBridge** | Intelligent event routing and filtering |

---

<details>
<summary><strong>Final Decision Guide</strong></summary>

| Requirement | Solution |
|---|---|
| Application processes tasks asynchronously | **SQS** |
| Backend cannot keep up with requests | **SQS** |
| Send one message to multiple systems | **SNS** |
| Fan-out pattern | **SNS + SQS** |
| React to AWS service events | **EventBridge** |
| Complex event filtering | **EventBridge** |

</details>

---

# Architecture Memory Map

```

Need a buffer?
↓
SQS

Need many subscribers?
↓
SNS

Need intelligent event routing?
↓
EventBridge

```

---

# Exam Summary

✅ Microservices = small independent services  
✅ Synchronous = API call and wait  
✅ Asynchronous = message-based communication  
✅ SQS = queue and decouple  
✅ SNS = broadcast events  
✅ SNS + SQS = fan-out pattern  
✅ EventBridge = event routing with rules


----

# Part IV. Disaster Recovery Strategies

# 1. Disaster Recovery Concepts

Disaster Recovery (DR) defines how an application recovers after a failure.

Two key metrics determine the required DR solution:

| Metric | Meaning |
|---|---|
| **RPO (Recovery Point Objective)** | Maximum acceptable amount of data loss |
| **RTO (Recovery Time Objective)** | Maximum acceptable downtime |

---

## RPO vs RTO

<details>
<summary><strong>Understanding RPO and RTO</strong></summary>

### RPO — Data Loss Tolerance

RPO defines how much data can be lost after a disaster.

Example:

- RPO = 15 minutes
- The application can lose up to 15 minutes of data.

Lower RPO requires:

- More frequent backups.
- Data replication.
- Continuous synchronization.

---

### RTO — Recovery Time Requirement

RTO defines how quickly the application must become available again.

Example:

- RTO = 1 hour
- The application must recover within one hour.

Lower RTO requires:

- More infrastructure prepared in advance.
- Faster recovery mechanisms.

</details>

---

# DR Strategy Comparison

| Strategy | Cost | RTO | RPO | Description |
|---|---|---|---|---|
| **Backup & Restore** | Lowest | Hours | Hours | Restore systems from backups after failure |
| **Pilot Light** | Low | Minutes | Minutes | Keep core services running and scale during recovery |
| **Warm Standby** | Medium | Minutes | Seconds | Maintain a reduced but fully functional environment |
| **Multi-Site Active-Active** | Highest | Seconds | Near Zero | Run multiple active production environments |

---

# 1. Backup and Restore

## Cheapest DR Strategy

The application stores backups and restores resources only after a disaster.

Characteristics:

✅ Lowest cost  
✅ Simple to implement  
❌ Slowest recovery time  

Best for:

- Non-critical workloads.
- Applications where downtime is acceptable.
- Long recovery windows.

---

# 2. Pilot Light

## Core Services Always Available

The most important components remain running, usually:

- Databases
- Essential infrastructure

During a disaster:

- Additional resources are launched.
- The environment is scaled.
- Traffic is redirected.

Characteristics:

✅ Faster than Backup & Restore  
✅ Lower cost than Warm Standby  
❌ Requires additional setup during recovery  

Best for:

- Critical databases.
- Applications requiring minutes of recovery.

---

# 3. Warm Standby

## Reduced but Functional Environment

A smaller version of the production environment runs continuously in the recovery location.

Characteristics:

✅ Faster recovery than Pilot Light  
✅ Application components are already available  
❌ Higher cost than Pilot Light  

Best for:

- Business-critical applications.
- Applications requiring faster recovery.

---

# 4. Multi-Site Active-Active

## Maximum Availability

The application runs fully in multiple locations at the same time.

Characteristics:

✅ Lowest RTO  
✅ Near-zero data loss  
✅ Immediate failover capability  
❌ Most expensive option  

Best for:

- Mission-critical applications.
- Systems requiring minimal downtime.

---

# DR Strategy Decision Guide

<details>
<summary><strong>Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| Lowest cost DR solution | **Backup & Restore** |
| Hours of downtime acceptable | **Backup & Restore** |
| Database running in DR environment | **Pilot Light** |
| Scale application servers after disaster | **Pilot Light** |
| Reduced environment already running | **Warm Standby** |
| Business-critical application | **Warm Standby** |
| Near-zero downtime | **Multi-Site Active-Active** |
| Near-zero data loss | **Multi-Site Active-Active** |

</details>

---

# DR Cost vs Recovery Speed

| Strategy | Cost | Recovery Speed |
|---|---|---|
| Backup & Restore | Lowest | Slowest |
| Pilot Light | Low | Faster |
| Warm Standby | Medium | Fast |
| Multi-Site Active-Active | Highest | Fastest |

---

# Final DR Memory Map

| Requirement | Solution |
|---|---|
| Backups only | **Backup & Restore** |
| Core systems ready, scale during recovery | **Pilot Light** |
| Smaller complete environment running | **Warm Standby** |
| Full production environment available | **Multi-Site Active-Active** |

---

# Key Exam Rule

**Lower RTO and lower RPO always require higher cost.**

The faster the recovery and the less data lost, the more infrastructure must already be running.

---

# Part V.AWS Organizations & Control Tower

# 1. AWS Organizations

AWS Organizations allows companies to centrally manage multiple AWS accounts.

It provides:

- Centralized account management.
- Consolidated billing.
- Security governance.
- Policy enforcement across accounts.

---

# Why Use Multiple AWS Accounts?

A multi-account strategy provides:

| Benefit | Description |
|---|---|
| **Security isolation** | Limits the impact of security issues |
| **Cost separation** | Tracks spending by team or environment |
| **Environment separation** | Separates production, development, and testing |
| **Governance** | Applies organization-wide policies |

---

# Organizational Units (OUs)

Organizational Units are logical groups of AWS accounts.

Examples:

- Production
- Development
- Security
- Sandbox

<details>
<summary><strong>OU Rules</strong></summary>

- Accounts are grouped inside OUs.
- OUs can contain other OUs.
- Policies can be applied at the OU level.
- Each account belongs to one organization.

</details>

---

# Consolidated Billing

AWS Organizations combines billing for all accounts.

Benefits:

- One central bill.
- Shared volume discounts.
- Easier cost management.

---

# Service Control Policies (SCPs)

SCPs are governance policies used to control what AWS accounts can do.

They define the maximum available permissions for accounts.

---

## SCP Important Rules

<details>
<summary><strong>Critical SCP Facts</strong></summary>

### SCPs Do NOT Grant Permissions

SCPs only restrict permissions.

A user still requires:

- IAM permissions
- Resource permissions

Example:

An SCP allows EC2 usage, but an IAM policy is still required to launch EC2 instances.

---

### Explicit Deny Always Wins

If an SCP denies an action:

- IAM policies cannot override it.
- Even administrators cannot perform the denied action.

---

### Management Account Exception

SCPs do not apply to the AWS Organizations management account.

They apply to:

- Member accounts
- Organizational Units

</details>

---

# SCP Exam Examples

| Requirement | Solution |
|---|---|
| Prevent resources outside approved Regions | SCP |
| Block a service across all accounts | SCP |
| Enforce organization-wide restrictions | SCP |

---

# AWS Organizations vs IAM

| AWS Organizations | IAM |
|---|---|
| Controls multiple accounts | Controls users and roles |
| Applies organization policies | Grants permissions |
| Uses SCPs | Uses IAM policies |

---

# 2. AWS Control Tower

AWS Control Tower provides an automated way to create and govern a multi-account AWS environment.

It is built on top of:

- AWS Organizations
- AWS IAM Identity Center
- AWS Config
- CloudTrail

---

# Control Tower Features

| Feature | Purpose |
|---|---|
| **Landing Zone** | Preconfigured multi-account environment |
| **Guardrails** | Security and compliance controls |
| **Account Factory** | Automated account creation |
| **Centralized logging** | Collects security logs |

---

# Landing Zone

A Landing Zone is a secure, best-practice AWS environment created automatically.

It typically includes:

- Management account
- Log Archive account
- Audit account

---

# Guardrails

Guardrails enforce governance rules.

Two types exist:

| Type | Purpose |
|---|---|
| **Preventive Guardrails** | Block unwanted actions |
| **Detective Guardrails** | Detect configuration violations |

---

## Preventive vs Detective Guardrails

<details>
<summary><strong>Guardrail Examples</strong></summary>

### Preventive Guardrails

Uses:

- Service Control Policies (SCPs)

Example:

> Prevent users from creating resources in unauthorized Regions.

---

### Detective Guardrails

Uses:

- AWS Config rules

Example:

> Detect resources that do not meet security requirements.

</details>

---

# Account Factory

Account Factory automatically creates new AWS accounts with:

- Required security settings.
- Network configuration.
- Logging enabled.
- Governance controls applied.

Useful for:

- Large organizations.
- Teams needing self-service account creation.

---

# AWS Organizations vs Control Tower

| Requirement | Answer |
|---|---|
| Manage multiple AWS accounts | **AWS Organizations** |
| Consolidated billing | **AWS Organizations** |
| Apply SCP restrictions | **AWS Organizations** |
| Automated multi-account setup | **Control Tower** |
| Create Landing Zone | **Control Tower** |
| Automated account provisioning | **Control Tower Account Factory** |

---

# Exam Decision Guide

<details>
<summary><strong>Common Exam Keywords</strong></summary>

| Keyword | Answer |
|---|---|
| "Prevent accounts from using a Region" | **SCP** |
| "Restrict actions across accounts" | **SCP** |
| "Central account management" | **AWS Organizations** |
| "Automated landing zone" | **Control Tower** |
| "Best practice multi-account environment" | **Control Tower** |
| "Create accounts automatically" | **Account Factory** |

</details>

---

# Final Memory Map

| Service | Remember |
|---|---|
| **AWS Organizations** | Manage accounts and apply governance |
| **SCP** | Restrict permissions, never grant |
| **Control Tower** | Automated multi-account setup |
| **Guardrails** | Prevent and detect non-compliance |
| **Account Factory** | Create governed AWS accounts quickly |

---

# Part VI. Container & Managed Compute Services

# 1. Compute Evolution on AWS

AWS compute services move from more infrastructure management to less management:

| Service | Management Level |
|---|---|
| **EC2** | Manage servers, OS, and applications |
| **Containers (ECS/EKS)** | Manage applications and containers |
| **Fargate** | Manage containers, AWS manages infrastructure |
| **Lambda** | Manage only code |

---

# 2. Amazon ECS (Elastic Container Service)

Amazon ECS is AWS's managed container orchestration service.

It runs and manages Docker containers.

A container deployment requires:

- Container image
- Task Definition
- Cluster
- Service

---

# ECS Task Definition

A Task Definition describes how a container should run.

It defines:

- Docker image
- CPU and memory requirements
- Environment variables
- Networking settings
- IAM roles

---

# ECS Launch Types

| Launch Type | Who Manages Infrastructure? | Best For |
|---|---|---|
| **ECS on EC2** | Customer manages EC2 instances | More control and customization |
| **ECS on Fargate** | AWS manages infrastructure | Serverless containers |

---

# ECS on EC2

The customer manages:

- EC2 instances
- Operating system
- Cluster capacity

Advantages:

✅ More control  
✅ Custom instance types  
✅ Can optimize costs  

Use when:

- Specific EC2 configurations are required.
- GPU instances are needed.
- Full infrastructure control is important.

---

# ECS on Fargate

Fargate removes the need to manage servers.

AWS manages:

- EC2 infrastructure
- Operating system
- Scaling of compute capacity

The customer manages:

- Container image
- Application configuration

Advantages:

✅ No server management  
✅ Pay only for task resources  
✅ Automatic infrastructure management  

---

# ECS Anywhere

ECS Anywhere extends ECS outside AWS.

It allows containers to run on:

- On-premises servers
- Virtual machines
- External infrastructure

The ECS agent connects external machines to ECS.

---

<details>
<summary><strong>ECS Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| AWS-native container orchestration | **ECS** |
| Serverless containers | **ECS with Fargate** |
| Need control over EC2 instances | **ECS on EC2** |
| Run ECS containers on-premises | **ECS Anywhere** |

</details>

---

# 3. Amazon EKS (Elastic Kubernetes Service)

Amazon EKS is AWS's managed Kubernetes service.

AWS manages the Kubernetes control plane.

The customer manages:

- Worker nodes (unless using Fargate)
- Applications
- Kubernetes configuration

---

# ECS vs EKS

| ECS | EKS |
|---|---|
| AWS-native container service | Kubernetes-based |
| Simpler to operate | More flexible |
| Less Kubernetes knowledge required | Requires Kubernetes expertise |
| Best for AWS-native applications | Best for Kubernetes workloads |

---

<details>
<summary><strong>When to Choose ECS or EKS</strong></summary>

### Choose ECS when:

- Starting a new AWS container application.
- Simplicity is preferred.
- The team does not use Kubernetes.
- Deep AWS integration is required.

---

### Choose EKS when:

- Existing Kubernetes workloads exist.
- Kubernetes compatibility is required.
- Using Helm, kubectl, or Kubernetes operators.
- Running hybrid or multi-cloud Kubernetes environments.

</details>

---

# 4. AWS Fargate

AWS Fargate is a serverless compute engine for:

- ECS
- EKS

Fargate removes the need to manage EC2 instances.

The customer specifies:

- CPU
- Memory
- Container image

AWS handles:

- Infrastructure provisioning
- Patching
- Scaling compute resources

---

# Fargate Pricing

Billing is based on:

- vCPU allocated
- Memory allocated
- Duration of task execution

Best for:

- Variable workloads.
- Applications without a need for server control.

---

# 5. AWS Elastic Beanstalk

Elastic Beanstalk is AWS's Platform-as-a-Service (PaaS).

Developers upload application code, and Beanstalk manages:

- EC2 instances
- Load balancers
- Auto Scaling Groups
- CloudWatch monitoring
- Optional RDS databases

---

# Elastic Beanstalk Important Point

Elastic Beanstalk is **not serverless**.

It creates AWS resources underneath.

The customer still has access to:

- EC2 instances
- Security Groups
- Load Balancers
- RDS settings

---

<details>
<summary><strong>Elastic Beanstalk Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| Deploy application without managing infrastructure | **Elastic Beanstalk** |
| PaaS solution | **Elastic Beanstalk** |
| Need access to underlying EC2 resources | **Elastic Beanstalk** |
| Fully serverless execution | **Lambda** |

</details>

---

# 6. AWS Batch

AWS Batch is a fully managed service for running batch computing workloads.

It automatically manages compute resources based on job requirements.

Suitable for:

- Large-scale processing.
- Parallel jobs.
- Long-running workloads.

Examples:

- Genomics analysis.
- Financial modelling.
- Video rendering.
- Machine learning preprocessing.

---

# AWS Batch Features

| Feature | Description |
|---|---|
| Managed compute environment | Automatically provisions resources |
| Job queues | Organizes workload execution |
| EC2 and Spot support | Optimizes cost |
| Dynamic scaling | Adds/removes compute automatically |

---

# AWS Batch vs Lambda

| Lambda | AWS Batch |
|---|---|
| Event-driven functions | Large-scale batch jobs |
| Maximum 15-minute execution | Long-running jobs |
| No custom infrastructure | Managed compute environments |
| Lightweight processing | Heavy computation |

---

# Managed Compute Decision Guide

<details>
<summary><strong>Exam Keywords</strong></summary>

| Requirement | Answer |
|---|---|
| Docker containers on AWS | **ECS** |
| Kubernetes workloads | **EKS** |
| Serverless containers | **Fargate** |
| Run containers on-premises | **ECS Anywhere** |
| Deploy application without infrastructure management | **Elastic Beanstalk** |
| Thousands of batch jobs | **AWS Batch** |
| Event-driven short tasks | **Lambda** |

</details>

---

# Final Container Memory Map

| Service | Remember |
|---|---|
| **ECS** | AWS-native container orchestration |
| **EKS** | Managed Kubernetes |
| **Fargate** | Serverless container compute |
| **ECS Anywhere** | Containers outside AWS |
| **Elastic Beanstalk** | PaaS with infrastructure access |
| **AWS Batch** | Large-scale batch processing |

---

# Final Exam Rules

✅ ECS = AWS containers  
✅ EKS = Kubernetes  
✅ Fargate = Serverless compute for ECS/EKS  
✅ Elastic Beanstalk = Managed application deployment, not serverless  
✅ AWS Batch = Large compute jobs with dynamic scaling  
