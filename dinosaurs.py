from weapon import Weapon

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = ("teeth", 9)

    def attack(self, robot):
        robot.health -= self.attack_power
        # robot.health = robot.health - self.weapon.attack_power 
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
        
#dino1 = (Triceratops)
#dino2 = (T-Rex)
#dino3 = (Velociraptor)