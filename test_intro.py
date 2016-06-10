import scipy as sp
from scipy import stats
from intro import *

# random numers
nums = sp.randn(100)

# normal distribution
nd1 = stats.norm()

basic_stat = stats.describe(nums)
print "no obs = %i" % basic_stat.nobs
print "mean = %.2f" % basic_stat.mean
print "variance = %.2f" % basic_stat.variance
print "skewness = %.2f" % basic_stat.skewness
print "kurtosis = %.2f" % basic_stat.kurtosis

# function calls
plot_hist(nums)
plot_cdf(nd1)
plot_pmf(nd1)
