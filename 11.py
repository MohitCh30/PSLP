from scipy.optimize import linprog

costs = [8, 6, 10, 9, 12, 13, 14, 9, 6]
supply = [20, 30, 25]
demand = [10, 25, 40]

A_eq = [[1 if k // 3 == j else 0 for k in range(9)] for j in range(3)]
A_eq += [[1 if k % 3 == j else 0 for k in range(9)] for j in range(3)]
b_eq = supply + demand

res = linprog(c=costs, A_eq=A_eq, b_eq=b_eq, method='highs')

if res.success:
    x = res.x.reshape(3, 3)
    print("Optimal Transportation Plan (units from source to destination):")
    for i in range(3):
        for j in range(3):
            print(f"From Source {i+1} to Destination {j+1}: {x[i][j]:.2f}")
    print(f"\nTotal Minimum Cost: {res.fun:.2f}")
else:
    print("No optimal solution found!")
