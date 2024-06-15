class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data.rendimiento < node.data.rendimiento or (data.rendimiento == node.data.rendimiento and data.edad > node.data.edad):
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        res = []
        if node:
            res = self._in_order(node.left)
            res.append(node.data)
            res = res + self._in_order(node.right)
        return res

def quicksort(arr, low, high, key=lambda x: x):
    if low < high:
        pi = partition(arr, low, high, key)
        quicksort(arr, low, pi - 1, key)
        quicksort(arr, pi + 1, high, key)

def partition(arr, low, high, key):
    pivot = key(arr[high])
    i = low - 1
    for j in range(low, high):
        # Modificamos la comparación para considerar la edad en caso de empate en el rendimiento
        if key(arr[j]) < pivot or (key(arr[j]) == pivot and arr[j].edad > arr[high].edad):
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


class Jugador:
    def __init__(self, id, nombre, edad, rendimiento):
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.rendimiento = rendimiento

    def __repr__(self):
        return f"{self.id}"

class Equipo:
    def __init__(self, sede, deporte):
        self.deporte = deporte
        self.jugadores = BinarySearchTree()
        self.sede = sede

    def agregar_jugador(self, jugador):
        self.jugadores.insert(jugador)

    def obtener_jugadores_ordenados(self):
        return self.jugadores.in_order()

    def rendimiento_promedio(self):
        jugadores = self.obtener_jugadores_ordenados()
        if jugadores:
            return sum(j.rendimiento for j in jugadores) / len(jugadores)
        else:
            return 0
    def __repr__(self):
        ids = ', '.join(str(j) for j in self.jugadores)
        return f"{self.deporte}, Rendimiento: {self.rendimiento_promedio()}\n{{ {ids} }}"
    

class Sede:
    def __init__(self, nombre):
        self.nombre = nombre
        self.equipos = []

    def agregar_equipo(self, equipo):
        self.equipos.append(equipo)

    def rendimiento_promedio(self):
        if self.equipos:
            return sum(equipo.rendimiento_promedio() for equipo in self.equipos) 
        else:
            return 0
         


    def ordenar_equipos(self):
        quicksort(self.equipos, 0, len(self.equipos) - 1, key=lambda x: (x.rendimiento_promedio(), len(x.obtener_jugadores_ordenados())))
    
    def __repr__(self):
        equipos_str = '\n\n'.join(str(e) for e in self.equipos)
        return f"{self.nombre}, Rendimiento: {self.rendimiento_promedio()}\n\n{equipos_str}"

input1 = "input 1"
print("#" * 50)
print("{:^50}".format("input 1"))
print("#" * 50)
print(input1)
with open("inputs/input1b.txt", "r") as file:
    codigo = file.read()


exec(codigo)

input2 = "input 2"
print("#" * 50)
print("{:^50}".format("input 2"))
print("#" * 50)
print(input2)
with open("inputs/input2b.txt", "r") as file:
    codigo = file.read()


exec(codigo)


input3 = "input 3"
print("#" * 50)
print("{:^50}".format("input 3"))
print("#" * 50)
print(input3)
with open("inputs/input3b.txt", "r") as file:
    codigo = file.read()


exec(codigo)



input4 = "input 4"
print("#" * 50)
print("{:^50}".format("input 4"))
print("#" * 50)
print(input4)
with open("inputs/input4b.txt", "r") as file:
    codigo = file.read()


exec(codigo)










