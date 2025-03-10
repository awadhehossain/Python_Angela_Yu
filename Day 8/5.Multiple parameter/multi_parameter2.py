def my_function(name,location):
    # This name and location is function parameter
    print(f"Hello {name}.")
    print(f"Is your location in {location}?")

my_function(name=input("What is your name?\n"),location=input("What is your location?\n"))

# Its gives the same output because this time we insert the parameter value directly
my_function(location=input("What is your location?\n"),name=input("What is your name?\n"))


