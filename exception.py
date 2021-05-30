# print(10/0)
# open("abc.py")
# pin = "1234"
# userPin = input("Enter your PIN: ")
# if userPin == pin[::-1]:
#     raise ValueError("Reverse PIN detected..account blocked")


def calc(a, b, operator):
    print(eval(a + operator + b))


while True:
    choices = {
        1: '+',
        2: '-',
        3: '*',
        4: '/'
    }
    choice = int(input("Enter your choice: "))
    fnum = input("Enter first number: ")
    snum = input("Enter second number: ")
    try:
        calc(fnum, snum, choices[choice])
    except ZeroDivisionError as err:
        # print("Please enter a valid number for divisor")
        print("Error:", err)
    except KeyError:
        print("Invalid choice.")
    except Exception:
        print("Something went wrong..")
