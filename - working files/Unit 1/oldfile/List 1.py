# students = []
#
# students.append("Peter")
# students.append("Paul")
# students.append("Marry")
# print(type(students))
# print(students)
# print(students[1])
# print(len(students))
# print(students[-1])
#
# for students in students:
#     print(students)
#
# students.append('Hi')
# print(students)
# students.sort()
# print(students)
# students.reverse()
# print(students)
#
# #########################################################
#
# new_students = ["Somon", "Andrew", "Martha", "Andrea"]
# grades = [23, 45, 79, 32]
#
# for i in range(len(new_studnets)):
#     print(new_students[i], "got the grade", grades[i])

#create a list from string
name = 'Louis'
letters = list(name)
print(letters)

#create a list from splitting a string
name = "Louis Tsai"
name_parts = name.split()
print(name_parts)
first_name = name_parts[0]
last_name = name_parts[1]
print(first_name.upper(), last_name)


