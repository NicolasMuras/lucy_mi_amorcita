class Carrito:
    """
        Esta clase permite manejar los objetos de tipo "Producto", de manera que podremos
        agregar, quitar y listar los objetos contenidos en nuestra lista de productos.
        
        Parametros:
        - precio_final:
            Aqui se guarda el precio total de todos los productos acumulados en el carrito.

        - descuento_total:
            El descuento total por promociones en productos (No incluye promociones de tarjetas).

        - productos:
            Es una lista de objetos de tipo "Producto" donde se almacena lo que se va a comprar.

        NOTA: Tener en cuenta de que en nuestro sistema tenemos un solo objeto de tipo "Carrito".
        
    """

    def __init__(self):
        """
            Cuando se crea un nuevo "Carrito", la funcion __init__ permite inicializar los valores.
            En este caso, el precio_final se inicializa con el precio en 0.
            En este caso, el valor de descuentos, tambien se inicializa en 0.
            En este caso la lista "productos" va a inicializarse vacia.
        """

        self.precio_final = 0
        self.descuento_total = 0
        self.productos = []

    def agregar_al_carro(self, nombre_producto, catalogo):
        """
            1 - Lo que hace esta funcion es agregar objetos al carrito de compras.
            Los pasos que siguen es utilizar el if any() para verificar de que el producto que queremos
            agregar al carrito exista en el catalogo, para esto utiliamos el valor de "nombre_producto"
            como filtro, e iteramos a traves del catalogo de productos para encontrar coincidencias.

            2 - Luego de validar de que el producto exista, buscamos el producto el cual queremos agregar al carro de compras.

            3 - Utilizamos la funcion de Python: "lista.append(objeto)" para agregar un objeto a la lista.
            (En nuestro caso es "self.productos.append(producto)" siendo self.productos la lista y producto el objeto.). 
            
            Parametros:
            
            - nombre_producto:
                El nombre del producto que queremos agregar. Ej: Mochila.
            
            - catalogo:
                Es el objeto de tipo "Catalogo" que utiliza nuestro sistema para listar productos. 

        """
        if any(producto.nombre == nombre_producto for producto in catalogo.productos):
            for producto in catalogo.productos:
                if producto.nombre == nombre_producto:
                    self.productos.append(producto)
        else:
            return "[ERROR] El producto no esta en el catalogo."

    def quitar_del_carro(self, nombre_producto):
        """
            Lo mismo que en la funcion anterior para agregar productos al carrito.
            Solo que aqui utilizamos la funcion "lista.remove(objeto)" para eliminar objetos de la lista.        
        """
        if any(producto.nombre == nombre_producto for producto in self.productos):
            for producto in self.productos:
                if producto.nombre == nombre_producto:
                    self.productos.remove(producto)
        else:
            return "[ERROR] El producto no esta en el carrito."

    def listar_objetos_en_el_carrito(self):
        print("------------------------------------- CARRITO -------------------------------------\n")
        for producto in self.productos:
            print("{} | {}\t\t\t\t\t | $ {}\n".format(producto.codigo, producto.nombre, producto.obtener_precio()))

    def obtener_precio_final(self):
        """
            Primero se inicializamos los atributos "precio_final" y "descuento_total" en 0 para limpiar valores anteriores.
            Luego iteramos a traves del listado de productos y vamos sumando el valor del precio
            de cada producto al atributo "precio_final" y tambien obtenemos los descuentos y los vamos sumando a "descuento_total".

            Notese que para obtener estos valores de precio y descuentos accedemos a funciones que pertenecen al objeto "Producto".
            Por eso utilizamos el "." para acceder a estas funciones.
        """
        self.precio_final = 0
        self.descuento_total = 0
        for producto in self.productos:
            self.descuento_total += producto.obtener_descuento()
            self.precio_final += producto.obtener_precio()

    def limpieza_post_compra(self):
        """
            Se limpia el carrito al realizar la compra.
            Esto es necesario para que al finalizar la compra podamos tener todo en orden para realizar una nueva.
        """
        self.precio_final = 0
        self.descuento_total = 0
        self.productos = []
 
#    NOTA: "self" es una palabra reservada que se utiliza para acceder a atributos de nuestro objeto (clase).
#    Suele ser utilizada dentro de la misma clase para acceder a sus valores o modificarlos.

#    NOTA: recorda que con el . podes acceder a los distintos atributos del objeto (clase) y a funciones que pertenezcan al objeto.