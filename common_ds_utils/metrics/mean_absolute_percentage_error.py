import numpy as np


def mean_absolute_percentage_error(y_true, y_pred):
    """function to calculate mean_absolute_percentage_error, excluding zeros in actuals

    Args:
        y_true (np array): array containing true values
        y_pred (np array): array container predictions

    Returns:
        float: mape value in percentage
    """
    if len(y_true) == 0 or len(y_pred) == 0:
        return 0
    mask = y_true != 0
    count_of_zeros = len(y_true) - len(mask)
    if count_of_zeros:
        print("{} zero values encountered in the y_true".format(count_of_zeros))
    return (np.fabs(y_true - y_pred)/y_true)[mask].mean()*100
