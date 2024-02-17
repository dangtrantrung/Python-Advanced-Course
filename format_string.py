name='trung'
weight=6.2
# string module operator
my_string='my name is %s, weight is %s' %(name,weight)
my_string1='my name is %s, weight is %.3f' %(name,weight)

print(my_string)
print(my_string1)


''' Format string '''
loc="TP.HCM"
my_string2=f'my name is {name}, weight is {weight:.3f}. I am from {loc}'
print(my_string2)

''' Template String '''
from string import Template

my_string3=Template('my name 3 is $name, weight is $weight. I am from $loc')

print(my_string3.safe_substitute(name='tèo',weight=45,loc='ha nội'))
