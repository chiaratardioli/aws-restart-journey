# Useful Linux Command Line

## whoami
The concatenation of the strings **who**, **am**, and **i** is `whoami`. In Linux, it's used to show the current user's username when the command is invoked.  
A use case for this command would be to use it after you log in as `UserA`, then switch users and run commands as another user to see the context.

---

## id
The `id` command is used to print real and effective user and group IDs.  
This command helps identify the user and group name and numeric IDs (UID or GID) of the current user or any other user on the server.

---

## hostname
The `hostname` command is used to either set or display the current host, domain, or node name of the system.  
Many networking programs use hostnames to identify the system.

---

## uptime
The `uptime` command indicates how long the system has been up since the last boot.

---

## date
The `date` command provides the current date and time.  
It can display the time in a specific format and can also set the system date.

---

## cal
The `cal` command is used to display a simple calendar.  
If no arguments are specified, the current month is displayed.

**Note:** The month can be specified as:
- A number (1–12)
- A month name
- An abbreviated month name

---

## clear
The `clear` command clears the terminal screen and displays a new prompt.

---

## echo
Example:
```bash
username~$ echo "Hello world!"
```

The `echo` command prints specified text to the screen.  
It is commonly used in scripts to display information to users.

---

## history
The `history` command shows the command history.

Example:
```bash
!143
```

This re-runs the command with event number **143**.

---

## touch
The `touch` command can:
- Create new empty files
- Change or update timestamps on existing files

---

## cat
The `cat` (concatenate) command reads data from files and outputs the contents to the terminal.

Example:
```bash
sudo cat /etc/passwd | cut -d: -f1
```

---

## tail
The `tail` command displays the last lines of a file.

Default: last **10 lines**

Example:
```bash
tail -n 5 /etc/passwd
```

---

## head
The `head` command displays the first lines of a file.

Default: first **10 lines**

Example:
```bash
head -n 5 /etc/passwd
```

---

## useradd
Adds a new user to the system.

Example:
```bash
useradd major
```

Common options:
- `-c` comment
- `-e` expiration date
- `-d` home directory

---

## usermod
The `usermod` command modifies an existing user account.

Example:
```bash
usermod -aG hr,marketing mmajor
```

Common options:
- `-c`
- `-e`
- `-aG`

---

## gpasswd
The `gpasswd` command manages group memberships.

Examples:
```bash
gpasswd -a jdoe marketing
gpasswd -M smartinez,rroe ec2-user
```

Common options:
- `-a` add user
- `-d` remove user
- `-M` set member list
- `-A` set group administrators

---

## userdel
The `userdel` command deletes a user account.

Example:
```bash
userdel -r username
```

`-r` removes the user's home directory.

---

## passwd
The `passwd` command sets or changes user passwords.

- Users can change their own password.
- The root user can reset any password.
- Password characters are not displayed when typed.

---

## grep
The `grep` command searches for a string in a file.

Example:
```bash
grep mmajor /etc/passwd
```

---

## Pipe |
A **pipe (`|`)** redirects the output of one command to another.

Example:
```bash
ls /etc/passwd | grep hello
```

---

## groupadd, groupmod, groupdel
Commands used to manage groups.

Example:
```bash
groupmod -n new_group old_group
```

---

## su
The `su` command switches users.

Examples:
```bash
su root
su - root
su -
su student02
```

- Provides full administrative permissions
- Prompts for the **root password**

---

## sudo
The `sudo` command allows a user to run commands with delegated administrative permissions.

Example:
```bash
sudo -lU student01
```

Key points:
- Users enter **their own password**
- Permissions are logged

Logs:
- `/var/log/messages`
- `/var/log/secure`

---

## visudo
The `visudo` command safely edits the sudo configuration file:

```bash
/etc/sudoers
```

It ensures the file syntax is correct before saving.
