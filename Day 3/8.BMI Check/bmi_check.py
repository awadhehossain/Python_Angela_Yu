height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kg:\n"))
bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇
if bmi<18.5:
    print("underweight")
elif 18.5<=bmi<25:
    print("normal weight")
else:
    print("overweight")