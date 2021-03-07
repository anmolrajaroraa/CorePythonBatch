
n = 1
k = 2
j = 3
m = 0
p = 0
num = 0

if n < 0 or k <= 0 or j <= 0 or m < 0 or p < 0:
    print("INVALID INPUT")
else:
    num += m // k
    num += p // j
    if m % k > 0 or p % j > 0:
        num += 1
    leftOverMonkeys = n - num
    while leftOverMonkeys < 0:
        leftOverMonkeys += n
    print(f"Number of Monkeys left on the Tree:{n}")
