import unittest

import numpy as np
from common_ds_utils.metrics.mean_absolute_percentage_error import \
    mean_absolute_percentage_error


class TryTesting(unittest.TestCase):

    def test_one(self):
        y1 = np.array([1, 2, 4])
        y2 = np.array([1, 2, 2])
        mape = round(mean_absolute_percentage_error(y1, y2), 2)
        self.assertAlmostEqual(mape, 16.67)

    def test_two(self):
        y1 = np.array([1, 4])
        y2 = np.array([])
        mape = round(mean_absolute_percentage_error(y1, y2), 2)
        self.assertEqual(mape, 0)


if __name__ == '__main__':
    try:
        unittest.main()
    except Exception as e:
        print(str(e))
