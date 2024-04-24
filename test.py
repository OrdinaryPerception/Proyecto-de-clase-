class Nodo_Libro:
    def __init__(self, Titulo, Autor, Año, Edicion, Identificador):
        self.titulo = Titulo
        self.autor = Autor
        self.año = Año
        self.edicion = Edicion
        self.identificador = Identificador
        self.izquierda=None
        self.derecha=None

class Arbol_Libros:
        # Funciones privadas
        def __init__(self, Titulo, Autor, Año, Edicion, Identificador):
            self.raiz = Nodo_Libro(Titulo, Autor, Año, Edicion, Identificador)
            
        def __crear_libro(self,Titulo, Autor, Año, Edicion, Identificador):
            return Nodo_Libro(Titulo, Autor, Año, Edicion, Identificador)
        

        def __agregar_recursivo(self,nodo,dato,Titulo, Autor, Año, Edicion, Identificador):
            if dato==None:
                dato=self.__crear_libro(Titulo, Autor, Año, Edicion, Identificador)
                
            if dato.identificador < nodo.identificador:
                if nodo.izquierda is None:
                    nodo.izquierda = dato
                else:
                    self.__agregar_recursivo(nodo.izquierda, dato,Titulo, Autor, Año, Edicion, Identificador)
            else:
                if nodo.derecha is None:
                    nodo.derecha = dato
                else:
                    self.__agregar_recursivo(nodo.derecha, dato,Titulo, Autor, Año, Edicion, Identificador)

        def __inorden_recursivo(self, nodo):
            if nodo is not None:
                self.__inorden_recursivo(nodo.izquierda)
                print(nodo.titulo, end=", ")
                self.__inorden_recursivo(nodo.derecha)

        def __buscar(self, nodo, busqueda):
            if nodo is None:
                return None
            if nodo.identificador == busqueda:
                return nodo
            if busqueda < nodo.identificador:
                return self.__buscar(nodo.izquierda, busqueda)
            else:
                return self.__buscar(nodo.derecha, busqueda)

        # Funciones públicas

        def agregar(self,Titulo=None, Autor=None, Año=None, Edicion=None, Identificador=None,dato=None ):
            self.__agregar_recursivo(self.raiz, dato,Titulo, Autor, Año, Edicion, Identificador)

        def inorden(self):
            print("Imprimiendo árbol inorden: ")
            self.__inorden_recursivo(self.raiz)
            print("")

        def buscar(self, busqueda):
            return self.__buscar(self.raiz, busqueda)


class Nodo_Usuarios:
    def __init__(self, Nombre ,Email, Estado, Codigo ):
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Email = Email
        self.Estado = Estado
        self.Libros_Prestados = Arbol_Libros("0","0",23,12,0)
        self.izquierda=None
        self.derecha=None
        

class Arbol_Usuarios:
    # Funciones privadas
    def __init__(self, Nombre ,Email, Estado,Codigo ):
        raiz=Nodo_Usuarios(Nombre ,Email, Estado,Codigo)
        self.raiz = raiz
        
    def __crear_usuario(self,Nombre ,Email, Estado,Codigo):
        return Nodo_Usuarios(Nombre ,Email, Estado,Codigo)

    def __agregar_recursivo(self,nodo,dato,Nombre,Email,Estado,Codigo):
        if dato==None:
            dato=self.__crear_usuario(Nombre,Email,Estado,Codigo)
            
        if dato.Codigo < nodo.Codigo:
            if nodo.izquierda is None:
                nodo.izquierda = dato
            else:
                self.__agregar_recursivo(nodo.izquierda, dato,Nombre,Email,Estado,Codigo)
        else:
            if nodo.derecha is None:
                nodo.derecha = dato
            else:
                self.__agregar_recursivo(nodo.derecha, dato,Nombre,Email,Estado,Codigo)

    def __inorden_recursivo(self, nodo):
        if nodo is not None:
            self.__inorden_recursivo(nodo.izquierda)
            print(nodo.Nombre, end=", ")
            self.__inorden_recursivo(nodo.derecha)

    def __buscar(self, nodo, busqueda):
        if nodo is None:
            return None
        if nodo.Codigo == busqueda:
            return nodo
        if busqueda < nodo.Codigo:
            return self.__buscar(nodo.izquierda, busqueda)
        else:
            return self.__buscar(nodo.derecha, busqueda)

    # Funciones públicas

    def agregar(self,Nombre=None,Email=None,Estado=None,Codigo=None,dato=None):
        self.__agregar_recursivo(self.raiz, dato,Nombre,Email,Estado,Codigo)

    def inorden(self):
        print("Imprimiendo árbol inorden: ")
        self.__inorden_recursivo(self.raiz)
        print("")

    def buscar(self, busqueda):
        return self.__buscar(self.raiz, busqueda)
    
    
ab=Arbol_Usuarios("Juan","nose","Activo",25)
ab.agregar("Pedro","nose","Activo",14)
ab.agregar("Jose","nose","Activo",10)
ab.inorden()
jose=ab.buscar(10)
jose.Libros_Prestados.agregar("XD","XD",2012,14,22)
jose.Libros_Prestados.inorden()
libro=jose.Libros_Prestados.buscar(22)
print(libro.titulo)