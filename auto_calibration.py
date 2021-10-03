import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import threshold
import data

chunks = pd.read_csv('./Data/GT3X+ (01 day)RAW.csv', chunksize=300,
                     header=None)


def py_plotter():
    # chunks.plot()
    # plt.show()
    initial_array = [[0, 0]]
    for chunk in chunks.itertuples():
        print(chunk)
        y = math.sqrt(math.pow(
            chunk[1], 2) + math.pow(chunk[2], 2) + math.pow(chunk[3], 2))
    # adder = pd.DataFrame([[chunk[0], y]], columns=["Time", "Acceleration"])
        initial_array.append([chunk[0], y])
    # df.append(adder, ignore_index=True)

    # df = pd.DataFrame({"Time": b[:, 0], "Acceleration": b[:, 1]})
    # print(df)
    plot_array = np.array(initial_array)
    plt.plot(plot_array[:, 0], plot_array[:, 1], 'o')
    plt.xlabel('Time')
    plt.ylabel("|Acceleration|")
    plt.show()


def non_movement_windows():
    max_std = threshold.finder(chunks)
    nmw_array = []
    for chunk in pd.read_csv('./Data/GT3X+ (01 day)RAW.csv', chunksize=300,
                             header=None):
        x_std = pd.DataFrame.std(chunk[0])
        y_std = pd.DataFrame.std(chunk[1])
        z_std = pd.DataFrame.std(chunk[2])
        if x_std < max_std and y_std < max_std and z_std < max_std:
            for i in chunk.itertuples():
                nmw_array.append([i[1], i[2], i[3]])
    nmw_array.pop(0)
    return nmw_array


final_array = pd.DataFrame(non_movement_windows(), columns=['x', 'y', 'z'])
final_array = final_array.loc[(final_array != 0).any(axis=1)]
print(final_array)


def average_calibration_error():
    # get the mean euclidean norm of nmw
    # find the difference between mean euclidean norm and 1 g
    # minimise
    pass
