# Cree una clase llamada Persona con los siguientes atributos: nombre, fecha de nacimiento (como un string) y cédula de identidad. Luego cree dos clases que herenden de Persona:

# 1. una llamada Estudiante, con un atributo adicional denominado carrera, para indicar que carrera cursa

# 2. otra llamada Profesor, con un atributo adicional denominado asignatura, para indicar la materia que dicta.

# En ambos casos recuerde sobreescribir el método __str__() para mostrar su representación.

# A contininuación instancie dos objetos uno de tipo Estudiante y otro de tipo Profesor, e imprima sus atributos por la pantalla.

class Persona:
    def __init__(self, nombre: str, fecha_nacimiento: str, cedula: str):
        self.nombre = nombre
        self.fecha_nacimiento = fecha_nacimiento
        self.cedula = cedula

    def __str__(self) -> str:
        return f"Nombre: {self.nombre}, Fecha de Nacimiento: {self.fecha_nacimiento}, Cédula: {self.cedula}"

class Estudiante(Persona):
    def __init__(self, nombre: str, fecha_nacimiento: str, cedula: str, carrera: str):
        super().__init__(nombre, fecha_nacimiento, cedula)
        self.carrera = carrera

    def __str__(self) -> str:
        return super().__str__() + f", Carrera: {self.carrera}"

class Profesor(Persona):
    def __init__(self, nombre: str, fecha_nacimiento: str, cedula: str, asignatura: str):
        super().__init__(nombre, fecha_nacimiento, cedula)
        self.asignatura = asignatura

    def __str__(self) -> str:
        return super().__str__() + f", Asignatura: {self.asignatura}"

estudiante = Estudiante("Jamal", "2002-12-15", "12345678", "Ingeniería")
profesor = Profesor("Carlos", "1980-03-22", "87654321", "Matemáticas")

print(estudiante)
print(profesor)