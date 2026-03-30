# Challenge Lab: Build Your DB Server and Interact With Your DB
  
This lab is designed to reinforce the concept of leveraging an AWS-managed database instance for solving relational database needs.

**Amazon Relational Database Service** (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. 
It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows you to 
focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from: Amazon Aurora, 
Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

## Steps

1. Launch an Amazon RDS DB instance using either Amazon Aurora Provisioned DB or MySQL database engines. 
Make a note of the DB credentials, as it will be needed in next steps. Please note the following lab restrictions:

    * DatabaseEngine: `Aurora (MySQL compatible)`
    * Template: Choose `Dev/Test`
    * DB instance identifier: `db-cluster-challenge`
    * Master username: `admin`
    * Password: `labchallenge123&` (self-manage)
    * DB instance size: `Burstable classes` type `db.t3.micro`
    * Storage: `Aurora Standard`
    * Availability and durability: `Don't create an Aurora Replica`
    * Amazon VPC: `Lab VPC`
    * DB subnet group: `lab subnet`
    * Security Group: `WebSecurityGorup` (the security group needs to allow the LinuxServer to connect to the RDS instance)
    * Initial database name: `lab`
    *  Under Additional configuration:
        * Disable Enable Enhanced monitoring
        * Disable Enable automated backup
        * Disable Enable encryption
        * Disable Enable auto minor version upgrade
    * Purchasing Options: On-Demand instances are allowed. Other purchasing options are disabled

![DB Aurora (MySQL compatible)]()

2. Click the Details followed by Show. Click Download PEM (for Linux or macOS) or Download PPK (for Windows) depending on your local operating system.
Make a note of the LinuxServer address. Connect (SSH) to the LinuxServer using the details you made a note of.
Install a MySQL client, and use it to connect to your db. Some helpful information is available here

3. Create a table RESTART with the following columns – Capture screenshot for submission

* Student ID (Number),
* Student Name,
* Restart City,
* Graduation Date (Date Time)

4. Insert 10 sample rows into this table – Capture screenshot for submission

5. Select all rows from this table – Capture screenshot for submission

6. Create a table CLOUD_PRACTITIONER with the following columns – Capture screenshot for submission

* Student ID (Number)
* certification date (Date Time)
* Insert 5 sample rows into this table – Capture screenshot for submission

7. Select all rows from this table – Capture screenshot for submission

8. Perform an inner join between the 2 tables created above and display student ID, Student Name, Certification Date – Capture screenshot for submission    


## Conclusion
* I created an RDS instance
* I used the Amazon RDS Query Editor to query data.
