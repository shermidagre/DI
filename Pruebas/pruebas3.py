l5=["un","dos","tres","cuatro","cinco"]
l5.sort(key=len)#ordena por tamaño de frase
print(l5)
tabla_alturas=[("Manuel",1.17),("Pepe",2.05),("Ana",1.76)]#tabla de personas con alturas
def altura(persoa):
    return persoa[1]#ordena por altura de menor a mayor

tabla_alturas.sort(key=altura)
print(tabla_alturas)

#Funciones y diccionarios

def saudar (lingua):
    def saudar_es():
        print("Hola")
    def saudar_gl():
        print("Ola")
    def saudar_en():
        print("Hello")
    def saludar_ru():
        print("привет")
    def saludar_ma():
        print("هيلو")
    def saludar_be():
        print("ফলের")
    #diccionario
    func_saudo={"es":saudar_es,#solo hacemos referencia
                "gl":saudar_gl,
                "en":saudar_en,
                "ru":saludar_ru,
                "ma":saludar_ma,
                "be":saludar_be}

    return func_saudo[lingua] #devuelve del diccionario el codigo elegido
f=saudar("ru")#guara la referencia pero no el contenido
print(f)#muestra referencia
f()#desglosa el contenido
saudar("ma")()
saudar("be")()

l6=[1,2,3,4]

def es_par(n):
    return n%2==0
l2= filter(es_par,l6)#compara numeros de l6 con funcion es_par para sacar pares

l2= filter(lambda n: n % 2 == 0, l6)

for n in l2:
    print(n)
#Filtrar y trabajar con listas
#Filter,map,reduce

l3=[n+1 for n in l6]#sumamos uno a cada elemento de l

print(l3)

l4=[n for n in l6 if n%2==0]
print(l4)
m=["=","*"]
z=[]
for s in m:
    for n in l6:
        if n<4:
            z.append(n*s)#añade elementos n veces como elemento menor que cuatro

print(z)

z2=[n*s for s in m
    for n in l6
    if n<4]#forma parecida de hacerlo pero mas compacta
print(z2)


x2=(n**2 for n in l6)#objeto generador de datos

for n in x2:
    print(n)#saca datos elevados a 2

def mi_range(fin,inicio=0,salto=1):
    while inicio<=fin :
        yield inicio #retorna valor pero continua ejecutandose sin salir del bucle
        inicio = inicio + salto

x3=mi_range(inicio=4,fin=99,salto=15) #generador de rango

l7=[n for n in x3]

for n in x3 :
    print(n)#ejecucion de una sola vez
print(l7)

