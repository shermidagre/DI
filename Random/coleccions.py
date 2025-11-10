"""coleccions

Listas
Tuplas
Diccionarios

"""

#Listas

l = [11,[1,2,2,4],[3,"algo random"],"xd"]
print(l)
print(l[0])
l[0] = "random x2"
print(l)
l.append("nuevo elemento")
print(l)
print(l[-1])

#SLicing
print(l[1:3])
print(l[:5])
print(l[3:])
print(l[::-1])
"""Te lo pone al reves"""

#Tuplas

T = ((2,3,6+3),"un TEXTO","otra cosa",[1,2,3],5)
print(T)
T[3][2] = "random x3"
print(T)

#Diccionarios

d = {1:"uno",2:"dos",3:"tres"}
print(d[2])

#sentencias condicionales
n1 = 5

if n1 > 3:
    print("5 es mayor que 3")
elif n1==0:
    print("xd")
else:
    print("menor que 3")

#operadores ternarios
vehiculo = "turismo" if n1 <= 3 else "moto"
print(vehiculo)



while n1 < 11:
    print(n1)
    n1 += 1

n1 = 5
while True:
    print(n1)
    n1 += 1
    if n1 == 11:
        break


# Bucle for in
print("Listado de numeros con for in:")
for i in range(11):
    print(i)


print("printeo de lista con for in :")

listarandom= [1,2,34,4,75,7457,24,25,25,26,1,63,2,3,734,68,33,2,421,424,62,23757234,8]
for i in listarandom:
        print(i)


print("printeo de diccionario con for in:")

for i in d:
    print(i,":",d[i])



for i in range(3,19,2):# empieza por el 3 y termina en el 18, con salto de 2
   print(listarandom[i])

