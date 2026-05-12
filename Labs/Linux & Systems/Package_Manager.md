# Linux Software Management

In this lab, I learnt how to:

- Update the Linux machine using the package manager
- Roll back or downgrade a previously updated package through the package manager
- Install the AWS Command Line Interface (AWS CLI)

## Task 1: Use SSH to connect to an Amazon Linux EC2 instance
I am using a Mac OS, so I uses an SSH utility to connect to a Amazon Linux EC2 instance. Same steps apply for Linuz users, while Windows users need to follow different operations.

I download the file **labuser.pem** from the lab platform and saved the **PublicIP** address, that for my lab is `4.243.242.89`.
Then, I opened a terminal and, after giving my user read permission on the file, I connect to the EC2 via `ssh`.
This is how it looks like on my terminal.
```bash
chiara@macbook-air:~/labs$ chmod 400 labsuser.pem 
chiara@macbook-air:~/labs$ ls -l labsuser.pem
-r--------@ 1 chiara  staff   1.6K 15 Mar 13:42 labsuser.pem
chiara@macbook-air:~/labs$ ssh -i labsuser.pem ec2-user@44.243.242.89
The authenticity of host '44.243.242.89 (44.243.242.89)' can't be established.
ED25519 key fingerprint is SHA256:0YeEq//xFB8hgIK/qVkg4i9tBzCIJ60eC77Ce4wSvlM.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '44.243.242.89' (ED25519) to the list of known hosts.
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

[ec2-user@ip-10-0-10-161 ~]$ 

```

## Task 2: Update your Linux machine
Here I used the yum package manager to update and upgrade the machine, including relevant security packages.

1. I entered `sudo yum -y check-update` to query repositories for available updates.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo yum -y check-update
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
amzn2-core                                               | 3.6 kB     00:00  
```

2. I entered `sudo yum update --security` to apply security-related updates.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo yum update --security
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
No packages needed for security; 0 packages available
No packages marked for update
```

3. I entered `sudo yum -y upgrade` to update packages.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo yum -y upgrade
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
No packages marked for update
```

4. Eventually, I used the command `sudo yum install httpd -y` to view the install of httpd and view the history of updates.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo yum install httpd -y
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Resolving Dependencies
--> Running transaction check
---> Package httpd.x86_64 0:2.4.66-1.amzn2.0.1 will be installed
--> Processing Dependency: httpd-filesystem = 2.4.66-1.amzn2.0.1 for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: httpd-tools = 2.4.66-1.amzn2.0.1 for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: /etc/mime.types for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: httpd-filesystem for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: mod_http2 for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: system-logos-httpd for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: libapr-1.so.0()(64bit) for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Processing Dependency: libaprutil-1.so.0()(64bit) for package: httpd-2.4.66-1.amzn2.0.1.x86_64
--> Running transaction check
---> Package apr.x86_64 0:1.7.2-1.amzn2.0.1 will be installed
---> Package apr-util.x86_64 0:1.6.3-1.amzn2.0.1 will be installed
--> Processing Dependency: apr-util-bdb(x86-64) = 1.6.3-1.amzn2.0.1 for package: apr-util-1.6.3-1.amzn2.0.1.x86_64
---> Package generic-logos-httpd.noarch 0:18.0.0-4.amzn2 will be installed
---> Package httpd-filesystem.noarch 0:2.4.66-1.amzn2.0.1 will be installed
---> Package httpd-tools.x86_64 0:2.4.66-1.amzn2.0.1 will be installed
---> Package mailcap.noarch 0:2.1.41-2.amzn2 will be installed
---> Package mod_http2.x86_64 0:1.15.19-1.amzn2.0.2 will be installed
--> Running transaction check
---> Package apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1 will be installed
--> Finished Dependency Resolution

Dependencies Resolved

================================================================================
 Package                Arch      Version                   Repository     Size
================================================================================
Installing:
 httpd                  x86_64    2.4.66-1.amzn2.0.1        amzn2-core    1.4 M
Installing for dependencies:
 apr                    x86_64    1.7.2-1.amzn2.0.1         amzn2-core    130 k
 apr-util               x86_64    1.6.3-1.amzn2.0.1         amzn2-core    101 k
 apr-util-bdb           x86_64    1.6.3-1.amzn2.0.1         amzn2-core     22 k
 generic-logos-httpd    noarch    18.0.0-4.amzn2            amzn2-core     19 k
 httpd-filesystem       noarch    2.4.66-1.amzn2.0.1        amzn2-core     25 k
 httpd-tools            x86_64    2.4.66-1.amzn2.0.1        amzn2-core     90 k
 mailcap                noarch    2.1.41-2.amzn2            amzn2-core     31 k
 mod_http2              x86_64    1.15.19-1.amzn2.0.2       amzn2-core    149 k

Transaction Summary
================================================================================
Install  1 Package (+8 Dependent packages)

Total download size: 1.9 M
Installed size: 5.3 M
Downloading packages:
(1/9): apr-1.7.2-1.amzn2.0.1.x86_64.rpm                    | 130 kB   00:00     
(2/9): apr-util-1.6.3-1.amzn2.0.1.x86_64.rpm               | 101 kB   00:00     
(3/9): apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64.rpm           |  22 kB   00:00     
(4/9): generic-logos-httpd-18.0.0-4.amzn2.noarch.rpm       |  19 kB   00:00     
(5/9): httpd-2.4.66-1.amzn2.0.1.x86_64.rpm                 | 1.4 MB   00:00     
(6/9): httpd-filesystem-2.4.66-1.amzn2.0.1.noarch.rpm      |  25 kB   00:00     
(7/9): httpd-tools-2.4.66-1.amzn2.0.1.x86_64.rpm           |  90 kB   00:00     
(8/9): mailcap-2.1.41-2.amzn2.noarch.rpm                   |  31 kB   00:00     
(9/9): mod_http2-1.15.19-1.amzn2.0.2.x86_64.rpm            | 149 kB   00:00     
--------------------------------------------------------------------------------
Total                                              9.3 MB/s | 1.9 MB  00:00     
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Installing : apr-1.7.2-1.amzn2.0.1.x86_64                                 1/9 
  Installing : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                        2/9 
  Installing : apr-util-1.6.3-1.amzn2.0.1.x86_64                            3/9 
  Installing : httpd-tools-2.4.66-1.amzn2.0.1.x86_64                        4/9 
  Installing : httpd-filesystem-2.4.66-1.amzn2.0.1.noarch                   5/9 
  Installing : generic-logos-httpd-18.0.0-4.amzn2.noarch                    6/9 
  Installing : mailcap-2.1.41-2.amzn2.noarch                                7/9 
  Installing : mod_http2-1.15.19-1.amzn2.0.2.x86_64                         8/9 
  Installing : httpd-2.4.66-1.amzn2.0.1.x86_64                              9/9 
  Verifying  : apr-1.7.2-1.amzn2.0.1.x86_64                                 1/9 
  Verifying  : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                        2/9 
  Verifying  : mod_http2-1.15.19-1.amzn2.0.2.x86_64                         3/9 
  Verifying  : httpd-tools-2.4.66-1.amzn2.0.1.x86_64                        4/9 
  Verifying  : mailcap-2.1.41-2.amzn2.noarch                                5/9 
  Verifying  : generic-logos-httpd-18.0.0-4.amzn2.noarch                    6/9 
  Verifying  : httpd-2.4.66-1.amzn2.0.1.x86_64                              7/9 
  Verifying  : httpd-filesystem-2.4.66-1.amzn2.0.1.noarch                   8/9 
  Verifying  : apr-util-1.6.3-1.amzn2.0.1.x86_64                            9/9 

Installed:
  httpd.x86_64 0:2.4.66-1.amzn2.0.1                                             

Dependency Installed:
  apr.x86_64 0:1.7.2-1.amzn2.0.1                                                
  apr-util.x86_64 0:1.6.3-1.amzn2.0.1                                           
  apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1                                       
  generic-logos-httpd.noarch 0:18.0.0-4.amzn2                                   
  httpd-filesystem.noarch 0:2.4.66-1.amzn2.0.1                                  
  httpd-tools.x86_64 0:2.4.66-1.amzn2.0.1                                       
  mailcap.noarch 0:2.1.41-2.amzn2                                               
  mod_http2.x86_64 0:1.15.19-1.amzn2.0.2                                        

Complete!
```

## Task 3: Roll back a package
Here I downgraded a package that has been updated through the yum package manager by doing the following:

- Using the yum history to list what has been installed and updated
- Rolling back to the most recent updates in the history list

1. In the folder **companyA**, I typed `sudo yum history list` to view the history of updates.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo yum history list
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
ID     | Command line             | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     1 | install httpd -y         | 2026-03-15 12:46 | Install        |    9   
history list
```
The output is defferent than expected. It does not show the column for the **Login user** but the **Command Line**. 
To see the **Login User** column I added the option `history_list_view=users`.

```bash
[ec2-user@ip-10-0-10-161 companyA]$ sudo yum --setopt=history_list_view=users history list
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
ID     | Login user               | Date and time    | Action(s)      | Altered
-------------------------------------------------------------------------------
     1 | EC2 ... <ec2-user>       | 2026-03-15 12:46 | Install        |    9   
history list
```

2. To view the most recent set of updates for the command `install httpd -y`, I entered `sudo yum history info 1`, where `1` is the ID of the command.
```bash
[ec2-user@ip-10-0-10-161 companyA]$ sudo yum history info 1
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Transaction ID : 1
Begin time     : Sun Mar 15 12:46:31 2026
Begin rpmdb    : 455:7d1868e24da50b759c4f89a3cd02a65a626bae3b
End time       :            12:46:32 2026 (1 seconds)
End rpmdb      : 464:553f3024885bb76000cb71512d3790ac844b2d6e
User           : EC2 Default User <ec2-user>
Return-Code    : Success
Command Line   : install httpd -y
```

3. Entually, I rolled back to the most recent updates by typing `sudo yum -y history undo 1`.
```bash
[ec2-user@ip-10-0-10-161 companyA]$ sudo yum -y history undo 1
Loaded plugins: extras_suggestions, langpacks, priorities, update-motd
Undoing transaction 1, from Sun Mar 15 12:46:31 2026
    Dep-Install apr-1.7.2-1.amzn2.0.1.x86_64               @amzn2-core
    Dep-Install apr-util-1.6.3-1.amzn2.0.1.x86_64          @amzn2-core
    Dep-Install apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64      @amzn2-core
    Dep-Install generic-logos-httpd-18.0.0-4.amzn2.noarch  @amzn2-core
    Install     httpd-2.4.66-1.amzn2.0.1.x86_64            @amzn2-core
    Dep-Install httpd-filesystem-2.4.66-1.amzn2.0.1.noarch @amzn2-core
    Dep-Install httpd-tools-2.4.66-1.amzn2.0.1.x86_64      @amzn2-core
    Dep-Install mailcap-2.1.41-2.amzn2.noarch              @amzn2-core
    Dep-Install mod_http2-1.15.19-1.amzn2.0.2.x86_64       @amzn2-core
Resolving Dependencies
--> Running transaction check
---> Package apr.x86_64 0:1.7.2-1.amzn2.0.1 will be erased
---> Package apr-util.x86_64 0:1.6.3-1.amzn2.0.1 will be erased
---> Package apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1 will be erased
---> Package generic-logos-httpd.noarch 0:18.0.0-4.amzn2 will be erased
---> Package httpd.x86_64 0:2.4.66-1.amzn2.0.1 will be erased
---> Package httpd-filesystem.noarch 0:2.4.66-1.amzn2.0.1 will be erased
---> Package httpd-tools.x86_64 0:2.4.66-1.amzn2.0.1 will be erased
---> Package mailcap.noarch 0:2.1.41-2.amzn2 will be erased
---> Package mod_http2.x86_64 0:1.15.19-1.amzn2.0.2 will be erased
--> Finished Dependency Resolution
amzn2-core/2/x86_64                                      | 3.6 kB     00:00     

Dependencies Resolved

================================================================================
 Package                Arch      Version                  Repository      Size
================================================================================
Removing:
 apr                    x86_64    1.7.2-1.amzn2.0.1        @amzn2-core    275 k
 apr-util               x86_64    1.6.3-1.amzn2.0.1        @amzn2-core    206 k
 apr-util-bdb           x86_64    1.6.3-1.amzn2.0.1        @amzn2-core     11 k
 generic-logos-httpd    noarch    18.0.0-4.amzn2           @amzn2-core     21 k
 httpd                  x86_64    2.4.66-1.amzn2.0.1       @amzn2-core    4.2 M
 httpd-filesystem       noarch    2.4.66-1.amzn2.0.1       @amzn2-core    366  
 httpd-tools            x86_64    2.4.66-1.amzn2.0.1       @amzn2-core    172 k
 mailcap                noarch    2.1.41-2.amzn2           @amzn2-core     62 k
 mod_http2              x86_64    1.15.19-1.amzn2.0.2      @amzn2-core    382 k

Transaction Summary
================================================================================
Remove  9 Packages

Installed size: 5.3 M
Downloading packages:
Running transaction check
Running transaction test
Transaction test succeeded
Running transaction
  Erasing    : httpd-2.4.66-1.amzn2.0.1.x86_64                              1/9 
  Erasing    : mod_http2-1.15.19-1.amzn2.0.2.x86_64                         2/9 
  Erasing    : mailcap-2.1.41-2.amzn2.noarch                                3/9 
  Erasing    : httpd-filesystem-2.4.66-1.amzn2.0.1.noarch                   4/9 
  Erasing    : generic-logos-httpd-18.0.0-4.amzn2.noarch                    5/9 
  Erasing    : httpd-tools-2.4.66-1.amzn2.0.1.x86_64                        6/9 
  Erasing    : apr-util-1.6.3-1.amzn2.0.1.x86_64                            7/9 
  Erasing    : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                        8/9 
  Erasing    : apr-1.7.2-1.amzn2.0.1.x86_64                                 9/9 
  Verifying  : apr-1.7.2-1.amzn2.0.1.x86_64                                 1/9 
  Verifying  : apr-util-bdb-1.6.3-1.amzn2.0.1.x86_64                        2/9 
  Verifying  : mod_http2-1.15.19-1.amzn2.0.2.x86_64                         3/9 
  Verifying  : apr-util-1.6.3-1.amzn2.0.1.x86_64                            4/9 
  Verifying  : mailcap-2.1.41-2.amzn2.noarch                                5/9 
  Verifying  : generic-logos-httpd-18.0.0-4.amzn2.noarch                    6/9 
  Verifying  : httpd-2.4.66-1.amzn2.0.1.x86_64                              7/9 
  Verifying  : httpd-filesystem-2.4.66-1.amzn2.0.1.noarch                   8/9 
  Verifying  : httpd-tools-2.4.66-1.amzn2.0.1.x86_64                        9/9 

Removed:
  apr.x86_64 0:1.7.2-1.amzn2.0.1                                                
  apr-util.x86_64 0:1.6.3-1.amzn2.0.1                                           
  apr-util-bdb.x86_64 0:1.6.3-1.amzn2.0.1                                       
  generic-logos-httpd.noarch 0:18.0.0-4.amzn2                                   
  httpd.x86_64 0:2.4.66-1.amzn2.0.1                                             
  httpd-filesystem.noarch 0:2.4.66-1.amzn2.0.1                                  
  httpd-tools.x86_64 0:2.4.66-1.amzn2.0.1                                       
  mailcap.noarch 0:2.1.41-2.amzn2                                               
  mod_http2.x86_64 0:1.15.19-1.amzn2.0.2                                        

Complete!
```

# Task 4: Install the AWS CLI on Red Hat Linux
Here I installed the AWS CLI on Amazon Elastic Compute Cloud (Amazon EC2) Linux.

1. I verified that Python is installed.
```bash
[ec2-user@ip-10-0-10-161 ~]$ python3 --version
Python 3.7.16
```
I have Python Python 3 version 3.7+, so I can continue with the AWS CLI imstallation.

2. I checked that the pip package manager is already installed.
```bash
[ec2-user@ip-10-0-10-161 ~]$ pip3 --version
pip 20.2.2 from /usr/lib/python3.7/site-packages/pip (python 3.7)
```
**Note**: The primary distribution method for the AWS CLI on Linux, Windows, and macOS is pip. pip is a package manager for Python that provides you with an easy way to install, upgrade, and remove Python packages and their dependencies.

3. In order to install the AWS CLI, I downloaded the installation file using the **curl** command. 
```bash
[ec2-user@ip-10-0-10-161 ~]$ curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 63.7M  100 63.7M    0     0   276M      0 --:--:-- --:--:-- --:--:--  277M
```
The `-o` option specifies the file name that the downloaded package is written to. In this case, the command write the downloaded file to the current directory with the local name `awscliv2.zip`.

4. I unzipped the installer. 
```bash
[ec2-user@ip-10-0-10-161 ~]$ unzip awscliv2.zip
Archive:  awscliv2.zip
   creating: aws/
   creating: aws/dist/
  inflating: aws/README.md           
  inflating: aws/install            
....
[ec2-user@ip-10-0-10-161 ~]$ ll
total 65332
drwxr-xr-x  3 ec2-user ec2-user        78 Mar 13 18:16 aws
-rw-rw-r--  1 ec2-user ec2-user  66897254 Mar 15 13:13 awscliv2.zip
drwxr-xr-x 11 ec2-user Personnel      184 Mar 15 12:40 companyA
```

5. I run the install program.
```bash
[ec2-user@ip-10-0-10-161 ~]$ sudo ./aws/install
You can now run: /usr/local/bin/aws --version
```
The installation command uses a file named install in the newly unzipped aws directory. By default, the files are all installed to /usr/local/aws-cli, and a symbolic link is created in /usr/local/bin. The command includes sudo to grant write permissions to those directories.

6. To verify that the AWS CLI is now working, I typed `aws help`. The help command displayed the help information for the AWS CLI.
```bash
AWS()                                                                    AWS()



NAME
       aws -

DESCRIPTION
       The  AWS  Command  Line  Interface is a unified tool to manage your AWS
       services.

SYNOPSIS
          aws [options] <command> <subcommand> [parameters]

       Use aws command help for information on a  specific  command.  Use  aws
       help  topics  to view a list of available help topics. The synopsis for
       each command shows its parameters and their usage. Optional  parameters
       are shown in square brackets.

GLOBAL OPTIONS
       --debug (boolean)

       Turn on debug logging.

       --endpoint-url (string)
:
```
And then press `q` to exit.

# Task 5: Configure the AWS CLI to connect to your AWS account

1. I configured the **AWS CLI** with these options.
```bash
[ec2-user@ip-10-0-10-161 ~]$ aws configure
AWS Access Key ID [None]: 
AWS Secret Access Key [None]: 
Default region name [None]: us-west-2
Default output format [None]: json
```

2. In the file `~/.aws/credentials` I copied the **aws_access_key_id** and **aws_secret_access_key** for my lab. It was something like this.
```
[default]
aws_access_key_id=<your access key ID>
aws_secret_access_key=<your access key>
aws_session_token=<your session token>
```
To edit the file I used the `nano` editor with `sudo`, `crl+o` and `enter` to save the file, `crl+x` to exit the editor.

3. From the **AWS Management Console** I copied the istance ID of the **Command Host** istance.

4. Then on the terminal, I used the command `aws ec2` with the option to retrive the `istanceType` from the given `istance ID`
```bash
[ec2-user@ip-10-0-10-161 ~]$ aws ec2 describe-instance-attribute --instance-id i-0acc6bb474b327f89 --attribute instanceType
{
    "InstanceId": "i-0acc6bb474b327f89",
    "InstanceType": {
        "Value": "t3.micro"
    }
}
```
