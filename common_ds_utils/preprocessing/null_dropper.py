from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class NullDropper(BaseEstimator, TransformerMixin):
    """Drops rows with nulls greater than a treshold.
    Treshold value is expected between 0 and 1

    Args:
        BaseEstimator ([type]): [description]
        TransformerMixin ([type]): [description]

    Returns:
        pandas df: dataframe after dropping nulls
    """
    # Class Constructor
    def __init__(self, treshold):
        self.treshold = treshold
        self.cols_with_nulls = None

    def fit(self, X, y=None):
        self.cols_with_nulls = list(
            X.columns[X.isnull().mean() > self.treshold])
        return self

    def transform(self, X, y=None):
        temp = X.copy()
        check_is_fitted(self, 'cols_with_nulls')
        print("self.cols_with_nulls : {}".format(self.cols_with_nulls))
        temp.drop(self.cols_with_nulls, axis=1, inplace=True)
        return temp
