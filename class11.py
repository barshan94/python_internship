
#polumorphism

"""

class intro():
    def details(self):
        print("This is a negative wishlist. Be aware before reading this.\n")
    def bsize(self):
        print("The standard size is only 34 inches.\n")
class ex1(intro):
    def bsize(self):
        print("The standard size for Neha is only 36 inches.\n")
class ex2(intro):
    def bsize(self):
        print("The standard size for Anu is only 38 inches.\n")
class ex3(intro):
    def bsize(self):
        print("The standard size for Tithi is only 40 inches which is very rare.\n")

neha=ex1()
neha.details()
neha.bsize()

anu=ex2()
anu.details()
anu.bsize()

tithi=ex3()
tithi.details()
tithi.bsize()

"""

#string formatting
"""
%
.format()
fstring
string template class
"""

"""

# % operator

print("Hi my darling, %s . You are so %s and %s too. I wish I could %s you for %s . "%("Neha","cute","hot","spend with","an hour"))

# .format

print("My darling name is {3}. Her Bsize is {1}. Her Ksize is {2}. The most beautiful Hsize is {0}. ".format("40","36","30","Neha"))

# fstring
s1=36
s2=30
s3=40
n1="Neha"
print("I am glad to tell the name of my first darling "+n1+f" . Her Bsize is {s1} . Her Ksize is {s2}. Her Hsize is {s3} .")


# String template class
# Assignment

from string import Template

A= Template("Hi, I am $x. I want to $y with $z.")
print(A.substitute(x="BGB",z="Neha",y="meet"))

details=[("Neha",36,"dark","borolok"),("Anu",38,"white","fokirni"),("Tithi",40,"white","Kotipoti")]
B=Template("Hi, this is $name , and her size is $size. She is $color in nature and very $status.")
for i in details:
    print(B.substitute(name=i[0],size=i[1],color=i[2],status=i[3]))

C= Template("Hi, this is the usage of $name and a method which is $method of $language.")
print(C.safe_substitute(name="Template",method="safe")) #applicable when one $ is undescriable

dollar=Template("$$ is the symbol of ${name}s")
print(dollar.safe_substitute(name="Dollar"))


"""


#python decorator

"""

def increment(num):
    print(num+1)
def decrement(num):
    print(num-1)
def incdec(fun,num):
    print(fun(num))

a=increment(10)
#a(10)
increment(10)
incdec(increment,10)

def Print():
    print("YOYO")
Print()
Print1=Print
Print1()

"""
