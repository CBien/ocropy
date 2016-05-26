from numpy import *
from scipy import *
try:
    from matplotlib import *
    from matplotlib.pyplot import *
except ImportError:
    import logging
    logging.getLogger(__name__).error(
            'Warning : Could not import matplotlib : graphical debug will not work')

