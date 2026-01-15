#panda.py
from .animal import Animal


class Panda(Animal):
    def __init__(self, name="Po"):
        super().__init__(name, species="Panda")

    def sound(self):
        return "Haiya!"

    def action(self):
        return "Is the Dragon Warrior!"


def test_sound():
   assert Panda().sound() == "Haiya!"

def test_action():
   assert Panda().action() == "Is the Dragon!"