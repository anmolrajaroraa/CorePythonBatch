'''Python 3.7.3 (v3.7.3: ef4ec6ed12, Mar 25 2019, 16: 52: 21)
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>> > student = {
    "id": 101,
    "name": "Ram",
    "subject_1": "English",
    "subject_2": "Physics",
    "subject_3": "Chemistry",
    "subject_4": "Geography",
    "subject_5": "Sanskrit",
    "subject_1_marks": 99,
    "subject_2_marks": 98,
    "subject_3_marks": 97,
    "subject_4_marks": 96,
    "subject_5_makrs": 95
}
>> > student
{'id': 101, 'name': 'Ram', 'subject_1': 'English', 'subject_2': 'Physics', 'subject_3': 'Chemistry', 'subject_4': 'Geography',
    'subject_5': 'Sanskrit', 'subject_1_marks': 99, 'subject_2_marks': 98, 'subject_3_marks': 97, 'subject_4_marks': 96, 'subject_5_makrs': 95}
>> > student = {
    "id": 101,
    "name": "Ram",
    "subjects": ["English", "Physics", "Chemistry", "Geography", "Sanskrit"],
    "marks": [99, 98, 97, 96, 95]
}
>> > student["name"]
'Ram'
>> > student["subjects"]
['English', 'Physics', 'Chemistry', 'Geography', 'Sanskrit']
>> > student["marks"]
[99, 98, 97, 96, 95]
>> > student["subjects"][0]
'English'
>> > student["marks"][0]
99
>> > student = {
    "id": 101,
    "name": "Ram",
    "marks": {
            "English": 99,
            "Physics": 98,
        "Chemistry": 97,
        "Geography": 96,
        "Sanskrit": 95
    }
}
>> > student
{'id': 101, 'name': 'Ram', 'marks': {'English': 99, 'Physics': 98,
                                     'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95}}
>> > student["marks"]
{'English': 99, 'Physics': 98, 'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95}
>> > student["marks"]["English"]
99
>> > student["marks"]
{'English': 99, 'Physics': 98, 'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95}
>> > student["marks"].values()
dict_values([99, 98, 97, 96, 95])
>> > student["marks"].keys()
dict_keys(['English', 'Physics', 'Chemistry', 'Geography', 'Sanskrit'])
>> > help(dict)
|  Methods defined here:
    |
    |  clear(...)
    |      D.clear() -> None.  Remove all items from D.
    |
    |  copy(...)
    |      D.copy() -> a shallow copy of D
    |
    |  get(self, key, default=None, /)
    |      Return the value for key if key is in the dictionary, else default.
    |
    |  items(...)
    |      D.items() -> a set-like object providing a view on D's items
    |
    |  keys(...)
    |      D.keys() -> a set-like object providing a view on D's keys
    |
    |  pop(...)
    |      D.pop(k[, d]) -> v, remove specified key and return the corresponding value.
    |      If key is not found, d is returned if given, otherwise KeyError is raised
    |
    |  popitem(...)
    |      D.popitem() -> (k, v), remove and return some(key, value) pair as a
    |      2-tuple
    but raise KeyError if D is empty.
    |
    |  setdefault(self, key, default=None, /)
    |      Insert key with a value of default if key is not in the dictionary.
    |
    |      Return the value for key if key is in the dictionary, else default.
    |
    |  update(...)
    |      D.update([E, ]**F) -> None.  Update D from dict/iterable E and F.
    |      If E is present and has a .keys() method, then does: for k in E: D[k] = E[k]
    |      If E is present and lacks a .keys() method, then does: for k, v in E: D[k] = v
    |      In either case, this is followed by: for k in F:  D[k] = F[k]
    |
    |  values(...)
    |      D.values() -> an object providing a view on D's values
    |
    | ----------------------------------------------------------------------
    |  Class methods defined here:
    |
    |  fromkeys(iterable, value=None, /) from builtins.type
    |      Create a new dictionary with keys from iterable and values set to value.
    |
    |

>> > student["marks"].keys()
dict_keys(['English', 'Physics', 'Chemistry', 'Geography', 'Sanskrit'])
>> > student["marks"].values()
dict_values([99, 98, 97, 96, 95])
>> > student["marks"].items()
dict_items([('English', 99), ('Physics', 98), ('Chemistry', 97),
            ('Geography', 96), ('Sanskrit', 95)])
>> > student.pop('id')
101
>> > student
{'name': 'Ram', 'marks': {'English': 99, 'Physics': 98,
                          'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95}}
>> > student.popitem()
('marks', {'English': 99, 'Physics': 98,
           'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95})
>> > student
{'name': 'Ram'}
>> > student["id"] = 101
>> > student
{'name': 'Ram', 'id': 101}
>> > student["id"] = 102
>> > student
{'name': 'Ram', 'id': 102}
>> > student.setdefault("id", 103)
102
>> > student
{'name': 'Ram', 'id': 102}
>> > student.pop('id')
102
>> > student.setdefault("id", 103)
103
>> > student
{'name': 'Ram', 'id': 103}
>> > student2 = {
    "id": 105,
    "name": "Shyam",
    "percentage": 99.9
}
>> > student.update(student2)
>> > student
{'name': 'Shyam', 'id': 105, 'percentage': 99.9}
>> >
>>> student = {}
>>> student
{}
>>> student['id'] = 102
>>> student['name'] = "Shyam"
>>> student['marks'] = {}
>>> studnet['marks']['English'] = 99
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    studnet['marks']['English'] = 99
NameError: name 'studnet' is not defined
>>> student['marks']['English'] = 99
>>> student
{'id': 102, 'name': 'Shyam', 'marks': {'English': 99}}
>>> student = {
    "id": 101,
    "name": "Ram",
    "marks": {
            "English": 99,
            "Physics": 98,
	"Chemistry": 97,
	"Geography": 96,
	"Sanskrit": 95
    }
}
>>> student
{'id': 101, 'name': 'Ram', 'marks': {'English': 99, 'Physics': 98, 'Chemistry': 97, 'Geography': 96, 'Sanskrit': 95}}
>>> student.keys()
dict_keys(['id', 'name', 'marks'])
>>> student_keys = student.keys()
>>> student_keys
dict_keys(['id', 'name', 'marks'])
>>> dict.fromkeys(student_keys)
{'id': None, 'name': None, 'marks': None}
>>> student2 = dict.fromkeys(student_keys)
>>> student2
{'id': None, 'name': None, 'marks': None}
>>> student2['marks'] = dict.fromkeys(["English","Physics","Chemistry","Geography","Sanskrit"])
>>> student2
{'id': None, 'name': None, 'marks': {'English': None, 'Physics': None, 'Chemistry': None, 'Geography': None, 'Sanskrit': None}}
>>> student2['marks']['English']
>>> student['marks']['Computer Science']
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    student['marks']['Computer Science']
KeyError: 'Computer Science'
>>> student2['marks'] = dict.fromkeys(["English","Physics","Chemistry","Geography","Sanskrit","Computer Science"])
>>> student['marks']['Computer Science']
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    student['marks']['Computer Science']
KeyError: 'Computer Science'
>>> student2['marks']['Computer Science']
>>> def add():
    print(x + y)

    
>>> def sub():
    print(x - y)

    
>>> def mul():
    print(x * y)

    
>>> def div():
    print(x / y)

    
>>> choices = {
    1: add(),
    2: sub(),
    3: mul(),
    4: div()
}
Traceback (most recent call last):
  File "<pyshell#32>", line 2, in <module>
    1: add(),
  File "<pyshell#25>", line 2, in add
    print(x + y)
NameError: name 'x' is not defined
>>> x = 10
>>> y = 20
>>> choices = {
    1: add(),
    2: sub(),
    3: mul(),
    4: div()
}
30
-10
200
0.5
>>> choices
{1: None, 2: None, 3: None, 4: None}
>>> choices = {
    1: add,
    2: sub,
    3: mul,
    4: div
}
>>> choices
{1: <function add at 0x7ff8ea7c22f0>, 2: <function sub at 0x7ff8ea7c2378>, 3: <function mul at 0x7ff8ea7c2400>, 4: <function div at 0x7ff8ea7c2488>}
>>> choices[1]
<function add at 0x7ff8ea7c22f0>
>>> choices[2]
<function sub at 0x7ff8ea7c2378>
>>> choices[2]()
-10
>>> student = {
    "id": 101,
    "name": "Ram",
    "marks": {
            "English": 99,
            "Physics": 98,
	"Chemistry": 97,
	"Geography": 96,
	"Sanskrit": 95
    },
    "default": "Key not found"
}
>>> student.get("xyz", "default")
'default'
>>> student.get("xyz", "key not found")
'key not found'
>>> student.get("name", "key not found")
'Ram'
'''

x = 10
y = 20


def add():
    print(x + y)


def sub():
    print(x - y)


def mul():
    print(x * y)


def div():
    print(x / y)


def errorHandler():
    print("Invalid operation")


print('''
1. Add
2. Sub
3. Mul
4. Div
5. Mod
''')
choices = {
    1: add,
    2: sub,
    3: mul,
    4: div
}
user_choice = int(input("Your choice: "))
# choices[user_choice]()
choices.get(user_choice, errorHandler)()
# if choice == 1:
#     add()
# elif choice == 2:
#     sub()
# elif choice == 3:
#     mul()
# elif choice == 4:
#     div()
# else:
#     print("Invalid choice")
