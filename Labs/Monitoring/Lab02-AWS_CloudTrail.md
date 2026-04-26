# Working with AWS CloudTrail

## Introduction
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of AWS accounts. 
It records account activity and API usage across AWS services, allowing users to track changes and investigate actions performed within an environment.

In this lab, a CloudTrail trail was created to monitor activity in an AWS account hosting a Café website on an Amazon EC2 instance. 
Shortly after configuration, the website was compromised, and security group rules were modified. The objective of this lab is to 
investigate the incident using CloudTrail logs, identify the responsible user, and restore system security using multiple analysis tools, 
including Linux commands, AWS CLI, and Amazon Athena.


## Task 1: Observing the System and Modifying Security Group
In this task, I accessed the EC2 instance running the Café Web Server and reviewed its security group configuration. Initially, only HTTP (port 80) access was allowed. 
I then added an SSH rule allowing access from my IP address only.

After updating the rule, I verified that the Café website was functioning normally by accessing it through the public IP address.

![Initial Café Website Status](./images/MN-02-initial-cafe-website.png)


## Task 2: Creating CloudTrail and Detecting the Security Incident
I created a new CloudTrail trail named **monitor**, configured to store logs in an S3 bucket. Shortly after enabling logging, I noticed that the 
Café website had been modified unexpectedly.

Upon reviewing the EC2 security group, I discovered an additional inbound rule allowing SSH access from anywhere (0.0.0.0/0), which indicated a 
security breach.

![CloudTrail Trail Creation](./images/MN-02-cloudtrail-trail-creation.png)  
![Modified Security Group Rule](./images/MN-02-security-group-breach.png)


## Task 3: Analyzing CloudTrail Logs Using grep and AWS CLI
I connected to the EC2 instance via SSH and downloaded CloudTrail logs from the S3 bucket. The logs were extracted and analyzed using Linux commands such as `grep`.

I filtered log entries based on `sourceIPAddress` and `eventName` to identify suspicious activity. This helped narrow down actions related to the security group changes.

I also used AWS CLI commands such as `lookup-events` to investigate EC2 security group modifications and identify the user responsible for the changes.

![CloudTrail Logs Downloaded](./images/MN-02-cloudtrail-logs-download.png)  
![grep Log Analysis](./images/MN-02-grep-analysis.png)  
![AWS CLI CloudTrail Lookup](./images/MN-02-cli-cloudtrail-lookup.png)


## Task 4: Querying CloudTrail Logs Using Amazon Athena
To simplify log analysis, I created an Athena table based on CloudTrail logs stored in S3. This allowed structured querying using SQL.

I ran queries to extract key fields such as:
- useridentity.userName  
- eventtime  
- eventsource  
- eventname  
- requestparameters  

Using Athena, I was able to filter security-related events and identify the user responsible for modifying the security group.

![Athena Table Creation](./images/MN-02-athena-table-creation.png)  
![Athena Query Results](./images/MN-02-athena-query-results.png)


### Challenge: Identifying the Hacker
By combining results from CloudTrail logs, AWS CLI, and Athena queries, I identified:
- The IAM user responsible for the security group modification
- The timestamp of the malicious activity
- The source IP address used for access
- The method of access (programmatic or console)

This confirmed the root cause of the security breach.


## Task 5: Securing the Environment and Recovering the System

1. Removing Unauthorized OS Access

I detected an unauthorized OS user (`chaos-user`) on the EC2 instance. I terminated their session and removed the account from the system.

![Unauthorized User Detection](./images/MN-02-unauthorized-user.png)


2. Fixing SSH Security Configuration

I reviewed the SSH configuration file and found that password authentication was enabled. I disabled password authentication and ensured only key-based 
authentication was allowed. I then restarted the SSH service.

![SSH Configuration Fix](./images/MN-02-ssh-security-fix.png)


3. Restoring Website Integrity

I restored the original Café website image by replacing the modified file with the backup version. After refreshing the website, the correct content was displayed again.

![Website Restoration](./images/MN-02-website-restored.png)


4. Removing Malicious IAM User

Finally, I deleted the unauthorized IAM user (**chaos**) from the AWS account to prevent further misuse of permissions.

![IAM User Deletion](./images/MN-02-iam-user-deletion.png)

## Conclusion
This lab demonstrated how AWS CloudTrail can be used to monitor, investigate, and respond to security incidents in an AWS environment. 
I configured a CloudTrail trail, analyzed logs using multiple tools, and identified unauthorized modifications to a security group.

I used Linux utilities, AWS CLI commands, and Amazon Athena to trace the source of the incident and determine the responsible user. 
After identifying the issue, I removed unauthorized access, corrected SSH configuration settings, restored the compromised website, 
and deleted the malicious IAM user.

Overall, the lab highlighted the importance of continuous monitoring, log analysis, and proactive security measures in maintaining 
a secure AWS environment.

In summary:
- I configured a CloudTrail trail
- I analyzed CloudTrail logs by using various methods to discover relevant information
- I imported CloudTrail log data into Athena
- I run queries in Athena to filter CloudTrail log entries
- I resolved security concerns within the AWS account and on an EC2 Linux instance

