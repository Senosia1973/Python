class Autor:
    def __init__(self, nombre):
        self.nombre = nombre

    def biografia(self):
        raise NotImplementedError("El método biografia debe ser implementado por la subclase")


class Escritor(Autor):
    def __init__(self, nombre, genero):
        super().__init__(nombre)
        self.genero = genero

    def biografia(self):
        return f"Nombre: {self.nombre}, Género literario: {self.genero}"


escritor = Escritor("Gabriel García Márquez", "Realismo mágico")

print(escritor.biografia())
