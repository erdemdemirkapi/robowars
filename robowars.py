from robot import Robot
from ability import Ability
import random

import tkinter as tk

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

canvas = tk.Canvas(root, height = 400, width = 700)
canvas.pack()

enter_ability_label = tk.Label(root, text = "Enter abilities: ")
enter_ability_label.place(x = 10, y = 40)

attack_label = tk.Label(root, text = "Attack")
attack_label.place(x = 120, y = 5)
attack_input1 = tk.Entry(width = 5)
attack_input1.place(x = 120, y = 25)

defence_label = tk.Label(root, text = "Defence")
defence_label.place(x = 190, y = 5)
defence_input1 = tk.Entry(width = 5)
defence_input1.place(x = 190, y = 25)

speed_label = tk.Label(root, text = "Speed")
speed_label.place(x = 260, y = 5)
speed_input1 = tk.Entry(width = 5)
speed_input1.place(x = 260, y = 25)

attack_label = tk.Label(root, text = "Attack")
attack_label.place(x = 120, y = 60)
attack_input2 = tk.Entry(width = 5)
attack_input2.place(x = 120, y = 60)

defence_label = tk.Label(root, text = "Defence")
defence_label.place(x = 190, y = 60)
defence_input2 = tk.Entry(width = 5)
defence_input2.place(x = 190, y = 60)

speed_label = tk.Label(root, text = "Speed")
speed_label.place(x = 260, y = 60)
speed_input2 = tk.Entry(width = 5)
speed_input2.place(x = 260, y = 60)

def set_robot_ability():
    attack1_string = attack_input1.get()
    attack1_int = int(attack1_string)
    defence1_string = defence_input1.get()
    defence1_int = int(defence1_string)
    speed1_string = speed_input1.get()
    speed1_int = int(speed1_string)

    attack2_string = attack_input2.get()
    attack2_int = int(attack2_string)
    defence2_string = defence_input2.get()
    defence2_int = int(defence2_string)
    speed2_string = speed_input2.get()
    speed2_int = int(speed2_string)
    
    ability1 = Ability(attack1_int, defence1_int, speed1_int)
    ability2 = Ability(attack2_int, defence2_int, speed2_int)
    
    return ability1, ability2

save_button = tk.Button(root, text ="Save", command = set_robot_ability, bg = '#80c1ff')
save_button.place(x = 330, y = 40)

ability1 = Ability(6, 2, 2)
ability2 = Ability(5, 3, 2)

robot1 = Robot('robot1', ability1, 100, 0)
robot2 = Robot('robot2', ability2, 100, 19)

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

if robot1.energy <= 0:
    print('Winner: ', robot2.name)
elif robot2.energy <= 0:
    print('Winner: ', robot1.name)


root.mainloop()