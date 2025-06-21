# Setting up the simulation
import numpy
import numpy as np
import matplotlib.pyplot as plt
import math as m
from vehicle import Vehicle
from environment import Environment
from dynamics import getTrajectory
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

# Angle is measured starting at the positive x-axis and going counterclockwise
missile1 = Vehicle(
    mass=5000,
    velocity=32,
    angle=15,
    pos=[0, 0],
    acc=[0, 0]
)
missile2 = Vehicle(
    mass=5000,
    velocity=85,
    angle=91,
    pos=[0, 5],
    acc=[0, 0]
)
time = np.linspace(0, 5, 100)
trajectory, flightTime = getTrajectory(env, missile1, time)
plotTrajectory(trajectory, missile1, env)
time = np.linspace(0, 20, 100)
trajectory2, flightTime2 = getTrajectory(env, missile2, time)
plotTrajectory(trajectory2, missile2, env)






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


