Python 3.7.7 (default, Mar 10 2020, 15:43:03) 
[Clang 11.0.0 (clang-1100.0.33.17)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
WARNING: The version of Tcl/Tk (8.5.9) in use may be unstable. Visit
http://www.python.org/download/mac/tcltk/ for current information.
>>> list1 = [1, 2, 3, 4, 5, 100, True, False, "hello", 'world']
>>> help(list)
Help on class list in module builtins:

class list(object)
 |  list(iterable=(), /)
 |  
 |  Built-in mutable sequence.
 |  
 |  If no argument is given, the constructor creates a new empty list.
 |  The argument must be an iterable if specified.
 |  
 |  Methods defined here:
 |  
 |  __add__(self, value, /)
 |      Return self+value.
 |  
 |  __contains__(self, key, /)
 |      Return key in self.
 |  
 |  __delitem__(self, key, /)
 |      Delete self[key].
 |  
 |  __eq__(self, value, /)
 |      Return self==value.
 |  
 |  __ge__(self, value, /)
 |      Return self>=value.
 |  
 |  __getattribute__(self, name, /)
 |      Return getattr(self, name).
 |  
 |  __getitem__(...)
 |      x.__getitem__(y) <==> x[y]
 |  
 |  __gt__(self, value, /)
 |      Return self>value.
 |  
 |  __iadd__(self, value, /)
 |      Implement self+=value.
 |  
 |  __imul__(self, value, /)
 |      Implement self*=value.
 |  
 |  __init__(self, /, *args, **kwargs)
 |      Initialize self.  See help(type(self)) for accurate signature.
 |  
 |  __iter__(self, /)
 |      Implement iter(self).
 |  
 |  __le__(self, value, /)
 |      Return self<=value.
 |  
 |  __len__(self, /)
 |      Return len(self).
 |  
 |  __lt__(self, value, /)
 |      Return self<value.
 |  
 |  __mul__(self, value, /)
 |      Return self*value.
 |  
 |  __ne__(self, value, /)
 |      Return self!=value.
 |  
 |  __repr__(self, /)
 |      Return repr(self).
 |  
 |  __reversed__(self, /)
 |      Return a reverse iterator over the list.
 |  
 |  __rmul__(self, value, /)
 |      Return value*self.
 |  
 |  __setitem__(self, key, value, /)
 |      Set self[key] to value.
 |  
 |  __sizeof__(self, /)
 |      Return the size of the list in memory, in bytes.
 |  
 |  append(self, object, /)
 |      Append object to the end of the list.
 |  
 |  clear(self, /)
 |      Remove all items from list.
 |  
 |  copy(self, /)
 |      Return a shallow copy of the list.
 |  
 |  count(self, value, /)
 |      Return number of occurrences of value.
 |  
 |  extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
 |  
 |  index(self, value, start=0, stop=9223372036854775807, /)
 |      Return first index of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  insert(self, index, object, /)
 |      Insert object before index.
 |  
 |  pop(self, index=-1, /)
 |      Remove and return item at index (default last).
 |      
 |      Raises IndexError if list is empty or index is out of range.
 |  
 |  remove(self, value, /)
 |      Remove first occurrence of value.
 |      
 |      Raises ValueError if the value is not present.
 |  
 |  reverse(self, /)
 |      Reverse *IN PLACE*.
 |  
 |  sort(self, /, *, key=None, reverse=False)
 |      Stable sort *IN PLACE*.
 |  
 |  ----------------------------------------------------------------------
 |  Static methods defined here:
 |  
 |  __new__(*args, **kwargs) from builtins.type
 |      Create and return a new object.  See help(type) for accurate signature.
 |  
 |  ----------------------------------------------------------------------
 |  Data and other attributes defined here:
 |  
 |  __hash__ = None

>>> list1.append("new element")
>>> list1
[1, 2, 3, 4, 5, 100, True, False, 'hello', 'world', 'new element']
>>> id(list1)
4401034976
>>> list1.clear()
>>> list1
[]
>>> id(list1)
4401034976
>>> del list1
>>> list1
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    list1
NameError: name 'list1' is not defined
>>> list1 = [1, 2, 3, 4, 5, 100, True, False, 'hello', 'world', 'new element']
>>> del list1[0]
>>> list1
[2, 3, 4, 5, 100, True, False, 'hello', 'world', 'new element']
>>> del list1[0:5]
>>> list1
[True, False, 'hello', 'world', 'new element']
>>> list1.append([1,2,3,4,5])
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5]]
>>> list1[-1]
[1, 2, 3, 4, 5]
>>> list1[-1][-1]
5
>>> list2 = list1
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5]]
>>> list2
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5]]
>>> id(list1)
4401808800
>>> id(list2)
4401808800
>>> list1.append("common element")
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5], 'common element']
>>> list2
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5], 'common element']
>>> list3 = list1.copy()
>>> id(list1)
4401808800
>>> id(list3)
4401900992
>>> list1.append("diff element")
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5], 'common element', 'diff element']
>>> list2
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5], 'common element', 'diff element']
>>> list3
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5], 'common element']
>>> import copy
>>> list1[-2].append(6)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    list1[-2].append(6)
AttributeError: 'str' object has no attribute 'append'
>>> list1[-3].append(6)
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6], 'common element', 'diff element']
>>> list2
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6], 'common element', 'diff element']
>>> list3
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6], 'common element']
>>> list4 = copy.deepcopy(list1)
>>> list1[-3].append(7)
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7], 'common element', 'diff element']
>>> list2
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7], 'common element', 'diff element']
>>> list3
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7], 'common element']
>>> list4
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6], 'common element', 'diff element']
>>> list1[-3].append([100,200,300])
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300]], 'common element', 'diff element']
>>> list4
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6], 'common element', 'diff element']
>>> list5 = copy.deepcopy(list1)
>>> id(list1)
4401808800
>>> id(list5)
4401755152
>>> id(list1[-3])
4401394704
>>> id(list5[-3])
4401394304
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300]], 'common element', 'diff element']
>>> list5
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300]], 'common element', 'diff element']
>>> id(list1[-3)
   
SyntaxError: invalid syntax
>>> id(list1[-3][-1])
4401034976
>>> id(list1[-5][-1])
4354182128
>>> list1[-3][-1].append(400)
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element']
>>> list5
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300]], 'common element', 'diff element']
>>> list1.count(1)
1
>>> list1.count(0)
1
>>> list1.count(100)
0
>>> list1.count([100,200,300])
0
>>> list1.count([1, 2, 3, 4, 5, 6, 7, [100, 200, 300]])
0
>>> list1.count([1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]])
1
>>> list1.count(value=1)
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    list1.count(value=1)
TypeError: count() takes no keyword arguments
>>> list1.count(1, second=100)
Traceback (most recent call last):
  File "<pyshell#69>", line 1, in <module>
    list1.count(1, second=100)
TypeError: count() takes no keyword arguments
>>> list1.extend([99,999,9999])
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999]
>>> list1.append([99,999,9999])
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999, [99, 999, 9999]]
>>> list1.index(99)
8
>>> list1[8]
99
>>> list1.index(99, 9)
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    list1.index(99, 9)
ValueError: 99 is not in list
>>> list1.index(99, 0, 7)
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    list1.index(99, 0, 7)
ValueError: 99 is not in list
>>> list1.index(99, 7)
8
>>> list1.index(99, stop=7)
Traceback (most recent call last):
  File "<pyshell#79>", line 1, in <module>
    list1.index(99, stop=7)
TypeError: index() takes no keyword arguments
>>> list1
[True, False, 'hello', 'world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999, [99, 999, 9999]]
>>> list1[3] = "new world"
>>> list1
[True, False, 'hello', 'new world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999, [99, 999, 9999]]
>>> list1.insert(3, "mars")
>>> list1
[True, False, 'hello', 'mars', 'new world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999, [99, 999, 9999]]
>>> list1.pop()
[99, 999, 9999]
>>> list1
[True, False, 'hello', 'mars', 'new world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99, 999, 9999]
>>> list1.pop()
9999
>>> list1.pop()
999
>>> list1
[True, False, 'hello', 'mars', 'new world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99]
>>> list1.pop(3)
'mars'
>>> list1
[True, False, 'hello', 'new world', 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99]
>>> list1[3] = 0
>>> list1
[True, False, 'hello', 0, 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99]
>>> list1.remove(0)
>>> list1
[True, 'hello', 0, 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99]
>>> list1.sort()
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    list1.sort()
TypeError: '<' not supported between instances of 'str' and 'bool'
>>> list_int = [1,3,2,4,6,5,7]
>>> list_int.sort()
>>> list_int
[1, 2, 3, 4, 5, 6, 7]
>>> list_int.sort(x=10, y=20)
Traceback (most recent call last):
  File "<pyshell#100>", line 1, in <module>
    list_int.sort(x=10, y=20)
TypeError: 'x' is an invalid keyword argument for sort()
>>> list_int.sort(10,20)
Traceback (most recent call last):
  File "<pyshell#101>", line 1, in <module>
    list_int.sort(10,20)
TypeError: sort() takes no positional arguments
>>> list_int.sort(*=20)
SyntaxError: invalid syntax
>>> list_int.sort(*=True)
SyntaxError: invalid syntax
>>> list_int.sort(True)
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    list_int.sort(True)
TypeError: sort() takes no positional arguments
>>> list_int.sort(False)
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    list_int.sort(False)
TypeError: sort() takes no positional arguments
>>> list_int.sort(*="1"
	      
SyntaxError: invalid syntax
>>> list_int.sort(*="1")
SyntaxError: invalid syntax
>>> list_int.sort([10,20,30])
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    list_int.sort([10,20,30])
TypeError: sort() takes no positional arguments
>>> list_int
[1, 2, 3, 4, 5, 6, 7]
>>> list_new = [ *list_int, 10,20 ]
>>> list_new
[1, 2, 3, 4, 5, 6, 7, 10, 20]
>>> list_new = [ list_int, 10,20 ]
>>> list_new
[[1, 2, 3, 4, 5, 6, 7], 10, 20]
>>> list_int.sort(reverse=True)
>>> list_int
[7, 6, 5, 4, 3, 2, 1]
>>> list1
[True, 'hello', 0, 'new element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'common element', 'diff element', 99]
>>> list1.reverse()
>>> list1
[99, 'diff element', 'common element', [1, 2, 3, 4, 5, 6, 7, [100, 200, 300, 400]], 'new element', 0, 'hello', True]
>>> 