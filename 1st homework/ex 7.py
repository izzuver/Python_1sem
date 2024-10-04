import numpy as np

N = int(input())
M = int(input())
lin = np.eye(N, M - 1)
x = np.arange(N)

for i in range(N):
    s = input().split()
    for j in range(M - 1):
        lin[i, j] = int(s[j])
    x[i] = int(s[M - 1])

solv = np.linalg.solve(lin, x)
print(solv)