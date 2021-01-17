kilometres = float(input("Enter value in kilometres: "))
conv_fac = 0.621

# miles = float(kilometres) * conv_fac
miles = kilometres * conv_fac
print("line 25", type(kilometres))
# print("%s kilometres is equal to %d miles" % (kilometres, miles))
print("%0.1f kilometres is equal to %0.3f miles" % (kilometres, miles))
# print(kilometres, ' kms is equal to ', miles, " miles")

# if condition:
#     statement1
#     statement2
#     statement3
# statement4


if False:
    print("statement1")
    print("statement2")
    print("statement3")
    print("statement4")

'''
if kilometres.find('.') > -1:
    miles = float(kilometres) * conv_fac
else:
    miles = int(kilometres) * conv_fac
'''


"""
everything in python is treated as object

int i = 5  // primitive
String s = "Ram"  // reference

>>> input("Enter something: ")
Enter something: 5
'5'
>>> '5' * 0.6
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can't multiply sequence by non-int of type 'float'
>>> '5' * 6
'555555'
>>> # string replication
... 
>>> "ram" * 108
'ramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramramram'
>>> kilometres = '5'
>>> int(kilometres) * 0.621
3.105
"""

'''
1. float type casting
options - convert at the time of input - if you don't require the input to be used as string later on
convert later on to float or int as required while performing calculations

2. import random
3. if else condition + maintaining indentation
4. string functions usage + help terminal of python
5. string replication
6. print syntax borrowed from c++ + how to control printing of float numbers using %f
'''
