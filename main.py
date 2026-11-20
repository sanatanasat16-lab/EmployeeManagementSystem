
from ContractEmployee import ContractEmployee
from PermanentEmployee import PermanentEmployee

employee1 = PermanentEmployee('Darsana', 24, 'Engineer', 100000)
employee2 = ContractEmployee('Jaya',22,'Data Analyst',100000)

print('salary is ' ,employee1.calculate_salary())
print('salary is ' ,employee2.calculate_salary())
employee1.display_details()
employee2.display_details()
