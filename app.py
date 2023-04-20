import pymysql as sql #Importar el controlador para la conexion a la base de datos

userBD = "root"
passBD = ""
baseDatos = "productospython" #Nombre de la base de datos
host = "localhost"

miConexion = sql.connect(host=host,user=userBD,passwd=passBD,db=baseDatos) #Obtener conexión

# -------------------------------------------------------------------------------------------------

#Agregar un producto a la tabla productos_python de la base de datos
def agregarProducto():
    try:
        codigo = 13
        nombre = "Televisor"
        precio = 2500000
        categoria = "Electrodomestico"
        #producto
        producto = (codigo,nombre,precio,categoria)
        #cursor
        cursor = miConexion.cursor() #cursos para realizar operaciones en la BD ejemplo, una consulta
        print(type(cursor))
        #agregar un producto
        consulta = "insert into productos_python values(null,%s,%s,%s,%s)" #texto de la consulta con los parametros requeridos de la tabla de la base de datos
        resultado = cursor.execute(consulta,producto) #ejecutar la consulta
        miConexion.commit() #aceptar la consulta (actualizar-eliminar-consultar)
        
        if(cursor.rowcount == 1): #cantidad de registro - un solo registro (mayor a cero)
            print("Producto registrado correctamente")
        else:
            print("¡Problemas al registrar el producto!")
            
    except sql.err as error:
        miConexion.rollback() #borra las modificaciones de datos realizados hasta un punto de retorno
        print(f"Problemas al agregar producto. Error: {error}")
        
# -------------------------------------------------------------------------------------------------

#Consultar un prodcto por código de la tabla productos_pyhon de la base de datos
def consultarProductoPorCodigo():
    try:
        codigo = 13 #código del producto a consultar
        producto = (codigo,) #tupla con los parametros, en este caso uno solo
        cursor = miConexion.cursor() #crear cursor
        consulta = "select * from productos_python where proCodigo=%s" #texto de la conslta
        resultado = cursor.execute(consulta,producto) #ejecutar consulta
        productoConsultado = cursor.fetchone() #Obtener los datos del producto (fetchAll - fetchmany)
        #imprimir producto  
        if(cursor.rowcount == 1): #>0
            print("\nProducto consultado:\n")
            print(productoConsultado)
            print(f"\nCódigo: {productoConsultado[1]}")
            print(f"Nombre: {productoConsultado[2]}")
            print(f"Precio: {productoConsultado[3]}")
            print(f"Categoria: {productoConsultado[4]}")
        else:
            print("¡No existe ningún producto con ese código!")
            
    except sql.err as error:
        miConexion.rollback() 
        print(f"Problemas al consultar el producto. Error: {error}")
    
# -------------------------------------------------------------------------------------------------

#Actualizar un producto de la tabla productos_python de la base de datos
def actualizarProducto():
    try:
        idProducto = 1 #id del producto a actualizar
        #Nuevos parametros del producto a actualiar
        nuevoCodigo = 24
        nuevoNombre = "Lavadora"
        nuevoPrecio = 185000000
        nuevaCategoria = "Electrodomestico"
        cursor = miConexion.cursor() #crear cursor
        productoActualizado = (nuevoCodigo,nuevoNombre,nuevoPrecio,nuevaCategoria,idProducto) #proctos con los valores a actualizar
        consulta = "update productos_python set proCodigo=%s, proNombre=%s, proPrecio=%s, proCategoria=%s where idProducto=%s" #texto de la cosulta para actualizar
        resultado = cursor.execute(consulta,productoActualizado) #ejecutar consulta
        miConexion.commit() #aceptar consulta (actualizar)
        if(cursor.rowcount == 1):
            print("Producto actualizado")
        else:
            print("¡NO es posible actualizar el producto, por favor revisar...!")
            
    except sql.err as error:
        miConexion.rollback() 
        print(f"Problemas al actualizar el producto. Error: {error}")
        
# -------------------------------------------------------------------------------------------------  

#Eliminar un producto de la tabla productos_python de la base de datos
def eliminarProducto():
    try:
        codigo = 10
        productoEliminar = (codigo,)
        cursor = miConexion.cursor()
        consulta = "delete from productos_python where proCodigo=%s"
        #consulta = f"delete from productos_python where proCodigo={codigo}"
        resultado = cursor.execute(consulta,productoEliminar)
        miConexion.commit() #se esta modificando la base de datos
        if(cursor.rowcount == 1):
            print("Producto eliminado")
        else:
            print("¡No es posible eliminar. No existe producto con ese código!")
        
    except miConexion.Error as error:
        miConexion.rollback() 
        print(f"Problemas al eliminar el producto. Error: {error}")
    
# -------------------------------------------------------------------------------------------------

#Lista todos los productos de la tabla productos_python de la base de datos
def  listarProductos():
    try:
        cursor = miConexion.cursor()
        consulta = "select * from productos_python"
        resultado = cursor.execute(consulta)
        listaProductos = cursor.fetchall()
        print(listaProductos)
        if(len(listaProductos)>0):
            for p in listaProductos:
                print(f"\nCódigo: {p[1]}")
                print(f"Nombre: {p[2]}")
                print(f"Precio: {p[3]}")
                print(f"Categoria: {p[4]}")
                print("-"*50)
        else:
            print("¡No hay productos registrados!")
        
    except miConexion.Error as error:
        print(f"{error}")
        
# -------------------------------------------------------------------------------------------------
        
#Agreagar varios productos a la tabla productos_python de la base de datos
def agregarVariosProductos():
    try:
        p1 = (20,"zapatos dama",233000,"Calzado")
        p2 = (21,"tenis tejo",199000,"Calzado")
        p3 = (22,"chaqueta jean",432000,"Ropa")
        p4 = (23,"Hoddie",120000,"Ropa")
        listaProductos = []
        listaProductos.append(p1)
        listaProductos.append(p2)
        listaProductos.append(p3)
        listaProductos.append(p4)
        cursor = miConexion.cursor()
        consulta = "insert into productos_python values(null,%s,%s,%s,%s)"
        resultado = cursor.executemany(consulta,listaProductos)
        miConexion.commit()
        if(cursor.rowcount >= 1):
            print("Productos registrados correctamente")
        else:
            print("¡Problemas al agregar los productos!")
        
    except miConexion.Error as error:
        miConexion.rollback()
        print(f"{error}") 
    
# -------------------------------------------------------------------------------------------------
    
#agregarProducto()
#consultarProductoPorCodigo()
#actualizarProducto()
#eliminarProducto()
#listarProductos()
#agregarVariosProductos()