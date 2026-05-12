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

