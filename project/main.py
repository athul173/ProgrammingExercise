import pandas as pd
import statistics
import time
from calculations import calculations
from windows import windows
from calibration import methods


def main():
    chunks = pd.read_csv('./Data/GT3X+ (01 day)RAW.csv', chunksize=300,
                         header=None)
    nmw_data = windows.nonmovement(chunks)
    print('Finding Coefficients..')
    coefficients = methods.curve_fitting(nmw_data)
    calibration_method(nmw_data, coefficients)


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
    print("Mean of the old data is:  " + str(old_mean))
    print("Mean linear transformed data is:  " + str(new_mean))
    print("Standard deviation of the old data is:  " + str(old_std))
    print("Standard deviation of the linear transformed data is:  " + str(new_std))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("---Execution time:  %s seconds ---" % (time.time() - start_time))
