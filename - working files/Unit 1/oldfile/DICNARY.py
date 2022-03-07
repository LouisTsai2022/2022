students = ["Peter", "Paul", "Mary"] #a list
# print(students[0])

students_ages = {} #empty dictionary
students_ages["Elliot"] = 16
students_ages["Ronan"] = 17
students_ages['Matthew'] = 17
students_ages['Louis'] = 18
print(len(students_ages))

if "Ronan" in students_ages:
    print(students_ages['Ronan'])

#ask put in name if not put name in dic
name = input("Enter Name: ")
if name not in students_ages:
    age = int(input("Enter Age: "))
    students_ages[name] = age
print(students_ages)

#how to loop throw dic printing keys and value



