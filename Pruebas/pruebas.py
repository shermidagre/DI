#Numeros
numEnteiro = 10

print(f"Número enteiro: {numEnteiro}")

#Flotante
numDecimal = 10.5
numDecimal2 = 10.5
print(f"Número decimal: {numDecimal+numDecimal2}")

#Complexos

numComplexo = 2 + 3j
print(f"Número complexo: {numComplexo}")
print(f"Parte real: {numComplexo.real}")
print(f"Parte imaginária: {numComplexo.imag}")


#Booleanos

booleanoTrue = 1
booleanoFalse = 0
print(f"Booleano True: {booleanoTrue}")
print(f"Booleano False: {booleanoFalse}")

#Strings

"""
Fluida maxima  """

nome = "Samuel"
print(f"Nome: {nome}")

print(type (numComplexo));

fraseramdo = "FraseRamdonr"
print(fraseramdo.lower().count("r") & fraseramdo.upper().count("R"))

operacionesrandom = 2**6
print(f"Operaciones random: {operacionesrandom}")

div2 = 10//3
print(f"División para sacar un numero entero: {div2}")

# operaciones arigmetricos << >> ^ & | ~
print(2^3)

#operaciones de booleanos

print(True and False)
print(True or False)
print(not True)

"""Colecciones

    Listas

    Tuplas

    Diccionarios

"""
#Listas
l=[23, 4.20, 16-3j, "albatros", -5, 22,[34,"Manuel"],4>>1,~5]
print(type(l))


l[4]= "marcelo"
l[6]=[1,2,3,4]

print(l[6][-3])#puedes hacer que empiece por la derecha con - delante del nombre de la lista

#Partidas
print(l[2:5])
print(l[4][1:3])
print(l[:-3])
print(l[1:5:2])
print(l[::-1])

#Tuplas

t=(2,5,2+3j, "Alberto",[1,3,4,5,6],6,9) #Elementos inmutables dentro de la tupla
t[4][3]=2
print(t)
t2=5,
print(type(t2)) #Es posible su salida de diferentes formas sin cambiar su contenido

#Condiciones

numeros=[1,2,3,4,5,20,45,67,3,4,5,6,7,8]
for numeros in range(5):
    print(numeros)


"""for indice in range(3,10,3):
    print(numeros[indice])
    """


#Diccionarios
d={1: "uno",2:"dos",3:"tres"}#diccionario

print(d[3])

l2=[1,2,3]#lista
l3=list((1,2,3))#tupla

t2=[1,2,3]
t3=tuple(l3)#Se puede crear tupla con listas
l3[0]=1000
print(t3)
print(t3,l3)

d2={1:"1",2:"11",3:"111"}
d3=dict()#diccionario vacio

l2.append([3,2,1])#inserta el objeto en lista como único elemento
l2.extend([3,2,(2,"Dos","11"),1])#añade como elementos a la lista
l2.insert(3,"Objeto en 4ª lugar")#añade en el lugar el objeto descrito

print(l2.count(3))#busca el elemento y lo cuenta las veces en q se repita

print(l2.index(3,3,7))#busca coincidencias a partir del inicio y fin de la lista
extraer=l2.pop(5)#Quita el valor de la lista en la posicion asignada
l2.remove(3)#elimina la primera coincidencia de la lista
l2.reverse()#invirte la lista
t3=l2[::-1]#la devuelve desinvirtiendola
print("Elemento extraido :",extraer)
print(l2)
print(t3)
