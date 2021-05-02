'''>> > set1 = {}
>> > type(set1)
<class 'dict' >
>> > set1 = set()
>> > type(set1)
<class 'set' >
>> > set1 = {1, 2, 3, 4, 5, 100, 999, True, False, "hello", "bye", "John", "Smith", "Ram"}
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 'Smith', 'hello', 'bye', 'Ram'}
>> > set1 = {1, 2, 3, 4, 5, 100, 999, True, False, "hello", "bye", "John", "Smith", "Ram"}
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 'Smith', 'hello', 'bye', 'Ram'}
>> > set1 = {1, 2, 3, 4, 5, 100, 999, True, False, "hello", "bye", "John", "Smith", "Ram", "Alice"}
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 'Smith', 'hello', 'Alice', 'bye', 'Ram'}
>> > set1 = {1, 2, 3, 4, 5, 100, 999, True, False, "hello", "bye", "John", "Smith", "Ram", "Alice"}
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 'Smith', 'hello', 'Alice', 'bye', 'Ram'}
>> > set1 = {1, 2, 3, 4, 5, 100, 999, True, False, "hello", "bye", "John", "Smith", "Ram", "Alice", 99.9, 99.09, 0.99}
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 99.9, 99.09,
    'Smith', 0.99, 'hello', 'Alice', 'bye', 'Ram'}
>> > help(set)
Help on class set in module builtins:


class set(object)


|  set() -> new empty set object
|  set(iterable) -> new set object
|
|  Build an unordered collection of unique elements.
|
|  Methods defined here:
    |
    |  add(...)
    |      Add an element to a set.
    |
    |      This has no effect if the element is already present.
    |
    |  clear(...)
    |      Remove all elements from this set.
    |
    |  copy(...)
    |      Return a shallow copy of a set.
    |
    |  difference(...)
    |      Return the difference of two or more sets as a new set.
    |
    |      (i.e. all elements that are in this set but not the others.)
    |
    |  difference_update(...)
    |      Remove all elements of another set from this set.
    |
    |  discard(...)
    |      Remove an element from a set if it is a member.
    |
    |      If the element is not a member, do nothing.
    |
    |  intersection(...)
    |      Return the intersection of two sets as a new set.
    |
    |      (i.e. all elements that are in both sets.)
    |
    |  intersection_update(...)
    |      Update a set with the intersection of itself and another.
    |
    |  isdisjoint(...)
    |      Return True if two sets have a null intersection.
    |
    |  issubset(...)
    |      Report whether another set contains this set.
    |
    |  issuperset(...)
    |      Report whether this set contains another set.
    |
    |  pop(...)
    |      Remove and return an arbitrary set element.
    |      Raises KeyError if the set is empty.
    |
    |  remove(...)
    |      Remove an element from a set
    it must be a member.
    |
    |      If the element is not a member, raise a KeyError.
    |
    |  symmetric_difference(...)
    |      Return the symmetric difference of two sets as a new set.
    |
    |      (i.e. all elements that are in exactly one of the sets.)
    |
    |  symmetric_difference_update(...)
    |      Update a set with the symmetric difference of itself and another.
    |
    |  union(...)
    |      Return the union of sets as a new set.
    |
    |      (i.e. all elements that are in either set.)
    |
    |  update(...)
    |      Update a set with the union of itself and others.
    |
    | ----------------------------------------------------------------------
    |  Static methods defined here:
    |
    |  __new__(*args, **kwargs) from builtins.type
    |      Create and return a new object.  See help(type) for accurate signature.
    |
    | ----------------------------------------------------------------------
    |  Data and other attributes defined here:
    |
    |  __hash__ = None


>> > set1.add(77.7)
>> > set1
{False, 1, 2, 3, 4, 5, 100, 999, 'John', 99.9, 99.09,
    'Smith', 77.7, 0.99, 'hello', 'Alice', 'bye', 'Ram'}
>> > set2 = {1, 2, 3, 4, 5}
>> > set1 - set2
{False, 0.99, 99.9, 100, 99.09, 'John', 999,
    'Smith', 77.7, 'hello', 'Alice', 'bye', 'Ram'}
>> > set2 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>> > set1 - set2
{False, 0.99, 99.9, 100, 99.09, 'John', 999,
    'Smith', 77.7, 'hello', 'Alice', 'bye', 'Ram'}
>> > set2 - set1
{6, 7, 8, 9, 10}
>> > set1.difference(set2)
{False, 0.99, 99.9, 100, 99.09, 'John', 999,
    'Smith', 77.7, 'hello', 'Alice', 'bye', 'Ram'}
>> > set2.difference(set1)
{6, 7, 8, 9, 10}
>> > (set1-set2).union(set2-set1)
{False, 0.99, 99.9, 100, 99.09, 'John', 999, 6, 7, 8,
    'Smith', 9, 77.7, 10, 'hello', 'Alice', 'bye', 'Ram'}
>> > set1.symmetric_difference(set2)
{False, 0.99, 6, 7, 8, 9, 10, 'Smith', 'Alice', 'bye',
    'John', 77.7, 'hello', 99.09, 99.9, 100, 999, 'Ram'}
>> > set1.union(set2)
{False, 1, 2, 3, 4, 5, 'John', 0.99, 6, 7, 8, 'Smith', 9, 77.7,
    10, 'hello', 'Alice', 'bye', 99.9, 100, 99.09, 999, 'Ram'}
>> > set1.intersection(set2)
{1, 2, 3, 4, 5}
>> >
>> >
>> > set1.difference(set2)
{False, 0.99, 99.9, 100, 99.09, 'John', 999,
    'Smith', 77.7, 'hello', 'Alice', 'bye', 'Ram'}
>> > set3 = set1.difference(set2)
>> > set3
{False, 0.99, 99.9, 100, 99.09, 'John', 999,
    'Smith', 77.7, 'hello', 'Alice', 'bye', 'Ram'}
>> > set1.difference_update(set2)
>> > set1
{False, 100, 999, 'John', 99.9, 99.09, 'Smith',
    77.7, 0.99, 'hello', 'Alice', 'bye', 'Ram'}
>> > set3 = {11, 12, 13, 14, 15}
>> > set1.union(set2, set3)
{False, 0.99, 1, 2, 3, 4, 'John', 5, 6, 7, 8, 'Smith', 9, 77.7, 10, 11,
    12, 13, 'hello', 14, 'Alice', 15, 'bye', 99.9, 100, 99.09, 999, 'Ram'}
>> > set1.update(set2, set3)
>> > set1
{False, 0.99, 1, 2, 3, 4, 'John', 5, 6, 7, 8, 'Smith', 9, 77.7, 10, 11,
    12, 13, 'hello', 14, 'Alice', 15, 'bye', 99.9, 100, 99.09, 999, 'Ram'}
>> > set1.pop()
False
>> > set1.pop()
0.99
>> > set1.pop()
1
>> > set1.pop()
2
>> > set1.pop()
3
>> > set1.pop()
4
>> > set1.pop()
'John'
>> > set1.pop()
5
>> > set1.remove(99.9)
>> > set1
{6, 7, 8, 'Smith', 9, 77.7, 10, 11, 12, 13, 'hello',
    14, 'Alice', 15, 'bye', 100, 99.09, 999, 'Ram'}
>> >
>> >
>> >
>> > set1
{6, 7, 8, 'Smith', 9, 77.7, 10, 11, 12, 13, 'hello',
    14, 'Alice', 15, 'bye', 100, 99.09, 999, 'Ram'}
>> > set2
{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
>> > set3
{11, 12, 13, 14, 15}
>> > set2.isdisjoint(set3)
True
>> > set2.isdisjoint(set1)
False
>> > set1.issubset(set2)
False
>> > set4 = {6, 7, 8, 'Smith', 9, 77.7, 10, 11, 12, 13, 'hello', 14, 'Alice', 15, 'bye', 100, 99.09, 999, 'Ram', 90, 91}
>> > set1.issubset(set4)
True
>> > set4.issuperset(set1)
True
>> > type(set4)
<class 'set' >
>> > set4 = frozenset({6, 7, 8, 'Smith', 9, 77.7, 10, 11, 12, 13, 'hello', 14, 'Alice', 15, 'bye', 100, 99.09, 999, 'Ram', 90, 91})
>> > type(set4)
<class 'frozenset' >
>> > set4.pop()
Traceback(most recent call last):
    File "<pyshell#64>", line 1, in < module >
    set4.pop()
AttributeError: 'frozenset' object has no attribute 'pop'
>> > for value in set4:
    print(value)


6
7
8
9
10
Smith
11
12
13
14
15
77.7
hello
Alice
bye
90
91
99.09
100
999
Ram
>> >
'''
