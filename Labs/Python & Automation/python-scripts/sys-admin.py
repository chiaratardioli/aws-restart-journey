# Python3.6  
# Coding: utf-8  

import os
import subprocess

# Run the Bash command ls using OS.SYSTEM()
os.system("ls")

# Run the Bash command ls using SUBPROCESS.RUN()
# subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, 
#    capture_output=False, shell=False, cwd=None, timeout=None, check=False, 
#    encoding=None, errors=None, text=None, env=None, universal_newlines=None)
subprocess.run(["ls"])

# Run subprocess.run with two arguments
subprocess.run(["ls","-l"])

# Run subprocess.run with three arguments
subprocess.run(["ls","-l","README.md"])

# Retrieve system information
command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])

# Retrieve information about disk space
command="ps"
commandArgument="-x"
print(f'Gathering active process information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])