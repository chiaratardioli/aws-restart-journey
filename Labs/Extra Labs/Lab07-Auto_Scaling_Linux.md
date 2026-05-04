# Using Auto Scaling in AWS (Linux)

This lab demonstrates how to build a scalable and highly available web application infrastructure using Amazon Web Services. 
It combines the use of the AWS Command Line Interface (AWS CLI), Amazon EC2, Auto Scaling, and Elastic Load Balancing to dynamically 
respond to changes in workload. The goal is to automate instance provisioning, distribute traffic efficiently, and maintain application 
performance under varying load conditions.

The architecture evolves from a single command host instance to a distributed system with multiple EC2 instances managed by an Auto Scaling 
group and balanced by an Application Load Balancer across multiple Availability Zones.

![Starting Architecture](./images/EX-07-starting-architecture.png)

![Final Architecture](./images/EX-07-final-architecture.png)

## Task 1: Creating a New AMI for Amazon EC2 Auto Scaling

### 1.1 Connecting to the Command Host Instance

I began by accessing the EC2 Management Console and connecting to the **Command Host** instance using EC2 Instance Connect. This instance provided a preconfigured environment where I could execute AWS CLI commands required for the lab.

![Connect Command Host](./images/EX-07-connect-command-host.png)

### 1.2 Configuring the AWS CLI

After connecting, I verified the AWS Region using a metadata query and configured the AWS CLI with the appropriate region and output format. This ensured that all subsequent commands were executed in the correct environment.

![AWS CLI Configuration](./images/EX-07-aws-cli-config.png)

### 1.3 Creating a New EC2 Instance

I inspected the provided `UserData.txt` script, which installs and configures a web server capable of generating CPU load. Then, I executed an AWS CLI command to launch a new EC2 instance using the specified parameters such as AMI ID, subnet, and security group.

After launching the instance, I waited until it reached the running state and retrieved its public DNS name. I accessed the web application through the browser to confirm that the web server was functioning correctly.

![EC2 Instance Creation](./images/EX-07-ec2-instance.png)

### 1.4 Creating a Custom AMI

Next, I created a custom AMI from the running EC2 instance using the AWS CLI. This AMI captured the configured web server environment and would later be used to launch identical instances in the Auto Scaling group.

![Create AMI CLI](./images/EX-07-create-ami.png)

## Task 2: Creating an Auto Scaling Environment

### Task 2.1: Creating an Application Load Balancer

I created an Application Load Balancer named **WebServerELB**. I configured it to operate across two Availability Zones and associated it with public subnets. I also created a target group named **webserver-app** with a health check path of `/index.php`.

After setup, I copied the DNS name of the load balancer for later testing.

![Load Balancer Setup](./images/EX-07-load-balancer.png)

### 2.2 Creating a Launch Template

I created a launch template named **web-app-launch-template** using the custom AMI created earlier. I selected the instance type `t3.micro` and assigned the HTTPAccess security group. This template defines how new instances are launched within the Auto Scaling group.

![Launch Template](./images/EX-07-launch-template.png)

### 2.3 Creating an Auto Scaling Group

Using the launch template, I created an Auto Scaling group named **Web App Auto Scaling Group**. I configured it to launch instances in private subnets across two Availability Zones.

I attached the group to the target group created earlier and enabled load balancer health checks. I set the desired capacity to 2, minimum to 2, and maximum to 4 instances. I also configured a target tracking scaling policy to maintain average CPU utilization at 50%.

![Auto Scaling Group](./images/EX-07-auto-scaling-group.png)

## Task 3: Verifying the Auto Scaling Configuration

I verified that two EC2 instances were automatically launched by the Auto Scaling group. I waited until both instances passed their status checks.

Then, I checked the target group and confirmed that both instances were registered and marked as healthy. This indicated that the load balancer was correctly routing traffic to the instances.

![Healthy Instances](./images/EX-07-healthy-instances.png)

## Task 4: Testing Auto Scaling Configuration

To test the scaling behavior, I accessed the web application using the load balancer DNS and initiated the **Start Stress** function. This caused CPU utilization to increase significantly.

I monitored the Auto Scaling group activity and observed that a new EC2 instance was launched after CPU utilization exceeded the defined threshold. This confirmed that the scaling policy was working correctly.

![Scaling Activity](./images/EX-07-scaling-activity.png)

## Conclusion

In this lab, I successfully created and configured a scalable web application infrastructure using AWS services.

I used the AWS CLI to launch an EC2 instance and create a custom AMI. I then configured an Application Load Balancer to distribute incoming traffic and created a launch template to standardize instance configuration. Using this template, I deployed an Auto Scaling group that dynamically adjusted the number of instances based on CPU utilization.

Finally, I validated the system by generating load and observing automatic scaling behavior. This lab demonstrated how to combine AWS services to build a resilient, efficient, and scalable cloud architecture.
