from robot import Robot
from ability import Ability
import random

ability1 = Ability(8, 1, 1)
ability2 = Ability(5, 3, 2)

robot1 = Robot('robot1', ability1, 100, 0)
robot2 = Robot('robot2', ability2, 100, 19)

i = 0
while(robot1.energy > 0 and robot2.energy > 0):
    i += 1
    #DAMAGE(R2) = ( RANDOM(BETWEEN 1 AND 10) * A(R1) / DISTANCE ) – (D(R2) * (DISTANCE / 10))

    distance = abs(robot1.location - robot2.location)

    damage_r2 = (random.randint(0, 10) * robot1.ability.attack / distance) - (robot2.ability.defence * (distance / 10))
    if damage_r2 < 0:
        damage_r2 = 0
    
    robot2.energy -= damage_r2
    print(robot2.energy)

    damage_r1 = (random.randint(0, 10) * robot2.ability.attack / distance) - (robot1.ability.defence * (distance / 10))
    if damage_r1 < 0:
        damage_r1 = 0

    robot1.energy -= damage_r1
    print(robot1.energy)


    #robot1.energy = 0

print('total step: ', i)



if robot1.energy <= 0:
    print('Winner: ', robot2.name)
elif robot2.energy <= 0:
    print('Winner: ', robot1.name)