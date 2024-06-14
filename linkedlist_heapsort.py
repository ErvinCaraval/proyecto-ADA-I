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

def heapify(arr, n, i, key=lambda x: x):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and key(arr[l]) > key(arr[largest]):
        largest = l
    elif l < n and key(arr[l]) == key(arr[largest]) and arr[l].edad < arr[largest].edad:  # Desempate por edad
        largest = l

    if r < n and key(arr[r]) > key(arr[largest]):
        largest = r
    elif r < n and key(arr[r]) == key(arr[largest]) and arr[r].edad < arr[largest].edad:  # Desempate por edad
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key)

def heapsort(arr, key=lambda x: x):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0, key)

class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"{{ {self.id} , {self.nombre} , {self.edad} , {self.rendimiento} }}"

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
        jugadores_ids = [j.id for j in self.jugadores.to_list()]
        return f"{self.deporte}, Rendimiento: {self.rendimiento_promedio()}\n{self.jugadores.to_list()}"

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
        equipos_list = self.equipos.to_list()
        return f"Sede {self.nombre}, Rendimiento: {self.rendimiento_promedio()}\n" + "\n".join([f"{equipo.deporte}, Rendimiento: {equipo.rendimiento_promedio()}\n{equipo.jugadores.to_list()}" for equipo in equipos_list])

print("input1")
# Lee el contenido del archivo
with open("input1a.txt", "r") as file:
    codigo = file.read()

# Ejecuta el código
exec(codigo)


print("input2")
# Lee el contenido del archivo
with open("input2a.txt", "r") as file:
    codigo = file.read()

# Ejecuta el código
exec(codigo)






