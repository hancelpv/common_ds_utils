import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import StandardScaler


class CustomScaler(BaseEstimator, TransformerMixin):
    """Custom Scaler which identifies numeric cols except target and applies standard scaler

    Args:
        BaseEstimator ([type]): [description]
        TransformerMixin ([type]): [description]

    Returns:
        pandas df: returns scaled df
    """
    # Class Constructor

    def __init__(self, target_col):
        self.target_col = target_col
        self.cols_to_scale = None

    def fit(self, X, y=None):
        numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        numeric_cols = list(X.select_dtypes(include=numerics).columns)
        self.cols_to_scale = [x for x in numeric_cols if x != self.target_col]
        self.std = StandardScaler().fit(X[self.cols_to_scale])
        return self

    def transform(self, X, y=None):
        temp = X.copy()
        print("self.cols : {}".format(self.cols_to_scale))
        temp[self.cols_to_scale] = self.std.transform(temp[self.cols_to_scale])
        return temp


if __name__ == '__main__':
    a = CustomScaler("")
    df = pd.DataFrame()
    print(df)
    df['a1'] = [1, 2, 4]
    df['a2'] = [1.0, 3, 4]
    df['a3'] = ['one', 'two', 'three']

    print(df.dtypes)
    print(a.fit_transform(df))
