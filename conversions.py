# from dictionary import add
# import factorial
# print(factorial.factorial)
# from factorial import factorial
# print(factorial)
import "./factorial/factorial.py"

'''Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> # type(expression)
>>> int("15")
15
>>> int("3f")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    int("3f")
ValueError: invalid literal for int() with base 10: '3f'
>>> hexNum = 0x3f
>>> type(hexNum)
<class 'int'>
>>> int("3f", 10)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    int("3f", 10)
ValueError: invalid literal for int() with base 10: '3f'
>>> int("3f", 16)
63
>>> # base of integer number can be specified in 2nd parameter
>>> int(15.56)
15
>>> # truncate decimal part
>>> 22/7
3.142857142857143
>>> int(22/7)
3
>>> round(22/7)
3
>>> round(100.29)
100
>>> round(100.89)
101
>>> int(100.29)
100
>>> int(100.89)
100
>>> round(22/7, 1)
3.1
>>> round(22/7, 2)
3.14
>>> # rounding off to 2 decimal places
>>> bool(None)
False
>>> 1 == 2
False
>>> bool()
False
>>> x = None
>>> bool(x)
False
>>> bool(False)
False
>>> bool(0)
False
>>> bool(0.0)
False
>>> bool(4)
True
>>> bool(4.8)
True
>>> bool("chgcc")
True
>>> bool("")
False
>>> y = ""
>>> bool(y)
False
>>> type(y)
<class 'str'>
>>> str(0)
'0'
>>> str(0.0)
'0.0'
>>> str("uygjacb")
'uygjacb'
>>> str(True)
'True'
>>> str(0x15)
'21'
>>> str(0b11)
'3'
>>> str(0o15)
'13'
>>> chr()  # ascii code -> char
Traceback (most recent call last):
  File "<pyshell#42>", line 1, in <module>
    chr()  # ascii code -> char
TypeError: chr() takes exactly one argument (0 given)
>>> chr(64)
'@'
>>> chr(164)  # unicode code -> char
'¤'
>>> chr(1640)  # unicode code -> char
'٨'
>>> chr(16400)  # unicode code -> char
'䀐'
>>> # char -> unicode
>>> ord('@')  # ordinal
64
>>> ord('#')  # ordinal
35
>>> ord('$')  # ordinal
36
>>> ord('^')  # ordinal
94
>>> ord('₹')
8377
>>> 2.0/11.0
0.18181818181818182
>>> str(2.0/11.0)
'0.18181818181818182'
>>> print(2.0/11.0)
0.18181818181818182
>>> print(str(2.0/11.0))
0.18181818181818182
>>> print(repr(2.0/11.0))
0.18181818181818182
>>> print(str("hello, world"))
hello, world
>>> print(repr("hello, world"))
'hello, world'
>>> import datetime
>>> type(datetime)
<class 'module'>
>>> type(datetime.datetime)
<class 'type'>
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2021, 5, 2, 18, 53, 43, 280096)
>>> from datetime import datetime as dt
>>> dt.now()
datetime.datetime(2021, 5, 2, 18, 54, 48, 762452)
>>> print(str(datetime.now()))
2021-05-02 18:55:08.369797
>>> print(repr(datetime.now()))
datetime.datetime(2021, 5, 2, 18, 55, 14, 535759)
>>> import os
>>> os.listdir()
['Demo', 'Aws-ppt-8.key', 'Accounting', 'genetic.py', 'Video Streaming.docx', '07-Functions.py', 'FullStack.key', 'Financial Analyst.xlsx', 'Aws-ppt-9.key', 'abc', 'Windows not Detecting Changes.rtfd', 'nested functions.py', 'core-python-march', 'string-basics.py', 'fn-basics.py', 'testFolder', 'Untitled1.ipynb', 'IOT copy.pptx', '06-Functions.py', 'Cloud Computing with AWS.docx', 'AWS-steps.rtf', '01-Functions.py', 'Unix Commands.docx', 'index.html', '.DS_Store', 'python.key', 'Docker.key', 'xyz.py', 'Networking.pptx', '~$b Crawling.docx', 'Print Statement with Python3.docx', 'python-intro.py', 'boto3_signed_url.py', 'python', '.localized', 'Profile_AnmolArora.docx', 'Switch Case Python.key', 'pydemo.py', 'DataScience.docx', 'Web Crawling.docx', 'Untitled.ipynb', 'Docker-ppt.key', 'python-demo.py', 'Multi-container deployments to AWS.xml', 'acro_test.side', 'Cloud Computing.pptx', 'python-reg-sept', 'Book1.xlsx', 'DevOps.docx', 'Selenium Training Proposal.pdf', 'def.py', 'Dockerizing Multiple Services.xml', 'print-video.docx', 'open_test.py', 'adv-python-reg-nov', 'workspace', 'bigBasket.pem', 'Lambda.zip', 'Python JSON API call.docx', 'GettingStarted.side', 'if-else.py', 'demo2.py', 'Data Preprocessing.png', '.Cloud', 'sendRedirect vs RequestDispatcher.rtf', 'python-reg-sept-11', 'Selenium 2.0.key', 'google_images.py', 'CI:CD with AWS.xml', 'Docker 2.0.key', 'uploads', 'SaratogaHouses.csv', 'python-wknd-sep', 'CoverLetter.docx', 'mysql-notes.rtf', 'apache-tomcat-9.0.27', 'core-python-reg-11am', '*args and *kwargs.py', 'test.py', 'Selenium Training Proposal.docx', 'connect.php', 'test2.py', '(EBook -  NLP) - Mind Control - How To Get The Truth Out Of Anyone.pdf', 'google-calendar', 'CI Workflow for Multiple Images.xml', 'Instructions2.sb-7bf5ee61-2IDHe0', '~$AWS Pricing.xlsx', 'Walkthrough of HTML.pdf', 'script.js', 'python-reg-oct', 'pk-APKAIHLXMOKUVCP7CZIA.pem', 'test.java', 'python-basics.py', '~$IOT.pptx', 'myspider.py', '08-Functions.py', '04 - Functions.py', 'Java Questions.docx', 'Demo.class', 'WebEx', 'Selenium Course Content.docx', 'main4.html', 'ml', 'map lambda filter.py', 'Selenium_2.0.side', 'calc.ui', 'AdvPython', 'rd_college_python_iot', 'aws-notes-june-wknd.docx', 'main.html', 'SeleniumClass.side', 'Data PreProcessing.docx', 'Selenium Training Agenda.pdf', 'style.css', 'calc.py', '5ee31c9bc97d410fb4ee3789_into time 2_into time 2JDBC First Program - YouTube (721p).mp4', 'python-batch-reg', 'Ads Record.xlsx', 'App.py', 'print-python.key', 'haarcascade_frontalface_default.xml', '~$thon JSON API call.docx', 'Profile_AnmolArora.pdf', 'Test1Test.java', 'game_exe_test', '.ipynb_checkpoints', 'A.class', '03-Functions.py', 'nlp.ipynb', 'Test1.java', 'fn-3.py', 'Affiliate Marketing and Success Systems.pdf', 'main2.html', 'TMU Python ML Course Content.docx', 'IOT.pptx', 'Advance MySQL.docx', 'calc1.txt', 'Demo.java', 'SeleniumDemo.side', 'Aws-ppt-2.key', 'Building a Multi-container application.xml', 'demo.py', 'Selenium IDE.key', 'Data PreProcessing Draft 2.docx', 'DateTime.py', 'Aws-ppt.key', 'Aws-ppt-3.key', 'Manage My Money for September.numbers', 'Machine Learning copy.pptx', 'Aws-ppt-7.key', 'asjak.py', 'Python JSON API.docx', 'error.html', '~$ix Commands.docx', 'Aws-ppt-6.key', 'Instructions2', '05-Functions.py', 'Social_Network_Ads.csv', 'py.py', '01-Print.py', 'imdb_labelled.txt', '02-Functions.py', 'main3.html', 'git', 'Selenium IDE.pptx', 'Aws-ppt-4.key', 'image.jpg', 'video_1.mp4', 'fn-2.py', 'Machine Learning.pptx', 'java-demo.java', 'AWS Pricing.xlsx', 'abc.py', 'Aws-ppt-5.key', 'Docker Course Content.docx']
>>> os.getcwd()
'/Users/anmolrajarora/Documents'
>>> os.chdir('C:/Users/Ram/Documents/CorePythonBatch')
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    os.chdir('C:/Users/Ram/Documents/CorePythonBatch')
FileNotFoundError: [Errno 2] No such file or directory: 'C:/Users/Ram/Documents/CorePythonBatch'
>>> os.chdir('/Users/anmolrajarora/Documents/CorePythonBatch')
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    os.chdir('/Users/anmolrajarora/Documents/CorePythonBatch')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/anmolrajarora/Documents/CorePythonBatch'
>>> os.chdir('/Users/anmolrajarora/google drive/work/CorePythonBatch')
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    os.chdir('/Users/anmolrajarora/google drive/work/CorePythonBatch')
FileNotFoundError: [Errno 2] No such file or directory: '/Users/anmolrajarora/google drive/work/CorePythonBatch'
>>> os.chdir('/Users/anmolrajarora/google drive/work/2021/CorePythonBatch')
>>> os.getcwd()
'/Users/anmolrajarora/google drive/work/2021/CorePythonBatch'
>>> os.listdir()
['list-demo.py', 'list-functionality.py', 'base-types.py', 'palindrome.py', '.DS_Store', 'prime-number.py', 'img.png', 'nested-list.py', 'even-or-odd.py', 'container-types.py', 'monkey-question.py', 'celsius-to-fahrenheit.py', 'generate-random-number.py', 'swap-two-variables.py', 'armstrong-narcissistic.py', 'factorial.py', 'kilometres-to-miles.py', 'check-leap-year.py', 'prime-numbers-in-interval.py', 'dictionary.py', 'set.py', 'lambda_function.py', 'fibonacci.py', 'largest-among-three.py', 'identifiers_variables_assignment.py', 'list-functions.py']
>>> # import os
>>> # from os import chdir
>>> # from datetime import datetime as dt
>>> # import pandas as pd
>>> from os import *
>>> getcwd()
'/Users/anmolrajarora/google drive/work/2021/CorePythonBatch'
>>> listdir()
['list-demo.py', 'list-functionality.py', 'base-types.py', 'palindrome.py', '.DS_Store', 'prime-number.py', 'img.png', 'nested-list.py', 'even-or-odd.py', 'container-types.py', 'monkey-question.py', 'celsius-to-fahrenheit.py', 'generate-random-number.py', 'swap-two-variables.py', 'armstrong-narcissistic.py', 'factorial.py', 'kilometres-to-miles.py', 'check-leap-year.py', 'prime-numbers-in-interval.py', 'dictionary.py', 'set.py', 'lambda_function.py', 'fibonacci.py', 'largest-among-three.py', 'identifiers_variables_assignment.py', 'list-functions.py']
>>> # 1. from os import chdir
>>> # 2. from datetime import datetime as dt
>>> # 3. import os
>>> # 4. import pandas as pd
>>> # 5. from os import *
>>> '''
'''
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> bytes([72,9,64])
b'H\t@'
>>> bytes(72)
b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
>>> bytes.fromhex('A890DE')
b'\xa8\x90\xde'
>>> list("abc")
['a', 'b', 'c']
>>> list((10,20,30))
[10, 20, 30]
>>> list(10,20,30)
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    list(10,20,30)
TypeError: list expected at most 1 arguments, got 3
>>> student = {
	name : "Ram",
	marks : 96
	}
Traceback (most recent call last):
  File "<pyshell#11>", line 2, in <module>
    name : "Ram",
NameError: name 'name' is not defined
>>> student = {
	"name" : "Ram",
	"marks" : 96
}
>>> list(student)
['name', 'marks']
>>> student.items()
dict_items([('name', 'Ram'), ('marks', 96)])
>>> list(student.items())
[('name', 'Ram'), ('marks', 96)]
>>> dict( (1:"one"), (2:"two"), (3:"three") )
SyntaxError: invalid syntax
>>> dict( (1,"one"), (2,"two"), (3,"three") )
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    dict( (1,"one"), (2,"two"), (3,"three") )
TypeError: dict expected at most 1 arguments, got 3
>>> dict( ( (1,"one"), (2,"two"), (3,"three") ) )
{1: 'one', 2: 'two', 3: 'three'}
>>> list1 = ["one","two","three","four"]
>>> dict(list1)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    dict(list1)
ValueError: dictionary update sequence element #0 has length 3; 2 is required
>>> list1 = [("one","two"),("three","four")]
>>> dict(list1)
{'one': 'two', 'three': 'four'}
>>> 
>>> 
>>> 
>>> list1 = ["one","two","three","four"]
>>> set(list1)
{'one', 'four', 'two', 'three'}
>>> set(student)
{'marks', 'name'}
>>> 
>>> 
>>> str1 = "dictionary update sequence element #0 has length 3; 2 is required"
>>> str1.split()
['dictionary', 'update', 'sequence', 'element', '#0', 'has', 'length', '3;', '2', 'is', 'required']
>>> str1.split('e')
['dictionary updat', ' s', 'qu', 'nc', ' ', 'l', 'm', 'nt #0 has l', 'ngth 3; 2 is r', 'quir', 'd']
>>> words = str1.split()
>>> words
['dictionary', 'update', 'sequence', 'element', '#0', 'has', 'length', '3;', '2', 'is', 'required']
>>> " ".join(words)
'dictionary update sequence element #0 has length 3; 2 is required'
>>> "$".join(words)
'dictionary$update$sequence$element$#0$has$length$3;$2$is$required'
>>> input("Enter numbers separated by spaces: ")
Enter numbers separated by spaces: 1 2 3 4 5 6 7 8 9 10
'1 2 3 4 5 6 7 8 9 10'
>>> for char in '1 2 3 4 5 6 7 8 9 10':
	print(char)

	
1
 
2
 
3
 
4
 
5
 
6
 
7
 
8
 
9
 
1
0
>>> '1 2 3 4 5 6 7 8 9 10'.split()
['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
>>> for element in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
	print(int(x))

	
Traceback (most recent call last):
  File "<pyshell#45>", line 2, in <module>
    print(int(x))
NameError: name 'x' is not defined
>>> for element in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']:
	print(int(element))

	
1
2
3
4
5
6
7
8
9
10
>>> [int(element) for element in '1 2 3 4 5 6 7 8 9 10'.split()]
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
>>> list1 = [10,20,30,40,50]
>>> len(list1)
5
>>> list1[0]
10
>>> list1[-1]
50
>>> list1[1]
20
>>> list1[-2]
40
>>> del list1[3]
>>> list1
[10, 20, 30, 50]
>>> list1[2] = 90
>>> list1
[10, 20, 90, 50]
>>> #[start:stop:step]
>>> list1[:-1]
[10, 20, 90]
>>> list1[1:-1]
[20, 90]
>>> list1[::2]
[10, 90]
>>> list1[::-1]
[50, 90, 20, 10]
>>> list1[::-2]
[50, 20]
>>> list1[:]
[10, 20, 90, 50]
>>> list1
[10, 20, 90, 50]
>>> list1[1:3]
[20, 90]
>>> list1[3:]
[50]
>>> # creating a sub-sequence thorugh slicing gives you back a shallow copy of original list
>>> list1 = [1,2,3,4,5,6,7,8,9]
>>> del list1[3:5]
>>> list1
[1, 2, 3, 6, 7, 8, 9]
>>> list1[1:4] = 45
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    list1[1:4] = 45
TypeError: can only assign an iterable
>>> list1[1:4] = [12,23]
>>> list1
[1, 12, 23, 7, 8, 9]
>>> 10 < 20 and 20 < 30
True
>>> 10 < 2 and 20 < 30
False
>>> 10 < 20 and 20 < 3
False
>>> 10 < 2 and 20 < 3
False
>>> 10 < 20 or 20 < 30
True
>>> 10 < 2 or 20 < 30
True
>>> 10 < 20 or 20 < 3
True
>>> 10 < 2 or 20 < 3
False
>>> 10 < 2 | 20 < 3
False
>>> 10 or 20
10
>>> 10 and 20
20
>>> 10 and -1
-1
>>> 0 and -1
0
>>> 0 or -1
-1
>>> 
'''
