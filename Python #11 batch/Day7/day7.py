Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> # Intro Python
>>> # Identifier
>>> # Rules of declaring an identifier
>>> # keywords/ reserved keywords in python
>>> # Python Literals
>>> # Python Operators
>>> # Bitwise operator
>>> 10 & 7
2
>>> 10 and 7
7
>>> # x and y
>>> True and False
False
>>> 1 and 6
6
>>> #Rule: when your x is True then print y for logical 'and'
>>> # Rule2: when your x is False then print x
>>> False and True
False
>>> 0 and 1
0
>>> 0 and 34456
0
>>> 0 and false
0
>>> False and 23
False
>>> False and false
False
>>> false and False
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    false and False
NameError: name 'false' is not defined
>>> false
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    false
NameError: name 'false' is not defined
>>> 0 and 12
0
>>> None and 12
>>> False and 12
False
>>> '' and 12
''
>>> 12 and None
>>> # 0 False ''====> False
>>> ' ' and 12
12
>>> # space is also considered as a block
>>> id('')
4226272
>>> id(' ')
36178328
>>> ##################################
>>> #bitwise NOT: ~ (tild symbol)
>>> ~ True
-2
>>> ~ 0
-1
>>> ~ False
-1
>>> ~ 2
-3
>>> ~ 4
-5
>>> 0b0111
7
>>> 0b1000
8
>>> ~7
-8
>>> # when we negate using bitwise NOT it performs Two's complement
>>> not 7
False
>>> not 'A'
False
>>> not 12.30
False
>>> not 0
True
>>> not False
True
>>> not ''
True
>>> not None
True
>>> ##########################
>>> #Membership Operators
>>> # These operators are used to check the avalability in the given object/ presence in the object
>>> # in  not in
>>> 'Ak' in 'Akshay Kotawar'
True
>>> 'AK' in 'Akshay Kotawar'
False
>>> 'ak' in 'Akshay Kotawar'
False
>>> # here it will identify the given sequence is a part of original sequence or not
>>> 14 in [1,45,20,33,14,18,90,14]
True
>>> '14' in [1,45,20,33,14,18,90,14]
False
>>> origin = [1,45,20,33,14,18,90,14]
>>> origin
[1, 45, 20, 33, 14, 18, 90, 14]
>>> # How to take input from user: use input() function
>>> val = input('Enter the value for search:')
Enter the value for search:45
>>> val
'45'
>>> type(val)
<class 'str'>
>>> val in origin
False
>>> int(val)
45
>>> int(val) in origin
True
>>> # basic use of membership operator is Searching
>>> 'hit' in 'rohit sharma'
True
>>> 'hit' not in 'rohit sharma'
False
>>> 'Hit' not in 'rohit sharma'
True
>>> #######################################
>>> #identity Operator
>>> # is      is not
>>> # it check the identity or equality of two ojects
>>> 2 is 2
True
>>> 2 is 2.0
False
>>> id(2)
8791299249216
>>> id(2.0)
4308112
>>> # when we want to check address equality we can make use of identity operators
>>> 2==2
True
>>> 2==2.0
True
>>> # == works on content equality
>>> # what is difference btwn == and is
>>> 
