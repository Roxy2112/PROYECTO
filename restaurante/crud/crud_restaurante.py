from models.menu import Restaurante    

class CRUDRestaurante:
    def __init__(self, restaurante):
        self.restaurante = restaurante

    def crear_plato(self, nombre, precio):
        self.restaurante.agregar_plato(nombre, precio)

    def leer_plato(self, nombre):
        if nombre in self.restaurante.menu:
            precio = self.restaurante.menu[nombre]
            ventas = self.restaurante.ventas[nombre]
            return {"nombre": nombre, "precio": precio, "ventas": ventas}
        else:
            print(f"El plato '{nombre}' no está en el menú.")
            return None

    def actualizar_plato(self, nombre, nuevo_precio):
        if nombre in self.restaurante.menu:
            self.restaurante.menu[nombre] = nuevo_precio
            print(f"El precio de '{nombre}' ha sido actualizado a ${nuevo_precio:.2f}")
        else:
            print(f"El plato '{nombre}' no está en el menú.")

    def eliminar_plato(self, nombre):
        if nombre in self.restaurante.menu:
            del self.restaurante.menu[nombre]
            del self.restaurante.ventas[nombre]
            print(f"El plato '{nombre}' ha sido eliminado del menú.")
        else:
            print(f"El plato '{nombre}' no está en el menú.")
