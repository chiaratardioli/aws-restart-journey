# Optimize Utilization

## Introduction

This lab focused on optimizing AWS resources used by the Café web application to reduce operational costs and improve efficiency. 
The primary objectives were to remove an unnecessary local database from an Amazon EC2 instance and resize the instance to a more 
cost-effective type. Additionally, the AWS Pricing Calculator was used to estimate and compare costs before and after optimization.

This diagram illustrates the topology of the Café web application runtime environment before and after the optimization.

[Café Web Application Architecture](./images/EX-02-architecture.png)


## Task 1: Optimize the Website to Reduce Costs

In this task, I connected to the Café EC2 instance and the CLI Host using SSH to perform optimization steps.

1. Connect to the Café Instance

I established an SSH connection to the Café EC2 instance using the provided key pair and public IP address.

[SSH connection to CafeInstance](./images/MN-01-ssh-cafeinstance.png)

I also configured the AWS CLI by setting the access key, secret key, region, and default output format.

[AWS CLI configuration](./images/MN-01-aws-cli-config.png)

2. Connect to the CLI Host

Next, I opened a second SSH session to the CLI Host instance and configured the AWS CLI there as well.

[SSH connection to CLI Host](./images/MN-01-ssh-clihost.png)

3. Uninstall MariaDB and Resize the Instance

I stopped and removed the local MariaDB database from the Café instance using the following commands:

```bash
sudo systemctl stop mariadb
sudo yum -y remove mariadb-server
```

[MariaDB removal output](./images/MN-01-remove-mariadb.png)

Then, from the CLI Host, I identified the instance ID of the Café instance:

```bash
aws ec2 describe-instances 
--filters "Name=tag:Name,Values= CafeInstance" 
--query "Reservations[*].Instances[*].InstanceId"
```

[Describe instances output](./images/MN-01-describe-instance.png)

After obtaining the instance ID, I stopped the instance:

```bash
aws ec2 stop-instances --instance-ids <instance-id>
```

[Stop instance](./images/MN-01-stop-instance.png)

I modified the instance type to `t3.micro`:

```bash
aws ec2 modify-instance-attribute 
--instance-id <instance-id> 
--instance-type "{"Value": "t3.micro"}"
```

[Modify instance type](./images/MN-01-modify-instance.png)

Then I restarted the instance:

```bash
aws ec2 start-instances --instance-ids <instance-id>
```

[Start instance](./images/MN-01-start-instance.png)

Finally, I verified that the instance was running and recorded its new public DNS and IP:

```bash
aws ec2 describe-instances 
--instance-ids <instance-id> 
--query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
```

[Instance status check](./images/MN-01-instance-status.png)

I accessed the Café website via the browser to confirm it was functioning correctly after the changes.

[Website test](./images/MN-01-website-test.png)


## Task 2: Estimate AWS Service Costs

1. Costs Before Optimization

I used the AWS Pricing Calculator to estimate the monthly cost of the infrastructure before optimization with the following configuration:

- EC2 instance: t3.small
- EBS storage: 40 GB
- RDS instance: db.t3.micro (20 GB storage)

[Calculator before optimization](./images/MN-01-calculator-before.png)

**Estimated Monthly Cost (Before Optimization): $35.60**

2. Costs After Optimization

I updated the estimate to reflect the optimized setup:

- EC2 instance: t3.micro
- EBS storage: 20 GB
- RDS unchanged

[Calculator after optimization](./images/MN-01-calculator-after.png)

**Estimated Monthly Cost (After Optimization): $25.18**


3. Cost Savings Calculation

I compared the two estimates:

- Before Optimization: $35.60  
- After Optimization: $25.18  

**Projected Monthly Savings: $10.42**

[Cost comparison](./images/MN-01-cost-comparison.png)


## Conclusion

In this lab, I successfully optimized the Café web application infrastructure by removing an unused local database and downsizing the EC2 instance. 
These changes reduced both compute and storage costs without affecting application functionality.

Using the AWS Pricing Calculator, I confirmed that the optimizations resulted in an estimated monthly savings of $10.42. This exercise demonstrated 
how small architectural improvements can lead to meaningful cost reductions in cloud environments while maintaining performance and reliability.

In summary:
- I optimized an Amazon Elastic Compute Cloud (Amazon EC2) instance to reduce costs.
- I used the AWS Pricing Calculator to estimate AWS service costs.

## Bash Commands

```bash
# Stop the MariaDB service on the CafeInstance
sudo systemctl stop mariadb

# Remove the MariaDB server package from the CafeInstance
sudo yum -y remove mariadb-server

# Retrieve the AWS region from the instance metadata
curl http://169.254.169.254/latest/dynamic/instance-identity/document | grep region

# Configure AWS CLI with credentials, region, and output format
aws configure

# Describe EC2 instances filtered by the CafeInstance tag to get the instance ID
aws ec2 describe-instances \
--filters "Name=tag:Name,Values= CafeInstance" \
--query "Reservations[*].Instances[*].InstanceId"

# Stop the CafeInstance EC2 instance (replace <instance-id> with actual ID)
aws ec2 stop-instances --instance-ids <instance-id>

# Modify the instance type to t3.micro (replace <instance-id> with actual ID)
aws ec2 modify-instance-attribute \
--instance-id <instance-id> \
--instance-type "{\"Value\": \"t3.micro\"}"

# Start the CafeInstance EC2 instance (replace <instance-id> with actual ID)
aws ec2 start-instances --instance-ids <instance-id>

# Check instance details including type, DNS, IP, and status (replace <instance-id>)
aws ec2 describe-instances \
--instance-ids <instance-id> \
--query "Reservations[*].Instances[*].[InstanceType,PublicDnsName,PublicIpAddress,State.Name]"
```
