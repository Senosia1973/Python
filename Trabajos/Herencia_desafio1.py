 class Escritor:
    """
    Clase base para escritores.

    Atributos:
        nombre (str): El nombre del escritor.

    Métodos:
        biografia()
    """

    def _init_(self, nombre):
        """
        Inicializa el escritor.

        Argumentos:
            nombre (str): El nombre del escritor.
        """
        self.nombre = nombre

    def biografia(self):
        """
        Devuelve la biografía del escritor.

        Devuelve:
            La biografía del escritor.
        """
        return f"El escritor {self.nombre} nació en el año 1900 en la ciudad de Madrid."


class Novelista(Escritor):
    """
    Clase para novelistas.
     Atributos:
        nombre (str): El nombre del novelista.
        numero_novelas (int): El número de novelas escritas.

    Métodos:
        biografia()
    """

    def _init_(self, nombre, numero_novelas):
        """
        Inicializa el novelista.

        Argumentos:
            nombre (str): El nombre del novelista.
            numero_novelas (int): El número de novelas escritas.
        """
        super()._init_(nombre)
        self.numero_novelas = numero_novelas

    def biografia(self):
        """
        Devuelve la biografía del novelista.

        Devuelve:
            La biografía del novelista.
        """
        return f"El novelista {self.nombre} nació en el año 1900 en la ciudad de Madrid. Ha escrito {self.numero_novelas} novelas."


novelista = Novelista("Gabriel García Márquez", 10)

print(novelista.biografia())