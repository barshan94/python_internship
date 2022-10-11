# class 8


"""

mylist=[1,2,3,4,5,6,2,8]
mylist1=[]
for i in mylist:
    if i%2==0:
        mylist1.append(i)
print(mylist1)
        # mylist1=i
        # print(mylist1)


#comphresion

# list comphresion

mylist2=[i for i in mylist if i%2 ==0]
print(mylist2)

"""

"""

mylist=[1,2,3,4,5,6,2,8]
mylist1={}
for i in mylist:
    mylist1[i]=i**3
print(mylist1)

# dictionary comphresion

mylist2={i:i**3 for i in mylist}
print(mylist2)

"""

"""
mylist=(1,2,3,4,5,6,2,8)
mylist1=set()
for i in mylist:
    if i%2==0:
        mylist1.add(i)
print(mylist1)


mylist2={i for i in mylist if i%2 ==0}
print(mylist2)

"""

#iteration

"""

mylist=[1,2,3,4,5,6,2,8]
myiter=iter(mylist)
print(next(myiter))
print(next(myiter))

"""

"""
mylist=[1,2,3,4,5,6,2,8]
myiter=iter(mylist)
for i in mylist:
    print(next(myiter))


"""

#generator

"""
def cal(x):
    yield x+10
    yield x-1
    yield x*2
for i in cal(7):
    print(i)

"""
