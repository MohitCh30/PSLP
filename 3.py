import math as m
import matplotlib.pyplot as plt

listy = []

def iterator(n, lamb):
    for i in range(n + 1):
        result = (m.exp(-lamb) * (lamb**i)) / m.factorial(i)
        print(f"p({i}) = {result:.5f}")
        listy.append(result)

trials = int(input("Enter number of trials: "))
lamb = float(input("Enter the lambda (rate parameter): "))
iterator(trials, lamb)
plt.plot(listy, marker='o')
plt.title("Poisson Distribution")
plt.xlabel("Number of Events")
plt.ylabel("Probability")
plt.show()
