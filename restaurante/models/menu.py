class Restaurante:
    def __init__(self):
        self.menu = {}
        self.ventas = {}

    def agregar_plato(self, nombre, precio):
        self.menu[nombre] = precio
        self.ventas[nombre] = 0

    def registrar_venta(self, nombre, cantidad):
        if nombre in self.menu:
            self.ventas[nombre] += cantidad
        else:
            print(f"El plato '{nombre}' no está en el menú.")

    def mostrar_menu(self):
        print("=" * 40)
        print("          🌟 Menú del Restaurante 🌟")
        print("=" * 40)
        for i, (nombre, precio) in enumerate(self.menu.items(), start=1):
            print(f"{i}. {nombre:<25} ${precio:>8.2f}")
        print("=" * 40)

    def mostrar_ventas(self):
        print("=" * 40)
        print("          🛒 Ventas Registradas 🛒")
        print("=" * 40)
        for nombre, cantidad in self.ventas.items():
            if cantidad > 0:
                ingreso = cantidad * self.menu[nombre]
                print(f"{nombre:<25} {cantidad:>5} vendidos, ingreso total: ${ingreso:>8.2f}")
        total_ingresos = sum(cantidad * self.menu[nombre] for nombre, cantidad in self.ventas.items())
        print("=" * 40)
        print(f"Ingreso total del día: ${total_ingresos:>8.2f}")
        print("=" * 40)

    def tomar_pedido(self):
        pedido = {}
        while True:
            self.mostrar_menu()
            eleccion = input("Escribe el número del plato que deseas ordenar (o 'fin' para terminar): ")
            if eleccion.lower() == 'fin':
                break
            if eleccion.isdigit():
                eleccion = int(eleccion)
                if 1 <= eleccion <= len(self.menu):
                    plato = list(self.menu.keys())[eleccion - 1]
                    cantidad = int(input(f"¿Cuántas unidades de '{plato}' deseas? "))
                    if plato in pedido:
                        pedido[plato] += cantidad
                    else:
                        pedido[plato] = cantidad
                    self.registrar_venta(plato, cantidad)
                    print(f"Has añadido {cantidad} unidades de '{plato}' a tu pedido.")
                else:
                    print("Número de plato no válido.")
            else:
                print("Entrada no válida, por favor ingresa un número.")
            
            continuar = input("¿Deseas pedir algo más? (si/no): ").strip().lower()
            if continuar != 'si':
                break

        total = sum(self.menu[plato] * cantidad for plato, cantidad in pedido.items())
        print("=" * 40)
        print("          🧾 Resumen del Pedido 🧾")
        print("=" * 40)
        for plato, cantidad in pedido.items():
            costo = self.menu[plato] * cantidad
            print(f"{plato:<25} {cantidad:>5} unidades, costo: ${costo:>8.2f}")
        print("=" * 40)
        print(f"Total a pagar: ${total:>8.2f}")
        print("=" * 40)
