
#file=open('text.txt')

##Reading nly the first two characters or bytes
#a=file.read(2)
#print(a)
##nice to close the file
#file.close()

##Reading full file
#a=file.read()

##Reading full file line by line
#a=file.readline()
#print(a)

##Reading full file line by line
#a=file.readlines()
#for i in a:
#    print(i)


file =open('text.txt')
a=[]
#line=file.readline()
line=file.readline()
while line!="":
    print(line)
    line=file.readline()


#with open('text.txt','r') as file:

#with open('text.txt','w') as file:


with open('text.txt','r') as reader:
    a=reader.readlines()
    with open('text.txt','w') as writer:
        for i in reversed(a):
            writer.write(i)