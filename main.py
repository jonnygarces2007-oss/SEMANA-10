from servicios.restaurante import Restaurante
from servicios.archivo_servicio import ArchivoServicio
from modelos.producto import Producto
from modelos.usuario import Usuario


# Tupla: opciones fijas del menú
OPCIONES_MENU: tuple = (
    "1. Registrar producto",
    "2. Buscar producto",
    "3. Actualizar producto",
    "4. Eliminar producto",
    "5. Listar productos",
    "6. Registrar usuario",
    "7. Listar usuarios",
    "8. Mostrar categorías",
    "9. Salir"
)


def mostrar_menu() -> None:
    print("\n========================================")
    print("        SISTEMA DE RESTAURANTE")
    print("========================================")
    for linea in OPCIONES_MENU:
        if linea.startswith(("5", "7", "8")):
            print("----------------------------------------")
        print(linea)
    print("========================================")


def guardar_cambios(restaurante: Restaurante) -> None:
    """Guarda la lista actual de productos en JSON tras cada modificación"""
    productos = restaurante.listar_productos()
    if ArchivoServicio.guardar_productos(productos):
        print("💾 Cambios guardados correctamente.")


def registrar_producto(restaurante: Restaurante) -> None:
    print("\n--- Registrar Producto ---")
    try:
        codigo = int(input("Código único: "))
        nombre = input("Nombre: ")
        categoria = input("Categoría: ")
        precio = float(input("Precio: $"))
        nuevo = Producto(codigo, nombre, categoria, precio)
        if restaurante.registrar_producto(nuevo):
            print("✅ Producto registrado.")
            guardar_cambios(restaurante)
        else:
            print("❌ Error: el código ya existe.")
    except ValueError as e:
        print(f"❌ Datos inválidos: {e}")


def buscar_producto(restaurante: Restaurante) -> None:
    print("\n--- Buscar Producto ---")
    try:
        codigo = int(input("Código a buscar: "))
        producto = restaurante.buscar_producto(codigo)
        if producto:
            print("🔍 Encontrado:", producto.mostrar_informacion())
        else:
            print("❌ Producto no encontrado.")
    except ValueError:
        print("❌ El código debe ser un número.")


def actualizar_producto(restaurante: Restaurante) -> None:
    print("\n--- Actualizar Producto ---")
    try:
        codigo = int(input("Código del producto a modificar: "))
        nombre = input("Nuevo nombre: ")
        categoria = input("Nueva categoría: ")
        precio = float(input("Nuevo precio: $"))
        if restaurante.actualizar_producto(codigo, nombre, categoria, precio):
            print("✅ Producto actualizado.")
            guardar_cambios(restaurante)
        else:
            print("❌ Producto no encontrado o datos inválidos.")
    except ValueError:
        print("❌ Datos inválidos.")


def eliminar_producto(restaurante: Restaurante) -> None:
    print("\n--- Eliminar Producto ---")
    try:
        codigo = int(input("Código del producto a eliminar: "))
        if restaurante.eliminar_producto(codigo):
            print("✅ Producto eliminado.")
            guardar_cambios(restaurante)
        else:
            print("❌ Producto no encontrado.")
    except ValueError:
        print("❌ El código debe ser un número.")


def listar_productos(restaurante: Restaurante) -> None:
    print("\n--- Lista de Productos ---")
    productos = restaurante.listar_productos()
    if not productos:
        print("No hay productos registrados.")
        return
    for prod in productos:
        print(prod.mostrar_informacion())


def registrar_usuario(restaurante: Restaurante) -> None:
    print("\n--- Registrar Usuario ---")
    try:
        identificacion = int(input("Identificación: "))
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        nuevo = Usuario(identificacion, nombre, correo)
        if restaurante.registrar_usuario(nuevo):
            print("✅ Usuario registrado.")
        else:
            print("❌ Error: esa identificación ya está registrada.")
    except ValueError:
        print("❌ Datos inválidos.")


def listar_usuarios(restaurante: Restaurante) -> None:
    print("\n--- Lista de Usuarios ---")
    usuarios = restaurante.listar_usuarios()
    if not usuarios:
        print("No hay usuarios registrados.")
        return
    for usu in usuarios:
        print(usu.mostrar_informacion())


def mostrar_categorias(restaurante: Restaurante) -> None:
    print("\n--- Categorías Únicas ---")
    categorias = restaurante.obtener_categorias_unicas()
    if not categorias:
        print("No hay categorías registradas.")
        return
    for cat in categorias:
        print(f"• {cat}")


def salir(restaurante: Restaurante) -> None:
    guardar_cambios(restaurante)
    print("👋 Gracias por usar el sistema. ¡Hasta pronto!")


def main():
    # 🔄 Cargar productos desde JSON al iniciar
    print("🔄 Cargando productos...")
    productos_cargados = ArchivoServicio.cargar_productos()

    restaurante = Restaurante(nombre="Sabor Andino")
    restaurante.cargar_desde_lista(productos_cargados)
    print(f"✅ {len(productos_cargados)} producto(s) cargado(s).")

    # Diccionario: opción → función
    acciones = {
        1: registrar_producto,
        2: buscar_producto,
        3: actualizar_producto,
        4: eliminar_producto,
        5: listar_productos,
        6: registrar_usuario,
        7: listar_usuarios,
        8: mostrar_categorias,
        9: salir
    }

    while True:
        mostrar_menu()
        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in acciones:
                acciones[opcion](restaurante)
                if opcion == 9:
                    break
            else:
                print("⚠️ Opción no válida. Intente nuevamente.")
        except ValueError:
            print("⚠️ Por favor ingrese un número.")


if __name__ == "__main__":
    main()
