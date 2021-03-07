# list0 = list()
list1 = [1, 2, 3, 100, True, False, "hello", "working", 99.99, 3.14]
print(list1[0])
print(list1[0::3])
print(list1[-1])
print(list1[-1:-6:-2])
print(list1[-1::-1])
print(list1[-1:-6])
print(list[-1::-1])

list1.reverse()  # reverses list in place
# means list will be reversed permanently and nothing will be returned
print(list1)

# range(10) -> range(0,10) -> [0, .. ,9]
# range(5,10) -> [5,6,7,8,9,10]
# range(5,100,5) -> [5,10,15,20,25,..,100]
