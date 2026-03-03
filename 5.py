import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Inputs
n = int(input("Enter number of trials (n): "))
p = float(input("Enter probability of success (p): "))
size = int(input("Enter sample size: "))

# Mean and Variance
mean, var = n * p, n * p * (1 - p)
print(f"Mean: {mean:.2f}\nVariance: {var:.2f}")

data = np.random.binomial(n, p, size)
x_vals = np.arange(n + 1)
sample_probs = np.bincount(data, minlength=n + 1) / size
theory_probs = binom.pmf(x_vals, n, p)

plt.figure(figsize=(10, 6))
plt.bar(x_vals - 0.2, sample_probs, width=0.4, label="Sample Data", color='skyblue', edgecolor='black')
plt.plot(x_vals, theory_probs, 'ro-', label="Theoretical PMF", linewidth=2, markersize=6)

plt.title(f"Binomial Distribution\nMean = {mean:.2f}, Variance = {var:.2f}", fontsize=16)
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.xticks(x_vals)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
