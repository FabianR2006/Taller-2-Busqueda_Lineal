productos = [
    {'id': 1, 'nombre': 'Laptop Lenovo', 'marca': 'Lenovo', 'categoria': 'Computadores', 'precio': 3200, 'stock': 5, 'disponible': True},
    {'id': 2, 'nombre': 'iPhone 13', 'marca': 'Apple', 'categoria': 'Telefonos', 'precio': 4200, 'stock': 2, 'disponible': True},
    {'id': 3, 'nombre': 'Samsung Galaxy S22', 'marca': 'Samsung', 'categoria': 'Telefonos', 'precio': 3500, 'stock': 0, 'disponible': False},
    {'id': 4, 'nombre': 'Laptop HP Pavilion', 'marca': 'HP', 'categoria': 'Computadores', 'precio': 2800, 'stock': 3, 'disponible': True},
    {'id': 5, 'nombre': 'iPad Air', 'marca': 'Apple', 'categoria': 'Tablets', 'precio': 2500, 'stock': 4, 'disponible': True},
    {'id': 6, 'nombre': 'Mouse Logitech', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 120, 'stock': 10, 'disponible': True},
    {'id': 7, 'nombre': 'Teclado Razer', 'marca': 'Razer', 'categoria': 'Accesorios', 'precio': 300, 'stock': 0, 'disponible': False},
    {'id': 8, 'nombre': 'Monitor Samsung 24"', 'marca': 'Samsung', 'categoria': 'Monitores', 'precio': 800, 'stock': 5, 'disponible': True},
    {'id': 9, 'nombre': 'Laptop Acer Aspire', 'marca': 'Acer', 'categoria': 'Computadores', 'precio': 2600, 'stock': 6, 'disponible': True},
    {'id': 10, 'nombre': 'Huawei P50', 'marca': 'Huawei', 'categoria': 'Telefonos', 'precio': 3100, 'stock': 3, 'disponible': True},
    {'id': 11, 'nombre': 'Tablet Samsung Tab S7', 'marca': 'Samsung', 'categoria': 'Tablets', 'precio': 2700, 'stock': 2, 'disponible': True},
    {'id': 12, 'nombre': 'MacBook Pro', 'marca': 'Apple', 'categoria': 'Computadores', 'precio': 5200, 'stock': 1, 'disponible': True},
    {'id': 13, 'nombre': 'Teclado Logitech', 'marca': 'Logitech', 'categoria': 'Accesorios', 'precio': 150, 'stock': 8, 'disponible': True},
    {'id': 14, 'nombre': 'iPhone 12', 'marca': 'Apple', 'categoria': 'Telefonos', 'precio': 3800, 'stock': 4, 'disponible': True},
    {'id': 15, 'nombre': 'Monitor LG UltraWide', 'marca': 'LG', 'categoria': 'Monitores', 'precio': 900, 'stock': 0, 'disponible': False}
]

empleados = [
    {'id': 101, 'nombre': 'Samuel', 'apellido': 'Arias', 'departamento': 'Ventas', 'salario': 35000, 'activo': True},
    {'id': 102, 'nombre': 'Fabian', 'apellido': 'Rodas', 'departamento': 'Tecnico', 'salario': 42000, 'activo': True},
    {'id': 103, 'nombre': 'Daniel', 'apellido': 'Carmona', 'departamento': 'Ventas', 'salario': 38000, 'activo': False},
    {'id': 104, 'nombre': 'Laura', 'apellido': 'Martinez', 'departamento': 'Inventario', 'salario': 30000, 'activo': True},
    {'id': 105, 'nombre': 'Andres', 'apellido': 'Gomez', 'departamento': 'Administracion', 'salario': 50000, 'activo': True}
]


def buscar_producto_por_nombre(lista, nombre):
    return [p for p in lista if nombre.lower() in p['nombre'].lower()]

def buscar_producto_por_id(lista, id_buscar):
    return [p for p in lista if p['id'] == id_buscar]

def buscar_producto_por_categoria(lista, categoria):
    return [p for p in lista if p['categoria'].lower() == categoria.lower()]

def buscar_productos_disponibles(lista):
    return [p for p in lista if p['stock'] > 0]

def buscar_por_marca(lista, marca):
    return [p for p in lista if p['marca'].lower() == marca.lower()]

def buscar_por_rango_precios(lista, minimo, maximo):
    return [p for p in lista if minimo <= p['precio'] <= maximo]

def buscar_empleado_por_nombre(lista, nombre, apellido):
    return [e for e in lista if e['nombre'].lower() == nombre.lower() and e['apellido'].lower() == apellido.lower()]

def buscar_empleado_por_departamento(lista, depto):
    return [e for e in lista if e['departamento'].lower() == depto.lower()]

def buscar_empleados_activos(lista):
    return [e for e in lista if e['activo']]

def menu_productos():
    while True:
        print("\n--- MENU DE PRODUCTOS ---")
        print("1. Buscar por nombre")
        print("2. Buscar por ID")
        print("3. Buscar por categoria")
        print("4. Buscar por marca")
        print("5. Buscar productos disponibles")
        print("6. Buscar por rango de precios")
        print("7. Volver al menu principal")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            resultado = buscar_producto_por_nombre(productos, nombre)
        elif opcion == "2":
            try:
                id_buscar = int(input("ID del producto: "))
                resultado = buscar_producto_por_id(productos, id_buscar)
            except ValueError:
                print("Error: ingrese un numero valido.")
                continue
        elif opcion == "3":
            categoria = input("Categoria: ")
            resultado = buscar_producto_por_categoria(productos, categoria)
        elif opcion == "4":
            marca = input("Marca: ")
            resultado = buscar_por_marca(productos, marca)
        elif opcion == "5":
            resultado = buscar_productos_disponibles(productos)
        elif opcion == "6":
            try:
                minimo = float(input("Precio minimo: "))
                maximo = float(input("Precio maximo: "))
                resultado = buscar_por_rango_precios(productos, minimo, maximo)
            except ValueError:
                print("Error: ingrese valores numericos.")
                continue
        elif opcion == "7":
            break
        else:
            print("Opcion no valida.")
            continue

        if resultado:
            for r in resultado:
                print(r)
        else:
            print("No se encontraron resultados.")

def menu_empleados():
    while True:
        print("\n--- MENU DE EMPLEADOS ---")
        print("1. Buscar por nombre completo")
        print("2. Buscar por departamento")
        print("3. Buscar empleados activos")
        print("4. Volver al menu principal")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            resultado = buscar_empleado_por_nombre(empleados, nombre, apellido)
        elif opcion == "2":
            depto = input("Departamento: ")
            resultado = buscar_empleado_por_departamento(empleados, depto)
        elif opcion == "3":
            resultado = buscar_empleados_activos(empleados)
        elif opcion == "4":
            break
        else:
            print("Opcion no valida.")
            continue

        if resultado:
            for r in resultado:
                print(r)
        else:
            print("No se encontraron resultados.")

def menu_principal():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1. Gestion de productos")
        print("2. Gestion de empleados")
        print("3. Salir")

        opcion = input("Elige una opcion: ")

        if opcion == "1":
            menu_productos()
        elif opcion == "2":
            menu_empleados()
        elif opcion == "3":
            print("Saliendo del sistema...")
            break
        else:
            print("Opcion no valida.")

menu_principal()

