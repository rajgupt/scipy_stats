import numpy as np
import scipy as sp
from scipy import stats
from matplotlib import pyplot as plt

# random numers
nums = sp.randn(100)
x = np.arange(-3, 3, 0.1)

# normal distribution
nd1 = stats.norm()

basic_stat = stats.describe(nums)
print "no obs = %i" % basic_stat.nobs
print "mean = %.2f" % basic_stat.mean
print "variance = %.2f" % basic_stat.variance
print "skewness = %.2f" % basic_stat.skewness
print "kurtosis = %.2f" % basic_stat.kurtosis

# basic statistic plot


def plot_hist(nums):
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


def plot_cdf(dist):
    '''
    plots the cdf of the distribution having cdf member defined
    '''
    # new figure - cdf (commulative probability function)
    plt.figure()
    # get current axis
    ax = plt.gca()
    plt.plot(x, dist.cdf(x), 'r-', label='cdf')
    plt.title('CDF of Normal Dist')
    ax.legend()


def plot_pmf(dist):
    '''
    plots the pdf of the distribution having cdf member defined
    '''
    # new figure - pdf (probabilty density function)
    plt.figure()
    ax = plt.gca()
    plt.plot(x, dist.pdf(x), 'r-', label='pdf')
    plt.title('PDF of Normal Dist')
    ax.legend()

plot_hist(nums)
plot_cdf(nd1)
plot_pmf(nd1)
