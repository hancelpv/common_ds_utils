##################
common_ds_utils
##################

Common Data Science Utilities required for DS/ML workflows

***********
Find a Bug?
***********
Check if there’s already an open `issue <https://github.com/idanmoradarthas/DataScienceUtils/issues>`_ on the topic. If
needed, file an issue.

***********
Open Source
***********
common_ds_utils license is `MIT License <https://opensource.org/licenses/MIT>`_.

******************
Installation
******************
pip install -i https://test.pypi.org/simple/ common-ds-utils==1.0.2

******************
Usage
******************

from common_ds_utils.metrics.mean_absolute_percentage_error import mean_absolute_percentage_error
import numpy as np

y1 = np.array([1, 2, 4])
y2 = np.array([1, 2, 2])
mape = round(mean_absolute_percentage_error(y1, y2), 2)
print(mape)
