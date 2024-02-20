#import itertools

class SuperMan:
    id_generator = 0
    #constructor, inittailize method
    def __init__(self,para_name,para_weapon,para_color):
        SuperMan.id_generator+=1
        self.Name=para_name
        self.Weapon=para_weapon
        self.Color=para_color
        self.id = SuperMan.id_generator
    def Hello (self):
        print("My power is: ", self.power)
        return "Hello, My name is: " + self.Name
    # variable, attribute of class
    power=50
    
SuperMan_A=SuperMan("Trung","Sword","Red")
SuperMan_B=SuperMan("Trung 1","Sword","Red")
SuperMan_C=SuperMan("Trung 2","Sword","Red")


''' SuperMan_A.Name="Trung"
SuperMan_A.Weapon="Sword"
SuperMan_A.Color="Red" '''
print("Name of SuperMan_A:",SuperMan_A.Name)
print("Weapon of SuperMan_A:",SuperMan_A.Weapon)
print("Color of SuperMan_A:",SuperMan_A.Color)
# print("Color of SuperMan_A:",SuperMan_A.Age)
print(SuperMan_A.Hello())
print(SuperMan.Hello(SuperMan_A))
print(SuperMan_A.power)
print(SuperMan.power)
#change attribute of class, all instance will update attribute value,...# c#:static variable
SuperMan.power=40
print(SuperMan_A.power)
print(SuperMan.power)
print(SuperMan_A.id)
print(SuperMan_B.id)
print(SuperMan_C.id)
print(SuperMan_A.Hello())
print(SuperMan.Hello(SuperMan_A))