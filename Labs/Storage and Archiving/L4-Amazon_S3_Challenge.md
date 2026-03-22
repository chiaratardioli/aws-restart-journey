# Challenge Lab: Amazon S3
In this challenge lab, I will create an Amazon Simple Storage Service (Amazon S3) bucket and perform some routine tasks, 
such as uploading objects and configuring permissions to make those objects publicly accessible through a browser.

## Objectives
- Create an S3 bucket. 
- Upload an object into this bucket. 
- Access the object by using a web browser. 
- List the contents of the S3 bucket by using the AWS Command Line Interface (AWS CLI).

## Task 1: Connecting to the CLI Host instance
On the AWS Management Console, in the Search bar, I enter and choose EC2 to open the EC2 Management Console.
Then I select **CLI Host** instance from the available instances and choose Connect.
On the EC2 Instance Connect tab, I click Connect.
```bash

```

## Task 2: Configuring the AWS CLI
To set up the AWS CLI profile with credentials I run the command `aws configure` with options:
- **AWS Access Key ID**:`ccessKey`
- **AWS Secret Access Key**: `SecretKey`
- **Default region name**: `us-west-2`
- **Default output format**: `json`

```bash

```

## Task 3: Finishing the challenge

1. I create an S3 bucket.

2. I upload an object into this bucket.

3. I try to access the object by using a web browser.

4. I make the object (not the bucket) publicly accessible.

5. I access the object by using a web browser.

6. I list the contents of the S3 bucket by using the AWS CLI. 

## Conclusion
In this lab I learnt how to:
- Created an S3 bucket
- Uploaded an object into this bucket
- Accessed the object by using a web browser
- Listed the contents of the S3 bucket by using AWS CLI

## Additional resources
- ![S3 CLI Command Reference](https://docs.aws.amazon.com/cli/latest/reference/s3/)
- ![Getting Started with Amazon S3](https://aws.amazon.com/s3/getting-started/)
- ![How Can I Grant Public Read Access to Some Objects in My Amazon S3 Bucket?](https://repost.aws/knowledge-center/read-access-objects-s3-bucket)
- ![Connect to Your Linux Instance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/connect-to-linux-instance.html)

