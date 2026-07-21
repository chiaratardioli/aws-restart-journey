# Lab Report: Implementing a Serverless Architecture on AWS

**Lab:** Module 13 – Guided Lab 2: Implementing a Serverless Architecture on AWS
**Scenario:** Build an inventory tracking system for stores worldwide. Stores upload inventory files to Amazon S3, which triggers an AWS Lambda function that loads the data into an Amazon DynamoDB table. A serverless dashboard displays inventory levels, and a second Lambda function monitors stock and sends a notification through Amazon SNS when an item is out of stock.

## Introduction

This lab implements a fully serverless, event-driven inventory tracking system on AWS, without provisioning or managing any servers. The architecture chains four managed services together: Amazon S3 receives inventory files, AWS Lambda processes them and writes to Amazon DynamoDB, a DynamoDB Stream triggers a second Lambda function that checks stock levels, and Amazon SNS delivers out-of-stock notifications by email. The solution demonstrates key serverless principles: automatic scaling, pay-per-use billing, and loose coupling between independent, single-purpose functions.

## Task 1: Create the Lambda Function to Load Data

I created a Lambda function named `Load-Inventory` (Python 3.9), using an existing execution role scoped with the permissions needed to read from S3 and write to DynamoDB. I deployed the provided handler code, which:

- Downloads the CSV file from the S3 bucket that triggered the event
- Parses each row with `csv.DictReader`
- Writes each row (`Store`, `Item`, `Count`) into the DynamoDB `Inventory` table using `put_item`

This function is not invoked directly; it is designed to run only in response to an S3 event, which I configured in the next task.

![Load-Inventory Lambda function configuration](./images/01-01-load-inventory-lambda.png)

## Task 2: Configure the Amazon S3 Event Trigger

I created an S3 bucket (`inventory-<random-number>`) to serve as the upload endpoint for stores. In the bucket's **Properties**, I added an event notification (`Load-Inventory`) for **All object create events**, with the destination set to the `Load-Inventory` Lambda function. This wires the two services together: any object uploaded to the bucket now automatically invokes the Lambda function, with no polling or scheduling required.

![S3 event notification configuration](./images/02-01-s3-event-trigger.png)

## Task 3: Test the Loading Process

I uploaded a sample inventory CSV file (store, item, count columns) to the S3 bucket. This upload triggered the `Load-Inventory` function, which parsed the file and inserted the records into DynamoDB.

I verified the result in two ways: through the serverless dashboard application (a static site on S3 that authenticates anonymously via Amazon Cognito and reads directly from DynamoDB), and by inspecting the `Inventory` table's Items tab in the DynamoDB console.

![Inventory dashboard displaying uploaded data](./images/03-01-inventory-dashboard.png)

![DynamoDB Inventory table items](./images/03-02-dynamodb-items.png)

## Task 4: Configure Notifications with Amazon SNS

I created an SNS topic named `NoStock` (Standard type) to handle out-of-stock alerts. I then created an email subscription to the topic using my own address and confirmed it via the confirmation link sent by Amazon SNS. Any message published to this topic from this point on is delivered directly to my inbox.

![SNS topic and email subscription](./images/04-01-sns-topic-subscription.png)

## Task 5: Create the Lambda Function to Send Notifications

Rather than embedding stock-checking logic into `Load-Inventory`, I created a second, single-purpose function named `Check-Stock` (Python 3.9) with its own execution role scoped for SNS access. This separation keeps each function focused on one responsibility and lets new business logic be added independently without affecting the existing load pipeline.

I deployed the provided handler code, which:

- Iterates over the incoming DynamoDB stream records
- Checks the `Count` value of each new/updated item
- If `Count` equals zero, looks up the `NoStock` topic ARN and publishes an "Inventory Alert!" message identifying the store and item

I then added a **DynamoDB trigger** to the function, pointing at the `Inventory` table, so it fires automatically whenever the table is updated by the loading process.

![Check-Stock Lambda function and DynamoDB trigger](./images/05-01-check-stock-lambda-trigger.png)

## Task 6: Test the End-to-End System

I uploaded another inventory file to the S3 bucket to exercise the full pipeline: S3 → `Load-Inventory` Lambda → DynamoDB → DynamoDB Stream → `Check-Stock` Lambda → SNS → email. I refreshed the dashboard and confirmed the new store's data appeared. Shortly after, I received an email notification for the item with zero stock, confirming that every stage of the event-driven chain worked correctly end to end.

![Out-of-stock email notification received](./images/06-01-out-of-stock-email.png)

Uploading multiple inventory files at the same time would trigger multiple concurrent, independent invocations of `Load-Inventory`, since Lambda scales out automatically per event rather than queuing them behind a single instance. Each file would be processed in parallel and would independently trigger `Check-Stock` for any resulting DynamoDB writes.

## Conclusion

I implemented a complete serverless inventory tracking system using Amazon S3, AWS Lambda, Amazon DynamoDB, and Amazon SNS, with Amazon Cognito supporting anonymous read access for the dashboard. This lab reinforced how event-driven, decoupled functions replace traditional server-based workflows: S3 events, DynamoDB Streams, and SNS topics act as the connective tissue between independent Lambda functions, each with a single, well-defined responsibility. I also saw firsthand how this design scales automatically with load and incurs cost only when it is actually used, since there is no idle compute to pay for. This project gave me practical, hands-on experience with the core AWS services used in production serverless architectures.
