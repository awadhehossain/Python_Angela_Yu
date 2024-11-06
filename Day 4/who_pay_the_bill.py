# Method 1
import random
Friend_list=["Awadhe","Sifat","Shawon","Komol","Shakil","Shomrat"]
a=random.randint(0,len(Friend_list)-1)
# 0r a=random.randint(0,5)
# Or a=random.randint(1,len(Friend_list))
# If we do this we have to change the if elif condition first start with 1 not 0
if a==0:
    print("Awadhe will pay the bill")
elif a==1:
    print("Sifat will pay the bill")
elif a==2:
    print("Shawon will pay the bill")
elif a==3:
    print("komol will pay the bill")
elif a==4:
    print("Shakil will pay the bill")
else:
    print("Shomrat will pay the bill")

# Method 2
b=random.randint(0,5)
print(Friend_list[b]+" Will pay the bill") 

# Method 3 use coice function
s=random.choice(Friend_list)
print(f"{s} will pay the bill")



