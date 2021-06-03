class Animal(object):
    def __init__(self, nombre: str, salud: int, felicidad: int):
        self.nombre = nombre
        self.salud = salud
        self.felicidad = felicidad
        self.especie = str()

    def descripcion(self):
        s = f"Este(a) {self.especie} se llama {self.nombre}, sus puntos de vida son {self.salud}, y su felicidad es {self.felicidad}."
        return s

    def alimentar(self):
        self.salud += 10
        self.felicidad += 10

class Zoo:
    def __init__(self, zoo_nombre):
        self.animales = []
        self.nombre = zoo_nombre

    def agregar_leon(self, nombre):
        self.animales.append(Leon(nombre))

    def agregar_tigre(self, nombre):
        self.animales.append(Tigre(nombre))

    def imprimir_todo(self):
        print("-" * 30, self.nombre, "-" * 30)
        for animal in self.animales:
            animal.descripcion()

zool = Zoo("Zoologico de Pucon")

class Leon(Animal):
    def __init__(self, nombre: str, salud: int = 3, felicidad: int = 3, macho: bool = True):
        super().__init__(nombre, salud, felicidad)
        self.macho = macho
zool.agregar_leon("Tom")

class Oso(Animal):
    def __init__(self, nombre: str, salud: int = 2, felicidad: int = 10, color: str="brown"):
        super().__init__(nombre, salud, felicidad)
        self.color = color


class Tigre(Animal):
    def __init__(self, nombre: str, salud: int = 4, felicidad: int = 5):
        super().__init__(nombre, salud, felicidad)
zool.agregar_tigre("Zucarita")



zool.imprimir_todo()