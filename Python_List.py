celegants_phenoltype=['Emb','Him','Unc','Lon','Dpy','Sma']
for e in celegants_phenoltype:
    print(e)
for e in celegants_phenoltype:
    print(e,end=" ")

whales=[5,4,6,7,8,9]
new_whales=[x+1 for x in whales]
print(new_whales)
alkaline_earth_metals=[
    [4,9.012],
    [12,24.305],
    [20,40.078],
    [38,87.62],
    [56,137.372],
    [88,226]
]
print(alkaline_earth_metals,end=None)
for e in alkaline_earth_metals:
    print(e[0])
    print(e[1])
number_and_weight=[]
for e in alkaline_earth_metals:
    number_and_weight.append(e[0])
    number_and_weight.append(e[1])
print(number_and_weight)
# 2
flatten_lst=[num for row in alkaline_earth_metals for num in row]
print(flatten_lst)

def mystery_function(values):
    '''(list)->list
    Return a copy of a list, value and the sublist it contains
    The top- level sublist have their element reversed
    in the returned list
    >>>mystery_function([[1,2,3],[4,5,6]])
    [[3,2,1],[6,5,4]]
    '''
    result=[]
    for sublist in values:
        # copy the element in reverse
        # order by inserting each element in sublist to
        # the front of result
        result.append([sublist[0]])
        for i in sublist[1:]:
            result[-1].insert(0,i)
    return result
help(mystery_function)
print(mystery_function([[1,2,3],[4,5,6]]))
