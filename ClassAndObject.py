class Calculator:
    num = 100
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am called automatically when object is created")
    def getData(self):
        print("I am now executing as method in class")
    def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

obj = Calculator(2,3) #syntax to create object in python
obj.getData()
print(obj.num)

obj1 = Calculator(4,5) #syntax to create object in python
obj1.getData()
print(obj1.Summation())