# Create Subnets and Allocate IP addresses in an Amazon Virtual Private Cloud (Amazon VPC)

In this lab, I will investigate a customer’s environment and analyze their request to provide a clear walkthrough 
of their infrastructure. I will learn how to launch a VPC, determine the appropriate CIDR block and IP range to assign, 
and guide the customer through the process of building a VPC in AWS. This lab will help reinforce best practices for 
designing and deploying secure, properly structured virtual networks.

## Scenario
My role is a cloud support engineer at AWS. During my shift, a customer from a startup company requests assistance regarding 
a networking issue within their AWS infrastructure. The following is the email and an attachment regarding their architecture:

Ticket from the customer

>Hello, Cloud Support!
>
>I'm new to AWS, and I need help setting up a VPC. Can you please help me through the setup process? I would like to build only
>the VPC part and would like to make it look something like the following picture. Can you help me ensure  I have around 15,000
>private IP addresses in this VPC available?  I would also like the VPC IPv4 CIDR block to be a 192.x.x.x. I don't remember which
>is a private range though. Can you confirm that? I would also like to allocate at least 50 IP addresses for the public subnet.
>
>Thanks!
>
>Paulo Santos
>
>Startup Owner

![VPC Subnets and IP addresses Architecture](./images/NF-03-architecture.png)

Figure: In the customer's VPC architecture, the customer needs approximately 15,000 IP addresses for their Seattle office 
headquarters and 50 IP addresses for their operations department, which will be in the public subnet.

## Task 1: Investigate the customer's needs

## Task 2: Solution Design

## Task 3: Send the response to the customer

## Conclusion
- I summarized the customer scenario
- I created a Amazon Virtual Private Cloud (Amazon VPC) with subnets and IP addresses
- I familiarized with the Amazon Web Services (AWS) Management Console
- I developped a solution to the customer's issue in this lab
- I summarized and described my findings

## Additional resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
- [IP Addressing in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-ip-addressing.html)
- [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918)
- [VPC CIDR](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html#add-cidr-block-restrictions)
- [Subnet calculator](https://www.subnet-calculator.com/)
