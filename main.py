import igraph as ig
import scipy.io as sio
import numpy as np


class Tematicas:
    def __init__(self):
        self.tematicas=["Sin clasificar","arte","Autoayuda y espiritualidad","Ciencias Humanas",
                   "Ciencias","Cocina","Cómics y manga infantil y juvenil","Cómics","Derecho",
                   "Economía y empresa","Filología","Guías de viaje","Historia","Idiomas","Infantil",
                   "Informática","Ingeniería","Juvenil","Libros de texto y formación",
                   "Literatura en otros idiomas","Literatura","Medicina",
                   "Ocio y deporte","Oposiciones","Psicología y pedagogía","Salud y dietas"]
        
    def agregar_temática(self,tematica): #temática:String
        self.tematicas.append(tematica)
        print(f'''La temática: "{tematica}", ha sido agregada 
              correctamente en la posicion {self.tematicas.index(tematica)}''')
    
    def eliminar_temática(self,tematica): #tematica:String
        
        if tematica in self.tematicas:
            self.tematicas.remove(tematica)
            print("La tematica se eliminó correctamente")
        else:
            print("La tematica no se encuentra registrada")
            
class Codigo:
    def __init__(self,nodo,objeto_tematica):
        self.codigo=0
        self.tematicas=objeto_tematica
        self.nodo=nodo #fase1fase2fase3fase4fase5
    
    def __fase_1(self): #En base a la temática del libro
        for tupla in enumerate(self.tematicas.tematicas): #tupla: (indice,tematica)
            if self.nodo["Tematica"]==tupla[1]:
                if tupla[0]<10:
                    self.codigo="0"+str(tupla[0])  #Pone un cero delante del indice
                else:
                    self.codigo=str(tupla[0])
                
    
    def __fase_2(self): #En base al año de publicacion
        self.codigo+=str(self.nodo["Año"])  
    
    def __fase_3(self): #En base a los primeros dos caracteres del titulo
        self.codigo+=self.nodo["name"][0]+self.nodo["name"][1]  
    
    def __fase_4(self): #En base a los primeros dos caracteres del autor
        self.codigo+=self.nodo["Autor"][0]+self.nodo["Autor"][1]  
    
    def __fase_5(self): #Fase para enumerar coincidencias
        pass   
    
    def crear_codigo(self):
        pass
            
            

class Coleccion:
    def __init__(self):
        self.grafo=ig.Graph()
        self.tematicas=Tematicas()
        self.metadatos=["name","Autor","Tematica","Año","Edicion"]
        self.num_vertices=0
        self.SIN_CLASIFICAR=self.tematicas.tematicas[0]
        
    def __comparar_atributos(self,vertice1,vertice2):
        for metadato in self.metadatos:
            if vertice1[metadato]==vertice2[metadato]:return True
        else:
            return False
        
        
    def __encontrar_vertices(self,indice_vertice):
        vertice=self.grafo.vs[indice_vertice]
        metadatos={self.grafo.vs[indice_vertice][metadato] for metadato in self.metadatos} #inserto todos los metadatos del vertice creado en un conjunto
        metadatos_lista=list(metadatos)
        vertices_similares=self.grafo.vs.select(lambda vertex: len(metadatos.intersection({vertex[metadato] for metadato in self.metadatos}))>0)
        return vertices_similares.select(name_ne=metadatos_lista[0],Autor_ne=metadatos_lista[1],Tematica_ne=metadatos_lista[2],Año_ne=metadatos_lista[3],Edicion_ne=metadatos_lista[4])
        
        #vertex.index
    def __crear_arcos(self,indice_vertice):
        if self.grafo.vcount()!=0:
            vertices_similares=self.__encontrar_vertices(indice_vertice)
            for vs in vertices_similares:
                self.grafo.add_edge(indice_vertice,vs.index) 
    
    def añadir_libro(self,Titulo,Autor,Año,Edicion,Tematica=None):
        metadatos=["name","Autor","Tematica","Año","Edicion"]
        metadatos_2=[Titulo,Autor,Tematica,Año,Edicion]
        
        if Tematica is None:
            Tematica=self.SIN_CLASIFICAR
            metadatos_2=[Titulo,Autor,Tematica,Año,Edicion]
        elif Tematica not in self.tematicas.tematicas:
            print("La tematica ingresada no esta registrada")
        elif 
        else:
            self.grafo.add_vertex(self.num_vertices)
            for metadato_nombre,metadato in zip(self.metadatos,metadatos_2):
                self.grafo.vs[self.num_vertices][metadato_nombre]=metadato
            else:
                self.grafo.vs[self.num_vertices]["Titulo"]=Titulo
                self.__crear_arcos(self.num_vertices)
        
            self.num_vertices+=1
    
    def mostrar_coleccion(self):
        #ig.plot(self.grafo,bbox=(0,0,500,500))
        print(self.grafo)
        print([x for x in self.grafo.vs])
        
        
    def obtener_adyacencia(self,indice_nodo):
        nodo=indice_nodo
        mode="all"
        incidents=self.grafo.incident(nodo,mode)
        print(f'''El nodo {nodo} con nombre {self.grafo.vs[nodo]['name']} 
            tiene los siguientes arcos incidentes: {incidents}, 
            y la siguiente lista de adyacencia {[self.grafo.vs[self.grafo.es[a].tuple[0]]['name'] for a in incidents]}''')
            
        


