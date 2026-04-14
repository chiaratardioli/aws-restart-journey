# Calculating the Net Charge of Insulin by Using Python Lists and Loops

I will use lists, for and while loops, and basic math to calculate the net charge of insulin from pH 0 to pH 14.

## Solution: Net Charge of Insulin

The python code is [net-charge.py](./python-scripts/net-charge.py).

This program calculates the net charge of insulin from pH 0 to 14 based on the ionization of amino acids.

Net Charge = positive residues (K, H, R) − negative residues (Y, C, D, E)

The charge varies with pH:
- Low pH → positive charge  
- High pH → negative charge  
- Net charge = 0 → isoelectric point (pI)

![Insulin Net Charge](./images/PY11-net-charge.png)

## Conclusion
- I created a dictionary of pKa values (which indicate the strength of an acid) that will be used in the net charge calculations
- I used the count() method to get a count of amino acids
- I used a while loop to calculate the net charge of insulin from pH 0 to pH 14
