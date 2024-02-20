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
    def transform(self):
        print(f'SuperMan: {self.Name} will transform')
    # variable, attribute of class
    power=50
    #class method
    @classmethod
    def classmethod_update_power(cls,power):
        ''' pass '''
        cls.power=power
    @staticmethod
    def staticmethod_SuperMan_Transform():
        ''' pass '''
        print('SuperMan will transform')


    @classmethod
    def from_string(cls,s):
        lst=s.split('-')
        new_lst=[st.strip() for st in lst]
        Name,Weapon,Color=new_lst
        return cls(Name,Weapon,Color)

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
SuperMan.classmethod_update_power(30)
print(SuperMan_A.power)
print(SuperMan.power)
print(SuperMan_A.id)
print(SuperMan_B.id)
print(SuperMan_C.id)
print(SuperMan_A.Hello())
print(SuperMan.Hello(SuperMan_A))

SuperMan_D=SuperMan.from_string('Tèo-Gun-Blue')
print(SuperMan_D.id)
print(SuperMan_D.Name)
print(SuperMan_D.__dict__)
SuperMan.staticmethod_SuperMan_Transform()
SuperMan_A.transform()
SuperMan_B.transform()
SuperMan_C.transform()
SuperMan_D.transform()