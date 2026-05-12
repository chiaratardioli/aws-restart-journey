# Challenge Lab: Python Scripting Exercise


## Your Challenge
- Write a Python script to:
  - Display all the **prime numbers between 1 to 250**.
  - Store the results in a **results.txt** file.
- Test the script. Verify that it produced the expected results in the results.txt file.
- Save the script and make a note of its location (absolute path) for future reference.
- Use *python3*

## Solution

I decide to use a brute-force approach to find the prime numbers between 1 and 250.
I log to the EC2 instance via SSH and create a folder `python`.
There I create the program [prime_numbers.py](./python-scripts/prime_numbers.py) 
so that the location of my python script is `/home/ec2-user/python`.

```python
# ----------------------------------------------------------------------------------
#                  PRIME NUMBERS BETWEEN 1 AND 250
# Python 3.11.3
# Coding: utf-8
# Author: CT, 2026.04.15
# ----------------------------------------------------------------------------------
import math

def is_prime(number):
    max_div=int(math.sqrt(number))
    d=2
    while(d<=max_div):
        if number % d == 0:
            return False
        d+=1
    return True
    
def write_on_file(filename, list):
    with open(filename, "w") as file:
        file.write("\n".join(str(n) for n in list))
        file.write("\n")
    
def main():
    start=2
    end=250
    prime_list=[]
    for n in range(start,end):
        if is_prime(n):
            prime_list.append(n)
    print(f"There are {len(prime_list)} prime numbers between {start} and {end}")
    print(",".join(str(n) for n in prime_list))
    write_on_file("results.txt", prime_list)
    
main()
```

To run the code, while in the folder `python`, I type on terminal:
```bash
python3 prime_numbers.py
```

The program returns the following output on screen:
```bash
[ec2-user@ip-10-1-11-68 python]$ python3 prime_numbers.py 
There are 53 prime numbers between 2 and 250
2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101,103,107,109,113,127,131,137,139,149,151,157,163,167,173,179,181,191,193,197,199,211,223,227,229,233,239,241
```

The program also prints the prime numbers on the file [results.txt](./files/results.txt), one number per line.
First I check that the number of rows of the file is equal to the total number of prime numbers found by the program:
```bash
[ec2-user@ip-10-1-11-68 python]$ wc -l results.txt 
53 results.txt
```

Then I open the file and manually check the results. All prime numbers were there, as expected.
