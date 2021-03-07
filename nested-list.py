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

list1 = []
for i in range(100):
    if i % 2 == 0:
        list1.append(i**2)
print(list1)

# [i+1 for i in [0,1,2,3,4]]  -> list comprehension
# [append_expression loop condition]
# [1]

print([i**2 for i in range(100) if i % 2 == 0])

# import numpy
# # size = 3,5
# list1 = [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
# print(list1)
# print(numpy.array(list1))
