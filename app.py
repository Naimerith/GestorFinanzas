from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)

# Necesario para usar el flash
app.secret_key = 'mi_clave_secreta'
 
# Crear la tabla si no existe
def crear_tabla():
    conn = sqlite3.connect('finanzas.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS gastos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad REAL,
            descripcion TEXT,
            categoria TEXT,
            fecha TEXT
        )
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/agregar', methods=['GET', 'POST'])
def agregar():
    if request.method == 'POST':
        cantidad = request.form['cantidad']
        descripcion = request.form['descripcion']
        categoria = request.form['categoria']  # Nuevo campo
        fecha = request.form['fecha']  # Nuevo campo
        
        # Conectar a la base de datos SQLite
        conn = sqlite3.connect('finanzas.db')
        c = conn.cursor()
        
        # Insertar el nuevo gasto en la base de datos
        c.execute('''
            INSERT INTO gastos (cantidad, descripcion, categoria, fecha)
            VALUES (?, ?, ?, ?)
        ''', (cantidad, descripcion, categoria, fecha))
        
        conn.commit()
        conn.close()
        
        # Mostrar mensaje de éxito con flash
        flash('Gasto registrado correctamente')
        
        # Redirigir a la página de ver gastos
        return redirect(url_for('ver_gastos'))
    # Calcular el total gastado
    conn = sqlite3.connect('finanzas.db')
    c = conn.cursor()
    c.execute('SELECT COALESCE(SUM(cantidad), 0) FROM gastos')  # Si no hay datos, devuelve 0
    total_gastado = c.fetchone()[0]
    conn.close()

    return render_template('agregar.html', total_gastado=total_gastado)
    #return render_template('agregar.html')

@app.route('/ver_gastos')
def ver_gastos():
    # Conectar a la base de datos
    conn = sqlite3.connect('finanzas.db')
    c = conn.cursor()
    c.execute('SELECT cantidad, descripcion, categoria, fecha FROM gastos')
    gastos = c.fetchall()
    conn.close()
    
    return render_template('ver_gastos.html', gastos=gastos)

if __name__ == '__main__':
    crear_tabla()
    app.run(debug=True)
