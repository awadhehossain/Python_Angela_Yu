name=["Awadhe","Shomrat","Sifat","Arfan"]
# Printing name one by one use function

for Name in name:
    print(Name)

# Add another substring and print all string from the list one by one

name=["Awadhe","Shomrat","Sifat","Arfan"]
for Name in name:
    print(Name+" Hossain")

# Fun 
# Add individual name title use if else condition

name=["Awadhe","Shomrat","Sifat","Arfan"]
for Name in name:
    if Name=="Awadhe":
        print(Name+" Hossain")
    elif Name=="Shomrat":
        print(Name+" Shikder")
    elif Name=="Sifat":
        print("Md "+Name)
    else:
        print(Name+" Khan")

