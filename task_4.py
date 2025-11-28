class EmployeeSalary:
    
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email
    
    def salary(self):
        salary = self.hours * self.hourly_payment
        return f"Имя: {self.name}, Отработанные часы: {self.hours}, Почта: {self.email}, Зарплата: {salary}"

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)
    
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_hourly_payment):
        cls.hourly_payment = new_hourly_payment

employee1 = EmployeeSalary('Петров',8,6,'petrov@email.com')
employee2 = EmployeeSalary.get_email('Петров',8,6)
employee3 = EmployeeSalary.get_hours('Петров',3,'petrov@email.com')
EmployeeSalary.set_hourly_payment(2000)

print (employee1.salary())    
print (employee2.salary())   
print (employee3.salary()) 
