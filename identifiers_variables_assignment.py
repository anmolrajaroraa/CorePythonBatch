'''Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> "aaA_0".isidentifier()
True
>>> "aaA_0$".isidentifier()
False
>>> "AaA_0$".isidentifier()
False
>>> "AaA_0".isidentifier()
True
>>> "_aA_0".isidentifier()
True
>>> "9_aA_0".isidentifier()
False
>>> "9_sßåç®´œA_0".isidentifier()
False
>>> "9_åA_0".isidentifier()
False
>>> 
>>> "False".isidentifier()
True
>>> False = 10
SyntaxError: can't assign to keyword
>>> set = 10
>>> type(set)
<class 'int'>
>>> bigOne
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    bigOne
NameError: name 'bigOne' is not defined
>>> BigOne
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    BigOne
NameError: name 'BigOne' is not defined
>>> bIgoNe
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    bIgoNe
NameError: name 'bIgoNe' is not defined
>>> a = 10+1,20+2,30+3
>>> a
(11, 22, 33)
>>> a,b,c = 10+1,20+2,30+3
>>> a
11
>>> b
22
>>> c
33
>>> a,b = 10+1,20+2,30+3
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    a,b = 10+1,20+2,30+3
ValueError: too many values to unpack (expected 2)
>>> x=1.2+8+sin(0)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    x=1.2+8+sin(0)
NameError: name 'sin' is not defined
>>> import math
>>> math.sin(0)
0.0
>>> x=1.2+8+sin(0)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x=1.2+8+sin(0)
NameError: name 'sin' is not defined
>>> x=1.2+8+math.sin(0)
>>> x
9.2
>>> from math import sin
>>> x=1.2+8+sin(0)
>>> x
9.2
>>> a=b=c=0
>>> a
0
>>> b
0
>>> c
0
>>> y,z,r=9.2,-7.6,0
>>> y
9.2
>>> z
-7.6
>>> r
0
>>> a,b = b,a
>>> a=9
>>> b=8
>>> a,b = b,a
>>> a
8
>>> b
9
>>> 10+1,20+2,30+3
(11, 22, 33)
>>> a,b,c = 10+1,20+2,30+3
>>> a,*b = 10+1,20+2,30+3 # *b -> multiple/dynamic args
>>> a
11
>>> b
[22, 33]
>>> *a,b = 10+1,20+2,30+3
>>> a
[11, 22]
a
>>> b
33
>>> *a,b = 10+1,20+2,30+3,40+4,50+5
>>> a
[11, 22, 33, 44]
>>> b
55
>>> *a,b,c = 10+1,20+2,30+3,40+4,50+5
>>> b
44
>>> c
55
>>> a
[11, 22, 33]
>>> a,*b,c = 10+1,20+2,30+3,40+4,50+5
>>> a
11
>>> c
55
>>> b
[22, 33, 44]
>>> # unpacking of sequence(tuple) in item and list
>>> a++
SyntaxError: invalid syntax
>>> a+=1
>>> a
12
>>> a = a+1
>>> a-=2
>>> a
11
>>> a = a-2
>>> a
9
>>> a**=5
>>> a
59049
>>> a//=5
>>> a
11809
>>> a
11809
>>> x
9.2
>>> xx
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    xx
NameError: name 'xx' is not defined
>>> xx = None
>>> xx
>>> del xx
>>> xx
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    xx
NameError: name 'xx' is not defined
>>> del x
>>> x
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    x
NameError: name 'x' is not defined
>> >
'''
