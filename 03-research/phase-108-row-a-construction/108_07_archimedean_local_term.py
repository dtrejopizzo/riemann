#!/usr/bin/env python3
"""
108_07 verifier: the archimedean local term of T_S on the graded family.

W_inf(f_a) = PV int_{R^x} |u|^a/|1-u| d*u ,  d*u = du/|u|.

Checks, plain python3 + numpy only (no scipy, no mpmath):

 1. Theorem 2.2 (Beta half):  int_0^inf v^{a-1}/(1+v) dv = pi/sin(pi a)
    against symmetric-midpoint quadrature, cross-validated at two
    independent (T,n) configurations.
 2. Theorem 3.1 (cotangent half, PV):
    PV int_0^inf u^{a-1}/(1-u) du = pi*cot(pi a)
    against symmetric-midpoint quadrature (which realises the PV directly,
    since grid points never land on the pole and symmetric pairs cancel
    its leading term).
 3. Theorem 4.1: the sum equals pi*cot(pi a / 2), and the elementary
    identity cot(x)+csc(x)=cot(x/2).
 4. Theorem 5.1: the convergence region is exactly 0 < Re a < 1. The two
    endpoint tail integrals (near u=0 and u=infinity) are elementary
    exponential integrals; their closed forms are cross-checked against
    the same quadrature engine, and then used (exactly, not by noisy
    fitting) to exhibit the growth rate of the divergent tails, which is
    compared to the theoretical rate Re(a) resp. Re(a)-1.
 5. Corollary 6.1: value pi at a=1/2, and regularity (no blow-up) there.
"""

import cmath
import math
import numpy as np


# ----------------------------------------------------------------------
# 1-2. Quadrature of the two halves via symmetric midpoint rule
# ----------------------------------------------------------------------

def beta_half(a, T=100.0, n=40000):
    """int_0^inf v^{a-1}/(1+v) dv via v=e^t, midpoint rule on t in (-T,T)."""
    h = 2.0 * T / n
    k = np.arange(n) - n / 2.0 + 0.5
    t = k * h
    et = np.exp(t)
    g = np.exp(t * a) / (1.0 + et)
    return np.sum(g) * h


def cot_half_pv(a, T=100.0, n=40000):
    """PV int_0^inf u^{a-1}/(1-u) du via u=e^t, symmetric midpoint rule.

    Grid points sit at t=(k+0.5)h, k=-n/2,...,n/2-1, so t=0 (the pole u=1)
    is never sampled and symmetric pairs +-t cancel the leading -1/t part
    of the pole exactly, term by term.
    """
    h = 2.0 * T / n
    k = np.arange(n) - n / 2.0 + 0.5
    t = k * h
    denom = -np.expm1(t)  # = 1 - e^t, accurate near t=0
    g = np.exp(t * a) / denom
    return np.sum(g) * h


def cot(z):
    return cmath.cos(z) / cmath.sin(z)


def W_inf_closed(a):
    return cmath.pi * cot(cmath.pi * a / 2.0)


def beta_closed(a):
    return cmath.pi / cmath.sin(cmath.pi * a)


def cot_closed(a):
    return cmath.pi * cot(cmath.pi * a)


# ----------------------------------------------------------------------
# main checks
# ----------------------------------------------------------------------

def check_closed_forms():
    print("=== Theorem 2.2, 3.1, 4.1: closed forms vs quadrature ===")
    grades = [0.3, 0.5, 0.7, 0.3 + 0.2j, 0.6 - 0.15j, 0.45 + 0.35j]
    configs = [(100.0, 20000), (150.0, 60000)]  # two independent setups
    ok = True
    for a in grades:
        results = []
        for T, n in configs:
            b = beta_half(a, T, n)
            c = cot_half_pv(a, T, n)
            results.append((b, c))

        bc = beta_closed(a)
        cc = cot_closed(a)
        wc = W_inf_closed(a)

        # beta half: relative error against a nonzero closed form (never
        # vanishes for 0<Re a<1)
        err_b = [abs(b - bc) / abs(bc) for b, c in results]

        # cotangent half: cc can vanish (at a=1/2), so use an absolute
        # error scaled by a fixed reference (pi), not a relative one
        err_c = [abs(c - cc) / math.pi for b, c in results]

        # combined value: W_inf_closed is nonzero throughout the open
        # strip (Corollary 6.1), so relative error is safe here
        err_combined = [abs(b + c - wc) / abs(wc) for b, c in results]

        # cross-validation: the two independent (T,n) configurations
        # must agree with each other
        cross = abs((results[0][0] + results[0][1]) - (results[1][0] + results[1][1])) / abs(wc)

        good = (max(err_b) < 1e-8 and max(err_c) < 1e-8
                and max(err_combined) < 1e-8 and cross < 1e-8)
        ok = ok and good
        print(f"  a={a}: beta err={max(err_b):.2e} | cot err(abs/pi)={max(err_c):.2e}"
              f" | combined err={max(err_combined):.2e} | cross-config diff={cross:.2e}"
              f"  {'OK' if good else 'FAIL'}")
    return ok


def check_trig_identity():
    print("=== Theorem 4.1: elementary identity cot(x)+csc(x)=cot(x/2) ===")
    ok = True
    for x in [0.3, 1.1, 2.0, 0.7 + 0.4j, 1.5 - 0.2j]:
        lhs = cot(x) + 1.0 / cmath.sin(x)
        rhs = cot(x / 2.0)
        err = abs(lhs - rhs) / abs(rhs)
        good = err < 1e-12
        ok = ok and good
        print(f"  x={x}: err={err:.2e}  {'OK' if good else 'FAIL'}")
    return ok


def zero_tail_closed(rea, U):
    """int_0^U e^{-u*rea} du = int_delta^1 t^{rea-1} dt with delta=e^{-U}."""
    if abs(rea) < 1e-13:
        return U
    return (1.0 - math.exp(-U * rea)) / rea


def zero_tail_quad(rea, U, n=40000):
    u = np.linspace(0.0, U, n)
    return np.trapz(np.exp(-u * rea), u)


def inf_tail_closed(rea, U):
    """int_0^U e^{u*(rea-1)} du = int_1^T t^{rea-2} dt with T=e^U."""
    if abs(rea - 1.0) < 1e-13:
        return U
    return (math.exp(U * (rea - 1.0)) - 1.0) / (rea - 1.0)


def inf_tail_quad(rea, U, n=40000):
    u = np.linspace(0.0, U, n)
    return np.trapz(np.exp(u * (rea - 1.0)), u)


def check_convergence_region():
    print("=== Theorem 5.1: convergence region is exactly 0 < Re a < 1 ===")
    ok = True

    print("  --- near u=0: integrand ~ |u|^{a-1}, converges iff Re a > 0 ---")
    for rea in [0.7, 0.3, -0.2, -0.5]:
        # (i) quadrature engine vs closed form, at a moderate U
        Uq = 8.0
        q = zero_tail_quad(rea, Uq)
        c = zero_tail_closed(rea, Uq)
        quad_err = abs(q - c) / max(abs(c), 1.0)

        if rea > 0:
            # convergent: closed form -> 1/rea as U -> infinity; check
            # directly at large U (residual e^{-U*rea} is then negligible)
            U = 100.0
            val = zero_tail_closed(rea, U)
            plateau = 1.0 / rea
            err = abs(val - plateau) / abs(plateau)
            good = err < 1e-10 and quad_err < 1e-6
            print(f"  Re a={rea:+.2f} (inside): tail(U=60)={val:.10f} vs 1/Re a={plateau:.10f},"
                  f" err={err:.2e}; quadrature-vs-closed at U={Uq}: {quad_err:.2e}"
                  f"  {'OK' if good else 'FAIL'}")
        else:
            # divergent: exact growth rate from the closed form at two
            # large, well-separated U (no fitting noise: the additive
            # constant is astronomically negligible there)
            U1, U2 = 100.0, 200.0
            v1, v2 = zero_tail_closed(rea, U1), zero_tail_closed(rea, U2)
            rate = (math.log(v2) - math.log(v1)) / (U2 - U1)
            good = abs(rate - abs(rea)) < 1e-9 and quad_err < 1e-6
            print(f"  Re a={rea:+.2f} (outside): exact growth rate={rate:.10f} vs |Re a|={abs(rea):.10f};"
                  f" quadrature-vs-closed at U={Uq}: {quad_err:.2e}  {'OK' if good else 'FAIL'}")
        ok = ok and good

    print("  --- near u=infinity: integrand ~ |u|^{a-2}, converges iff Re a < 1 ---")
    for rea in [0.3, 0.7, 1.2, 1.5]:
        Uq = 8.0
        q = inf_tail_quad(rea, Uq)
        c = inf_tail_closed(rea, Uq)
        quad_err = abs(q - c) / max(abs(c), 1.0)

        if rea < 1:
            U = 100.0
            val = inf_tail_closed(rea, U)
            plateau = 1.0 / (1.0 - rea)
            err = abs(val - plateau) / abs(plateau)
            good = err < 1e-10 and quad_err < 1e-6
            print(f"  Re a={rea:+.2f} (inside): tail(U=60)={val:.10f} vs 1/(1-Re a)={plateau:.10f},"
                  f" err={err:.2e}; quadrature-vs-closed at U={Uq}: {quad_err:.2e}"
                  f"  {'OK' if good else 'FAIL'}")
        else:
            U1, U2 = 100.0, 200.0
            v1, v2 = inf_tail_closed(rea, U1), inf_tail_closed(rea, U2)
            rate = (math.log(v2) - math.log(v1)) / (U2 - U1)
            good = abs(rate - (rea - 1.0)) < 1e-9 and quad_err < 1e-6
            print(f"  Re a={rea:+.2f} (outside): exact growth rate={rate:.10f} vs Re a-1={rea-1.0:.10f};"
                  f" quadrature-vs-closed at U={Uq}: {quad_err:.2e}  {'OK' if good else 'FAIL'}")
        ok = ok and good

    return ok


def check_regularity_at_half():
    print("=== Corollary 6.1: value pi at a=1/2, regular (no blow-up) ===")
    val = W_inf_closed(0.5)
    err = abs(val - math.pi) / math.pi
    good = err < 1e-14
    print(f"  W_inf(f_{{1/2}}) = {val.real:.12f} (+ {val.imag:.2e}i), pi = {math.pi:.12f},"
          f" err={err:.2e}  {'OK' if good else 'FAIL'}")

    # regularity: closed form is continuous at a=1/2 (no pole there: the
    # nearest poles of cot(pi a/2) are at a=0 and a=2), so the deviation
    # from pi should shrink monotonically to 0 as eps -> 0 from both sides
    eps = [0.1, 0.01, 0.001, 0.0001, 0.00001]
    dev_plus = [abs(W_inf_closed(0.5 + e) - math.pi) for e in eps]
    dev_minus = [abs(W_inf_closed(0.5 - e) - math.pi) for e in eps]
    monotone_plus = all(dev_plus[i + 1] < dev_plus[i] for i in range(len(eps) - 1))
    monotone_minus = all(dev_minus[i + 1] < dev_minus[i] for i in range(len(eps) - 1))
    vanish = dev_plus[-1] < 1e-3 and dev_minus[-1] < 1e-3
    good2 = monotone_plus and monotone_minus and vanish
    print(f"  |W_inf(f_{{1/2+-eps}})-pi| decreases monotonically to 0 as eps->0"
          f" (last: +{dev_plus[-1]:.2e}, -{dev_minus[-1]:.2e}):"
          f"  {'OK' if good2 else 'FAIL'}")
    return good and good2


def main():
    r1 = check_closed_forms()
    r2 = check_trig_identity()
    r3 = check_convergence_region()
    r4 = check_regularity_at_half()

    all_ok = r1 and r2 and r3 and r4
    print()
    if all_ok:
        print("VERDICT: PASS - archimedean local term W_inf(f_a) = pi*cot(pi a/2) "
              "confirmed on 0<Re a<1, convergence strip matches, regular at a=1/2.")
    else:
        print("VERDICT: FAIL - see failed checks above.")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
