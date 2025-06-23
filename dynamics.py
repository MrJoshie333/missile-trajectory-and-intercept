# Aerodynamic Equations for missile dynamics
from dataclasses import dataclass
import numpy as np






# don't need acceleration/thrust in this class
@dataclass
class kinematicState:
    x: list[float]
    y: list[float]
    vX: list[float]
    vY: list[float]
    totalAccelerationX: list[float]
    totalAccelerationY: list[float]
    thrustAccelerationX: list[float]
    thrustAccelerationY: list[float]

#STATE USES SEMI-IMPLICIT EULER!!!!
def getState(env, missile, time):
    t = 0.0
    dt = time.timeStep #use dt as time step for kinematic equations
    while t <= time.runTime:
        # Use previous pos, v
        # do i calculate change in m,g first?
        # Calculate new angle
        missile.flightAngle.append(np.arctan2(missile.vY[-1], missile.vX[-1]))

        # Thrust Acceleration:
        kinematicState.thrustAccelerationX.append(missile.getThrustAccelerationX())
        kinematicState.thrustAccelerationY.append(missile.getThrustAccelerationY())

        # total acceleration
        kinematicState.totalAccelerationX.append(kinematicState.thrustAccelerationX[-1])
        kinematicState.totalAccelerationY.append(kinematicState.thrustAccelerationY[-1] + (-1 * env.gravity))

        # updated velocity:
        missile.vX.append(missile.vX[-1] + kinematicState.totalAccelerationX[-1] * dt)
        missile.vY.append(missile.vY[-1] + kinematicState.totalAccelerationY[-1] * dt)

        # updated position:
        missile.x.append(missile.x[-1] + missile.vX[-1] * dt)
        missile.y.append(missile.y[-1] + missile.vY[-1] * dt)

        #updated mass, later



        t += dt


def getTrajectory(env, missile, time):
    for t in time:
        # zip the x and y together

        x = missile.x[0] + (missile.vx[0] * t)
        y = missile.y[0] + (missile.vy[0] * t) - 0.5 * env.gravity * t ** 2
        missile.x.append(x)
        missile.y.append(y)
        # print(x, y)
        if y <= 0 and len(
                missile.y) > 2:  # if the missile hits the ground, assuming y(t)=0; needs to be length 2 because we initialize with y=0
            del missile.x[-1]
            del missile.y[-1]
            missile.flightTime = (missile.vy[0] + np.sqrt(
                missile.vy[0] ** 2 + 2 * env.gravity * missile.y[0])) / env.gravity
            # Final Range:
            xTraveled = missile.x[0] + missile.vx[0] * missile.flightTime
            missile.x.append(xTraveled)
            missile.y.append(0)
            break

    if missile.flightTime is None:  # if it never reaches the ground
        missile.flightTime = t
    return missile.x, missile.y
