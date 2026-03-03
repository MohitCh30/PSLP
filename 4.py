# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(-10, 10, 500)

# mean = int(input("Enter mean: "))
# std = int(input("Enter Standard Deviation: "))

# plt.figure(figsize=(10, 6))
# y = (1 / (std * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std)**2)
# plt.plot(x, y, label=f"μ = {mean}, σ = {std}")

# plt.title("Normal Distribution for Various Parametric Values")
# plt.xlabel('x')
# plt.ylabel('Probability Density')
# plt.legend()
# plt.grid()
# plt.show()

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

x = np.linspace(-10, 10, 500)

mean = int(input("Enter mean: "))
std = int(input("Enter Standard Deviation: "))

plt.figure(figsize=(10, 6))
y = norm.pdf(x, loc=mean, scale=std)
plt.plot(x, y, label=f"μ = {mean}, σ = {std}")

plt.title("Normal Distribution using scipy.stats.norm")
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.legend()
plt.grid()
plt.show()
