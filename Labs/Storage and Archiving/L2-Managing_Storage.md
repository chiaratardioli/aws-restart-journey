# Managing Storage

AWS provides multiple ways to manage data on Amazon Elastic Block Store (Amazon EBS) volumes. 
In this lab, I will use AWS Command Line Interface (AWS CLI) to create snapshots of an EBS volume 
and configure a scheduler to run Python scripts to delete older snapshots.

In the challenge section, I will sync the contents of a directory on an EBS volume to an Amazon Simple 
Storage Service (Amazon S3) bucket using an Amazon S3 sync command.

![Managing Storage Archtecture](./images/managing-storage-archtecture.png)

This lab environment consists of a virtual private cloud (VPC) with a public subnet. Amazon Elastic Compute 
Cloud (Amazon EC2) instances named "Command Host" and "Processor" have already been created in this VPC.

The "Command Host" instance will be used to administer AWS resources including the "Processor" instance.

## Objectives
- Create and maintain snapshots for Amazon EC2 instances.
- Use Amazon S3 sync to copy files from an EBS volume to an S3 bucket.
- Use Amazon S3 versioning to retrieve deleted files.

## Task 1: Creating and configuring resources
I create an Amazon S3 bucket and configure the "Command Host" EC2 instance to have secure access to other AWS resources.

1. Create an S3 bucket
2. Attach instance profile to Processor

## Task 2: Taking snapshots of your instance
Here I use the AWS Command Line Interface (AWS CLI) to manage the processing of snapshots of an instance.

1. Connecting to the Command Host EC2 instance
2. Taking an initial snapshot
3. Scheduling the creation of subsequent snapshots
4. Retaining the last two snapshots

## Task 3: Challenge: Synchronize files with Amazon S3
Here I've been challenged to sync the contents of a directory with the Amazon S3 bucket that you created earlier.

1. Downloading and unzipping sample files
2. Syncing files

## Conclusion
In this lab I learnt how to:

- create and maintain snapshots for Amazon EC2 instances.
- use Amazon S3 sync to copy files from an EBS volume to an S3 bucket.
- use Amazon S3 versioning to retrieve deleted files.

