# Bash Shell Scripts

In this lab I created a bash script that will automate the backup of a folder.

### Folder Data Structure
These are the folders in my home folder:
```
home/ec2-user/
|- CompanyA/
|- backups/
```


### Steps:
1. I created the bash script file and assigned permissions:
```bash
$touch backup.sh
$sudo chmod 755 backup.sh
```

2. I typed the command `ls -ltr` to verify the new permissions:
```bash
[ec2-user@ip-10-0-10-243 ~]$ ls -ltr
total 0
drwxr-xr-x 2 ec2-user root      6 Mar 15 10:58 backups
drwxr-xr-x 8 ec2-user root     97 Mar 15 10:58 CompanyA
-rwxr-xr-x 1 ec2-user ec2-user  0 Mar 15 11:05 backup.sh
```

3. Then I opend the file with the `vi` editor and I inserted the code:
```bash
#!/bin/bash                                                                                                           
DAY="$(date +%Y_%m_%d)"                                                       
BACKUP="/home/$USER/backups/$DAY-backup-CompanyA.tar.gz"                             
tar -csvpzf $BACKUP /home/$USER/CompanyA     
```
Note:

- I use the date +%Y%m%d command to retrieve the current date and time. This command formats this information as follows: 2021_08_31.

- $USER returns the current user, which is ec2-user in this lab. This is the equivalent of entering the whoami command in the shell. The created archive will be located in /home/ec2-user/backups.

4. I pressed the Esc key and entered `:wq` to save my script and exit from the editor.

5. Eventually, I run the backup.sh file:
```bash
./backup.sh
```

6. To verify that the archive is created in the backups folder, I used this command:
```bash
ls backups/
```

### Conclusion
This type of script are useful because they can be scheduled via cron to create a daily backup of the folder. 
I could also use other commands to copy this archive to other servers.
