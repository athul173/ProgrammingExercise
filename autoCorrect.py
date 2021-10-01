import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

chunks = pd.read_csv('GT3X+ (01 day)RAW.csv',
                     iterator=True, chunksize=300, header=None)


def thresholdFinders():
    #combinedstdarray = [[0, 0, 0]]
    #modarray = [[0]]
    maxthreshold = [[0]]
    for chunk in chunks:
        xstd = pd.DataFrame.mean(chunk[0])
        ystd = pd.DataFrame.mean(chunk[1])
        zstd = pd.DataFrame.mean(chunk[2])
        print('Values area: ' + str(xstd), str(ystd), str(zstd))
        windowrep = max(xstd, ystd, zstd)
        print('The rep is : ' + str(windowrep))
    # if xstd < threshold and ystd < threshold and zstd < threshold:
        # for i in chunk.itertuples():
        #     mod = math.sqrt(math.pow(
        #         i[1], 2) + math.pow(i[2], 2) + math.pow(i[3], 2))
        #     modarray.append([mod])
        #combinedstdarray.append([xstd, ystd, zstd])
        maxthreshold.append([windowrep])

    print(*maxthreshold)
    print("Maximum threshold is: " + str(max(maxthreshold)))
    # plotarray = np.array(modarray[1:])
    # plt.plot(plotarray, 'o')
    # plt.xlabel('Time')
    # plt.ylabel('|Acceleration|')
    # plt.show()


def pyplotter():
    # chunks.plot()
    # plt.show()
    initialarray = [[0, 0]]
    for chunk in chunks.itertuples():
        print(chunk)
        y = math.sqrt(math.pow(
            chunk[1], 2) + math.pow(chunk[2], 2) + math.pow(chunk[3], 2))
    # adder = pd.DataFrame([[chunk[0], y]], columns=["Time", "Acceleration"])
        initialarray.append([chunk[0], y])
    #df.append(adder, ignore_index=True)

    #df = pd.DataFrame({"Time": b[:, 0], "Acceleration": b[:, 1]})
    # print(df)
    plotarray = np.array(initialarray)
    plt.plot(plotarray[:, 0], plotarray[:, 1], 'o')
    plt.xlabel('Time')
    plt.ylabel("|Acceleration|")
    plt.show()
