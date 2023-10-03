# Definimos la clase base Musico
class Musico:
def instrumento(self):
print("El músico toca un instrumento")
# Definimos la clase hija Guitarrista
class Guitarrista(Musico):
def instrumento(self):
print("El guitarrista toca una guitarra")
# Definimos la clase hija Baterista
class Baterista(Musico):
def instrumento(self):
print("El baterista toca una batería")
# Creamos un objeto de la clase Guitarrista
guitarrista = Guitarrista()
Llamamos al método instrumento()
guitarrista.instrumento()
# Creamos un objeto de la clase Baterista
baterista = Baterista()
# Llamamos al método instrumento()
baterista.instrumento()
