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
aws s3api create-bucket --bucket flowlog20260405 --region 'us-west-2' --create-bucket-configuration LocationConstraint='us-west-2'
```

Output:
```bash
{
    "Location": "http://flowlog20260405.s3.amazonaws.com/"
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
        "vpc-0d6117f5364c05d1d", 
        [
            "VPC1"
        ], 
        "10.0.0.0/16"
    ]
]
```

4. I create VPC Flow Logs on VPC1 to capture information about IP traffic between network interfaces in VPC1. The flow logs are then published to the S3 bucket.
```bash
aws ec2 create-flow-logs --resource-type VPC --resource-ids vpc-0d6117f5364c05d1d --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::flowlog20260404
```

Output:
```bash
{
    "Unsuccessful": [], 
    "FlowLogIds": [
        "fl-0ce3731cfc100a6c5"
    ], 
    "ClientToken": "alZro6sAbJYDU90H+bHPHcrZAy2Wg7Otd29+FWNOOUM="
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
            "ResourceId": "vpc-0d6117f5364c05d1d", 
            "CreationTime": "2026-04-05T09:29:36.737Z", 
            "TrafficType": "ALL", 
            "FlowLogStatus": "ACTIVE", 
            "LogFormat": "${version} ${account-id} ${interface-id} ${srcaddr} ${dstaddr} ${srcport} ${dstport} ${protocol} ${packets} ${bytes} ${start} ${end} ${action} ${log-status}", 
            "FlowLogId": "fl-0ce3731cfc100a6c5", 
            "MaxAggregationInterval": 600, 
            "LogDestination": "arn:aws:s3:::flowlog20260405", 
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
aws ec2 describe-instances --filter "Name=ip-address,Values='16.148.88.255'"
```

A large JSON document is returned that provides more details than I need for your troubleshooting. 
To return only relevant details, you filter the results on the client side by using the query parameter.
The command in the next step returns only the state of the instance, the private IP address, the instance ID, 
the security groups that are applied to it, the subnet in which it runs, and the key pair name that is associated with it. 

3. I filter the results using the query parameter:
```bash
aws ec2 describe-instances --filter "Name=ip-address,Values='16.148.88.255'" --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'
```

Output:
```bash
[
    [
        [
            {
                "Code": 16, 
                "Name": "running"
            }, 
            "10.0.1.113", 
            "i-080537e8fee8c21f5", 
            [
                {
                    "GroupName": "c203346a5187757l14538602t1w761183759049-WebSecurityGroup-nay824whUpA4", 
                    "GroupId": "sg-00fd2748ee040b1db"
                }
            ], 
            "subnet-0d697d9f218ade797", 
            "vockey"
        ]
    ]
]
```

4. I verify that I cannpt connect to the *Cafe Web Server* instance using the EC2 Management Console.

## Troubleshooting challenge #1

1. I check which ports are open on the web server EC2 instance using the command `nmap`
```bash
[ec2-user@cli-host ~]$ nmap 16.148.88.255

Starting Nmap 6.40 ( http://nmap.org ) at 2026-04-05 09:46 UTC
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.03 seconds
```

The command *nmap* cannot find any open ports.

2. I check the security group details by using the command `aws ec2 describe-security-groups --group-ids '<GroupID>'`
```bash
[ec2-user@cli-host ~]$ aws ec2 describe-security-groups --group-ids 'sg-00fd2748ee040b1db'
{
    "SecurityGroups": [
        {
            "IpPermissionsEgress": [
                {
                    "IpProtocol": "-1", 
                    "PrefixListIds": [], 
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ], 
                    "UserIdGroupPairs": [], 
                    "Ipv6Ranges": []
                }
            ], 
            "Description": "Enable HTTP access", 
            "Tags": [
                {
                    "Value": "c203346a5187757l14538602t1w761183759049", 
                    "Key": "cloudlab"
                }, 
                {
                    "Value": "arn:aws:cloudformation:us-west-2:761183759049:stack/c203346a5187757l14538602t1w761183759049/f4650cf0-30d0-11f1-af86-02a472f2502d", 
                    "Key": "aws:cloudformation:stack-id"
                }, 
                {
                    "Value": "WebSecurityGroup", 
                    "Key": "aws:cloudformation:logical-id"
                }, 
                {
                    "Value": "c203346a5187757l14538602t1w761183759049", 
                    "Key": "aws:cloudformation:stack-name"
                }, 
                {
                    "Value": "WebSecurityGroup", 
                    "Key": "Name"
                }
            ], 
            "IpPermissions": [
                {
                    "PrefixListIds": [], 
                    "FromPort": 80, 
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ], 
                    "ToPort": 80, 
                    "IpProtocol": "tcp", 
                    "UserIdGroupPairs": [], 
                    "Ipv6Ranges": []
                }, 
                {
                    "PrefixListIds": [], 
                    "FromPort": 22, 
                    "IpRanges": [
                        {
                            "CidrIp": "0.0.0.0/0"
                        }
                    ], 
                    "ToPort": 22, 
                    "IpProtocol": "tcp", 
                    "UserIdGroupPairs": [], 
                    "Ipv6Ranges": []
                }
            ], 
            "GroupName": "c203346a5187757l14538602t1w761183759049-WebSecurityGroup-nay824whUpA4", 
            "VpcId": "vpc-0d6117f5364c05d1d", 
            "OwnerId": "761183759049", 
            "GroupId": "sg-00fd2748ee040b1db"
        }
    ]
}
```

The security group settings that are applied to the web server EC2 instance look like they are allowing connectivity to port 22.

3. I check the route table settings for the route table that is associated with the subnet where the web server is running.
```bash
[ec2-user@cli-host ~]$ aws ec2 describe-route-tables --filter "Name=association.subnet-id,Values='subnet-0d697d9f218ade797'"
{
    "RouteTables": [
        {
            "Associations": [
                {
                    "SubnetId": "subnet-0d697d9f218ade797", 
                    "AssociationState": {
                        "State": "associated"
                    }, 
                    "RouteTableAssociationId": "rtbassoc-0d260dbb0618579fd", 
                    "Main": false, 
                    "RouteTableId": "rtb-05f86acb7cacdb3a9"
                }
            ], 
            "RouteTableId": "rtb-05f86acb7cacdb3a9", 
            "VpcId": "vpc-0d6117f5364c05d1d", 
            "PropagatingVgws": [], 
            "Tags": [
                {
                    "Value": "VPC1PublicRouteTable", 
                    "Key": "aws:cloudformation:logical-id"
                }, 
                {
                    "Value": "VPC1 Public Route Table", 
                    "Key": "Name"
                }, 
                {
                    "Value": "c203346a5187757l14538602t1w761183759049", 
                    "Key": "aws:cloudformation:stack-name"
                }, 
                {
                    "Value": "c203346a5187757l14538602t1w761183759049", 
                    "Key": "cloudlab"
                }, 
                {
                    "Value": "arn:aws:cloudformation:us-west-2:761183759049:stack/c203346a5187757l14538602t1w761183759049/f4650cf0-30d0-11f1-af86-02a472f2502d", 
                    "Key": "aws:cloudformation:stack-id"
                }
            ], 
            "Routes": [
                {
                    "GatewayId": "local", 
                    "DestinationCidrBlock": "10.0.0.0/16", 
                    "State": "active", 
                    "Origin": "CreateRouteTable"
                }
            ], 
            "OwnerId": "761183759049"
        }
    ]
}
```

## Troubleshooting challenge #2

## Task 4: Analyzing flow logs

1. Downloading and extracting flow logs
2. Analyzing the logs

## Conclusion
- I created VPC Flow Logs
- I troubleshot VPC configuration issues
- I analyzed flow logs

## AWS CLI
```bash
# Start AWS CLI
aws configure

# Create the S3 bucket
aws s3api create-bucket --bucket flowlog###### --region 'us-west-2' --create-bucket-configuration LocationConstraint='us-west-2'

# Get the VPC ID for VPC1
aws ec2 describe-vpcs --query 'Vpcs[*].[VpcId,Tags[?Key==`Name`].Value,CidrBlock]' --filters "Name=tag:Name,Values='VPC1'"

# Create VPC Flow Logs on VPC1
aws ec2 create-flow-logs --resource-type VPC --resource-ids <vpc-id> --traffic-type ALL --log-destination-type s3 --log-destination arn:aws:s3:::<flowlog######>

# Confirm that the flow log was created
aws ec2 describe-flow-logs

# Delete AWS VPC Flow Log fl-XXXXXXX
aws ec2 delete-flow-logs --flow-log-ids <fl-XXXXXXX>

# Show all details about the web server instance
aws ec2 describe-instances --filter "Name=ip-address,Values='<WebServerIP>'"

# Show relevant details about the web server instance
aws ec2 describe-instances --filter "Name=ip-address,Values='<WebServerIP>'" --query 'Reservations[*].Instances[*].[State,PrivateIpAddress,InstanceId,SecurityGroups,SubnetId,KeyName]'

# Install the nmap utility
sudo yum install -y nmap

# Display which ports are open (on the web server EC2 instance)
nmap <WebServerIP>

# Display the security group details
aws ec2 describe-security-groups --group-ids 'WebServerSgId'

# Check the route table settings for the route table that is associated with the subnet where the web server is running
aws ec2 describe-route-tables --filter "Name=association.subnet-id,Values='<VPC1PubSubnetID>'"

# or if there are more than one route tables
aws ec2 describe-route-tables  --route-table-ids '<VPC1PubRouteTableId>' --filter "Name=association.subnet-id,Values='<VPC1PubSubnetID>'"
```

## Additional resources
- [Flow Log Records](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html#flow-log-records)
- [AWS CLI Command Reference: create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html)
- [AWS CLI Command Reference: delete-network-acl-entry](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-network-acl-entry.html#delete-network-acl-entry)
- [AWS CLI Command Reference: describe-security-groups](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-security-groups.html)
- [Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AccessingInstances.html)
  
