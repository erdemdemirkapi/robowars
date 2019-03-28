from robot import Robot
from ability import Ability
import random

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
