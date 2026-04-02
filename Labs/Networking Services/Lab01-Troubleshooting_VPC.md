# Troubleshooting a VPC

In this lab, I will troubleshoot virtual private cloud (VPC) configurations and analyze VPC Flow Logs.

I will begin with an environment that includes two VPCs, Amazon Elastic Compute Cloud (Amazon EC2) instances, and other networking components shown 
in the diagram below.
This diagram also shows four numbered circles (#1–4) that indicate the order in which I will work through this lab.

![Troubleshooting a VPC Architecture](./images/lab2-architecture.png)

My tasks includes the following:
- creating an Amazon Simple Storage Service (Amazon S3) bucket to hold VPC Flow Log data
- creating a flow log to capture all IP traffic passing through network interfaces in the VPC
- troubleshooting the VPC configuration issues to allow access to the resources
- downloading and analyzing the flow log data

## Task 1: Connecting to the CLI Host instance

## Task 2: Creating VPC Flow Logs

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
  
