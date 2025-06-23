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
        f"Position: ({missile.x[0]}, {missile.y[0]}) m\n"
        f"Acceleration: ({missile.ax[0]}, {missile.ay[0]}) m/s²\n"
        f"Density: {environment.rho} kg/m³\n"
        f"Pressure: {environment.p} Pa\n"
        f"Temperature: {environment.T} K\n"
        f"Speed of Sound: {environment.a} m/s\n"
        f"Gravity: {environment.gravity} m/s²\n"
        f"Time of Flight: {missile.flightTime:.5f} s\n"
        f"x-Range: {missile.x[-1]:.5f} m"
    )

    ax.text(x0, y0, text,
            verticalalignment='top',
            horizontalalignment='left',
            transform=ax.transAxes,
            family='monospace',
            bbox=dict(facecolor='lightgray', edgecolor='black', boxstyle='round,pad=0.3', alpha=0.3),
            )


def plotTrajectory(env, missiles, trajectories):
    fix, ax = plt.subplots(figsize=(10, 10))

    for idx, (missile, trajectory) in enumerate(zip(missiles, trajectories)):

        xVals, yVals = zip(*trajectory)
        xVals = np.array(xVals)
        yVals = np.array(yVals)

        ax.scatter(xVals, yVals, label=f"Missile {idx + 1}")
        ax.plot(np.unique(xVals), np.poly1d(np.polyfit(xVals, yVals, 2))(np.unique(xVals)),
                label=f"Missile {idx + 1} Fit")

    ax.set_xlabel('X Position (m)')
    ax.set_ylabel('Y Position (m)')
    ax.set_title('All Missile Trajectory')
    ax.legend(['Actual Trajectory', 'Fitted Line'], loc='upper left')
    ax.grid(True, alpha=0.5)

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
