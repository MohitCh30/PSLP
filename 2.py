import math as m
import matplotlib.pyplot as plt

listy = []

def iterator(n, p, q):
    for i in range(n + 1):
        result = m.comb(n, i) * (p*i) * (q*(n - i))
        print(f"p({i}) = {result:.5f}")
        listy.append(result)

trials = int(input("Enter number of trials: "))
prob1 = float(input("Enter the probability of one success: "))
prob2 = 1 - prob1

iterator(trials, prob1, prob2)
plt.plot(listy, marker='o')
plt.title("Binomial Distribution")
plt.xlabel("Number of Successes")
plt.ylabel("Probability")
plt.show() 

