# 🛍️ Sistema Integrado de Búsqueda de Productos

## 📋 Descripción General
Este programa permite realizar **búsquedas simples** dentro de una lista de productos tecnológicos (teléfonos y computadores).  
El usuario puede buscar productos por **nombre**, **ID**, **categoría**, **marca**, **rango de precios** o **disponibilidad**.  
Además, cuenta con un **menú interactivo** que facilita la navegación y permite salir del sistema cuando se desee.

---

## ⚙️ Funcionalidades Principales

### 🧭 Menú Principal
Al ejecutar el programa, se muestra un menú con varias opciones de búsqueda:
1. Buscar producto por nombre  
2. Buscar producto por ID  
3. Buscar productos por categoría  
4. Buscar productos disponibles (stock > 0)  
5. Buscar productos por rango de precios  
6. Buscar productos por marca  
7. Contar productos en una categoría  
8. Salir del programa  

Cada opción ejecuta una búsqueda específica y muestra los resultados en pantalla.

---

## 💻 Instrucciones de Uso

1. **Ejecuta el programa** en tu entorno de Python (por ejemplo, VS Code, PyCharm o IDLE).  
2. Se mostrará el menú principal.  
3. **Escribe el número de la opción** que deseas usar y presiona Enter.  
4. Según la opción, el programa pedirá información adicional (por ejemplo, nombre del producto, ID, rango de precios, etc.).  
5. El resultado de la búsqueda aparecerá en pantalla.  
6. Puedes repetir el proceso tantas veces como quieras.  
7. Para **salir del programa**, elige la opción **8**.

---

## 📦 Datos de Ejemplo
El programa contiene una lista predefinida de **15 productos tecnológicos**, como:
- Teléfonos de marcas como Samsung, Apple, Xiaomi, Motorola, etc.  
- Computadores de marcas como Dell, HP, Lenovo, Acer, Asus, entre otras.  

Cada producto tiene los siguientes campos:
```python
{
    'id': 1,
    'nombre': 'Samsung Galaxy S22',
    'categoria': 'telefono',
    'marca': 'Samsung',
    'precio': 3500000,
    'stock': 10
}
