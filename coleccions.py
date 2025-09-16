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
