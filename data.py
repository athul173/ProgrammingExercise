from os import read
import pandas as pd


def parser(data, window_size):
    reader = pd.read_csv(data, chunksize=window_size,
                         header=None)
    chunk_array = [[[]]]
    for windows in reader:
        window = [[]]
        for tuple in windows.itertuples():
            window.append([tuple])
        chunk_array.append(window)

    chunk_array.pop(0)
    return pd.DataFrame(chunk_array)
