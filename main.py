# Setting up the simulation
import numpy as np

from dynamics import getState
from environment import Environment, Time
from vehicle import Vehicle
from visualization import plotTrajectory

# === Environment configuration ===
# Adjust these values as needed.
# Leave them as-is to use the default values defined in environment.py

environment_params = {
    "gravity": 9.81,  # default: 9.81 m/s²
    "rho": 1.225,  # default: 1.225 kg/m³
    "p": 101325,  # default: 101325 Pa
    "T": 288.15,  # default: 288.15 K
    "a": 343  # default: 343 m/s
}

env = Environment(**environment_params)
# === End of environment configuration ===

# === Vehicle configuration ===

# Angle is measured starting at the positive x-axis and going counterclockwise
#Missile arguments: initialMass, initialVelocity, launchAngle, initialPosition, initialAcceleration, thrustForce, thrustTime
missiles = [
Vehicle(initialMass=5000,initialVelocity=32,launchAngle=15,initialPosition=[0, 0],initialAcceleration=[0, 0], initialThrustForce=200000, thrustTime = 6),
Vehicle(initialMass=5000,initialVelocity=32,launchAngle=15,initialPosition=[0, 0],initialAcceleration=[0, 0], initialThrustForce=200000, thrustTime = 1),
Vehicle(initialMass=5000,initialVelocity=32,launchAngle=15,initialPosition=[0, 0],initialAcceleration=[0, 0], initialThrustForce=200000, thrustTime = 0),


]

time = Time(5, 500) #Time (s), numSteps


results = []
allTrajectories = []
for missile in missiles:
    state = getState(env, missile, time)
    allTrajectories.append([(x,y) for x,y in zip(missile.KinematicState.x, missile.KinematicState.y)])

plotTrajectory(env, missiles, allTrajectories)

# # /----- Debugging -----/
#
# print("time taken: " + str(timeBeforeHitGround))
# # print("trajectory: " + str(missile.trajectory))
#
# testValue = 225 * np.sin(2 * m.pi / 4) / 9.81  # assuming a 45 degree angle, 15 vo, (0,0) starting pos
# # print("range equation trajectory" + str(testValue))
# print("final x position: " + str(trajectory[-1][0]))
#
# print("final y position: " + str(trajectory[-1][1]))
