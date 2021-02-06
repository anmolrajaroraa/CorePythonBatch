lower = 900
upper = 1000
print(f"Prime numbers between {lower} and {upper} are:")

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num // 2 + 1):
            if num % i == 0:
                print(f"{i} x {num//i} = {num}")
                break
        else:
            print(num)
