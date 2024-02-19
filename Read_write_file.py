filename=input("Please enter your file name need to backup: ")
bak_filename=filename +'.bak'

with open(bak_filename,'w') as file:
    for line in open(filename+'.txt','r'):
        file.write(line)


#2
list_alkaline_metals=[]
for line in open('alkaline_metals.txt'):
    line = line.strip()
    print(line)
    list=line.split()
    print(list)
    list_alkaline_metals.append(list)
print(list_alkaline_metals)
