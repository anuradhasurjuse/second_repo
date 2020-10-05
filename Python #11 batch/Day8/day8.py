Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # & | ^ ~ >> << bitwise operators
>>> 2<<2
8
>>> 0b0010
2
>>> # 0010====== 1000
>>> 0b1000
8
>>> #shifting of the bits is performed here
>>> 2>>2
0
>>> #0010====0000
>>> 7>>3
0
>>> # 0111====0000
>>> 7>>2#ans:0001
1
>>> #####################################################
>>> #Type casting/ Type conversion
>>> -10>>2
-3
>>> 0b1010
10
>>> #1010===0010
>>> # 2 Types are there:
>>> # Implicit type casting: which is performed by python interpreter itself
>>> # Type casting: coverting of data from one type to other type
>>> #ex: implicit
>>> 8/2
4.0
>>> 2 + 2.5
4.5
>>> # int ---- float ---- complex
>>> 2.3 + 3+4j
(5.3+4j)
>>> 4 + (1+2j)
(5+2j)
>>> # 32----64----128 memory
>>> 2 + 2.0
4.0
>>> # Explicit type casting: which is performed by user
>>> s = '10'
>>> type(s)
<class 'str'>
>>> int(s)
10
>>> float(s)
10.0
>>> complex(s)
(10+0j)
>>> bool(s)
True
>>> bin(s)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    bin(s)
TypeError: 'str' object cannot be interpreted as an integer
>>> oct(s)
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    oct(s)
TypeError: 'str' object cannot be interpreted as an integer
>>> hex(s)
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    hex(s)
TypeError: 'str' object cannot be interpreted as an integer
>>> list(s)
['1', '0']
>>> tuple(s)
('1', '0')
>>> set(s)
{'0', '1'}
>>> dict(s)
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    dict(s)
ValueError: dictionary update sequence element #0 has length 1; 2 is required
>>> #dict requires key:value
>>> x = 25
>>> bin(x)
'0b11001'
>>> oct(x)
'0o31'
>>> hex(x)
'0x19'
>>> bin(0x19)
'0b11001'
>>> 0b11001
25
>>> b = True
>>> b
True
>>> int(b)
1
>>> float(b)
1.0
>>> bool(b)
True
>>> oct(b)
'0o1'
>>> hex(b)
'0x1'
>>> bin(x)
'0b11001'
>>> bin(b)
'0b1'
>>> s
'10'
>>> s = int(s)
>>> s
10
>>> tyep(s)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    tyep(s)
NameError: name 'tyep' is not defined
>>> type(s)
<class 'int'>
>>> ###########################################
>>> # How to take input from the user
>>> #########################################
>>> # input() built in function used
>>> input('Enter name:')
Enter name:Amol
'Amol'
>>> name = input('Enter your name:')
Enter your name:Amol
>>> name
'Amol'
>>> # input uses str type as a default
>>> per_day_sal = input('Enter your per day salary:')
Enter your per day salary:500
>>> per_day_sal
'500'
>>> per_month_sal = per_day_sal*30
>>> per_month_sal
'500500500500500500500500500500500500500500500500500500500500500500500500500500500500500500'
>>> # when we use one str and one int object then it performs repitition
>>> '10'*4
'10101010'
>>> per_day_sal = float(input('Enter your per day salary:'))
Enter your per day salary:500
>>> per_day_sal
500.0
>>> per_month_sal = per_day_sal*30
>>> per_month_sal
15000.0
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py ===
Enter your personal information
Enter your name:Yameen
Enter your age30
Enter your salary:34000
Yameen 30 34000.0
>>> #########################
>>> # eval(): this function is used to evaluate expression
>>> 12+2*3
18
>>> input('Enter expression:')
Enter expression:12+2*3
'12+2*3'
>>> int(input('Enter expression:'))
Enter expression:12+2*3
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    int(input('Enter expression:'))
ValueError: invalid literal for int() with base 10: '12+2*3'
>>> exp = eval(input('Calculate area of circle:'))
Calculate area of circle:3.14*4*4
>>> exp
50.24
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py ===
Enter the radius:4
Traceback (most recent call last):
  File "C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py", line 9, in <module>
    eval(pi*rad*rad)
TypeError: eval() arg 1 must be a string, bytes or code object
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py ===
Enter the radius:4
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py ===
Enter the radius:4
50.24
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/info.py ===
Enter the radius:4
Area of Circle is: 50.24
>>> s= '12345678'
>>> len(s)
8
>>> 
