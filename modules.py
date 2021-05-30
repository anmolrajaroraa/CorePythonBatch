'''
Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 16:52:21) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> from math import sin as sin_fn, cos as cos_fn
>>> math
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    math
NameError: name 'math' is not defined
>>> sin
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    sin
NameError: name 'sin' is not defined
>>> cos
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    cos
NameError: name 'cos' is not defined
>>> sin_fn
<built-in function sin>
>>> cos_fn
<built-in function cos>
>>> # direct access to fns, renaming using 'as'
>>> import math
>>> math.sin
<built-in function sin>
>>> math.cos
<built-in function cos>
>>> math.sin_fn
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    math.sin_fn
AttributeError: module 'math' has no attribute 'sin_fn'
>>> import pandas
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    import pandas
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/__init__.py", line 26, in <module>
    from pandas._libs import (hashtable as _hashtable,
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/_libs/__init__.py", line 4, in <module>
    from .tslibs import (
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/pandas/_libs/tslibs/__init__.py", line 7, in <module>
    from .period import Period, IncompatibleFrequency
  File "pandas/_libs/tslibs/period.pyx", line 1, in init pandas._libs.tslibs.period
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 963, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 906, in _find_spec
  File "<frozen importlib._bootstrap_external>", line 1280, in find_spec
  File "<frozen importlib._bootstrap_external>", line 1252, in _get_spec
  File "<frozen importlib._bootstrap_external>", line 1364, in find_spec
  File "<frozen importlib._bootstrap_external>", line 81, in _path_stat
KeyboardInterrupt
>>> import scikit
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import scikit
ModuleNotFoundError: No module named 'scikit'
>>> import sklearm
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    import sklearm
ModuleNotFoundError: No module named 'sklearm'
>>> import sklearn
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    import sklearn
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/sklearn/__init__.py", line 76, in <module>
    from .base import clone
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/sklearn/base.py", line 16, in <module>
    from .utils import _IS_32BIT
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/sklearn/utils/__init__.py", line 20, in <module>
    from .validation import (as_float_array,
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/sklearn/utils/validation.py", line 21, in <module>
    from .fixes import _object_dtype_isnan
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/sklearn/utils/fixes.py", line 18, in <module>
    from scipy.sparse.linalg import lsqr as sparse_lsqr  # noqa
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/scipy/sparse/linalg/__init__.py", line 114, in <module>
    from .isolve import *
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/scipy/sparse/linalg/isolve/__init__.py", line 6, in <module>
    from .iterative import *
  File "/Library/Frameworks/Python.framework/Versions/3.7/lib/python3.7/site-packages/scipy/sparse/linalg/isolve/iterative.py", line 12, in <module>
    from scipy.sparse.linalg.interface import LinearOperator
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 963, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 906, in _find_spec
  File "<frozen importlib._bootstrap_external>", line 1280, in find_spec
  File "<frozen importlib._bootstrap_external>", line 1252, in _get_spec
  File "<frozen importlib._bootstrap_external>", line 1364, in find_spec
  File "<frozen importlib._bootstrap_external>", line 81, in _path_stat
KeyboardInterrupt
>>> 1+2-3*4/5//6%7**8
3.0
>>> 7**8
5764801
>>> 1+2-3*4/5//6%5764801
3.0
>>> 1+2-12/5//6%5764801
3.0
>>> 12/5
2.4
>>> 1+2-2.4//6%5764801
3.0
>>> 2.4//6
0.0
>>> 2.4/6
0.39999999999999997
>>> 1+2-0.0%5764801
3.0
>>> 0.0%5764801
0.0
>>> 3-0.0
3.0
>>> (1+2-3*4/5//6%7)**8
6561.0
>>> 1+2-3*4/5//6%7
3.0
>>> 3**8
6561
>>> mat1 = ([1, 6, 5],[3 ,4, 8],[2, 12, 3])
>>> mat2 = ([3, 4, 6],[5, 6, 7],[6,56, 7])
>>> mat1 @ mat2
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    mat1 @ mat2
TypeError: unsupported operand type(s) for @: 'tuple' and 'tuple'
>>> import numpy as np
>>> mat1 @ mat2
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    mat1 @ mat2
TypeError: unsupported operand type(s) for @: 'tuple' and 'tuple'
>>> mat1 = np.array([1, 6, 5],[3 ,4, 8],[2, 12, 3])
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    mat1 = np.array([1, 6, 5],[3 ,4, 8],[2, 12, 3])
ValueError: only 2 non-keyword arguments accepted
>>> mat1 = np.array(([1, 6, 5],[3 ,4, 8],[2, 12, 3]))
>>> mat2 = (([3, 4, 6],[5, 6, 7],[6,56, 7]))
>>> mat1 @ mat2
array([[ 63, 320,  83],
       [ 77, 484, 102],
       [ 84, 248, 117]])
>>> mat1 = np.array([[1, 6, 5],[3 ,4, 8],[2, 12, 3]])
>>> mat2 = ([[3, 4, 6],[5, 6, 7],[6,56, 7]])
>>> mat1 @ mat2
array([[ 63, 320,  83],
       [ 77, 484, 102],
       [ 84, 248, 117]])
>>> np.dot(mat1,mat2)
array([[ 63, 320,  83],
       [ 77, 484, 102],
       [ 84, 248, 117]])
>>> abs(3.2)
3.2
>>> abs(-3.2)
3.2
>>> round(3.57)
4
>>> round(3.57,1)
3.6
>>> pow(4,3)
64
>>> 4**#
SyntaxError: invalid syntax
>>> 4**3
64
>>> import math
>>> from math import *
>>> pi
3.141592653589793
>>> sin(pi/4)
0.7071067811865475
>>> cos(2*pi/3)
-0.4999999999999998
>>> sqrt(81)
9.0
>>> log(e**2)
2.0
>>> ceil(12.5)
13
>>> floor(12.5)
12
>>> round(12.5)
12
>>> int(12.5)
12
>>> round(12.6)
13
>>> round(12.5)
12
>>> round(12.51)
13
>>> ceil(12.000001)
13
>>> #if, if..else, if..elif, if..elif..else
>>> x = 10
>>> if bool(x) == True:
	print(True)

	
True
>>> if x == True:
	print(True)

	
>>> x == True
False
>>> if bool(x):
	print(True)

	
True
>>> if x:
	print(True)

	
True
>>> 
'''
