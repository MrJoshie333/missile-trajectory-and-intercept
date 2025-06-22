# Aerodynamic Equations for missile dynamics
from dataclasses import dataclass

import numpy as np

@dataclass
class motionState:
    x: list[float]
    y: list[float]
    vx: list[float]
    vy: list[float]
    ax: list[float]
    ay: list[float]
    currentAngle: float
    currentMass: float
    flightTime: None


# def getAcceleration(env, missile):


def getTrajectory(env, missile, time):
    for t in time:
        #zip the x and y together

        x = missile.state.x[0] + (missile.state.vx[0] * t)
        y = missile.state.y[0] + (missile.state.vy[0] * t) - 0.5 * env.gravity * t ** 2
        missile.state.x.append(x)
        missile.state.y.append(y)
        # print(x, y)
        if y <= 0 and len(missile.state.y) > 2: #if the missile hits the ground, assuming y(t)=0; needs to be length 2 because we initialize with y=0
            del missile.state.x[-1]
            del missile.state.y[-1]
            missile.state.flightTime = (missile.state.vy[0] + np.sqrt(missile.state.vy[0] ** 2 + 2 * env.gravity * missile.state.y[0])) / env.gravity
            # Final Range:
            xTraveled = missile.state.x[0] + missile.state.vx[0] * missile.state.flightTime
            missile.state.x.append(xTraveled)
            missile.state.y.append(0)
            break

    if missile.state.flightTime is None: #if it never reaches the ground
        missile.state.flightTime = t
    return missile.state.x, missile.state.y


