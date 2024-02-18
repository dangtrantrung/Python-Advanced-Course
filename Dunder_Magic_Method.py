class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __del__(self):
        print("object is being decontructed!")

p=Person("Mike",40)
del p

class Vector:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def __add__(self,other):
        return Vector(self.x+other.x,self.y+other.y)
v1=Vector(10,20)
v2=Vector(50,60)
v3=v1.__add__(v2)
v4=v1+v2
print(v3.x,v3.y)
print(v4.x,v4.y)