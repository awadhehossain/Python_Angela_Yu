print("Welcome to the rollercoaster!")
height=int(input("What is your in cm?\n"))
bill=0
if height>120:
    print("You can ride the rollercoaster.")
    age=int(input("What is your age?\n"))
    bill=5
    if age<=12:
        print("Child tickets are $5")
    elif 12<age<=18:
        bill=7
        print("Youth tickets are $7")
    else:
        bill=12
        print("Adult tickets are $12")
    want_photos=input("Do you want to  capture any photo? type y for yes or type n for no\n")
    if want_photos=="y":
        bill+=3
    print(f"YOur total bill is ${bill}")    

else:
    print("Sorry you have to grow taller before riding!")