# Створимо 3 класи ігрових персонажів: Character -  Воїн, Маг, Стрілець
# *Параметри: імʼя, здоровʼя, ocnovna zbroja
# *Метод: attack(), take_damage()
# Воїн - сила
# Маг - мана
# Стрілець - точність

import random
import time

class character:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def attack(self):
        print(f"personash atakuet")

    def take_damege(self, damage):
        self.hp = self.hp - damage
        print("personash otrymav shkodu")

class Warrior(character):
    def __init__(self, name, hp, strength):
        super().__init__(name, hp)
        self.stenght = strength

    def attack(self):
        super().attack()
        ronddamedg = random.randint(1, 20)
        if (ronddamedg == 1):
            self.hp-=10
            print("u was upal topor na nogu i wy poterialy 10hp")
            print(f"u was ostalos{self.hp} hp ")
        else:
            enemy.take_damege({ronddamedg-1}) 
            print(f"wy nanesly {ronddamedg-1} urona")

class Magik(character):
    def __init__(self, name, hp, mana):
         super().__init__(name, hp)
         self.mana = mana

    def attack(self):
        super().attack()
        print(f"")

class strelec(character):
    def __init__(self, name, hp, tochnost):
        super().__init__(name, hp)
        self.tochnost = tochnost

    def attack(self):
        super().attack()
        print(f"")


woin = Warrior("woin", 150, random.randint(1, 20))
woin.