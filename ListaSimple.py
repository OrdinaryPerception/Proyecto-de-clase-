from contextlib import nullcontext
from operator import truediv


class Nodo_Usuarios:
    def __init__(self, Nombre ,Email, Estado, Libros_Prestados  ):
        self.Nombre = Nombre
        self.Email = Email
        self.Estado = Estado
        self.Libros_Prestados = Libros_Prestados
        self.siguiente = None

class Nodo_Libro:
    def __init__(self, Titulo, Autor, Año, Edicion, Identificador):
        self.titulo = Titulo
        self.autor = Autor
        self.año = Año
        self.edicion = Edicion
        self.identificador = Identificador
        self.siguiente = None

class Lista_Usuarios:
    def __init__(self):
        self.cabeza = None
        
    
#Funcion para Imprimir la lista
    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.Nombre, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
#Funcion para agregar al inicio
    def agregarInicio(self, Nombre ,Email, Estado, Libros_Prestados):
        nuevo_nodo = Nodo_Usuarios(Nombre ,Email, Estado, Libros_Prestados)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            

    #Función para buscar elemento por valor
    def buscarElemento(self, Nombre):
    
        elementoActual = self.cabeza

        while elementoActual != None:
            if elementoActual.Nombre is Nombre: return elementoActual
            else: 
                print("El elemento no Se encontro")
                elementoActual = elementoActual.siguiente
        
        return False


    #Función para contar cuántos elementos tiene la lista
    def contarElementos(self):

        longitud = 0

        elementoActual = self.cabeza

        while elementoActual != None:
            elementoActual = elementoActual.siguiente
            longitud += 1
        
        return longitud

    #Función para indicar si la lista está vacía
    def estaVacia(self):

        if self.cabeza is None: 
            return True
        else: return False
        
    #Funcion Propia
    def Imprimir_Libros(self,Nombre):
        if self.buscarElemento(Nombre) is not None:
            self.buscarElemento(Nombre).Libros_Prestados.imprimir_lista()
        

#Fin de la lista_Usuarios




class Lista_Libros:
    def __init__(self):
        self.cabeza = None
        
    
#Funcion para Imprimir la lista
    def imprimir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual is not None:
            print(nodo_actual.titulo, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")
#Funcion para agregar al inicio
    def agregarInicio(self, Titulo, Autor, Año, Edicion, Identificador):
        nuevo_nodo = Nodo_Libro(Titulo, Autor, Año, Edicion, Identificador)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            return
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
            
    #Función para buscar elemento por valor
    def buscarElemento(self, elemento):

        elementoActual = self.cabeza

        while elementoActual != None:
            if elementoActual.titulo is elemento: 
                print("true")
                return True
            else: 
                print("false")
                elementoActual = elementoActual.siguiente
        return False


    #Función para contar cuántos elementos tiene la lista
    def contarElementos(self):

        longitud = 0

        elementoActual = self.cabeza

        while elementoActual != None:
            elementoActual = elementoActual.siguiente
            longitud += 1
        
        return longitud

    #Función para indicar si la lista está vacía
    def estaVacia(self):

        if self.cabeza is None: 
            return True
        else: return False

#Fin de la lista_Usuarios


#Prueba de funciones y comandos
Lista1 = Lista_Usuarios()
ListaSimple = Lista_Libros()
print(ListaSimple.estaVacia())
ListaSimple.agregarInicio("calculo2", "Zill" , 2008, 3, "sadasdf")
print(ListaSimple.estaVacia())
print(ListaSimple.contarElementos())
ListaSimple.imprimir_lista()
ListaSimple.buscarElemento("calculo2")

print("\nSiguiente\n")


print(Lista1.estaVacia())
Lista1.agregarInicio("Juan" , "kadsk", "Activo" , ListaSimple)
print(Lista1.estaVacia())
print(Lista1.contarElementos())
Lista1.imprimir_lista()
Lista1.Imprimir_Libros("Juan")
Lista1.buscarElemento("Juan")
