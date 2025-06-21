# Aerodynamic Equations for missile dynamics

import numpy as np



def getTrajectory(env, missile, time):
    for t in time:
        x = missile.pos[0] + (missile.vel[0] * t)
        y = missile.pos[1] + (missile.vel[1] * t) - 0.5 * env.gravity * t ** 2
        missile.trajectory.append((x, y))

        if y <= 0 and len(missile.trajectory) > 1: #if the missile hits the ground, assuming y(t)=0
            del missile.trajectory[-1]
            missile.tFlight = (missile.vel[1] + np.sqrt(missile.vel[1] ** 2 + 2 * env.gravity * missile.pos[1])) / env.gravity
            # Final Range:
            missile.xTraveled = missile.pos[0] + missile.vel[0] * missile.tFlight
            missile.trajectory.append((missile.xTraveled, 0))
            break

    if missile.tFlight is None: #if it never reaches the ground
        missile.tFlight = t
        missile.xTraveled=missile.trajectory[-1][0]
    return missile.trajectory


