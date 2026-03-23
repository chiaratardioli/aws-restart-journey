# Activity - Working with AWS Lambda

In this lab, I will deploy and configure an AWS Lambda based serverless computing solution. 
The Lambda function generates a sales analysis report by pulling data from a database and emailing the results daily. 
The database connection information is stored in Parameter Store, a capability of AWS Systems Manager. 
The database itself runs on an Amazon Elastic Compute Cloud (Amazon EC2) Linux, Apache, MySQL, and PHP (LAMP) instance.

The following diagram shows the architecture of the sales analysis report solution and illustrates the order in which actions occur.

![AWS Lambda Architecture](./images/lab01-architecture.png)

## Sales Analysis Report Workflow

| Step | Details |
|------|---------|
| 1 | An Amazon CloudWatch Events event calls the `salesAnalysisReport` Lambda function at 8 PM every day Monday through Saturday. |
| 2 | The `salesAnalysisReport` Lambda function invokes another Lambda function, `salesAnalysisReportDataExtractor`, to retrieve the report data. |
| 3 | The `salesAnalysisReportDataExtractor` function runs an analytical query against the café database (`cafe_db`). |
| 4 | The query result is returned to the `salesAnalysisReport` function. |
| 5 | The `salesAnalysisReport` function formats the report into a message and publishes it to the `salesAnalysisReportTopic` Amazon SNS topic. |
| 6 | The `salesAnalysisReportTopic` SNS topic sends the message by email to the administrator. |

## Task 1: Observing the IAM role settings

1. The **salesAnalysisReportRole** IAM role has 4 policies:
- **AmazonSNSFullAccess** provides full access to Amazon SNS resources.
- **AmazonSSMReadOnlyAccess** provides read-only access to Systems Manager resources.
- **AWSLambdaBasicRunRole** provides write permissions to CloudWatch logs (which are required by every Lambda function).
- **AWSLambdaRole** gives a Lambda function the ability to invoke another Lambda function.  
Besides, *lambda.amazonaws.com* is listed as a trusted entity, which means that the Lambda service can use this role.

3. The **salesAnalysisReportDERole** IAM role has 2 policies:
- **AWSLambdaBasicRunRole** provides write permissions to CloudWatch logs.
- **AWSLambdaVPCAccessRunRole** provides permissions to manage elastic network interfaces to connect a function to a virtual private cloud (VPC).
Besides, *lambda.amazonaws.com* is listed as a trusted entity.

## Task 2: Creating a Lambda layer and a data extractor Lambda function
1. Creating a Lambda Layer
2. Creating a data extractor Lambda function
3. Adding the Lambda layer to the function
4. Importing the code for the data extractor Lambda function
5. Configuring network settings for the function

## Task 3: Testing the data extractor Lambda function

1. Launching a test of the Lambda function
2. Troubleshooting the data extractor Lambda function
3. Analyzing and correcting the Lambda function
4. Placing an order and testing again

## Task 4: Configuring notifications

1. Creating an SNS topic
2. Subscribing to the SNS topic

## Task 5: Creating the salesAnalysisReport Lambda function

1. Connecting to the CLI Host instance
2. Configuring the AWS CLI
3. Creating the salesAnalysisReport Lambda function using the AWS CLI
4. Configuring the salesAnalysisReport Lambda function
5. Testing the salesAnalysisReport Lambda function
6. Adding a trigger to the salesAnalysisReport Lambda function

## 

## Conclusions
In this lab I learnt the followings.
- Recognize necessary AWS Identity and Access Management (IAM) policy permissions to facilitate a Lambda function to other Amazon Web Services (AWS) resources.
- Create a Lambda layer to satisfy an external library dependency.
- Create Lambda functions that extract data from database, and send reports to user.
- Deploy and test a Lambda function that is initiated based on a schedule and that invokes another function.
- Use CloudWatch logs to troubleshoot any issues running a Lambda function.



