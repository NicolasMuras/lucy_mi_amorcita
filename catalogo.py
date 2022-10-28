"""
Aqui tenemos dos tipos de objeto, producto y catalogo.
Van aqui ambos por que estan relacionados fuertemente.
"""

class Producto:
    """
        Cada objeto "Producto" tiene su codigo, nombre, precio y promocion asociada.

        Parametros:

        - codigo:
            Es un valor que se genera solo al crear el producto.

        - nombre:
            Ej: Mochila
    
        - precio:
            Puede ser de tipo entero o flotante. Ej: 100 o 250.0

        - promocion:
            Es un valor flotante en este rango 0.01 - 0.99. Por defecto es 'None'
            Ya que al comienzo el producto no tiene una promocion asociada.

    """
    def __init__(self, codigo, nombre, precio):
        """
            Esta funcion inicializa los valores del objeto Producto.
            Es una funcion especial que se ejecuta al crearse el objeto.
            el modo de crear un objeto en Python es por ej: 
            producto = Producto(1, mochila, 150)
        """
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.promocion = None

    def obtener_precio(self):
        """
            El "descuento" se aplica sobre el precio del producto para reducir el precio.
            - Ej tenemos un Producto que vale 200 y una promocion de descuento de 20%:

            self.precio = 200
            self.promocion = 0.80

            La funcion devolveria lo siguiente (160):

            200 * 0.80 = 160

            NOTA: Hay que tener en cuenta, de que por ejemplo si se quiere un 30% de descuento,
             el valor del atributo "self.promocion" de nuestro Producto debe ser 0.70.
        """
        # Recordemos de que si al producto no se le asigno un valor de promocion al principio, entonces el valor es None.
        # Por esto es importante aplicar este filtro, para que solo se le aplique la formula de promocion a los productos que corresponde.
        if self.promocion != None: 
            return int(self.precio) * (1 - self.promocion)
        return int(self.precio)

    def obtener_descuento(self):
        if self.promocion != None: 
            return self.precio - (int(self.precio) * (1 - self.promocion))
        return 0


class Catalogo:
    """
        El catalogo almacena los objetos de tipo Producto y tiene funciones para gestionar la lista de productos.

        Parametros:

        - productos:
            Es una lista de objetos de tipo "Producto", aqui se almacenaran todos los productos que el usuario carge.
    """

    def __init__(self):
        """
            Aqui la funcion __init__ no recibe parametros, ya que el Catalogo se inicializa vacio.
        """
        self.productos = []
    
    def agregar_producto(self, nombre, precio):
        """
            Esta es la funcion encargada de crear y agregar productos a nuestro catalogo.
            Recibe los parametros de nombre y precio. Crea el producto y lo agrega al catalogo.

            Utilizamos '.append()' sobre una lista para agregarle objetos.
            En este caso, agregamos "producto" a la lista de produtos del catalogo.
        """
        codigo = len(self.productos) # Con esto, obtenemos el numero total de productos y vamos generando automaticamente los codigos.
        producto = Producto(codigo, nombre, int(precio)) # Se crea el producto

        # Se agrega el producto a la lista de productos. (se utiliza "self" para decir que estamos accediendo al atributo "productos" de esta clase "Catalogo").
        self.productos.append(producto) 

    def agregar_promocion(self, nombre, promocion):
        """
            Esta funcion asigna una promocion a un producto existente.

            El if any() funciona para verificar de que existan productos con el nombre dado.
            En caso de no encontrar ningun producto con ese nombre devolvera un error. 

            Luego iteramos a traves de la lista de productos de nuestro catalogo
            hay un "if" dentro del bucle for, cuando encuentra un producto cuyo nombre corresponde
            al valor "nombre" que le pasamos a la funcion, le aplica el valor "promocion" que le pasamos.

            Parametros:

            - nombre:
                Ej: Vaso
            
            - promocion:
                Ej: 20

        """
        if any(producto.nombre == nombre for producto in self.productos):
            for producto in self.productos:
                if producto.nombre == nombre:
                    producto.promocion = float(promocion) / 100 # Aqui se asigna la promocion al producto.
        else:
            return "[ERROR] El producto no existe."

    def listar_productos(self):
        """
            Imprime la lista de productos de una forma legible para el usuario.
            Itero a traves de un bucle for y voy imprimiendo los productos con su precio.
            El precio impreso ya viene con el calculo de la promocion aplicado.

            NOTA: Utilizo la \ y las letras t y n para formatear el texto. 
            - La 't' se usa para imprimir un tab (agrega un espacio grande).
            - La 'n' se utiliza para imprimir un salto de linea (enter).

            NOTA: Utilizo .format() para insertar valores dentro de la cadena de texto.
            Eso funciona asi: se colocal {} en la cadena de texto y 
            luego se pasan los valores que quieres insertar en la cadena a imprimir.
        """
        print("------------------------------------- CATALOGO -------------------------------------\n")
        for producto in self.productos:
            print("{} | {}\t\t\t\t\t | $ {}\n".format(producto.codigo, producto.nombre, producto.obtener_precio()))

    def listar_promociones(self):
        """
            Imprimo una lista de los productos que tienen su promocion y el valor de la promocion.
        """
        print("------------------------------------ PROMOCIONES -----------------------------------\n")
        for producto in self.productos:
            if producto.promocion != None:
                print("{} | {}\t\t\t\t\t | {:.0f}%\n".format(producto.codigo, producto.nombre, producto.promocion * 100))
            else:
                print("{} | {}\t\t\t\t\t | No hay promociones asociadas.\n".format(producto.codigo, producto.nombre))
