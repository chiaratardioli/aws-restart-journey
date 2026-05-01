# Troubleshoot CloudFormation – Lab Report

## Introduction

This lab focused on developing practical skills for troubleshooting AWS CloudFormation deployments. The activity covered querying JSON data using JMESPath, 
identifying and resolving stack creation failures, analyzing EC2 instance logs, detecting configuration drift, and resolving issues encountered during stack deletion. 
The goal was to better understand how infrastructure as code (IaC) behaves in real-world scenarios and how to diagnose and fix deployment problems efficiently.

The architectural diagram is illustrated below.

![Architecture](./images/EX-02-architecture.png)


## Task 1: Querying JSON Data with JMESPath

In this task, I explored how to use JMESPath expressions to extract specific data from JSON documents. I practiced selecting elements using array indices, retrieving attributes, and applying filters.

I successfully:
- Retrieved specific elements using index-based queries.
- Extracted attributes such as `name` and `price`.
- Used projections to return values from all elements.
- Applied filters to locate elements without knowing their position.

Finally, I constructed a query to extract the `LogicalResourceId` of an EC2 instance:

```
StackResources[?ResourceType == 'AWS::EC2::Instance'].LogicalResourceId
```

This exercise helped me understand how JMESPath is used within AWS CLI commands.

![JMESPath Query Results](./images/EX-04-jmespath-results.png)


## Task 2: Troubleshooting CloudFormation Stack Creation

#### Connecting to CLI Host and Configuring AWS CLI

I connected to the CLI Host EC2 instance using SSH and configured the AWS CLI with the provided credentials and region.

![CLI Configuration](./images/EX-04-cli-config.png)

#### Initial Stack Creation Attempt

I attempted to create a CloudFormation stack using a provided template. The stack creation failed, and resources were rolled back automatically.

Using CLI commands, I monitored:
- Resource creation status
- Stack status
- Stack events

The error indicated that the `WaitCondition` resource timed out.

![Stack Failure](./images/EX-04-stack-failure.png)

#### Investigating the Failure

To debug the issue, I recreated the stack with rollback disabled. This allowed me to access the EC2 instance logs.

I connected to the web server instance and examined:

- `/var/log/cloud-init-output.log`
- User data script (`part-001`)

I identified the issue:
- The script attempted to install a package named `http`, which does not exist.

Because of the `-e` flag in the script, the failure caused the entire script to stop, preventing the success signal required by the `WaitCondition`.

![Cloud-init Log Error](./images/EX-04-cloud-init-error.png)

#### Fixing the Template

I edited the CloudFormation template and replaced:

```
yum install -y http
```

with:

```
yum install -y httpd
```

After saving the changes, I deleted the failed stack and created a new one.

This time, the stack creation completed successfully.

![Successful Stack Creation](./images/EX-04-stack-success.png)

#### Verifying the Web Server

I accessed the web server using its public IP address and confirmed that it displayed the expected message.

![Web Server Output](./images/EX-04-web-server.png)


## Task 3: Drift Detection

#### Manual Modification

I manually modified the security group by restricting SSH access to my IP address.

![Security Group Change](./images/EX-04-sg-change.png)

I also uploaded a file to the S3 bucket created by the stack.

![S3 Upload](./images/EX-04-s3-upload.png)

#### Detecting Drift

I initiated drift detection using the AWS CLI and analyzed the results.

Findings:
- The security group showed a status of `MODIFIED`.
- The S3 bucket remained `IN_SYNC` because adding objects does not count as drift.

![Drift Detection Results](./images/EX-04-drift-results.png)

This demonstrated that CloudFormation detects configuration changes but not data changes within resources.


### Task 4: Stack Deletion and Troubleshooting

#### Failed Deletion Attempt

I attempted to delete the stack, but the process failed due to the S3 bucket containing objects.

![Delete Failure](./images/EX-04-delete-failure.png)

CloudFormation does not delete non-empty buckets to prevent data loss.

#### Resolving the Issue

To resolve this, I used the AWS CLI option to retain the S3 bucket during deletion.

Steps:
1. Retrieved the logical resource ID of the bucket.
2. Executed the delete command with the `--retain-resources` parameter.

Example:

```
aws cloudformation delete-stack 
--stack-name myStack 
--retain-resources MyBucket
```

This allowed the stack to be deleted successfully while preserving the bucket and its contents.

![Successful Deletion](./images/EX-04-delete-success.png)


## Conclusion

In this lab, I learned how to troubleshoot CloudFormation deployments by analyzing stack events, inspecting EC2 logs, and identifying configuration issues in templates. I gained hands-on experience using JMESPath for querying CLI outputs, which improved my ability to extract relevant information efficiently.

I also understood the importance of disabling rollback during debugging and how small configuration errors can lead to stack failures. Additionally, I explored drift detection and observed how manual changes affect infrastructure managed by CloudFormation.

Finally, I resolved a failed stack deletion scenario by retaining specific resources, demonstrating how to manage dependencies and prevent data loss. This lab provided practical insight into managing infrastructure as code and reinforced best practices for debugging and maintaining AWS environments.
```
