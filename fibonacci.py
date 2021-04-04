nterms = int(input("How many terms: "))
firstTerm = 0
secondTerm = 1
count = 2

# walrus operator
# if (nterms := int(input("How many terms: "))) <= 0:
if nterms <= 0:
    print("Please enter a positive integer")
elif nterms == 1:
    print("Fibonacci sequence upto 1 term:", firstTerm)
else:
    print(f"Fibonacci sequence upto {nterms} terms:")
    print(f"{firstTerm}, {secondTerm}", end='')
    while count < nterms:
        nextTerm = firstTerm + secondTerm
        # print(nextTerm, end=', ')
        print(f", {nextTerm}", end='')
        firstTerm, secondTerm = secondTerm, nextTerm
        count += 1
print()
