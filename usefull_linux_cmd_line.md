# 🐧 Useful Linux Command Line Cheat Sheet

![Platform](https://img.shields.io/badge/platform-linux-blue)
![Maintained](https://img.shields.io/badge/maintained-yes-brightgreen)
![Contributions](https://img.shields.io/badge/contributions-welcome-orange)
![License](https://img.shields.io/badge/license-MIT-green)

A quick reference guide for commonly used Linux commands including system information, file operations, and user administration.

---

# 💻 Terminal Preview Example

```bash
student@linux:~$ whoami
student

student@linux:~$ uptime
10:21:02 up 3 days, 4:17, 1 user, load average: 0.10, 0.05, 0.02

student@linux:~$ grep student /etc/passwd
student:x:1001:1001::/home/student:/bin/bash
```

---

# ⚡ Ultra-Fast Linux Command Reference

| Command | Purpose | Example |
|-------|--------|--------|
| `whoami` | Show current user | `whoami` |
| `id` | Show UID and groups | `id` |
| `hostname` | Show system hostname | `hostname` |
| `uptime` | Show system uptime | `uptime` |
| `date` | Show current date/time | `date` |
| `cal` | Display calendar | `cal` |
| `clear` | Clear terminal screen | `clear` |
| `echo` | Print text | `echo "Hello"` |
| `history` | Command history | `history` |
| `touch` | Create file | `touch file.txt` |
| `cat` | Show file content | `cat file.txt` |
| `head` | First lines of file | `head -n 5 file.txt` |
| `tail` | Last lines of file | `tail -n 5 file.txt` |
| `grep` | Search text | `grep user /etc/passwd` |
| `|` | Pipe command output | `ls /etc \| grep passwd` |
| `useradd` | Create user | `useradd username` |
| `usermod` | Modify user | `usermod -aG group user` |
| `userdel` | Delete user | `userdel -r username` |
| `passwd` | Change password | `passwd username` |
| `groupadd` | Create group | `groupadd devs` |
| `groupmod` | Modify group | `groupmod -n new old` |
| `groupdel` | Delete group | `groupdel devs` |
| `gpasswd` | Manage group users | `gpasswd -a user group` |
| `su` | Switch user | `su - root` |
| `sudo` | Run command as admin | `sudo command` |
| `visudo` | Edit sudo config | `visudo` |

---

# 📚 Command Categories

| Category | Description | Commands |
|---------|-------------|---------|
| 🖥 System Information | View system status | whoami, id, hostname, uptime, date, cal |
| 💻 Terminal Output | Terminal interaction | clear, echo, history |
| 📂 File Management | File creation & viewing | touch, cat, head, tail |
| 🔎 Searching & Pipes | Search and command chaining | grep, \| |
| 👤 User Management | Manage user accounts | useradd, usermod, userdel, passwd |
| 👥 Group Management | Manage user groups | groupadd, groupmod, groupdel, gpasswd |
| 🔐 Privileges | Administrative commands | su, sudo, visudo |

---

# 📑 Table of Contents

- [System Information](#system-information)
- [Terminal & Output](#terminal--output)
- [File Management](#file-management)
- [Text Searching & Pipes](#text-searching--pipes)
- [User Management](#user-management)
- [Group Management](#group-management)
- [Privilege & Access](#privilege--access)

---

# System Information

### whoami
Displays the current username.

Example:
```bash
whoami
```

---

### id
Displays user ID (UID), group ID (GID), and group memberships.

```bash
id
```

---

### hostname
Displays or sets the system hostname.

```bash
hostname
```

---

### uptime
Shows how long the system has been running since the last boot.

```bash
uptime
```

---

### date
Displays or sets the system date and time.

```bash
date
```

---

### cal
Displays a calendar.

```bash
cal
```

---

# Terminal & Output

### clear
Clears the terminal screen.

```bash
clear
```

---

### echo
Prints text to the terminal.

```bash
echo "Hello world!"
```

---

### history
Displays previously executed commands.

```bash
history
```

Run a command again:

```bash
!143
```

---

# File Management

### touch
Creates an empty file or updates file timestamps.

```bash
touch file.txt
```

---

### cat
Displays the contents of a file.

```bash
cat file.txt
```

Example:

```bash
sudo cat /etc/passwd | cut -d: -f1
```

---

### head
Displays the first lines of a file.

```bash
head -n 5 file.txt
```

---

### tail
Displays the last lines of a file.

```bash
tail -n 5 file.txt
```

---

# Text Searching & Pipes

### grep
Searches for text inside files.

```bash
grep username /etc/passwd
```

---

### Pipe `|`
Redirects output of one command into another.

```bash
ls /etc | grep passwd
```

---

# User Management

### useradd
Creates a new user.

```bash
useradd username
```

---

### usermod
Modifies an existing user account.

```bash
usermod -aG group username
```

---

### userdel
Deletes a user.

```bash
userdel -r username
```

---

### passwd
Changes a user password.

```bash
passwd username
```

---

# Group Management

### groupadd
Creates a new group.

```bash
groupadd developers
```

---

### groupmod
Modifies a group.

```bash
groupmod -n new_group old_group
```

---

### groupdel
Deletes a group.

```bash
groupdel developers
```

---

### gpasswd
Manages group membership.

```bash
gpasswd -a user group
```

---

# Privilege & Access

### su
Switch user.

```bash
su - root
```

---

### sudo
Run a command with administrative privileges.

```bash
sudo command
```

Check permissions:

```bash
sudo -l
```

---

### visudo
Safely edit the sudo configuration file.

```bash
visudo
```

Configuration file:

```
/etc/sudoers
```

---

# 🤝 Contributing

Contributions are welcome!  
Feel free to add more Linux commands or examples.
