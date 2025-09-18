class Persona:
    nombre = ""
    dni = ""
    edad = 0

    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
        print(f"Se ha creado la persona {nombre} con DNI {self.dni}")


    def comer(self,comida):
        print(f"{self.nombre} come {comida}")


def añadirdatos(self,Maisdatos):

    for v,c in Maisdatos.items():
        print(f"Se ha añadido el dato {v} con el valor {c}")
        setattr(self, v, c)

p = Persona("Juan", 25,"123456789")
p.comer("pan")
p.añadirdatos(direccion="C/ San Francisco", telefono="6666666")
