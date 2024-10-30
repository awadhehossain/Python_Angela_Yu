# Use temp veriable
a=23
b=56
print(a,b)
temp=a
a=b
b=temp
print(a,b)

# Without temp veriable
num1=23
num2=67
print(num1,num2)
num1 = num1 - num2
num2 = num1 + num2
num1 = num2 - num1
print(num1,num2)