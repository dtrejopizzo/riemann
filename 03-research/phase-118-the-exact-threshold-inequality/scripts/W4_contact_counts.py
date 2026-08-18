"""W4 -- number of active prime-power contacts at the certified endpoint and
at the next few prime-power thresholds (SPEC.md Rules: every reported number
must come from a script left in scripts/).

An n contributes a term w_n(S_{log n}+S_{-log n}) to A_T iff n < e^{2T}
(strict; rowd_assembly.assemble uses the same strict cutoff with a 1e-13
tolerance).  This just counts prime powers below e^{2T} at each threshold,
using rowd_assembly's own prime_powers_upto.

Command:
  cd .../phase-118-the-exact-threshold-inequality/scripts
  python3 W4_contact_counts.py
"""
import math
import rowd_assembly as RA

thresholds = [
    (math.log(2), "log2 (certified endpoint)"),
    (0.5 * math.log(5), "(1/2)log5 (next threshold)"),
    (0.5 * math.log(7), "(1/2)log7"),
    (0.5 * math.log(8), "(1/2)log8"),
    (0.5 * math.log(9), "(1/2)log9"),
    (0.5 * math.log(11), "(1/2)log11"),
]

for T, label in thresholds:
    N = int(math.floor(math.exp(2 * T)))
    pp = [n for n in RA.prime_powers_upto(max(N, 2))
          if n < math.exp(2 * T) - 1e-13]
    print(f"{label:28s} T={T:.5f}  e^2T={math.exp(2*T):.4f}  "
          f"active contacts={pp}  count={len(pp)}")
