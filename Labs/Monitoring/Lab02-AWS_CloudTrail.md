# Working with AWS CloudTrail

## Introduction
AWS CloudTrail is a service that enables governance, compliance, operational auditing, and risk auditing of AWS accounts. 
It records account activity and API usage across AWS services, allowing users to track changes and investigate actions performed within an environment.

In this lab, a CloudTrail trail was created to monitor activity in an AWS account hosting a Café website on an Amazon EC2 instance. 
Shortly after configuration, the website was compromised, and security group rules were modified. The objective of this lab is to 
investigate the incident using CloudTrail logs, identify the responsible user, and restore system security using multiple analysis tools, 
including Linux commands, AWS CLI, and Amazon Athena.

The architectural diagram illustrates the setup that this activity uses.

![AWS CloudTrail Architecture](./images/MN-01-architecture.png)

## Task 1: Observing the System and Modifying Security Group
In this task, I accessed the EC2 instance running the Café Web Server and reviewed its security group configuration. Initially, only HTTP (port 80) access was allowed. 
I then added an SSH rule allowing access from my IP address only.

After updating the rule, I verified that the Café website was functioning normally by accessing it through the public IP address.

![Initial Café Website Status](./images/MN-02-initial-cafe-website.png)


## Task 2: Creating CloudTrail and Detecting the Security Incident
I created a new CloudTrail trail named **monitor**, configured to store logs in an S3 bucket with the following configuration:
- Trail name: `monitor`
- Create a new S3 bucket: `checked`
- Trail log bucket and folder: `monitoring2704`
- AWS KMS alias: `ct-KMS`

![CloudTrail Trail](./images/MN-02-cloudtrail-trail.png)  

Shortly after enabling logging, I noticed that the Café website had been modified unexpectedly.

![Café Website Hacked](./images/MN-02-cafe-website-hacked.png)

Upon reviewing the EC2 security group, I discovered an additional inbound rule allowing SSH access from anywhere (0.0.0.0/0), which indicated a 
security breach.

![Modified Security Group Rule](./images/MN-02-security-group-breach.png)


## Task 3: Analyzing CloudTrail Logs Using grep and AWS CLI
I connected to the EC2 instance via SSH and downloaded CloudTrail logs from the S3 bucket. The logs were extracted and analyzed using Linux commands:
```bash
chiara@macbook-air:~/labs$ chmod 700 labsuser.pem 
chiara@macbook-air:~/labs$ ssh -i labsuser.pem ec2-user@34.216.153.22
The authenticity of host '34.216.153.22 (34.216.153.22)' can't be established.
ED25519 key fingerprint is SHA256:X/yDuY7DUS98loVkCG13oySLwiEISr8rF6QNH1kNaj4.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '34.216.153.22' (ED25519) to the list of known hosts.
   ,     #_
   ~\_  ####_        Amazon Linux 2
  ~~  \_#####\
  ~~     \###|       AL2 End of Life is 2026-06-30.
  ~~       \#/ ___
   ~~       V~' '->
    ~~~         /    A newer version of Amazon Linux is available!
      ~~._.   _/
         _/ _/       Amazon Linux 2023, GA and supported until 2028-03-15.
       _/m/'           https://aws.amazon.com/linux/amazon-linux-2023/

[ec2-user@web-server ~]$ mkdir ctraillogs
[ec2-user@web-server ~]$ cd ctraillogs/
[ec2-user@web-server ctraillogs]$ aws s3 ls
2026-04-27 07:51:59 cafeimagefiles72344
2026-04-27 08:03:48 monitoring2704
[ec2-user@web-server ctraillogs]$ aws s3 cp s3://monitoring2704/ . --recursive
download: s3://monitoring2704/AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json.gz to AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json.gz
download: s3://monitoring2704/AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json.gz to AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json.gz
[ec2-user@web-server ctraillogs]$ ls AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/
106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json.gz
106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json.gz
[ec2-user@web-server ctraillogs]$ cd AWSLogs/106643185353/CloudTrail/us-west-2/2026/04/27/
[ec2-user@web-server 27]$ gunzip *.gz
[ec2-user@web-server 27]$ ls
106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json
106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json
```

The log files are in `json` format. To improve readability, I used a Python utility to format the content:
```bash
cat 106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json | python -m json.tool
````

This made it easier to understand the structure of the log entries. Each entry contains standard fields such as `awsRegion`, `eventName`, `eventSource`, 
`eventTime`, `requestParameters`, `sourceIPAddress`, and `userIdentity`.

However, even a single log file contains a large number of entries. Since multiple log files are generated over time, analyzing them manually 
becomes inefficient.

To search across multiple files and filter relevant information, I used Linux commands such as `grep`. I filtered log entries based on `sourceIPAddress` 
and `eventName` to identify suspicious activity. This approach helped narrow down actions related to the security group modifications.
```bash
[ec2-user@web-server 27]$ ip=34.216.153.22
[ec2-user@web-server 27]$ for i in $(ls); do echo $i && cat $i | python -m json.tool | grep sourceIPAddress ; done
106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json
            "sourceIPAddress": "193.5.232.113",
            "sourceIPAddress": "16.148.102.148",
            "sourceIPAddress": "34.216.153.22",
            "sourceIPAddress": "34.216.153.22",
            "sourceIPAddress": "34.216.153.22",
            ...
[ec2-user@web-server 27]$ for i in $(ls); do echo $i && cat $i | python -m json.tool | grep eventName ; done
106643185353_CloudTrail_us-west-2_20260427T0810Z_2fxF0z1ItT1MUoxC.json
            "eventName": "GetEventSelectors",
            "eventName": "DescribeSecurityGroups",
            "eventName": "DescribeInstances",
            "eventName": "DescribeInstances",
            ...
106643185353_CloudTrail_us-west-2_20260427T0815Z_teNeI2QmobmBTIs2.json
            ...
            "eventName": "UpdateInstanceInformation",
            "eventName": "GetParametersByPath",
            "eventName": "DescribeRegions",
            "eventName": "DescribeSecurityGroups",
            "eventName": "DescribeInstances",
           ...
[ec2-user@web-server 27]$ 
```

A more effective approach was to use AWS CLI CloudTrail commands to analyze the logs. I used the `lookup-events` command to investigate EC2 
security group modifications and identify the user responsible for the changes.

First, I checked for console login activity:
```bash
[ec2-user@web-server 27]$ aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin
{
    "Events": []
}
```

The result returned no events, indicating that the actions were not performed through the AWS Management Console.

Next, I retrieved the AWS Region and the security group ID associated with the Café Web Server instance:

```bash
[ec2-user@web-server 27]$ region=$(curl http://169.254.169.254/latest/dynamic/instance-identity/document|grep region | cut -d '"' -f4)
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100   474  100   474    0     0   153k      0 --:--:-- --:--:-- --:--:--  231k
[ec2-user@web-server 27]$ sgId=$(aws ec2 describe-instances --filters "Name=tag:Name,Values='Cafe Web Server'" --query 'Reservations[*].Instances[*].SecurityGroups[*].[GroupId]' --region $region --output text)
[ec2-user@web-server 27]$ echo $region
us-west-2
[ec2-user@web-server 27]$ echo $sgId
sg-0c64bf38ac8ac6d0f
```

Using this information, I filtered CloudTrail events related to security group changes:
```bash
aws cloudtrail lookup-events \
--lookup-attributes AttributeKey=ResourceType,AttributeValue=AWS::EC2::SecurityGroup \
--region $region --output text | grep $sgId
```

From the output, I identified a suspicious event:
- Event Name: `AuthorizeSecurityGroupIngress`
- User: `chaos`
- Source IP: `34.216.153.22`
- Action: Opened port 22 (SSH) to 0.0.0.0/0
- Method: AWS CLI (based on user agent)

This confirmed that the IAM user chaos was responsible for modifying the security group and introducing the security vulnerability.


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

## Additional resources
- [AWS CLI Reference page for CloudTrail](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/)
