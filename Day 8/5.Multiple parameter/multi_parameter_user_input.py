def greet_information(name,location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

Name=input("What is your name?\n")
Location=input("Give me a location name\n")

greet_information(Name,Location)

greet_information(Location,Name)
# Order is important