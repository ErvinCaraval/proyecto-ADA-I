# El problema de la asociacion de deportes

### Análisis de Organización Deportiva

La asociación de deportes realiza un análisis detallado de su organización deportiva para asignar recursos de manera efectiva y mejorar el rendimiento. Aquí hay una descripción:

- La asociación cuenta con múltiples sedes en todo el país, cada una con equipos para diferentes deportes.
- Cada sede tiene varios equipos, donde cada equipo tiene un deporte definido y un número específico de jugadores.
- Los jugadores están caracterizados por un identificador único, nombre, edad y rendimiento (1-100).
- Se busca ordenar internamente los equipos por rendimiento de los jugadores y edad en caso de empate.
- A nivel de sede, se ordenan los equipos por su rendimiento promedio, priorizando mayor cantidad de jugadores en caso de empate.
- Las sedes se ordenan por el promedio de rendimientos de sus equipos, priorizando más jugadores en caso de empate.
- Se genera un ranking de todos los jugadores de todas las sedes ordenados por rendimiento para la toma de decisiones estratégicas.

Este análisis permitirá identificar equipos y jugadores destacados, así como áreas de mejora en la organización deportiva.


# Instrucciones de Ejecución

Este repositorio contiene dos archivos de código Python para implementaciones de estructuras de datos y algoritmos de ordenamiento. A continuación, se detallan las instrucciones para ejecutar cada archivo:

## Binary Search Tree con Quicksort

El archivo `binary_search_tree_quicksort.py` contiene una implementación de un árbol de búsqueda binaria y el algoritmo de ordenamiento Quicksort.

### Ejecución

1. Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde [python.org](https://www.python.org/) e instalarlo siguiendo las instrucciones adecuadas para tu sistema operativo.

2. Abre una terminal o línea de comandos.

3. Navega al directorio que contiene el archivo `binary_search_tree_quicksort.py`.

4. Ejecuta el siguiente comando: python binary_search_tree_quicksort.py

## Linked List con Heapsort

El archivo `linkedlist_heapsort.py` contiene una implementación de una lista enlazada y el algoritmo de ordenamiento Heapsort.

### Ejecución

1. Asegúrate de tener Python instalado en tu sistema.

2. Abre una terminal o línea de comandos.

3. Navega al directorio que contiene el archivo `linkedlist_heapsort.py`.

4. Ejecuta el siguiente comando: python linkedlist_heapsort.py

## Requisitos

- Python 3.x

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

## Descripción de las funciones de salida

### `mostrar_resultados_sedes(sedes)`
Esta función muestra los resultados de rendimiento de cada sede y sus respectivos equipos. Para cada equipo, se muestra su rendimiento promedio y la lista de jugadores ordenados por rendimiento.

### `mostrar_ranking_jugadores(jugadores)`
Muestra el ranking de jugadores ordenados por su rendimiento, desde el más alto hasta el más bajo.

### `mostrar_mejor_y_peor_jugador(jugadores)`
Muestra al jugador con el mayor y menor rendimiento en función de su puntaje de rendimiento.

### `mostrar_jugador_mas_joven_y_veterano(jugadores)`
Encuentra al jugador más joven y al más veterano en función de su edad.

### `mostrar_promedio_edad_y_rendimiento(jugadores)`
Calcula y muestra el promedio de edad y rendimiento de todos los jugadores.

### `mostrar_equipo_mejor_y_peor_rendimiento(sedes)`
Encuentra y muestra el equipo con el mayor y menor rendimiento entre todas las sedes. Se ordenan los equipos por rendimiento promedio.


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

## Descripción de las funciones de salida

### `mostrar_resultados_sedes(sedes)`
Esta función muestra los resultados de rendimiento de cada sede y sus respectivos equipos, junto con el rendimiento promedio de cada equipo y la lista de jugadores ordenados dentro de cada equipo.

### `mostrar_ranking_jugadores(jugadores)`
Esta función muestra el ranking de jugadores ordenados por su rendimiento, desde el más alto hasta el más bajo.

### `mostrar_mejor_y_peor_jugador(jugadores)`
Muestra al jugador con el mayor y menor rendimiento en función de su puntaje de rendimiento.

### `mostrar_jugador_mas_joven_y_veterano(jugadores)`
Muestra al jugador más joven y al más veterano en función de su edad.

### `mostrar_promedio_edad_y_rendimiento(jugadores)`
Calcula y muestra el promedio de edad y rendimiento de todos los jugadores.

### `mostrar_equipo_mejor_y_peor_rendimiento(sedes)`
Encuentra y muestra el equipo con el mayor y menor rendimiento entre todas las sedes.


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


## Descripción de los archivos de salida funciones de salida todos los  input.txt 

- **mostrar_resultados_sedes(sedes)**
- **mostrar_ranking_jugadores(jugadores)**
- **mostrar_mejor_y_peor_jugador(jugadores)**
- **mostrar_equipo_mejor_y_peor_rendimiento(sedes)**
- **mostrar_jugador_mas_joven_y_veterano(jugadores)**
- **mostrar_promedio_edad_y_rendimiento(jugadores)**

Estos archivos se utilizan como entrada para el programa y contienen datos de jugadores, equipos y sedes en un formato específico, y sus salidas que se visualizan por consola. 

