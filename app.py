from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

menu = {
    'Pabellón': 8.5, 'Reina pepiada': 10.0, 'Empanada': 12.0, 
    'Arepa': 5.0, 'Tequeños': 7.0, 'Cachapa': 9.5, 
    'Patacón': 11.0, 'Perico': 6.5, 'Tostones': 8.0
}
ventas = {nombre: 0 for nombre in menu.keys()}
pedidos_actuales = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/menu')
def mostrar_menu():
    return render_template('menu.html', menu=menu)

@app.route('/ventas')
def mostrar_ventas():
    return render_template('ventas.html', ventas=ventas)

@app.route('/reset_ventas')
def reset_ventas():
    global ventas
    ventas = {nombre: 0 for nombre in menu.keys()}
    return redirect(url_for('mostrar_ventas'))

@app.route('/agregar_plato')
def agregar_plato():
    return render_template('agregar_plato.html')

@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    menu[nombre] = precio
    ventas[nombre] = 0
    return redirect(url_for('mostrar_menu'))

@app.route('/actualizar_plato/<nombre>')
def actualizar_plato(nombre):
    plato = {'nombre': nombre, 'precio': menu[nombre]}
    return render_template('actualizar_plato.html', plato=plato)

@app.route('/actualizar/<nombre>', methods=['POST'])
def actualizar(nombre):
    precio = float(request.form['precio'])
    menu[nombre] = precio
    return redirect(url_for('mostrar_menu'))

@app.route('/eliminar_plato/<nombre>')
def eliminar_plato(nombre):
    del menu[nombre]
    del ventas[nombre]
    return redirect(url_for('mostrar_menu'))

@app.route('/pedidos')
def pedidos():
    return render_template('pedidos.html', menu=menu, pedidos=pedidos_actuales)

@app.route('/pedidos', methods=['POST'])
def hacer_pedido():
    nombre = request.form['nombre']
    cantidad = int(request.form['cantidad'])
    precio = menu[nombre] * cantidad
    pedidos_actuales.append({'nombre': nombre, 'cantidad': cantidad, 'precio': precio})
    ventas[nombre] += cantidad
    return redirect(url_for('pedidos'))

@app.route('/finalizar_pedido')
def finalizar_pedido():
    global pedidos_actuales
    total = sum(pedido['precio'] for pedido in pedidos_actuales)
    pedidos = pedidos_actuales.copy()  # Crear una copia para mostrar en la factura
    pedidos_actuales = []
    return render_template('factura.html', pedidos=pedidos, total=total)

if __name__ == '__main__':
    app.run(debug=True)
