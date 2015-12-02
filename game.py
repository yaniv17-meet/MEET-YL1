from meet import *
import random

num_cells = 0
colors = ["brown", "green", "red", "dodgerblue", "blue", "pink", "yellow"]
        
ball1 = {"radius": 50, "x": 7, "y": 5, "dx": 0.1, "dy": 0.1, "color": "dodgerblue"}
cells = []
'''
def borders():
        if(x > get_screen_width):
                cell.set_dx = -cell.get_dx
        if(y > get_screen_height):
                cell.set_dy = -cell.get_dy
'''
while(num_cells<=30):
#checking random moving not equals to zero
        dx = random.uniform(-1.0, 1.0)
        dy = random.uniform(-1.0, 1.0)
        while(dx == 0):
                dx = random.uniform(-1.0, 1.0)
        while(dy == 0):
                dy = random.uniform(-1.0, 1.0)
#create balls                
        ball1 = {"radius": random.randint(5, 60), "x": random.randint(0, 100), "y": random.randint(0, 100), "dx": dx, "dy": dy, "color": colors[random.randint(0,4)]}
        circle1 = create_cell(ball1)
        cells.append(circle1)
        #borders()
        num_cells+=1
while (True):
	move_cells(cells)

