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



