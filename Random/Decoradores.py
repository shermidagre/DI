#Decoradores
#Añadir funcionalidad sin tocar la original

def mi_decorador(funcion_origen):
    def funcion_envolvente():
        print("Intrucciones antes de funcion original")
        funcion_origen()
        print("Instrucciones para despues de funcion origen")
    return funcion_envolvente

@ mi_decorador #otra forma de hacerlo
def funcion_necesita_decoracion():
    print("precio decoracion")


#funcion_necesita_decoracion= mi_decorador(funcion_necesita_decoracion)#Se emplea para realizar pruebas previas y posteriores
funcion_necesita_decoracion()

autenticado = False

def requiere_autenticacion(funcioon):
    def funcion_decorada(*args ,**kwargs):
        if autenticado:
            return funcioon(*args,**kwargs)
        else:
            print("Necesitas iniciar sesion")
    return funcion_decorada


def sauda ():
        print("Hola")

requiere_autenticacion(sauda())