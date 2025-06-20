Interfaz Productos:
    -método obtener_costo_total(cantidad_noches)

Clase Vuelo implementa Productos:
    -variable fecha_ida (Tipo de Dato Fecha)
    -variable fecha_vuelta (Tipo de Dato Fecha, vuelta se chequea que sea mayor a fecha_ida)
    -variable Aerolinea (No habla mucho del mismo, asumo es un tipo String con el nombre de la empresa con la que  se viajo)
    -variable Precio (Cada Vuelo/Viaje tiene su propio Precio determinado)
    - método obtener_costo_total(cantidad_noches) (devuelve cuando cuesta en total, en base a cantidad de ambientes y noches, noche no parece ser necesario para vuelo por ende su valor default es 0)

Interfaz Alojamiento:
    -método getdomicilio (interpreto que los alojamientos tienen en comun que todos se puede consultar su domicilio)

Clase Hotel implementa interfaz Alojamiento,Productos:
    - variable domicilio (Coherente al imprementar la interfaz, un string con la dirección del Hotel )
    - variable nombre (Nombre del Hotel String) 
    - variable cantidad_estrellas (Cantidad de estrellas del Hotel int)
    - variable precio_cantidad_estrellas (Precio por Cantidad de estrellas del Hotel float)
    - método getdomicilio (devuelve el domicilio del Hotel)
    - método obtener_costo_total(cantidad_noches) (devuelve cuando cuesta en total, en base a cantidad de noches, el precio por estrella y la cantidad de estrellas, float)

Hotel->obtener_costo_total(cantidad_noches):
    return precio_cantidad_estrellas*cantidad_estrellas*cantidad_noches

Clase CasaDepartamento implementa interfaz Alojamiento,Productos:
    - variable domicilio (Coherente al imprementar la interfaz, un string con la dirección de la Casa/Departamento)
    - variable cantidad_ambientes (Cantidad ambientes de casa/departamento int)
    - método getdomicilio (devuelve el domicilio de la Casa/Departamento)
    - método obtener_costo_total(cantidad_noches) (devuelve cuando cuesta en total, en base a cantidad de ambientes y noches)

#Solo se ameritaria un Strategy, si la forma de calculo fueran algorimia muy distinta para Casa/Departamento
#Por limitacion de tiempo hardcodeo los valores de calculo, deberian ser variables o clase de calculo auxiliar...
CasaDepartamento->obtener_costo_total(cantidad_noches):
    if cantidad_ambientes == 1: return 15000*cantidad_noches
    elseif cantidad_ambientes >= 2 and cantidad_ambientes <= 4: return 30000*cantidad_noches
    elseif return 50000*cantidad_noches

#Se indentifica el patron Composite para resolver lo de Paquetes ya que es una composicion o no de productos
Clase Paquete implements Productos:
    -variable productos: List<Productos>  (Lista de Productos)

    Paquete->agregar producto(Producto):
        productos.add(Producto)

    Paquete->quitar_producto(Producto):
        productos.remove(Producto)

    Paquete->obtener_costo_total(cantidad_noches):
        costo_total = 0
        for each producto in productos:
            costo_total = costo_total + costo_total.obtener_costo_total(cantidad_noches)
        return costo_total

Clase Usuario:
    -variable nombre_usuario (String nombre usuario)
    -variable productos_contratados (Listado de Productos Contratados)
    -variable presupuesto (Float el presupuesto el usuario en especifico para contratar Productos)
    -metodo contratarProducto(cantidad_noches) (dado un producto verifica si puede contratarlo, de hacerlo se agrega a productos contratados y se descuenta del presupuesto)

Usuario->contratarProducto(Producto):
    costo_total_producto = Producto.obtener_costo_total(cantidad_noches)
    if presupuesto >= costo_total_producto:
        productos_contratados.add(Producto)
        presupuesto = presupuesto -= costo_total_producto
    elseif return "No es posible contratar $Producto con el presupuesto $presupuesto"

"Se utiliza un Quick Sort modificado, no es de me interes la algoritmia del mismo, resuelve el item obligatorio solicitado de mostrar listado descendente"
// Función para obtener la cantidad de productos contratados por un usuario
Funcion ObtenerCantidadProductos(usuario):
    Retornar Longitud(usuario.productos_contratados)
// Algoritmo de Ordenamiento Quick Sort Modificado (Descendente)
Funcion OrdenarUsuariosPorProductos(lista_usuarios):
    Si Longitud(lista_usuarios) <= 1 Entonces
        Retornar lista_usuarios
    
    // Seleccionar un pivote (por simplicidad, elegimos el elemento del medio)
    pivote_usuario = lista_usuarios[Longitud(lista_usuarios) / 2]
    pivote_cantidad = ObtenerCantidadProductos(pivote_usuario)

    menores = Lista Vacia
    mayores = Lista Vacia
    iguales = Lista Vacia

    Para Cada usuario En lista_usuarios:
        cantidad_productos = ObtenerCantidadProductos(usuario)
        Si cantidad_productos > pivote_cantidad Entonces
            Agregar usuario A mayores
        Sino Si cantidad_productos < pivote_cantidad Entonces
            Agregar usuario A menores
        Sino
            Agregar usuario A iguales
    
    // Concatenar las sublistas ordenadas
    Retornar Concatenar(OrdenarUsuariosPorProductos(mayores), iguales, OrdenarUsuariosPorProductos(menores))

"Cuando deba informarse el item obligatorio del listado simplemente se llama a la función pasando una lista de usuarios List<Usuarios> y listo"
lista_usuarios_ordenada = OrdenarUsuariosPorProductos(lista_de_usuarios)

#Finalmente es de suma importancia considerar las Cabañas un caso particular a modelar
Clase Cabaña implementa Productos:
    -variable casas: List<CasaDepartamentoCabaña>
    "Limitación de tiempo... el razonamiento es el siguiente la entidad usuario contratante seria el usuario que pudo contratar una casa ya se individual o grupal con su respectivo descuento"
    "Tal vez no es la mejor decisión de diseño, pero me permite resolver la funcionalidad..."
    -variable usuarios_contratante: List<UsuarioContratante>
    "Noto algo interesante sobre el mismo, se agrega el hecho que puede ser individual o grupal..."
    "La entidad CasaDepartamentoCabaña ademas de tener una Casa dice si esta habilitada para compra o no"
    metodo obtener_costo_total(ListadoCasasAQuererContratar, cantidad_noches):
       List<CasaDepartamentoCabaña> CasasAQuererContratar = casas.find(CasasAQuererContratar)
        "evidentemente si no esta habilitada la casa para comprar se tira un error..."

        si esta todo ok "EN BASE A LO DEDUCIDO por 122, tengo que buscar si el usuario tiene descuento por ende el costo total ya no es costo total si no costo total*descuento si contrato mas de 1 casa en la cabaña"
            for casas each CasasAQuererContratar:
                costo_total = costo_total + casas.obtener_costo_total(cantidad_noches)
            return costo_total * descuento_usuario (se obtiene de recorrer usuario_contratante si y solo si se encuentra en ese listado...)
    "aca hay un pequeño dilema, por tema de cohesion yo no soy el encargado de manejo de presupuesto del usuario en esta entidad"
    "una forma de subsanarlo es si es una cabaña en la algoritmia de usuario al "contratar" debe haber algo intermedio o un llamado postoperacion que permita hacer lo siguiente"
        "método que se ejecuta solo si el usuario tiene presupuesto para contratarlo"
        metodo_clave(ListadoCasasAQuererContratar):
            for casasContratadas each casas:
                "limitacion de tiempo"
                simplemente marcar la casa como contratada (lógico)
            if no exite usuario en usuario_contratante: usuarios_contratante.add (UsuarioContratente) //esta accion solo se realiza si es la primera vez es para guardar el usuario y se guarda con el primer descuento
            elseif: caso contrario se busca el usuario contratante y se le actualiza el descuento, recordar limitación de maximo 50%

    "!!!Por ende la solución es el usuario antes de agregarse el producto si le da el presupuesto es llamar a este metodo_clave y pasarse el usuario, como es peculiar de Cabaña, solo cabaña hace operatorio  con metodo_clave, en el resto de los productos sería ignorado osea no ejecuta nada..."