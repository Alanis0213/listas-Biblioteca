clientes=[["juan",3100],["maria",3101],["pedro",3102],["laura",3103]]
#nombre del cliente, codigo del cliente
libros=[[12552,"iliada",5300,25],[12553,"platero",2500,16],[12554,"cien",3600,35]]
#codigo del libro ISBN, titulo del libro,precio del libro, unidades de libros disponibles
ventas=[(1020,3100,12552,4,21200),(1025,3103,12553,2,5000),(1030,3100,12554,3,10800),(1035,3101,12553,9,22500)]
#codigo de venta (generado automaticamente),codigo del cliente,codigo del libro,cantidad vendida,valor de la venta

def menu_principal():
    while True:
        print("====Menu principal====")
        print("1 - clientes")
        print("2 - libros")
        print("3 - ventas")
        print("4 - estadisticas")
        print("5 - salir")
        opcion=input("ingrese una opcipn: ")
        if opcion == '1':
            menu_clientes()
        elif opcion == '2':
            menu_libros()
        elif opcion == '3':
            menu_ventas()
        elif opcion == '4':
            menu_estadisticas()
        elif opcion=='5':
            print("fin del programa")
            break
        else:
            print("opcion invalida, intente nuevamente")

def menu_clientes():
    while True:
        print("====Menu clientes====")
        print("1 - ingresar clientes")
        print("2 - lista de clientes")
        print("3 - borrar cliente")
        print("4 - buscar cliente")
        print("5 - actualizar cliente")
        print("6 - salir")
        opcion1=input("ingrese una opcion: ")

        if opcion1 == '1':
            ingresar_clientes(clientes)
        elif opcion1 == '2':  
            lista_clientes(clientes)
        elif opcion1 == '3':
            borrar_cliente(clientes)
        elif opcion1 == '4':
            buscar_cliente(clientes)
        elif opcion1== '5':
            actualizar_cliente(clientes)
        elif opcion1 == '6':
            break
        else:
            print("opcion invalida - intente nuevamente")

def ingresar_clientes(clientes):
    while True:
        print("===============================================")
        print("Para salir, ingrese '0' en ambos campos.")
        nombre = input("Ingrese el nombre del cliente: ")
        if nombre == '0':
            break
        codigo = int(input("Ingrese el código del cliente: "))
        print("===============================================")
        for cliente in clientes:
            if codigo == cliente[1]:
                print("El código ya ha sido registrado.")
                break
        else:
            clientes.append([nombre, codigo])
            print("Cliente registrado exitosamente.")

def lista_clientes(clientes):
    print("=========================================")
    print("Lista de clientes:")
    for cliente in clientes:
        print(f"Nombre: {cliente[0]}, Código: {cliente[1]}")
    print("=========================================")

def borrar_cliente(clientes):
    while True:
        print("=======================================")
        codigo = int(input("Ingrese el código del cliente a borrar - ingrese '0' para salir: "))
        if codigo == 0:
            break
        cliente_encontrado = False
        for cliente in clientes:
            if cliente[1] == codigo:
                cliente_encontrado = True
                for venta in ventas:
                    if venta[1] == codigo:
                        print("El cliente no se puede eliminar porque tiene compras registradas.")
                        break
                else:
                    clientes.remove(cliente)
                    print(f"El cliente con código {codigo} y nombre {cliente[0]} ha sido eliminado.")
                break
        if not cliente_encontrado:
            print("El cliente no existe.")

def buscar_cliente(clientes):
    while True:
        print("=======================================")
        cd_cliente = int(input("Ingrese el código del cliente - ingrese '0' para salir: "))
        if cd_cliente == 0:
            break
        cliente_encontrado = False
        pos = 0
        for cliente in clientes:
            pos += 1
            if cliente[1] == cd_cliente:
                cliente_encontrado = True
                print("=========================================")
                print(f"Nombre del cliente: {cliente[0]}. Código del cliente: {cliente[1]}.")
                print(f"Ubicación en la lista: {pos}")
                print("=========================================")
                break
        if not cliente_encontrado:
            print("El código no está registrado.")

def actualizar_cliente(clientes):
    while True:
        print("Para salir, ingrese '0'")
        cd_cliente = int(input("Ingrese el código del cliente: "))
        if cd_cliente == 0:
            break
        cliente_encontrado = False
        for cliente in clientes:
            if cliente[1] == cd_cliente:
                cliente_encontrado = True
                nv_nombre = input("Ingrese el nuevo nombre: ")
                cliente[0] = nv_nombre
                print("================================")
                print("El nombre se ha actualizado.")
                print(f"El nuevo nombre es: {cliente[0]}")
                print(f"El código es: {cliente[1]}")
                print("================================")
                break
        if not cliente_encontrado:
            print("=======================")
            print("El código no existe")
            print("========================")

def menu_libros():
    while True:
        print("====Menu libros====")
        print("1 - ingresar libros")
        print("2 - lista de libros")
        print("3 - borrar libros")
        print("4 - buscar libro")
        print("5 - actualizar libro")
        print("6 - actualizar cantidad de libros")
        print("7 - actualizar precio del libro")
        print("8 - salir")
        opcion1=input("ingrese una opcion: ")
        if opcion1== '1':
            ingreso_libros(libros)
        elif opcion1 == '2':
            lista_libros(libros)
        elif opcion1 == '3':
            borrar_libro(libros)
        elif opcion1 == '4':
            buscar_libro()
        elif opcion1== '5':
            actualizar_libro(libros)
        elif opcion1 =='6':
            actualizar_cantidad(libros)
        elif opcion1 == '7':
            actualizar_precio(libros)
        elif opcion1 == '8':
            break
        else:
            print("opcion invalida - intente nuevamente")

def ingreso_libros(libros):
    while True:
        print("===============================================")
        print("Para salir, ingrese '0' en todos los campos.")
        nombre = input("Ingrese el nombre del libro: ")
        if nombre == '0':
            break
        codigo = int(input("Ingrese el código del libro: "))
        precio = float(input("Ingrese el precio del libro: "))
        unidades = int(input("Ingrese la cantidad de unidades recibidas: "))
        print("===============================================")
        for libro in libros:
            if codigo == libro[0]:
                print("El código ya ha sido registrado.")
                break
        else:
            libros.append([codigo, nombre, precio, unidades])
            print("Libro registrado exitosamente.")

def lista_libros(libros):
    print("--------------------------------------------------------")
    print("Lista de libros:")
    for libro in libros:
        print(f"Código: {libro[0]}, Nombre: {libro[1]}, Precio: {libro[2]}, Unidades disponibles: {libro[3]}")
    print("--------------------------------------------------------")


def actualizar_cantidad(libros):
    while True:
        print("=======================================")
        print("para salor ingrese '0' ")
        codigo = int(input("Ingrese el código del libro: "))
        if codigo == 0:
            break
        for libro in libros:
            if codigo == libro[0]:
                unidades = int(input("Ingrese la cantidad de unidades recibidas: "))
                libro[3] += unidades
                print(f"Se han agregado {unidades} unidades del libro {libro[1]}. Nuevo total: {libro[3]}")
                break
            else:
                print("El código no está registrado.")
                print("=======================================")

def actualizar_precio(libros):
    while True:
        print("==========================================")
        codigo = int(input("Ingrese el código del libro a actualizar - para salir ingrese '0': "))
        precio = float(input("Ingrese el nuevo precio del libro: "))
        libro_encontrado = False
        if codigo == 0:
            break
        for libro in libros:
            if libro[0] == codigo:
                libro[2] = precio
                libro_encontrado = True
                print(f"Se ha actualizado el precio del libro con código {codigo} a ${precio}.")
                break
        if not libro_encontrado:
            print("El libro no está registrado en la lista.")

def borrar_libro(libros):
    while True:
        codigo = int(input("Ingrese el código del libro a borrar - ingrese '0' para salir: "))
        if codigo == 0:
            break
        libro_encontrado = False
        for libro in libros:
            if libro[0] == codigo:
                libro_encontrado = True
                for venta in ventas:
                    if venta[2] == codigo:
                        print("El libro no se puede eliminar porque tiene ventas registradas.")
                        break
                else:
                    libros.remove(libro)
                    print(f"El libro con código {codigo} y nombre {libro[1]} ha sido eliminado.")
                break
        if not libro_encontrado:
            print("El libro no existe.")

def buscar_libro():
    while True:
        print("=======================================")
        cd_libro = int(input("Ingrese el código del libro - ingrese '0' para salir: "))
        if cd_libro == 0:
            break
        libro_encontrado = False
        pos = 0
        for libro in libros:
            pos += 1
            if libro[0] == cd_libro:
                libro_encontrado = True
                print("=========================================")
                print(f"Nombre del libro: {libro[1]}. Código del libro: {libro[0]}.")
                print(f"Ubicación en la lista: {pos}")
                print("=========================================")
                break
        if not libro_encontrado:
            print("El código no está registrado.")

def actualizar_libro(libros):
    while True:
        print("Para salir, ingrese '0'")
        cd_libro = int(input("Ingrese el código del libro: "))
        if cd_libro == 0:
            break
        libro_encontrado = False
        for libro in libros:
            if libro[0] == cd_libro:
                libro_encontrado = True
                nv_nombre = input("Ingrese el nuevo nombre: ")
                libro[1] = nv_nombre
                print("======================================")
                print("El nombre se ha actualizado.")
                print(f"El nuevo código es: {libro[0]}")
                print(f"El nuevo nombre es: {libro[1]}")
                print("======================================")
                break
        if not libro_encontrado:
            print("========================")
            print("El código no existe")
            print("========================")


def menu_ventas():
    while True:
        print("====Menu Ventas====")
        print("1 - realizar venta")
        print("2 - lista de ventas realizadas")
        print("3 - buscar venta realizada")
        print("4 - borrar venta")
        print("5 - actualizar venta")
        print("6 - salir")
        opcion4=input("ingrese una opcion: ")
        if opcion4 == '1':
            registrar_venta(ventas)
        elif opcion4 == '2':
            mostrar_ventas()
        elif opcion4 == '3':
            buscar_venta_menu()
        elif opcion4 == '4':
            eliminar_venta()
        elif opcion4 == '5':
            actualizar_venta()
        elif opcion4 =='6':
            break
        else:
            print("opcion invalida")

def generar_codigo_venta(cliente_actual):
    codigo_actual = ventas[-1][0]
    codigo_cliente_actual = cliente_actual[1]
    
    if codigo_actual != 0:
        nuevo_codigo = codigo_actual + 5
    else:
        nuevo_codigo = 1020
    
    return nuevo_codigo, codigo_cliente_actual

def buscar_cl(codigo):
    for cliente in clientes:
        if cliente[1] == codigo:
            return cliente
    return False

def buscar_li(codigo):
    for libro in libros:
        if libro[0] == codigo:
            return libro
    return False

def registrar_venta(ventas):
    while True:
        print("===========================================")
        print("para salir ingrese '0' ")
        codigo_cliente = int(input("Ingrese el codigo del cliente: "))
        if codigo_cliente == 0:
            break
        cliente =False
        for c in clientes:
            if c[1] == codigo_cliente:
                cliente = c
                continue
        if cliente is False:
            print("El cliente no existe.")
            return 
        codigo_libro = int(input("Ingrese el codigo del libro: "))
        libro = False
        for l in libros:
            if l[0] == codigo_libro:
                libro = l
                continue
        if libro is False:
            print("El libro no existe.")
            return 
        cantidad = int(input("Ingrese la cantidad vendida: "))
        if cantidad == 0:
            print("Ingrese una cantidad valida")
            print("=====================================")
            continue
        if cantidad > libro[3]:
            print("No hay suficientes unidades disponibles.")
            return 

        nuevo_codigo_venta, codigo_cliente_actual = generar_codigo_venta(cliente)
        valor_venta = cantidad * libro[2]
        venta = (nuevo_codigo_venta, codigo_cliente_actual, codigo_libro, cantidad, valor_venta)
        ventas.append(venta)
        libro[3] -= cantidad
        print("Venta registrada exitosamente.")
        print(f"Codigo de venta: {nuevo_codigo_venta}")

def mostrar_ventas():
    print("==== Lista de ventas realizadas ====")
    for venta in ventas:    
        print("======================================")
        print(f"Código de venta: V-{venta[0]},Código del cliente: {venta[1]},Código del libro: {venta[2]},Cantidad vendida: {venta[3]},Valor de la venta: ${venta[4]}")
        print("======================================")

def buscar_venta_menu():
    while True:
        print("Para salir, ingrese '0'")
        codigo_venta = int(input("Ingrese el código de la venta a buscar: "))
        
        if codigo_venta == 0:
            break
        
        venta_encontrada = False
        for venta in ventas:
            if venta[0] == codigo_venta:
                venta_encontrada = True
                print("================================")
                print(f"Código de venta: V-{venta[0]}, Código de cliente: {venta[1]}, Código de libro: {venta[2]}, Cantidad vendida: {venta[3]}, Valor de venta: {venta[4]}")
                print("=================================")
                break
        
        if not venta_encontrada:
            print("======================================")
            print("La venta no fue encontrada.")
            
def eliminar_venta():
    codigo_venta = int(input("Ingrese el código de venta que desea eliminar: "))
    for venta in ventas:
        if venta[0] == codigo_venta:
            ventas.remove(venta)
            print("La venta se eliminó correctamente.")
            return
    print("No se encontró ninguna venta con ese código.")

def actualizar_venta():
    codigo_venta = int(input("Ingrese el código de venta que desea actualizar: "))
    cantidad_vendida = int(input("Ingrese la nueva cantidad vendida: "))
    venta_encontrada = False
    for i in range(len(ventas)):
        if ventas[i][0] == codigo_venta:
            codigo_libro = ventas[i][2]
            for j in range(len(libros)):
                if libros[j][0] == codigo_libro:
                    precio_libro = libros[j][2]
                    unidades_vendidas_previas = ventas[i][3]
                    unidades_disponibles = libros[j][3]
                    diferencia = cantidad_vendida - unidades_vendidas_previas
                    if diferencia <= unidades_disponibles:
                        venta_actual=list(ventas[i])
                        venta_actual[3]=cantidad_vendida
                        venta_actual[4]=cantidad_vendida*precio_libro
                        ventas[i]=tuple(venta_actual)
                        libros[j][3] -= diferencia
                        venta_encontrada = True
                    else:
                        print("No hay suficientes unidades disponibles.")
                    break
            break
    if venta_encontrada:
        print("La venta se actualizó correctamente.")
    else:
        print("No se encontró ninguna venta con ese código.")


def menu_estadisticas():
    while True:
        print("====Menu estadisticas====")
        print("1 - ventas totales de libros por ISBN")
        print("2 - libro mas y menos vendido")
        print("3 - venta total de la libreria")
        print("4 - cliente con mayor compra por venta")
        print("5 - cliente con mayor volumen de compra total")
        print("6 - salir")
        opcion5=input("ingrese una opcion:" )

        if opcion5 == '1':
            obtener_ventas_totales_por_codigo_libro(ventas)
        elif opcion5 == '2':
            mostrar_libros_mas_y_menos_vendido(ventas)
        elif opcion5 == '3':
            calcular_venta_total_libreria(ventas)
        elif opcion5 =='4':  
            cliente_mayor_compra(clientes,ventas)
        elif opcion5 =='5':
            volumen_compra(clientes,libros,ventas)
        elif opcion5 == '6':
            break
        else:
            print("opcincion inavalida")

def obtener_ventas_totales_por_codigo_libro(ventas):
    ventas_totales_por_libro = []

    for libro in libros:
        codigo_libro = libro[0]
        ventas_totales = 0

        for venta in ventas:
            if venta[2] == codigo_libro:
                ventas_totales += venta[3]

        ventas_totales_por_libro.append((codigo_libro, ventas_totales))

    print("Ventas por libro:")
    for venta in ventas_totales_por_libro:
        codigo_libro = venta[0]
        ventas_totales = venta[1]
        print("Libro con código", codigo_libro, "- Ventas totales:", ventas_totales)

def mostrar_libros_mas_y_menos_vendido(ventas):
    libros_vendidos = []
    for venta in ventas:
        codigo_libro = venta[2]
        encontrado = False

        for i in range(len(libros_vendidos)):
            if libros_vendidos[i][0] == codigo_libro:
                libros_vendidos[i][1] += venta[3]
                encontrado = True
                break
        if not encontrado:
            libros_vendidos.append([codigo_libro, venta[3]])
    max_vendidos = libros_vendidos[0]

    for libro in libros_vendidos:
        if libro[1] > max_vendidos[1]:
            max_vendidos = libro
    codigo_mas_vendido = max_vendidos[0]
    unidades_mas_vendidas = max_vendidos[1]
    min_vendidos = libros_vendidos[0]

    for libro in libros_vendidos:
        if libro[1] < min_vendidos[1]:
            min_vendidos = libro
    codigo_menos_vendido = min_vendidos[0]
    unidades_menos_vendidas = min_vendidos[1]

    print("==============================================")
    print("Libro más vendido:")
    print("Código:", codigo_mas_vendido)
    print("Unidades vendidas:", unidades_mas_vendidas)
    print("==============================================")
    print("Libro menos vendido:")
    print("Código:", codigo_menos_vendido)
    print("Unidades vendidas:", unidades_menos_vendidas)
    print("==============================================")

def calcular_venta_total_libreria(ventas):
    venta_total = 0
    for venta in ventas:
        valor_venta = venta[4]
        venta_total += valor_venta
    print("====================================================")
    print("Venta Total de la librería:", venta_total)
    print("====================================================")

def cliente_mayor_compra(clientes,ventas):
    mayor_compra = 0
    cliente = ""
    cantidad_comprada = 0
    for venta in ventas:
        valor_venta = venta[3] * venta[2]
        if valor_venta > mayor_compra:
            mayor_compra = valor_venta
            cantidad_comprada = venta[3]
            codigo_cliente = venta[1]
            for cliente_info in clientes:
                if cliente_info[1] == codigo_cliente:
                    cliente = cliente_info[0]
    print("====================================================")
    print(f"El cliente con la mayor compra por venta fue: {cliente}")
    print(f"Cantidad comprada: {cantidad_comprada} libros")
    print(f"Monto total comprado: ${mayor_compra}")
    print("====================================================")




def volumen_compra(clientes, libros, ventas):
    mayor_volumen = 0
    cliente = ""
    cantidad_comprada = 0
    valor_comprado = 0

    for cliente_info in clientes:
        codigo_cliente = cliente_info[1]
        volumen_cliente = 0
        cantidad_cliente = 0
        valor_cliente = 0

        for venta in ventas:
            if venta[1] == codigo_cliente:
                codigo_libro = venta[2]
                cantidad_vendida = venta[3]
                valor_venta = 0

                for libro in libros:
                    if libro[0] == codigo_libro:
                        valor_venta = cantidad_vendida * libro[2]
                        break

                volumen_cliente += valor_venta
                cantidad_cliente += cantidad_vendida
                valor_cliente += valor_venta

        if volumen_cliente > mayor_volumen:
            mayor_volumen = volumen_cliente
            cantidad_comprada = cantidad_cliente
            valor_comprado = valor_cliente
            cliente = cliente_info[0]
    print("===================================================================")
    print(f"El cliente con el mayor volumen de compra total es: {cliente}")
    print(f"Cantidad comprada: {cantidad_comprada} libros")
    print(f"Dinero gastado: {valor_comprado} pesos")
    print("===================================================================")





menu_principal()