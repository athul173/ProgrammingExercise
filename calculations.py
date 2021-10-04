import math


def find_mod(data):
    modarray = []
    for i in data.itertuples():
        mod = math.sqrt(math.pow(
            i[1], 2) + math.pow(i[2], 2) + math.pow(i[3], 2))
        modarray.append(mod)
    return modarray
