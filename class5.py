#day5

'''
#frozen set is used for not changing rhe list anymore

a=[1,2,3,4,5]
print(a)
a[2]=10
print(a)
b=a
b[1]=100
print(b)
b=frozenset(a)
print(b)
b[1]=100 #doesnot work
print(b)

'''

#function

'''
def sum(num1,num2):
    print("Sum is ",(num1+num2))
sum(100,20)

def sub(num1,num2):
    print("Sub is ",(num1-num2))
sub(100,20)

def mul(num1,num2):
    print("Mul is ",(num1*num2))
mul(100,20)

def div(num1,num2):
    print("Sum is ",(num1/num2))
div(100,20)

item=["Chicken","Fish","Hilisha","Mutton"]
for x in item:
    print(x)

numb=[1,2,3,4,5,6,7,8,9,10]
for i in numb:
    print(i)

x=input()
y=input()
z=int(input())
print("Hi ",x," . Hope that you will shine in life. You are from ",y," batch and your year is ",z)

'''

#done
