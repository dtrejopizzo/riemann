"""
SURF-B step 1: is the real-structure constraint (T2) a sign handle, or vacuous? (Phase 17)

Constraint (T2): the operator T (spectrum = zeros) must intertwine the real structure
    j(s) = 1 - conj(s)   [anti-holomorphic reflection, Fix(j) = critical line].

There are TWO readings, and the distinction decides everything:
  (T2-weak)   j permutes the spectrum as a SET.            <- always true (quartet symmetry)
  (T2-strong) j FIXES each eigenvalue pointwise            <- spectrum in Fix(j) = all on-line = RH

This script shows (T2-weak) holds UNCONDITIONALLY -- even for an RH-violating off-line
spectrum -- so it gives NO information about the sign / about whether zeros are on the line.
The content (RH) is entirely in the pointwise (T2-strong) statement, which is the missing
positivity (CAP), not something the real structure supplies.
"""
import numpy as np

j = lambda s: 1 - np.conjugate(s)        # anti-holomorphic real structure; Fix(j)={Re s=1/2}

def is_setwise_invariant(spec, tol=1e-9):
    """does j permute the spectrum as a set?"""
    img = j(np.asarray(spec))
    pool = list(spec)
    for x in img:
        for i, y in enumerate(pool):
            if abs(x - y) < tol:
                del pool[i]; break
        else:
            return False
    return len(pool) == 0

def num_fixed_pointwise(spec, tol=1e-9):
    """how many eigenvalues lie ON Fix(j) (j(s)=s, i.e. Re s = 1/2)?"""
    return int(np.sum(np.abs(j(np.asarray(spec)) - np.asarray(spec)) < tol))

print("="*72)
print("(T2-weak vs T2-strong)  Does the real structure j detect off-line zeros?")
print("="*72)

g = 14.13
specs = {
    "RH-true  (all on-line)        ": [0.5+1j*g, 0.5-1j*g, 0.5+1j*21.0, 0.5-1j*21.0],
    "RH-FALSE (off-line quartet)   ": [0.5+0.18+1j*g, 0.5-0.18+1j*g,
                                       0.5+0.18-1j*g, 0.5-0.18-1j*g],
    "RH-FALSE (mixed on+off)       ": [0.5+1j*g, 0.5-1j*g,
                                       0.5+0.30+1j*21.0, 0.5-0.30+1j*21.0,
                                       0.5+0.30-1j*21.0, 0.5-0.30-1j*21.0],
}
for name, spec in specs.items():
    setwise = is_setwise_invariant(spec)
    nfix = num_fixed_pointwise(spec)
    n = len(spec)
    print(f"  {name}: j permutes spectrum (T2-weak)? {setwise!s:5} | "
          f"on Fix(j) pointwise: {nfix}/{n}  -> {'all on-line (RH)' if nfix==n else 'OFF-LINE present'}")

print("\n  -> T2-weak (j permutes the spectrum) is TRUE even for RH-FALSE spectra:")
print("     the real structure is satisfied by off-line zeros just as well as on-line ones.")
print("     It is the unconditional quartet symmetry; it carries NO sign information.")
print("  -> T2-strong (j fixes every eigenvalue) <=> spectrum in Fix(j) <=> all zeros on-line <=> RH.")
print("     That is the missing positivity (CAP), NOT something the real structure provides.")

# The thing that DOES detect off-line zeros is the Pontryagin index kappa (P25/P26),
# i.e. the negative index of the bilinear form -- unchanged by adding the real structure.
print("\n" + "="*72)
print("What actually detects off-line zeros: the negative index kappa (bilinear form), not j")
print("="*72)
WIDTHS = np.array([0.35, 0.6, 1.0, 1.7, 2.8, 4.5])
def neg_index(spec):
    # bilinear Weil-Gram over the test basis; kappa = number of negative directions
    def w(s):
        b = np.real(s) - 0.5; gam = np.imag(s)
        return np.exp(1j*gam*b/(2*WIDTHS))
    # group conjugate-symmetric points; build the full bilinear Gram
    M = np.zeros((len(WIDTHS),)*2)
    for s in spec:
        ws = w(s); M = M + np.real(np.outer(ws, ws))
    ev = np.linalg.eigvalsh((M+M.T)/2); sc = max(np.abs(ev).max(), 1e-300)
    return int((ev < -1e-8*sc).sum())
for name, spec in specs.items():
    print(f"  {name}: kappa (neg index) = {neg_index(spec)}   "
          f"({'0 = RH-consistent' if neg_index(spec)==0 else '>0 = off-line detected'})")

print("\n" + "="*72)
print("VERDICT (SURF-B, on T2): the real-structure constraint is a SYMMETRY, not a")
print("positivity. j permutes the spectrum unconditionally (T2-weak, vacuous for the sign);")
print("forcing j to fix the spectrum pointwise (T2-strong) IS RH = the standing CAP. The real")
print("structure adds NO new handle on the sign. Off-line detection lives entirely in kappa.")
print("=> SURF-B's leverage is NOT T2; it is the inverse spectral problem (T1)+(T3): build the")
print("   canonical-system / de Branges operator whose spectrum is {gamma}. Its positivity = CAP.")
print("="*72)
