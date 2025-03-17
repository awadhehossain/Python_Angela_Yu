# 1
# Create a dictionary 
# We create a dictionary by placing key: value pairs inside curly brackets {}
# separated by commas.
Country_capitals={"Bangladesh": "Dhaka","Germany": "Berlin","Canada": "Otawa","England": "London"}

# Printing the dictionary
print(Country_capitals)

# 2
# Access dictionaries itmes
# We can access the value of a dictionary item by placing the key inside square brackets.
print(Country_capitals["Bangladesh"])
print(Country_capitals["Germany"])

# We can also do this use get function
# The get() method returns the value of the specified key in the dictionary.
print(Country_capitals.get("Bangladesh"))
print(Country_capitals.get('Germany'))
# We can use single qoutes or double qouters

# 3
# Add Items to a Dictionary
# We can add an item to a dictionary by assigning a value to a new key
Country_capitals["Italy"]="Rome"
print(Country_capitals)

# 4
# Remove dictionary itmes
# We can use the del statement to remove an element from a dictionary.
del Country_capitals["Italy"]
print(Country_capitals)

# We can also use the pop() method to remove an itme from a dictionary
# If we store this in a new variable we can access the dictionary keys value
result=Country_capitals.pop('Bangladesh')
print(result)
print(Country_capitals)

# 5
# If we need to remove all items from a dictionary at once, we can use the clear() method.
# Country_capitals.clear()
# print(Country_capitals)

# 6
# Change dictionary itme
# Python dictionaries are mutable (changeable).
# We can change the value of a dictionary element by referring to its key. 
Country_capitals['Canada']="Ottawa"
print(Country_capitals)

# We can also use the update() method to add or change dictionary it
Country_capitals.update({"England": "New London"})
print(Country_capitals)

# We can also add new itmes by use update method
Country_capitals.update({"Bangladesh": "Dhaka"})
print(Country_capitals)

# 7 
# Find the dictionarty length
print(len(Country_capitals))

# 8
# Iterate Through a Dictionary
# We can iterate through dictionary keys one by one using a for loop.

# Print dictionary keys one by one
for country in Country_capitals:
    print(country)

# Print dictionary values one by one
for country in Country_capitals:
    capital=Country_capitals[country]
    print(capital)

# The keys() method extracts the keys of the dictionary and
# returns the list of keys as a view object.
keys=Country_capitals.keys()
print(keys)

# The values() method returns a view object that
# displays a list of all the values in the dictionary.
value=Country_capitals.values()
print(value)

# WE can copy a dictionary to others
new_dictionary={}
new_dictionary=Country_capitals.copy()
print(new_dictionary)

# The popitem() method removes and returns the (key, value) 
# pair from the dictionary in the Last
new_dictionary.popitem()
print(new_dictionary)

# How setdefault() works when key is in the dictionary?
capital=Country_capitals.setdefault("Korea")
print(capital)

# How setdefault() works when key is not in the dictionary?
age=Country_capitals.setdefault('age', 22)
print(age)









