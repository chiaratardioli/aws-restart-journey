# AWS Well-Architected Framework

The **AWS Well-Architected Framework** is a collection of AWS best practices and design principles used to build secure, reliable, 
efficient, cost-effective, and sustainable cloud architectures. It provides a consistent method for evaluating AWS workloads, 
identifying architectural risks, and implementing improvements based on proven cloud design patterns.

The framework evaluates workloads through **design principles**, **six pillars**, **review questions**, and **lenses** for specific 
technologies or industries. During a Well-Architected Review, architects answer questions for each pillar to identify risks and 
recommended improvements, helping organizations continuously optimize their cloud environments.

### Main Components

- **Design Principles** – High-level best practices that guide architectural decisions within each pillar.
- **Six Pillars** – Operational Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.
- **Questions** – A structured set of questions used to evaluate workloads against the best practices of each pillar.
- **Lenses** – Specialized guidance that extends the framework for specific workloads, technologies, or industries (for example,
- Serverless, Machine Learning, IoT, and Financial Services).

### Key Benefits

- Evaluate architectures using AWS best practices.
- Identify and mitigate architectural risks.
- Make informed design decisions.
- Build scalable, secure, and resilient workloads.
- Continuously improve cloud architectures over time.
- Apply specialized guidance through AWS Well-Architected Lenses.

### The Six Pillars

The framework is organized around **six pillars**, each focusing on a key aspect of cloud architecture. By reviewing workloads against 
these pillars, organizations can make informed architectural decisions, reduce operational risks, improve performance, and continuously 
optimize their systems as business requirements evolve.

- **Operational Excellence** – Run and monitor workloads effectively while continuously improving processes.
- **Security** – Protect systems, data, and resources through identity management, detection, and defense mechanisms.
- **Reliability** – Design workloads to recover quickly from failures and adapt to changing demand.
- **Performance Efficiency** – Use computing resources efficiently and scale to meet workload requirements.
- **Cost Optimization** – Minimize unnecessary costs while maximizing business value.
- **Sustainability** – Reduce the environmental impact of cloud workloads by optimizing resource usage.

## AWS Well-Architected Tool (AWS WA Tool)

The **AWS Well-Architected Framework** defines the best practices and principles for designing cloud architectures. The **AWS Well-Architected Tool (AWS WA Tool)** is the AWS service that helps apply those principles by reviewing workloads against the framework. It provides a structured way to assess architectures, identify risks, and create improvement plans based on AWS recommendations.

The AWS WA Tool guides architects through a **Well-Architected Review**, where a workload is evaluated by answering a series of questions for each of the six pillars. The tool identifies **High-Risk Issues (HRIs)** and **Medium-Risk Issues (MRIs)**, tracks improvements over time using **milestones**, and supports **lenses** for specialized workloads such as Serverless, Machine Learning, IoT, and Financial Services.

### Key Features

- **Workload Reviews** – Evaluate AWS workloads against the Well-Architected Framework.
- **Question-Based Assessment** – Answer pillar-specific questions to identify architectural risks.
- **Risk Identification** – Highlights High-Risk Issues (HRIs) and Medium-Risk Issues (MRIs).
- **Milestones** – Capture snapshots of a workload to monitor improvements over time.
- **Lenses** – Apply additional best practices for specific technologies and industries.
- **Improvement Plans** – Receive AWS recommendations to remediate identified risks.
- **Pillar Prioritization** – Customize the priority of the six pillars according to business requirements.

> **Exam Tip:** The **Well-Architected Framework** defines the best practices, while the **AWS Well-Architected Tool** helps assess workloads against those practices and track continuous improvements.

## AWS Architectural Best Practices

The **AWS Architectural Best Practices** are a set of recommendations based on the **AWS Well-Architected Framework**. They help architects design workloads that are secure, reliable, scalable, cost-effective, and operationally efficient throughout their entire lifecycle. Rather than being a one-time checklist, these practices should be applied continuously as applications evolve and business requirements change.

Successful architectures begin with careful planning. Before selecting AWS services, architects should gather both **functional requirements** (what the system must do) and **non-functional requirements** (how well the system should perform, such as security, availability, scalability, and performance). These requirements guide architectural decisions and ensure the final solution meets both business and technical objectives.

### AWS Best Practices

- **Start with business requirements** – Understand the customer's goals before designing the architecture.
- **Design for failure** – Assume components will fail and build systems that can recover automatically.
- **Implement security at every layer** – Apply the principle of least privilege, encrypt data, and protect workloads throughout the stack.
- **Automate wherever possible** – Use Infrastructure as Code (IaC), automation, and managed deployments to reduce manual work.
- **Use managed services** – Prefer AWS managed services to reduce operational overhead and improve reliability.
- **Monitor and measure** – Collect metrics, logs, and alarms to continuously improve workloads.
- **Stay current** – Regularly adopt new AWS features, services, and best practices.

### Functional vs Non-Functional Requirements

| Functional Requirements | Non-Functional Requirements |
|--------------------------|-----------------------------|
| Describe **what** the system does | Describe **how well** the system performs |
| Define business features | Define quality attributes |
| Specified by the customer | Often defined by architects or technical teams |
| Mandatory for the application | Usually desirable but may affect cost |
| Examples: user login, order processing, file upload | Examples: security, availability, scalability, performance, latency |

> **Exam Tip:** AWS exam questions often describe **non-functional requirements** (high availability, low latency, security, scalability, disaster recovery, or cost optimization). The correct answer is usually the AWS architecture that best satisfies these quality attributes rather than simply providing the requested functionality.
