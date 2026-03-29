# Challenge Lab: Build Your DB Server and Interact With Your DB
  
This lab is designed to reinforce the concept of leveraging an AWS-managed database instance for solving relational database needs.

**Amazon Relational Database Service** (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. 
It provides cost-efficient and resizable capacity while managing time-consuming database administration tasks, which allows you to 
focus on your applications and business. Amazon RDS provides you with six familiar database engines to choose from: Amazon Aurora, 
Oracle, Microsoft SQL Server, PostgreSQL, MySQL and MariaDB.

## Steps

1. Launch an Amazon RDS DB instance using either Amazon Aurora Provisioned DB or MySQL database engines. 
Make a note of the DB credentials, as it will be needed in next steps. Please note the following lab restrictions:

* DatabaseEngine: Supported engines are Amazon Aurora or MySQL. Amazon Aurora serverless is not available.
* Template: Choose Dev/Test or Free tier.
* Availability and durability: Avoid creating a standby instance.
* DB instance size: Choose Burstable classes - db.t3 instances of type db. t*.micro to db.t*.medium.
* Storage: Choose General Purpose SSD (gp2) of a size up to 100 GB. Provisioned IOPS access is restricted.
* Amazon VPC: Use the Lab VPC
* Security Group: Include a security group that will allow the LinuxServer to connect to the RDS instance.
* For MySQL, under Additional configuration - Enable Enhanced monitoring - Disable the option
* Purchasing Options: On-Demand instances are allowed. Other purchasing options are disabled.
  
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
