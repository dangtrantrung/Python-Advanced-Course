#serialize and deserialize bython object

import pickle

dict={
    'name':'Trung',
    'age':40,
    'job':'dev AI'
}
# save python object to pickle file
# with open('save.pickle','wb') as stream:
#     pickle.dump(dict,stream) # save AI models .h5 to byte in pick file

# # load content from pickle file to txt

# with open('save.pickle', 'rb') as stream:
#      my_dict=pickle.load(stream)
# print(my_dict)
# print(type(my_dict))

pickle_obj=pickle.dumps(dict)
new_dict=pickle.loads(pickle_obj)
print(new_dict)