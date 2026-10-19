"""
Why 'building the operator' is the whole difficulty, shown with two operators.

(A) The VACUOUS Hilbert-Polya operator:  H = diag(gamma_1, ..., gamma_N).
    It is self-adjoint and its eigenvalues ARE the zeros... but it was built
    FROM the zeros. It proves nothing; it is circular. Hilbert-Polya asks for
    the opposite: derive the zeros from an independent structure.

(B) A random GUE matrix, unfolded to the density N(T).
    Its eigenvalues have the SAME statistics as the zeros (repulsion,
    rigidity, ramp+plateau) but they ARE NOT the zeros. Statistics do
    NOT determine the operator: infinitely many matrices share the phenomenology.

Moral: exactness => circular;  statistics => non-unique.
The only valid path (derive the EXACT gamma from the arithmetic and prove
self-adjointness) is the open problem.
"""
import math
import numpy as np

g = np.loadtxt("zeros_10000.txt")
N = 12

# ---------- (A) vacuous operator diag(gamma) ----------
H_A = np.diag(g[:N])
autov_A = np.linalg.eigvalsh(H_A)
print("(A) H = diag(gamma):  self-adjoint, eigenvalues = EXACT zeros")
print("    eigenvalues:", np.round(autov_A, 4))
print("    actual zeros:", np.round(g[:N], 4))
print("    -> perfect match BECAUSE it was built from the zeros. CIRCULAR.\n")

# ---------- (B) GUE matrix with the same density ----------
rng = np.random.default_rng(1)
M = (rng.standard_normal((N, N)) + 1j*rng.standard_normal((N, N))) / math.sqrt(2)
M = (M + M.conj().T) / 2          # Hermitian matrix (GUE)
ev = np.sort(np.linalg.eigvalsh(M))
# rescale to the window of the first N zeros (same mean density)
ev_scaled = (ev - ev.min())/(ev.max()-ev.min())*(g[N-1]-g[0]) + g[0]
print("(B) rescaled GUE matrix:  self-adjoint, correct statistics")
print("    eigenvalues:", np.round(ev_scaled, 4))
print("    actual zeros:", np.round(g[:N], 4))
print("    -> SAME statistics, DIFFERENT eigenvalues. Statistics are not enough.\n")

print("CONCLUSION:")
print("  exactness without circularity + proved self-adjointness: open.")
