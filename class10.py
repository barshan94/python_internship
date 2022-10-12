
#oop

"""

class spec():
    processor="Ryzen"
    Ram="8 GB"
    Graphics="2 GB"

ob1=spec()
print(ob1.processor,ob1.Ram,ob1.Graphics)
ob1.processor="Intel"
print(ob1.processor,ob1.Ram,ob1.Graphics)


"""

#inheritance

"""

class spec():
    bsize=36
    hsize=38
    ksize=24

class add(spec):
    def __init__(self,color,height):  #part of instances
        self.color=color
        self.height=height

Neha=add("dark","65")
Neha.bsize=36
print(Neha.bsize)
print(Neha.hsize)
print(Neha.ksize)
print(Neha.color)
print(Neha.height)
print("\n")
Tithi=add("White","67")
Tithi.bsize=38
print(Tithi.bsize)
print(Tithi.hsize)
print(Tithi.ksize)
print(Tithi.color)
print(Tithi.height)


"""

#Encapsulation

"""

class details():
  #  def __init__(self, username, password):
    def __init__(self,username,password):
        self.username=username
        self.__password=password
    def show(self):
        print(self.__password)

bgb=details("badhan","123456")
print(bgb.username)
print(bgb.show())
print(bgb.password) #cannot execute


"""
