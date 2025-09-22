from symtable import Class


class Persona:
    nombre = ""
    dni = ""
    edad = 0

    def __init__(self, nombre, edad, dni):
        self.nombre = nombre
        self.comprobaredad(edad)
        self.dni = dni
        print(f"Se ha creado la persona {nombre} con DNI {dni}")


    def comer(self,comida):
        print(f"{self.nombre} come {comida}")

    def comprobaredad(self, ed):
        if ed >=  0 and ed <= 100:
            return ed
        else:
            return "Edad incorrecta"


    def comprobarDNI(self, dni):
        if len(dni) == 9 and dni.isdigit():
            return dni
        else:
            return "DNI incorrecto"

def añadirdatos(self, Maisdatos):

    for v,c in Maisdatos.items():
        print(f"Se ha añadido el dato {v} con el valor {c}")
        setattr(self, v, c)

p = Persona("Juan", 25,"123456789")
p.comer("pan")
#p.añadirdatos(direccion="C/ San Francisco", telefono="6666666")
#print(p.direccion)

class posto :
    def __init__(self,tarefa,horario):
        self.tarefa = tarefa
        self.horario = horario

class Traballador(Persona, posto):

    def __init__(self, nombre, edad, dni, salario, formacion, tarefa, horario):
        Persona.__init__(self,nombre, edad, dni)
        posto.__init__(self,tarefa, horario)

        self.salario = salario
        self.formacion = formacion


t = Traballador("asda", 43, "123456789", 2000,"puto random","Trabajando","24 horas")
print(t.formacion)
