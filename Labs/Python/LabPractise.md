# AWS Cloud9 : Practise Python

### Accessing the AWS Cloud9 IDE

## Labs

![AWS Cloud9 IDE](./images/PY00.png)

### 1. Creating a Hello, World Program

Python file name: `hello-world.py`
```python
#Exercise 2: Writing your first Python program
print("Hello, World")
```

![Hello World!](./images/py-1.png)

### 2. Working with Numeric Data Types

Python file name: `numeric-data.py`
```python
print("Python has three numeric types: int, float, and complex")

# Exercise 2: Introducing the int data type
myValue=1
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

# Exercise 3: Introducing the float data type
myValue=3.14
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))


# Exercise 4: Introducing the complex data type
myValue=5j
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

# Exercise 5: Introducing the bool data type
myValue=True
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))

myValue=False
print(myValue)
print(type(myValue))
print(str(myValue) + " is of the data type " + str(type(myValue)))
```

![Numeric Data Types](./images/PY02.png)

### 3. Working with the String Data Type

Python file name: `string-data.py`
```python
# Exercise 1: Introducing the string data type
myString = "This is a string."
print(myString)
print(type(myString))
print(myString + " is of the data type " + str(type(myString)))

# Exercise 2: Working with string concatenation
firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString)

# Exercise 3: Working with input strings
name = input("What is your name? ")
print(name)

# Exercise 4: Formatting output strings
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("{}, you like a {} {}!".format(name,color,animal))
```

![String Data Type](./images/PY03.png)

### 4. Working with Lists, Tuples, and Dictionaries

Python file name: `collections.py`
```python
# Exercise 1: Introducing the list data type

# 1.1 efining a list
myFruitList = ["apple", "banana", "cherry"]
print(myFruitList)
print(type(myFruitList))


# 1.2 Accessing a list by position
print(myFruitList[0])   # apple
print(myFruitList[1])   # banana
print(myFruitList[2])   # cherry

# 1.3 Changing the values in a list: change cherry to orange
myFruitList[2] = "orange"
print(myFruitList)

# Exercise 2: Introducing the tuple data type

# 2.1 Defining a tuple
myFinalAnswerTuple = ("apple", "banana", "pineapple")
print(myFinalAnswerTuple)
print(type(myFinalAnswerTuple))

# 2.2 Accessing a tuple by position
print(myFinalAnswerTuple[0])  # apple
print(myFinalAnswerTuple[1])  # banana
print(myFinalAnswerTuple[2])  # pineapple


# Exercise 3: Introducing the dictionary data type

# 3.1 Defining a dictionary
myFavoriteFruitDictionary = {
  "Akua" : "apple",
  "Saanvi" : "banana",
  "Paulo" : "pineapple"
}
print(myFavoriteFruitDictionary)
print(type(myFavoriteFruitDictionary))

# 3.2 Accessing a dictionary by name
print(myFavoriteFruitDictionary["Akua"])    # Akua's favorite fruit
print(myFavoriteFruitDictionary["Saanvi"])  # Saanvi's favorite fruit
print(myFavoriteFruitDictionary["Paulo"])   # Paulo's favorite fruit
```

![Lists, Tuples, and Dictionaries](./images/PY04.png)

### 5. Categorizing Values

Python file name: `.py`
```python

```

![Categorizing Values](./images/PY05.png)

### 6.

Python file name: `.py`
```python

```

![](./images/PY06.png)

### 7.

Python file name: `.py`
```python

```

![](./images/PY07.png)

### 17.

Python file name: `.py`
```python

```

![](./images/PY08.png)
