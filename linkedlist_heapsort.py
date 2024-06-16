class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def to_list(self):
        lst = []
        current = self.head
        while current:
            lst.append(current.data)
            current = current.next
        return lst
    def __iter__(self):
        self.current = self.head
        return self

    def __next__(self):
        if self.current:
            data = self.current.data
            self.current = self.current.next
            return data
        else:
            raise StopIteration

    def from_list(self, lst):
        for item in lst:
            self.append(item)

def heapify(arr, n, i, key=lambda x: x, consider_age=True):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    elif consider_age and l < n and key(arr[l]) == key(arr[largest]) and hasattr(arr[l], 'edad'):
        largest = l

    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r
    elif consider_age and r < n and key(arr[r]) == key(arr[largest]) and hasattr(arr[r], 'edad'):
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key, consider_age)

def heapsort(arr, key=lambda x: x, consider_age=True):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key, consider_age)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key, consider_age)


class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"{self.id}"

class Equipo:
    def __init__(self, deporte, sede):
        self.deporte = deporte
        self.sede = sede
        self.jugadores = LinkedList()

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def ordenar_jugadores(self):
        jugadores_list = self.jugadores.to_list()
        heapsort(jugadores_list, key=lambda x: (x.rendimiento, -x.edad))
        self.jugadores = LinkedList()
        self.jugadores.from_list(jugadores_list)

    def rendimiento_promedio(self):
        jugadores_list = self.jugadores.to_list()
        return sum(j.rendimiento for j in jugadores_list) / len(jugadores_list) if jugadores_list else 0

    def __repr__(self):
        ids = ', '.join(str(j) for j in self.jugadores)
        return f"{self.deporte}, Rendimiento: {self.rendimiento_promedio()}\n{{ {ids} }}"


class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = LinkedList()

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def ordenar_equipos(self):
        equipos_list = self.equipos.to_list()
        heapsort(equipos_list, key=lambda x: (sum(j.rendimiento for j in x.jugadores.to_list()) / len(x.jugadores.to_list()), len(x.jugadores.to_list())))
        self.equipos = LinkedList()
        self.equipos.from_list(equipos_list)

    def rendimiento_promedio(self):
        equipos_list = self.equipos.to_list()
        total_rendimiento = sum(equipo.rendimiento_promedio() for equipo in equipos_list)
        return total_rendimiento if equipos_list else 0

    def __repr__(self):
        equipos_str = '\n\n'.join(str(e) for e in self.equipos)
        return f"{self.nombre}, Rendimiento: {self.rendimiento_promedio()}\n\n{equipos_str}"


# Función para mostrar resultados de las sedes
# Corrección en la función mostrar_resultados_sedes
def mostrar_resultados_sedes(sedes):
    for sede_nombre, sede in sedes.items():
        print(f"Sede {sede_nombre}, Rendimiento: {sede.rendimiento_promedio()}\n")
        for equipo in sede.equipos:
            print(f"{equipo.deporte}, Rendimiento: {equipo.rendimiento_promedio()}")
            equipo.ordenar_jugadores()  # Corregido aquí
            jugadores = ', '.join(str(j) for j in equipo.jugadores.to_list())
            print(f"Jugadores: {{ {jugadores} }}")
            print()

# Corrección en la función mostrar_ranking_jugadores
def mostrar_ranking_jugadores(jugadores):
    heapsort(jugadores, key=lambda x: x.rendimiento)
    ranking_jugadores = ', '.join(str(j.id) for j in jugadores)
    print(f"Ranking Jugadores:\n{{ {ranking_jugadores} }}\n")

# Función para mostrar al jugador con mayor y menor rendimiento
def mostrar_mejor_y_peor_jugador(jugadores):
    jugador_mayor_rendimiento = jugadores[-1]
    jugador_menor_rendimiento = jugadores[0]
    print(f"Jugador con mayor rendimiento: {{ {jugador_mayor_rendimiento.id} , {jugador_mayor_rendimiento.nombre} , {jugador_mayor_rendimiento.rendimiento} }}")
    print(f"Jugador con menor rendimiento: {{ {jugador_menor_rendimiento.id} , {jugador_menor_rendimiento.nombre} , {jugador_menor_rendimiento.rendimiento} }}\n")

# Función para mostrar al jugador más joven y más veteran
def mostrar_jugador_mas_joven_y_veterano(jugadores):
    jugador_mas_joven = jugadores[0]
    jugador_mas_veterano = jugadores[0]

    for jugador in jugadores:
        if jugador.edad < jugador_mas_joven.edad:
            jugador_mas_joven = jugador
        if jugador.edad > jugador_mas_veterano.edad:
            jugador_mas_veterano = jugador

    print(f"jugador mas joven: {{ {jugador_mas_joven.id} , {jugador_mas_joven.nombre} , {jugador_mas_joven.edad} }}")
    print(f"jugador mas veterano: {{ {jugador_mas_veterano.id} , {jugador_mas_veterano.nombre} , {jugador_mas_veterano.edad} }}\n")

# Función para calcular y mostrar el promedio de edad y rendimiento de los jugadores
def mostrar_promedio_edad_y_rendimiento(jugadores):
    edades = [jugador.edad for jugador in jugadores]
    rendimientos = [jugador.rendimiento for jugador in jugadores]
    promedio_edad = sum(edades) / len(edades)
    promedio_rendimiento = sum(rendimientos) / len(rendimientos)
    print("\nPromedio de edad de los jugadores:", promedio_edad)
    print("Promedio de rendimiento de los jugadores:", promedio_rendimiento)

# Función para encontrar el equipo con mayor y menor rendimiento
def mostrar_equipo_mejor_y_peor_rendimiento(sedes):
    todos_los_equipos = []

    for sede in sedes.values():
        todos_los_equipos.extend(sede.equipos.to_list())

    # Ordenar todos los equipos por rendimiento promedio
    heapsort(todos_los_equipos, key=lambda x: x.rendimiento_promedio(),consider_age=True)

    # Equipo con mayor y menor rendimiento
    equipo_mayor_rendimiento = todos_los_equipos[-1] if todos_los_equipos else None
    equipo_menor_rendimiento = todos_los_equipos[0] if todos_los_equipos else None

    # Obtener la sede de cada equipo
    sede_equipo_mayor = "N/A" if not equipo_mayor_rendimiento else next((sede for sede, s in sedes.items() if equipo_mayor_rendimiento in s.equipos.to_list()), None)
    sede_equipo_menor = "N/A" if not equipo_menor_rendimiento else next((sede for sede, s in sedes.items() if equipo_menor_rendimiento in s.equipos.to_list()), None)

    print("Equipo con mayor rendimiento entre las sedes:", end=" ")
    if equipo_mayor_rendimiento:
        print(f"{equipo_mayor_rendimiento.deporte} en {sede_equipo_mayor}")
    else:
        print("N/A")

    print("Equipo con menor rendimiento entre las sedes:", end=" ")
    if equipo_menor_rendimiento:
        print(f"{equipo_menor_rendimiento.deporte} en {sede_equipo_menor}")
    else:
        print("N/A")



input1 = "input 1"
print("#" * 50)
print("{:^50}".format("input 1"))
print("#" * 50)
print(input1)
with open("inputs/input1a.txt", "r") as file:
    codigo = file.read()


exec(codigo)

input2 = "input 2"
print("#" * 50)
print("{:^50}".format("input 2"))
print("#" * 50)
print(input2)
with open("inputs/input2a.txt", "r") as file:
    codigo = file.read()


exec(codigo)


input3 = "input 3"
print("#" * 50)
print("{:^50}".format("input 3"))
print("#" * 50)
print(input3)
with open("inputs/input3a.txt", "r") as file:
    codigo = file.read()

exec(codigo)


input4 = "input 4"
print("#" * 50)
print("{:^50}".format("input 4"))
print("#" * 50)
print(input4)
with open("inputs/input4a.txt", "r") as file:
    codigo = file.read()


exec(codigo)


input5 = "input 5"
print("#" * 50)
print("{:^50}".format("input 5"))
print("#" * 50)
print(input5)
with open("inputs/input5a.txt", "r") as file:
    codigo = file.read()


exec(codigo)


input6 = "input 6"
print("#" * 50)
print("{:^50}".format("input 6"))
print("#" * 50)
print(input6)
with open("inputs/input6a.txt", "r") as file:
    codigo = file.read()


exec(codigo)











