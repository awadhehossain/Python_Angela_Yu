#Learn to use the Python input() function to collect user input 
input()

# We can also give message to the users what he input their
# A message in input Funtion.

input("What is your name?")

#For a better output we can use newline after the message

input("What is your name?\n")

# Users input his name only 
#You are looking to print a sentence like this:
#Hello Name!
#e.g. Hello Awadhe!
# In this task you have to take a name from user and prind this name 
# with extra "Hello" and "!" two string 
 
a=input("What is your name?\n")
print("Hello"+" "+a+"!")

#Or you can directly print in this process
print("Hello"+" "+input("What is your name?\n")+"!")
