hight = float(input("Enter your hight in meters: ").strip())

weight = float(input("Enter your weight in kg: ").strip())

BMI = weight / (hight * hight) # height power 2

if BMI < 18.5:
    msg = "Below healthy range"
elif BMI >= 18.5 and BMI <= 24.9:
    msg = "Within healthy range"
else:
    msg = "Above healthy range"

print(msg)

