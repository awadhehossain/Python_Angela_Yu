height = float(input("Enter your height in meters:\n"))
weight = float(input("Enter your weight in kg:\n"))

# Calculate the BMI using weight and height.
bmi = weight / (height ** 2)
print("Your BMI is:", bmi)
