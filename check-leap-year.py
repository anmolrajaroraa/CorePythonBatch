year = 2400
if (year % 4) == 0:
    if (year % 100) == 0:
        if (year % 400) == 0:
            print("{} is a leap year".format(year))
        else:
            print("{} is not a leap year".format(year))
    else:
        print("{} is a leap year".format(year))
else:
    print("{} is not a leap year".format(year))


# year = 2400
# if (year % 4) == 0:
#     # print("{} is a leap year".format(year))
#     if ((year % 100) == 0) and ((year % 400) != 0):
#         print("{} is not a leap year".format(year))
#     else:
#          print("{} is a leap year".format(year))
# else:
#     print("{} is not a leap year".format(year))

# 2100 -> 4 true
# -> 100 true
# -> 400 false

'''
1. if else - multiple blocks
2. and , or operators 
3. maintain readability as much as possible
'''
