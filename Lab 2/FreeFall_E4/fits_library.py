import numpy as np

def linear_fit(arr1,arr2):
    fit, error = np.polyfit(arr1, arr2, 1, cov = True)
    slope, intercept = fit[0], fit[1]
    slope_error, intercept_error = np.sqrt(error[0][0]), np.sqrt(error[1][1])
    return slope, intercept, slope_error, intercept_error

def quadratic_fit(data1, data2):
    fit, error = np.polyfit(data1, data2, 2, cov = True)
    a, b, c = fit[0], fit[1], fit[2]
    a_error, b_error, c_error = np.sqrt(error[0][0]), np.sqrt(error[1][1]), np.sqrt(error[2][2])
    return a, b, c, a_error, b_error, c_error