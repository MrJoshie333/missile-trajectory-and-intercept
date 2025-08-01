# Aerodynamic Equations for missile dynamics
from dataclasses import dataclass

import numpy as np


# don't need acceleration/thrust in this class
@dataclass
class KinematicState:
    x: list[float]
    y: list[float]
    vX: list[float]
    vY: list[float]
    totalAccelerationX: list[float]
    totalAccelerationY: list[float]
    thrustAccelerationX: list[float]
    thrustAccelerationY: list[float]
    gravitationalAccelerationY: list[float]
    thrustForce: list[float]


# STATE USES SEMI-IMPLICIT EULER!!!!
def getState(env, missile, time):
    t = 0.0
    dt = time.timeStep  # use dt as time step for kinematic equations
    while t <= time.runTime:
        # Use previous pos, v
        # do i calculate change in m,g first?

        #------------#
        ####Thrust####
        #------------#

        # If time passes thrust time, then thrust goes to zero
        if t > missile.thrustTime:
            missile.KinematicState.thrustForce.append(0)
        else:
        # If thrust still goes, current thrust equals immediately previous thrust
            missile.KinematicState.thrustForce.append(missile.KinematicState.thrustForce[-1])
        #Thrust Acceleration
        missile.KinematicState.thrustAccelerationX.append(missile.getThrustAccelerationX())
        missile.KinematicState.thrustAccelerationY.append(missile.getThrustAccelerationY())

        #--------------

        # Gravitational Acceleration
        missile.KinematicState.gravitationalAccelerationY.append(missile.getGravitationalAcceleration())

        # Total Acceleration
        missile.KinematicState.totalAccelerationX.append(missile.KinematicState.thrustAccelerationX[-1])
        missile.KinematicState.totalAccelerationY.append(
            missile.KinematicState.thrustAccelerationY[-1] + (
                    -1 * missile.KinematicState.gravitationalAccelerationY[-1]))
        # print(missile.KinematicState.totalAccelerationY[-1]) #debug; should be -9.8ish in free fall, positive in upward thrust


        # updated velocity
        missile.KinematicState.vX.append(
            missile.KinematicState.vX[-1] + missile.KinematicState.totalAccelerationX[-1] * dt)
        missile.KinematicState.vY.append(
            missile.KinematicState.vY[-1] + missile.KinematicState.totalAccelerationY[-1] * dt)

        # Calculate new angle
        missile.flightAngle.append(np.arctan2(missile.KinematicState.vY[-1], missile.KinematicState.vX[-1]))
        print("velocity-based angle: " + str(np.rad2deg(missile.flightAngle[-1])))
        # print("porition-based angle:")

        # updated position:
        missile.KinematicState.x.append(missile.KinematicState.x[-1] + missile.KinematicState.vX[-1] * dt)
        missile.KinematicState.y.append(missile.KinematicState.y[-1] + missile.KinematicState.vY[-1] * dt)

        print(f"t={t:.2f}  vx={missile.KinematicState.vX[-1]:.2f}  vy={missile.KinematicState.vY[-1]:.2f}  θ={np.rad2deg(missile.flightAngle[-1]):.1f}°")
        # grav = missile.getGravitationalAcceleration()
        # # print("grav:", grav)
        #updated time
        t += dt

        # updated mass, later

        # Check if it hits the ground
        if missile.KinematicState.y[-1] <= 0 and len(
                missile.KinematicState.y) > 2:  # if the missile hits the ground, assuming y(t)=0; needs to be length 2 because we initialize with y=0
            for last in [missile.KinematicState.x, missile.KinematicState.y, missile.KinematicState.vX,
                         missile.KinematicState.vY,
                         missile.KinematicState.totalAccelerationX, missile.KinematicState.totalAccelerationY,
                         missile.KinematicState.thrustAccelerationX, missile.KinematicState.thrustAccelerationY,
                         missile.KinematicState.gravitationalAccelerationY]:
                del last[-1]
            # solve ½ a_n τ² + v_n τ + y_n = 0 for τ in [0,dt]
            discriminant = missile.KinematicState.vY[-1] ** 2 - (
                    2 * missile.KinematicState.totalAccelerationY[-1] * missile.KinematicState.y[-1])
            # prevent negative discriminants:
            discriminant = max(0, discriminant)
            # Current time is calculating the time between the last non-negative timestep and it touching the ground.
            # Can probably be generalized to every single timestep for live simulation
            currentTime = (-missile.KinematicState.vY[-1] - np.sqrt(discriminant)) / \
                          missile.KinematicState.totalAccelerationY[-1]

            # Gets currentTime if it does not land
            # currentTime = min(currentTime, dt)

            missile.flightTime = currentTime + t
            break

    if missile.flightTime is None:  # if it never reaches the ground
        missile.flightTime = t
    return missile
