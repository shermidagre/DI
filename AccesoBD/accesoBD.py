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


bd.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY,
        nombre TEXT
    )
""")


#bd.execute("insert into usuarios (id, nombre) ""VALUES (?, ?)", (3,"random3"))





bd.execute("SELECT * FROM usuarios")
resultados = bd.fetchall()
print("-----------------------------")
print(resultados)
print("-----------------------------")



# Guardar los cambios
bdd.commit()
bdd.close()