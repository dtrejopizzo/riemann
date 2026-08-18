#!/usr/bin/env python3
"""Directed geometric-delta cover from the D.65 bridge to T=0.347.

Requires python-flint.  Prints one JSON record per certified leaf.  Every
entry is an Arb ball; midpoint eigenballs are combined with the Frobenius
norm of all entry radii by Weyl's inequality.
"""
import json
import numpy as np
from decimal import Decimal, getcontext
try:
    from flint import arb, arb_mat, ctx
except ImportError as exc:
    raise SystemExit("pip install python-flint") from exc

ctx.prec = 192
ctx.threads = 4
getcontext().prec = 50

A = arb(2).log()
PI = arb.pi()
C_PRIME = A/arb(2).sqrt()
M0 = PI.log()+arb.const_euler()+PI/2+3*A
BVALS = [arb(2*j)+arb("0.5") for j in range(20)]
C19 = sum((2/b for b in BVALS), arb(0))-M0
HTARGET = Decimal("0.002")


def ceil_decimal(x):
    return int(x.to_integral_value(rounding="ROUND_CEILING"))


def build_leaf(dl_s, dr_s, rho=10):
    dl_d, dr_d = Decimal(dl_s), Decimal(dr_s)
    # a > .693 and all leaves end below .001: these integer choices are
    # valid uniformly.  Force an even middle count for equal parity blocks.
    mb = max(1, ceil_decimal(dr_d/HTARGET))
    mm = 348
    n = 2*mb+mm
    assert n % 2 == 0

    delta = arb(str((dl_d+dr_d)/2), str((dr_d-dl_d)/2))
    T = (A+delta)/2
    x0 = -T
    x1 = x0+delta
    x2 = x1+(A-delta)
    x3 = x2+delta
    segments = ((x0, delta, mb), (x1, A-delta, mm), (x2, delta, mb))
    left, right, length = [], [], []
    for lo, total_length, count in segments:
        step = total_length/count
        for k in range(count):
            left.append(lo+k*step)
            right.append(lo+(k+1)*step)
            length.append(step)

    R = [[arb(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        R[i][i] = C19
    for i in range(mb):
        R[i][n-mb+i] -= C_PRIME
        R[n-mb+i][i] -= C_PRIME

    for b in BVALS:
        b2 = b*b
        ep = [(b*left[i]).exp() for i in range(n)]
        em = [(-b*right[i]).exp() for i in range(n)]
        inc = [(b*length[i]).expm1() for i in range(n)]
        for i in range(n):
            ell = length[i]
            # Cancellation-free expansion of
            # 2/b * (1 + expm1(-z)/z), z=b*ell.
            z = b*ell
            term = z/2
            diag_series = term
            for k in range(2, 25):
                term *= -z/(k+1)
                diag_series += term
            rem = 2/b * z.abs_upper()**25/arb.fac_ui(26)
            diag_value = 2/b*diag_series + arb(0, rem)
            R[i][i] -= diag_value
            for j in range(i+1, n):
                value = ep[i]*inc[i]*em[j]*inc[j]/(b2*(length[i]*length[j]).sqrt())
                R[i][j] -= value
                R[j][i] -= value

    mp, mn = [], []
    for i in range(n):
        root = length[i].sqrt()
        mp.append(2*(left[i]/2).exp()*(length[i]/2).expm1()/root)
        mn.append(2*(-right[i]/2).exp()*(length[i]/2).expm1()/root)
    for i in range(n):
        for j in range(i, n):
            v = arb(rho)*(mp[i]*mp[j]+mn[i]*mn[j])
            R[i][j] += v
            if i != j:
                R[j][i] += v

    # Uniform worst-case residual, retained as a ball on the diagonal.
    # On this cover delta < .001 while the middle-cell length is about
    # .693/348; hence the middle length is uniformly the maximum.
    hmax = length[mb]
    I19 = arb(0)
    for bi in BVALS:
        for bj in BVALS:
            I19 += bi*bj*(1-(-2*T*(bi+bj)).exp())/(bi+bj)
    I19 *= 4*T
    epsK = 2*hmax/PI*I19.sqrt()
    epsH = 4*arb(rho)*T.sinh()*hmax/PI
    eps = epsK+epsH
    for i in range(n):
        R[i][i] -= eps

    half = n//2
    blocks = {
        "even": [[R[i][j]+R[i][n-1-j] for j in range(half)] for i in range(half)],
        "odd": [[R[i][j]-R[i][n-1-j] for j in range(half)] for i in range(half)],
    }
    margins = {}
    variations = {}
    for name, entries in blocks.items():
        center = [[x.mid() for x in row] for row in entries]
        for i, row in enumerate(center):
            for j, x in enumerate(row):
                if not x.is_finite():
                    raise ArithmeticError(f"nonfinite center entry {name} {i} {j}: {entries[i][j]}")
        # A floating eigensystem is used only as a rational change of basis.
        # Positivity is then proved by Arb Gershgorin bounds on Q^T A Q.
        approx = np.array([[float(x) for x in row] for row in center])
        _, q = np.linalg.eigh(approx)
        qball = arb_mat([[arb(repr(float(q[i, j]))) for j in range(len(q))]
                         for i in range(len(q))])
        gram_q = qball.transpose()*qball
        qnorm2 = arb(0)
        qinvert_lower = None
        for i in range(len(q)):
            rowsum = arb(0)
            offsum = arb(0)
            for j in range(len(q)):
                rowsum += abs(gram_q[i, j])
                if i != j:
                    offsum += abs(gram_q[i, j])
            if rowsum.upper() > qnorm2.upper():
                qnorm2 = rowsum
            disk_lower = gram_q[i, i]-offsum
            if qinvert_lower is None or disk_lower.lower() < qinvert_lower.lower():
                qinvert_lower = disk_lower
        if not (qinvert_lower > 0):
            raise ArithmeticError(f"rational change of basis not certified invertible: {qinvert_lower}")
        diagonalized = qball.transpose()*arb_mat(center)*qball
        gersh = []
        for i in range(len(q)):
            radius = arb(0)
            for j in range(len(q)):
                if i != j:
                    radius += abs(diagonalized[i, j])
            gersh.append(diagonalized[i, i]-radius)
        # Directed selection: compare certified lower endpoints, never
        # midpoint orderings, even though these balls are extremely narrow.
        least_ball = min(gersh, key=lambda x: x.lower())
        if not (least_ball > 0):
            raise ArithmeticError(f"center Gershgorin failed {dl_s} {dr_s} {name}: {least_ball}")
        # Congruence by a non-exactly-orthogonal rational matrix costs the
        # certified upper bound ||Q||^2.
        least = (least_ball/qnorm2).lower()
        variation_sq = arb(0)
        for row in entries:
            for x in row:
                variation_sq += x.rad()**2
        variation = variation_sq.sqrt()
        margin = arb(least)-variation
        if not (margin > 0):
            raise ArithmeticError(f"FAIL {dl_s} {dr_s} {name}: least={least}, variation={variation}")
        margins[name] = str(margin.lower())
        variations[name] = str(variation.upper())
    return {
        "delta_left": dl_s,
        "delta_right": dr_s,
        "mb": mb,
        "mm": mm,
        "dimension": n,
        "margin_even_lower": margins["even"],
        "margin_odd_lower": margins["odd"],
        "variation_even_upper": variations["even"],
        "variation_odd_upper": variations["odd"],
        "eps_upper": str(eps.upper()),
    }


def initial_leaves(start="0.000037", end="0.0008529"):
    """Geometrically seeded exact-decimal leaves for adaptive refinement."""
    end = Decimal(end)
    d = Decimal(start)
    out = []
    while d < end:
        r = min(2*d, end)
        out.append((str(d), str(r)))
        d = r
    return out


def certify_adaptive(dl, dr, depth=0):
    """Certify a leaf, bisecting it exactly whenever its strict test fails."""
    try:
        rec = build_leaf(dl, dr)
    except ArithmeticError as exc:
        if depth >= 16:
            raise ArithmeticError(
                f"adaptive depth exhausted on [{dl},{dr}]: {exc}"
            ) from exc
        dl_d, dr_d = Decimal(dl), Decimal(dr)
        mid = (dl_d+dr_d)/2
        print(
            "SPLIT",
            json.dumps({"delta_left": dl, "delta_right": dr,
                        "delta_mid": str(mid), "reason": str(exc)},
                       sort_keys=True),
            flush=True,
        )
        return (certify_adaptive(dl, str(mid), depth+1)
                + certify_adaptive(str(mid), dr, depth+1))
    print("LEAF", json.dumps(rec, sort_keys=True), flush=True)
    return [rec]


def run_cover(start, end):
    records = []
    for dl, dr in initial_leaves(start, end):
        records.extend(certify_adaptive(dl, dr))
    assert Decimal(records[0]["delta_left"]) == Decimal(start)
    for x, y in zip(records, records[1:]):
        assert Decimal(x["delta_right"]) == Decimal(y["delta_left"])
    assert Decimal(records[-1]["delta_right"]) == Decimal(end)
    return records


if __name__ == "__main__":
    records = run_cover("0.000037", "0.0008529")
    assert arb("0.0008529")-(arb("0.694")-A) > 0
    print("COVERAGE_PASS", len(records), flush=True)
    print("MANIFEST", json.dumps({
        "schema": "phase114-d66-directed-arb-cover-v1",
        "arb_precision_bits": ctx.prec,
        "delta_bridge_left": "0.000037",
        "delta_overcover_right": "0.0008529",
        "target_relation": "delta=2*T-log(2); 0.0008529 > 0.694-log(2)",
        "leaves": records,
    }, sort_keys=True), flush=True)
