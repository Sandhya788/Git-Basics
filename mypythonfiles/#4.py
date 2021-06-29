Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> tup=(21,25,6,14)
>>> tup
(21, 25, 6, 14)
>>> tup[1]
25
>>> tup[1]=35
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    tup[1]=35
TypeError: 'tuple' object does not support item assignment
>>> tup.index(0)
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    tup.index(0)
ValueError: tuple.index(x): x not in tuple
>>> tup.index(5,0,6)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    tup.index(5,0,6)
ValueError: tuple.index(x): x not in tuple
>>> tup.index(6)
2
>>> tup.count(1)
0
>>> tup.count(21)
1
>>> s={22,25,1}
>>> s
{25, 22, 1}
>>> s={22,25,14,21,5}
>>> s
{5, 14, 21, 22, 25}
>>> s={25,14,98,63,75,98}
>>> s
{98, 75, 14, 25, 63}
>>> s[2]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    s[2]
TypeError: 'set' object is not subscriptable
>>> nums=[25,36,95,14,12,26]
>>> nums
[25, 36, 95, 14, 12, 26]
>>> del.nums([95,14,12])
SyntaxError: invalid syntax
>>> del nums([95,14,12])
SyntaxError: can't delete function call
>>> del nums[95,14,12]
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    del nums[95,14,12]
TypeError: list indices must be integers or slices, not tuple
>>> del nums[2:5]
>>> nums
[25, 36, 26]
>>> v=[1,2,3,4,5,6,7,8]
>>> v
[1, 2, 3, 4, 5, 6, 7, 8]
>>> nums.extend(v)
>>> nums
[25, 36, 26, 1, 2, 3, 4, 5, 6, 7, 8]
>>> f=[78,89,45,56,12,23]
>>> f
[78, 89, 45, 56, 12, 23]
>>> j=[]
>>> j
[]
>>> j.copy(f)
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    j.copy(f)
TypeError: copy() takes no arguments (1 given)
>>> j.copy()
[]
>>> f.copy()
[78, 89, 45, 56, 12, 23]
>>> nums.reverse()
>>> nums
[8, 7, 6, 5, 4, 3, 2, 1, 26, 36, 25]
>>> 
