# Aerodynamic Equations for missile dynamics

import numpy as np


def getTrajectory(env, missile, time):
    # get positions
    for t in time:
        x = missile.pos[0] + (missile.vel[0] * t)
        y = missile.pos[1] + (missile.vel[1] * t) - 0.5 * env.gravity * t ** 2
        # missile.trajectory = np.append(missile.trajectory, (x, y), axis=0)
        missile.trajectory.append((x, y))
        # stop the missile if it hits the ground

        if y <= 0 and len(missile.trajectory) > 1:
            # missile.trajectory = np.delete(missile.trajectory, -1, axis=0)
            del missile.trajectory[-1]

            # Getting last position, for y=0
            # time of flight, assuming y(t)=0:
            tFlight = (missile.vel[1] + np.sqrt(missile.vel[1] ** 2 + 2 * env.gravity * missile.pos[1])) / env.gravity
            # Final Range:
            xRange = missile.pos[0] + missile.vel[0] * tFlight
            # missile.trajectory = np.append(missile.trajectory,(xRange, 0), axis=0)
            missile.trajectory.append((xRange, 0))

            break
    # print(missile.trajectory)
    return missile.trajectory, t
