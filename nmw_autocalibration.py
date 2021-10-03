import math
import statistics
import numpy as np
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

    # Formulate and solve the least squares problem ||Ax - b ||^2
    A = np.hstack([X**2, X * Y, Y**2, X, Y, Z])
    b = np.ones_like(X)
    x = np.linalg.lstsq(A, b)[0].squeeze()

    # Print the equation of the ellipse in standard form
    print('The ellipse is given by {0:.3}x^2 + {1:.3}xy+{2:.3}y^2+{3:.3}x+{4:.3}y = 1'.format(
        x[0], x[1], x[2], x[3], x[4]))

    # Plot the noisy data
    plt.scatter(X, Y, label='Data Points')

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
