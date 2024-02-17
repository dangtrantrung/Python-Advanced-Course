print(f'__name__ in the module_main.py:{__name__}')

print(f'My running file name is {__name__}')

def func (a,b):
    print('a+b= ',a+b)

''' func(4,5)
 '''
# conditional statement name=='main' exclude funcs when import modules

if __name__=='__main__':
    func(4,6)
