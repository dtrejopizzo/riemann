"""Design110: exact first-mode factorization in the unchanged REST functions.

NO theta, Gauss construction, or certificate is evaluated on import.
Execution is conditional on109 finishing WITHOUT FULLPASS and on independent
approval of this literal.  This module never stops, restarts, or alters109.

The origin is EXACTLY the audited109 proxy of the unchanged107/108 literals.
The REST precision, nodes, errors, domain, traversal and budgets stay unchanged.
Only Theta16(y+v)/Theta16(y) and its logarithmic derivative are factored.
"""

from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
from types import SimpleNamespace
import sys

from flint import arb, arb_series, ctx


EXPECTED = {
    "power_mixed_four_origin_branch_107.py":
        "15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553",
    "power_mixed_four_compact_107_verify.py":
        "2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054",
    "power_mixed_four_polynomial_108_verify.py":
        "eb200a9061a3761d2b1a5dc5ca38def6c5c16e1e0901524c39969555eb791f6a",
    "power_mixed_four_cauchy_109_verify.py":
        "c3fe2df06692622dcaddbb4f2eb21047a7f4be46affdbe151af27f25bbef48ba",
}

PREC, CAP, LOCAL_CAP, MODES = 512, 4, 5, 16
INITIAL_CELLS, MAX_DEPTH, MAX_EVALUATIONS = 508, 10, 8192


def ball(value):
    value = Q(value)
    return arb(value.numerator)/value.denominator


def series(coefficients, cap):
    result = arb_series(coefficients, prec=cap)
    assert result.prec >= cap
    assert all(result[j].is_finite() for j in range(cap))
    return result


def power_two(exponent):
    return arb(2**exponent) if exponent >= 0 else arb(1)/2**(-exponent)


def symmetric_error(radius):
    assert radius.is_finite() and radius >= 0
    return arb(0, radius.upper())


def mode_exponentials(y):
    # m=1 is the factored principal mode, never an omitted mode.
    return tuple((-(m*m-1)*y).exp() for m in range(2, MODES+1))


def correction(y, exponentials, cap):
    """Theta16(y)=(2y-3)*(1+R16(y)), with the exterior m^2 retained."""
    denominator = 2*y-3
    assert denominator[0] > 0
    result = series([arb(0)], cap)
    for m, exponential in zip(range(2, MODES+1), exponentials):
        rate = m*m-1
        coefficient = m**4+3*m*m*rate/denominator
        result += coefficient*exponential
    assert result.prec >= cap
    assert all(result[j].is_finite() for j in range(cap))
    assert 1+result[0] > 0
    return result


def factored_x_column(t_ball, yc, pi):
    """Same p16, from its exact factored temporal derivative; cap5 -> cap4."""
    ctx.cap = LOCAL_CAP
    t = series([t_ball, arb(1)], LOCAL_CAP)
    y = pi*(2*t).exp()
    denominator = 2*y-3
    assert denominator[0] > 0
    exponentials = mode_exponentials(y)
    r16 = correction(y, exponentials, LOCAL_CAP)
    r16_temporal_derivative = series([arb(0)], LOCAL_CAP)
    for m, exponential in zip(range(2, MODES+1), exponentials):
        rate = m*m-1
        coefficient = m**4+3*m*m*rate/denominator
        r16_temporal_derivative -= exponential*(
            2*y*rate*coefficient
            +12*y*m*m*rate/(denominator*denominator))
    # d/dt, NOT d/dy: y'=2y is already present in the explicit formula.
    p16 = (2*y-arb(9)/2-6/denominator
           -r16_temporal_derivative/(1+r16))
    x = (t*p16-1)/yc
    assert x.prec >= CAP
    result = []
    for j in range(CAP):
        # Unchanged full-mode error of the SAME complete local function X/Yc.
        result.append(x[j]+symmetric_error(power_two(-687+5*j)))
    assert all(value.is_finite() for value in result)
    return result


def factored_integrated_columns(t_ball, yc, a, nodes, pi):
    """Same640 Gauss nodes; conserve the explicit common first-mode factor."""
    ctx.cap = CAP
    t = series([t_ball, arb(1)], CAP)
    y = pi*(2*t).exp()
    denominator = 2*y-3
    assert denominator[0] > 0 and y[0] > 0
    exponentials = mode_exponentials(y)
    r16 = correction(y, exponentials, CAP)
    tau = series([arb(0)], CAP)
    kappa = series([arb(0)], CAP)
    yc_squared = yc*yc

    for node in nodes:
        argument = 1+node.v/y
        assert argument[0] > 0
        logarithm = argument.log()
        r = logarithm/2
        shifted_y = y+node.v
        shifted_exponentials = tuple(
            exponential*node.mode_exponentials[m-1]
            for m, exponential in zip(range(2, MODES+1), exponentials))
        shifted_r16 = correction(shifted_y, shifted_exponentials, CAP)
        theta_ratio = ((1+2*node.v/denominator)
                       *(1+shifted_r16)/(1+r16))
        a16 = (node.exp_minus_v/(2*y)
               *(logarithm/4).exp()*theta_ratio)
        tau += node.weight*yc*(t+r)*a16
        kappa += node.weight*yc_squared*(a*r-(t+r)*r*r/2)*a16

    tau_coefficients, kappa_coefficients = [], []
    for j in range(CAP):
        # Exactly the same conservative errors as immutable107, before the
        # determinant and conversion from normalized coefficients to derivatives.
        radius = (power_two(-81+5*j)+power_two(-450+5*j)
                  +power_two(-675+5*j))
        error = symmetric_error(radius)
        tau_coefficients.append(tau[j]+error)
        kappa_coefficients.append(kappa[j]+error)
    assert all(value.is_finite()
               for value in tau_coefficients+kappa_coefficients)
    return kappa_coefficients, tau_coefficients


def evaluate_cell(left, right, a, nodes, pi, common):
    assert Q(1, 2) <= left < right <= 64
    midpoint, halfwidth = (left+right)/2, (right-left)/2
    assert halfwidth <= Q(1, 16)
    t_ball = ball(midpoint)+symmetric_error(ball(halfwidth))
    yc = pi*(2*ball(midpoint)).exp()  # Fixed CENTER scale, not a jet variable.
    assert yc > 0
    x_column = factored_x_column(t_ball, yc, pi)
    kappa, tau = factored_integrated_columns(t_ball, yc, a, nodes, pi)
    rows = [[factorial(j)*column[j] for column in (kappa, tau, x_column)]
            for j in range(1, CAP)]
    # Expansion along the constant third column has positive cofactor sign.
    return common.determinant_three(rows)


def certify_factored_rest(a, common):
    """Identical predeclared subdivision algorithm107, custom exact evaluator."""
    ctx.prec, ctx.cap = PREC, CAP
    assert a.is_finite() and 0 < a < 1
    assert (common.REST_PREC, common.REST_CAP, common.LOCAL_CAP, common.MODES,
            common.GAUSS_N, common.INITIAL_CELLS,
            common.MAX_DEPTH, common.MAX_EVALUATIONS) == (
                PREC, CAP, LOCAL_CAP, MODES, 64, INITIAL_CELLS,
                MAX_DEPTH, MAX_EVALUATIONS)
    pi = arb.pi()
    # This immutable107 helper returns rigorous scalar balls, including all
    # cached exp[-(m^2-1)v]. It performs no theta evaluation or sign probing.
    nodes = common.prepare_gauss_nodes()
    evaluations = accepted = 0

    def visit(left, right, depth):
        nonlocal evaluations, accepted
        if evaluations >= MAX_EVALUATIONS:
            return {"status": "INCONCLUSIVE", "reason": "evaluation budget",
                    "cell": (str(left), str(right)), "depth": depth}
        evaluations += 1
        determinant = evaluate_cell(left, right, a, nodes, pi, common)
        if determinant > 0:
            accepted += 1
            print("REST110 PASS CELL", str(left), str(right),
                  "depth", depth, "evaluation", evaluations,
                  "det", determinant, flush=True)
            return None
        if determinant < 0:
            return {"status": "NEGATIVE", "cell": (str(left), str(right)),
                    "depth": depth, "determinant": determinant}
        if depth >= MAX_DEPTH:
            return {"status": "INCONCLUSIVE", "reason": "depth budget",
                    "cell": (str(left), str(right)), "depth": depth,
                    "determinant": determinant}
        midpoint = (left+right)/2
        failure = visit(left, midpoint, depth+1)
        if failure is not None:
            return failure
        return visit(midpoint, right, depth+1)

    for j in range(INITIAL_CELLS):
        left = Q(1, 2)+Q(j, 8)
        right = left+Q(1, 8)
        failure = visit(left, right, 0)
        if failure is not None:
            failure.update(evaluations=evaluations, accepted=accepted)
            print("REST110", failure, flush=True)
            return failure
    result = {"status": "PASS", "evaluations": evaluations,
              "accepted": accepted, "initial_cells": INITIAL_CELLS}
    print("REST110 FULL PASS", result, flush=True)
    return result


def main():
    # OWNER PRECONDITION:109 has already FINISHED without FULLPASS; independent
    # independent approval is required BEFORE any invocation of this main().
    here = Path(__file__).resolve().parent
    print("DRIVER110 SHA256", sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
    for name, expected in EXPECTED.items():
        actual = sha256((here/name).read_bytes()).hexdigest()
        assert actual == expected, (name, actual, expected)
        print("UNCHANGED MODULE SHA256", name, actual, flush=True)
    import power_mixed_four_origin_branch_107 as origin
    import power_mixed_four_polynomial_108_verify as polynomial
    import power_mixed_four_cauchy_109_verify as cauchy
    import power_mixed_four_compact_107_verify as common
    # Identical proxy and original literals109. No imported module is patched.
    proxy = SimpleNamespace(**{name: getattr(origin, name) for name in (
        "PREC", "CAP", "MODES", "DEGREE", "INITIAL_CELLS", "MAX_DEPTH",
        "MAX_EVALS", "ball", "certified_a")})
    proxy.build_origin_polynomials = lambda a: cauchy.clipped_builder(origin, a)
    try:
        result = polynomial.run_correlated_origin(proxy)
    except ValueError as error:
        print("INCONCLUSIVE110: origin construction error", str(error), flush=True)
        return 2
    if result["status"] != "PASS":
        print("NO FULLPASS110: ORIGIN", result, flush=True)
        return 1 if result["status"] == "NEGATIVE" else 2
    rest = certify_factored_rest(result["a"], common)
    if rest["status"] != "PASS":
        print("NO FULLPASS110: REST", rest, flush=True)
        return 1 if rest["status"] == "NEGATIVE" else 2
    print("FULLPASS110: unchanged109 origin and factored rest", result, rest, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
