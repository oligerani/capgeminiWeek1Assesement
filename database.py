#Define an abstract class `IDatabaseOperations` with methods `insert()`, `update()`, and `delete()`. Implement this in `SQLDatabase` and `NoSQLDatabase`.
from abc import ABC,abstractmethod
class IDatabaseOperations(ABC):
    
    @abstractmethod
    def insert(self):
        pass
    
    @abstractmethod
    def update(self):
        pass
    @abstractmethod
    
    def delete(self):
        pass
class SQLDatabase(IDatabaseOperations):
    def __init__(self,data):
        self.data=data
        
    def insert(self):
        
        return f'the data is added {self.data}'
    def update(self):
        
        return f'the data is updated {self.data}'
    def delete(self):
        
        return f'the data is removed {self.data}' 
class NoSQLDatabase(IDatabaseOperations):
    def __init__(self,data):
        self.data=data
        
    def insert(self):
        
        return f'the data is added {self.data}'
    def update(self):
        
        return f'the data is updated {self.data}'
    def delete(self):
        
        return f'the data is removed {self.data}'
ob=NoSQLDatabase("user data")
print(ob.insert())
print(ob.delete())
print(ob.update()) 
  
       