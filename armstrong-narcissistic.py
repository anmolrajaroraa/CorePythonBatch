digitCount = len((num:= input("Enter a number to check: ")))
temp = (num: = int(num))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** digitCount
    temp //= 10

print(num, "is an Armstrong no") if num == sum else print(
    num, "is not an Armstrong no")

# num == sum ? true: false  // C
# true if condition else false  // python
