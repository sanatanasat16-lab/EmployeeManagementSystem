from Employee import Employee

class PermanentEmployee(Employee):        # child class of Employee
 
    def calculate_salary(self):            # to calculate salary of permanent employee
         salary = (self.basic_salary + self.basic_salary *0.2)   # 20 % allowence for permanent employee
         return salary
    