print("This is a BMI calculator made by Talal")

name = input("Enter your name: ")
height_m = float(input("Enter your height in meters: "))
weight_kg = float(input("Enter your weight in kilograms: "))

def bmi_calculator(name, height_m, weight_kg):
    print(name)
    bmi = weight_kg / (height_m ** 2)
    print(bmi)
    if bmi > 25:
        return name + " is overweight"
    else:
        return name + " is not overweight"

result = bmi_calculator(name, height_m, weight_kg)

print(result)