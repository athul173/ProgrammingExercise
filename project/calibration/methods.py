import math
import statistics
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def brute_force(nmw_data):

    value = 10
    g = -9
    # find all non movement window mods
    dx = value
    dy = value
    dz = value
    gx = g
    gy = g
    gz = g
    combined_mod = []
    mean_error_array = []
    for tuples in nmw_data.itertuples():
        mod = math.sqrt(math.pow(
            tuples[1], 2) + math.pow(tuples[2], 2) + math.pow(tuples[3], 2))
        combined_mod.append(mod)
        ax = tuples[1]
        ay = tuples[2]
        az = tuples[3]

        sum_of_dx2 = math.pow(dx, 2) + math.pow(dy, 2) + math.pow(dz, 2)
        sum_of_gax2 = math.pow(gx * ax, 2) + math.pow(gy *
                                                      ay, 2) + math.pow(gz * az, 2)
        sum_of_dgax = 2 * (dx * gx * ax + dy * gy * ay + dz * gz * az)
        root = math.sqrt(sum_of_dx2 + sum_of_gax2 + sum_of_dgax)
        mean_error_array.append(abs(1 - root))

    mean_error = statistics.mean(mean_error_array)
    print(root)
    print(mean_error)
    print(statistics.mean(combined_mod))
    # get the mean euclidean norm of non-movement windows

    # combined_mod_mean = pd.DataFrame.mean(combined_mod)

    # print(statistics.mean(combined_mod))

    # minimise

    # root = math.sqrt(sum_of_dx2 + sum_of_gax2 + sum_of_dgax)
    #  abs( 1 - root )


def Objective(X, A, B, C, D, E, F):
    x, y, z = X[0], X[1], X[2]
    sum_of_dx2 = A**2 + B**2 + C**2
    sum_of_gax2 = (x*D)**2 + (y*E)**2 + (z*F)**2
    sum_of_dgax = 2*(x*D*A + y*E*B + z*F*C)
    shu = sum_of_dx2 + sum_of_gax2 + sum_of_dgax
    return shu


def curve_fitting(nmw_data):
    combined_mod = []
    xdata = []
    ydata = []
    zdata = []
    for column in nmw_data:
        # mod = math.sqrt(math.pow(
        #     tuples[1], 2) + math.pow(tuples[2], 2) + math.pow(tuples[3], 2))
        # combined_mod.append(mod)
        if column == 'x':
            xdata.append(nmw_data[column])
        if column == 'y':
            ydata.append(nmw_data[column])
        if column == 'z':
            zdata.append(nmw_data[column])

    xdata = np.array(xdata[0])
    ydata = np.array(ydata[0])
    zdata = np.array(zdata[0])
    data = [xdata, ydata, zdata]
    onedata = np.ones(len(xdata), int)
    parameters, covariance = curve_fit(
        Objective, [xdata, ydata, zdata], onedata, maxfev=5000)
    fit_A = parameters[0]
    fit_B = parameters[1]
    fit_C = parameters[2]
    fit_D = parameters[3]
    fit_E = parameters[4]
    fit_F = parameters[5]
    print("xOffset is : " + str(fit_A))
    print("yOffset is : " + str(fit_B))
    print("zOffset is : " + str(fit_C))
    print("xGain is : " + str(fit_D))
    print("yGain is : " + str(fit_E))
    print("zGain is : " + str(fit_F))
    return [fit_A, fit_B, fit_C, fit_D, fit_E, fit_F]
#
