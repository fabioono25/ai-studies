# Statistics: The study of data collection, analysis, interpretation, presentation, and organization.
# Descriptive Statistics: Methods for summarizing and organizing data.
# Inferential Statistics: Techniques for making predictions or inferences about a population based on a sample.

# Central Tendency: Measures that summarize a set of data by identifying the central point within that set.

from statistics import mode

data = [10, 20, 30, 40, 50, 20]
mean = sum(data) / len(data)  # Mean (average)
print("Mean:", mean)
median = sorted(data)[len(data) // 2] if len(data) % 2 == 1 else  (sorted(data)[len(data) // 2 - 1] + sorted(data)[len(data) // 2]) / 2  # Median (middle value)
print("Median:", median)
print("Mode:", mode(data))  # Mode (most frequent value)

# Dispersion: Measures that describe the spread or variability of a dataset.
variance = sum((x - mean) ** 2 for x in data) / (len(data) - 1)  # Sample variance
print("Variance:", variance)

# Standard Deviation: The square root of the variance, representing the average distance of each data point from the mean.
std_dev = variance ** 0.5
print("Standard Deviation:", std_dev)

# Hypotestic Testing: A statistical method used to make inferences or draw conclusions about a population based on sample data. Steps:
# 1. Formulate a null hypothesis (H0) and an alternative hypothesis (H1).
# 2. Choose a significance level (alpha), typically 0.05. 
# 3. Collect data and calculate a test statistic.
# 4. Compare the test statistic to a critical value or use a p-value to determine
#    whether to reject or fail to reject the null hypothesis.
# Example: Testing if the mean of a sample is significantly different from a known population mean.

# Confidence Intervals: A range of values that is likely to contain the true population parameter with a specified level of confidence (e.g., 95%).

import scipy.stats as stats

sample_mean = mean
z_score = 1.96  # Z-score for 95% confidence level
ci = (sample_mean - z_score * (std_dev / (len(data) ** 0.5)), sample_mean + z_score * (std_dev / (len(data) ** 0.5)))  # Confidence interval
print("Confidence Interval (95%):", ci)


# Statistical Significance: A measure of whether the results of a statistical test are likely to be due to chance or if they reflect a true effect in the population.

########################################################################################################

# Perform a T-Test
group1 = [2.1, 2.5, 2.8, 3.0, 3.2]
group2 = [1.8, 2.0, 2.4, 2.7, 2.9]

# Perform a t-test
t_stat, p_value = stats.ttest_ind(group1, group2)
print("T-Statistic:", t_stat)
print("P-Value:", p_value)

# Interpretation
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: There is a significant difference between the two groups.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference between the two groups.")
