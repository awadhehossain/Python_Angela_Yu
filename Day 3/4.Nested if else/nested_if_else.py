print("Welcome to the rollercoaster!")
height=int(input("What is your in cm?\n"))
if height>120:
    print("You can ride the rollercoaster.")
    age=int(input("What is your age?\n"))
    if age<=12:
        print("Please pay $5")
    elif 12<age<=18:
        print("Please pay $7")
    else:
        print("Please pay $12")

else:
    print("Sorry you have to grow taller before riding!")