
from datetime import date

class Employee:
    raise_rate = 1.2
    employee_count = 0

    def __init__(self, name, salary=2000):
        self.name = name
        self.salary = int(salary)
        Employee.employee_count += 1

    def display_info(self):
        return f"Name: {self.name} Salary: {self.salary}"

    @classmethod
    def get_employee_count(cls):
        return cls.employee_count

    @classmethod
    def from_string(cls, data_str):
        name, salary = data_str.split("-")
        return cls(name, int(salary))

    @classmethod
    def from_birth_year(cls, name, birth_year):
        calculated_salary = date.today().year - birth_year
        return cls(name, calculated_salary)

    def apply_raise(self):
        self.salary = int(self.salary * self.raise_rate)

    @staticmethod
    def calculate_birth_year(age):
        return date.today().year - age


# --- Instances and Tests ---
emp1 = Employee("Ali", 2500)
emp2 = Employee("Ahmet", 4500)

emp3 = Employee.from_string("Ayse-5000")
emp4 = Employee.from_birth_year("Fatma", 1990)
emp5 = Employee.from_string("Selman-8000")

print(emp1.display_info())
print(emp2.display_info())
print(emp3.display_info())
print(f"Total Employees: {Employee.employee_count}")
print(f"Count from ClassMethod: {Employee.get_employee_count()}")
print(f"Emp4 Details: {emp4.name}, {emp4.salary}")
print(emp5.display_info())

# Applying Raises
emp1.raise_rate = 2.2
emp2.raise_rate = 1.1
emp1.apply_raise()
emp2.apply_raise()

print(f"Emp1 New Salary: {emp1.salary}")
print(f"Emp2 New Salary: {emp2.salary}")
print(f"Birth Year Calculation: {Employee.calculate_birth_year(34)}")

