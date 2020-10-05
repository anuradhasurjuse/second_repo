Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> #pYthon literal
>>> # Operators in Python
>>> # When we want to perform a perticular operation we nedd an operator
>>> # when we use operator we require operands(inputs)
>>> #Operation====( Operand , Operator)
>>> # basic 7 types of Operators
>>> #1. Arithmetic Operator: +,-,*,/,%,//(floor div),**(expo)
>>> 1+2
3
>>> 2-1
1
>>> 4*2
8
>>> 4/5
0.8
>>> 4%2
0
>>> 3%2
1
>>> # % gives remainder
>>> 10/3
3.3333333333333335
>>> 10//3
3
>>> # floating number ex 12.33=(12 as floor . as floating point 33 as ceil)
>>> 8/3
2.6666666666666665
>>> 8//3
2
>>> 10/2
5.0
>>> 10//2
5
>>> # ** exponential operator: used as power of--- 2**3 -- 2 to the power of 3
>>> 2**3
8
>>> 4**2
16
>>> 25**25
88817841970012523233890533447265625
>>> #########################
>>> #2. Assignment operators: it can perform the operation and also save the result in the same variable
>>> x = 10
>>> x
10
>>> x+10
20
>>> x
10
>>> # = means as assignment operator
>>> x = x + 10
>>> x
20
>>> # += -= *= /= %= //= **=
>>> x #current x value
20
>>> x+=10 #lets add 10 more and save result in x itself
>>> x
30
>>> 25+=10
SyntaxError: can't assign to literal
>>> x
30
>>> x-=5 # will subtract 5 from 30 and will save result in s itself
>>> x
25
>>> # Perform operations using : *= /= %= //= **=
>>> #3. Conditional or Comparison Operators
>>> # <,>,<=,>=,==, !=
>>> # THese operators gives boolean result---> True / False
>>> 10>2
True
>>> 5<13
True
>>> 5>13
False
>>> 3>=3
True
>>> 4<=3
False
>>> 2 == 2
True
>>> 3 != 2
True
>>> 3 != 3
False
>>> # Conditional operators are used to compare the objects
>>> 2 == 2
True
>>> 2 == 2.0
True
>>> 2.0 == 2.0
True
>>> # Conent equality and Address equality?
>>> id(2)
8791369241664
>>> id(2.0)
767008
>>> id(2)==id(2.0)
False
>>> id(2)==id(2)
True
>>> 2 is 2
True
>>> ##################################
>>> #4. Logical Operators: and or not
>>> # and: when both expressions are True then result is True
>>> #otherwise result is False
>>> True and True
True
>>> True and False
False
>>> False and True
False
>>> False and False
False
>>> 2==2 and 3>2
True
>>> 2!=2 and 3>2
False
>>> # when we use logical operators we get the asnwer in bool
>>> # or: will get True answer for all expression except when both expressions are False
>>> False or False
False
>>> True or True
True
>>> True or False
True
>>> False or True
True
>>> #not: negation
>>> # if input is True then it will result False and vice versa
>>> not True
False
>>> not False
True
>>> not 2==2
False
>>> not 3==2
True
>>> ###############################################
>>> #5. Bitwise Operators:
>>> # &(and) |(or) ^(xor) ~(not/negation) >>(right shift) <<(left shift)
>>> # Bitwise means it works on binary
>>> 7 & 2
2
>>> True & False
False
>>> 1 & 0
0
>>> 1 & 1
1
>>> True & True
True
>>> # or==> |
>>> 0 | 0
0
>>> 1 | 0
1
>>> 0 | 1
1
>>> 1 | 1
1
>>> True | False
True
>>> #xor: it will result True/1 only for either or condition of True and False otherwise result will be False/0
>>> 0 ^ 0
0
>>> False ^ False
False
>>> 1 ^ 0
1
>>> True ^ False
True
>>> 0 ^ 1
1
>>> 1 ^ 1
0
>>> True ^ True
False
>>> ###################
>>> 10 and 7
7
>>> 10 & 7
2
>>> #why?
>>> 
