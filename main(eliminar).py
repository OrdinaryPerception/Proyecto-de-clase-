import igraph as ig

class Tematicas:
    def __init__(self):
        self.tematicas = ["Sin clasificar","arte","Autoayuda y espiritualidad","Ciencias Humanas",
                        "Ciencias","Cocina","Cómics y manga infantil y juvenil","Cómics","Derecho",
                        "Economía y empresa","Filología","Guías de viaje","Historia","Idiomas","Infantil",
                        "Informática","Ingeniería","Juvenil","Libros de texto y formación",
                        "Literatura en otros idiomas","Literatura","Medicina",
                        "Ocio y deporte","Oposiciones","Psicología y pedagogía","Salud y dietas"]
        
    def agregar_temática(self, tematica): 
        self.tematicas.append(tematica)
        print(f'''La temática: "{tematica}", ha sido agregada 
            correctamente en la posición {self.tematicas.index(tematica)}''')
    
    def eliminar_temática(self, tematica): 
        if tematica in self.tematicas:
            self.tematicas.remove(tematica)
            print("La tematica se eliminó correctamente")
        else:
            print("La tematica no se encuentra registrada")

class Codigo:
    def __init__(self, objeto_tematica):
        self.tematicas = objeto_tematica
    
    def __fase_1(self, nodo, codigo): 
        for tupla in enumerate(self.tematicas.tematicas): 
            if nodo["Tematica"] == tupla[1]:
                if tupla[0] < 10:
                    codigo = "0" + str(tupla[0])  
                else:
                    codigo = str(tupla[0])
        else:
            return self.__fase_2(nodo, codigo)
                
    def __fase_2(self, nodo, codigo): 
        codigo += str(nodo["Año"]) 
        return self.__fase_3(nodo, codigo) 
    
    def __fase_3(self, nodo, codigo): 
        codigo += nodo["name"][0] + nodo["name"][1]  
        return self.__fase_4(nodo, codigo)
    
    def __fase_4(self, nodo, codigo): 
        codigo += nodo["Autor"][0] + nodo["Autor"][1] 
        return self.__fase_5(nodo, codigo) 
    
    def __fase_5(self, nodo, codigo): 
        codigo += "0"
        print(f"Se ha creado el código: {codigo}")
        return codigo
        
    def obtener_codigo_coincidencia(self, nodo):
        if nodo["Codigo"] == 0: 
            return self.crear_codigo(nodo)
        else:
            codigo = nodo["Codigo"]
            fase_5 = int(codigo[len(codigo)-1])
            anterior_elemento = codigo[len(codigo)-2]
            codigo_antiguo = codigo
            codigo_nuevo = codigo.replace(anterior_elemento + str(fase_5), anterior_elemento + str(fase_5 + 1))
            print(f"Se ha actualizado el codigo de {codigo_antiguo} a {codigo_nuevo}")
            return codigo_nuevo
    
    def crear_codigo(self, nodo):
        return self.__fase_1(nodo, codigo=0)

class Coleccion:
    def __init__(self):
        self.grafo = ig.Graph()
        self.tematicas = Tematicas()
        self.objeto_codigo = Codigo(self.tematicas)
        self.metadatos = ["name", "Autor", "Tematica", "Año", "Edicion"]
        self.num_vertices = 0
        self.SIN_CLASIFICAR = self.tematicas.tematicas[0]
    
    def __encontrar_vertices(self, indice_vertice):
        metadatos = {self.grafo.vs[indice_vertice][metadato] for metadato in self.metadatos} 
        vertices_similares = self.grafo.vs.select(lambda vertex: len(metadatos.intersection({vertex[metadato] for metadato in self.metadatos})) > 0)
        return vertices_similares
        
    def __crear_arcos(self, indice_vertice):
        if self.grafo.vcount() != 0: 
            vertices_similares = self.__encontrar_vertices(indice_vertice)
            for vs in vertices_similares:
                if len(self.grafo.es.select(_within=[vs.index, indice_vertice])) == 0:
                    self.grafo.add_edge(indice_vertice, vs.index) 
    
    def añadir_libro(self, Titulo, Autor, Año, Edicion, Tematica=None):
        metadatos = ["name", "Autor", "Tematica", "Año", "Edicion"]
        metadatos_2 = [Titulo, Autor, Tematica, Año, Edicion]
        
        if Tematica is None:
            Tematica = self.SIN_CLASIFICAR
            metadatos_2 = [Titulo, Autor, Tematica, Año, Edicion]
        elif Tematica not in self.tematicas.tematicas:
            print("La tematica ingresada no esta registrada") 
        else:
            self.grafo.add_vertex(str(self.num_vertices))
            for metadato_nombre, metadato in zip(self.metadatos, metadatos_2):
                self.grafo.vs[self.num_vertices][metadato_nombre] = metadato
            else:
                self.grafo.vs[self.num_vertices]["Titulo"] = Titulo
                self.grafo.vs[self.num_vertices]["Codigo"] = 0
                codigo = self.objeto_codigo.crear_codigo(self.grafo.vs[self.num_vertices])
                
                nodos_codigo_igual = self.grafo.vs.select(Codigo_eq=codigo)
                
                while len(nodos_codigo_igual) > 0:
                    codigo = self.objeto_codigo.obtener_codigo_coincidencia(nodos_codigo_igual[0])
                    nodos_codigo_igual = self.grafo.vs.select(Codigo_eq=codigo)
                    
                self.grafo.vs[self.num_vertices]["Codigo"] = codigo
                self.__crear_arcos(self.num_vertices)
        
            self.num_vertices += 1
    
    def eliminar_libro(self, indice_libro):
        if indice_libro < self.grafo.vcount():
            self.grafo.delete_vertices(indice_libro)
            self.num_vertices -= 1
            print(f"Se ha eliminado el libro en el índice {indice_libro}")
        else:
            print(f"No existe ningún libro en el índice {indice_libro}")

    def mostrar_coleccion(self):
        print(self.grafo)
        print([x for x in self.grafo.vs])
        
    def obtener_adyacencia(self, indice_nodo):
        nodo = indice_nodo
        mode = "all"
        incidents = self.grafo.incident(nodo, mode)
        print(f'''El nodo {nodo} con nombre {self.grafo.vs[nodo]['name']} 
            tiene los siguientes arcos incidentes: {incidents}, 
            y la siguiente lista de adyacencia {[self.grafo.vs[self.grafo.es[a].tuple[0]]['name'] for a in incidents]}''')
        
        # Crear una instancia de la colección de libros
coleccion = Coleccion()

# Añadir algunos libros a la colección
coleccion.añadir_libro("El Aleph", "Jorge Luis Borges", 1949, 1, "Literatura")
coleccion.añadir_libro("Cien años de soledad", "Gabriel García Márquez", 1967, 1, "Literatura")
coleccion.añadir_libro("Python for Data Analysis", "Wes McKinney", 2012, 2, "Informática")

coleccion.mostrar_coleccion()

coleccion.eliminar_libro(1)

coleccion.mostrar_coleccion()

coleccion.obtener_adyacencia(0)
