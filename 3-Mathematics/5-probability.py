# Probability: The study of uncertainty and the likelihood of events occurring.
# It is a branch of mathematics that deals with the analysis of random phenomena.
# Probability Theory: The mathematical framework for quantifying uncertainty and modeling random events.
# Bayes' Theorem: A fundamental theorem in probability theory that describes how to update the probability of a hypothesis based on new evidence.

def bayes_theorem(prior, likelihood, evidence):
    return (likelihood * prior) / evidence
  
# Common Probability Distributions:
# 1. Uniform Distribution: All outcomes are equally likely.
def uniform_distribution(a, b, x):
    if a <= x <= b:
        return 1 / (b - a)
    else:
        return 0
      
# 2. Normal Distribution: A continuous probability distribution characterized by its bell-shaped curve.
import numpy as np
import matplotlib.pyplot as plt

# mu, sigma = 0, 1  # mean and standard deviation
# x = np.linspace(-4, 4, 100)  # range of x values
# y = (1 / (np.sqrt(2 * np.pi * sigma))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)  # normal distribution formula

# plt.plot(x, y)
# plt.title('Gaussian Distribution (mu=0, sigma=1)')
# plt.xlabel('x')
# plt.ylabel('Probability Density')
# plt.grid()
# plt.show()

def normal_distribution(mu, sigma, x):
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)
  
# 3. Binomial Distribution: A discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials.
def binomial_distribution(n, k, p):
    from math import comb
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))
  
# Bernoulli Distribution: A special case of the binomial distribution where n = 1.
def bernoulli_distribution(p, x):
    if x == 1:
        return p
    elif x == 0:
        return 1 - p
    else:
        raise ValueError("x must be either 0 or 1 for Bernoulli distribution")

# Plotting the Bernoulli distribution
# x = bernoulli_distribution(0.6, 1)  # Probability of success
# plt.bar([0, 1], [1 - x, x], tick_label=['Failure', 'Success'])
# plt.title('Bernoulli Distribution (p=0.5)')
# plt.xlabel('Outcome')
# plt.ylabel('Probability')
# plt.grid()
# plt.show()


# 4. Poisson Distribution: A discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space.
def poisson_distribution(lam, k): 
    from math import exp, factorial
    return (lam ** k * exp(-lam)) / factorial(k)
  
# 5. Binomial Distribution: A discrete probability distribution that describes the number of successes in a fixed number of independent Bernoulli trials.
from scipy.stats import binom

n, p = 10, 0.5  # number of trials and probability of success
x = np.arange(0, n + 1)  # possible number of successes
y = binom.pmf(x, n, p)  # probability mass function

# plt.bar(x, y)
# plt.title('Binomial Distribution (n=10, p=0.5)')
# plt.xlabel('Number of Successes')
# plt.ylabel('Probability')
# plt.grid()
# plt.show()

# Poisson Distribution: A discrete probability distribution that expresses the probability of a given number of events occurring in a fixed interval of time or space.
from scipy.stats import poisson

lam = 3  # average rate (lambda)
x = np.arange(0, 10)  # possible number of events
y = poisson.pmf(x, lam)  # probability mass function

# plt.bar(x, y)
# plt.title('Poisson Distribution (lambda=3)')
# plt.xlabel('Number of Events')
# plt.ylabel('Probability')
# plt.grid()
# plt.show()

# Applications in ML:
# Gaussian Distribution: Used in Gaussian Naive Bayes classifiers, which assume that the features follow a Gaussian distribution.
# It is also used in Gaussian Mixture Models (GMMs) for clustering and density estimation.
# Bernoulli Distribution: Used in binary classification problems, where the outcome can be either success (1) or failure (0).   
# It is also used in logistic regression, which models the probability of a binary outcome.
# Poisson Distribution: Used in modeling count data, such as the number of events occurring in a fixed interval of time or space.
# It is commonly used in natural language processing (NLP) for modeling word occurrences in documents.
# Binomial Distribution: Used in binary classification problems, where the outcome can be either success (1) or failure (0).
# It is also used in logistic regression, which models the probability of a binary outcome.
# Bayes' Theorem: Used in Bayesian inference, which updates the probability of a hypothesis based on new evidence.
# It is also used in Bayesian networks, which model the relationships between random variables.

# Baye's Theorem Example:
# a disease affects 1% of the population, the test is 95% accurate for diseased individuals, and 90% accurate for healthy individuals. 
# Find the probability of having the disease given a positive test result.
def bayes_theorem_example(prior, sensitivity, specificity):
    # Given data
    evicence = (sensitivity * prior) + ((1 - specificity) * (1 - prior))  # Total probability of a positive test result
    posterior = (sensitivity * prior) / evicence  # Posterior probability of having the disease given a positive test result
    
    return posterior
    # Applying Bayes' theorem
    
    
    # P_disease = prior  # Prior probability of disease
    # P_positive_given_disease = sensitivity  # Probability of positive test given disease
    # P_positive_given_no_disease = 1 - specificity  # Probability of positive test given no disease
    # P_no_disease = 1 - P_disease  # Probability of no disease

    # # Total probability of a positive test result
    # P_positive = (P_positive_given_disease * P_disease) + (P_positive_given_no_disease * P_no_disease)

    # # Applying Bayes' theorem
    # P_disease_given_positive = (P_positive_given_disease * P_disease) / P_positive

    # return P_disease_given_positive

# Example usage of Bayes' theorem
probability = bayes_theorem_example(0.01, 0.95, 0.90)
print("Probability of having the disease given a positive test result:", probability)
  