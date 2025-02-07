import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('finanzas_personales.db')
cursor = conn.cursor()

# Consultar todos los usuarios
cursor.execute("SELECT * FROM usuarios")
usuarios = cursor.fetchall()

# Consultar todas las transacciones
cursor.execute("SELECT * FROM transacciones")
transacciones = cursor.fetchall()

# Mostrar los resultados
print("Usuarios:", usuarios)
print("Transacciones:", transacciones)

# Cerrar conexión
conn.close()
