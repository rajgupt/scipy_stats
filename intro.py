import numpy as np
from matplotlib import pyplot as plt


# basic statistic plot
def plot_hist(nums):
    # histogram
    bins = plt.hist(nums)
    plt.title('Normal Dist Sample Histogram')

    # Tip: to prettify the printing of double numbers, use np.set_printoptions
    np.set_printoptions(precision=2, suppress=True)

    print "counts = ", bins[0]
    print "bin values = ", bins[1]

# probability distributions #


def plot_cdf(dist):
    '''
    plots the cdf of the distribution having cdf member defined
    '''
    x = np.arange(-3, 3, 0.1)

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
    x = np.arange(-3, 3, 0.1)
    # new figure - pdf (probabilty density function)
    plt.figure()
    ax = plt.gca()
    plt.plot(x, dist.pdf(x), 'r-', label='pdf')
    plt.title('PDF of Normal Dist')
    ax.legend()
