# EC2 (Elastic Compute Cloud)

Amazon Web Services **EC2 (Elastic Compute Cloud)** is a virtual server service from Amazon Web Services that lets you run applications in the cloud without managing physical hardware.

### In simple terms

EC2 gives you **rentable computers on demand**. You choose:

* CPU and memory size
* Operating system
* Storage
* Networking
* Geographic region

Then AWS launches a virtual machine called an **instance**.

### Important Concepts I Learned

* **Instance** → the virtual server
* **AMI (Amazon Machine Image)** → template used to create instances
* **Instance types** → hardware configurations (compute resources) such as CPU, memory, and storage
* Instance types are grouped into **instance families** optimized for different workloads.
* **EBS** → persistent storage disks attached to instances
* **Security Groups** → virtual firewalls controlling inbound/outbound traffic
* **Elastic IP** → static public IP address
* **Auto Scaling** → automatically add/remove instances based on demand
* **Load Balancer** → distributes traffic across multiple instances

---

### EC2 Instance Types

AWS provides hundreds of **EC2 instance types**, grouped into **instance families**. Each family is designed and optimized for a specific workload pattern.

#### Main EC2 Instance Families

| Instance Family | Description | Common Use Cases |
|---|---|---|
| **General Purpose (M, T)** | Balanced combination of compute, memory, and networking | Web servers, application servers, development/test environments |
| **Compute Optimized (C)** | High CPU performance with a higher compute-to-memory ratio | Batch processing, scientific computing, gaming servers, media processing |
| **Memory Optimized (R, X, z)** | Large amounts of RAM for memory-intensive applications | In-memory databases, caching, real-time analytics |
| **Storage Optimized (I, D, H)** | High-performance local storage with high IOPS and low latency | Databases, data warehouses, distributed file systems |
| **Accelerated Computing (P, G, Inf, Trn)** | GPU or specialized hardware acceleration | Machine learning, AI inference, video rendering, HPC |

#### General Purpose Instances (M and T families)

General Purpose instances provide a balance between **CPU, memory, and networking resources**.

**T-Series (Burstable Performance)**
- Uses a **CPU credit system** to handle occasional bursts of high CPU usage.
- Best for workloads with variable or unpredictable CPU demand.
- Cost-effective for applications that do not require constant maximum performance.

**Use cases:**
- Development and testing environments
- Small websites
- Low-traffic applications
- Applications with occasional CPU spikes

**M-Series (Balanced Workloads)**
- Provides a balanced ratio of CPU, memory, and networking.
- Considered the standard "workhorse" EC2 family.

**Use cases:**
- Web servers
- Application servers
- Enterprise applications
- Small to medium-sized databases

### Compute Optimized Instances (C Family)

Compute Optimized instances provide a **high CPU-to-memory ratio**.

They are designed for applications where processing power is more important than memory capacity.

**Use cases:**
- Batch processing
- Media transcoding
- High-performance web servers
- Scientific simulations
- Gaming servers
- Machine learning inference

**Keyword:**  
➡️ **CPU-intensive workload = C family**


#### Memory Optimized Instances (R, X, z Families)

Memory Optimized instances provide a **large amount of RAM** compared to CPU resources.

They are ideal when applications need to store large datasets in memory for fast access.

**Use cases:**
- SAP HANA
- Redis
- Memcached
- In-memory databases
- Real-time big data analytics
- Large-scale caching

**Keyword:**  
➡️ **In-memory database or large dataset = R/X family**


#### Storage Optimized Instances (I, D, H Families)

Storage Optimized instances are designed for workloads requiring:

- Very high disk throughput
- High IOPS
- Low-latency local storage
- NVMe SSD performance

**Use cases:**
- OLTP databases
- NoSQL databases using local storage
- Data warehouses
- Distributed file systems
- Log processing systems

**Keyword:**  
➡️ **High IOPS or local disk performance = I family**

### Accelerated Computing Instances (P, G, Inf, Trn Families)

Accelerated Computing instances use GPUs or specialized AWS hardware to speed up specific workloads.

**Use cases:**
- Machine learning model training
- AI inference
- Video rendering
- Graphics processing
- High-performance computing (HPC)

Examples:
- **P family** → GPU-based machine learning training
- **G family** → Graphics and inference workloads
- **Inf family** → Machine learning inference using AWS Inferentia
- **Trn family** → Machine learning training using AWS Trainium

**Keyword:**  
➡️ **GPU or ML workload = Accelerated Computing**


#### 📝 Exam Tips — EC2 Instance Family Keywords

| Requirement in Question | Choose |
|---|---|
| High CPU workload, batch processing, scientific computing | **C family (Compute Optimized)** |
| In-memory database, SAP HANA, Redis, Memcached | **R/X family (Memory Optimized)** |
| Machine learning training, GPU workloads, video rendering | **P/G/Inf/Trn family (Accelerated Computing)** |
| High random IOPS, local NVMe storage, NoSQL databases | **I family (Storage Optimized)** |
| Development/testing, variable CPU usage, cost-sensitive workloads | **T family (Burstable General Purpose)** |
| Balanced web/app workloads | **M family (General Purpose)** |

#### Quick Memory Trick

- **T = Tiny bursts** → Burstable workloads  
- **M = Medium balance** → General purpose  
- **C = Compute** → CPU-heavy workloads  
- **R = RAM** → Memory-heavy workloads  
- **I = IOPS** → Storage performance  
- **P/G = Processing Graphics** → GPU acceleration  

---

### vCPU

A **vCPU (virtual CPU)** represents a thread of a physical CPU core and measures processing power.

#### Common use cases

* Web hosting
* APIs and backend services
* Databases
* Development/test environments
* Machine learning workloads
* Big data processing
* Gaming servers

---

### Pricing model

EC2 uses pay-as-you-go pricing:

* **On-Demand** → pay by usage
* **Reserved Instances / Savings Plans** → cheaper long-term commitment
* **Spot Instances** → discounted unused capacity
* **Dedicated Hosts** → isolated physical servers

#### Advantages

* Highly scalable
* Fast provisioning
* Global availability
* Flexible configurations
* Integrates with other AWS services

#### Drawbacks

* Can become expensive if unmanaged
* Requires system administration knowledge
* Misconfiguration can create security risks

#### Example workflow

1. Choose an AMI (e.g., Ubuntu Linux)
2. Select instance type (e.g., t3.micro)
3. Configure networking/security
4. Launch instance
5. Connect via SSH or RDP
6. Deploy your application

#### Analogy

Think of EC2 as:

> “Renting computers from AWS by the hour instead of buying your own servers.”

Official documentation: [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/?utm_source=chatgpt.com)
