from typing import List, Optional, Set
from modelos.producto import Producto
from modelos.usuario import Usuario


class Restaurante:
    """Clase de servicio: administra colecciones y operaciones"""

    def __init__(self, nombre: str):
        self.nombre = nombre
        self._productos: List[Producto] = []
        self._usuarios: List[Usuario] = []

    # ------------------- Carga inicial desde archivo -------------------
    def cargar_desde_lista(self, lista_productos: List[Producto]) -> None:
        """Agrega productos cargados desde JSON evitando códigos duplicados"""
        for prod in lista_productos:
            if not self._codigo_producto_existe(prod.codigo):
                self._productos.append(prod)

    # ------------------- Validaciones -------------------
    def _codigo_producto_existe(self, codigo: int) -> bool:
        return any(prod.codigo == codigo for prod in self._productos)

    def _id_usuario_existe(self, identificacion: int) -> bool:
        return any(usu.identificacion == identificacion for usu in self._usuarios)

    # ------------------- Operaciones de Productos -------------------
    def registrar_producto(self, producto: Producto) -> bool:
        if self._codigo_producto_existe(producto.codigo):
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo: int) -> Optional[Producto]:
        return next((prod for prod in self._productos if prod.codigo == codigo), None)

    def actualizar_producto(self, codigo: int, nombre_nuevo: str, categoria_nueva: str, precio_nuevo: float) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False
        try:
            producto.nombre = nombre_nuevo.strip().capitalize()
            producto.categoria = categoria_nueva.strip().capitalize()
            producto.precio = round(float(precio_nuevo), 2)
            return True
        except ValueError:
            return False

    def eliminar_producto(self, codigo: int) -> bool:
        producto = self.buscar_producto(codigo)
        if not producto:
            return False
        self._productos.remove(producto)
        return True

    def listar_productos(self) -> List[Producto]:
        return list(self._productos)

    # ------------------- Operaciones de Usuarios -------------------
    def registrar_usuario(self, usuario: Usuario) -> bool:
        if self._id_usuario_existe(usuario.identificacion):
            return False
        self._usuarios.append(usuario)
        return True

    def listar_usuarios(self) -> List[Usuario]:
        return list(self._usuarios)

    # ------------------- Conjunto: categorías únicas -------------------
    def obtener_categorias_unicas(self) -> Set[str]:
        return {prod.categoria for prod in self._productos}
