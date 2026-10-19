"""
GUE is not 'the answer': it is a universality CLASS, not an operator.

Three independent GUE matrices are generated. All three have the SAME statistics
(those of the zeros), but their eigenvalues are ALL DIFFERENT from each other and
from the zeros. 'GUE' names a distribution with infinitely many members;
the zeros are ONE deterministic member, selected by the arithmetic (the primes).

'Tuning the mechanism' to pass from the GUE class to the exact member means
injecting the primes, i.e. building the arithmetic operator. It is not a knob;
it is the whole mountain.
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
N = 10

def gue_spectrum(seed, N):
    rng = np.random.default_rng(seed)
    M = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N)))/math.sqrt(2)
    M = (M + M.conj().T)/2
    ev = np.sort(np.linalg.eigvalsh(M))
    return (ev - ev.min())/(ev.max()-ev.min())*(g[N-1]-g[0]) + g[0]

print("Riemann zeros (fixed, deterministic):")
print("  ", np.round(g[:N], 3), "\n")

for s in [1, 2, 3]:
    ev = gue_spectrum(s, N)
    print(f"GUE draw #{s} (same statistics, same range):")
    print("  ", np.round(ev, 3))
print()
print("The 3 GUE draws: identical statistics, ALL eigenvalues different.")
print("None reproduces the zeros. GUE = distribution, not operator.")
print()
print("What SELECTS the correct member of the class = the primes.")
print("That selector is the missing arithmetic operator. That is where the WHOLE problem lies.")
