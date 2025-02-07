import sqlite3

# Crear una conexión a la base de datos (la base de datos se creará si no existe)
conn = sqlite3.connect('finanzas_personales.db')

# Crear un cursor para ejecutar comandos SQL
cursor = conn.cursor()

# Crear la tabla de usuarios (por ejemplo, para almacenar la información de los usuarios)
cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nombre TEXT NOT NULL,
                    correo TEXT UNIQUE NOT NULL,
                    contrasena TEXT NOT NULL)''')

# Crear la tabla de transacciones (para las finanzas)
cursor.execute('''CREATE TABLE IF NOT EXISTS transacciones (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    usuario_id INTEGER,
                    fecha TEXT NOT NULL,
                    categoria TEXT NOT NULL,
                    monto REAL NOT NULL,
                    tipo TEXT NOT NULL,
                    descripcion TEXT,
                    FOREIGN KEY (usuario_id) REFERENCES usuarios (id))''')

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("✅ Base de datos y tablas creadas con éxito.")
