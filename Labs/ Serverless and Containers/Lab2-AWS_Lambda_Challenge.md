# AWS Lambda Exercise (Challenge)

In this challenge lab, I will create an AWS Lambda function to count the number of words in a text file.

## Challenge 1: Create a Lambda function to count the number of words in a text file. 

1. Use the AWS Management Console to develop a Lambda function in Python and create the function's required resources.
2. Report the word count in an email by using an SNS topic. Optionally, also send the result in an SMS (text) message.
3. Format the response message as follows:
   - The word count in the <textFileName> file is nnn. 
   - Replace <textFileName> with the name of the file.
4. Enter the following text as the email subject: Word Count Result
5. Automatically invoke the function when the text file is uploaded to an S3 bucket.

## Challenge 2: Test the function by uploading a few sample text files with different word counts to the S3 bucket.

## Challenge 3: Forward the email that one of your tests produces and a screenshot of your Lambda function to your instructor.

## Conclusion
In this lab, I learnt how to:
- Create a Lambda function to count the number of words in a text file.
- Configure an Amazon Simple Storage Service (Amazon S3) bucket to invoke a Lambda function when a text file is uploaded to the S3 bucket.
- Create an Amazon Simple Notification Service (Amazon SNS) topic to report the word count in an email.


## Additional resources
- [What is AWS Lambda?](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)
- [Using an Amazon S3 trigger to invoke a Lambda function](https://docs.aws.amazon.com/lambda/latest/dg/with-s3-example.html)
- [AWS managed policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies)

