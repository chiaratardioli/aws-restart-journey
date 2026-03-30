# Migrate to Amazon RDS

In this lab, I will migrate the café web application to use a fully managed Amazon Relational Database Service (Amazon RDS) 
database (DB) instance instead of a local database instance.

I will begin by generating some data on the existing database. This data is migrated to the new Amazon RDS instance.
During the migration process, I will build the required components, including two private subnets in different 
Availability Zones, a security group for the database instance, and the RDS DB instance itself. After the database 
has been migrated, I will reconfigure the café application to use the Amazon RDS instance instead of a local database.

## Starting architecture

The following diagram illustrates the topology of the café web application runtime environment before the migration. 
The application database runs in an Amazon Elastic Compute Cloud (Amazon EC2) Linux, Apache, MySQL, and PHP (LAMP) 
instance along with the application code. The instance has a T3 small instance type and runs in a public subnet so 
that internet clients can access the website. A CLI Host instance resides in the same subnet to facilitate the a
dministration of the instance by using the AWS Command Line Interface (AWS CLI).

![Starting architecture](./images/lab01-starting-architecture.png)

## Final architecture

The following diagram illustrates the topology of the café web application runtime environment after the migration.
I will migrate the local café database to an Amazon RDS database that resides outside the instance. The Amazon RDS 
database is deployed in the same virtual private cloud (VPC) as the instance.

![Final architecture after migration](./images/lab01-final-architecture.png)

## Task 1: Generating order data on the café website

## Task 2: Creating an Amazon RDS instance by using the AWS CLI

1. Connecting to the CLI Host instance
2. Connecting to the CLI Host instance
3. Creating prerequisite components
4. Creating the Amazon RDS MariaDB instance

## Task 3: Migrating application data to the Amazon RDS instance


## Task 4: Configuring the website to use the Amazon RDS instance


## Task 5: Monitoring the Amazon RDS database


## Conclusion
- I created an Amazon RDS MariaDB instance by using the AWS CLI.
- I migrated data from a MariaDB database on an EC2 instance to an Amazon RDS MariaDB instance.
- I monitored the Amazon RDS instance by using Amazon CloudWatch metrics.
