# Introduction to Amazon DynamoDB

Amazon DynamoDB is a fast and flexible NoSQL database service for all applications that need consistent, 
single-digit millisecond latency at any scale. It is a fully managed database and supports both document
and key-value data models. Its flexible data model and reliable performance make it a great fit for mobile, 
web, gaming, ad-tech, Internet of Things (IoT), and many other applications.

In this lab, I will create a table in DynamoDB to store information about a music library. 
I will query the music library and then delete the DynamoDB table.

## Task 1: Create a new table
In DynamoDB each table requires a partition key (or a primary key) that is used to partition data across DynamoDB servers. 
A table can also have a sort key. The combination of a partition key and sort key uniquely identifies each item in a DynamoDB table.

I create a new table in DynamoDB with this configuration:
* Table name: `Music`
* Partition key: `Artist` (String)
* Sort key - optional: `Song` (String)

![DynamoDB Music Table](./imanges/lab09-dynamoDB-music.png)

## Task 2: Add data


## Task 3: Modify an existing item


## Task 4: Query the table


## Task 5: Delete the table

## Conclusion
* I created an Amazon DynamoDB table
* I entered data into an Amazon DynamoDB table
* I queried an Amazon DynamoDB table
* I deleted an Amazon DynamoDB table

## Additional resources
* [DynamoDB documentation](http://aws.amazon.com/documentation/dynamodb)
