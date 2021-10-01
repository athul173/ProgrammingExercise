import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

chunks = pd.read_csv('GT3X+ (01 day)RAW.csv',
                     iterator=True, chunksize=300, header=None)


def threshold_finder():
    #combinedstdarray = [[0, 0, 0]]
    #modarray = [[0]]
    max_threshold = [[0]]
    for chunk in chunks:
        x_std = pd.DataFrame.mean(chunk[0])
        y_std = pd.DataFrame.mean(chunk[1])
        z_std = pd.DataFrame.mean(chunk[2])
        print('Values area: ' + str(x_std), str(y_std), str(z_std))
        windowrep = max(x_std, y_std, z_std)
        print('The rep is : ' + str(windowrep))
    # if x_std < threshold and y_std < threshold and z_std < threshold:
        # for i in chunk.itertuples():
        #     mod = math.sqrt(math.pow(
        #         i[1], 2) + math.pow(i[2], 2) + math.pow(i[3], 2))
        #     modarray.append([mod])
        #combinedstdarray.append([x_std, y_std, z_std])
        max_threshold.append([windowrep])

    print(*max_threshold)
    print("Maximum threshold is: " + str(max(max_threshold)))
    # plot_array = np.array(modarray[1:])
    # plt.plot(plot_array, 'o')
    # plt.xlabel('Time')
    # plt.ylabel('|Acceleration|')
    # plt.show()


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
