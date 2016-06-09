import numpy as np
import scipy as sp
from scipy import stats


# import matplotlib as mpl
from matplotlib import pyplot as plt

# random numers
nums = sp.randn(100)

basic_stat = stats.describe(nums)
print "no obs = %i" % basic_stat.nobs
print "mean = %.2f" % basic_stat.mean
print "variance = %.2f" % basic_stat.variance
print "skewness = %.2f" % basic_stat.skewness
print "kurtosis = %.2f" % basic_stat.kurtosis

# basic statistic plot

# histogram
bins = plt.hist(nums)
plt.title('Normal Dist Sample Histogram')
# Tip: to prettify the printing of double numbers, use np.set_printoptions
np.set_printoptions(precision=2, suppress=True)

print "counts = ", bins[0]
print "bin values = ", bins[1]

#############################
#                           #
# probability distributions #
#                           #
#############################

x = np.arange(-3, 3, 0.1)

# normal distribution
nd1 = stats.norm()

# new figure - cdf (commulative probability function)
plt.figure()
ax = plt.gca()
plt.plot(x, nd1.cdf(x), 'r-', label='cdf')
plt.title('CDF of Normal Dist')
ax.legend()

# new figure - pdf (probabilty density function)
plt.figure()
ax = plt.gca()
plt.plot(x, nd1.pdf(x), 'r-', label='pdf')
plt.title('PDF of Normal Dist')
ax.legend()
