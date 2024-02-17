def my_func(x,y):
    return x+y
print(my_func(4,6))

my_func1=lambda x,y: x+y
print(my_func1(3,4))

# sort list
lst=["Huy", "hoi dan IT","CodeXplore","Coding AI", "Mi AI","Trung AI"]
print(sorted(lst))
print(sorted(lst,key=lambda x:len(x)))

#filter (func, iterable)
lst=[1,2,3,4,5,9,8,10]
new_lst=list(filter(lambda x: x%2==0,lst))
print(new_lst)

#map(func,iterable)
lst=[1,23,45,67,8]
new_lst=map(lambda x:x+3,lst)
print(list(new_lst))

#reduce (func,iterable)
from functools import reduce

lst=[(1,23,2,3,45,67),(45,67,8,2,3,23)]
new_lst=reduce(lambda x,y: x.union(y),lst,set())
print(new_lst)