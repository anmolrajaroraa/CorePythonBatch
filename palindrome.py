string = "Was it a car or a cat I saw?"
# string = ' \'Mr. Owl\' ate!@#$%^&*()_+{}": <>? my metal worm!!'
# for char in string:
#     print(char)
while not string.isalnum():
    print(f"string is '{string}'")
    for char in string:
        print(char)
        if not char.isalnum():
            string = string.replace(char, '')
            print("string updated...")
            print("going to restart for loop")
            break

string = string.lower()
print(f"Clean string - '{string}'")
n = len(string)
for i in range(0, (n // 2) + 1):
    if string[i] != string[n - i - 1]:
        print("string is not a palindrome!")
        break
else:
    print("string is a palindrome!!")

# if n % 2 == 0:
#     for i in range(0, n // 2)):
#         # print("->", string[i])
#         # print(i, n - i - 1)
#         if string[i] != string[n - i - 1]:
#             print("string is not a palindrome!")
#     else:
#         print("string is a palindrome!!")
# else:
#     for i in range(0, (n // 2) + 1):
#         # print("->", string[i])
#         # print(i, n) - i - 1)
#         if string[i] != string[n - i - 1]:
#             print("string is not a palindrome!")
#     else:
#         print("string is a palindrome!!")

    # 02022020
    # MrOwlatemymetalworm
    # madam
