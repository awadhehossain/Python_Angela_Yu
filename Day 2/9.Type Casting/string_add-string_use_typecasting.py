name_of_the_user = input("Enter your name:\n")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))  #type casting 

#Fun
print("Number of letters in your name: " + str(len(input("Enter your name:\n"))))