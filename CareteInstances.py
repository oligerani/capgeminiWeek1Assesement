from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def work(self) ->str:
        pass
    @abstractmethod
    def get_salary(self) ->float:
        pass
    
    
    def display(self):
        print(f'the employee name is {self.name} and salary is {self.salary}')
class Manger(Employee):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"work of employee with name{self.name} is manager")   
    def get_salary(self):
        print(self.salary)        
class Developer(Employee):
    def __init__(self,name:str,salary:float):
        self.name=name
        self.salary=salary
    def work(self):
        print(f"work of employee with name{self.name} developer")   
    def get_salary(self):
        print(self.salary)    
class Department:
    def __init__(self):
        self.department=[]
    
    def hire(self, employee: Employee):
        self.department.append(employee)

    def fire(self, emp: Employee):
        if emp in self.department:
            self.department.remove(emp)    
    
    def display_all(self):
        for i in self.department:
            i.display()    
    def expenses(self):
        total=0
        for j in self.department:
            total+= j.salary
        return total               
m=Manger("ammu",25000)
d=Developer("anu",50000)
dd=Department() 
 
dd.hire(m)
dd.hire(d)
print("employee details")
dd.display_all()               
print("total salary expenses")
t=dd.expenses()
print(t)