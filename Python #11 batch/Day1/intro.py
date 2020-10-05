Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> print('Hello')
Hello
>>> print('Hello
	  
SyntaxError: EOL while scanning string literal
>>> print('Hello world')
	  
Hello world
>>> x = 100
	  
>>> type(x)
	  
<class 'int'>
>>> x = 'A'
	  
>>> type(x)
	  
<class 'str'>
>>> x = 21.33
	  
>>> type(x)
	  
<class 'float'>
>>> x = 2+4j
	  
>>> type(x)
	  
<class 'complex'>
>>> 
=============================== RESTART: Shell ===============================
>>> x
	  
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> y
	  
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    y
NameError: name 'y' is not defined
>>> import sample
	  
>>> x
	  
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x
NameError: name 'x' is not defined
>>> from sample import x,y
	  
>>> x
	  
10
>>> y
	  
'python'
>>> x = 100
	  
>>> y = 'python'
	  
>>> y
	  
'python'
>>> y = 'python
	  
SyntaxError: EOL while scanning string literal
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample.py ==
10
python
Hello
500
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample.py ==
10
python
Hello
500
>>> x = 400
	  
>>> x
	  
400
>>> x
	  
400
>>> 
== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/sample.py ==
10
python
Hello
500
>>> x
	  
10
>>> print('Hello')
	  
Hello
>>> print('hello');print('Good Morning')
	  
hello
Good Morning
>>> print('Hi');x=100;print(x)
	  
Hi
100
>>> if True:
	  print('Hello')

	  
Hello
>>> if 10>2:
    print('10 greater')
print('End....')
	  
SyntaxError: invalid syntax
>>> 
=== RESTART: C:/Users/Admin/AppData/Local/Programs/Python/Python37/test.py ===
10 greater
End....
>>> for i in range(10):
	  print(i)

	  
0
1
2
3
4
5
6
7
8
9
>>> for i in range(10):
	  print(i)
print('Completed')
	  
SyntaxError: invalid syntax
>>> for i in range(10):
	  print(i)
	  print('Completed')

	  
0
Completed
1
Completed
2
Completed
3
Completed
4
Completed
5
Completed
6
Completed
7
Completed
8
Completed
9
Completed
>>> print()
	  

>>> Print()
	  
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    Print()
NameError: name 'Print' is not defined
>>> p
