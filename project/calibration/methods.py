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


def fit(nmw_data):

    N = len(nmw_data)
    DIM = 3

  #  X = Column vector of ax (first column in csv file)
  #  Y = Column vector of ay (second column in csv file)
  #  Z = Column vector of az (third column in csv file)

    # Formulate and solve the least squares problem ||Ax - b ||^2
    A = np.hstack([1, 1, 1, X**2, Y**2, Z**2, 2 * X, 2*Y, 2*Z])
    b = np.ones_like(X)
    x = np.linalg.lstsq(A, b)[0].squeeze()

    # Print the equation of the ellipse in standard form
    print('The ellipse is given by {0:.3}+{1:.3}+{2:.3}+{3:.3}x^2 + {4:.3}y^2+ {5:.3}z^2+{6:.3}x+{7:.3}y+{8:.3}z = 1'.format(
        x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7], x[8]))

    # Plot the noisy data
    plt.scatter(X, Y, Z, label='Data Points')

    # Plot the original ellipse from which the data was generated
    phi = np.linspace(0, 2*np.pi, 1000).reshape((1000, 1))
    c = np.hstack([np.cos(phi), np.sin(phi)])
    ground_truth_ellipse = c.dot(B)
    plt.plot(ground_truth_ellipse[:, 0], ground_truth_ellipse[:,
             1], 'k--', label='Generating Ellipse')

    # Plot the least squares ellipse
    x_coord = np.linspace(-5, 5, 300)
    y_coord = np.linspace(-5, 5, 300)
    X_coord, Y_coord = np.meshgrid(x_coord, y_coord)
    Z_coord = x[0] * X_coord ** 2 + x[1] * X_coord * Y_coord + \
        x[2] * Y_coord**2 + x[3] * X_coord + x[4] * Y_coord
    plt.contour(X_coord, Y_coord, Z_coord, levels=[
                1], colors=('r'), linewidths=2)

    plt.legend()
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.show()


#  X = [x, y, z]


def objective(X, dx, dy, dz, gx, gy, gz):
    ax = X[0]
    ay = X[1]
    az = X[2]
    sum_of_dx2 = dx**2 + dy**2 + math.pow(dz, 2)
    sum_of_gax2 = math.pow(gx * ax, 2) + math.pow(gy *
                                                  ay, 2) + math.pow(gz * az, 2)
    sum_of_dgax = 2 * (dx * gx * ax + dy * gy * ay + dz * gz * az)
    return sum_of_dx2 + sum_of_gax2 + sum_of_dgax


def Gauss(X, A, B, C, D, E, F):
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
        Gauss, [xdata, ydata, zdata], onedata, maxfev=5000)
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
