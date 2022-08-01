from math import sqrt

class Rocket():
     
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def move_rocket(self, x_increment, y_increment):
        self.x += x_increment
        self.y += y_increment
        
    def print_rocket(self):
        print(self.x, self.y)
        
roc1 = Rocket()

roc1.move_rocket(1,2)

roc1.print_rocket()