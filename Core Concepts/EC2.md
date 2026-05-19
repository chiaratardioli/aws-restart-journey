# AWS EC2 (Elastic Compute Cloud)

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

### Main Instance Families

| Family                | Description                              |
| --------------------- | ---------------------------------------- |
| General Purpose       | Balanced compute, memory, and networking |
| Compute Optimized     | High-performance processors              |
| Memory Optimized      | Large memory workloads                   |
| Storage Optimized     | High disk throughput                     |
| Accelerated Computing | GPU-based workloads                      |

### vCPU

A **vCPU (virtual CPU)** represents a thread of a physical CPU core and measures processing power.
### Common use cases

* Web hosting
* APIs and backend services
* Databases
* Development/test environments
* Machine learning workloads
* Big data processing
* Gaming servers

### Pricing model

EC2 uses pay-as-you-go pricing:

* **On-Demand** → pay by usage
* **Reserved Instances / Savings Plans** → cheaper long-term commitment
* **Spot Instances** → discounted unused capacity
* **Dedicated Hosts** → isolated physical servers

### Advantages

* Highly scalable
* Fast provisioning
* Global availability
* Flexible configurations
* Integrates with other AWS services

### Drawbacks

* Can become expensive if unmanaged
* Requires system administration knowledge
* Misconfiguration can create security risks

### Example workflow

1. Choose an AMI (e.g., Ubuntu Linux)
2. Select instance type (e.g., t3.micro)
3. Configure networking/security
4. Launch instance
5. Connect via SSH or RDP
6. Deploy your application

### Analogy

Think of EC2 as:

> “Renting computers from AWS by the hour instead of buying your own servers.”

Official documentation: [Amazon EC2 Documentation](https://docs.aws.amazon.com/ec2/?utm_source=chatgpt.com)
