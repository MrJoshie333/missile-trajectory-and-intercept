import matplotlib.pyplot as plt
import numpy as np

def initialConditionsText(vehicle, environment):
    plt.text(0.01, 0.99,
             #bold just Initial Conditions:
             r"$\bf{Initial\ Conditions:}$" + "\n"
             f"Mass: {vehicle.mass} kg\n"
             f"Velocity: {vehicle.velocity} m/s\n"
             f"Angle: {np.ceil(np.rad2deg(vehicle.angle))} degrees\n"
             f"Position: ({vehicle.pos[0]}, {vehicle.pos[1]})m\n"
             f"Acceleration: ({vehicle.acc[0]}, {vehicle.acc[1]}) m/$s^2$\n"
             f"Density: {environment.rho} kg/$m^3$\n"
             f"Pressure: {environment.p} Pa\n"
             f"Temperature: {environment.T} K\n"
             f"Speed of Sound: {environment.a} m/s\n"
             f"Gravity: {environment.gravity} m/$s^2$\n"
             f"Time of Flight: {vehicle.tFlight:.5f} s"
             , transform=plt.gca().transAxes,
             ha = 'left', va = 'top', fontsize = 12)

def plotTrajectory(trajectory, vehicle, environment):
    #create plot
    plt.figure(figsize=(10, 10))
    xVals, yVals = zip(*trajectory)
    xVals = np.array(xVals)
    yVals = np.array(yVals)

    plt.scatter(xVals, yVals)
    plt.plot(np.unique(xVals), np.poly1d(np.polyfit(xVals, yVals, 2))(np.unique(xVals)))

    plt.xlabel('X Position (m)')
    plt.ylabel('Y Position (m)')
    plt.title('Missile Trajectory')
    plt.legend(['Actual Trajectory', 'Fitted Line'])

    initialConditionsText(vehicle, environment) #Initial Conditions Text
    plt.grid(True, alpha = 0.5)


    plt.show()

#<----- Debugging ----->
if __name__ == '__main__':
    trajectory = ([1, 4], [2, 6])
    plotTrajectory(trajectory)