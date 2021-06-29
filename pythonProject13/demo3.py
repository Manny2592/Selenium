##MAin class


class calculator:
    num=100

    def __init__(self,a,b):
        print("I am inside the class")
        self.a=a
        self.b=b

    def mul(self,a):
        return calculator.num*a

    def Summation(self):
        return (self.a+self.b)




obj=calculator(5,10)

print(obj.mul(10))
print(obj.Summation())