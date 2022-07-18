from cvxopt import matrix
from cvxopt.glpk import ilp
import numpy as np

x = int(input("Enter Position X :"))
y = int(input("Enter Position Y :"))

"""
minimize A + B + C + D + E + F + G + H

Subject to

A, B, C, D, E, F, G, H >= 0
2 (A - B + E - F) + (C - D + G - H) = x
(A - B - E + F) + 2 (C - D - G + H) = y
"""

knight_var_x = [2, -2, 1, -1, 2, -2, 1, -1]
knight_var_y = [1, -1, 2, -2, -1, 1, -2, 2]

def minimize_knights_move(x, y):
    # Minimize Cx
    C = matrix([1] * 8, tc='d')
    # Equal Constraints (Ax = b)
    A = matrix([knight_var_x, knight_var_y], tc='d')
    b = matrix([x, y], tc='d')
    # >= 0 Constraints (Gx <= h)
    G = []
    for i in range(8):
        a = [0 for k in range(8)]
        a[i] = -1
        G.append(a)
    G = matrix(G, tc='d')
    h = matrix([0] * 8, tc='d')

    (status, x) = ilp(
        c = C,
        A = A.T,
        b = b,
        G = G.T,
        h = h,
        I = set(range(8))
    )
    res = np.array(x, dtype=np.int64).flatten().tolist()
    return res

res = minimize_knights_move(x, y)

for k_x, k_y, n_move in zip(knight_var_x, knight_var_y, res):
    if n_move == 0: continue
    print("Move type :", k_x, k_y, "| n_moves :", n_move)
