#class 9

#exception handling
#if found an exception in the try block it wont go inn the next condiotion

"""

try:
    a=[1,2,36,5,6,8]
    print(a[2])
    a+"do"
except:
    print("An error occured")
finally:
    print("The task has been run at least once")

try:
    print(5+2)
    print(5/0)
    print(2+3)
except:
    print("An error occured")
finally:
    print("The task has been run at least once.")

#raising an error

try:
    raise NameError("Data is not present")
except:
    print("There is an error")
    raise
# finally:    #cant use if use error will not raise
#     print("The task has been analyzed")


"""

"""

# Regular Expression
# search,sub,split,findall

import re
a="Hi . I am BGB. My date of birth is 20-01-2001. I am 21 years old. My expected income is 999999."
b=re.search("Hi",a)
print(b)
c=re.sub("\s","whitespace",a)
print(c)
d=re.sub("\d","forteen",a)
print(d)
e=re.split("\d",a)
print(e)
e=re.split("\d+",a)  #for merging all digit together
print(e)
f=re.findall("\d",a)
print(f)
g=re.findall("\d+",a)
print(g)
h=re.findall("\d\d-\d\d-\d\d\d\d",a)
print(h)


"""

# Lambda function used for declare and work in function in the same line

"""

a=lambda x:x+7
print(a(5))
b=[lambda x=x:x**3 for x in range(1,10)]  #when using range the last number will not execute
for y in b:
    print(y())

c=lambda a,b,c: print("Triagonometry") if (c**2==(a**2 + b**2)) else print("Not")
print(c(3,4,5))

"""
