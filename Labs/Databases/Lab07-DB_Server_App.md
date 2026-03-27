# Build Your DB Server and Interact With Your DB Using an App

In this lab I will leverage an AWS-managed database instance by solving relational database needs.

**Amazon Relational Database Service** (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. 
It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows to focus 
on the applications and business. Amazon RDS provides with six familiar database engines to choose from: 
Amazon Aurora, Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

![DB Server App Architecture](./images/lab07-architecture.png)

## Task 1: Create a Security Group for the RDS DB Instance
I In this task, I create a security group to allow the web server to access the RDS DB instance:
- Security group name: `DB Security Group`
- Description: `Permit access from Web Security Group`
- VPC: `Lab VPC`

Then I addd an inbound rule to permit traffic on port 3306 (database requests) from any EC2 instance 
that is associated with the Web Security Group:
- Type: MySQL/Aurora (3306)
- Source: Type sg in the search field and then select Web Security Group.

The security group will be used when launching the Amazon RDS database instance.

## Task 2: Create a DB Subnet Group
I In this task, I create a DB subnet group that is used to tell RDS which subnets can be used for the database:
- Name: `DB Subnet Group`
- Description: `DB Subnet Group`
- VPC ID: `Lab VPC`

Each DB subnet group requires subnets in at least two Availability Zones. 
So I add Private Subnet 1 (10.0.1.0/24) and Private Subnet 2 (10.0.3.0/24).




## Task 3: Create an Amazon RDS DB Instance

## Task 4: Interact with Your Database

## Conclusions
- I launch an Amazon RDS DB instance with high availability.
- I configure the DB instance to permit connections from my web server.
- I open a web application and interact with my database.
