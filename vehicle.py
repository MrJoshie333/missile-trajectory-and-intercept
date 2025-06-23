# Constants for the vehicle
import numpy as np

from dynamics import kinematicState
from environment import Environment


# from dynamics import motionState


class Vehicle:
    import numpy as np
    def __init__(self, initialMass: float, initialVelocity: float = 0.0, launchAngle: float = 90.0,
                 initialPosition: list[float] = None,
                 initialAcceleration: list[float] = None, thrustForce: float = 0.0,
                 env: Environment = None):  # keep environment at the end

        self.initialMass = initialMass
        self.flightAngle = []
        self.flightAngle.append(np.deg2rad(launchAngle))
        self.thrustForce = thrustForce
        self.env = env or Environment()

        initialPosition = initialPosition or [0.0, 0.0]  # initial pos
        self.initialVelocity = initialVelocity  # init vel
        initialAcceleration = initialAcceleration or [0.0, 0.0]  # init acc
        initialThrustAccelerationX = thrustForce / initialMass * np.cos(np.deg2rad(launchAngle))
        initialThrustAccelerationY = thrustForce / initialMass * np.sin(np.deg2rad(launchAngle))

        # CURRENTLY ASSUMING:
        # Constant, always on Thrust (eventually: thrustForce = ...)
        # Constant mass
        #flat earth, so there is no x-component of g

        self.kinematicState = kinematicState(x=[initialPosition[0]], y=[initialPosition[1]],
                                             vX=[initialVelocity * np.cos(np.deg2rad(launchAngle))],
                                             vY=[initialVelocity * np.sin(np.deg2rad(launchAngle))],
                                             totalAccelerationX=[initialAcceleration[0]],
                                             totalAccelerationY=[initialAcceleration[1]],
                                             thrustAccelerationX=[initialThrustAccelerationX],
                                             thrustAccelerationY=[initialThrustAccelerationY],
                                            gravitationalAccelerationY=[getGravitationalAcceleration]#) #syntax here??

    def getFlightAngle(self):  # in radians
        return np.arctan2(self.kinematicState.vY[-1], self.kinematicState.vX[-1])
    
    def getGravitationalAcceleration(self):
        return self.env.gravitationalConst * (self.env.earthRadius / (self.env.earthRadius + self.kinematicState.y[-1])) ** 2
    def getThrustAccelerationX(self): #eventually change once mass and thrust force are variables
        return (self.thrustForce / self.initialMass) * np.cos(self.flightAngle[-1]) #returns x thrust acceleration
    def getThrustAccelerationY(self):
        return (self.thrustForce / self.initialMass) * np.sin(self.flightAngle[-1]) #returns y thrust acceleration
