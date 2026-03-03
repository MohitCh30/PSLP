import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats


x_norm = np.linspace(-10, 10, 1000)

x_exp = np.linspace(0, 10, 1000)


normal_params = [(0, 1), (0, 2), (-2, 1.5)]
plt.figure(figsize=(12, 5))

for mean, std in normal_params:
    y = stats.norm.pdf(x_norm, mean, std)
    plt.plot(x_norm, y, label=f"μ={mean}, σ={std}")

plt.title("Normal Distributions")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()


exp_params = [0.5, 1, 2]
plt.figure(figsize=(12, 5))

for lambd in exp_params:
    y = stats.expon.pdf(x_exp, scale=1/lambd)
    plt.plot(x_exp, y, label=f"λ={lambd}")

plt.title("Exponential Distributions")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid()
plt.show()