s = 0
i = 1

while i <= 100:
    s += i ** 2
    i += 1

print("Sum:", s)

s = "Some text"
cnt = 0

for c in s:
    if c == 'e':
        cnt += 1

print("found", cnt, "'e'")

list1 = [11, 18, 9, 12, 23, 4, 17]
lost = []

for index in range(len(list1)):
    value = list1[index]
    if value > 15:
        lost.append(value)
        list1[index] = 15

print(f"modified:{list1}, lost:{lost}")

for index, value in enumerate(list1):
    print(index, value)

# range([start,]end[,step])
# range(5) -> 01234
# range(3, 8) -> 34567
print(type(range(2, 12, 3)))
print(range(2, 12, 3))
print(list(range(2, 12, 3)))
