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

print("-----------------------------")

sqlprofesores = """
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY,
        nombre varchar
    )
"""
sqlusuarios = """
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre text
    )
"""
try:
    bd.execute(sqlprofesores)
    bd.execute(sqlusuarios)
    print("tablas creadas")
except dbapi.StandartError:
    print("error al crear las tablas")


#bd.execute("""insert into profesores values (2,"profe2")""")





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