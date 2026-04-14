# Creating File Handlers and Modules for Retrieving Information about Insulin


## Solution

I created the JSON molecules data file [insulin.json](./files/insulin.json).
This JSON document stores all the information of previous lab, such as the insulin molecules, the numeric weights of the amino acids and the actual weight of the insulin molecule

The python files for this lab are: 
- [calc_weight_json.py](./python-scripts/calc_weight_json.py)
- [jsonFileHandler.py](./python-scripts/jsonFileHandler.py)

The output files are stored in a subfolder named `files`.

![File Handlers and Modules for Retrieving Information about Insulin](./images/PY14-FileHandler-insulin.png)

## Conclusion
- I created a module
- I opened a file and load the JSON data it contains using the built-in JSON module of Python
- I parsed the JSON structure to access insulin data
- I calculated the rough molecular weight of human insulin using given code (similar to the lab Working with the String Sequence and Numeric Weight of Insulin in Python)
