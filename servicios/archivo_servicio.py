import json
from typing import List
from modelos.producto import Producto


RUTA_ARCHIVO = "datos/productos.json"


class ArchivoServicio:
    """Servicio encargado únicamente de leer y escribir productos en JSON"""

    @staticmethod
    def cargar_productos() -> List[Producto]:
        """
        Lee productos.json y reconstruye objetos Producto.
        Maneja excepciones específicas para no detener el programa.
        """
        productos: List[Producto] = []
        try:
            with open(RUTA_ARCHIVO, mode="r", encoding="utf-8") as archivo:
                registros = json.load(archivo)

            for registro in registros:
                try:
                    producto = Producto.from_dict(registro)
                    productos.append(producto)
                except KeyError as e:
                    print(f"⚠️ Registro incompleto, falta el campo: {e} — se omite.")
                except ValueError as e:
                    print(f"⚠️ Registro con datos inválidos: {e} — se omite.")

        except FileNotFoundError:
            print("ℹ️ Archivo productos.json no encontrado. Se inicia con lista vacía.")
        except json.JSONDecodeError:
            print("⚠️ El archivo JSON tiene formato incorrecto. Se inicia con lista vacía.")
        except PermissionError:
            print(f"❌ Sin permiso para leer {RUTA_ARCHIVO}. Se inicia con lista vacía.")
        except Exception as e:
            print(f"⚠️ Error inesperado al leer archivo: {e}")

        return productos

    @staticmethod
    def guardar_productos(productos: List[Producto]) -> bool:
        """Convierte objetos a diccionarios y los guarda en formato JSON"""
        try:
            registros = [prod.to_dict() for prod in productos]
            with open(RUTA_ARCHIVO, mode="w", encoding="utf-8") as archivo:
                json.dump(registros, archivo, indent=4, ensure_ascii=False)
            return True
        except PermissionError:
            print(f"❌ Sin permiso para escribir en {RUTA_ARCHIVO}.")
        except Exception as e:
            print(f"⚠️ Error al guardar archivo: {e}")
        return False
