# Descripción de archivos y su implementación

## linkedlist_heapsort.py

Este archivo contiene la implementación de dos estructuras de datos y sus algoritmos asociados:

### LinkedList

Una lista enlazada que se utiliza para almacenar jugadores y equipos. Tiene los siguientes métodos:

- `append(data)`: Agrega un elemento al final de la lista.
- `to_list()`: Convierte la lista enlazada a una lista de Python.
- `from_list(lst)`: Crea una lista enlazada a partir de una lista de Python.

### Funciones de ordenamiento:

- `heapify(arr, n, i, key)`: Convierte un arreglo en un montículo.
- `heapsort(arr, key)`: Ordena un arreglo utilizando heapsort.

### Clases:

- `Jugador`: Representa un jugador con atributos como id, nombre, edad y rendimiento.
- `Equipo`: Representa un equipo con jugadores. Tiene métodos para agregar jugadores, ordenarlos por rendimiento y calcular el rendimiento promedio del equipo.
- `Sede`: Representa una sede que contiene equipos. Tiene métodos para agregar equipos, ordenarlos por rendimiento y calcular el rendimiento promedio de la sede.

## binary_search_tree_quicksort.py

Este archivo contiene la implementación de un árbol de búsqueda binaria y el algoritmo de ordenamiento quicksort adaptado para trabajar con él.

### Clases:

- `TreeNode`: Representa un nodo de un árbol de búsqueda binaria.
- `BinarySearchTree`: Implementa un árbol de búsqueda binaria. Tiene métodos para insertar nodos y realizar un recorrido in-order.
- `Jugador`: Representa un jugador con atributos similares al archivo anterior.
- `Equipo`: Representa un equipo con jugadores, pero esta vez implementado utilizando un árbol de búsqueda binaria.
- `Sede`: Representa una sede que contiene equipos, similar al archivo anterior.

### Funciones de ordenamiento:

- `quicksort(arr, low, high, key)`: Ordena un arreglo utilizando el algoritmo quicksort adaptado para considerar el rendimiento y la edad en caso de empate.

---

