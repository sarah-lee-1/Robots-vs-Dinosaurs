from fleet import Fleet
from herd import Herd  
class Battlefield:
    def __init__(self):
        self.fleet = Fleet()
        self.herd = Herd() 
        # print(self.herd)

    def run_game(self):  #(self, name) 
        self.welcome_player() 
        self.battle() 
        self.display_winners()
    
    def welcome_player(self):
        print("Welcome to Robots vs. Dinosaurs. ") 
        print("You will fight on the Waterloo battlefield")
    
    def battle(self): 
        print("Please choose a fighter. ")
        #1 choose fighter
        # robo = self.show_robo_opponent_options()
        self.show_dino_opponent_options()
        
        # while fleet and herd still have members
        while(len(self.fleet.robot_list) > 0 and len(self.herd.dinosaur_list) > 0):
            #2 fight against   
            self.dino_turn()
            self.robo_turn() 
        
            # check health 
            print('robo health', robo.health)
            print('dino health', dino.health)
        
            # remove from list 
            if (len(dino_item = [0, -1])):
                self.herd.dinosaur_list.remove() 
            elif (len(robo_item = [0, -1])):
                self.fleet.robot_list.remove() 
            
        # end battle when one fighter reaches 0 points. 
        self.display_winners   

    # battle() 
   


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
        return user_input
        # return self.herd.dinosaur_list[user_input]
        
    def show_robo_opponent_options(self):
        item = 0
        for robo in self.fleet.robot_list:
            print(item, ") - ",robo.name)
            item += 1
        user_input = int(input("\nPlease choose a robot: "))
        return user_input
        # return self.fleet.robot_list[user_input]
    

    def display_winners(self):
        if (len(self.fleet.robot_list) > 0 ):
            print("Robot has won the battle. ")
        else:
            (len(self.herd.dinosaur_list) > 0)
            print("Dinosaur has won the battle. ")
