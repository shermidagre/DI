from symtable import Class

"""
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
"""



class Persona3:

    def __init__(self, nombre, edad, dni):
        self.__nombre = nombre
        self.__edad= self.setedad(edad)
        self.__dni = dni

    def setnombre(self, nombre):
        self.__nombre = nombre

    def getnombre(self):
        return self.__nombre

    def getedad(self):
        return self.__edad

    def setedad(self, id):
        if id >=  0 and id < 100:
            self.__edad = id
        else:
            self.__edad = 0

    def getdni(self):
        return self.__dni

    def setdni(self, dni):
        if isinstance(dni, str) and len(dni) == 9:
            self.__dni = dni
        else:
            self.__dni = "ER"

    nombre = property(getnombre,setnombre)
    edad = property(getedad,setedad)
    dni = property(getdni, setdni)

t = Persona3("Juan", 25,"123456789")

t.dni = "aposjdas"
print(t.dni)

"""

class Persona2:
    nombre = ""
    dni = ""
    edad = 0

    def __init__(self, nombre, edad, dni, **outros):
        self.nombre = nombre
        self.edad=self.comprobaredad2(edad)
        self.dni = dni

  def comprobaredad2(self, edad):
        if edad >=  0 and edad <= 100:
            return edad
        else:
            return "Edad incorrecta"

class posto2 :
    def __init__(self,tarefa,horario,renumeracion,formacion, **outros):
        self.tarefa = tarefa
        self.horario = horario
        self.renumeracion = renumeracion
        self.formacion = formacion

class Traballador2(Persona2, posto2):

    def __init__(self, nombre, edad, dni, salario, formacion, tarefa, horario,NUSS):

        super().__init__(nombre= nombre, edad=edad, dni=dni, tarefa = tarefa, horario=horario, formacion=formacion)
        self.salario = salario
        self.NUSS = NUSS




 Traballador2 = Traballador2("asda", 43, "123456789", 2000,"puto random","Trabajando","",23)

 print(Traballador2.formacion)
"""
