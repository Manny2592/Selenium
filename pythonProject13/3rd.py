##Inherited classs

from demo3 import calculator


class third(calculator):

    def __init__(self):
        calculator.__init__(self,2,10)

    def getCompleteData(self):
        return self.Summation()+self.a+self.b

obj1=third()
print(obj1.getCompleteData())










