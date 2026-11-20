from Employee import Employee

class PermanentEmployee(Employee):

    def __init__ (self,name,age, role,basic_salary):
        super().__init__( name,age,role,basic_salary)
    
    def calculate_salary(self):
         salary = (self.basic_salary + self.basic_salary *0.2)
         return salary
    