"""x = 'global'
class Test:
    print(x)
obj = Test()

print(x)"

x = 'global'
class Test:
    x ='Local'
    print(x)
obj = Test()
print(obj.x)
print(x)
"""
#x = 'global'
class Test:
    __x ='Local'
    print(__x)
obj = Test()
print(obj.__x)
#print(__x)
#print(x)
















