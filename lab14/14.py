from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

class Senior(Employee):
    def calculate_bonus(self):
        return self.salary * 0.1

class Middle(Employee):
    def calculate_bonus(self):
        return self.salary * 0.05
class Junior(Employee):
    def calculate_bonus(self):
        return self.salary * 0.02
def calculate_employee_bonus(employees):
    for employee in employees:
        print(f"{employee.name} отримує бонус: {employee.calculate_bonus()}")

employees = [
    Senior("Юрій", 5000),
    Middle("Юра", 3000),
    Junior("Георгій", 1000),
]

calculate_employee_bonus(employees)
