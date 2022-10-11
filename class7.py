

# three mode - Read(r)/Write(w)/Append(a)

"""

myfile=open("file.txt","r")
print(myfile.read())

myfile1=open("file.txt","w")
myfile1.write("Be motivated. Be the one. ")

myfile2=open("file.txt","r")
print(myfile2.read())

myfile3=open("file.txt","a")
myfile3.write(" Only you can do everything.")

myfile4=open("file.txt","r")
print(myfile4.read())


"""


#context manager

"""

with open("file.txt","r") as file1:
    print(file1.read())

with open("file.txt","w") as file2:
    file2.write("This is using context manager. ")
with open("file.txt","r") as file1:
    print(file1.read())

with open("file.txt","a") as file3:
    file3.write(" This is using context manager. ")
with open("file.txt","r") as file4:
    print(file4.read())
file4.close()



"""

#Assignment

"""
#for r+

with open("file.txt","r") as file1:
   # file1.write("YOYO") #not possible
    print(file1.read())

# using r+

with open("file.txt","r+") as file2:
    print(file2.read())
    file2.write(" YoYo")
    file2.write(" Honey")
    file2.write(" Singh")
    print(file2.read())

"""

#for w+

"""
with open("file.txt","w") as file1:
    file1.write("YOYO")
    # print(file1.read()) #not possible

# using w+

with open("file.txt","w+") as file2:
    file2.write(" YoYo")
    file2.write(" Honey")
    file2.write(" Singh")
    file2.seek(0) #wont work unless moving the pointer
    print(file2.read())


"""


#for a+

"""

with open("file.txt","a") as file1:
    file1.write("YOYO")
    # print(file1.read()) #not possible

# using a+

with open("file.txt","a+") as file2:
    file2.write(" YoYo")
    file2.write(" Honey")
    file2.write(" Singh")
    file2.seek(0) #wont work unless moving the pointer
    print(file2.read())


"""



#Simple calculator
#Assignment

"""

a=int(input())
c=input()
b=int(input())
calc = {"+": a+b, "-": a-b, "*": a*b, "/": a/b, "%": a%b}
z=str(calc[c])
print(z)
with open("calc.txt","a") as file1:
    file1.write(z)
    file1.close()
with open("calc.txt","r") as file1:
    print(file1.read())

"""



"""

import datetime
x=datetime.datetime.now()
print(x)

"""
