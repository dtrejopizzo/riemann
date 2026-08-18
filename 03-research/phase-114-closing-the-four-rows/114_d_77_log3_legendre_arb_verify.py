#!/usr/bin/env python3
"""Directed endpoint certificate at T=log(3)/2.

The first 80 Gamma resolvents are compressed to cellwise Legendre degree 9.
Diagonal-cell resolvents are retained exactly.  Off-cell and high-space
errors are controlled analytically; the infinite tail is handled by D.76.
Requires python-flint and numpy.
"""
from fractions import Fraction
import math
import numpy as np

try:
    from flint import arb, arb_mat, ctx
except ImportError as exc:
    raise SystemExit("Install python-flint or expose it through PYTHONPATH") from exc

ctx.prec = 512
ctx.threads = 4

DEG = 9
D = DEG + 1
DEPTH = 80
RHO = arb(1000)
T = arb(3).log()/2
A = arb(2).log()
C_PRIME = A/arb(2).sqrt()
PI = arb.pi()
M0 = PI.log()+arb.const_euler()+PI/2+3*A
MB, MM = 28, 20
NC = 2*MB+MM
HALF_CELLS = NC//2
DIM_HALF = HALF_CELLS*D
BVALS = [arb(2*j)+arb("0.5") for j in range(DEPTH)]


def add_poly(a, b):
    out = [Fraction(0)]*max(len(a), len(b))
    for i, x in enumerate(a): out[i] += x
    for i, x in enumerate(b): out[i] += x
    return out


def scale_shift(a, scale, shift=0):
    return [Fraction(0)]*shift+[scale*x for x in a]


# Rational Legendre coefficients, followed by orthonormal Arb scaling.
pleg = [[Fraction(1)], [Fraction(0), Fraction(1)]]
for n in range(1, DEG):
    num = add_poly(scale_shift(pleg[n], Fraction(2*n+1), 1),
                   scale_shift(pleg[n-1], Fraction(-n)))
    pleg.append([x/Fraction(n+1) for x in num])
LCOEFF = []
for k, p in enumerate(pleg[:D]):
    norm = (arb(2*k+1)/2).sqrt()
    LCOEFF.append([norm*arb(x.numerator)/x.denominator for x in p])


def derivative(p, order):
    q = list(p)
    for _ in range(order):
        q = [arb(i)*q[i] for i in range(1, len(q))]
        if not q: return [arb(0)]
    return q


def poly_inner(p, q):
    s = arb(0)
    for i, x in enumerate(p):
        for j, y in enumerate(q):
            if (i+j) % 2 == 0:
                s += x*y*2/(i+j+1)
    return s


def poly_endpoint(p, sign):
    return sum((x*(sign**i) for i, x in enumerate(p)), arb(0))


def exp_moments(z, count=D):
    ez, emz = z.exp(), (-z).exp()
    out = [(ez-emz)/z]
    for m in range(1, count):
        boundary = (ez-((-1)**m)*emz)/z
        out.append(boundary-arb(m)/z*out[-1])
    return out


def feature(z, h):
    moments = exp_moments(z)
    fac = (h/2).sqrt()
    return [fac*sum((c*moments[i] for i, c in enumerate(p)), arb(0))
            for p in LCOEFF]


def exp_inner(rate, h):
    if rate == 0:
        return h
    return 2*(rate*h/2).sinh()/rate


def robin_local_gap(b, h):
    """Lower bound 2/b-lambda_max(K_b) by directed bisection."""
    lo, hi = arb(0), PI/2
    target = b*h/2
    for _ in range(180):
        mid = (lo+hi)/2
        val = mid*mid.tan()-target
        if val < 0: lo = mid
        else: hi = mid
    # x is in [lo,hi]; lambda increases when x decreases.
    mu = 2*lo/h
    lam_upper = 2*b/(b*b+mu*mu)
    return 2/b-lam_upper


def cell_package(h):
    """Projected local block, exponential features, local cross bound."""
    plus, minus = [], []
    local = [[arb(0) for _ in range(D)] for _ in range(D)]
    for i in range(D): local[i][i] = sum((2/b for b in BVALS), arb(0))-M0
    residual_rows = []
    for b in BVALS:
        z = b*h/2
        fp, fm = feature(z, h), feature(-z, h)
        plus.append(fp); minus.append(fm)

        # Physical derivative matrices in the orthonormal Legendre basis.
        deriv_mats = {}
        for order in range(0, DEG+1):
            factor = (2/h)**order
            deriv_mats[order] = [[factor*poly_inner(LCOEFF[i], derivative(LCOEFF[j], order))
                                  for j in range(D)] for i in range(D)]
        vcoef = [[arb(0) for _ in range(D)] for _ in range(D)]
        for i in range(D):
            for j in range(D):
                for m in range(DEG//2+1):
                    order = 2*m
                    if order <= DEG:
                        vcoef[i][j] += (2/b)*deriv_mats[order][i][j]/(b**order)

        scale0 = (2/h).sqrt()
        basis_left = [scale0*poly_endpoint(p, -1) for p in LCOEFF]
        basis_right = [scale0*poly_endpoint(p, 1) for p in LCOEFF]
        basis_d_left = [scale0*(2/h)*poly_endpoint(derivative(p, 1), -1) for p in LCOEFF]
        basis_d_right = [scale0*(2/h)*poly_endpoint(derivative(p, 1), 1) for p in LCOEFF]
        arow, brow = [], []
        for j in range(D):
            vl = sum((vcoef[i][j]*basis_left[i] for i in range(D)), arb(0))
            vr = sum((vcoef[i][j]*basis_right[i] for i in range(D)), arb(0))
            vpl = sum((vcoef[i][j]*basis_d_left[i] for i in range(D)), arb(0))
            vpr = sum((vcoef[i][j]*basis_d_right[i] for i in range(D)), arb(0))
            brow.append((-z).exp()*(vpl-b*vl)/(2*b))
            arow.append(-(-z).exp()*(vpr+b*vr)/(2*b))
        residual_rows.extend([(b, 1, fp, arow), (b, -1, fm, brow)])
        kblock = [[vcoef[i][j]+fp[i]*arow[j]+fm[i]*brow[j]
                   for j in range(D)] for i in range(D)]
        for i in range(D):
            for j in range(D):
                kij = (kblock[i][j]+kblock[j][i])/2
                local[i][j] -= kij

    # Exact finite Gram of Q K_local P; trace bounds its operator norm^2.
    nr = len(residual_rows)
    gram = [[arb(0) for _ in range(nr)] for _ in range(nr)]
    for i, (bi, si, fi, _) in enumerate(residual_rows):
        for j in range(i, nr):
            bj, sj, fj, _ = residual_rows[j]
            gij = exp_inner(si*bi+sj*bj, h)-sum((fi[k]*fj[k] for k in range(D)), arb(0))
            gram[i][j] = gram[j][i] = gij
    cmat = arb_mat([row[3] for row in residual_rows])
    resid = cmat.transpose()*arb_mat(gram)*cmat
    trace = sum((resid[i, i] for i in range(D)), arb(0))
    if not (trace > 0):
        raise ArithmeticError(f"local residual trace not resolved at h={h}: {trace}")
    return {"h": h, "plus": plus, "minus": minus,
            "local": local, "beta_local_sq": trace}


delta = 2*T-A
h_boundary = delta/MB
h_middle = (A-delta)/MM
packages = {"b": cell_package(h_boundary), "m": cell_package(h_middle)}
print("PASS local packages resolved at 512 bits", flush=True)
# The cancellation-sensitive local Gram has now been enclosed.  Subsequent
# matrix assembly has wide safety margins and is faster at this still
# rigorous precision.
ctx.prec = 224
types = ["b"]*MB+["m"]*MM+["b"]*MB
left = []
x = -T
for typ in types:
    left.append(x)
    x += packages[typ]["h"]
mid = [left[i]+packages[types[i]]["h"]/2 for i in range(NC)]

# Full projected lower-block matrix.
DIM = NC*D
mat = [[arb(0) for _ in range(DIM)] for _ in range(DIM)]
for ci, typ in enumerate(types):
    block = packages[typ]["local"]
    for k in range(D):
        for l in range(D): mat[ci*D+k][ci*D+l] += block[k][l]
for jb, b in enumerate(BVALS):
    for i in range(NC):
        fp = packages[types[i]]["plus"][jb]
        for j in range(i+1, NC):
            fm = packages[types[j]]["minus"][jb]
            decay = (-b*(mid[j]-mid[i])).exp()
            for k in range(D):
                for l in range(D):
                    value = decay*fp[k]*fm[l]
                    mat[i*D+k][j*D+l] -= value
                    mat[j*D+l][i*D+k] -= value
for i in range(MB):
    j = MB+MM+i
    for k in range(D):
        mat[i*D+k][j*D+k] -= C_PRIME
        mat[j*D+k][i*D+k] -= C_PRIME

# Exact rank-two moment penalty.
moments = []
for sig in (arb("0.5"), arb("-0.5")):
    v = []
    for i, typ in enumerate(types):
        v.extend([((sig*mid[i]).exp())*x for x in feature(sig*packages[typ]["h"]/2,
                                                          packages[typ]["h"])])
    moments.append(v)
for i in range(DIM):
    for j in range(i, DIM):
        value = RHO*sum((v[i]*v[j] for v in moments), arb(0))
        mat[i][j] += value
        if i != j: mat[j][i] += value


def parity_block(sign):
    out = [[arb(0) for _ in range(DIM_HALF)] for _ in range(DIM_HALF)]
    for ci in range(HALF_CELLS):
        for k in range(D):
            row = ci*D+k
            for cj in range(HALF_CELLS):
                rj = NC-1-cj
                for l in range(D):
                    col = cj*D+l
                    out[row][col] = mat[row][col]+sign*((-1)**l)*mat[row][rj*D+l]
    return out


projected_lower = {}
for name, sign in (("even", 1), ("odd", -1)):
    print(f"CERTIFY projected {name} block dim={DIM_HALF}", flush=True)
    block = parity_block(sign)
    shift = arb("0.00050")
    for i in range(DIM_HALF): block[i][i] += shift
    center = [[x.mid() for x in row] for row in block]
    # A floating Cholesky is only a preconditioner.  Its explicitly lower
    # triangular inverse S is a rational (binary-float) invertible matrix;
    # positivity is proved by Arb Gershgorin on S A S^T.
    approx = np.array([[float(x) for x in row] for row in center])
    chol = np.linalg.cholesky(approx)
    sinv = np.linalg.inv(chol)
    sinv[np.triu_indices(DIM_HALF, 1)] = 0.0
    assert np.all(np.diag(sinv) != 0.0)
    sball = arb_mat([[arb(repr(float(sinv[i, j]))) for j in range(DIM_HALF)]
                     for i in range(DIM_HALF)])
    preconditioned = sball*arb_mat(block)*sball.transpose()
    disks = []
    for i in range(DIM_HALF):
        radius = sum((abs(preconditioned[i, j]) for j in range(DIM_HALF) if i != j), arb(0))
        disks.append(preconditioned[i, i]-radius)
    least = min(disks, key=lambda z: z.lower())
    assert least > 0
    projected_lower[name] = -shift
    print(f"PASS projected {name}: lambda_min > -0.00050; preconditioned disk={least}")

# Cross/high residuals for off-cell kernels.
r = DEG+1
hmax = max(h_boundary, h_middle)
Ix = arb(0); Ixy = arb(0)
rect_cache = {}
for bi in BVALS:
    for bj in BVALS:
        s = bi+bj
        key = int(float(s))
        if key not in rect_cache:
            rect = arb(0)
            for i in range(NC-1):
                hi = packages[types[i]]["h"]
                for j in range(i+1, NC):
                    hj = packages[types[j]]["h"]
                    gap = left[j]-(left[i]+hi)
                    rect += (-s*gap).exp()*(-(-s*hi).expm1())*(-(-s*hj).expm1())/(s*s)
            rect_cache[key] = 2*rect
        rect = rect_cache[key]
        Ix += (bi**r)*(bj**r)*rect
        Ixy += (bi**(2*r))*(bj**(2*r))*rect
taylor = hmax**r/arb.fac_ui(r)
beta_cross = taylor*Ix.sqrt()
qq_cross = taylor*taylor*Ixy.sqrt()
beta_local = max((packages[x]["beta_local_sq"].sqrt() for x in packages),
                 key=lambda z: z.upper())
beta_h = RHO*taylor*(arb("0.5")**r)*4*T.sinh()
beta = beta_cross+beta_local+beta_h
dmin = sum((robin_local_gap(b, hmax) for b in BVALS), arb(0))
alpha = dmin-M0-C_PRIME-qq_cross
assert alpha > 0
schur_loss = beta*beta/alpha
assert schur_loss < arb("0.00001")
print(f"PASS high block alpha={alpha}")
print(f"PASS beta_cross={beta_cross}, beta_local={beta_local}, beta_H={beta_h}")
print(f"PASS Schur loss={schur_loss} < 1e-5")

# D.76 tail: directed Robin roots, with deliberately coarse target bounds.
B = arb(2*DEPTH)+arb("0.5")
def bisect_root(kind, lo_s, hi_s):
    lo, hi = arb(lo_s), arb(hi_s)
    def fun(x):
        if kind == "even": return x*x.tan()-B*T
        return x/x.tan()+B*T
    if kind == "even": assert fun(lo) < 0 < fun(hi)
    else: assert fun(lo) > 0 > fun(hi)
    for _ in range(180):
        x = (lo+hi)/2
        val = fun(x)
        if kind == "even":
            if val < 0: lo = x
            else: hi = x
        else:
            if val > 0: lo = x
            else: hi = x
    return lo, hi

x0 = bisect_root("even", "1.55", "1.5707")
x1 = bisect_root("even", "4.65", "4.67")
xo = bisect_root("odd", "3.10", "3.12")
def lam_from_x(interval, use_lo):
    x = interval[0] if use_lo else interval[1]
    mu = x/T
    return 2*B/(B*B+mu*mu)
lam0_upper = lam_from_x(x0, True)
lam0_lower = lam_from_x(x0, False)
lam1_upper = lam_from_x(x1, True)
lam1_lower = lam_from_x(x1, False)
lamo_upper = lam_from_x(xo, True)
root_center = ((x0[0]+x0[1])/2).str(80, radius=False, more=True)
x0_ball = arb(f"{root_center} +/- 1e-40")
assert x0_ball.contains(x0[0]) and x0_ball.contains(x0[1])
mu0 = x0_ball/T
norm_cos = T+(2*mu0*T).sin()/(2*mu0)
inner = 2*(arb("0.5")*(T/2).sinh()*(mu0*T).cos()
           +mu0*(T/2).cosh()*(mu0*T).sin())/(mu0*mu0+arb("0.25"))
norm_h = T+T.sinh()
r2_lower = (inner*inner/(norm_cos*norm_h)).lower()
# d_e = 2/B-lambda_0+(lambda_0-lambda_1)r^2.  Every
# occurrence is chosen at the adverse directed endpoint.
d_even = 2/B-lam0_upper+(lam0_lower-lam1_upper)*r2_lower
d_odd = 2/B-lamo_upper
tail_even = B/4*d_even
tail_odd = B/4*d_odd
assert tail_even > arb("0.00110")
assert tail_odd > arb("0.00060")
final_even = tail_even-arb("0.00050")-schur_loss
final_odd = tail_odd-arb("0.00050")-schur_loss
assert final_even > arb("0.00059")
assert final_odd > arb("0.00009")
print(f"PASS tail even={tail_even}, tail odd={tail_odd}")
print(f"PASS primitive endpoint margins: even={final_even}, odd={final_odd}")
print("PASS T=log(3)/2 primitive endpoint certificate")
