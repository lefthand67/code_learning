import platform
import numpy as np
import matplotlib
import pandas as pd

print('Machine:', platform.machine())
print('Python:', platform.python_version())
print('pandas:', pd.__version__)
print('numpy:', np.version.version)
print('matplotlib:', matplotlib.__version__)