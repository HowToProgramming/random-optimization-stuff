from cvxopt import matrix
from cvxopt.glpk import ilp
import numpy as np

money = int(input("Enter Money : "))
# Minimize Coin Count
c = matrix([1] * 9, tc='d')
# Subject to Ax = b
banktypes = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
A = matrix([banktypes], tc='d')
b = matrix([money], tc='d')
# Coin Count > 0
G = []
for i in range(9):
    a = [0 for k in range(9)]
    a[i] = -1
    G.append(a)
G = matrix(G, tc='d')
h = matrix([0] * 9, tc='d')

(status, x) = ilp(
    c = c,
    A = A.T,
    b = b,
    G = G.T,
    h = h,
    I = set(range(9))
)

res = np.array(x, dtype=np.int64).flatten().tolist()
for count, banktype in zip(res, banktypes):
    print(count, banktype)