def greet_information(name,location):
    print(f"Hello {name}.")
    print(f"What is it like in {location}?")

Name=input("What is your name?\n")
Location=input("Give me a location name\n")

greet_information(name=Name,location=Location)

greet_information(location=Location,name=Name)

# Order is not nesseary

