
from ContractEmployee import ContractEmployee        # importing class ContractEmployee
from PermanentEmployee import PermanentEmployee       # importing Class PermanentEmployeee

employee1 = PermanentEmployee('Darsana', 24, 'Engineer', 100000)
employee2 = ContractEmployee('Jaya',22,'Data Analyst',100000)

print('salary of Permanent Employee is ' ,employee1.calculate_salary())    
print('salary of Contract Employee is ' ,employee2.calculate_salary())         

employee1.display_details()      # displayng the details of the Permanent employee
employee2.display_details()      # displaying the details of the Contract employees
