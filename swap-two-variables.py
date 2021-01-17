# Python program to swap two variables

# To take input from the user

# dynamic typing
x = int(input("Enter value of x: "))
y = int(input("Enter value of y: "))
# print(x, y, x, y, x, y, x, y, sep="<-->")
# print("X is " + x + " y is " + y)
print("Before swapping: ")
print("X is ", x, " y is ", y)
# temp = x
# x = y
# y = temp
# print(x, y)

x, y = y, x
print("After swapping: ")
print("X is ", x, " y is ", y)

# 1. Input always takes input from user as string
# 2. int() can be used for type casting
# 3. you don't need to initialise variables with a concrete type
# 4. java's print sytnax can be used in python as it is but it requires type casting everything to string on our part, but the better way out is we can use comma (,) instead of concatenating. comma concatenates as well as type casts variables to strings automatically if required.
# 5. comments are done using #
# 6. shortcut for swapping values -> a,b = b,a
# a,b,c = c,a,b

Homework
Kilometres to miles
k * 0.621 -> miles
Celsius to fahrenheit
(c * 1.8) + 32 -> f
