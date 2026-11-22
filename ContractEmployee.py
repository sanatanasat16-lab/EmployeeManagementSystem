
from Employee import Employee       # using Employee class from Employee.py file

class ContractEmployee(Employee):  # child class of Employee
         
    def calculate_salary(self):        # to calculate salary of contract employee
        return  (self.basic_salary + (self.basic_salary * 0.05))     # 5% allowance for contract employee