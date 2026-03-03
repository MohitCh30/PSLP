import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

x = np.linspace(0, 10, 1000)
lambdas = [0.5, 1.27]

plt.figure(figsize=(10, 5))
for lam in lambdas:
    y = expon.pdf(x, scale=1/lam)
    plt.plot(x, y, label=f'λ = {lam}')

plt.title("Exponential Distributions")
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.legend()
plt.grid(True)
plt.show()
