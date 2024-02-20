class SuperMan:
    #constructor, inittailize method
    def __init__(self,para_name,para_weapon,para_color):
        self.Name=para_name
        self.Weapon=para_weapon
        self.Color=para_weapon
    def Hello (self):
        return "Hello, My name is: " + self.Name
    # variable, attribute of class
    power=50
SuperMan_A=SuperMan("Trung","Sword","Red")
''' SuperMan_A.Name="Trung"
SuperMan_A.Weapon="Sword"
SuperMan_A.Color="Red" '''
print("Name of SuperMan_A:",SuperMan_A.Name)
print("Weapon of SuperMan_A:",SuperMan_A.Weapon)
print("Color of SuperMan_A:",SuperMan_A.Color)
# print("Color of SuperMan_A:",SuperMan_A.Age)
print(SuperMan_A.Hello())
print(SuperMan.Hello(SuperMan_A))
