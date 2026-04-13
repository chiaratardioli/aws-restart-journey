# Build Your VPC and Launch a Web Server

In this lab, I will use Amazon Virtual Private Cloud (VPC) to create my own VPC and add additional components to build a customized network 
for a Fortune 100 customer. I will also create security groups for my EC2 instance. I will then configure and customize an EC2 instance to 
run a web server and launch it into the VPC that matches the customer diagram shown below.

![Web Server Architecture](./images/NF-07-architecture.png)

## Task 1: Create your VPC

I use the VPC Wizard to create a VPC, an internet gateway, and two subnets in a single Availability Zone. An internet gateway is a VPC component 
that allows communication between instances in my VPC and the internet.

After creating the VPC, I add subnets. Each subnet resides entirely within one Availability Zone and cannot span zones. If a subnet’s traffic is routed 
to an internet gateway, it is known as a public subnet. If a subnet does not have a route to the internet gateway, it is known as a private subnet.

The wizard also creates a NAT gateway, which is used to provide internet connectivity to EC2 instances in private subnets.

![VPC Configuration](./images/NF-07-vpc-configuration-1.png)

![VPC Configuration](./images/NF-07-vpc-configuration-2.png)

![VPC Configuration](./images/NF-07-vpc-create.png)

![VPC Details](./images/NF-07-vpc-details.png)

## Task 2: Create additional subnets

I create two additional subnets in a second Availability Zone. This option is useful for creating resources in multiple Availability Zones to provide high availability.

## Task 3: Associate the subnets and add routes

## Task 4: Create a VPC security group

## Task 5: Launch a web server instance

## Conclusion
- I created a virtual private cloud (VPC)
- I created subnets
- I configured a security group
- I launched an Amazon Elastic Compute Cloud (Amazon EC2) instance into a VPC

## Additional resources
- [What is Amazon VPC?](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)
