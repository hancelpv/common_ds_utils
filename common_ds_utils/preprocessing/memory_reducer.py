import numpy as np
from pandas.api.types import is_categorical_dtype
from pandas.api.types import is_datetime64_any_dtype as is_datetime


def reduce_memory_usage(X):
    """Checks the ranges of values, assigns datatypes accordingly and reduce memory usage

    Args:
        X (pandas df): input dataframe

    Returns:
        X: dataframe after memory reduction
    """
    # Storing initial memory
    start_mem = X.memory_usage().sum() / 1024 ** 2
    print("Memory usage of dataframe is {:.2f} MB".format(start_mem))

    # Looping through columns, reducing memory usage one by one
    for col in X.columns:
        if is_datetime(X[col]) or is_categorical_dtype(X[col]):
            continue
        col_type = X[col].dtype

        if col_type != object:
            c_min = X[col].min()
            c_max = X[col].max()
            if str(col_type)[:3] == "int":
                if (
                    c_min > np.iinfo(np.int8).min
                    and c_max < np.iinfo(np.int8).max
                ):
                    X[col] = X[col].astype(np.int8)
                elif (
                    c_min > np.iinfo(np.int16).min
                    and c_max < np.iinfo(np.int16).max
                ):
                    X[col] = X[col].astype(np.int16)
                elif (
                    c_min > np.iinfo(np.int32).min
                    and c_max < np.iinfo(np.int32).max
                ):
                    X[col] = X[col].astype(np.int32)
                elif (
                    c_min > np.iinfo(np.int64).min
                    and c_max < np.iinfo(np.int64).max
                ):
                    X[col] = X[col].astype(np.int64)
            else:
                if (c_min > np.finfo(np.float16).min
                    and c_max < np.finfo(np.float16).max
                    ):
                    X[col] = X[col].astype(np.float16)
                elif (
                    c_min > np.finfo(np.float32).min
                    and c_max < np.finfo(np.float32).max
                ):
                    X[col] = X[col].astype(np.float32)
                else:
                    X[col] = X[col].astype(np.float64)
        else:
            X[col] = X[col].astype("category")

    end_mem = X.memory_usage().sum() / 1024 ** 2
    print(
        "Memory usage after optimization is: {:.2f} MB".format(end_mem)
    )
    print(
        "Decreased by {:.1f}%".format(
            100 * (start_mem - end_mem) / start_mem
        )
    )
    return X
