ItemsinCart=0

if ItemsinCart!=2:#raise Exception("Nothing happened")
    pass

#assert(ItemsinCart==2)

try:
    with open('txt.txt','r') as reader:
        a=reader.read()
        with open('text.txt','w') as writer:
            for i in reversed(a):
                writer.write(i)
except Exception as e:
    print(e)
finally:
    #Meant for closing the connections or deleting the cookies
    reader.close()
    writer.close()