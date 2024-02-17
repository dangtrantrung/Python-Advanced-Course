import module_main

print(f'My current running module file name is {__name__}')

def my_func(c,d):
    print('c-d= ',c-d)

# conditional statement name=='main' can exclude not expectative funcs when import modules
if __name__=='__main__':
    my_func(10,4)
    module_main.func(4,5)