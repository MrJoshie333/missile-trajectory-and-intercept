import matplotlib.pyplot as plt
import numpy as np


def initialConditionsText(ax, missile, environment, idx, numVehicles, x_pad=0.02, y_pad=0.02):
    # Compute box position
    box_height = 1 / numVehicles
    y0 = 1 - idx * box_height - y_pad
    x0 = 1 + x_pad

    text = (
        fr"$\bf{{Missile\ {idx + 1}\ Initial\ Conditions:}}$" + f"\n" 
        f"Mass: {missile.initialMass} kg\n"
        f"Velocity: {missile.initialVelocity} m/s\n"
        f"Angle: {np.ceil(missile.launchAngle)}°\n"
        f"Position: ({missile.KinematicState.x[0]}, {missile.KinematicState.y[0]}) m\n"
        f"Acceleration: ({missile.KinematicState.totalAccelerationX[0]}, {missile.KinematicState.totalAccelerationY[0]}) m/s²\n"
        f"Initial Thrust Force: {missile.initialThrustForce} N\n"
        fr"$\bf{{Atmosphere\ {idx + 1}\ Initial\ Conditions:}}$" + f"\n"
        f"Density: {environment.rho} kg/m³\n"
        f"Pressure: {environment.p} Pa\n"
        f"Temperature: {environment.T} K\n"
        f"Speed of Sound: {environment.a} m/s\n"
        f"Gravity: {environment.gravitationalAcceleration} m/s²\n"
        fr"$\bf{{Missile\ {idx + 1}\ Current\ Conditions:}}$" + f"\n"                                                            
        f"Time of Flight: {missile.flightTime:.5f} s\n"
        f"x-Range: {missile.KinematicState.x[-1]:.5f} m"
    )

    ax.text(x0, y0, text,
            verticalalignment='top',
            horizontalalignment='left',
            transform=ax.transAxes,
            family='monospace',
            bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.3),
            )


def plotTrajectory(env, missiles, trajectories, fixed_axes: bool = False, xLimits: tuple[float, float] = None, yLimits: tuple[float, float] = None):
    fix, ax = plt.subplots(figsize=(10, 10))

    #If fixed axes is chosen, but limits are not provided:
    if fixed_axes and (xLimits is None or yLimits is None):
        xRange = np.concatenate([np.array([p[0] for p in traj]) for traj in trajectories])
        yRange = np.concatenate([np.array([p[1] for p in traj]) for traj in trajectories])
        # Get max of x and y across all trajectories
        max_val = max(np.max(xRange), np.max(yRange))

        #Get min and max of x and y:
        xmin, xmax = (0, np.max(xRange))
        ymin, ymax = (0, np.max(yRange)) #change the ymin from zero to anything if the ground is not at 0

    else:
        xmin, xmax = xLimits or (None, None)
        ymin, ymax = yLimits or (None, None)


    for idx, (missile, trajectory) in enumerate(zip(missiles, trajectories)):

        xVals, yVals = zip(*trajectory)
        xVals = np.array(xVals)
        yVals = np.array(yVals)

        ax.scatter(xVals, yVals, label=f"Missile {idx + 1}")
        ax.plot(np.unique(xVals), np.poly1d(np.polyfit(xVals, yVals, 3))(np.unique(xVals)),
                label=f"Missile {idx + 1} Fit")

    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_title('All Missile Trajectory')
    ax.legend(['Actual Trajectory', 'Fitted Line'], loc='upper left')
    ax.grid(True, alpha=0.5)

    if fixed_axes:
        #All max x:
        max_x = max(max(missile.KinematicState.x) for missile in missiles)
        max_y = max(max(missile.KinematicState.y) for missile in missiles)
        max_val = max(max_x, max_y)
        ax.set_xlim([xmin, max_val])
        ax.set_ylim([-1, max_val]) #-1, just so we can see dots more clearly on the ground
        ax.set_aspect('equal')
    else:
        ax.relim()
        ax.autoscale_view()

    # Initial conditions Text:
    plt.subplots_adjust(right=0.75)
    for idx, missile in enumerate(missiles):
        initialConditionsText(ax, missile, env, idx, len(missiles))

    plt.grid(True, alpha=0.5)
    plt.show()


# <----- Debugging ----->
if __name__ == '__main__':
    trajectory = ([1, 4], [2, 6])
    plotTrajectory(trajectory)
