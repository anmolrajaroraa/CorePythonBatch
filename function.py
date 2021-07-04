'''Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> x = 10
>>> id(x)
4540095952
>>> def print_student_details(enrl_no, name, course):
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> print_student_details(101, "Ram", "MBBS")
Enrl no is 101
Name is Ram
Course is MBBS
>>> print_student_details(101, "Ram")
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print_student_details(101, "Ram")
TypeError: print_student_details() missing 1 required positional argument: 'course'
>>> print_student_details("Ram", "MBBS", 101)
Enrl no is Ram
Name is MBBS
Course is 101
>>> print_student_details(name="Ram", course="MBBS", enrl_no=101)
Enrl no is 101
Name is Ram
Course is MBBS
>>> print_student_details(enrl_no=101, "Ram", "MBBS")
SyntaxError: positional argument follows keyword argument
>>> print_student_details(101, name="Ram", course="MBBS")
Enrl no is 101
Name is Ram
Course is MBBS
>>> print_student_details(101, course="MBBS", name="Ram")
Enrl no is 101
Name is Ram
Course is MBBS
>>> print_student_details(course="MBBS", name="Ram", 101)
SyntaxError: positional argument follows keyword argument
>>> def print_student_details(enrl_no, name, course):
	'''Prints important details of a student based on enrl_no'''
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> print_student_details.__doc__
'Prints important details of a student based on enrl_no'
>>> print.__doc__
"print(value, ..., sep=' ', end='\\n', file=sys.stdout, flush=False)\n\nPrints the values to a stream, or to sys.stdout by default.\nOptional keyword arguments:\nfile:  a file-like object (stream); defaults to the current sys.stdout.\nsep:   string inserted between values, default a space.\nend:   string appended after the last value, default a newline.\nflush: whether to forcibly flush the stream."
>>> print(print.__doc__)
print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)

Prints the values to a stream, or to sys.stdout by default.
Optional keyword arguments:
file:  a file-like object (stream); defaults to the current sys.stdout.
sep:   string inserted between values, default a space.
end:   string appended after the last value, default a newline.
flush: whether to forcibly flush the stream.
>>> def print_student_details(enrl_no, name, course):
	'''Prints important details of a student based on enrl_no'''
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	return None

>>> result = print_student_details(101, name="Ram", course="MBBS")
Enrl no is 101
Name is Ram
Course is MBBS
>>> result
>>> print(result)
None
>>> def print_student_details(enrl_no, name, course):
	'''Prints important details of a student based on enrl_no'''
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> result = print_student_details(101, name="Ram", course="MBBS")
Enrl no is 101
Name is Ram
Course is MBBS
>>> print(result)
None
>>> def print_student_details(enrl_no, name, course):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> result = print_student_details(1, name="Ram", course="MBBS")
>>> print(result)
Student not found
>>> result = print_student_details(111, name="Ram", course="MBBS")
Enrl no is 111
Name is Ram
Course is MBBS
>>> print(result)
None
>>> print("Enrl no is", enrl_no)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    print("Enrl no is", enrl_no)
NameError: name 'enrl_no' is not defined
>>> def print_student_details(enrl_no, name, course, *args):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> def print_student_details(enrl_no, name, course):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)

	
>>> result = print_student_details(111, name="Ram", course="MBBS", "01/01/2001")
SyntaxError: positional argument follows keyword argument
>>> result = print_student_details(111, "Ram", "MBBS", "01/01/2001")
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    result = print_student_details(111, "Ram", "MBBS", "01/01/2001")
TypeError: print_student_details() takes 3 positional arguments but 4 were given
>>> def print_student_details(enrl_no, name, course, *extra_info):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	print("Some more info:", extra_info)

	
>>> result = print_student_details(111, "Ram", "MBBS", "01/01/2001")
Enrl no is 111
Name is Ram
Course is MBBS
Some more info: ('01/01/2001',)
>>> result = print_student_details(111, "Ram", "MBBS", "01/01/2001", 20, 33, 40)
Enrl no is 111
Name is Ram
Course is MBBS
Some more info: ('01/01/2001', 20, 33, 40)
>>> def print_student_details(enrl_no, name, course, **extra_info):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	print("Some more info:", extra_info)

	
>>> Some more info: ('01/01/2001', 20, 33, 40)
SyntaxError: invalid syntax
>>> result = print_student_details(111, "Ram", "MBBS", "01/01/2001", 20, 33, 40)
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    result = print_student_details(111, "Ram", "MBBS", "01/01/2001", 20, 33, 40)
TypeError: print_student_details() takes 3 positional arguments but 7 were given
>>> result = print_student_details(111, name="Ram", course="MBBS")
Enrl no is 111
Name is Ram
Course is MBBS
Some more info: {}
>>> result = print_student_details(111, name="Ram", course="MBBS", dob="01/01/2001")
Enrl no is 111
Name is Ram
Course is MBBS
Some more info: {'dob': '01/01/2001'}
>>> result = print_student_details(111, name="Ram", course="MBBS", dob="01/01/2001", age=20, marks=33, attendance=40)
Enrl no is 111
Name is Ram
Course is MBBS
Some more info: {'dob': '01/01/2001', 'age': 20, 'marks': 33, 'attendance': 40}
>>> def print_student_details(enrl_no, name, course, **extra_info):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	print("Some more info:")
	for k,v in extra_info.items():
		print(f"{k} is {v}")

		
>>> result = print_student_details(111, name="Ram", course="MBBS", dob="01/01/2001", age=20, marks=33, attendance=40)
Enrl no is 111
Name is Ram
Course is MBBS
Some more info:
dob is 01/01/2001
age is 20
marks is 33
attendance is 40
>>> def print_student_details(enrl_no, name, course, **extra_info):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	print("Some more info:")
	for k,v in extra_info.items():
		print(f"\t{k} is {v}")

		
>>> result = print_student_details(111, name="Ram", course="MBBS", dob="01/01/2001", age=20, marks=33, attendance=40)
Enrl no is 111
Name is Ram
Course is MBBS
Some more info:
	dob is 01/01/2001
	age is 20
	marks is 33
	attendance is 40
>>> def print_student_details(enrl_no, name, course="N/A", **extra_info):
	'''Prints important details of a student based on enrl_no'''
	if enrl_no <= 100:
		return "Student not found"
	print("Enrl no is", enrl_no)
	print("Name is", name)
	print("Course is", course)
	print("Some more info:")
	for k,v in extra_info.items():
		print(f"\t{k} is {v}")

		
>>> result = print_student_details(111, name="Ram", dob="01/01/2001", age=20, marks=33, attendance=40)
Enrl no is 111
Name is Ram
Course is N/A
Some more info:
	dob is 01/01/2001
	age is 20
	marks is 33
	attendance is 40
>>> result = print_student_details()
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    result = print_student_details()
TypeError: print_student_details() missing 2 required positional arguments: 'enrl_no' and 'name'
>>> '''
