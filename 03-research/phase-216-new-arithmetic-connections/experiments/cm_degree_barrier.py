"""Exact exhaustive checks supplementing Theorem R2-CM; standard library only."""
from fractions import Fraction
from itertools import product
import json

results = []
for m in range(5, 13):
    mean_square = Fraction(0)
    mean_residual = Fraction(0)
    for s in product((-1, 1), repeat=m):
        q = Fraction(sum(all(((-1)**a)*s[(i+j)%m] == 1 for j in range(4))
                         for a in (0, 1) for i in range(m)), 2*m)
        p = Fraction(sum(1 + sum(s[(i+j)%m]*s[(i+k)%m]
                                 for j in range(4) for k in range(j+1, 4))
                         for i in range(m)), 16*m)
        residual = Fraction(sum(s[i]*s[(i+1)%m]*s[(i+2)%m]*s[(i+3)%m]
                                for i in range(m)), 16*m)
        assert q - p == residual
        mean_square += residual * residual
        mean_residual += residual
    mean_square /= 2**m
    assert mean_residual == 0
    assert mean_square == Fraction(1, 256*m)
    results.append({"m": m, "types_checked": 2**m,
                    "residual_squared_L2": str(mean_square),
                    "identity_every_type": True})
print(json.dumps(results, indent=2))
