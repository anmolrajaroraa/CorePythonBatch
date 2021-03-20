# inputByUser = input(
#     "Enter the size of list in a comma-separated fashion: ").split(",")
# for i in range(len(inputByUser)):
#     inputByUser[i] = int(inputByUser[i])

# outerList = list()
# for i in range(inputByUser[0]):
#     innerList = list()
#     outerList.append(innerList)
#     for j in range(inputByUser[1]):
#         innerList.append(i * j)

# print(outerList)

# list1 = []
# for i in range(100):
#     if i % 2 == 0:
#         list1.append(i**2)
# print(list1)

# [i+1 for i in [0,1,2,3,4]]  -> list comprehension
# [append_expression loop condition]
# [1]

# print([i**2 for i in range(100) if i % 2 == 0])

# import numpy
# # size = 3,5
# list1 = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# print(list1)
# print(numpy.array(list1))

# print("Enter the value of X and Y :")
# X, Y = map(int, input().split(","))
# two_dim_list = [[i*j for i in range(Y)] for j in range(X)]
# print(two_dim_list)

# passwords = input("Enter the passwords you would like to have: ").split(",")
# for password in passwords:
#     conditionsMet = 0
#     if(len(password) >= 6 and len(password) <= 12):
#         for char in password:
#             if(char.isupper()):
#                 conditionsMet += 1
#             if(char.islower()):
#                 b = 1
#             if(char.isdigit()):
#                 c = 1
#             if(char in ("#", "$", "@")):
#                 d = 1
#     if(a+b+c+d == 4):
#         print(password)
#         break
# else:
#     print("INVALID PASSWORD")

'''passwords = input("Enter the passwords you would like to have: ").split(",")
for password in passwords:
    conditionsMet = 0
    if(len(password) >= 6 and len(password) <= 12):
        if (any(char.isupper() for char in password)):
            conditionsMet += 1
        if (any(char.islower() for char in password)):
            conditionsMet += 1
        if (any(char.isdigit() for char in password)):
            conditionsMet += 1
        if (any(char in ("#", "$", "@") for char in password)):
            conditionsMet += 1
else:
    print("INVALID PASSWORD")'''

passwords = input("Enter the passwords you would like to have: ").split(",")
validPasswordFound = False

for password in passwords:
    if(len(password) >= 6 and len(password) <= 12):
        if (not any(char.isupper() for char in password)):
            continue
        if (not any(char.islower() for char in password)):
            continue
        if (not any(char.isdigit() for char in password)):
            continue
        if (not any(char in ("#", "$", "@") for char in password)):
            continue
        print(password)
        validPasswordFound = True

if(not validPasswordFound):
    print("INVALID PASSWORD")
