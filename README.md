# Entrega-Final-Proyecto-de-clase-

Proyecto Estruc.de.Datos y Análisis de Algoritmos

Frank Sebastian Santamaria Lozano – 2211862

Fabian Ricardo Ardila Villarreal - 2230025

Eduar Andres Ortiz Martinez - 2141845

Kevin Yesid Vargas Ravelo – 2211253

24 de abril de 2024

2. Problema

Descripción del Problema

El proyecto se basa en la gestión de una biblioteca o un banco de libros y revistas donde cada usuario se puede registrar con una variedad de datos de contacto, puede adquirir una serie de libros que cambiaran a un estado de préstamo, lo que impedirá que otra persona pueda pedir ese mismo libro, por eso en caso de incumplir la devolución se generará una sanción que puede afectar un futuro préstamo.

Para facilitar la organización y el registro de los libros prestados y disponibles, estos están guardados por título, autor, año, edición y además un identificador que ayudara la búsqueda del mismo en el archivo presencial.

## Implementación con listas

Se aborda la implementación de una lista enlazada simple (ListaSE) en Python para almacenar elementos de cualquier tipo. la implementación de la ListaSE proporciona una estructura versátil y eficiente para gestionar colecciones de datos dinámicas, como las asociadas a un sistema de gestión de biblioteca. Esta estructura de datos proporciona operaciones clave como agregar elementos al inicio y final, buscar un elemento por valor, contar elementos y verificar si la lista está vacía. Además, se ha implementado un método adicional para mostrar los libros registrados a nombre de un usuario específico.
La lista enlazada se caracteriza por su capacidad de crecimiento dinámico y eficiencia en la inserción y eliminación de elementos. Cada nodo en la lista contiene datos y una referencia al siguiente nodo, lo que permite un acceso secuencial y eficiente a través de la lista.
El método adicional implementado permite buscar y mostrar los libros asociados a un usuario específico dentro de la lista. Esto facilita la gestión y visualización de los datos relacionados con los usuarios y los libros que tienen en préstamo o registro.

## Implementación con árboles

Además, se requiere la implementación de un árbol de búsqueda binaria en Python que permita insertar elementos, eliminarlos y buscarlos según el funcionamiento de los árboles BB.

Etapas desarrolladas:

Análisis de requisitos: Se identificaron los requisitos del sistema de la funcionalidad del árbol de búsqueda binaria que permita insertar elementos, eliminarlos y buscarlos según el funcionamiento de los árboles BB.

Implementación del sistema: Se desarrollo el sistema de la integración del árbol de búsqueda binaria en Python.

Pruebas y depuración: Se realización pruebas exhaustivas para garantizar el funcionamiento correcto del sistema y se corrigieron los erros identificados durante el proceso de prueba.

## Implementación con grafos

Un grafo es una estructura similar a un árbol pero con versatilidad aumentada, pues no limita las relaciones que puedan existir entre nodos. Debido a que esa característica es fundamental en un grafo, se quiso que la implementación no desaprovechara dicha versatilidad.

Para esta implementación se usó la librería igraph, ya que facilita mucho la creación y operaciones con grafos, además posee un método útil ( select( ) ) el cual genera listas de nodos (objeto vertexseq) que contiene los nodos que pasan por un determinado filtro.

Debido a la naturaleza del proyecto, se decidió que cada nodo del grafo representara un libro con sus metadatos adjuntos (nombre, autor, año, etc). Cada nodo añadido al grafo tendrá un código único basado en la información del libro que representa. Para las conexiones entre nodos se pensó que tal vez la opción mas apropiada sería relacionar los libros que contengan similitudes.

## Conclusiones


