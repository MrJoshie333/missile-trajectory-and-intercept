import matplotlib.pyplot as plt

def plotTrajectory(trajectory):
    #create plot
    plt.figure(figsize=(10, 10))
    for x, y in trajectory:
        plt.scatter(x, y)
    # plt.scatter(trajectory)
    plt.show()

#<----- Debugging ----->
if __name__ == '__main__':
    trajectory = ([1, 4], [2, 6])
    plotTrajectory(trajectory)