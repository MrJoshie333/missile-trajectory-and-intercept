# Constants for the vehicle
import numpy as np


class Vehicle:
    import numpy as np
    def __init__(self, mass: float, velocity: float = 0.0, angle: float = 90.0, pos: list[float] = None,
                 acc: list[float] = None, ):
        self.mass = mass
        vel = velocity
        self.angle = np.deg2rad(angle)
        self.vel = np.array([
            vel * np.cos(self.angle), #Vx
            vel * np.sin(self.angle) #Vy
        ])

        # Uses defaults only if values not provided
        self.pos = np.array(pos) if pos else np.array([0.0, 0.0])
        self.acc = np.array(acc) if acc else np.array([0.0, 0.0])
        # Assuming vertical launch is 90 degrees

        self.trajectory = []  # stores all the trajectory values at each time step
