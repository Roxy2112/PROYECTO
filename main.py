import sys
import os

# Agregar la ruta del proyecto al sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'restaurante')))

from models.menu import Restaurante
from crud.crud_restaurante import CRUDRestaurante

def esperar_para_continuar():
    input("\nPresiona Enter para volver al menú principal...")

def main():
    restaurante = Restaurante()
    crud = CRUDRestaurante(restaurante)
    
    # Agregar algunos platos predefinidos
    crud.crear_plato("Pabellon", 8.50)
    crud.crear_plato("Reina pepiada", 10.00)
    crud.crear_plato("Empanada", 12.00)
    crud.crear_plato("Arepa", 5.00)
    crud.crear_plato("Tequeños", 7.00)
    crud.crear_plato("Cachapa", 9.50)
    crud.crear_plato("Patacón", 11.00)
    crud.crear_plato("Perico", 6.50)
    crud.crear_plato("Tostones", 4.50)
    crud.crear_plato("Jugo de guayaba", 3.00)
    
    while True:
        print("\n" + "=" * 40)
        print("            🌟 Opciones del Restaurante 🌟")
        print("=" * 40)
        print("1. ➕ Agregar Plato al Menú")
        print("2. 🔍 Leer Plato del Menú")
        print("3. ✏️ Actualizar Plato del Menú")
        print("4. 🗑️ Eliminar Plato del Menú")
        print("5. 📜 Mostrar Menú")
        print("6. 🛒 Tomar Pedido")
        print("7. 📊 Mostrar Ventas")
        print("8. 🔄 Restablecer Ventas")
        print("9. ❌ Salir")
        print("=" * 40)

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            nombre = input("Nombre del plato: ")
            precio = float(input("Precio del plato: "))
            crud.crear_plato(nombre, precio)
            print(f"✅ El plato '{nombre}' se ha agregado de forma exitosa.")
            esperar_para_continuar()
        elif opcion == '2':
            nombre = input("Nombre del plato a leer: ")
            plato = crud.leer_plato(nombre)
            print(plato)
            esperar_para_continuar()
        elif opcion == '3':
            nombre = input("Nombre del plato a actualizar: ")
            nuevo_precio = float(input("Nuevo precio del plato: "))
            crud.actualizar_plato(nombre, nuevo_precio)
            print(f"✏️ El plato '{nombre}' se ha actualizado de forma exitosa.")
            esperar_para_continuar()
        elif opcion == '4':
            nombre = input("Nombre del plato a eliminar: ")
            crud.eliminar_plato(nombre)
            print(f"🗑️ El plato '{nombre}' se ha eliminado de forma exitosa.")
            esperar_para_continuar()
        elif opcion == '5':
            restaurante.mostrar_menu()
            esperar_para_continuar()
        elif opcion == '6':
            restaurante.tomar_pedido()
            esperar_para_continuar()
        elif opcion == '7':
            restaurante.mostrar_ventas()
            esperar_para_continuar()
        elif opcion == '8':
            confirmar = input("¿Estás seguro de que deseas restablecer todas las ventas a cero? (si/no): ").strip().lower()
            if confirmar == 'si':
                restaurante.ventas = {plato: 0 for plato in restaurante.ventas}
                print("🔄 Todas las ventas se han restablecido a cero.")
            else:
                print("❌ Operación cancelada.")
            esperar_para_continuar()
        elif opcion == '9':
            break
        else:
            print("❌ Opción no válida. Por favor, intenta de nuevo.")
            esperar_para_continuar()

if __name__ == "__main__":
    main()
