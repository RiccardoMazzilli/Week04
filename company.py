from employee import Employee
from manager import Manager
from car import Car


e1 = Employee("Mr. Bean", 15000)

print(e1)

m = Manager("B. Boss", 40000, "HR")

print(m)

print("----Incremento della paga----")
e1.increment_wage()
print(e1)
m.increment_wage()
print(m)

print("**** Struttura dati ****")
users = []
users.append(e1)
users.append(m)

# DUCK TYPING
users.append("abcdefg")
users.append(35)
car1 = Car("AB123CD", "Red", "False")
users.append(car1)


for user in users:
    print(str(user))
