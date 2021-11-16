from fleet import Fleet
from herd import Herd  
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd() 
        # print(self.herd)

    def run_game(self, name):
        self.welcome_player() 
        self.battle() 
        self.display_winners()
    
    def welcome_player(self):
        print("Welcome to Robots vs. Dinosaurs. ") 
        print("You will fight on the Waterloo battlefield")
        
    def battle(self):
  
        #1 choose fighters
        dino = Battlefield.show_dino_opponent_options()
        robo = Battlefield.show_robo_opponent_options()
            
        #2 fight against
            
        
        #3 check health 
        # remove from list 
        while( len(self.fleet.robot.health) > 0 and len(self.herd.dinosaur_list) > 0):
            (len(self.fleet.self.health)) 
        
        # while fleet and herd still have members
        while( len(self.fleet.robot_list) > 0 and len(self.herd.dinosaur_list) > 0):
            Battlefield.robo_turn()
        else:
            Battlefield.dino_turn() 
            
        
        pass    


    def dino_turn(self, dinosaur):
        defending_robo = self.show_robo_opponent_options()
        dinosaur.attack(defending_robo)
    
    
    def robo_turn(self, robot): 
        defending_dino = self.show_dino_opponent_options()
        robot.attack(defending_dino)
        

    def show_dino_opponent_options(self): 
        item = 0
        for dino in self.herd.dinosaur_list:
            print(item, ") - ", dino.name)
            item += 1
        user_input = int(input("\nPlease choose a dinosaur: "))
        return self.herd.dinosaur_list[user_input]
        
    def show_robo_opponent_options(self):
        item = 0
        for robo in self.fleet.robot_list
            print(item, ") - ",robo.name)
            item += 1
        user_input = int(input("\nPlease choose a robot: "))
        return self.fleet.robot_list[user_input]
    

    def display_winners(self):
        if (len(self.fleet.robot_list) > 0 ):
            print("Robot has won the battle. ")
        else:
            (len(self.herd.dinosaur_list) > 0)
            print("Dinosaur has won the battle. ")
