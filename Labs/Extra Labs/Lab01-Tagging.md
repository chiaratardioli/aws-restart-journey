# Managing Resources with Tagging

This lab explores how AWS resource tagging can be used to organize, identify, and manage EC2 instances efficiently. 
Tagging enables automation of operational tasks such as filtering, updating, stopping, starting, and terminating instances 
based on metadata rather than manual selection. The lab demonstrates practical use of AWS CLI commands and scripts to manage 
instances in a structured environment using tags like Project, Environment, and Version.


## Task 1: Inspecting and Updating Tags Using AWS CLI

I began by accessing the CommandHost instance where AWS CLI was preconfigured. My first step was to identify EC2 instances associated with the 
`ERPSystem` project using tag-based filtering.

I ran the following command:

```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
````

This returned all instances linked to the ERPSystem project. However, the output was too detailed, so I refined it using JMESPath queries.

To extract only instance IDs, I used:

```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].InstanceId'
```

To improve readability, I included both Instance ID and Availability Zone:

```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone}'
```

I then extended the query to include custom tags (Project, Environment, Version):

```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Project:Tags[?Key==`Project`] | [0].Value,Environment:Tags[?Key==`Environment`] | [0].Value,Version:Tags[?Key==`Version`] | [0].Value}'
```

To focus only on development instances, I applied an additional filter:

```bash
aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development"
```

This confirmed only development instances were selected.

### Updating the Version Tag

I edited the provided script:

```bash
nano change-resource-tags.sh
```

The script identified development instances and updated their Version tag from `1.0` to `1.1` using:

```bash
aws ec2 create-tags --resources $ids --tags 'Key=Version,Value=1.1'
```

I executed the script:

```bash
./change-resource-tags.sh
```

Finally, I verified the update using the same describe-instances command and confirmed that only development instances had their version updated.

[Text](./images/EX-01-version-update-verification.png)

## Task 2: Stopping and Starting Instances by Tag

I navigated to the tools directory:

```bash
cd aws-tools
```

I inspected the script:

```bash
nano stopinator.php
```

The script uses AWS SDK for PHP to stop or start instances based on tag filters.

To stop development instances:

```bash
./stopinator.php -t"Project=ERPSystem;Environment=development"
```

The script identified two instances and stopped them.

I verified the status in the AWS EC2 console:

[Text](./images/EX-01-instances-stopping.png)

Next, I restarted them using:

```bash
./stopinator.php -t"Project=ERPSystem;Environment=development" -s
```

I confirmed that both instances returned to running state.

[Text](./images/EX-01-instances-restarting.png)

## Task 3: Challenge – Terminate Non-Compliant Instances

In this challenge, I worked on identifying and terminating instances that did not have the required `Environment` tag.

I reviewed the provided script:

```bash
nano terminate-instances.php
```

The script performs three key actions:

1. Retrieves instances with the `Environment` tag.
2. Compares them against all instances in a subnet.
3. Identifies and terminates those missing the required tag.

To simulate non-compliance, I removed the `Environment` tag from two instances using the EC2 console.

[Text](./images/EX-01-remove-environment-tag.png)

Then I executed the script:

```bash
./terminate-instances.php -region <region> -subnetid <subnet-id>
```

The script detected non-compliant instances and terminated them automatically.

[Text](./images/EX-01-terminated-instances.png)

## Conclusion

This lab demonstrated how AWS tagging can be effectively used to manage and automate EC2 instance operations. I learned how to filter resources 
using AWS CLI, manipulate output using JMESPath queries, and automate tagging operations through scripts. Additionally, I gained practical 
experience using tags to control instance lifecycle actions such as stopping, starting, and terminating resources. Overall, tagging proved to be a 
powerful method for organizing and managing cloud infrastructure efficiently.

In summary:
- I applied tags to existing AWS resources.
- I find resources based on tags.
- I used the AWS CLI or AWS SDK for PHP to stop and terminate Amazon EC2 instances based on certain attributes of the resource.
