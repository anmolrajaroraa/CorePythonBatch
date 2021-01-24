# num1, num2, num3 = 12, 34, 45

# if (num1 > num2) and (num1 > num3):
#     print("The largest between {0}, {1}, {2} is {0}".format(num1, num2, num3))
# elif (num2 > num1) and (num2 > num3):
#     print("The largest between {0}, {1}, {2} is {1}".format(num1, num2, num3))
# else:
#     print("The largest between {1}, {2}, {0} is {0}".format(num3, num1, num2))


num1, num2, num3 = 12, 34, 45

if (num1 > num2) and (num1 > num3):
    largest = num1
elif (num2 > num1) and (num2 > num3):
    largest = num2
else:
    largest = num3
print("The largest between {}, {}, {} is {}".format(num1, num2, num3, largest))

# num1, num2, num3 = input("1st: "), input("2nd: "), input("3rd: ")
# print(num1, num2, num3)

# numbers = input("Enter three numbers separated by a blank space: ")
# num1, num2, num3 = numbers.split()
# print("num1 is {}, num2 is {}, num3 is {}".format(num1, num2, num3))

'''
1. if-elif-else block
2. reduce repeating code as much as possible
3. 2 ways of printing strings using format()
- stating variables in order
  print("The largest between {}, {}, {} is {}".format(num1, num2, num3, largest))
- stating indexes of variables between curly braces
  print("The largest between {1}, {2}, {0} is {0}".format(num3, num1, num2))

  0, 1, 1, 2, 3, 5, 8, 13, 21, 34

  nterms = 10
  a = 0
  b = 1
  count = 2
  while count < nterms:
      code


0
1
1
2
3
5
8
13
21
34
'''
