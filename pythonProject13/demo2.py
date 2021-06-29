##List , tuple and dictionary

values=[1, 2, 3]
print(values)
print(values[0])
values.insert(3,1)
values.sort()
values.append(7)


print(values[1:2])


d=(1,2,"Anirudh",4)

print(d[1:3])
e=(values)
print(e)

dic={"a":2, "d":3,"c":"HELLO"}

print(dic)
print(dic["c"])


dic["c"]="Rahul"
print(dic)

dic.values()
a=dic.keys()
print(type(e))
dic.popitem()
print(dic)




if a=="Good Morning":
    print("Matching Matching")
else:
    print("No Matching")



a=[1,2,3,4]

c=[]
for i in a:
    c.append(i)

print(c)


a=[1,2,3,4,5,6,7,8,9]

b=10
c=[]
while b>=0:
    if b==0:
        break
    elif b>=1:
        c.append(b)
        b-=1
        continue

print(c)


a=[1,2,3,4,5]


r=10

while r>1:
    if r==0:
        break
    elif r>=1:
        print(r*2)
        r-=1
        continue


def GreetMe(a,b):

    print(a+b)


def AddIntegers(a,b):
    return(a+b)


print(AddIntegers("hey","hola"))

GreetMe(10,20)












