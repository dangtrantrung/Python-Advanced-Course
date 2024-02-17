def my_func(x,y):
    return x+y
print(my_func(4,6))

my_func1=lambda x,y: x+y
print(my_func1(3,4))

# sort list
lst=["Huy", "hoi dan IT","CodeXplore","Coding AI", "Mi AI","Trung AI"]
print(sorted(lst))
print(sorted(lst,key=lambda x:len(x)))

