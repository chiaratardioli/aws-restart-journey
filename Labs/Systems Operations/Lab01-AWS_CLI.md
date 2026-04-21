# Install and Configure the AWS CLI

This lab focuses on the installation, configuration, and practical use of the **AWS Command Line Interface (AWS CLI**), a powerful tool that enables 
users to interact with Amazon Web Services (AWS) directly from a command-line environment. The AWS CLI provides an efficient way to manage cloud resources, 
automate tasks, and control AWS services without relying on the graphical web console.

Here, the AWS CLI is installed on a Red Hat Linux-based Amazon Elastic Compute Cloud (EC2) instance, which does not include the CLI by default. 
This setup highlights the manual installation and configuration process required for certain instance types, in contrast to others such as Amazon Linux 
that come pre-installed with the tool. A **Secure Shell (SSH)** connection is established to remotely access and manage the instance.

Once connected, the AWS CLI is configured using access credentials that enable secure interaction with an AWS account. The lab then explores basic 
command-line operations by interacting with AWS Identity and Access Management (IAM), allowing users to manage identities and permissions programmatically.

At the end of this lab, the resulting architecture consists of a Virtual Private Cloud (VPC) containing a Red Hat EC2 instance with the AWS CLI installed and configured. 
Through an SSH connection, the user accesses this instance and uses the CLI to communicate with IAM services. The diagram below illustrates this architecture, 
showing the relationship between the local environment, the EC2 instance, and AWS services within the cloud infrastructure.

![AWS CLI Final Architecture](./images/SO-01-architecture.png)

## Steps

1. I connect to the Red Hat EC2 instance by using SSH.
```bash
chiara@macbook-air:~/labs$ chmod 700 labsuser.pem 
chiara@macbook-air:~/labs$ ssh -i labsuser.pem ec2-user@35.93.48.118
The authenticity of host '35.93.48.118 (35.93.48.118)' can't be established.
ED25519 key fingerprint is SHA256:twvg2P0qHpbbuooZW2dcSQ6amXLRrwO7gcNXzefSbug.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '35.93.48.118' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-200-0-4 ~]$ 
```

2. I install the AWS CLI on a Red Hat Linux instance.
```bash
[ec2-user@ip-10-200-0-4 ~]$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 66.6M  100 66.6M    0     0   206M      0 --:--:-- --:--:-- --:--:--  206M
[ec2-user@ip-10-200-0-4 ~]$ unzip -u awscliv2.zip
Archive:  awscliv2.zip
   creating: aws/
   creating: aws/dist/
   ...
   inflating: aws/dist/prompt_toolkit-3.0.51.dist-info/licenses/AUTHORS.rst  
   inflating: aws/dist/prompt_toolkit-3.0.51.dist-info/licenses/LICENSE  
[ec2-user@ip-10-200-0-4 ~]$ sudo ./aws/install
You can now run: /usr/local/bin/aws --version
[ec2-user@ip-10-200-0-4 ~]$ aws --version
aws-cli/2.34.33 Python/3.14.4 Linux/4.14.355-281.714.amzn2.x86_64 exe/x86_64.amzn.2
[ec2-user@ip-10-200-0-4 ~]$ 
```

To verify that the AWS CLI is now working, I run the `aws help` command. The help command displays the information for the AWS CLI.

3. I observe IAM configuration details in the AWS Management Console.

Within the IAM dashboard, the *awsstudent* user is selected from the Users section.

![IAM User Record awsstudent](./images/SO-01-awsstudent-user.png)

In the Permissions tab, I click on the *lab_policy* and examine it in JSON format to understand the specific permissions granted to the user.

![IAM USer Lab Policy](./images/SO-01-lab-policy.png)

The *lab_policy* broadly allows the *awsstudent* user to perform most actions across services like EC2, CloudFormation, CloudWatch, IAM (read-only), 
and SSM, while explicitly denying certain advanced or cost-related EC2 operations such as reserved instances, spot instances, and capacity reservations.

Next, in the Security credentials tab, the access key ID associated with the awsstudent user is located. It is important to note that secret access keys 
must normally be saved at the time of creation; however, for this lab, both the access key ID and secret access key are provided in the lab instructions.

![IAM User Security Credentials](./images/SO-01-security-credentials.png)

4. I configure the AWS CLI to connect to my AWS Account:
```bash
[ec2-user@ip-10-200-0-4 ~]$ aws configure
AWS Access Key ID [None]: <AWS Access Key ID>
AWS Secret Access Key [None]: <AWS Secret Access Key>
Default region name [None]: us-west-2
Default output format [None]: json
[ec2-user@ip-10-200-0-4 ~]$ 
```

5. I observe IAM configuration details by using the AWS CLI:
```bash
[ec2-user@ip-10-200-0-4 ~]$ aws iam list-users

{
    "Users": [
        {
            "Path": "/",
            "UserName": "awsstudent",
            "UserId": "AIDAVD4OE6YMB7S5J65SZ",
            "Arn": "arn:aws:iam::351948568088:user/awsstudent",
            "CreateDate": "2026-04-21T08:44:07+00:00"
        }
    ]
}
[ec2-user@ip-10-200-0-4 ~]$ 
```

## Challenge
In this challenge I use the [AWS CLI Command Reference documentation](https://docs.aws.amazon.com/cli/latest/reference/iam/) and 
AWS CLI to download the *lab_policy document* in a JSON-formatted IAM policy document. 

1. I list all IAM customer managed policies by filtering the scope to local.
```bash
[ec2-user@ip-10-200-0-4 ~]$ aws iam list-policies --scope Local
{
    "Policies": [
        {
            "PolicyName": "lab_policy",
            "PolicyId": "ANPAVD4OE6YMFF3KNO7DW",
            "Arn": "arn:aws:iam::351948568088:policy/lab_policy",
            "Path": "/",
            "DefaultVersionId": "v1",
            "AttachmentCount": 1,
            "PermissionsBoundaryUsageCount": 0,
            "IsAttachable": true,
            "CreateDate": "2026-04-21T08:44:45+00:00",
            "UpdateDate": "2026-04-21T08:44:45+00:00"
        }
    ]
}
```

2. I use the version number *Arn* information and *DefaultVersionId* found inside the lab_policy document to retrieve the JSON IAM policy. 
I use the > command to save the file.

```bash
[ec2-user@ip-10-200-0-4 ~]$ aws iam get-policy-version --policy-arn arn:aws:iam::351948568088:policy/lab_policy --version-id v1 > lab_policy.json
[ec2-user@ip-10-200-0-4 ~]$ ls -ltr
total 68236
drwxr-xr-x 3 ec2-user ec2-user       78 Apr 20 18:21 aws
-rw-rw-r-- 1 ec2-user ec2-user 69864275 Apr 21 09:11 awscliv2.zip
-rw-rw-r-- 1 ec2-user ec2-user     5035 Apr 21 10:11 lab_policy.json
[ec2-user@ip-10-200-0-4 ~]$ head -n 10 lab_policy.json 
{
    "PolicyVersion": {
        "Document": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": [
                        "cloudformation:List*",
                        "cloudformation:Describe*",
                        "cloudformation:Detect*",
```

I note that the file *lab_policy.json* is the same document that is in the AWS Management Console.

## Conclusion
- I installed and configured the AWS CLI
- I connected the AWS CLI to an AWS account
- I accessed IAM by using the AWS CLI
- I used the AWS CLI to retrieve policy information by referencing AWS documentation.
- I can use the AWS CLI to manage and control multiple AWS services through the command line. I can also accomplish these tasks by using the AWS Management Console.
- To connect to the same AWS account, the AWS CLI needed an access key ID and secret access key. To sign in to the AWS Management Console, I need a user name and password.

## Additional resources
- [IAM AWS CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/iam/index.html)
- [Installing or Updating the Latest Version of the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [Troubleshooting AWS CLI Errors](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-troubleshooting.html)

## Useful AWS CLI commands
```bash
# Write the downloaded file to the current directory, option -o rename the file
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"

# Unzip the installer, option -u option to skip prompts asking you to overwrite any existing files
unzip -u awscliv2.zip

# Run the install program - The sudo command grants write permissions to the directory
sudo ./aws/install

# Confirm the installation
aws --version

# Verify that the AWS CLI is now working - The help command displays the information for the AWS CLI - type q to exit
aws help

# Confugure AWS CLI
aws configure

# List IAM users in the account
aws iam list-users

# Set the scope to local
aws iam list-policies --scope Local

# Returns the policy document for the v1 version of the policy whose ARN is arn:aws:iam::351948568088:policy/lab_policy
aws iam get-policy-version \
    --policy-arn arn:aws:iam::351948568088:policy/lab_policy \
    --version-id v1
```
