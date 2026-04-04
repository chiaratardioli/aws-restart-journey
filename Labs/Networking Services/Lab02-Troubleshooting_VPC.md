# Troubleshooting a VPC

In this lab, I will troubleshoot virtual private cloud (VPC) configurations and analyze VPC Flow Logs.

I will begin with an environment that includes two VPCs, Amazon Elastic Compute Cloud (Amazon EC2) instances, and other networking components shown 
in the diagram below.
This diagram also shows four numbered circles (#1–4) that indicate the order in which I will work through this lab.

![Troubleshooting a VPC Architecture](./images/lab02-architecture.png)

AWS services:
- EC2 instances
- Amazon Simple Storage Service (Amazon S3) bucket


## Task 1: Connecting to the CLI Host instance

1. I connect to the `CLI Host` using the EC2 Management Console.
```bash
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

[ec2-user@cli-host ~]$ 
```

2. I configure the AWS CLI on the CLI Host instance with the command `aws congigure` and the following parameters:
- AWS Access Key ID: `< AccessKey>`
- AWS Secret Access Key:`<SecretKey>`
- Default region name: `us-west-2`
- Default output format: `json`

## Task 2: Creating VPC Flow Logs

1. I create an S3 bucket  where the flow logs will be published:
```bash
aws s3api create-bucket --bucket flowlog20260404 --region 'us-west-2' --create-bucket-configuration LocationConstraint='us-west-2'
```

Output:
```bash
{
    "Location": "http://flowlog20260404.s3.amazonaws.com/"
}
```

3. I get the VPC ID for VPC1:
```bash
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,Tags[?Key==`Name`].Value,CidrBlock]' --filters "Name=tag:Name,Values='VPC1'"
```

Output:
```bash
[
    [
        "vpc-0f9c39be0b5406fb9", 
        [
            "VPC1"
        ], 
        "10.0.0.0/16"
    ]
]
```

4. I create VPC Flow Logs on VPC1 to capture information about IP traffic between network interfaces in VPC1. The flow logs are then published to the S3 bucket.
```bash
aws ec2 create-flow-logs --resource-type VPC --resource-ids vpc-0f9c39be0b5406fb9 --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::flowlog20260404
```

Output:
```bash
{
    "Unsuccessful": [], 
    "FlowLogIds": [
        "fl-0feb27c7f8419f694"
    ], 
    "ClientToken": "MlIbnTrt9lgna4pmmj9GBifSSeoEA1aUV+/FSWs60wQ="
}
```

5. To confirm that the flow log was created I run the command `aws ec2 describe-flow-logs`.
The command output shows that a single flow log was created with a FlowLogStatus of ACTIVE and a log destination that points to your S3 bucket.
```bash
{
    "FlowLogs": [
        {
            "LogDestinationType": "s3", 
            "Tags": [], 
            "ResourceId": "vpc-0f9c39be0b5406fb9", 
            "CreationTime": "2026-04-04T21:21:42.990Z", 
            "TrafficType": "ALL", 
            "FlowLogStatus": "ACTIVE", 
            "LogFormat": "${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}", 
            "FlowLogId": "fl-0feb27c7f8419f694", 
            "MaxAggregationInterval": 600, 
            "LogDestination": "arn:aws:s3:::flowlog20260404", 
            "DeliverLogsStatus": "SUCCESS"
        }
    ]
}
```

## Task 3: Troubleshooting VPC configuration issues to allow access to resources
Here, I analyze access to the web server instance and troubleshoot some networking issues. 

1. I copy and paste *WebServerIP IP address* `54.200.166.86` into a new browser tab. 
I recall that the cafe web server instance runs in the public subnet in VPC1.

2. In the CLI Host terminal, I find details about the web server instance:
```bash
aws ec2 describe-instances --filter "Name=ip-address,Values='54.200.166.86'"
```

A large JSON document is returned that provides more details than I need for your troubleshooting. 
To return only relevant details, you filter the results on the client side by using the query parameter.
The command in the next step returns only the state of the instance, the private IP address, the instance ID, 
the security groups that are applied to it, the subnet in which it runs, and the key pair name that is associated with it. 

3. I filter the results using the query parameter:
```bash
aws ec2 describe-instances --filter "Name=ip-address,Values='54.200.166.86'" --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'
```

Output:
```bash
ċ
    [
        [
            {
                "Code": 16, 
                "Name": "running"
            }, 
            "10.0.1.141", 
            "i-03e760bad906c10f0", 
            [
                {
                    "GroupName": "c203346a5187757l14538602t1w761183759049-WebSecurityGroup-YlE0AZHZU4cj", 
                    "GroupId": "sg-064fb798758e559f1"
                }
            ], 
            "subnet-01110cef37b3434c0", 
            "vockey"
        ]
    ]
]
```

4. I verify that I cannpt connect to the *Cafe Web Server* instance using the EC2 Management Console.

## Troubleshooting challenge #1

1. I check which ports are open on the web server EC2 instance using the command `nmap`
```bash
[ec2-user@cli-host ~]$ nmap 54.200.166.86

Starting Nmap 6.40 ( http://nmap.org ) at 2026-04-04 21:43 UTC
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.03 seconds
```

2. I check the security group details by using the command `aws ec2 describe-security-groups` with query parameters.
```bash
aws ec2 describe-security-groups --filter "Name=ip-address,Values='54.200.166.86'" --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'
```

4. 



## Troubleshooting challenge #2

## Task 4: Analyzing flow logs

1. Downloading and extracting flow logs
2. Analyzing the logs

## Conclusion
- I created VPC Flow Logs
- I troubleshot VPC configuration issues
- I analyzed flow logs

## Additional resources
- [Flow Log Records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records)
- [AWS CLI Command Reference: create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html)
- [AWS CLI Command Reference: delete-network-acl-entry](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-network-acl-entry.html#delete-network-acl-entry)
- [AWS CLI Command Reference: describe-security-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html)
- [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html)
  
