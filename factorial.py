num = 0
factorial = 1

if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
else:
    for i in range(1, num + 1):
        # factorial = factorial * i
        factorial *= i
    print(f"The factorial of {num} is {factorial}")
