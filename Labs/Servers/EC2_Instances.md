# Creating Amazon EC2 Instances

In this lab I learnt the following.
- How to launch an EC2 instance by using the AWS Management Console.
- How to connect to the EC2 instance by using EC2 Instance Connect.
- How to launch an EC2 instance by using the AWS CLI.

## Overview
AWS provides multiple ways to launch Amazon Elastic Compute Cloud (Amazon EC2) instance. 
In this lab, you use the AWS Management Console to launch an EC2 instance and then use it as a bastion host to launch another EC2 instance, which will be a web server. You use EC2 Instance Connect to securely connect to the bastion host and use the AWS Command Line Interface (AWS CLI) to launch a web server instance.
The following diagram illustrates the final architecture that you will build:

![My image BWBW](./ec2-final-architecture.png)

## Task 1: Launching an EC2 Instance by using the AWS Management Console
Here I launched an EC2 instance by using the AWS Management Console. The instance is a bastion host from which I can use the AWS CLI.

1. Set **Bastion host** in Name and tags section

When I name your instance, AWS creates a key-value pair. The key for this pair is Name, and the value is the name that you enter for your EC2 instance.

2. I kept **Amazon Linux 2** as AMI

An AMI includes the following:
- A template for the root volume for the instance (for example, an operating system or an application server with applications)
- Launch permissions that control which AWS accounts can use the AMI to launch instances
- A block device mapping that specifies the volumes to attach to the instance when it is launched

The Quick Start list contains the most commonly used AMIs bit it is also possible to create a custom AMI or select an AMI from the AWS Marketplace, an online store where you can sell or buy software that runs on AWS.

3. I kept **t3.micro** from the Instance type dropdown list.

An instance type determines the resources that will be allocated to your EC2 instance. Each instance type allocates a combination of virtual CPU, memory, disk storage, and network performance.

Instance types are divided into families, such as compute optimized, memory optimized, and storage optimized. The name of the instance type includes a family identifier, such as T3 and M5. The number indicates the generation of the instance, so M5 is newer than M4.

My application uses a t3.micro instance type, which is a small instance that can burst above baseline performance when it is busy. It is suitable for development and testing purposes and for applications that have bursty workloads.

4.  I selected **Proceed without key pair (Not recommended)** in the Key pair (login) section, from the Key pair name - required dropdown list.

Amazon EC2 uses public key cryptography to encrypt and decrypt login information. To log in to my instance, I must create a key pair, specify the name of the key pair when you launch the instance, and provide the private key when you connect to the instance.

I do not required a key pair here because I used EC2 Instance Connect to log in to my instance.

5. In the network settings, I seleceted **Lab VPC** for VPC.

The virtual private cloud (VPC) indicates which VPC I want to launch the instance into. An istance can have multiple VPCs, including different ones for development, testing, and production.

I launched the instance in a public subnet within the Lab VPC network.

6. In the network settings, I gave a name and description for the **Security Group**.

A security group acts as a virtual firewall that controls the traffic for one or more instances. When an instance is launched, one or more security groups are associated with the instance. I added rules to each security group that allow traffic to or from its associated instances. I can modify the rules for a security group at any time; the new rules are automatically applied to all instances that are associated with the security group.

7. I kept the default **8 gibibyte (GiB) disk volume** in the Configure storage pane.

In the configure storage it is possible to add additional Amazon Elastic Block Store (Amazon EBS) disk volumes and configure their size and performance. 
The EC2 instance is launched using a default 8 gibibyte (GiB) disk volume. This is called root volume (also known as a boot volume).

8. From IAM instance profile dropdown list, under the Advanced details pane, I chose Bastion-Role.

The Bastion-Role profile grants permission to applications running on the instance to make requests to the Amazon EC2 service. This association of Role is required for the second half of this lab, where you use the AWS CLI to communicate with the Amazon EC2 service.

9. After reviewing the instance configuration details in the Summary section, I clicked **Launch instance**.

![My Istance from Management Console](./istance-console.png)

## Task 2: Connect to the bastion host using the Management Console
Here I used EC2 Instance Connect to log in to the bastion host that created in the previous task.

1. On the EC2 Management Console, from the list of EC2 instances displayed, I selected the check box for the bastion host instance.
2. On the EC2 Instance Connect tab, I clicled **Connect** to connect to the bastion host.

![Connect to my Istance using Management Console](./istance-console-connect.png)

## Task 3: Launching an EC2 instance using the AWS CLI
Here I launched an EC2 instance using the AWS CLI. With the AWS CLI, I can automate the provisioning and configuration of AWS resources.

These are the parameters I gave to the to the command to successfully run it and launch.

1.  Code to retrieve **AMI**.
```bash
#Set the Region
AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
export AWS_DEFAULT_REGION=${AZ::-1}
#Retrieve latest Linux AMI
AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
echo $AMI
```
The AMI populates the boot disk of the instance. AWS continually patches and updates AMIs, so it is recommended to always use the latest AMI when launching instances.

3. Code to retrieve the **subnet ID** for the public subnet.
```bash
SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query Subnets[].SubnetId --output text)
echo $SUBNET
```

4.  Code to retrieve the **security group**, which allows inbound HTTP requests.
```bash
SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query SecurityGroups[].GroupId --output text)
echo $SG
```

5. Code to download a **user data script**.
```bash
wget https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt
```
The script installs a web server, downloads a .zip file containing the web application and installs the web application.

6. Eventually I launched the instance.
```bash
INSTANCE=$(\
aws ec2 run-instances \
--image-id $AMI \
--subnet-id $SUBNET \
--security-group-ids $SG \
--user-data file:///home/ec2-user/UserData.txt \
--instance-type t3.micro \
--tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Web Server}]' \
--query 'Instances[*].InstanceId' \
--output text \
)
echo $INSTANCE
```

7.  Wait for the instance to be ready

8.  Test the web server

## Optional challenge 1: Connect to an EC2 instance

## Optional challenge 2: Fix the web server installation







