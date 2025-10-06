import sqlite3 as dbapi

print("-----------------------------")
print(dbapi.apilevel)
print("Comparticion de modulo:", dbapi.threadsafety)
print(dbapi.paramstyle)
print("-----------------------------")

try:
    bdd = dbapi.connect('baseDatos.dat')
    print(bdd)
except dbapi.StandartError:
    print("error al abrir la base de datos")

try:
    bd = bdd.cursor()
    print(bd)
except dbapi.StandartError:
    print("error al crear el cursor")

sql = """
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY,
        nombre varchar
    )
"""

bd.execute(sql)


#bd.execute("insert into profesores (id, nombre) ""VALUES (?, ?)", (1,"profe1"))





bd.execute("select * from usuarios")
usuarios = bd.fetchall()

bd.execute("select * from profesores")
profesores = bd.fetchall()

print("-----------------------------")

print("\n=== PROFESORES ===")
for p in profesores:
    print(p)

print("\n-----------------------------")

print("\n=== USUARIOS ===")
for u in usuarios:
    print(u)

print("\n-----------------------------")




# Guardar los cambios
bdd.commit()
bdd.close()