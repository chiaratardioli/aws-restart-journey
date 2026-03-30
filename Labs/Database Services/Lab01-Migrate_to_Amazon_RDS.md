# Migrate to Amazon RDS

In this lab, I will migrate the café web application to use a fully managed Amazon Relational Database Service (Amazon RDS) 
database (DB) instance instead of a local database instance.

I will begin by generating some data on the existing database. This data is migrated to the new Amazon RDS instance.
During the migration process, I will build the required components, including two private subnets in different 
Availability Zones, a security group for the database instance, and the RDS DB instance itself. After the database 
has been migrated, I will reconfigure the café application to use the Amazon RDS instance instead of a local database.

## Starting architecture

The following diagram illustrates the topology of the café web application runtime environment before the migration. 
The application database runs in an Amazon Elastic Compute Cloud (Amazon EC2) Linux, Apache, MySQL, and PHP (LAMP) 
instance along with the application code. The instance has a T3 small instance type and runs in a public subnet so 
that internet clients can access the website. A CLI Host instance resides in the same subnet to facilitate the a
dministration of the instance by using the AWS Command Line Interface (AWS CLI).

![Starting architecture](./images/lab01-starting-architecture.png)

## Final architecture

The following diagram illustrates the topology of the café web application runtime environment after the migration.
I will migrate the local café database to an Amazon RDS database that resides outside the instance. The Amazon RDS 
database is deployed in the same virtual private cloud (VPC) as the instance.

![Final architecture after migration](./images/lab01-final-architecture.png)

## Task 1: Generating order data on the café website
First I get the details for the lab:

| Key                      | Value                                             |
|--------------------------|---------------------------------------------------|
| CafeInstancePublicDNS    | ec2-44-251-174-187.us-west-2.compute.amazonaws.com |
| SecretKey                | 62NgYPWMJSy38UTkB8IGdC6Ae34nRfAH631KNMEO           |
| CafeInstanceAZ           | us-west-2a                                        |
| LabRegion                | us-west-2                                         |
| CafeVpcID                | vpc-0312ce684a69fa26a                             |
| AccessKey                | AKIARJAI3EF3C7N3NWRB                              |
| CafeSecurityGroupID      | sg-0b558107d178999b2                              |
| CafeInstanceURL          | 44.251.174.187/cafe                               |

Then, I browse the café website and place a few orders that are stored in the existing database. 
Placing orders creates data for the application before the application is migrated to new Amazon RDS instance.

![Café Order History](./images/lab01-cafe-order-history)

## Task 2: Creating an Amazon RDS instance by using the AWS CLI

1. I connect to the CLI Host instance using EC2 Instance Connect.
2. I connect to the CLI Host instance by providing the configuration parameters for the lab (plus output json).
3. I create the following components and save the ID:

| Component                   | ID                         |
|-----------------------------|----------------------------|
| CafeDatabaseSG              | sg-0ceb9e203f80b2fca       |
| CafeDB Private Subnet 1     | subnet-0a21667f0b5c348f5   |
| CafeDB Private Subnet 2     | subnet-07596cec9c018283d   |

Then I can create the CafeDB Subnet Group (Database subnet group):
```bash
[ec2-user@ip-10-200-0-17 ~]$ aws rds create-db-subnet-group \
> --db-subnet-group-name "CafeDB Subnet Group" \
> --db-subnet-group-description "DB subnet group for Cafe" \
> --subnet-ids subnet-0a21667f0b5c348f5 subnet-07596cec9c018283d \
> --tags "Key=Name,Value= CafeDatabaseSubnetGroup"
{
    "DBSubnetGroup": {
        "Subnets": [
            {
                "SubnetStatus": "Active", 
                "SubnetIdentifier": "subnet-0a21667f0b5c348f5", 
                "SubnetOutpost": {}, 
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            }, 
            {
                "SubnetStatus": "Active", 
                "SubnetIdentifier": "subnet-07596cec9c018283d", 
                "SubnetOutpost": {}, 
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2b"
                }
            }
        ], 
        "VpcId": "vpc-0312ce684a69fa26a", 
        "DBSubnetGroupDescription": "DB subnet group for Cafe", 
        "SubnetGroupStatus": "Complete", 
        "DBSubnetGroupArn": "arn:aws:rds:us-west-2:088065384822:subgrp:cafedb subnet group", 
        "DBSubnetGroupName": "cafedb subnet group"
    }
}
```

4. Creating the Amazon RDS MariaDB instance
Now I create the CafeDBInstance that is shown in the final architecture. Using the AWS CLI, I create an Amazon RDS MariaDB instance
with the following configuration settings:
- DB instance identifier: `CafeDBInstance`
- Engine option: `MariaDB`
- DB engine version: `10.5.13`
- DB instance class: `db.t3.micro`
- Allocated storage: `20 GB`
- Availability Zone: `CafeInstanceAZ`
- DB Subnet group: `CafeDB Subnet Group`
- VPC security groups: `CafeDatabaseSG`
- Public accessibility: `No`
- Username: `root`
- Password: `Re:Start!9`

These options specify the creation of a MariaDB database instance that is deployed in the same Availability Zone as the café instance. 
The MariaDB database instance also uses the DB subnet group that I built in the previous step.

The database instance takes up to 10 minutes to become available.
I monitor the status of the database instance until it shows a status of available:

```bash
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        null, 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "creating"
    ]
]
```

The command to check the status shows the following information for the database, including the status of the database as the last returned value:
- Endpoint address
- Availability Zone
- Preferred backup window
- Backup retention period
- Status of the database

Automated backups occur daily during the preferred backup window, and they are retained for the duration that is specified by the backup retention period. Note the value of 1 for the backup retention period, which indicates that, by default, daily backups are retained for only 1 day. Also, the preferred backup window is set to a 30 minute time interval by default. It is possible to modify these settings to match your desired backup policy.

The status attribute initially shows a value of *creating* and then changes to *modifying*, then *backing-up* and finally to *available*.

```
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        "cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com", 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "available"
    ]
]
```
When the database becomes *available*, I record the endpoint 
```
RDS Instance Database Endpoint Address: cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com
```

## Task 3: Migrating application data to the Amazon RDS instance
Here, I migrate the data from the existing local database to the newly created Amazon RDS database. Specifically, I do the following:
- Connect to the CafeInstance by using EC2 Instance Connect.
- Use the mysqldump utility to create a backup of the local database.
```bash
mysqldump --user=root --password='Re:Start!9' \
--databases cafe_db --add-drop-database > cafedb-backup.sql

less cafedb-backup.sql
```
- Restore the backup to the Amazon RDS database.
```bash
mysql --user=root --password='Re:Start!9' \
--host="cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com" \
--ssl \
< cafedb-backup.sql
```

- Test the data migration. I run the command to enter the SQL session
```sql
[ec2-user@ip-10-200-0-12 ~]$ mysql --user=root --password='Re:Start!9' \
> --host="cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com" \
> --ssl \
> cafe_db
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MariaDB monitor.  Commands end with ; or \g.
Your MariaDB connection id is 77
Server version: 11.8.5-MariaDB-log managed by https://aws.amazon.com/rds/

Copyright (c) 2000, 2018, Oracle, MariaDB Corporation Ab and others.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

MariaDB [cafe_db]> select * from product;
+----+---------------------------+-----------------------------------------------------------------+-------+---------------+---------------------------------------+
| id | product_name              | description                                                     | price | product_group | image_url                             |
+----+---------------------------+-----------------------------------------------------------------+-------+---------------+---------------------------------------+
|  1 |                 Croissant |                  Fresh, buttery and fluffy... Simply delicious! |  1.50 |             1 |                 images/Croissants.jpg |
|  2 |                     Donut |                         We have more than half-a-dozen flavors! |  1.00 |             1 |                     images/Donuts.jpg |
|  3 |     Chocolate Chip Cookie |    Made with Swiss chocolate with a touch of Madagascar vanilla |  2.50 |             1 |     images/Chocolate-Chip-Cookies.jpg |
|  4 |                    Muffin |                     Banana bread, blueberry, cranberry or apple |  3.00 |             1 |                    images/Muffins.jpg |
|  5 | Strawberry Blueberry Tart |                Bursting with the taste and aroma of fresh fruit |  3.50 |             1 | images/Strawberry-Blueberry-Tarts.jpg |
|  6 |           Strawberry Tart | Made with fresh ripe strawberries and a delicious whipped cream |  3.50 |             1 |           images/Strawberry-Tarts.jpg |
|  7 |                    Coffee |                Freshly-ground black or blended Columbian coffee |  3.00 |             2 |                     images/Coffee.jpg |
|  8 |             Hot Chocolate |                   Rich and creamy, and made with real chocolate |  3.00 |             2 |       images/Cup-of-Hot-Chocolate.jpg |
|  9 |                     Latte |            Offered hot or cold and in various delicious flavors |  3.50 |             2 |                      images/Latte.jpg |
+----+---------------------------+-----------------------------------------------------------------+-------+---------------+---------------------------------------+
9 rows in set (0.00 sec)
```
I type `exit` to exit the interactive SQL session.

Note that I can perform these steps from the command line after connecting to the CafeInstance. This instance can communicate with 
the Amazon RDS instance by using the MySQL protocol because I associated the CafeDatabaseSG security group with the Amazon RDS instance.

## Task 4: Configuring the website to use the Amazon RDS instance


## Task 5: Monitoring the Amazon RDS database


## Conclusion
- I created an Amazon RDS MariaDB instance by using the AWS CLI.
- I migrated data from a MariaDB database on an EC2 instance to an Amazon RDS MariaDB instance.
- I monitored the Amazon RDS instance by using Amazon CloudWatch metrics.

## Notes
1. CafeDB Private Subnet 1 hosts the RDS DB instance. It is a private subnet that is defined in the same Availability Zone as the CafeInstance.
You must assign the subnet a Classless Inter-Domain Routing (CIDR) address block that is within the address range of the VPC but that does not overlap with the address range of any other subnet in the VPC. This reason is why you collected the information about the VPC and existing subnet CIDR blocks:
    - Cafe VPC IPv4 CIDR block: 10.200.0.0/20
    - Cafe Public Subnet 1 IPv4 CIDR block: 10.200.0.0/24
    - Cafe Private Subnet 1 IPv4 CIDR block: 10.200.2.0/23

## Bash Script
```bash
# CafeDatabaseSG (Security group for the Amazon RDS database)
aws ec2 create-security-group \
--group-name CafeDatabaseSG \
--description "Security group for Cafe database" \
--vpc-id <CafeInstance VPC ID>

# Inbound rule for the security group
aws ec2 authorize-security-group-ingress \
--group-id <CafeDatabaseSG Group ID> \
--protocol tcp --port 3306 \
--source-group <CafeSecurityGroup Group ID>

# Confirm that the inbound rule was applied appropriately, run the following command: 
aws ec2 describe-security-groups \
--query "SecurityGroups[*].[GroupName,GroupId,IpPermissions]" \
--filters "Name=group-name,Values='CafeDatabaseSG'"

# Create the first subnet
aws ec2 create-subnet \
--vpc-id <CafeInstance VPC ID> \
--cidr-block 10.200.2.0/23 \
--availability-zone <CafeInstance Availability Zone>

# Create the second subnet (different AZ)
aws ec2 create-subnet \
--vpc-id <CafeInstance VPC ID> \
--cidr-block 10.200.10.0/23 \
--availability-zone <availability-zone>

# Create CafeDB Subnet Group
aws rds create-db-subnet-group \
--db-subnet-group-name "CafeDB Subnet Group" \
--db-subnet-group-description "DB subnet group for Cafe" \
--subnet-ids <Cafe Private Subnet 1 ID> <Cafe Private Subnet 2 ID> \
--tags "Key=Name,Value= CafeDatabaseSubnetGroup"

# Create the CafeDBInstance
aws rds create-db-instance \
--db-instance-identifier CafeDBInstance \
--engine mariadb \
--engine-version <latest version, e.g., 11.8.5> \
--db-instance-class db.t3.micro \
--allocated-storage 20 \
--availability-zone <CafeInstance Availability Zone> \
--db-subnet-group-name "CafeDB Subnet Group" \
--vpc-security-group-ids <CafeDatabaseSG Group ID> \
--no-publicly-accessible \
--master-username root --master-user-password 'Re:Start!9'

# Monitor the status of the database instance 
aws rds describe-db-instances \
--db-instance-identifier CafeDBInstance \
--query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"

# Use the mysqldump utility to create a backup of the local cafe_db database
mysqldump --user=root --password='Re:Start!9' \
--databases cafe_db --add-drop-database > cafedb-backup.sql

# Restore the backup to the Amazon RDS database
mysql --user=root --password='Re:Start!9' \
--host=<RDS Instance Database Endpoint Address> \
< cafedb-backup.sql

$ Verify that the cafe_db was successfully created and populated in the Amazon RDS instance
mysql --user=root --password='Re:Start!9' \
--host=<RDS Instance Database Endpoint Address> \
cafe_db
```

## Terminal Screen
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

[ec2-user@ip-10-200-0-17 ~]$ aws configure
AWS Access Key ID [None]: AKIARJAI3EF3C7N3NWRB
AWS Secret Access Key [None]: 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
Default region name [None]: us-west-2
Default output format [None]: json
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 create-security-group \
> --group-name CafeDatabaseSG \
> --description "Security group for Cafe database" \
> --vpc-id vpc-0312ce684a69fa26a
{
    "GroupId": "sg-0ceb9e203f80b2fca"
}
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 authorize-security-group-ingress \
> --group-id sg-0ceb9e203f80b2fca \
> --protocol tcp --port 3306 \
> --source-group sg-0b558107d178999b2
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 describe-security-groups \
> --query "SecurityGroups[*].[GroupName,GroupId,IpPermissions]" \
> --filters "Name=group-name,Values='CafeDatabaseSG'"
[
    [
        "CafeDatabaseSG", 
        "sg-0ceb9e203f80b2fca", 
        [
            {
                "PrefixListIds": [], 
                "FromPort": 3306, 
                "IpRanges": [], 
                "ToPort": 3306, 
                "IpProtocol": "tcp", 
                "UserIdGroupPairs": [
                    {
                        "UserId": "088065384822", 
                        "GroupId": "sg-0b558107d178999b2"
                    }
                ], 
                "Ipv6Ranges": []
            }
        ]
    ]
]
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 create-subnet \
> --vpc-id vpc-0312ce684a69fa26a \
> --cidr-block 10.200.2.0/23 \
> --availability-zone us-west-2a
{
    "Subnet": {
        "MapPublicIpOnLaunch": false, 
        "AvailabilityZoneId": "usw2-az2", 
        "AvailableIpAddressCount": 507, 
        "DefaultForAz": false, 
        "SubnetArn": "arn:aws:ec2:us-west-2:088065384822:subnet/subnet-0a21667f0b5c348f5", 
        "Ipv6CidrBlockAssociationSet": [], 
        "VpcId": "vpc-0312ce684a69fa26a", 
        "MapCustomerOwnedIpOnLaunch": false, 
        "AvailabilityZone": "us-west-2a", 
        "SubnetId": "subnet-0a21667f0b5c348f5", 
        "OwnerId": "088065384822", 
        "CidrBlock": "10.200.2.0/23", 
        "State": "available", 
        "AssignIpv6AddressOnCreation": false
    }
}
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 create-subnet \
> --vpc-id vpc-0312ce684a69fa26a \
> --cidr-block 10.200.2.0/23 \
> --availability-zone us-west-2b

An error occurred (InvalidSubnet.Conflict) when calling the CreateSubnet operation: The CIDR '10.200.2.0/23' conflicts with another subnet
[ec2-user@ip-10-200-0-17 ~]$ aws ec2 create-subnet \
> --vpc-id vpc-0312ce684a69fa26a \
> --cidr-block 10.200.10.0/23 \
> --availability-zone us-west-2b
{
    "Subnet": {
        "MapPublicIpOnLaunch": false, 
        "AvailabilityZoneId": "usw2-az1", 
        "AvailableIpAddressCount": 507, 
        "DefaultForAz": false, 
        "SubnetArn": "arn:aws:ec2:us-west-2:088065384822:subnet/subnet-07596cec9c018283d", 
        "Ipv6CidrBlockAssociationSet": [], 
        "VpcId": "vpc-0312ce684a69fa26a", 
        "MapCustomerOwnedIpOnLaunch": false, 
        "AvailabilityZone": "us-west-2b", 
        "SubnetId": "subnet-07596cec9c018283d", 
        "OwnerId": "088065384822", 
        "CidrBlock": "10.200.10.0/23", 
        "State": "available", 
        "AssignIpv6AddressOnCreation": false
    }
}
[ec2-user@ip-10-200-0-17 ~]$ aws rds create-db-subnet-group \
> --db-subnet-group-name "CafeDB Subnet Group" \
> --db-subnet-group-description "DB subnet group for Cafe" \
> --subnet-ids subnet-0a21667f0b5c348f5 subnet-07596cec9c018283d \
> --tags "Key=Name,Value= CafeDatabaseSubnetGroup"
{
    "DBSubnetGroup": {
        "Subnets": [
            {
                "SubnetStatus": "Active", 
                "SubnetIdentifier": "subnet-0a21667f0b5c348f5", 
                "SubnetOutpost": {}, 
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2a"
                }
            }, 
            {
                "SubnetStatus": "Active", 
                "SubnetIdentifier": "subnet-07596cec9c018283d", 
                "SubnetOutpost": {}, 
                "SubnetAvailabilityZone": {
                    "Name": "us-west-2b"
                }
            }
        ], 
        "VpcId": "vpc-0312ce684a69fa26a", 
        "DBSubnetGroupDescription": "DB subnet group for Cafe", 
        "SubnetGroupStatus": "Complete", 
        "DBSubnetGroupArn": "arn:aws:rds:us-west-2:088065384822:subgrp:cafedb subnet group", 
        "DBSubnetGroupName": "cafedb subnet group"
    }
}
[ec2-user@ip-10-200-0-17 ~]$ aws rds create-db-instance \
> --db-instance-identifier CafeDBInstance \
> --engine mariadb \
> --engine-version 10.5.13 \
> --db-instance-class db.t3.micro \
> --allocated-storage 20 \
> --availability-zone us-west-2a \
> --db-subnet-group-name "CafeDB Subnet Group" \
> --vpc-security-group-ids sg-0ceb9e203f80b2fca \
> --no-publicly-accessible \
> --master-username root --master-user-password 'Re:Start!9'

An error occurred (InvalidParameterCombination) when calling the CreateDBInstance operation: Cannot find version 10.5.13 for mariadb
[ec2-user@ip-10-200-0-17 ~]$ aws rds create-db-instance \
> --db-instance-identifier CafeDBInstance \
> --engine mariadb \
> --engine-version 11.8.5 \
> --db-instance-class db.t3.micro \
> --allocated-storage 20 \
> --availability-zone us-west-2a \
> --db-subnet-group-name "CafeDB Subnet Group" \
> --vpc-security-group-ids sg-0ceb9e203f80b2fca \
> --no-publicly-accessible \
> --master-username root --master-user-password 'Re:Start!9'
{
    "DBInstance": {
        "PubliclyAccessible": false, 
        "MasterUsername": "root", 
        "MonitoringInterval": 0, 
        "LicenseModel": "general-public-license", 
        "VpcSecurityGroups": [
            {
                "Status": "active", 
                "VpcSecurityGroupId": "sg-0ceb9e203f80b2fca"
            }
        ], 
        "CopyTagsToSnapshot": false, 
        "OptionGroupMemberships": [
            {
                "Status": "in-sync", 
                "OptionGroupName": "default:mariadb-11-8"
            }
        ], 
        "PendingModifiedValues": {
            "MasterUserPassword": "****"
        }, 
        "Engine": "mariadb", 
        "MultiAZ": false, 
        "DBSecurityGroups": [], 
        "DBParameterGroups": [
            {
                "DBParameterGroupName": "default.mariadb11.8", 
                "ParameterApplyStatus": "in-sync"
            }
        ], 
        "PerformanceInsightsEnabled": false, 
        "AutoMinorVersionUpgrade": true, 
        "PreferredBackupWindow": "11:33-12:03", 
        "DBSubnetGroup": {
            "Subnets": [
                {
                    "SubnetStatus": "Active", 
                    "SubnetIdentifier": "subnet-0a21667f0b5c348f5", 
                    "SubnetOutpost": {}, 
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2a"
                    }
                }, 
                {
                    "SubnetStatus": "Active", 
                    "SubnetIdentifier": "subnet-07596cec9c018283d", 
                    "SubnetOutpost": {}, 
                    "SubnetAvailabilityZone": {
                        "Name": "us-west-2b"
                    }
                }
            ], 
            "DBSubnetGroupName": "cafedb subnet group", 
            "VpcId": "vpc-0312ce684a69fa26a", 
            "DBSubnetGroupDescription": "DB subnet group for Cafe", 
            "SubnetGroupStatus": "Complete"
        }, 
        "ReadReplicaDBInstanceIdentifiers": [], 
        "AllocatedStorage": 20, 
        "DBInstanceArn": "arn:aws:rds:us-west-2:088065384822:db:cafedbinstance", 
        "BackupRetentionPeriod": 1, 
        "PreferredMaintenanceWindow": "tue:08:35-tue:09:05", 
        "DBInstanceStatus": "creating", 
        "IAMDatabaseAuthenticationEnabled": false, 
        "EngineVersion": "11.8.5", 
        "DeletionProtection": false, 
        "AvailabilityZone": "us-west-2a", 
        "DomainMemberships": [], 
        "StorageType": "gp2", 
        "DbiResourceId": "db-Q6KTLY5UTBNZC5DNTX2RURBYDY", 
        "CACertificateIdentifier": "rds-ca-rsa2048-g1", 
        "StorageEncrypted": false, 
        "AssociatedRoles": [], 
        "DBInstanceClass": "db.t3.micro", 
        "DbInstancePort": 0, 
        "DBInstanceIdentifier": "cafedbinstance"
    }
}
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        null, 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "creating"
    ]
]
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        null, 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "creating"
    ]
]
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        "cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com", 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "configuring-enhanced-monitoring"
    ]
]
[ec2-user@ip-10-200-0-17 ~]$ aws rds describe-db-instances \
> --db-instance-identifier CafeDBInstance \
> --query "DBInstances[*].[Endpoint.Address,AvailabilityZone,PreferredBackupWindow,BackupRetentionPeriod,DBInstanceStatus]"
[
    [
        "cafedbinstance.cuidhnvjgvfc.us-west-2.rds.amazonaws.com", 
        "us-west-2a", 
        "11:33-12:03", 
        1, 
        "available"
    ]
]
```

