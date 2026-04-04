# Troubleshooting a VPC

In this lab, I will troubleshoot virtual private cloud (VPC) configurations and analyze VPC Flow Logs.

I will begin with an environment that includes two VPCs, Amazon Elastic Compute Cloud (Amazon EC2) instances, and other networking components shown 
in the diagram below.
This diagram also shows four numbered circles (#1–4) that indicate the order in which I will work through this lab.

![Troubleshooting a VPC Architecture](./images/lab02-architecture.png)

AWS services:
- EC2 instances
- Amazon Simple Storage Service (Amazon S3) bucket
- 
- creating an Amazon Simple Storage Service (Amazon S3) bucket to hold VPC Flow Log data
- creating a flow log to capture all IP traffic passing through network interfaces in the VPC
- troubleshooting the VPC configuration issues to allow access to the resources
- downloading and analyzing the flow log data


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

## Troubleshooting challenge #1

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
  
