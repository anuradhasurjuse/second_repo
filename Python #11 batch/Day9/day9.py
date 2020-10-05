Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> str()
''
>>> int()
0
>>> float()
0.0
>>> complex()
0j
>>> bool()
False
>>> bin()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    bin()
TypeError: bin() takes exactly one argument (0 given)
>>> list()
[]
>>> tuple()
()
>>> set()
set()
>>> dict()
{}
>>> # above options are used for type casting also and for creating empty data typ/data structure
>>> ########################################################
>>> ############# OUTPUT FORMATTING ####################
>>> # print() function is used for output formatting
>>> help(print)
Help on built-in function print in module builtins:

print(...)
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    
    Prints the values to a stream, or to sys.stdout by default.
    Optional keyword arguments:
    file:  a file-like object (stream); defaults to the current sys.stdout.
    sep:   string inserted between values, default a space.
    end:   string appended after the last value, default a newline.
    flush: whether to forcibly flush the stream.

>>> print()

>>> print(10)
10
>>> print(10);print(20)
10
20
>>> print(10,end=' ');print(20)
10 20
>>> print(10,end='--');print(20)
10--20
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
	print(i,end=' ')

	
0 1 2 3 4 5 6 7 8 9 
>>> for i in range(10):
	print(i,end='\t')#tab

	
0	1	2	3	4	5	6	7	8	9	
>>> print()

>>> print(10,20,30,40,50)
10 20 30 40 50
>>> # sep= ' ' thats why we r getting space btwn two objects
>>> print(10,20,30,40,50,sep='==>')
10==>20==>30==>40==>50
>>> for i in range(10):
	print(i,i**2)

	
0 0
1 1
2 4
3 9
4 16
5 25
6 36
7 49
8 64
9 81
>>> for i in range(10):
	print(i,i**2,sep='::')

	
0::0
1::1
2::4
3::9
4::16
5::25
6::36
7::49
8::64
9::81
>>> for i in range(10):
	print(i,i**2,sep='::',end='\n\n')

	
0::0

1::1

2::4

3::9

4::16

5::25

6::36

7::49

8::64

9::81

>>> name = input('Enter your name:')
Enter your name:Soham
>>> name
'Soham'
>>> place = input('Enter your place:')
Enter your place:Pune
>>> place
'Pune'
>>> print(name,place)
Soham Pune
>>> print('Your name is',name)
Your name is Soham
>>> print('Your name is',name,'and place is',place)
Your name is Soham and place is Pune
>>> ##### Using format function ##########
>>> print('Your name is{}and place is{}'.format(name,place))
Your name isSohamand place isPune
>>> print('Your name is {}and place is {}'.format(name,place))
Your name is Sohamand place is Pune
>>> print('Your name is {} and place is {}'.format(name,place))
Your name is Soham and place is Pune
>>> # in format sequence is important when u r not using positional values
>>> print('Your name is {} and place is {}'.format(place,name))
Your name is Pune and place is Soham
>>> # how to set position
>>> print('Your name is {1} and place is {0}'.format(place,name))
Your name is Soham and place is Pune
>>> # name='prashant' this is keyword argument
>>> print('Your name is {1} and place is {0} , you are{design}'.format(place,name,design='Data Scientist'))
Your name is Soham and place is Pune , you areData Scientist
>>> print('Your name is {1} and place is {0} , you are {design}'.format(place,name,design='Data Scientist'))
Your name is Soham and place is Pune , you are Data Scientist
>>> ###################### Using % operator ################
>>> # while using % we have specify access modifiers
>>> # %d int, %f float, %s string
>>> print('My name is %s, age is %d and salary is %f'%('sham',25,543242.0))
My name is sham, age is 25 and salary is 543242.000000
>>> print('My name is %s, age is %d and salary is %.2f'%('sham',25,543242.1664578))
My name is sham, age is 25 and salary is 543242.17
>>> # if we change sequence of values
>>> # will get error
>>> print('My name is %s, age is %d and salary is %.2f'%(25,543242.1664578,'sham'))
Traceback (most recent call last):
  File "<pyshell#63>", line 1, in <module>
    print('My name is %s, age is %d and salary is %.2f'%(25,543242.1664578,'sham'))
TypeError: must be real number, not str
>>> print('My name is %s, age is %d and salary is %.2f'%(25,543242.1664578,12.50))
My name is 25, age is 543242 and salary is 12.50
>>> print('Value%s'%(23))
Value23
>>> print('Value %s'%(23.45654))
Value 23.45654
>>> print('Value %s'%(23+4j))
Value (23+4j)
>>> print('Value %d'%(23+4j))
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    print('Value %d'%(23+4j))
TypeError: %d format: a number is required, not complex
>>> print('Value %d'%23.34545656)
Value 23
>>> print('Value %d'%23.99545656)
Value 23
>>> print('Value %.f'%23.99545656)
Value 24
>>> d = {'l1':'Python','l2':'DS'}
>>> d
{'l1': 'Python', 'l2': 'DS'}
>>> print('I love {l1} and i am aspiring {l2}'.format(**d))
I love Python and i am aspiring DS
>>> 
