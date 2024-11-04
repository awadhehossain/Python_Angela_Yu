print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
elif size=="L":
    bill+=25
else:
    print("You input he wrong size.")

if pepperoni=="Y":
    bill+=2
elif pepperoni=="N":
    bill+=0
else:
    print("You put the wrong input")

if extra_cheese=="Y":
    bill+=1
elif extra_cheese=="N":
    bill+=0
else:
    print("You put the wrong input")
print(f"Your total bill is {bill}")
print("Thanks for odering the pizza!!!!!")



