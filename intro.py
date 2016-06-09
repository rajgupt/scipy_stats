import numpy as np
import scipy as sp
from scipy import stats


# import matplotlib as mpl
from matplotlib import pyplot as plt

# random numers
nums = sp.randn(100)

basic_stat = stats.describe(nums)
print "noobs = %i" % basic_stat.nobs
print "mean = %.2f" % basic_stat.mean
print "variance = %.2f" % basic_stat.variance
print "skewness = %.2f" % basic_stat.skewness
print "kurtosis = %.2f" % basic_stat.kurtosis

# basic statistic plot

# histogram
plt.hist(nums, bins=5)

#############################
#                           #
# probability distributions #
#                           #
#############################

x = np.arange(-3, 3, 0.1)

# normal distribution
nd1 = stats.norm()

