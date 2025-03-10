# A and B #Both conditions need to be true
# C or D #Only one condition needs to be true
# not E  The condition must be false

a=input("Input any number: ")
b=input("Input any number: ")

if a<20 and b>10:
    print("A and B") # A and B #Both conditions need to be true
else:
    print("!!!!!!!")# A or B false

if a<20 or b>10:
    print("A and B") # A and B # Only one condition needs to be true
else:
    print("!!!!!!!")# A and  B # Both conditions need to be false

if a!=10:
    print("A") # A=(Except 10)
else:
    print("!!!!!!!")# For only 10



