# a number is even if division by 2 gives remainder of 0.
# If remainder is 1, it is odd number.

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("{} is even".format(num))
else:
    print("{} is odd".format(num))

'''2021 - 5.5
2022 - 5.5
2023 - 5.5
2024 - 5.5 = 22 hours -> 366 -> 24 hours added

2000 -> divisible by 4 -> leap year
-> divisible by 100 -> no leap year
-> divisible by 400 -> leap year

1900 ->
2100 ->
2050 ->
2024 ->
2400
'''
