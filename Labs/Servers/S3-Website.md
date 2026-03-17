# Creating a Website on S3

In this lab I used the AWS Command Line Interface (AWS CLI) commands from an Amazon Elastic Compute Cloud (Amazon EC2) instance to:
- Create an Amazon Simple Storage Service (Amazon S3) bucket.
- Create a new AWS Identity and Access Management (IAM) user that has full access to the Amazon S3 service.
- Upload files to Amazon S3 to host a simple website for the Café & Bakery.
- Create a batch file that can be used to update the static website when you change any of the website files locally.

![S3 Website Architecture](./images/s3-website-overview)

## Task 1: Connect to an Amazon Linux EC2 instance using SSM

## Task 2: Configure the AWS CLI
Amazon Linux has already **AWS CLI** pre-installed. I run the command `aws configure` to update the AWS CLI software with credentials:
- AWS Access Key ID: from  the lab details
- AWS Secret Access Key: from  the lab details
- Default region name: us-west-2
- Default output format: json

## Task 3: Create an S3 bucket using the AWS CLI
The `s3api` command creates a new **S3 bucket** with the AWS credentials in this lab. By default, the S3 bucket is created in the us-east-1 Region.
Bucket must have a unique name, here I used `ctardi256`.
```bash
aws s3api create-bucket --bucket ctardi256 --region us-west-2 --create-bucket-configuration LocationConstraint=us-west-2
{
        "Location": "http://twhitlock256.s3.amazonaws.com/"
}
```

## Task 4: Create a new IAM user that has full access to Amazon S3
The AWS CLI command `aws iam create-user` creates a new IAM user for your AWS account. The option `--user-name` is used to create the name of the user and must be unique within the account.  Then the AWS CLI command `aws iam create-login-profile` creates a login profile for the new user.
```bash
aws iam create-user --user-name awsS3user
aws iam create-login-profile --user-name awsS3user --password Training123!
```
I login in with the new IAM user credentials:
- Account ID: ID of the account VocLabsUser from the AWS Management Console
- IAM user name: awsS3user
- password: Training123!

The IAM user didn't have access to the S3 bucket. Using the terminal I serach policy that grants full access to Amazon S3.
```bash
aws iam list-policies --query "Policies[?contains(PolicyName,'S3')]"
```
And after I found the policy, I and assigned it to the IAM user.
```bash
aws iam attach-user-policy --policy-arn arn:aws:iam::aws:policy/<policyYouFound> --user-name awsS3user
```

## Task 5: Adjust S3 bucket permissions
I changed the permission for the S3 bucket:
- Under Block public access (bucket settings), Block all public access: unchecked
- Under Object Ownership, ACLs enabled: selected
- Under Object Ownership, I acknowledge that ACLs will be restored: selected

## Task 6: Extract the files that you need for this lab
I extracted the file containing the static-website contents for the Amazon S3 bucket using the CLI.
```bash
cd ~/sysops-activity-files
tar xvzf static-website-v2.tar.gz
cd static-website
```
Among the files, there is one called `index.html`.

## Task 7: Upload files to Amazon S3 by using the AWS CLI
The files are extracted, you upload the contents of the file to Amazon S3 using the `s3` command. s3 commands are built on top of the operations that are found in the s3api commands.
1. In order to the the bucket to function as a website, I run the command `aws s3 website` with option `--index-document`. This process helps ensure that the index.html file will be known as the index document.
```bash
aws s3 website s3://ctardi256 --index-document index.html
```
2. To upload the files to the bucket, I run the command `aws s3 cp` with option `--recursive --acl public-read`. The access control list (ACL) parameter specifies that the uploaded files have public read access. It also includes the recursive parameter, which indicates that all files in the current directory on your machine should be uploaded.
```bash
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --recursive --acl public-read
```
3. To verify that all files were successfully uploaded I run the command `aws s3 ls ctardi256 `.

4. On AWS Management Console I checked that the Static website hosting is Enabled.

5. And here it is the bucket website endpoint URL in the browser!

![S3 Wesite](./images/s3-website.png)

## Task 8: Create a batch file to make updating the website repeatable
1. To create a repeatable deployment, I created a batch file called `update-website.sh` in the home directory.
```bash
#!/bin/bash
aws s3 cp /home/ec2-user/sysops-activity-files/static-website/ s3://<my-bucket>/ --recursive --acl public-read
```
2. Then I made some changes to the `sysops-activity-files/static-website/index.html` file:
- bgcolor="aquamarine" to bgcolor="gainsboro"
- bgcolor="orange" to bgcolor="cornsilk"
- bgcolor="aquamarine" to bgcolor="gainsboro"
3. Eventually, I run your batch file to update the website.
```bash
./update-website.sh
```
4. And here it is the uodated website!
![Updated S3 Wesite](./images/update-s3-website.png)

## Optional challenge
Use the `aws s3 sync` command to only copy the files that have been modified to the `S3 bucket`, increasing efficiency.
```bash
aws s3 sync /home/ec2-user/sysops-activity-files/static-website/<s3://<my-bucket>/ --acl public-read
```

# Conclusion
With this lab I learnt how to:
- Run AWS CLI commands that use IAM and Amazon S3 services.
- Deploy a static website to an S3 bucket.
- Create a script that uses the AWS CLI to copy files in a local directory to Amazon S3.
