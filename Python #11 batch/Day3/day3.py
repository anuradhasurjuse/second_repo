Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #Identifier
>>> #The name give to an object is an identifier
>>> 100
100
>>> id(100)
8791476134016
>>> 'Python'
'Python'
>>> id('python')
48946008
>>> x = 100
>>> id(x)
8791476134016
>>> s = 'python'
>>> id(s)
48946008
>>> # Identifier contraints
>>> # We can use alphabates [a-zA-z]
>>> #Remember Python is case sensitive lang
>>> S ='Python'
>>> s
'python'
>>> S
'Python'
>>> x
100
>>> X# captilize its not in memory now
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    X# captilize its not in memory now
NameError: name 'X' is not defined
>>> # Direct no. we cant use
>>> 1 = 100
SyntaxError: can't assign to literal
>>> 20 = 100
SyntaxError: can't assign to literal
>>> #but we can use nos. along with characters
>>> #condition is use nos. in between or at the end
>>> a20 =400
>>> a20
400
>>> 20a = 500
SyntaxError: invalid syntax
>>> #when we are using combinition of two things like one char and one number in that case use underscore _ in between
>>> a_20 =478
>>> a_20
478
>>> ab = 'p'
>>> a_b = 'p'
>>> #Special char. symbols are not allowed at all
>>> #~!@#$%^&*,;"'
>>> $ = 23
SyntaxError: invalid syntax
>>> @ = 30
SyntaxError: invalid syntax
>>> ; =45
SyntaxError: invalid syntax
>>> a$ =34
SyntaxError: invalid syntax
>>> # completely special char are not allowe in between or at the start or at the end
>>> $a = 23
SyntaxError: invalid syntax
>>> a$b = 45
SyntaxError: invalid syntax
>>> _ = 24
>>> _
24
>>> emp_id = 101
>>> emp_id
101
>>> _rollno = 23
>>> _rollno
23
>>> __pin = 1234
>>> __pin
1234
>>> _pin_ = 1234'
SyntaxError: EOL while scanning string literal
>>> _pin_ = 1234
>>> _pin_
1234
>>> __pin__ = 4567
>>> __pin__
4567
>>> pin =1234
>>> _pin
Traceback (most recent call last):
  File "<pyshell#54>", line 1, in <module>
    _pin
NameError: name '_pin' is not defined
>>> _pin =1234
>>> _pin
1234
>>> __pin
1234
>>> __pin__
4567
>>> __pin_=234
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
global
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
global
Traceback (most recent call last):
  File "C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py", line 5, in <module>
    print(obj.x)
AttributeError: 'Test' object has no attribute 'x'
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
global
global
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
Local
Local
global
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
Local
Local
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
Local
Local
Traceback (most recent call last):
  File "C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py", line 22, in <module>
    print(_x)
NameError: name '_x' is not defined
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py ==
Local
Traceback (most recent call last):
  File "C:/Users/Admin/AppData/Local/Programs/Python/Python37/class.py", line 21, in <module>
    print(obj.__x)
AttributeError: 'Test' object has no attribute '__x'
>>> #PEP8 Standards
>>> a  =20
>>> _a = 45
>>> __a = 60
>>> id(a)
8791476131456
>>> id(_a)
8791476132256
>>> id(__a)
8791476132736
>>> a = 20
>>> _a = 20
>>> __a = 20
>>> id(a)
8791476131456
>>> id(_a)
8791476131456
>>> id(__a)
8791476131456
>>> #PEP8 Standards
>>> #Python Enhanced Proposal
>>> # use lowercase letters to give names
>>> # to give function name use lower case
>>> # while using lowercase and there are two words use underscore in between (emp_info)
>>> # while giving the name to class use camelcase
>>> # Class name should be in Title format
>>> #example: class Test:
>>> # while giving the combinition of two word for class name follow camel case
>>> #class CompanyData
>>> #class companydata (this is not stand. one)
>>> x = 100
>>> x=100
>>> import sample2
>>> x
100
>>> 
=============================== RESTART: Shell ===============================
>>> import sample2
>>> x
Traceback (most recent call last):
  File "<pyshell#89>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> sample2.x
10
>>> 
=============================== RESTART: Shell ===============================
>>> from sample2 import y
>>> y
30
>>> x
Traceback (most recent call last):
  File "<pyshell#93>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> 
