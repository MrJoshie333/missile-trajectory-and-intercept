#Parameters and constants for the environment
import numpy as np

class Time:
    def __init__(self, runTime: float, numSteps: int):
        self.runTime = runTime
        self.timeStep = runTime / numSteps


class Environment:
    def __init__(self, gravity = 9.81, rho = 1.225, p = 101325, T = 288.15, a = 343):
        #radius of the Earth, in m
        self.earthRadius = 6371008.77
        #standard gravitational acceleration constant, m/s^2
        self.gravitationalConst = 9.80665
        #gravitational constant in m/s^2 (assuming unchanging with altitude)
        self.gravitationalAcceleration = gravity
        #density of air in kg/m^3 (assuming unchanging with altitude)
        self.rho = rho
        #pressure of air in Pa (assuming unchanging with altitude)
        self.p = p
        #temperature of air in K (assuming unchanging with altitude)
        self.T = T
        #speed of sound in m/s (assuming unchanging with altitude)
        self.a = a
