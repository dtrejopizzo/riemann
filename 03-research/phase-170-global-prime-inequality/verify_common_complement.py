"""Finite Galerkin diagnostics for R170_805; not an interval certificate."""
import json
import math
import numpy as np


def primitive(x):
    return x * math.log(x) - x if x else 0.0


def xlogx(x):
    return x * math.log(x) if x else 0.0


def check(n, slots):
    h = 1 / n
    beta = math.log(2) + 0.5
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            d = i - j
            integral = xlogx(d + 1) + xlogx(d - 1) - 2 * xlogx(d)
            matrix[i, j] = matrix[j, i] = -integral / 2
    for i in range(n):
        left, right = i * h, (i + 1) * h
        potential = -(primitive(right) - primitive(left)
                      + primitive(1 - left) - primitive(1 - right)) / (2 * h)
        matrix[i, i] = -sum(matrix[i]) + potential
    selected = [i for slot in slots for i in slot]
    complement = [i for i in range(n) if i not in selected]
    cross = matrix[np.ix_(selected, complement)]
    short = matrix[np.ix_(selected, selected)] - cross @ np.linalg.solve(
        matrix[np.ix_(complement, complement)], cross.T)
    width = len(slots[0])
    assert all(len(slot) == width and list(slot) == list(range(slot[0], slot[0] + width)) for slot in slots)
    epsilon = width * h
    lower = beta * np.eye(len(selected)) - beta * h / (
        2 * math.log(2) + len(selected) * h) * np.ones((len(selected), len(selected)))
    deficits = []
    for k, slot in enumerate(slots):
        distances = [abs(slot[0] - other[0]) / width for other in slots if other != slot]
        assert all(d >= 1 for d in distances)
        deficit = sum(math.log1p(1 / d) - 1 / (d + 1) for d in distances) / 2
        deficits.append(deficit)
        fluctuation = np.eye(width) - np.ones((width, width)) / width
        block = slice(k * width, (k + 1) * width)
        lower[block, block] += (math.log(1 / (2 * epsilon)) - deficit) * fluctuation
    margin = float(np.linalg.eigvalsh(short - lower)[0])
    assert margin >= -1e-10
    return dict(cells=n, slots=slots, minimum_eigenvalue_difference=margin,
                maximum_deficit=max(deficits), certification=False)


if __name__ == '__main__':
    cases = [(24, [[3, 4], [9, 10], [15, 16]]),
             (48, [[6, 7, 8, 9], [18, 19, 20, 21], [30, 31, 32, 33]]),
             (24, [[0, 1], [2, 3], [4, 5], [22, 23]])]
    print(json.dumps([check(n, slots) for n, slots in cases], indent=2))
