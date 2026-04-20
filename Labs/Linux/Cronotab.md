# Linux Administration Lab – Processes and Cron Jobs

In this lab, I learned essential Linux system administration skills, including process monitoring and task automation. The exercises included:

- Listing and filtering system processes
- Monitoring system performance using `top`
- Creating an automated task with `cron`

All tasks were performed in the directory:

```
/home/ec2-user/companyA
````

## Task 2: Create a List of Processes

### Objective

In this task, I learned how to generate a log file of running processes while filtering out unwanted entries. Specifically, I created a file named `processes.csv` that excluded:

- Processes owned by the `root` user
- Commands containing `[` or `]`

The log file was stored in the `SharedFolders` directory.

### Step 1: Verify the Working Directory

I first confirmed that I was in the correct folder:

```bash
pwd
````

Expected output:

```
/home/ec2-user/companyA
```

If I was not in the correct folder, I navigated there using:

```bash
cd companyA
```

### Step 2: Generate the Process Log

I ran the following command to list all processes while excluding the `root` user:

```bash
sudo ps -aux | grep -v root | sudo tee SharedFolders/processes.csv
```

This command allowed me to:

* Display all running processes (`ps -aux`)
* Filter out `root` processes (`grep -v root`)
* Save the output to a file while also viewing it (`tee`)

The file was saved as:

```
SharedFolders/processes.csv
```

### Step 3: Verify the Log File

To ensure that the log file contained the correct data, I viewed its contents:

```bash
cat SharedFolders/processes.csv
```

I confirmed that the file correctly listed the processes and excluded the unwanted entries.

## Task 3: Monitor Processes Using `top`

## Objective

In this task, I learned how to monitor system performance and active processes in real time using the `top` command.

### Step 1: Run the `top` Command

I executed:

```bash
top
```

This command provided a live view of system activity, showing:

* Total number of processes
* Running and sleeping tasks
* CPU and memory usage
* Swap usage

Example output I observed:

```
Tasks: 93 total, 1 running, 48 sleeping, 0 stopped, 0 zombie
```

I learned to interpret the task states:

| State    | Meaning                                   |
| -------- | ----------------------------------------- |
| Running  | Processes currently executing             |
| Sleeping | Processes waiting for resources           |
| Stopped  | Suspended processes                       |
| Zombie   | Completed processes waiting to be removed |

---

### Step 2: Exit `top`

I exited `top` by pressing:

```
q
```

## Step 3: Display Help and Version Information

I also explored the help and version options:

```bash
top -hv
```

This allowed me to better understand the available options for `top`.

## Task 4: Create a Cron Job

### Objective

In this task, I learned how to automate a task using `cron`. I created a cron job that generates an audit file covering all `.csv` files. The output file was:

```
SharedFolders/filteredAudit.csv
```

### Step 1: Open the Crontab Editor

I opened the crontab editor with:

```bash
sudo crontab -e
```

Since the editor opened in `vi`, I entered insert mode by pressing:

```
i
```

### Step 2: Add the Cron Configuration

I added the following lines:

```bash
SHELL=/bin/bash
PATH=/usr/bin:/bin:/usr/local/bin
MAILTO=root
0 * * * * ls -la $(find .) | sed -e 's/..csv/#####.csv/g' > /home/ec2-user/companyA/SharedFolders/filteredAudit.csv
```

Through this, I learned:

* How to define the shell (`SHELL`) and path (`PATH`) for cron jobs
* How to set email notifications (`MAILTO`)
* How to schedule a job every hour (`0 * * * *`)
* How to use `find` and `sed` to manipulate file names
* How to redirect output to a file (`>`)

### Step 3: Save and Exit

I saved and exited the editor by pressing:

```
ESC
```

Then typing:

```
:wq
```

### Step 4: Verify the Cron Job

I verified the cron job with:

```bash
sudo crontab -l
```

I confirmed that the cron configuration matched what I entered.

## Conclusion

In this lab, I learned how to:

* Generate a filtered process log using `ps` and `grep`
* Monitor system performance using the `top` command
* Automate tasks using cron, including creating audit files

This lab helped me understand essential Linux skills related to process management, system monitoring, and task automation.
