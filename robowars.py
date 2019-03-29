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


root = tk.Tk()

canvas = tk.Canvas(root, height = 400, width = 700)
canvas.pack()

enter_ability_label = tk.Label(root, text = "Enter abilities: ")
enter_ability_label.place(x = 10, y = 28)

enter_ability_label = tk.Label(root, text = "Attack")
enter_ability_label.place(x = 120, y = 5)
attack_input = tk.Entry(width = 5)
attack_input.place(x = 120, y = 25)

enter_ability_label = tk.Label(root, text = "Defence")
enter_ability_label.place(x = 190, y = 5)
defence_input = tk.Entry(width = 5)
defence_input.place(x = 190, y = 25)

enter_ability_label = tk.Label(root, text = "Speed")
enter_ability_label.place(x = 260, y = 5)
speed_input = tk.Entry(width = 5)
speed_input.place(x = 260, y = 25)


def helloCallBack():
    a = attack_input.get()
    print(a)

save_button = tk.Button(root, text ="Save", command = helloCallBack, bg = '#80c1ff')
save_button.place(x = 330, y = 25)



# background_label = tk.Label(root)
# background_label.place(relwidth=1, relheight=1)

# frame = tk.Frame(root, bg='#80c1ff', bd=5)
# frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = tk.Entry(frame, font=40)
# entry.place(relwidth=0.65, relheight=1)

# button = tk.Button(frame, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
# button.place(relx=0.7, relheight=1, relwidth=0.3)

# lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
# lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tk.Label(lower_frame)
# label.place(relwidth=1, relheight=1)

root.mainloop()