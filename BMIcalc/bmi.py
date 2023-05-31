height = input("Enter your height: ")
weight = input("Enter your weight: ")
bmi = float(weight)/(float(height) ** 2)
print("BMI = " + str(int(bmi)) + " kg/m²")

if bmi <= 18.5:
    print("You are underweight")

elif 18.5 < bmi <= 25:
    print("You have normal weight")

elif 25 < bmi <= 30:
    print("You are over weight")

elif 30 < bmi <= 35:
    print("You are obese")
elif bmi > 35:
    print("Clinical obese")


