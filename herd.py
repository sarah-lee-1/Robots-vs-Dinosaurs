from dinosaurs import Dinosaur 
class Herd:
    def __init__(self):
        self.dinosaur_list = []
        self.create_herd()
    
    def create_herd(self):
        dino1 = Dinosaur("Triceratops")
        dino2 = Dinosaur("T-Rex")
        dino3 = Dinosaur("Velociraptor")
        self.dinosaur_list.append(dino1)
        self.dinosaur_list.append(dino2)
        self.dinosaur_list.append(dino3)
