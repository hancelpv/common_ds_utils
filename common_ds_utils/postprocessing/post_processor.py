import numpy as np


class PostProcessor:
    """Generic post processor for processing predictions
    """

    def __init__(self, floor_at_zero=True, round_decimals=2):
        self.floor_at_zero = floor_at_zero
        self.round_decimals = round_decimals

    def process(self, y_pred):
        """process predictions

        Args:
            y_pred (np array): input data

        Returns:
            np array: predictions after post processing
        """

        if self.floor_at_zero:
            y_pred[y_pred < 0] = 0

        y_pred = np.round(y_pred, self.round_decimals)
        return y_pred


if __name__ == '__main__':
    y_pred = np.array([1.2352, 25.25123, -8.9])
    a = PostProcessor(floor_at_zero=False, round_decimals=3)
    print(a.process(y_pred))
