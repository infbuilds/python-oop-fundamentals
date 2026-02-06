class Employee:
    raise_rate = 1.1

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary
        self.email = f"{first_name.lower()}.{last_name.lower()}@email.com"

    def get_details(self):
        return "Name: {} {} Salary: {} \nEmail: {}".format(self.first_name, self.last_name, self.salary, self.email)


# Employee Instances
emp1 = Employee("jesse", "kentry", 9000)
emp2 = Employee("Ayse", "Demir", 6000)
emp3 = Employee("Fatma", "Kara", 7000)


class Developer(Employee):
    def __init__(self, first_name, last_name, salary=15000, language="Python"):
        super().__init__(first_name, last_name, salary)
        self.language = language

    raise_rate = 1.2

    def get_details(self):
        return "Name: {} {} Salary: {} Email: {} \nLanguage: {}".format(self.first_name, self.last_name, self.salary, self.email, self.language)

    def get_language(self):
        return f"Programming Language: {self.language}"


# Developer Instances
dev1 = Developer("WALTER", "WHİLE", 11000000000, "Python, C++, CSS, HTML")
dev2 = Developer("John", "Kaya", 7000, "Java")

# Output Section
print("-" * 30)
print("Employee Information:")
print(emp1.get_details())
print(emp2.get_details())
print(emp3.get_details())

print("-" * 30)
print("Developer Information:")
print(dev1.get_details())
print(dev1.get_language())
print("-" * 30)
print(dev2.get_details())
print(dev2.get_language())

