
class Administracion:

    """
        El modulo de administracion tiene atributos que sirven para registrar diferentes estadisticas o datos de interes
        y tambien para visualizar.

        Parametros:

        - total_vendido:
            Aqui va el total de unidades vendidas, es decir, si se vendieron 23 productos, ese numero va aqui.
            la idea es que cada vez que se venda algo, aumentar este numero.

        - sistema_tarjetas:
            Es de tipo lista, y es un listado de todos los clientes que realizaron compras.

        - total_descuento_por_promociones:
            Es un numero entero que representa el total acumulado de dinero que los clientes ahorraron con las promociones.

        NOTA: Existe una sola clase (objeto) de tipo "Administracion".
    """

    def __init__(self, sistema_tarjetas):
        """
            Notese que aqui el valor de "sistema_tarjeta" se inicializa con un objeto de tipo "SistemaTarjetas".
            Esto es por que permite que la clase "Administracion" tenga acceso para manejar las tarjetas.
        """
        self.total_vendido = 0
        self.sistema_tarjetas = sistema_tarjetas
        self.total_descuento_por_promociones = 0

    def imprimir_ventas_totales(self):
        print("\n| ======== VENTAS TOTALES ======== |")
        print("| Total vendido: \t\t {} |".format(self.total_vendido))
        print("| ================================ |\n")

    def registrar_venta(self, dni, carrito):
        """
            Esta es la funcion principal para registrar las compras realizadas por los clientes y guardar todos los datos en Administracion.
            Pasos que sigue:

            1 - Llama a la funcion "registrar_venta_cliente":
                Si todo sale bien, el valor "error" que nos devuelve sera == None, por lo tanto, entrara en el else.
            2 - Obtenemos los descuentos de los productos y de las tarjetas (por separado).
                Aqui se obtiene directamente el atributo "descuento_total" del objeto Carrito, para descuento de productos.
                Tambien obtenemos el descuento que realizan las tarjetas (el cual se aplica sobre el precio final luego de los descuentos por productos).
                Para esto utilizamos la funcion "obtener_descuento_tarjeta" de "sistema_tarjetas".
            3 - Luego imprimimos valores de interes como son los diferentes descuentos y actualizamos las estadisticas del sistema de Administracion.
        """
        
        error = self.registrar_venta_cliente(dni, carrito)
        if error != None: # Devolvera un error al momento de realizar la venta si es que existe. (Ej: el cliente no fue dado de alta)
            return error
        else:   # Si no hubo error, se procede normalmente y se registra la compra.
            descuento_productos = carrito.descuento_total
            descuento_tarjeta = self.sistema_tarjetas.obtener_descuento_tarjeta(dni, carrito.precio_final)
            print("Descuento productos: {}".format(descuento_productos))
            print("Descuento tarjeta: {}".format(descuento_tarjeta))
            self.total_vendido += len(carrito.productos)
            self.total_descuento_por_promociones += descuento_productos + descuento_tarjeta
            return None

    def registrar_venta_cliente(self, dni, carrito):
        """
            La funcion recibe como parametro un dni y el objeto Carrito.
            Si ese dni pertenece a un cliente que esta registrado:
                Iteramos a traves del listado de clientes que tenemos, 
                y le sumamos el total de objetos comprados al atributo 'compras' 
                de nuestro objeto Cliente y tambien al atributo 
                'compras' de nuestro objeto "Tarjeta" (Cada tarjeta es asignada a un cliente).

            Si el cliente no existe, devolvemos un mensaje de error diciendo que el cliente no fue dado de alta.
            
        """
        if any(str(cliente.dni) == str(dni) for cliente in self.sistema_tarjetas.clientes):
            for cliente in self.sistema_tarjetas.clientes:
                if cliente.dni == dni:
                    cliente.compras += len(carrito.productos)
                    cliente.tarjeta.compras += len(carrito.productos)
                    return None
        else:
            return "[Error] El cliente no fue dado de alta."

    def imprimir_ventas_por_cliente(self):
        """
            Imprimimos entonces el nombre y la cantidad de compras que realizo el cliente.
        """
        print("-------------------------------- VENTAS X CLIENTES ---------------------------------\n")
        for cliente in self.sistema_tarjetas.clientes:
            print("{} {} \t\t\t\t\t\t\t | {}\n".format(cliente.nombre, cliente.apellido, cliente.compras))

    def imprimir_ventas_por_tarjeta(self):
        """
            Imprimimos entonces las tarjetas y la cantidad de compras que se realizo con cada tarjeta.
        """
        print("-------------------------------- VENTAS X TARJETAS ---------------------------------\n")
        for cliente in self.sistema_tarjetas.clientes:
            print("{}\t\t\t\t\t | {}\n".format(cliente.tarjeta.numero_de_tarjeta, cliente.tarjeta.compras))

    def imprimir_total_descuentos(self):
        print("-------------------------------- TOTAL DESCUENTOS ----------------------------------\n")
        print("Descuento por promociones: {} \n".format(self.total_descuento_por_promociones))
