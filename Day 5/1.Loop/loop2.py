print("1. I hate you")
print("2. I love you")
print("3. I am sorry")

I = int(input("Which line do you want to print?\n"))
a = int(input("How many times do you want to print?\n"))

if I == 1:
    for k in range(a):
        print(f"{k+1}.I hate you")
elif I == 2:
    for k in range(a):
        print(f"{k+1}.I love you")
elif I == 3:
    for k in range(a):
        print(f"{k+1}.I am sorry")
else:
    print("Invalid selection")
