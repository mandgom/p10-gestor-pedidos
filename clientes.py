clientes = []

class Cliente:
    #Representa a un cliente dentro del sistema.
    def __init__(self, nombre, email, telefono=""):
        self.nombre = nombre
        self.email = email
        self.telefono = telefono

    def es_valido(self):
        if "@" in self.email:
            return True
        return False

def menu_clientes():
    terminar = False
    while terminar == False:
        print("\n--- CLIENTES ---")
        print("1. Añadir cliente")
        print("2. Listar clientes")
        print("3. Buscar cliente")
        print("4. Volver")
        op = input("Opción: ")

        if op == "1":
            crear_cliente()
        elif op == "2":
            listar_clientes()
        elif op == "3":
            buscar_cliente()
        elif op == "4":
            terminar = True
        else:
            print("No existe esa opción")

def crear_cliente():
    # Solicita datos por consola para registrar un nuevo cliente.
    nombre = input("Nombre: ")
    telefono = input("Teléfono: ")
    email = input("Email: ")

    if not validar_nombre(nombre):
        print("El nombre no puede estar vacío")
    elif not validar_email(email):
        print("El email no es válido")
    else:
        cliente = Cliente(nombre, email, telefono)
        clientes.append(cliente)
        print("Cliente añadido")

def listar_clientes():
    # Muestra por consola el listado de clientes registrados.
    print("\nLISTADO DE CLIENTES")
    if len(clientes) == 0:
        print("No hay clientes")
    else:
        i = 0
        while i < len(clientes):
            cliente = clientes[i]
            print(str(i + 1) + ". " + cliente.nombre + " - " + cliente.telefono + " - " + cliente.email)
            i = i + 1

def buscar_cliente():
    texto = input("Texto a buscar: ")
    encontrado = False
    for cliente in clientes:
        if texto.lower() in cliente.nombre.lower() or texto in cliente.telefono or texto.lower() in cliente.email.lower():
            print(cliente.nombre + " - " + cliente.telefono + " - " + cliente.email)
            encontrado = True
        if encontrado == False:
            print("No se encontraron clientes")

def validar_email(email):
    if "@" in email:
        return True
    return False

def validar_nombre(nombre):
    # .strip() elimina espacios en blanco para evitar nombres como "   "
    if len(nombre.strip()) > 0:
        return True
    return False