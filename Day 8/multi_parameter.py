def my_function(name,location):
    # This name and location is function parameter
    print(f"Hello {name}.")
    print(f"Is your location in {location}?")

name=input("What is your name?\n")
location=input("What is your location?\n")
# This name and location is variable which passes through the parameter both are not same thing 
# Also the sequence should be maintained otherwise you dont get the actuall output
my_function(name,location)

