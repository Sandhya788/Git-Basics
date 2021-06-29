Python 3.7.5 (tags/v3.7.5:5c02a39a0b, Oct 15 2019, 00:11:34) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> names=['navin','kiran','john']
>>> names
['navin', 'kiran', 'john']
>>> values=[9.5,'navin',25]
>>> values
[9.5, 'navin', 25]
>>> mil=[nums,names]
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    mil=[nums,names]
NameError: name 'nums' is not defined
>>> nums=[25,12,95,14,36]
>>> nums
[25, 12, 95, 14, 36]
>>> mil=[nums,names]
>>> mil
[[25, 12, 95, 14, 36], ['navin', 'kiran', 'john']]
>>> nums.append(45)
>>> nums
[25, 12, 95, 14, 36, 45]
>>> nums.insert(2,77)
>>> nums
[25, 12, 77, 95, 14, 36, 45]
>>> nums.remove(14)
>>> nums
[25, 12, 77, 95, 36, 45]
>>> nums.pop[1]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    nums.pop[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> nums.pop(1)
12
>>> nums.pop()
45
>>> del nums[2:]
>>> nums
[25, 77]
>>> nums.extend([29,14,12,36])
>>> nums
[25, 77, 29, 14, 12, 36]
>>> min(nums)
12
>>> max(nums)
77
>>> sum(nums)
193
>>> nums.sort()
>>> nums
[12, 14, 25, 29, 36, 77]
>>> name="Telsuko"
>>> print(name[-3])
u
>>> name="Telusko"
>>> print(name[-3])
s
>>> 
