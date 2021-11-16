from robots import Robot

class Fleet:
    def __init__(self):
        self.robot_list = []
        self.create_fleet()

    def create_fleet(self):
        robot1 = Robot("Hal")
        robot2 = Robot("Terminator")
        robot3 = Robot("Gerty")
        self.robot_list.append(robot1)
        self.robot_list.append(robot2)
        self.robot_list.append(robot3)
