
class Cliente:
    """
        Atributos:

        - dni:
            Tiene que ser un numero. Ej: 1324512 o 123.

        - nombre:
            Ej: Luciana

        - apellido:
            Ej: Altamirano

        - compras:
            Estadistica que sirve para medir la cantidad de compras realizadas por este cliente.

        - tarjeta:
            Por defecto empieza en None (Ya que el cliente al comienzo no tiene una tarjeta asignada)
            Pero luego se le asigna un objeto de tipo Tarjeta. Este objeto de tipo Tarjeta cuenta con sus
            attributos propios. Ej: numero_de_tarjeta, etc

        NOTA: Pueden existir muchos objetos de tipo Cliente.
    """
    def __init__(self, dni, nombre, apellido):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.compras = 0
        self.tarjeta = None


class Tarjeta:

    """
        El objeto "Tarjeta" tiene los siguientes atributos:

        Attributos:

        - numero_de_tarjeta:
            Ej: 3912 1231 1231 3252 tambien puede ser 666 (No hay validadores para el formato del numero).

        - beneficio:
            Aqui va el numero flotante que se utiliza para aplicar descuentos.
            Ej: 40 (Lo cual representa un 40% de descuento sobre el precio final de la compra).

        - compras:
            La cantidad de compras que se ha realizado con este tipo de tarjeta.

        
        NOTA: Pueden haber varios objetos de tipo Tarjeta (1 por cada objeto de tipo Cliente).

    """

    def __init__(self, numero_de_tarjeta):
        """
            El valor del atributo "self.beneficio" se inicializa en None ya que se le asigna posteriormente.
        """
        self.numero_de_tarjeta = numero_de_tarjeta
        self.beneficio = None
        self.compras = 0


class SistemaTarjetas:

    """
        Podemos pensarlo como un modulo para dar de alta clientes, tarjetas y beneficios.
    
        Atributos:

        clientes:
            Es de tipo lista y dentro van objetos de tipo Cliente.
            Cada cliente puede ser o no, poseedor de una tarjeta.

        Primero se debe dar de alta un cliente y posteriormente asignarle una tarjeta luego opcionalmente un beneficio.

        NOTA: Hay un solo objeto de tipo SistemaTarjetas y es utilizado por el objeto Administracion para gestionar esta parte del sistema.
    """

    def __init__(self):
        self.clientes = []

    def dar_de_alta_cliente(self, dni, nombre, apellido):
        """
            Creamos un nuevo cliente. (Por default, no tiene tarjeta)
            La funcion recibe como parametros el dni, nombre y apellido.

            Utilizamos la validacion if any() para filtrar por dni, en caso de que ya exista un cliente con ese dni, imprimimos un error.
            En caso de que el dni este disponible, utilizamos la funcion lista.append(producto) para agregar el objeto de tipo Cliente
            que acabamos de crear a la lista de clientes que maneja el sistema de tarjetas.
        """
        if any(cliente.dni == dni for cliente in self.clientes) or len(self.clientes) == 0:
            cliente = Cliente(dni, nombre, apellido)
            self.clientes.append(cliente)
            print("\n|  ==============================  |")
            print("|  [+] Cliente agregado con exito. |")
            print("|  ==============================  |\n")
        else:
            print("\n[ERROR] Ya existe un cliente con ese DNI.\n")
    
    def dar_de_alta_tarjeta(self, numero, dni):
        """
            Aqui damos de alta y asociamos tarjetas a usuarios.
            Se itera en un bucle for para buscar al cliente con el 'dni' dado
            y asignarle la tarjeta, si no existe el cliente, imprimira un error.

            Los pasos son:
            1 - Validamos de que exista un cliente con el DNI que recibe la funcion.
            2 - Creamos la nueva tarjeta.
            3 - Iterar a traves de clientes.
            4 - Identificar el cliente el cual es poseedor del DNI dado.
            5 - Cambiar el atributo "tarjeta" de ese cliente (Pasa de ser "None" a ser un objeto de tipo "Tarjeta").
                Para esto se utiliza cliente.tarjeta = nueva_tarjeta
        """

        if any(cliente.dni == dni for cliente in self.clientes):
            nueva_tarjeta = Tarjeta(numero)
            for cliente in self.clientes:
                if cliente.dni == dni:
                    cliente.tarjeta = nueva_tarjeta
                    print("\n|  ===============================  |")
                    print("|  [+] La tarjeta fue dada de alta. |")
                    print("|  ===============================  |\n")
        else:
            print("\n[ERROR] Cliente no encontrado.\n")
            
    def dar_de_alta_beneficios_a_tarjeta(self, numero, beneficio):
        """
            Aqui proporcionamos beneficios a la tarjeta de un numero dado.
            La funcion recibe estos dos parametros y los utiliza para aplicar una logica similar a la funcion anterior.

            Ej: 20 -> 3133 1231 1231 1231  | Esto quiere decir que la tarjeta tendra un 20% de descuento.
        """
        if any(cliente.tarjeta.numero_de_tarjeta == numero for cliente in self.clientes): # Se comprueba de que la tarjeta exista.
            for cliente in self.clientes: # Se itera a traves de nuestros clientes.
                if cliente.tarjeta.numero_de_tarjeta == numero: # Esto con el fin de identificar la tarjeta a la que le aplicaremos el beneficio.
                    cliente.tarjeta.beneficio = float(beneficio) / 100 # Se aplica el beneficio a la tarjeta (Se lo guarda como valor flotante).
                    print("\n|  =========================  |")
                    print("|  [+] Beneficio actualizado. |")
                    print("|  =========================  |\n")
        else:
            print("[ERROR] El tipo de tarjeta no es permitida.")

    def listar_tarjetas_de_credito(self):
        """
            Imprime un listado de las tarjetas y sus beneficios (descuentos), formateado de una forma legible.
            Si la tarjeta no tiene beneficios, cae en el "else", entonces le imprimimos el texto "No tiene beneficios".
        """
        print("------------------------------------- TARJETAS -------------------------------------\n")
        for cliente in self.clientes:
            if cliente.tarjeta != None:
                if cliente.tarjeta.beneficio != None:
                    print("{}\t\t\t\t\t | {:.0f}%\n".format(cliente.tarjeta.numero_de_tarjeta, cliente.tarjeta.beneficio * 100))
                else:
                    print("{}\t\t\t\t\t | No tiene beneficios.\n".format(cliente.tarjeta.numero_de_tarjeta))

    def listar_tarjetas_de_credito_con_beneficios(self):
        """
            Imprime un listado de las tarjetas y sus beneficios (descuentos), formateado de una forma legible.
            Aqui solo se incluyen las que tienen beneficios.
        """
        print("------------------------------ TARJETAS CON BENEFICIOS -----------------------------\n")
        for cliente in self.clientes:
            if cliente.tarjeta != None:
                if cliente.tarjeta.beneficio != None:
                    print("{}\t\t\t\t\t | {:.0f}%\n".format(cliente.tarjeta.numero_de_tarjeta, cliente.tarjeta.beneficio * 100))

    def obtener_descuento_tarjeta(self, dni, precio):

        for cliente in self.clientes:
            if cliente.dni == dni: # Iteramos para buscar al cliente que posee el dni dado.
                if cliente.tarjeta.beneficio != None: # Luego verificamos de que la tarjeta asociada al cliente tenga beneficios.
                    precio_con_descuento = precio * cliente.tarjeta.beneficio
                    total = precio - precio_con_descuento # Si tiene beneficios le restamos al precio original el descuento correspondiente. (Esto es el descuento).
                    return total
                else:
                    return 0 # Si no tiene beneficios, entonces simplemente devolvemos 0 (ya que no hay descuento).
