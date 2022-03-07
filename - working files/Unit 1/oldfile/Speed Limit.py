speed = int(input("Enter your speed in kph: ").strip())

fine = 0

if speed <= 100:
    print("No fine")
else:
    fine = 50 + ((speed - 100) * 5)
    if speed >= 120:
        fine = fine + 200
    print("fine is", fine)
