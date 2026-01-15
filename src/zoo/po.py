#panda.py
from .animal import Animal


class Panda(Animal):
    def __init__(self, name="Po"):
        super().__init__(name, species="Panda")

    def sound(self):
        return "Haiya!"

    def action(self):
        return "Is the Dragon Warrior!"


