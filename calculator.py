from abc import ABC,abstractmethod
class ICalculator(ABC):
    @abstractmethod
    def add(self):
        pass
    @abstractmethod
    def substract(self):
        pass
    @abstractmethod
    def multiply(self):
        pass
    @abstractmethod
    def divide(self):
        pass
class BasicCalculator(ICalculator):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def substract(self):
        return self.a-self.b
    def multiply(self):
        return self.a*self.b 
    def divide(self):
        return self.a/self.b
ob=BasicCalculator(4,2)
print(ob.add())
print(ob.substract())
print(ob.divide())
print(ob.multiply())   
        