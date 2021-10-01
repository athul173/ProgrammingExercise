import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import threshold

chunks = pd.read_csv('./Data/GT3X+ (01 day)RAW.csv',
                     iterator=True, chunksize=300, header=None)


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
    #df.append(adder, ignore_index=True)

    #df = pd.DataFrame({"Time": b[:, 0], "Acceleration": b[:, 1]})
    # print(df)
    plot_array = np.array(initial_array)
    plt.plot(plot_array[:, 0], plot_array[:, 1], 'o')
    plt.xlabel('Time')
    plt.ylabel("|Acceleration|")
    plt.show()


def non_movement_windows(chunks):
    max_std = threshold.finder(chunks)
    nmw_array = [[0, 0, 0]]
    for chunk in chunks:
        x_std = pd.DataFrame.std(chunk[0])
        y_std = pd.DataFrame.std(chunk[1])
        z_std = pd.DataFrame.std(chunk[2])

        if x_std < max_std and y_std < max_std and z_std < max_std:
            for i in chunk.itertuples():
                nmw_array.append([i])
                print(i)

    print(nmw_array)


non_movement_windows(chunks)
