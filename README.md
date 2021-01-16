## Common Data Science Utils
Common Data Science Utilities required for DS/ML workflows

## Installation
<pre>
pip install -i https://test.pypi.org/simple/ common-ds-utils==1.0.2
</pre>

## Usage
<pre>
from common_ds_utils.metrics.mean_absolute_percentage_error import mean_absolute_percentage_error
import numpy as np

y1 = np.array([1, 2, 4])
y2 = np.array([1, 2, 2])
mape = round(mean_absolute_percentage_error(y1, y2), 2)
print(mape)
</pre>

## Open Source
common_ds_utils license is `MIT License <https://opensource.org/licenses/MIT>`_.
