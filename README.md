# SEMANA-10

#  Sistema de Gestión de Restaurante - Semana 10

**Asignatura:** Programación Orientada a Objetos  
**Estudiante:** JONNY JAVIER GARCES ALMEIDA 
**Fecha:** Agosto 2026

---

## Objetivo
Incorporar **persistencia de datos en formato JSON** para los productos, manejo de excepciones específico y separación clara entre lógica de negocio y manejo de archivos. Los productos se conservan aunque se cierre el programa.

---

## 📁 Estructura del proyecto
restaurante_app/
├── datos/
│ └── productos.json ← Archivo generado automáticamente
├── modelos/
│ ├── producto.py ← Entidad, conversión a diccionario
│ └── usuario.py ← Entidad (en memoria esta semana)
├── servicios/
│ ├── archivo_servicio.py ← Lectura y escritura JSON
│ └── restaurante.py ← Lógica de negocio y colecciones
├── main.py ← Menú, carga inicial y coordinación
└── README.md
plaintext

---

##  ¿Cómo funciona la persistencia?

### Flujo de carga (al iniciar)
1. `main.py` pide a `ArchivoServicio` que lea `datos/productos.json`
2. Se lee el archivo con `json.load()` y codificación UTF-8
3. Cada diccionario recuperado se convierte en **objeto Producto** mediante `Producto.from_dict()`
4. Los objetos se entregan al servicio `Restaurante` y se trabajan normalmente

### Flujo de guardado (al modificar)
1. Al registrar, actualizar o eliminar → se modifica la lista en memoria
2. La colección de objetos se convierte en **lista de diccionarios** con `to_dict()`
3. Se escribe el archivo con `json.dump()` con formato legible
4. El archivo queda actualizado y disponible al reiniciar

---

##  Excepciones controladas específicamente

| Excepción | Situación | Respuesta del programa |
|---|---|---|
| `FileNotFoundError` | Primera ejecución, archivo aún no existe | Inicia con lista vacía sin error |
| `JSONDecodeError` | Archivo existe pero está dañado o vacío | Inicia con lista vacía y avisa |
| `PermissionError` | Sin permisos de lectura o escritura | Avisa y continúa en memoria |
| `KeyError` | Falta un campo en algún registro almacenado | Omite ese registro y avisa, continúa |
| `ValueError` | Datos inválidos en un registro | Omite ese registro y avisa, continúa |

---

## Comprobación de persistencia real
Para verificar que funciona:
1. Ejecuta: `python main.py`
2. Registra un producto nuevo
3. Verifica que `datos/productos.json` fue creado con esa información
4. Cierra el programa (opción 9)
5. Vuelve a ejecutarlo y lista productos
6.  El producto aparece sin volver a ingresarlo
7. Modifícalo o elimínalo, cierra y reinicia
8.  Los cambios también se conservan

---

##  Ejecución
```bash
python main.py
 La carpeta datos/ debe existir antes de la primera ejecución. El archivo productos.json se genera automáticamente al guardar el primer producto.
 Reflexión
La persistencia convierte objetos a diccionarios antes de guardarlos y los reconstruye al leer. Esto permite que el programa trabaje siempre con objetos (no con diccionarios directamente), mientras el archivo JSON actúa solo como medio de almacenamiento. Manejar excepciones específicas evita que problemas esperados —como la ausencia del archivo— detengan toda la aplicación.
plaintext

---

## Cumplimiento de requisitos
-  Estructura modular con carpeta `datos/` y servicio `archivo_servicio.py`
-  Conversión bidireccional: `Producto ↔ dict` mediante métodos de clase
-  Carga automática al iniciar y guardado tras cada modificación
-  Las 5 excepciones solicitadas controladas de forma específica
-  `main.py` coordina pero no administra directamente las listas
- Los productos se conservan al cerrar y reiniciar
-  Usuarios permanecen en memoria (no se pide su persistencia aún)
