import numpy as np
import matplotlib.pyplot as plt

def calculate_normal_distribution(x, mean, std_dev):
    return np.exp(-((x - mean) / std_dev)**2 / 2) / (std_dev * np.sqrt(2 * np.pi))

mean = float(input("Enter the mean of the normal distribution: "))
std_dev = float(input("Enter the standard deviation of the normal distribution: "))
num_data_points = int(input("Enter the number of data points to generate: "))

data = np.random.normal(mean, std_dev, num_data_points)

plt.hist(data, bins=30, density=True, alpha=0.5, label='Data')
x = np.linspace(mean - 3 * std_dev, mean + 3 * std_dev, 100)
plt.plot(x, calculate_normal_distribution(x, mean, std_dev), label='Given Normal Distribution', color='red')

plt.legend()
plt.show()
