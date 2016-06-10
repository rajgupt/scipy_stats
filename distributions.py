import numpy as np
import scipy.stats
import matplotlib.pyplot as plt

# stats distributions
from scipy import stats

allDists = ['norm', 'expon', 'binom', 'chi2', 't', 'f']

# 1. normal distribution
from scipy.stats import norm

# 2. exponential distribution
from scipy.stats import expon

# 3. binomial distribution
from scipy.stats import binom

# 4. chi-square distribution
from scipy.stats import chi2

# 5. t distribution
from scipy.stats import t

# 6. f distribution
from scipy.stats import f



##
# discussion items

# 1. Show histogram of all distributions
def plot_sample_hist(sample, title):
    plt.figure()
    plt.title(title)
    plt.hist(sample)

sample = norm.rvs(size=1000)
plot_sample_hist(sample, 'normal distribution')

sample = expon.rvs(size=1000)
plot_sample_hist(sample, 'exponential distribution')

sample = binom.rvs(10, 0.5, size=1000)
plot_sample_hist(sample, 'binomial distribution')

sample = chi2.rvs(10, size=1000)
plot_sample_hist(sample, 'chi-square distribution')

sample = t.rvs(10, size=1000)
plot_sample_hist(sample, 't distribution')

sample = f.rvs(10, 20, size=1000)
plot_sample_hist(sample, 'f distribution')
