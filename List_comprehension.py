import itertools

# create normal list
lst=[1,2,3,45,6,7,7,1,2,3]
new_lst=[]
for x in lst:
    new_lst.append(x)
print(new_lst)

# List Comprehension
# [expression for item in iterable if condition==True]
new_list_comp=[x for x in lst]
print(new_list_comp)
new_list_comp=[x**2 for x in lst]
print(new_list_comp)
even_ints=[x for x in lst if x%2==0]
print(even_ints)
odd_ints=[x for x in lst if x%2==1]
print(odd_ints)
''' apply function for each element in iterable
[expression1 if condition ==True else expression 2 for iten in iterable] '''

new_list_comp=[x if x%2==0 else x+2 for x in lst]
print(new_list_comp)

# Dictionary Comprehension
# {k:v for item in iterable}
new_dict={k:k**2 for k in lst}
print(new_dict)

# Set Comprehension
# {item for item in iterable}
my_string="MymmmMis"
new_set={letter for letter in my_string}
print(new_set)

# Practice
''' nested list - Multiple loops '''
nested_lst=[[i for i in range(5)] for _ in range(5)]
print(nested_lst)

arr_2d=[
    [1,2,3],
    [3,5,6],
    [7,7,8]
]
flatten_lst=[num for row in arr_2d for num in row]
print(flatten_lst)

# import itertools
list2d = [[1,2,3], [4,5,6], [7], [8,9]]
merged = list(itertools.chain(*list2d))
print(merged)
