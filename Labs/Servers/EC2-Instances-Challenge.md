# Amazon EC2 Instances (Challenge)
In this challenge I will create a web application running on an Amazon Linux EC2 instance.

## Task 1: Create an Amazon Linux EC2 instance to run a web application
I will use the AWS Management Console to launch the instance.

1. Before launching the instance, I create an internet gateway and properly configure the subnet's route table in your VPC.

2. I use an Amazon Linux Amazon Machine Image (AMI) and a `t3.small` instance type.

3. I launch the instance in a new virtual private cloud (VPC) and a new subnet, and auto-assign the instance's public IPv4 address.

4. In the user data, I install and start the httpd service as your web server. I give write permission to users to the web server's document root directory (/var/www/html).

5. I use a General Purpose SSD (gp2) volume type for the root volume.

6. I configure the instance, and create the necessary resources so that you I connect to it by using Secure Shell (SSH):
- Security group settings to allow for SSH and HTTP traffic.

Capture a screenshot of the EC2 instance's system log showing that the httpd service was successfully installed.

![My EC2 Instance Challenge](./images/challenge-ec3-instance.png)

noete: To make the EC2 instance accessible from the internet, I attached an Internet Gateway to the VPC, updated the route table to allow internet traffic, placed the instance in a public subnet with a public IP, and configured the security group to allow HTTP and SSH access.

## Task 2: Deploy and test the web page

1. I use EC2 Instance Connect to connect to your EC2 instance.

2. I create a file called `projects.html` with text:   
```bash
<!DOCTYPE html>
<html>
<body>
<h1>CHIARA's re/Start Project Work</h1>
<p>EC2 Instance Challenge Lab</p>
</body>
</html>
```
and save it in the `/var/www/html` directory of my EC2 instance (sudo).

3. I open a web browser, and navigate to the public IPv4 webpage. Here the results!

![My Web Application Challenge](./images/challenge-web-application.png)
