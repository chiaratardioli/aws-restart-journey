## Mock Exam

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


