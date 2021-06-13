'''Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> list1 = [12,23,34,45,56,67,78,89,90]
>>> len(list1)
9
>>> min(list1)
12
>>> max(list1)
90
>>> sum(list1)
494
>>> dict1 = {
	1: 100,
	2: 200}
>>> sum(dict1)
3
>>> dict1 = {
	1: 100,
	2: 200}
>>> dict1 = {
	"1": 100,
	"2": 200
	}
>>> sum(dict1)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    sum(dict1)
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> min(dict1)
'1'
>>> max(dict1)
'2'
>>> list1 = [12,23,34,45,56,67,78,89,90,11]
>>> sorted(list1)
[11, 12, 23, 34, 45, 56, 67, 78, 89, 90]
>>> dict1 = {
	"1": 100,
	"3": 300,
	"2": 200
	}
>>> sorted(dict1)
['1', '2', '3']
>>> 10 in list1  # in -> membership operator
False
>>> 11 in list1
True
>>> 1 in dict1
False
>>> "1" in dict1
True
>>> 1 not in dict1
True
>>> for index, element in list1:
	print(index)

	
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    for index, element in list1:
TypeError: cannot unpack non-iterable int object
>>> for index, element in enumerate(list1):
	print(index)

	
0
1
2
3
4
5
6
7
8
9
>>> for index, element in enumerate(list1):
	print(element)

	
12
23
34
45
56
67
78
89
90
11
>>> list1
[12, 23, 34, 45, 56, 67, 78, 89, 90, 11]
>>> names = ["Anmol", "Avanish", "Bharti", "Ram", "Shyam", "Sita", "Gita", "Aman", "Abhishek", "Himanshu"]
>>> for element in list1:
	for name in names:
		print(element, names)

		
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
12 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
23 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
34 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
45 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
56 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
67 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
78 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
89 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
90 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
11 ['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
>>> for element in list1:
	for name in names:
		print(element, name)

		
12 Anmol
12 Avanish
12 Bharti
12 Ram
12 Shyam
12 Sita
12 Gita
12 Aman
12 Abhishek
12 Himanshu
23 Anmol
23 Avanish
23 Bharti
23 Ram
23 Shyam
23 Sita
23 Gita
23 Aman
23 Abhishek
23 Himanshu
34 Anmol
34 Avanish
34 Bharti
34 Ram
34 Shyam
34 Sita
34 Gita
34 Aman
34 Abhishek
34 Himanshu
45 Anmol
45 Avanish
45 Bharti
45 Ram
45 Shyam
45 Sita
45 Gita
45 Aman
45 Abhishek
45 Himanshu
56 Anmol
56 Avanish
56 Bharti
56 Ram
56 Shyam
56 Sita
56 Gita
56 Aman
56 Abhishek
56 Himanshu
67 Anmol
67 Avanish
67 Bharti
67 Ram
67 Shyam
67 Sita
67 Gita
67 Aman
67 Abhishek
67 Himanshu
78 Anmol
78 Avanish
78 Bharti
78 Ram
78 Shyam
78 Sita
78 Gita
78 Aman
78 Abhishek
78 Himanshu
89 Anmol
89 Avanish
89 Bharti
89 Ram
89 Shyam
89 Sita
89 Gita
89 Aman
89 Abhishek
89 Himanshu
90 Anmol
90 Avanish
90 Bharti
90 Ram
90 Shyam
90 Sita
90 Gita
90 Aman
90 Abhishek
90 Himanshu
11 Anmol
11 Avanish
11 Bharti
11 Ram
11 Shyam
11 Sita
11 Gita
11 Aman
11 Abhishek
11 Himanshu
>>> for index, element in enumerate(list1):
	for index, name in enumerate(names):
		print(index, element, name)

		
0 12 Anmol
1 12 Avanish
2 12 Bharti
3 12 Ram
4 12 Shyam
5 12 Sita
6 12 Gita
7 12 Aman
8 12 Abhishek
9 12 Himanshu
0 23 Anmol
1 23 Avanish
2 23 Bharti
3 23 Ram
4 23 Shyam
5 23 Sita
6 23 Gita
7 23 Aman
8 23 Abhishek
9 23 Himanshu
0 34 Anmol
1 34 Avanish
2 34 Bharti
3 34 Ram
4 34 Shyam
5 34 Sita
6 34 Gita
7 34 Aman
8 34 Abhishek
9 34 Himanshu
0 45 Anmol
1 45 Avanish
2 45 Bharti
3 45 Ram
4 45 Shyam
5 45 Sita
6 45 Gita
7 45 Aman
8 45 Abhishek
9 45 Himanshu
0 56 Anmol
1 56 Avanish
2 56 Bharti
3 56 Ram
4 56 Shyam
5 56 Sita
6 56 Gita
7 56 Aman
8 56 Abhishek
9 56 Himanshu
0 67 Anmol
1 67 Avanish
2 67 Bharti
3 67 Ram
4 67 Shyam
5 67 Sita
6 67 Gita
7 67 Aman
8 67 Abhishek
9 67 Himanshu
0 78 Anmol
1 78 Avanish
2 78 Bharti
3 78 Ram
4 78 Shyam
5 78 Sita
6 78 Gita
7 78 Aman
8 78 Abhishek
9 78 Himanshu
0 89 Anmol
1 89 Avanish
2 89 Bharti
3 89 Ram
4 89 Shyam
5 89 Sita
6 89 Gita
7 89 Aman
8 89 Abhishek
9 89 Himanshu
0 90 Anmol
1 90 Avanish
2 90 Bharti
3 90 Ram
4 90 Shyam
5 90 Sita
6 90 Gita
7 90 Aman
8 90 Abhishek
9 90 Himanshu
0 11 Anmol
1 11 Avanish
2 11 Bharti
3 11 Ram
4 11 Shyam
5 11 Sita
6 11 Gita
7 11 Aman
8 11 Abhishek
9 11 Himanshu
>>> for i in range(len(list1)):
	print(list1[i],names[i])

	
12 Anmol
23 Avanish
34 Bharti
45 Ram
56 Shyam
67 Sita
78 Gita
89 Aman
90 Abhishek
11 Himanshu
>>> for index, element in enumerate(list1):
	print(element, names[index])

	
12 Anmol
23 Avanish
34 Bharti
45 Ram
56 Shyam
67 Sita
78 Gita
89 Aman
90 Abhishek
11 Himanshu
>>> for index, element in enumerate(list1, list2):
	print(element, names[index])

	
Traceback (most recent call last):
  File "<pyshell#46>", line 1, in <module>
    for index, element in enumerate(list1, list2):
NameError: name 'list2' is not defined
>>> for element in list1:
	print(element)

	
12
23
34
45
56
67
78
89
90
11
>>> for element in list1, list2:
	print(element)

	
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    for element in list1, list2:
NameError: name 'list2' is not defined
>>> for index, element in enumerate(list1, names):
	print(element, names[index])

	
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    for index, element in enumerate(list1, names):
TypeError: 'list' object cannot be interpreted as an integer
>>> for index, element in enumerate(list1, 5):
	print(element, names[index])

	
12 Sita
23 Gita
34 Aman
45 Abhishek
56 Himanshu
Traceback (most recent call last):
  File "<pyshell#55>", line 2, in <module>
    print(element, names[index])
IndexError: list index out of range
>>> names
['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
>>> for index, element in enumerate(list1, 5):
	print(list1[index], names[index])

	
67 Sita
78 Gita
89 Aman
90 Abhishek
11 Himanshu
Traceback (most recent call last):
  File "<pyshell#58>", line 2, in <module>
    print(list1[index], names[index])
IndexError: list index out of range
>>> for index, element in enumerate(list1):
	print(index, element)

	
0 12
1 23
2 34
3 45
4 56
5 67
6 78
7 89
8 90
9 11
>>> for index, element in enumerate(list1, 5):
	print(index, element)

	
5 12
6 23
7 34
8 45
9 56
10 67
11 78
12 89
13 90
14 11
>>> for element in zip(list1, names):
	print(element)

	
(12, 'Anmol')
(23, 'Avanish')
(34, 'Bharti')
(45, 'Ram')
(56, 'Shyam')
(67, 'Sita')
(78, 'Gita')
(89, 'Aman')
(90, 'Abhishek')
(11, 'Himanshu')
>>> for index, element in enumerate(zip(list1, list2)):
	print(index, element)

	
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    for index, element in enumerate(zip(list1, list2)):
NameError: name 'list2' is not defined
>>> for index, element in enumerate(zip(list1, names)):
	print(index, element)

	
0 (12, 'Anmol')
1 (23, 'Avanish')
2 (34, 'Bharti')
3 (45, 'Ram')
4 (56, 'Shyam')
5 (67, 'Sita')
6 (78, 'Gita')
7 (89, 'Aman')
8 (90, 'Abhishek')
9 (11, 'Himanshu')
>>> for index, element in enumerate(zip(list1, names), 101):
	print(index, element)

	
101 (12, 'Anmol')
102 (23, 'Avanish')
103 (34, 'Bharti')
104 (45, 'Ram')
105 (56, 'Shyam')
106 (67, 'Sita')
107 (78, 'Gita')
108 (89, 'Aman')
109 (90, 'Abhishek')
110 (11, 'Himanshu')
>>> for index, marks, name in enumerate(zip(list1, names), 101):
	print(index, marks, name)

	
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    for index, marks, name in enumerate(zip(list1, names), 101):
ValueError: not enough values to unpack (expected 3, got 2)
>>> for index, element in enumerate(zip(list1, names), 101):
	print(index, element[0], element[1])

	
101 12 Anmol
102 23 Avanish
103 34 Bharti
104 45 Ram
105 56 Shyam
106 67 Sita
107 78 Gita
108 89 Aman
109 90 Abhishek
110 11 Himanshu
>>> for index, element in enumerate(zip(list1, names), 101):
	print(f"{index}. {element[1]} -> {element[0]}")

	
101. Anmol -> 12
102. Avanish -> 23
103. Bharti -> 34
104. Ram -> 45
105. Shyam -> 56
106. Sita -> 67
107. Gita -> 78
108. Aman -> 89
109. Abhishek -> 90
110. Himanshu -> 11
>>> list1
[12, 23, 34, 45, 56, 67, 78, 89, 90, 11]
>>> names
['Anmol', 'Avanish', 'Bharti', 'Ram', 'Shyam', 'Sita', 'Gita', 'Aman', 'Abhishek', 'Himanshu']
>>> zip(list1,  names)
<zip object at 0x7ff5ae7a91c8>
>>> list(zip(list1,  names))
[(12, 'Anmol'), (23, 'Avanish'), (34, 'Bharti'), (45, 'Ram'), (56, 'Shyam'), (67, 'Sita'), (78, 'Gita'), (89, 'Aman'), (90, 'Abhishek'), (11, 'Himanshu')]
>>> 
>>> zip_list = [(12, 'Anmol'), (23, 'Avanish'), (34, 'Bharti'), (45, 'Ram'), (56, 'Shyam'), (67, 'Sita'), (78, 'Gita'), (89, 'Aman'), (90, 'Abhishek'), (11, 'Himanshu')]
>>> enumerate(zip_list)
<enumerate object at 0x7ff5ae789c60>
>>> list(enumerate(zip_list))
[(0, (12, 'Anmol')), (1, (23, 'Avanish')), (2, (34, 'Bharti')), (3, (45, 'Ram')), (4, (56, 'Shyam')), (5, (67, 'Sita')), (6, (78, 'Gita')), (7, (89, 'Aman')), (8, (90, 'Abhishek')), (9, (11, 'Himanshu'))]

>>> list(enumerate(zip_list), 101)
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    list(enumerate(zip_list), 101)
TypeError: list expected at most 1 arguments, got 2
>>> list(enumerate(zip_list, 101))
[(101, (12, 'Anmol')), (102, (23, 'Avanish')), (103, (34, 'Bharti')), (104, (45, 'Ram')), (105, (56, 'Shyam')), (106, (67, 'Sita')), (107, (78, 'Gita')), (108, (89, 'Aman')), (109, (90, 'Abhishek')), (110, (11, 'Himanshu'))]
>>> '''
'''
>>> all([1,2,3,4,5,'5','',None,False,0])
False
>>> all([1,2,3,4,5,'5','',None,True,0])
False
>>> all([1,2,3,4,5,'5','',None,True,-1])
False
>>> all([1,2,3,4,5,'5','',int,True,-1])
False
>>> all([1,2,3,4,5,'5','not an empty string',int,True,-1])
True
>>> all([''])
False
>>> all([None])
False
>>> all([0])
False
>>> all([False])
False
>>> any([1,2,3,4,5,'5','',None,True,-1])
True
>>> any(['',None,-1])
True
>>> any(['',None])
False
>>> reversed([1,2,3,4,5,'5','not an empty string',int,True,-1])
<list_reverseiterator object at 0x7f9e99f71ef0>
>>> list(reversed([1,2,3,4,5,'5','not an empty string',int,True,-1]))
[-1, True, <class 'int'>, 'not an empty string', '5', 5, 4, 3, 2, 1]
>>> 'hello'*5
'hellohellohellohellohello'
>>> [1,2,3,4,5,'5','not an empty string',int,True,-1]*5
[1, 2, 3, 4, 5, '5', 'not an empty string', <class 'int'>, True, -1, 1, 2, 3, 4, 5, '5', 'not an empty string', <class 'int'>, True, -1, 1, 2, 3, 4, 5, '5', 'not an empty string', <class 'int'>, True, -1, 1, 2, 3, 4, 5, '5', 'not an empty string', <class 'int'>, True, -1, 1, 2, 3, 4, 5, '5', 'not an empty string', <class 'int'>, True, -1]
>>> list1 = [1,2,3,4,5]
>>> list2 = [6,7,8,9,10]
>>> list1+list2
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list3 = [[1,2,3,4,5,'5','not an empty string',int,True,-1]]
>>> list3 = [1,2,3,4,5,'5','not an empty string',int,True,-1]
>>> list3.index('5')
5
>>> list3.count(1)
2
>>> def fct(x,y,z):
	"""documentation"""

	
>>> 
>>> 
>>> 
>>> def fct(x,y,z):
	"""documentation"""
	print("statement block")
	return x + y + z

>>> print(x)
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    print(x)
NameError: name 'x' is not defined
>>> fct(1,2,3)
statement block
6
>>> x
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> all.__doc__
'Return True if bool(x) is True for all values x in the iterable.\n\nIf the iterable is empty, return True.'
>>> fct.__doc__
'documentation'
>>> all([])
True
>>> any.__doc__
'Return True if bool(x) is True for any x in the iterable.\n\nIf the iterable is empty, return False.'
>>> import copy
>>> copy.deepcopy.__doc__
"Deep copy operation on arbitrary Python objects.\n\n    See the module's __doc__ string for more info.\n    "
>>> copy.__doc__
'Generic (shallow and deep) copying operations.\n\nInterface summary:\n\n        import copy\n\n        x = copy.copy(y)        # make a shallow copy of y\n        x = copy.deepcopy(y)    # make a deep copy of y\n\nFor module specific errors, copy.Error is raised.\n\nThe difference between shallow and deep copying is only relevant for\ncompound objects (objects that contain other objects, like lists or\nclass instances).\n\n- A shallow copy constructs a new compound object and then (to the\n  extent possible) inserts *the same objects* into it that the\n  original contains.\n\n- A deep copy constructs a new compound object and then, recursively,\n  inserts *copies* into it of the objects found in the original.\n\nTwo problems often exist with deep copy operations that don\'t exist\nwith shallow copy operations:\n\n a) recursive objects (compound objects that, directly or indirectly,\n    contain a reference to themselves) may cause a recursive loop\n\n b) because deep copy copies *everything* it may copy too much, e.g.\n    administrative data structures that should be shared even between\n    copies\n\nPython\'s deep copy operation avoids these problems by:\n\n a) keeping a table of objects already copied during the current\n    copying pass\n\n b) letting user-defined classes override the copying operation or the\n    set of components copied\n\nThis version does not copy types like module, class, function, method,\nnor stack trace, stack frame, nor file, socket, window, nor array, nor\nany similar types.\n\nClasses can use the same interfaces to control copying that they use\nto control pickling: they can define methods called __getinitargs__(),\n__getstate__() and __setstate__().  See the documentation for module\n"pickle" for information on these methods.\n'
>>> print(copy.__doc__)
Generic (shallow and deep) copying operations.

Interface summary:

        import copy

        x = copy.copy(y)        # make a shallow copy of y
        x = copy.deepcopy(y)    # make a deep copy of y

For module specific errors, copy.Error is raised.

The difference between shallow and deep copying is only relevant for
compound objects (objects that contain other objects, like lists or
class instances).

- A shallow copy constructs a new compound object and then (to the
  extent possible) inserts *the same objects* into it that the
  original contains.

- A deep copy constructs a new compound object and then, recursively,
  inserts *copies* into it of the objects found in the original.

Two problems often exist with deep copy operations that don't exist
with shallow copy operations:

 a) recursive objects (compound objects that, directly or indirectly,
    contain a reference to themselves) may cause a recursive loop

 b) because deep copy copies *everything* it may copy too much, e.g.
    administrative data structures that should be shared even between
    copies

Python's deep copy operation avoids these problems by:

 a) keeping a table of objects already copied during the current
    copying pass

 b) letting user-defined classes override the copying operation or the
    set of components copied

This version does not copy types like module, class, function, method,
nor stack trace, stack frame, nor file, socket, window, nor array, nor
any similar types.

Classes can use the same interfaces to control copying that they use
to control pickling: they can define methods called __getinitargs__(),
__getstate__() and __setstate__().  See the documentation for module
"pickle" for information on these methods.

>>> def fct(x,y,z,*args):
	pass

>>> def fct(x,y,z,*args,a=3,b=3):
	pass

>>> def fct(x,y,z,*args,a=3,b=3,**kwargs):
	pass

>>> fct()
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    fct()
TypeError: fct() missing 3 required positional arguments: 'x', 'y', and 'z'
>>> fct(x,y,z)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    fct(x,y,z)
NameError: name 'x' is not defined
>>> fct(1,2,3)
>>> def fct(x,y,z,*args,a=3,b=3,**kwargs):
	print(x,y,z)
	print(args)
	print(a,b)
	print(kwargs)

	
>>> fct(1,2,3)
1 2 3
()
3 3
{}
>>> fct(1,2,3,4,5,6)
1 2 3
(4, 5, 6)
3 3
{}
>>> fct(1,2,3,4,5,6,a=4,b=5)
1 2 3
(4, 5, 6)
4 5
{}
>>> fct(1,2,3,4,5,6,a=4,b=5,m="one",n="two")
1 2 3
(4, 5, 6)
4 5
{'m': 'one', 'n': 'two'}'''
