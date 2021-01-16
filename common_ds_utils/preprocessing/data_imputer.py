import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class DataFrameImputer(TransformerMixin):

    def __init__(self):
        """Impute missing values.

        Columns of dtype object are imputed with the most frequent value 
        in column.

        Columns of other types are imputed with mean of column.

        """

    def fit(self, X, y=None):

        self.fill = pd.Series([X[c].value_counts().index[0] if X[c].dtype.name == 'category'
                               else X[c].median() for c in X], index=X.columns)
        return self

    def transform(self, X, y=None):
        temp = X.copy(deep=True)
        check_is_fitted(self, 'fill')
        return temp.fillna(self.fill)
