#funcion
def suma(a,b):
    print(a+b)

    suma(5,7)


def saludo(nombre,edad):
    print(f"Hola {nombre}, tienes {edad} años")

    saludo("Juan",25)

def repetir_mensaje(mensaje,veces):
    for i in range(veces):
        print(mensaje)

    repetir_mensaje("Hola",5)