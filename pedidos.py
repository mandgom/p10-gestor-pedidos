from clientes import clientes
from utilidades import pedir_numero

pedidos = []

class LineaPedido:
    def __init__(self, producto, precio, cantidad):
        self.producto = producto
        self.precio = precio
        self.cantidad = cantidad

    def subtotal(self):
        if self.cantidad == 0:
            raise ValueError("La cantidad no puede ser cero")
        return self.precio * self.cantidad

class Pedido:
    # Almacena la información de un pedido y las líneas de artículos comprados
    def __init__(self, nombre_cliente=""):
        self.nombre_cliente = nombre_cliente
        self.lineas = []
    
    def agregar_linea(self, linea):
        self.lineas.append(linea)
    
    def total_con_descuento(self):
        total = calcular_total_lineas(self.lineas)
        return total - calcular_descuento(total)

def calcular_descuento(total):
    """Calcula el descuento aplicable según el importe total.
    Args:
        total: Suma de los artículos.
    Returns:
        Importe a descontar (float).
    """ 
    # El test nos chiva que 200€ ya tienen el 15% (baja a 170€)
    if total >= 200:
        return total * 0.15
    elif total >= 100:
        return total * 0.10
    elif total > 50:
        return total * 0.05
    return 0.0

def calcular_total_lineas(lineas):
    total = 0
    for linea in lineas:
        total += linea.subtotal()
    return total

def menu_pedidos():
    fin = False
    while fin == False:
        print("\n--- PEDIDOS ---")
        print("1. Crear pedido")
        print("2. Listar pedidos")
        print("3. Calcular total de un pedido")
        print("4. Volver")
        opcion = input("Opción: ")

        if opcion == "1":
            nuevo_pedido()
        elif opcion == "2":
            ver_pedidos()
        elif opcion == "3":
            calcular_total_desde_menu()
        elif opcion == "4":
            fin = True
        else:
            print("Opción incorrecta")

def nuevo_pedido():
    # Crea un pedido interactivo por consola asociándolo a un cliente
    print("\nCREAR PEDIDO")
    if len(clientes) == 0:
        print("Primero debes crear un cliente")
        return

    i = 0
    while i < len(clientes):
        print(str(i + 1) + ". " + clientes[i]["nombre"])
        i = i + 1

    numero_cliente = pedir_numero("Elige cliente: ")
    if numero_cliente < 1 or numero_cliente > len(clientes):
        print("Cliente incorrecto")
        return

    lineas = []
    seguir = "s"
    while seguir == "s":
        producto = input("Producto: ")
        cantidad = pedir_numero("Cantidad: ")
        precio = float(input("Precio unidad: "))

        if producto == "":
            print("Producto vacío")
        elif cantidad <= 0:
            print("Cantidad incorrecta")
        elif precio <= 0:
            print("Precio incorrecto")
        else:
            lineas.append(LineaPedido(producto, precio, cantidad))
            print("Línea añadida")

        seguir = input("¿Añadir otro producto? s/n: ")

    pedido = {"cliente": clientes[numero_cliente - 1], "lineas": lineas, "estado": "pendiente"}
    pedidos.append(pedido)
    print("Pedido creado")

def ver_pedidos():
    print("\nLISTADO DE PEDIDOS")
    if len(pedidos) == 0:
        print("No hay pedidos")
    else:
        pos = 0
        for p in pedidos:
            # Aquí aplicamos la refactorización para reusar código
            total = calcular_total_lineas(p["lineas"])
            total = total - calcular_descuento(total)
            
            print(str(pos + 1) + ". Cliente: " + p["cliente"]["nombre"] + " | Estado: " + p["estado"] + " | Total: " + str(round(total, 2)) + " €")
            pos = pos + 1

def calcular_total_desde_menu():
    if len(pedidos) == 0:
        print("No hay pedidos")
        return

    n = pedir_numero("Número de pedido: ")
    if n < 1 or n > len(pedidos):
        print("Pedido no válido")
        return

    p = pedidos[n - 1]
    
    # Aquí también reutilizamos la lógica extraída
    suma = calcular_total_lineas(p["lineas"])
    descuento = calcular_descuento(suma)

    iva = (suma - descuento) * 0.21
    total = suma - descuento + iva

    print("Subtotal: " + str(round(suma, 2)))
    print("Descuento: " + str(round(descuento, 2)))
    print("IVA: " + str(round(iva, 2)))
    print("TOTAL: " + str(round(total, 2)))

def cambiar_estado_pedido():
    # Función sin usar, pensada para detectar código muerto o incompleto
    x = input("Nuevo estado: ")
    return x