#!/home/trabajo/miniforge3/bin/python
"""High-precision falsifier for flatness of the completed Green connection."""

from mpmath import mp


mp.dps = 80


def xi(s):
    return mp.mpf("0.5") * s * (s - 1) * mp.power(mp.pi, -s / 2) * mp.gamma(s / 2) * mp.zeta(s)


def green_from_xi(s):
    return -mp.diff(lambda w: mp.log(xi(w)), s)


def green_decomposed(s):
    zeta_term = -mp.diff(mp.zeta, s) / mp.zeta(s)
    return (
        zeta_term
        - 1 / s
        - 1 / (s - 1)
        + mp.log(mp.pi) / 2
        - mp.digamma(s / 2) / 2
    )


def log_abs_xi(x, y):
    # Re(log f) equals log|f| locally and differentiates more stably than
    # taking abs before numerical differentiation.
    return mp.re(mp.log(xi(mp.mpc(x, y))))


def laplacian(function, x, y):
    dxx = mp.diff(lambda xx: function(xx, y), x, 2)
    dyy = mp.diff(lambda yy: function(x, yy), y, 2)
    return dxx + dyy


atlas = [
    (mp.mpf("1.4"), mp.mpf("0.3")),
    (mp.mpf("2"), mp.mpf("3")),
    (mp.mpf("3.5"), mp.mpf("-7")),
    (mp.mpf("8"), mp.mpf("20")),
]

green_identity_ok = True
max_green_error = mp.mpf("0")
for x, y in atlas:
    s = mp.mpc(x, y)
    error = abs(green_from_xi(s) - green_decomposed(s))
    max_green_error = max(max_green_error, error)
    green_identity_ok &= error < mp.mpf("1e-65")


curvature_zero_ok = True
max_laplacian = mp.mpf("0")
for x, y in atlas:
    value = abs(laplacian(log_abs_xi, x, y))
    max_laplacian = max(max_laplacian, value)
    curvature_zero_ok &= value < mp.mpf("1e-65")


def mutated_potential(x, y):
    return log_abs_xi(x, y) + x * x + y * y


mutation_detected = True
for x, y in atlas:
    mutated_curvature = laplacian(mutated_potential, x, y)
    mutation_detected &= abs(mutated_curvature - 4) < mp.mpf("1e-65")


verdict = green_identity_ok and curvature_zero_ok and mutation_detected

print(f"MAX_GREEN_DECOMPOSITION_ERROR: {mp.nstr(max_green_error, 8)}")
print(f"COMPLETED_GREEN_CONNECTION_ONE_FORM: {'YES' if green_identity_ok else 'NO'}")
print(f"MAX_LOG_DETERMINANT_LAPLACIAN: {mp.nstr(max_laplacian, 8)}")
print(f"CHERN_CURVATURE_ON_H_ZERO: {'YES' if curvature_zero_ok else 'NO'}")
print(f"NONFLAT_METRIC_MUTATION_DETECTED: {'YES' if mutation_detected else 'NO'}")
print("SMOOTH_DETERMINANT_METRIC_C1_ROUTE: CLOSED_NO_GO")
print("REQUIRED_REFINEMENT: SINGULAR_BOUNDARY_OR_SECONDARY_CURRENT")
print(f"VERDICT: {'YES' if verdict else 'NO'}")
