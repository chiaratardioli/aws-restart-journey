# Challenge Lab: Bash Shell Scripting Exercise

## Assignment

Write a Bash script based on the following requirements:
- Creates 25 empty (0 KB) files. (Hint: Use the **touch** command.)
- The file names should be **<yourName><number>, <yourName><number+1>, <yourName><number+2>**, and so on.
- Design the script so that each time you run it, it creates the next batch of 25 files with increasing numbers starting with the last or maximum number that already exists.
- Do not hard code these numbers. You need to generate them by using automation.
- Test the script. Display a long list of the directory and its contents to validate that the script created the expected files.

## My solutions

1. I created a new file called `bash_script.sh`.
```bash
touch bash_scripting.sh
```

2. Then I inserted the code using the `vi` editor
```bash
#!/bin/bash

prefix="Chiara"

max=$(ls ${prefix}* 2>/dev/null | sed 's/[^0-9]//g' | sort -n | tail -1)
max=${max:-0}
echo "Previous number: $max"

for i in {1..25}
do
#echo ${prefix}$(($i+$max))
touch ${prefix}$(($i+$max))
done
```

3. I made the file executable and run it.
```bash
chmod 744 bash_scripting.sh
./bash_scripting.sh
```

4. After the first run, here it is displayed the content of my directory.
```bash
[ec2-user@ip-10-0-10-227 ~]$ ./bash_script.sh 
Previous number: 0
[ec2-user@ip-10-0-10-227 ~]$ ll
total 4
-rwxr--r--  1 ec2-user ec2-user  230 Mar 15 15:11 bash_script.sh
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara1
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara10
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara11
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara12
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara13
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara14
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara15
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara16
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara17
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara18
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara19
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara2
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara20
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara21
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara22
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara23
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara24
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara25
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara3
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara4
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara5
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara6
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara7
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara8
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara9
drwxr-xr-x 11 ec2-user Personnel 184 Mar 15 14:59 companyA
```
5. And the content after the second run.
```bash
[ec2-user@ip-10-0-10-227 ~]$ ./bash_script.sh 
Previous number: 25
[ec2-user@ip-10-0-10-227 ~]$ ll
total 4
-rwxr--r--  1 ec2-user ec2-user  230 Mar 15 15:11 bash_script.sh
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara1
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara10
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara11
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara12
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara13
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara14
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara15
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara16
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara17
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara18
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara19
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara2
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara20
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara21
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara22
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara23
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara24
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara25
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara26
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara27
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara28
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara29
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara3
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara30
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara31
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara32
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara33
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara34
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara35
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara36
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara37
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara38
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara39
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara4
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara40
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara41
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara42
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara43
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara44
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara45
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara46
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara47
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara48
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara49
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara5
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:18 Chiara50
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara6
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara7
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara8
-rw-rw-r--  1 ec2-user ec2-user    0 Mar 15 15:17 Chiara9
drwxr-xr-x 11 ec2-user Personnel 184 Mar 15 14:59 companyA
```



