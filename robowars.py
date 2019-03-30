from robot import Robot
from ability import Ability
import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from time import sleep

def distance(d1, d2):
    return abs(d1 - d2)

def attack(attack_robot, defence_robot, distance_of_robots):
    damage_defence_robot = (random.randint(0, 10) * attack_robot.ability.attack / distance_of_robots) - (defence_robot.ability.defence * (distance_of_robots / 10))
    if damage_defence_robot < 0:
        damage_defence_robot = 0
    
    defence_robot.energy -= damage_defence_robot

def move(robot, location_of_other_robot):
    if robot.name == 'robot1':
        new_location = random.randint(0, location_of_other_robot - 1)
    elif robot.name == 'robot2':
        new_location = random.randint(location_of_other_robot + 1 , 19)

    consume_energy = (distance(robot.location, new_location) / robot.ability.speed) * 5
    robot.energy -= consume_energy
    robot.location = new_location

root = tk.Tk()
root.title("RoboWars")

canvas = tk.Canvas(root, height = 400, width = 900)
canvas.pack()

enter_ability_label = tk.Label(root, text = "Enter abilities: ")
enter_ability_label.place(x = 10, y = 40)

attack1 = tk.IntVar()
attack_label = tk.Label(root, text = "Attack")
attack_label.place(x = 120, y = 5)
attack_input1 = tk.Entry(width = 5, textvariable = attack1)
attack_input1.place(x = 120, y = 25)

defence1 = tk.IntVar()
defence_label = tk.Label(root, text = "Defence")
defence_label.place(x = 190, y = 5)
defence_input1 = tk.Entry(width = 5, textvariable = defence1)
defence_input1.place(x = 190, y = 25)

speed1 = tk.IntVar()
speed_label = tk.Label(root, text = "Speed")
speed_label.place(x = 260, y = 5)
speed_input1 = tk.Entry(width = 5, textvariable = speed1)
speed_input1.place(x = 260, y = 25)

attack2 = tk.IntVar()
attack_label = tk.Label(root, text = "Attack")
attack_label.place(x = 120, y = 60)
attack_input2 = tk.Entry(width = 5, textvariable = attack2)
attack_input2.place(x = 120, y = 60)

defence2 = tk.IntVar()
defence_label = tk.Label(root, text = "Defence")
defence_label.place(x = 190, y = 60)
defence_input2 = tk.Entry(width = 5, textvariable = defence2)
defence_input2.place(x = 190, y = 60)

speed2 = tk.IntVar()
speed_label = tk.Label(root, text = "Speed")
speed_label.place(x = 260, y = 60)
speed_input2 = tk.Entry(width = 5, textvariable = speed2)
speed_input2.place(x = 260, y = 60)

def attributes_checked():
    sum1 = attack1.get() + defence1.get() + speed1.get()
    sum2 = attack2.get() + defence2.get() + speed2.get()

    if attack1.get() == 0 or defence1.get() == 0 or speed1.get() == 0 or attack2.get() == 0 or defence2.get() == 0 or speed2.get() == 0:
        messagebox.showinfo("Warning", "Each attributes should grater than 0. Please try again!")
    elif sum1 != 10 or sum2 != 10:
        messagebox.showinfo("Warning", "Sum of attributes should be 10 for each robots. Please try again!")
    else:
        return True

winner_label = tk.Label(root, text = "Winner: ")
img1 = ImageTk.PhotoImage(Image.open("robot1.png").resize((100, 100), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("robot2.png").resize((100, 100), Image.ANTIALIAS))
robot1_label = tk.Label(root, image = img1)
robot2_label = tk.Label(root, image = img2)
robot1_energy_label = tk.Label(root, text = "Energy ")
robot2_energy_label = tk.Label(root, text = "Energy ")

def start_game():
    winner_label.config(text = "")
    robot1_label.config(image = "")
    robot2_label.config(image = "")
    robot1_energy_label.config(text = "")
    robot2_energy_label.config(text = "")
    
    if attributes_checked():
        print('Game started!')

        ability1 = Ability(attack1.get(), defence1.get(), speed1.get())
        ability2 = Ability(attack2.get(), defence2.get(), speed2.get())

        robot1 = Robot('robot1', ability1, 100, 0)
        robot2 = Robot('robot2', ability2, 100, 19)

        robot1_label.place(x = (robot1.location * 40) + 10, y = 140)
        robot1_energy_label.config(text = "Energy " + str(robot1.energy))
        robot1_energy_label.place(x = (robot1.location * 40) + 10, y = 130)
        
        robot2_label.place(x = (robot2.location * 40) + 10, y = 140)
        robot2_energy_label.config(text = "Energy " + str(robot2.energy))
        robot2_energy_label.place(x = (robot2.location * 40) + 10, y = 130)

        while(robot1.energy > 0 and robot2.energy > 0):

            distance_of_robots = distance(robot1.location, robot2.location)

            movement_list = ['attack', 'move']

            movement = random.choice(movement_list)
            if movement == 'attack':
                attack(robot1, robot2, distance_of_robots)
            elif movement == 'move':
                move(robot1, robot2.location)

            movement = random.choice(movement_list)
            if movement == 'attack':
                attack(robot2, robot1, distance_of_robots)
            elif movement == 'move':
                move(robot2, robot1.location)

            root.update()

            robot1_label.place(x = (robot1.location * 40) + 10, y = 140)
            robot1_label.configure(image = img1)
            robot1.energy = round(robot1.energy, 3)
            robot1_energy_label.config(text = "Energy " + str(robot1.energy))
            robot1_energy_label.place(x = 10, y = 130)

            robot2_label.place(x = (robot2.location * 40) + 10, y = 140)
            robot2_label.configure(image = img2)
            robot2.energy = round(robot2.energy, 3)
            robot2_energy_label.config(text = "Energy " + str(robot2.energy))
            robot2_energy_label.place(x = 770, y = 130)

            sleep(0.2)

        if robot1.energy <= 0:
            robot1_label.config(image = "")
            robot2_label.config(image = "")
            winner_label.config(font=("Courier", 44), text = "Winner: " + robot2.name)
            winner_label.place(x = 200, y = 200, anchor = "center")
            
        elif robot2.energy <= 0:
            robot1_label.config(image = "")
            robot2_label.config(image = "")
            winner_label.config(font=("Courier", 44), text = "Winner: " + robot1.name)
            winner_label.place(x = 200, y = 200, anchor="center")

    else:
        print('Failed to start game!')

save_button = tk.Button(root, text ="Start Game", command = start_game, bg = '#80c1ff')
save_button.place(x = 330, y = 40)

root.mainloop()