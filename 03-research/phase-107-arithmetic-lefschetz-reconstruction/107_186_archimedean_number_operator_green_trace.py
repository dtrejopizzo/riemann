#!/home/trabajo/miniforge3/bin/python
"""Direct spectral-sum falsifier for the archimedean Green trace."""

import math

import numpy as np
from mpmath import mp


mp.dps = 60
cutoffs = [100, 1000, 10000, 1000000]
a_values = [1.0, 1.25, 1.0 + 1.5j, 1.5 - 1.0j]

spectral_sum_ok = True
max_final_error = 0.0
for a in a_values:
    target = complex(-mp.digamma(a))
    errors = []
    for cutoff in cutoffs:
        spectrum = np.arange(cutoff + 1, dtype=float)
        finite_part = np.sum(1 / (spectrum + a)) - math.log(cutoff)
        errors.append(abs(finite_part - target))
    decreasing = all(errors[j + 1] < errors[j] for j in range(len(errors) - 1))
    final_ok = errors[-1] < 3e-6
    spectral_sum_ok = spectral_sum_ok and decreasing and final_ok
    max_final_error = max(max_final_error, errors[-1])
    print(
        f"A={a}_ERRORS=" + ",".join(f"{error:.8g}" for error in errors)
        + f"_OK={'YES' if decreasing and final_ok else 'NO'}"
    )


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


completed_checks_ok = True
completed_errors = []
for s in [mp.mpf("2"), mp.mpf("2.5"), mp.mpc(2, 3)]:
    finite = -mp.diff(mp.zeta, s) / mp.zeta(s)
    gamma_green = -mp.digamma(s / 2) / 2 + mp.log(mp.pi) / 2
    poles = -1 / s - 1 / (s - 1)
    assembled = finite + gamma_green + poles
    target = -mp.diff(xi, s) / xi(s)
    error = abs(assembled - target)
    completed_errors.append(error)
    completed_checks_ok = completed_checks_ok and error < mp.mpf("1e-50")

verdict = spectral_sum_ok and completed_checks_ok

print(f"DIRECT_SPECTRAL_CUTOFF_MAX: {cutoffs[-1]}")
print(f"MAX_FINAL_REGULARIZATION_ERROR: {max_final_error:.12g}")
print(f"REGULARIZED_RESOLVENT_EQUALS_MINUS_DIGAMMA: {'YES' if spectral_sum_ok else 'NO'}")
print(f"MAX_COMPLETED_ASSEMBLY_ERROR: {mp.nstr(max(completed_errors), 12)}")
print(f"COMPLETED_GREEN_ASSEMBLY: {'YES' if completed_checks_ok else 'NO'}")
print("ARCHIMEDEAN_GREEN_TRACE: CONSTRUCTED")
print("GLOBAL_ARAKELOV_GREEN_CURRENT: NOT_CONSTRUCTED")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
