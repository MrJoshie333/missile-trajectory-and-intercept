# Setting up the simulation
import numpy as np
import matplotlib.pyplot as plt

from vehicle import Vehicle
from environment import Environment
from dynamics import getTrajectory

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

#Angle is measured starting at the positive x-axis and going counterclockwise
missile1 = Vehicle(
    mass = 5000,
    velocity = 32,
    angle = 15,
    pos = [0,0],
    acc = [0,0]
)

time = np.linspace(0, .5, 1000)
getTrajectory(env, missile1, time)
