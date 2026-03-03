from scipy.optimize import linprog

objective = [-3, -5, -7]  # Coefficients for maximization (convert to minimization)

constraints = [
    [1, 2, 1],
    [2, 1, 3],
    [1, 1, 2]
]

rhs = [10, 15, 11]
bounds = [(0, None), (0, None), (0, None)]

result = linprog(c=objective, A_ub=constraints, b_ub=rhs, bounds=bounds, method='simplex')

if result.success:
    print("Optimal solution found!")
    print("Values for x1, x2, x3:", result.x)
    print("Optimal value (Z):", -result.fun)  # Negate for max
else:
    print("No solution found:", result.message)

