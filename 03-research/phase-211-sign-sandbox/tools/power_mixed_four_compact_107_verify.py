"""Round107: fixed RAMA RESTO of the mixed four-density certificate.

This module performs no theta evaluation or quadrature on import.  The origin
branch belongs to power_mixed_four_origin_branch_107.py and must return PASS
before main() can start the remaining interval.  No execution is authorized by
the existence of this file: the design and BOTH literals must first be audited.

REST ownership: invariante_nuevo.  Origin ownership: root.
Design: POWER_MIXED_FOUR_COMPACT_DESIGN_107.md, sections 2, 5--7.
Analytic errors: POWER_MIXED_NORMALIZED_INTEGRAL_106.md, section 8.
"""

from dataclasses import dataclass
from fractions import Fraction as Q
from hashlib import sha256
from itertools import permutations
from math import factorial
from pathlib import Path
import sys

from flint import arb, arb_series, ctx


REST_PREC = 512
REST_CAP = 4
LOCAL_CAP = 5
MODES = 16
GAUSS_N = 64
INITIAL_CELLS = 508
MAX_DEPTH = 10
MAX_EVALUATIONS = 8192
V_ENDPOINTS = (0, 1, 2, 4, 8, 16, 32, 64, 128, 256, 512)


def ball(value):
    """Convert an exact rational to an outward Arb ball."""
    value = Q(value)
    return arb(value.numerator) / value.denominator


def power_two(exponent):
    """Exact powers of two, with outward conversion for negative exponents."""
    if exponent >= 0:
        return arb(2**exponent)
    return arb(1) / 2**(-exponent)


def symmetric_error(radius):
    assert radius.is_finite() and radius >= 0
    return arb(0, radius.upper())


def series(coefficients, cap):
    result = arb_series(coefficients, prec=cap)
    assert result.prec >= cap
    assert all(result[j].is_finite() for j in range(cap))
    return result


@dataclass(frozen=True)
class GaussNode:
    v: object
    weight: object
    exp_minus_v: object
    # Entry m-1 is exp[-(m^2-1)v], rigorously enclosed as a scalar Arb ball.
    mode_exponentials: tuple


def prepare_gauss_nodes():
    """Precache the fixed 640 rigorous nodes and their scalar exponentials.

    Called only by certify_rest(), never on import.  In particular no midpoint
    extraction is used for nodes, weights, exponentials, or transformed nodes.
    """
    ctx.prec = REST_PREC
    roots = tuple(arb.legendre_p_root(GAUSS_N, k, weight=True)
                  for k in range(GAUSS_N))
    assert all(x.is_finite() and w.is_finite() for x, w in roots)
    assert all(-1 < x < 1 and w > 0 for x, w in roots)
    assert sum((w for _, w in roots), arb(0)).contains(arb(2))

    nodes = []
    for left, right in zip(V_ENDPOINTS, V_ENDPOINTS[1:]):
        midpoint = ball(Q(left + right, 2))
        halfwidth = ball(Q(right - left, 2))
        for x, weight in roots:
            v = midpoint + halfwidth*x
            transformed_weight = halfwidth*weight
            assert v > 0 and transformed_weight > 0
            assert v.is_finite() and transformed_weight.is_finite()
            exponentials = tuple((-(m*m - 1)*v).exp()
                                 for m in range(1, MODES + 1))
            assert all(e.is_finite() and e > 0 for e in exponentials)
            nodes.append(GaussNode(
                v=v,
                weight=transformed_weight,
                exp_minus_v=(-v).exp(),
                mode_exponentials=exponentials,
            ))
    assert len(nodes) == 10*GAUSS_N == 640
    return tuple(nodes)


def theta16_parts(y, cap):
    """Theta16 and reusable mode jets at the SAME uncertain temporal input."""
    bases = tuple(m*m * (-(m*m - 1)*y).exp()
                  for m in range(1, MODES + 1))
    theta = series([arb(0)], cap)
    for m, base in enumerate(bases, start=1):
        theta += base*(2*m*m*y - 3)
    assert theta.prec >= cap
    assert all(theta[j].is_finite() for j in range(cap))
    # This is a check on the actual real-interval enclosure, not an assumption
    # of the complex lower bound used in the analytic error proof.
    assert theta[0] > 0
    return theta, bases


def shifted_theta16(y, node, bases, cap):
    """Use exp[-k(y+v)] = exp[-ky] exp[-kv] without scalar rounding away."""
    theta = series([arb(0)], cap)
    shifted_y = y + node.v
    assert shifted_y[0] > 0
    for m, (base, scalar_exp) in enumerate(
            zip(bases, node.mode_exponentials), start=1):
        theta += base*scalar_exp*(2*m*m*shifted_y - 3)
    assert theta.prec >= cap
    assert all(theta[j].is_finite() for j in range(cap))
    return theta


def local_x_column(t_ball, yc, pi):
    """Cap5 is required BEFORE differentiating log Theta16 to cap4."""
    ctx.cap = LOCAL_CAP
    t = series([t_ball, arb(1)], LOCAL_CAP)
    y = pi*(2*t).exp()
    theta, _ = theta16_parts(y, LOCAL_CAP)
    logarithmic_derivative = theta.derivative()/theta
    assert logarithmic_derivative.prec >= REST_CAP
    p16 = 2*y - arb(5)/2 - logarithmic_derivative
    x_column = (t*p16 - 1)/yc
    assert x_column.prec >= REST_CAP
    result = [x_column[j] for j in range(REST_CAP)]
    for j in range(REST_CAP):
        # Full mode tail for X/Yc, BEFORE the determinant and factorials.
        result[j] += symmetric_error(power_two(-687 + 5*j))
    assert all(x.is_finite() for x in result)
    return result


def integrated_columns(t_ball, yc, a, nodes, pi):
    """Direct vector temporal jets for Yc^2*kappa and Yc*tau.

    The interval t_ball covers the ENTIRE temporal cell; its linear series
    coefficient is one.  Series coefficients therefore enclose derivatives
    divided by factorials at every real point of that cell.
    """
    ctx.cap = REST_CAP
    t = series([t_ball, arb(1)], REST_CAP)
    y = pi*(2*t).exp()
    assert y[0] > 0
    theta, bases = theta16_parts(y, REST_CAP)
    tau = series([arb(0)], REST_CAP)
    kappa = series([arb(0)], REST_CAP)
    yc_squared = yc*yc

    for node in nodes:
        ratio_argument = 1 + node.v/y
        assert ratio_argument[0] > 0
        logarithm = ratio_argument.log()
        r = logarithm/2
        theta_shift = shifted_theta16(y, node, bases, REST_CAP)
        # Algebraically identical to106's exp(-v)*(1+v/y)^(5/4)
        # divided by2(y+v).  This form avoids an unnecessary cancellation.
        a16 = (node.exp_minus_v/(2*y)
               * (logarithm/4).exp()*theta_shift/theta)
        tau_integrand = yc*(t+r)*a16
        kappa_integrand = yc_squared*(a*r-(t+r)*r*r/2)*a16
        tau += node.weight*tau_integrand
        kappa += node.weight*kappa_integrand

    tau_coefficients = []
    kappa_coefficients = []
    for j in range(REST_CAP):
        # Conservatively enlarge the analytic Gauss budget106 by a factor4.
        # Scalar Arb node/weight arithmetic is already present in the sums.
        radius = (power_two(-81 + 5*j)
                  + power_two(-450 + 5*j)
                  + power_two(-675 + 5*j))
        error = symmetric_error(radius)
        tau_coefficients.append(tau[j] + error)
        kappa_coefficients.append(kappa[j] + error)
    assert all(x.is_finite() for x in tau_coefficients+kappa_coefficients)
    return kappa_coefficients, tau_coefficients


def determinant_three(rows):
    """Six-term determinant, no division and no assumption on entry signs."""
    result = arb(0)
    for permutation in permutations(range(3)):
        inversions = sum(permutation[i] > permutation[j]
                         for i in range(3) for j in range(i+1, 3))
        term = arb(1)
        for i in range(3):
            term *= rows[i][permutation[i]]
        result += (-1)**inversions * term
    assert result.is_finite()
    return result


def evaluate_rest_cell(left, right, a, nodes, pi):
    """Enclose the normalized Wronskian on one exact rational cell."""
    assert Q(1, 2) <= left < right <= 64
    midpoint = (left+right)/2
    halfwidth = (right-left)/2
    assert halfwidth <= Q(1, 16)
    # Design107 section6 explicitly extends the domains106 to initial halfwidth
    # 1/16: union of Cauchy disks has |z-c|<=3/32 and Yc^2/Y^2<2.
    t_ball = ball(midpoint) + symmetric_error(ball(halfwidth))
    yc = pi*(2*ball(midpoint)).exp()  # CONSTANT with respect to the jet.
    assert yc > 0
    x_column = local_x_column(t_ball, yc, pi)
    kappa, tau = integrated_columns(t_ball, yc, a, nodes, pi)

    # Columns [Yc^2*kappa, Yc*tau, 1, X/Yc].  Expanding along the
    # constant column leaves rows1,2,3 and columns0,1,3 with sign+1.
    rows = [[factorial(j)*column[j] for column in (kappa, tau, x_column)]
            for j in range(1, REST_CAP)]
    return determinant_three(rows)


def certify_rest(a):
    """Run only the fixed RAMA RESTO; do not call before literal approval."""
    ctx.prec = REST_PREC
    ctx.cap = REST_CAP
    assert a.is_finite() and 0 < a < 1
    pi = arb.pi()
    nodes = prepare_gauss_nodes()
    evaluations = 0
    accepted = 0

    def visit(left, right, depth):
        nonlocal evaluations, accepted
        if evaluations >= MAX_EVALUATIONS:
            return {"status": "INCONCLUSIVE", "reason": "evaluation budget",
                    "cell": (str(left), str(right)), "depth": depth}
        evaluations += 1
        determinant = evaluate_rest_cell(left, right, a, nodes, pi)
        if determinant > 0:
            accepted += 1
            print("REST PASS CELL", str(left), str(right),
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
        # Mandatory, predeclared left-first internal subdivision.
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
            print("REST", failure, flush=True)
            return failure
    result = {"status": "PASS", "evaluations": evaluations,
              "accepted": accepted, "initial_cells": INITIAL_CELLS}
    print("REST FULL PASS", result, flush=True)
    return result


def main():
    """FULLPASS is impossible without the separate audited origin branch."""
    origin_path = Path(__file__).with_name("power_mixed_four_origin_branch_107.py")
    print("MAIN SHA256", sha256(Path(__file__).read_bytes()).hexdigest(), flush=True)
    if not origin_path.exists():
        print("INCONCLUSIVE: origin branch is not implemented", flush=True)
        return 2
    print("ORIGIN SHA256", sha256(origin_path.read_bytes()).hexdigest(), flush=True)
    from power_mixed_four_origin_branch_107 import run_origin
    origin = run_origin()
    assert isinstance(origin, dict) and "status" in origin
    if origin["status"] != "PASS":
        print("NO FULLPASS: ORIGIN", origin, flush=True)
        return 1 if origin["status"] == "NEGATIVE" else 2
    assert "a" in origin
    rest = certify_rest(origin["a"])
    if rest["status"] != "PASS":
        print("NO FULLPASS: REST", rest, flush=True)
        return 1 if rest["status"] == "NEGATIVE" else 2
    print("FULLPASS107: origin and rest", origin, rest, flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
