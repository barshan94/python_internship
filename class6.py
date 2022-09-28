#class 6

'''
#positional argument
print("Enter your name : ")
x=input()
print("Enter your batch : ")
y=input()
print("Enter the year : ")
z=int(input())
print("Hi ",x,".Hope that you will shine in life. You are from ",y," batch and your year is ",z,".")
'''

'''
#keyword argument

def greet(x,y,z):
    print("Hi ",x,".Hope that you will shine in life. You are from ",y," batch and your year is ",z,".")
greet("BGB","Sep",2022)
greet("Sep","BGB",2022)  #positional arfument
greet(y="Sep",x="BGB",z=2022)  #key arfument
greet("BGB",z=2022,y="Sep")  #key & positional arfument mix

'''

'''
#default argument

def grt(x="Amit",y="AUg",z=2021):
    print("Hi ",x,".Hope that you will shine in life. You are from ",y," batch and your year is ",z,".")
grt()
grt("Piyal","Jan",2022)

'''

# *a for positional argument
# **a for keyword argument

'''

def assign(teacher,*a):
    print(teacher," is assigned for all the students.")
    print("All the student list are : ")
    for i in a:
        print(i)
assign("Mr.Bauya","rahim","Karim","Shila","Choiti","Cinmoyee","Sornali","Sonali","Tushee","Neha","Astha","Sneha","Sithi","Madhobi")

print("For extra class list of these students are invited : ")

'''

'''
def home(x, **a):
    print("Teacher name is ",x,". He is assigned for taking extra class.")
    for i in a:
        print(i,a[i])
home("Barshan",Tithi="2 hours",Goldi="3 hours",Trishna="5 hours",Neha="12 hours",Cinmoyee="30 minutes")

'''

'''
#sequence

a="pineapple"
print("pineapple" in a)
print("pi" in a)
print("pineapple" not in a)
print("apple" not in a)

print(a.index("p"))
print(a.index("p",1))
print(a.index("p",6))
print(a.index("e",1,6))

'''
