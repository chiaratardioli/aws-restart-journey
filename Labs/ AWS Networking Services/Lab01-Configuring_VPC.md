# Configuring a VPC

Amazon Virtual Private Cloud (Amazon VPC) gives the ability to provision a logically isolated section of the 
Amazon Web Services (AWS) Cloud where AWS resources can be launched in a virtual network. You have complete 
control over your virtual networking environment, including selecting your IP address ranges, creating subnets, 
and configuring route tables and network gateways.

In this lab, I will build a virtual private cloud (VPC) and other network components required to deploy resources, 
such as an Amazon Elastic Compute Cloud (Amazon EC2) instance.

![VPC Architecture](./images/lab01-architecture.png)

## Task 1: Creating a VPC

## Task 2: Creating subnets

1. Creating a public subnet
2. Creating a private subnet

## Task 3: Creating an internet gateway

## Task 4: Configuring route tables

## Task 5: Launching a bastion server in the public subnet

## Task 6: Creating a NAT gateway

## Optional challenge: Testing the private subnet

1. Launching an instance in the private subnet
2. Logging in to the bastion server
3. Logging in to the private instance
4. Testing the NAT gateway

## Conclusions
- I created a VPC with a private and public subnet, an internet gateway, and a NAT gateway.
- I configure droute tables associated with subnets to local and internet-bound traffic by using an internet gateway and a NAT gateway.
- I launched a bastion server in a public subnet.
- I used a bastion server to log in to an instance in a private subnet.
- I completed the optional challenge section and created an Amazon EC2 instance in a private 
subnet and connect to it through the bastion server.
