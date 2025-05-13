# Cree una clase base llamada Employee con atributos name, employee_id y salary. Luego, cree subclases para diferentes tipos de empleados (por ejemplo, Gerente, Desarrollador, Vendedor). Cada subclase debe tener atributos y métodos adicionales específicos para su rol.

# Recuerde sobreescribir el método __str__() para mostrar su representación.

# A contininuación instancie objetos de tipo Gerente, Desarrollador y otro de tipo Vendedor, e imprima sus atributos por la pantalla.

# Copie su código y péguelo en el lugar indicado. Revise que la indentación quedó bien configurada.

class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary

    def __str__(self):
        return f"Name: {self.name}, ID: {self.employee_id}, Salary: {self.salary}"


class Manager(Employee):
    def __init__(self, name, employee_id, salary, department):
        super().__init__(name, employee_id, salary)
        self.department = department

    def __str__(self):
        return super().__str__() + f", Department: {self.department}"


class Developer(Employee):
    def __init__(self, name, employee_id, salary, programming_language):
        super().__init__(name, employee_id, salary)
        self.programming_language = programming_language

    def __str__(self):
        return super().__str__() + f", Programming Language: {self.programming_language}"


class Salesperson(Employee):
    def __init__(self, name, employee_id, salary, region):
        super().__init__(name, employee_id, salary)
        self.region = region

    def __str__(self):
        return super().__str__() + f", Region: {self.region}"


manager = Manager("Jose", 101, 75000, "HR")
developer = Developer("Jamal", 102, 65000, "Python")
salesperson = Salesperson("Randy", 103, 50000, "Sudamerica")

print(manager)
print(developer)
print(salesperson)