>> > students = [["Avanish", 90], ["Bharti", 89], ["Anmol", 85]]
>> > students.sort()
>> > students
[['Anmol', 85], ['Avanish', 90], ['Bharti', 89]]
>> > students = [[90, "Avanish"], [89, "Bharti"], [85, "Anmol"]]
>> > students.sort()
>> > students
[[85, 'Anmol'], [89, 'Bharti'], [90, 'Avanish']]
>> > students.sort(key=x: x[1])
SyntaxError: invalid syntax
>> > students.sort(key="x:x[1]")
Traceback(most recent call last):
    File "<pyshell#24>", line 1, in < module >
    students.sort(key="x:x[1]")
TypeError: 'str' object is not callable
>> > students.sort(key=lambda x: x[1])
>> > students
[[85, 'Anmol'], [90, 'Avanish'], [89, 'Bharti']]
>> >
>> >
>> >
>> > students.sort(key=lambda student: student[1])
>> > students
[[85, 'Anmol'], [90, 'Avanish'], [89, 'Bharti']]
>> > students.sort(key=lambda student: student[0])
>> > students
[[85, 'Anmol'], [89, 'Bharti'], [90, 'Avanish']]
>> > students = [[90, "Avanish", "E"], [89, "Bharti", "C"], [85, "Anmol", "A"], [80, "Ram", "B"]]
>> > students.sort()
>> > students
[[80, 'Ram', 'B'], [85, 'Anmol', 'A'], [89, 'Bharti', 'C'], [90, 'Avanish', 'E']]
>> > students.sort(key=lambda student: student[1])
>> > students
[[85, 'Anmol', 'A'], [90, 'Avanish', 'E'], [89, 'Bharti', 'C'], [80, 'Ram', 'B']]
>> > students.sort(key=lambda student: student[2])
>> > students
[[85, 'Anmol', 'A'], [80, 'Ram', 'B'], [89, 'Bharti', 'C'], [90, 'Avanish', 'E']]
