from ClassAndObject import Calculator
class InheritanceConcept(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 2, 10)
    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()

obj2 = InheritanceConcept()
print(obj2.getCompleteData())

