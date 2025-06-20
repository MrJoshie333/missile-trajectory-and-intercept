#Aerodynamic Equations for missile dynamics

import numpy as np
from environment import Environment
from vehicle import Vehicle
import math as m

def getTrajectory(env, missile, time):

    #get positions
    for t in time:
        x = missile.pos[0] + (missile.vel[0] * t)
        y = missile.pos[1] + (missile.vel[1] * t) - 0.5 * env.gravity * t ** 2
        missile.trajectory.append((x, y))
        #stop the missile if it hits the ground
        if y <= 0 and len(missile.trajectory) > 1:
            del missile.trajectory[-1]

            # Getting last position, for y=0
            # time of flight, assuming y(t)=0:
            tFlight = (missile.vel[1] + np.sqrt(missile.vel[1] ** 2 + 2 * env.gravity * missile.pos[1])) / env.gravity
            # Final Range:
            xRange = missile.pos[0] + missile.vel[0] * tFlight
            missile.trajectory.append((xRange, 0))

            break




    #/----- Debugging -----/

    print("time taken: " + str(t))
    # print("trajectory: " + str(missile.trajectory))

    testValue = 225 * np.sin(2 * m.pi / 4) / 9.81 # assuming a 45 degree angle, 15 vo, (0,0) starting pos
    # print("range equation trajectory" + str(testValue))
    print("final x position: " + str(missile.trajectory[-1][0]))


    print("final y position: " + str(missile.trajectory[-1][1]))



