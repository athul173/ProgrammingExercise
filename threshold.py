import pandas as pd


def finder(chunks):
    #combinedstdarray = [[0, 0, 0]]
    #modarray = [[0]]
    max_threshold = [[0]]
    for index, chunk in enumerate(chunks):
        if index > 4850 and index < 5400:
            x_std = pd.DataFrame.std(chunk[0])
            y_std = pd.DataFrame.std(chunk[1])
            z_std = pd.DataFrame.std(chunk[2])
            windowrep = max(x_std, y_std, z_std)
        # if x_std < threshold and y_std < threshold and z_std < threshold:
            # for i in chunk.itertuples():
            #     mod = math.sqrt(math.pow(
            #         i[1], 2) + math.pow(i[2], 2) + math.pow(i[3], 2))
            #     modarray.append([mod])
            #combinedstdarray.append([x_std, y_std, z_std])
            max_threshold.append([windowrep])

    # print(*max_threshold)
    threshold = max(max_threshold)
    print("Maximum threshold is: " + str(threshold[0]))
    # plot_array = np.array(modarray[1:])
    # plt.plot(plot_array, 'o')
    # plt.xlabel('Time')
    # plt.ylabel('|Acceleration|')
    # plt.show()

    return float(threshold[0])
