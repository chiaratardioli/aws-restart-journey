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

1. I create an S3 bucket named `s3-bucket-lab02-ct`.
2. I attach a pre-created IAM role `S3BucketAccessRole` as an instance profile to the EC2 instance **Processor**, 
giving it the permissions to interact with other AWS services such as EBS volumes and S3 buckets.

## Task 2: Taking snapshots of your instance
Here I use the AWS Command Line Interface (AWS CLI) to manage the processing of snapshots of an instance.

1. I connect to the Command Host EC2 instance.
```bash
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

[ec2-user@ip-10-5-0-109 ~]$
```

2. I shut down the "Processor" instance, which requires its instance ID using the following code.

```bash
#!/bin/bash
# Obtain the instance ID
INSTANCE_ID=$(aws ec2 describe-instances \
  --filters 'Name=tag:Name,Values=Processor' \
  --query 'Reservations[0].Instances[0].InstanceId' \
  --output text)
echo $INSTANCE_ID
# Shut down the "Processor" instance
aws ec2 stop-instances --instance-ids $INSTANCE_ID
# Verify that the "Processor" instance stopped
aws ec2 wait instance-stopped --instance-id $INSTANCE_ID
```

Here the output on screen.
```bash
[ec2-user@ip-10-5-0-109 ~]$ INSTANCE_ID=$(aws ec2 describe-instances \
>   --filters 'Name=tag:Name,Values=Processor' \
>   --query 'Reservations[0].Instances[0].InstanceId' \
>   --output text)
[ec2-user@ip-10-5-0-109 ~]$ echo $INSTANCE_ID
i-08e1f153a38133346
[ec2-user@ip-10-5-0-109 ~]$ # Shut down the "Processor" instance
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 stop-instances --instance-ids $INSTANCE_ID
{
    "StoppingInstances": [
        {
            "InstanceId": "i-08e1f153a38133346",
            "CurrentState": {
                "Code": 64,
                "Name": "stopping"
            },
            "PreviousState": {
                "Code": 16,
                "Name": "running"
            }
        }
    ]
}
[ec2-user@ip-10-5-0-109 ~]$ # Verify that the "Processor" instance stopped
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 wait instance-stopped --instance-id $INSTANCE_ID
[ec2-user@ip-10-5-0-109 ~]$ 
```

3. I take an initial snapshot.
```bash
#!/bin/bash
# Get the EBS volume-id
VOLUME_ID=$(aws ec2 describe-instances \
  --filter 'Name=tag:Name,Values=Processor' \
  --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.{VolumeId:VolumeId}' \
  --output text)
echo $VOLUME_ID
# Create the snapshot and save the Id
SNAPSHOT_ID=$(aws ec2 create-snapshot \
  --volume-id "$VOLUME_ID" \
  --query "SnapshotId" \
  --output text)
echo $SNAPSHOT_ID
# Verify the status of your snapshot,
aws ec2 wait snapshot-completed --snapshot-id $SNAPSHOT_ID
# Restart the "Processor" instance
aws ec2 start-instances --instance-ids $INSTANCE_ID
```

Here the output on screen.
```bash
[ec2-user@ip-10-5-0-109 ~]$ VOLUME_ID=$(aws ec2 describe-instances \
>   --filter 'Name=tag:Name,Values=Processor' \
>   --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.{VolumeId:VolumeId}' \
>   --output text)
[ec2-user@ip-10-5-0-109 ~]$ echo $VOLUME_ID
vol-0107814cf0363f3c2
[ec2-user@ip-10-5-0-109 ~]$ echo $VOLUME_ID
vol-0107814cf0363f3c2
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 create-snapshot --volume-id $VOLUME_ID
{
    "Tags": [],
    "SnapshotId": "snap-0b1319bdcc5824251",
    "VolumeId": "vol-0107814cf0363f3c2",
    "State": "pending",
    "StartTime": "2026-03-22T17:00:28.213Z",
    "Progress": "",
    "OwnerId": "642587893907",
    "Description": "",
    "VolumeSize": 8,
    "Encrypted": false
}
[ec2-user@ip-10-5-0-109 ~]$ SNAPSHOT_ID="snap-0b1319bdcc5824251"
[ec2-user@ip-10-5-0-109 ~]$ echo $SNAPSHOT_ID
snap-0b1319bdcc5824251
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 wait snapshot-completed --snapshot-id $SNAPSHOT_ID
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 start-instances --instance-ids $INSTANCE_ID
{
    "StartingInstances": [
        {
            "InstanceId": "i-08e1f153a38133346",
            "CurrentState": {
                "Code": 0,
                "Name": "pending"
            },
            "PreviousState": {
                "Code": 80,
                "Name": "stopped"
            }
        }
    ]
}
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 start-instances --instance-ids $INSTANCE_ID
{
    "StartingInstances": [
        {
            "InstanceId": "i-08e1f153a38133346",
            "CurrentState": {
                "Code": 16,
                "Name": "running"
            },
            "PreviousState": {
                "Code": 16,
                "Name": "running"
            }
        }
    ]
}
[ec2-user@ip-10-5-0-109 ~]$ 
```

4. I schedule the creation of subsequent snapshots using the command `cron`.
```bash
echo "* * * * *  aws ec2 create-snapshot --volume-id $VOLUME_ID 2>&1 >> /tmp/cronlog" > cronjob
crontab cronjob
aws ec2 describe-snapshots --filters "Name=volume-id,Values=$VOLUME_ID"
```

Here the output screen.
```bash
[ec2-user@ip-10-5-0-109 ~]$ echo "* * * * *  aws ec2 create-snapshot --volume-id $VOLUME_ID 2>&1 >> /tmp/cronlog" > cronjob
You have new mail in /var/spool/mail/ec2-user
[ec2-user@ip-10-5-0-109 ~]$ crontab cronjob
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 describe-snapshots --filters "Name=volume-id,Values=$VOLUME_ID"
{
    "Snapshots": [
        {
            "StorageTier": "standard",
            "TransferType": "standard",
            "CompletionTime": "2026-03-22T17:17:53.426Z",
            "FullSnapshotSizeInBytes": 2099249152,
            "SnapshotId": "snap-08339beae0838917d",
            "VolumeId": "vol-0107814cf0363f3c2",
            "State": "completed",
            "StartTime": "2026-03-22T17:17:02.749Z",
            "Progress": "100%",
            "OwnerId": "642587893907",
            "Description": "",
            "VolumeSize": 8,
            "Encrypted": false
        },
        {
            "StorageTier": "standard",
            "TransferType": "standard",
            "CompletionTime": "2026-03-22T17:01:16.260Z",
            "FullSnapshotSizeInBytes": 2097676288,
            "SnapshotId": "snap-0b1319bdcc5824251",
            "VolumeId": "vol-0107814cf0363f3c2",
            "State": "completed",
            "StartTime": "2026-03-22T17:00:28.213Z",
            "Progress": "100%",
            "OwnerId": "642587893907",
            "Description": "",
            "VolumeSize": 8,
            "Encrypted": false
        }
    ]
}
```

5. I stop the cron job with the command `crontab -r`.

6. I examine the contents of the Python script **snapshotter_v2.py** with the command `more /home/ec2-user/snapshotter_v2.py`.
```bash
#!/usr/bin/env python

import boto3 

MAX_SNAPSHOTS = 2   # Number of snapshots to keep

# Create the EC2 resource
ec2 = boto3.resource('ec2')

# Get a list of all volumes
volume_iterator = ec2.volumes.all()

# Create a snapshot of each volume
for v in volume_iterator:
  v.create_snapshot()

  # Too many snapshots?
  snapshots = list(v.snapshots.all())
  if len(snapshots) > MAX_SNAPSHOTS:

    # Delete oldest snapshots, but keep MAX_SNAPSHOTS available
    snap_sorted = sorted([(s.id, s.start_time, s) for s in snapshots], key=lambda k: k[1])
    for s in snap_sorted[:-MAX_SNAPSHOTS]:
      print("Deleting snapshot", s[0])
      s[2].delete()
```
The script finds all EBS volumes that are associated with the current user’s account and takes snapshots. 
It then examines the number of snapshots that are associated with the volume, sorts the snapshots by date, 
and removes all but the two most recent snapshots.

8. I show all the snapshot IDs associated to the volume.
```bash
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 describe-snapshots --filters "Name=volume-id, Values=$VOLUME_ID" --query 'Snapshots[*].SnapshotId'
[
    "snap-022eead0ab16f1c3e",
    "snap-0d058c55a2c125801",
    "snap-08339beae0838917d",
    "snap-0b1319bdcc5824251"
]
```

9. I retain the last two snapshots.
```bash
[ec2-user@ip-10-5-0-109 ~]$ python3.8 snapshotter_v2.py
Deleting snapshot snap-0b1319bdcc5824251
Deleting snapshot snap-08339beae0838917d
Deleting snapshot snap-022eead0ab16f1c3e
```

10. I examine the new number of snapshots for the current volume.
```bash
[ec2-user@ip-10-5-0-109 ~]$ aws ec2 describe-snapshots --filters "Name=volume-id, Values=$VOLUME_ID" --query 'Snapshots[*].SnapshotId'
[
    "snap-015c1fbd97bffaad6",
    "snap-0d058c55a2c125801"
]
```

## Task 3: Challenge: Synchronize files with Amazon S3
Here I've been challenged to sync the contents of a directory with the Amazon S3 bucket that you created earlier.

1. Downloading and unzipping sample files
2. Syncing files

## Conclusion
In this lab I learnt how to:

- create and maintain snapshots for Amazon EC2 instances.
- use Amazon S3 sync to copy files from an EBS volume to an S3 bucket.
- use Amazon S3 versioning to retrieve deleted files.

