# n = int(input("Enter a number: "))
# factor_count = 0
# for i in range(2, n+1):
#     if n % i == 0:
#         print (i)
#         factor_count += 1
#
# if factor_count > 1:
#     print(n, "is not a prime")
# else:
#     print(n, "is a prime")




for i in range(1,6): #loop for each line
    output = ""      #line string
    for j in range(1, i+1):
        output += str(i)
    print(output)



# for i in range(5):
#     line = ""
#     for j in range(0,i):
#         line = line + "_"
#     line = line + "#"
#     print(line)

