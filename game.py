from meet import *
import random
import math
import turtle
import time
num_cells = 0
colors = ["brown", "green", "red", "dodgerblue", "blue", "pink", "yellow","yellow"]
cells = []
def check_eat():
        for cell in cells:
                r2=cell.get_radius()
                r1=user_circle.get_radius()
                dist = math.sqrt((cell.xcor()-user_circle.xcor())**2+(cell.ycor()-user_circle.ycor())**2)
                if(dist<r1+r2):
                        if(r1>r2):
                                cell.goto(1000,1000)
                                user_circle.set_radius(user_circle.get_radius()+3)
                                if(user_circle.get_radius()>100):
                                        turtle.write('You win', align='center',font=('ariel',60,'bold'))
                                        time.sleep(1)
                                        exit()
                        elif(r2>r1):
                                turtle.write('game over', align='center',font=('ariel',60,'bold'))
                                time.sleep(1)
                                exit()
def borders(cells):
        for cell in cells:
                if(cell.xcor() > get_screen_width()):
                        cell.set_dx(-cell.get_dx())
                if(cell.ycor() > get_screen_height()):
                        cell.set_dy(-cell.get_dy())
                if(cell.xcor() < -get_screen_width()):
                        cell.set_dx(-cell.get_dx())
                if(cell.ycor() < -get_screen_height()):
                        cell.set_dy(-cell.get_dy())

while(num_cells<=30):
#checking random moving not equals to zero
        dx = random.uniform(-1.0, 1.0)
        dy = random.uniform(-1.0, 1.0)
        while(dx == 0):
                dx = random.uniform(-1.0, 1.0)
        while(dy == 0):
                dy = random.uniform(-1.0, 1.0)
        x = random.randint(-get_screen_width(), get_screen_width())
        y = random.randint(-get_screen_height(), get_screen_height())
        while(x < 100 and x > -100):
                x = random.randint(-get_screen_width(), get_screen_width())
        while(y < 100 and y > -100):
                y = random.randint(-get_screen_height(), get_screen_height())
#create balls                
        ball1 = {"radius": random.randint(5, 50), "x": x, "y": y, "dx": dx, "dy": dy, "color": colors[random.randint(0,7)]}
        circle1 = create_cell(ball1)
        cells.append(circle1)
        num_cells+=1
#user cell
user_cell = {"radius": 30, "x": 0, "y": 0, "dx": dx, "dy": dy, "color": "black"}
user_circle = create_cell(user_cell)
cells.append(user_circle)

while (True):
        move_cells(cells)
        borders(cells)
        user_cor=get_user_direction(user_circle)
        user_circle.set_dx(user_cor[0])
        user_circle.set_dy(user_cor[1])
        check_eat()
