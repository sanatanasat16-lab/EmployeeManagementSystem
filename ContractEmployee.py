
from Employee import Employee

class ContractEmployee(Employee):

    def __init__ (self,name,age, role,basic_salary):
        super().__init__(name,age,role,basic_salary)
         
    def calculate_salary(self):
        return  (self.basic_salary + (self.basic_salary * 0.05))