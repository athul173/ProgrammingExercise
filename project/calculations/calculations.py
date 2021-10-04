import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d


def find_mod(data):
    modarray = []
    for i in data.itertuples():
        mod = math.sqrt(math.pow(
            i[1], 2) + math.pow(i[2], 2) + math.pow(i[3], 2))
        modarray.append(mod)
    return modarray


def py_plotter(data):
    print("Starting Plotting...")
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    z_data = []
    x_data = []
    y_data = []
    for column in data:
        if column == 'x':
            x_data.append(data[column])
        if column == 'y':
            y_data.append(data[column])
        if column == 'z':
            z_data.append(data[column])
    ax.scatter3D(x_data, y_data, z_data, c=z_data, cmap='Greens')
    plt.show()
