from typing import AsyncIterable
from r_weapons import Weapon 
class Robot:
    def __init__(self, name):
        self.name = name 
        self.health = []       
        self.attack_power = Weapon()

 