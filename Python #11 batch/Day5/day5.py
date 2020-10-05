Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #will wait for 2 mins
>>> #SET PATH---- ADD PATH
>>> import sys
>>> sys.path
['', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\Lib\\idlelib', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\python37.zip', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\DLLs', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\lib', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37', 'C:\\Users\\Admin\\AppData\\Roaming\\Python\\Python37\\site-packages', 'C:\\Users\\Admin\\AppData\\Local\\Programs\\Python\\Python37\\lib\\site-packages']
>>> #Python is Programming or scripting lang?
>>> #Python is both programming as well as scripting lang
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/even.py ===
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
79
80
81
82
83
84
85
86
87
88
89
90
91
92
93
94
95
96
97
98
99
100
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/even.py ===
2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/even.py ===
2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38 40 42 44 46 48 50 52 54 56 58 60 62 64 66 68 70 72 74 76 78 80 82 84 86 88 90 92 94 96 98 100 
>>> list(range(2,101,2))
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]
>>> #When we want to satisfy temp. requirement then scripting is best solution
>>> # In scriptin there is no need to create file,save it,name it...nothing procedure we have to follow
>>> #Python Literals
>>> 100
100
>>> #Everything in python is Object
>>> id(100)
8791208681600
>>> 'ABC'
'ABC'
>>> id('ABC')
30596768
>>> x = 100
>>> x
100
>>> id(x)
8791208681600
>>> #x is an identifier
>>> #x(identifier) =(Operator) 100(Literal)
>>> # Literal is an entity/obj which is refered by identifier
>>> #Types of Literals:
>>> #1. String Literals:
>>> 'ABC'
'ABC'
>>> "Python"
'Python'
>>> # In string 2 categories are there: single line and multiline
>>> # 1.1 Single Line: 'skdnf klnsdf' "dfgdh 12315 df"
>>> # 1.2 Multiline:
>>> 'I am python'#single line
'I am python'
>>> 'I am\
Python\
Hello\
all'
'I amPythonHelloall'
>>> 'I
SyntaxError: EOL while scanning string literal
>>> 'I am\
 Python\
 Hello\
 all'
'I am Python Hello all'
>>> """I"""
'I'
>>> """I
 am
 Python
 Hello
 All
 """
'I\n am\n Python\n Hello\n All\n '
>>> #\n means newline
>>> #2. Integer Literal:
>>> #we can give the numbers with base10----[0-9]---Decimal
>>> 4
4
>>> 20
20
>>> 65
65
>>> type(4)
<class 'int'>
>>> A40
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    A40
NameError: name 'A40' is not defined
>>> #3. Float literal:
>>> # number should be in [0-9] and it should have floating point
>>> 45.20
45.2
>>> type(45.2)
<class 'float'>
>>> #4. Complex literal: real+img part
>>> 3+2j
(3+2j)
>>> type(3+2j)
<class 'complex'>
>>> # 5. Bool: True or False
>>> True
True
>>> False
False
>>> type(False)
<class 'bool'>
>>> # 6. Python collection Literals
>>> # Basically these literals are considered as Data strcutures of Python
>>> # Ex: list, tuple, set, dict
>>> #List:  []
>>> [1,2,3,4]
[1, 2, 3, 4]
>>> type([1,2,3,4])
<class 'list'>
>>> #Tuple: ()
>>> (1,2,3,4)
(1, 2, 3, 4)
>>> type((1,2,3,4))
<class 'tuple'>
>>> # set: {}
>>> {4,5,6}
{4, 5, 6}
>>> type({4,5,6})
<class 'set'>
>>> #dict: {key:value}
>>> {1:100,2:200}
{1: 100, 2: 200}
>>> type({1:100,2:200})
<class 'dict'>
>>> #None literal
>>> None
>>> #Number system Literals: bin(base2--0/1,oct(base8--[0-7]),dec(base10--[0-9],hex(base16--[0-9A-F]
>>> 0b1111
15
>>> 0b11
3
>>> 0B1111
15
>>> #above literal is binary
>>> # octal
>>> 0o05
5
>>> 0o235
157
>>> 0O123
83
>>> 123234534
123234534
>>> #hexadecimal
>>> 0x12A
298
>>> 0X65
101
>>> #Bult-in functions
>>> #Built-in functions
>>> print('hi')
hi
>>> #print is used to print the output on console
>>> # id()- is used to check the memory address of object
>>> id(x)
8791208681600
>>> x
100
>>> y = 100
>>> id(y)
8791208681600
>>> #type()-- is used to check the type of data
>>> type('')
<class 'str'>
>>> type(1)
<class 'int'>
>>> type(True)
<class 'bool'>
>>> type([])
<class 'list'>
>>> type(())
<class 'tuple'>
>>> #type() is used to check the type of litrals
>>> '1,2,3'
'1,2,3'
>>> list('1,2,3')
['1', ',', '2', ',', '3']
>>> [1,2,3]
[1, 2, 3]
>>> list(1,2,3)
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    list(1,2,3)
TypeError: list expected at most 1 arguments, got 3
>>> list((1,2,3))
[1, 2, 3]
>>> 5+2k
SyntaxError: invalid syntax
>>> 3+4J
(3+4j)
>>> 
