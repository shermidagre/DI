# Exercicio 3.1. Escribir dúas funciones que permitan calcular:
# A cantidade de segundos nun tempo dado en horas, minutos e segundos.
# A cantidade de horas, minutos e segundos dun tempo dado en segundos.


print("Exercicio 3.1:")
opcion=input("Elige una opción (1/2): ")
print("1. Quieres pasar de un tiempo en horas minutos y segundos a segundos?")
print("2. Quieres pasar un tempo en segundos a horas, minutos y segundos?")


def horaaseg():
    hora = int(input("Introduce la hora: "))

    if hora == 1:
        strh = "hora"
    else:
        strh = "horas"
    if hora>=24 or hora<0:
        print("La hora debe estar entre 0 y 23")
        return

    minuto = int(input("Introduce los minutos: "))
    if minuto == 1 :
        strm = "minuto"
    else:
        strm = "minutos"

    if minuto>=60 or minuto<0:
        print("Los minutos deben estar entre 0 y 59")
        return

    segundo = int(input("Introduce los segundos: "))
    if segundo == 1:
        strs = "segundo"
    else:
        strs = "segundos"

    segundos = (hora * 3600) + (minuto * 60) + segundo
    print(f" {hora} {strh} {minuto} {strm} {segundo} {strs} son {segundos} segundos.")

def segahora():
    segundos = int(input("Introduce los segundos: "))
    horas = segundos / 3600
    minutos = (segundos % 3600) / 60
    segundosnuevos = segundos % 60
    print(f"Los segundos {segundos} en horas son : {int(horas)} en minutos son : { int(minutos) } y segundos es: {int(segundosnuevos)}")

if (opcion == "1"):
    horaaseg()
elif (opcion == "2"):
    segahora()
else:
    print("Opción no válida")