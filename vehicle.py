# Constants for the vehicle
import numpy as np

from dynamics import motionState


class Vehicle:
    import numpy as np
    def __init__(self, initialMass: float, velocity: float = 0.0, launchAngle: float = 90.0, pos: list[float] = None,
                 acc: list[float] = None, ):
        pos = pos or [0.0, 0.0]
        acc = acc or [0.0, 0.0]
        self.initialVelocity = velocity
        self.initialMass = initialMass
        self.launchAngle = launchAngle
        self.state = motionState(x=[pos[0]], y=[pos[1]], vx=[velocity * np.cos(np.deg2rad(launchAngle))],
                                 vy=[velocity * np.sin(np.deg2rad(launchAngle))], ax=[acc[0]], ay=[acc[1]],
                                 currentAngle=launchAngle, currentMass=initialMass, flightTime=None)
