#This file holds code to program the player of the game
#
#
class Player:

    def __init__(self, name):
       self.name = name

#la f de antes es para llamar al atributo name, y asi acceda a él
    def speak(self):
      print(f"Hola me llamo {self.name}")

print("Bienvenidos a la alfa de SpaceSurvive")

name = input("Introduzca su nombre de jugador: ")

jugador = Player(name)

jugador.speak()