# Introduction to Amazon Aurora

This lab introduces to Amazon Aurora and provides basic understanding of how to use Aurora. 
I will follow the steps to create an Aurora instance and then connect to it.

## Amazon technologies n this lab
- **Amazon Aurora**
  
  Aurora is a fully managed, MySQL-compatible, relational database engine that combines the performance and reliability of high-end commercial
  databases with the simplicity and cost-effectiveness of open-source databases. It delivers up to five times the performance of MySQL without
  requiring changes to most of your existing applications that use MySQL databases.
- **Amazon Elastic Compute Cloud (Amazon EC2)**
  
  Amazon EC2 is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier
  for developers. Amazon EC2 reduces the time required to provision new server instances to minutes, giving you the ability to quickly scale
  capacity, both up and down, as your computing requirements change.
- **Amazon Relational Database Service (Amazon RDS)**
  
  Amazon RDS makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while
  managing time-consuming database administration tasks, freeing you up to focus on your applications and business. Amazon RDS provides you with six
  database engines to choose from, including Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL, and MariaDB.

## Task 1: Create an Aurora instance
Here, I create an Aurora database (DB) instance with this configuration:
- Engine type: `Aurora (MySQL Compatible)`
- Engine version: `Aurora MySQL 3.10.3`
- Templates: `Dev/Test`

Unser Settings, I configure the following options:
- DB cluster identifier: `aurora`
- Master username: `admin`
- Master password: `admin123`

Under Instance configuration, I configure the following for DB instance class:
- Select `Burstable classes (includes t classes)`
- Select `db.t3.medium`

Under Availability & durability section for Multi-AZ deployment, I choose `Don't create an Aurora Replica`.
Since this is a lab environment, I do not need to perform a multi-AZ deployment.

Under Connectivity, I configure the following options:
* Virtual private cloud (VPC): `LabVPC`
* Subnet group: `dbsubnetgroup`
* Public access: `No`
* VPC security group: choose existing and select `DBSecurityGroup`

Under Monitoring:
- Uncheck Enable Enhanced monitoring

I expand Additional configuration and then I configure the following:
- Database name: `world`
- Uncheck Enable encryption.
- Uncheck Enable auto minor version upgrade.

![DB Aurora (MySQL Compatible)](./images/db-aurora.png)

## Task 2: Connect to an Amazon EC2 Linux instance

## Task 3: Configure the Amazon EC2 Linux instance to connect to Aurora

## Task 4: Create a table and insert and query records

## Conclusions
- I created an Aurora instance.
- I connected to a pre-created Amazon EC2 instance.
- I configured the Amazon EC2 instance to connect to Aurora.
- I queried the Aurora instance.

## Additional resources
- [Amazon RDS Multi-AZ Deployments](https://aws.amazon.com/rds/details/multi-az/)
- [Working with an Amazon RDS DB Instance in a VPC](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_VPC.WorkingWithRDSInstanceinaVPC.html)
- [What Is Amazon VPC?](https://docs.aws.amazon.com/AmazonVPC/latest/UserGuide/VPC_Introduction.html)
- [Encrypting Amazon RDS Resources](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Overview.Encryption.html)
- [Enhanced Monitoring](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_Monitoring.OS.html)
- [Amazon EC2 Key Pairs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html)

## Lab Notes

1.  Amazon RDS Multi-AZ deployments provide enhanced availability and durability for DB instances, making them a natural fit 
for production database workloads. When you provision a Multi-AZ DB instance, Amazon RDS automatically creates a primary DB 
instance and synchronously replicates the data to a standby instance in a different Availability Zone.

2. Subnets are segments of a virtual private cloud (VPC) IP address range that you designate to group 
your resources based on security and operational needs. A DB subnet group is a collection of subnets (typically private) 
that you create in a VPC and that you then designate for your DB instances. With a DB subnet group, you can specify a particular 
VPC when creating DB instances using the command line interface (CLI) or application programming interface (API); 
if you use the console, you can select the VPC and subnets that you want to use.

3. You can encrypt your Amazon RDS instances and snapshots at rest by enabling the encryption option for your RDS DB instance. 
Data that is encrypted at rest includes the underlying storage for a DB instance, its automated backups, read replicas, and snapshots.
