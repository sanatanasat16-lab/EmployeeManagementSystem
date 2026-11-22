from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name, age, role, basic_salary):
        self.name = name
        self.age = age
        self.role = role
        self.__basic_salary = basic_salary

    def display_details(self):
        print(f'{self.name} {self.age} {self.role} {self.__basic_salary}')
        
    @property
    def basic_salary(self):            # property decorator to access private variable __basic_salary
        return self.__basic_salary
    
    @abstractmethod                  # abstract method to calculate salary of employee
    def calculate_salary(self):
        pass 

