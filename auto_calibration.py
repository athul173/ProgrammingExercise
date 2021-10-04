import pandas as pd
import math
import numpy as np
import nmw_autocalibration
import calculations
import threshold
import statistics


def non_movement_windows(chunks):
    print('Calculating non_movement_windows')
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

    # removing all zero values used
    print("Removing all zero values")
    nmw_data = pd.DataFrame(nmw_array, columns=['x', 'y', 'z'])
    nmw_data = nmw_data.loc[(nmw_data != 0).any(axis=1)]
    return nmw_data


def calibration_method(nmw_data, coefficients):
    linear_transformed_data = []
    for tuples in nmw_data.itertuples():
        new_tuple = [tuples[1]*coefficients[3] + coefficients[0], tuples[2] *
                     coefficients[4] + coefficients[1], tuples[3]*coefficients[5] + coefficients[2]]
        linear_transformed_data.append(new_tuple)
    linear_transformed_data = pd.DataFrame(
        linear_transformed_data, columns=['x', 'y', 'z'])
    old_mod = calculations.find_mod(nmw_data)
    new_mod = calculations.find_mod(linear_transformed_data)
    old_mean = statistics.mean(old_mod)
    new_mean = statistics.mean(new_mod)
    old_std = statistics.stdev(old_mod, 1)
    new_std = statistics.stdev(new_mod, 1)
    print("Standard deviation of the linear transformed data is:  " + str(new_std))


chunks = pd.read_csv('./Data/GT3X+ (01 day)RAW.csv', chunksize=300,
                     header=None)
nmw_data = non_movement_windows(chunks)
print('Finding Coefficients..')
coefficients = nmw_autocalibration.curve_fitting(nmw_data)
calibration_method(nmw_data, coefficients)
