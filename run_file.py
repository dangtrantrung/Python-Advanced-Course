# # read file
# file_obj=open('myfile.txt',encoding="utf-8") # rt
# content=file_obj.read()
# print(content)
# file_obj.close() # auto Garbage collection

# context manager - dont need to close file,...action
# with open('myfile.txt',encoding='utf-8') as file:
#     # content=file.read()
#     content=file.readline()
#     print(content)

# with open('write_file.txt','a',encoding='utf-8') as f:
#     f.write('\n Bạn làm nghề gì???')
# with open('write_file.txt','a',encoding='utf-8') as f:
#      f.write('\nBạn học gì???')

with open('create_new_file.txt','x',encoding='utf-8') as f:
    pass

