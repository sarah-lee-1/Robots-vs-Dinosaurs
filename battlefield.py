from robots import Robot
from weapon import Weapon
from dinosaurs import Dinosaur 
from weapon import Weapon 

class Battlefield:
    def __init__(self, name):
        self.name = name 

    def run_game(self):
        self.name = name 
    
    def welcome_player(self):
        print("Welcome to Robots vs. Dinosaurs") 
        print("Please choose your fighter")
        choose_fighter = input("Would you like to be Robot? ")
        # Robot will be proposed by default
        if choose_fighter == ("yes"): 
            # instantiate Robot
            self.robot_list.append(robot1)
            print("You have chosen Robot") 
        else:
            choose_fighter == ("no")
             # instantiate Dinosaur 
            self.dinosaur_list.append(dino1) 
            print("You have chosen Dinosuar")

    def battle(self):
        self.name = name 
        print("You will fight on the Waterloo battlefield")
         
    # def robot_go(self, robot):
        self.name = name
        # attack health
        # pass
    
    # def dinosaur_go(self, dinosaur):
        self.name = name 
        #  attack health 
        # pass
    
    def robot_play_options(self):
        robot.strike_play.append(attack)
         
        
    def dinosaur_play_options(self):
        dinosaur.strike_play.append(attack) 
        # loop
        # stop loop when one player reaches 0
    
    def announce_winner(self):
        print() # print player with >0 points to console
        # ("Congratulations. 'Robot' or 'Dinosaur' has won this round")
        pass