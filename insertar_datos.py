import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('finanzas_personales.db')
cursor = conn.cursor()

# Insertar un usuario
cursor.execute('''INSERT INTO usuarios (nombre, correo, contrasena)
                  VALUES ('Juan Pérez', 'juan.perez@example.com', '12345')''')

# Obtener el ID del usuario insertado
usuario_id = cursor.lastrowid

# Insertar una transacción
cursor.execute('''INSERT INTO transacciones (usuario_id, fecha, categoria, monto, tipo, descripcion)
                  VALUES (?, '2025-02-04', 'Alimentación', 100.50, 'Gasto', 'Compra supermercado')''', (usuario_id,))

# Confirmar cambios y cerrar conexión
conn.commit()
conn.close()

print("✅ Datos insertados correctamente.")
