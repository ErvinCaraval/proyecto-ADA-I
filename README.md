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

# Archivos de entrada y salida para las  versiónes  del programa

En este proyecto, los archivos `input1a.txt`, `input1b.txt`, `input2a.txt`, `input2b.txt`, `input3a.txt`, `input3b.txt`, `input4a.txt`, `input4b.txt`,`input5a.txt`,`input5b.txt`, `input6a.txt` y `input6b.txt` contienen datos de entrada  y las respectivas salidas para probar el programa, los archivos input.txt que tinen letra "a" son las pruebas de la version realizada con linkedlist_heapsort.py y los archivos con  letra "b" son las pruebas de binary_search_tree_quicksort.py .

## Descripción de los archivos de entrada y salida

### input1a.txt / input1b.txt

- **Tamaño de entrada de jugadores:** 12
- **Tamaño de entrada de equipos:** 4
- **Tamaño de entrada de sedes:** 2

### input2a.txt / input2b.txt

- **Tamaño de entrada de jugadores:** 20
- **Tamaño de entrada de equipos:** 6
- **Tamaño de entrada de sedes:** 2

### input3a.txt / input3b.txt

- **Tamaño de entrada de jugadores:** 60
- **Tamaño de entrada de equipos:** 15
- **Tamaño de entrada de sedes:** 3

### input4a.txt / input4b.txt

- **Tamaño de entrada de jugadores:** 100
- **Tamaño de entrada de equipos:** 15
- **Tamaño de entrada de sedes:** 3

### input5a.txt / input5b.txt

- **Tamaño de entrada de jugadores:** 100
- **Tamaño de entrada de equipos:** 20
- **Tamaño de entrada de sedes:** 4

### input6a.txt / input6b.txt

- **Tamaño de entrada de jugadores:** 200
- **Tamaño de entrada de equipos:** 40
- **Tamaño de entrada de sedes:** 8

Estos archivos se utilizan como entrada para el programa y contienen datos de jugadores, equipos y sedes en un formato específico, y sus salidas que se visualizan por consola. 

