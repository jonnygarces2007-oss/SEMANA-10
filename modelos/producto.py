class Producto:
    """Clase que representa un producto del restaurante con soporte para conversión a diccionario"""

    def __init__(self, codigo: int, nombre: str, categoria: str, precio: float):
        if not isinstance(codigo, int) or codigo <= 0:
            raise ValueError("El código debe ser un número entero positivo.")
        if not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")
        if not isinstance(precio, (int, float)) or precio <= 0:
            raise ValueError("El precio debe ser mayor a cero.")

        self.codigo = codigo
        self.nombre = nombre.strip().capitalize()
        self.categoria = categoria.strip().capitalize()
        self.precio = round(float(precio), 2)

    def mostrar_informacion(self) -> str:
        return (f"Código: {self.codigo} | Nombre: {self.nombre} | "
                f"Categoría: {self.categoria} | Precio: ${self.precio:.2f}")

    def to_dict(self) -> dict:
        """Convierte el objeto a diccionario para guardarlo en JSON"""
        return {
            "codigo": self.codigo,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "precio": self.precio
        }

    @classmethod
    def from_dict(cls, datos: dict):
        """Crea un objeto Producto a partir de un diccionario"""
        return cls(
            codigo=datos["codigo"],
            nombre=datos["nombre"],
            categoria=datos["categoria"],
            precio=datos["precio"]
        )
