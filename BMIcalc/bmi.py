height = input("Enter your height: ")
weight = input("Enter your weight: ")
mbi = float(weight)/(float(height) ** 2)
print("BMI = " + str(int(mbi)) + " kg/m²")
