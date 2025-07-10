#ARITHMETIC OPERATORS (+,-,*,/,%)

a=2
b=4
c=a+b
print(c)

#ASSINGMENT OPERATORS (=,+=,-=,*=,/=)

a=4*4
a+=4
a-=8
print(a)

#COMPARISON OPERATOR (<,>,<=,>=,!=,==) 
#Always returns boolean

a = 5<4
b=5>4
c=5>=4
print(a)
print(b)
print(c)

#LOGICAL OPERATOR

#For 'or' either one of the two or both should be True to get true.
#Only when both are false, false is returned
print("True or False is",True or False)
print("False or True is",False or True)
print("True or True is",True or True)
print("False or False is",False or False)

#For 'and' both the values should be True to get True
#If, even one of them is False, False will be returned
print("True and False is",True and False)
print("False and True is",False and True)
print("True and True is",True and True)
print("False and False is",False and False)

#For 'not', it turns true to false and false to true
print(not(True))
print(not(False))
