"""Assemble the Xi_a quadratic form on span{F_0..F_m} (see xiform.py)."""
import math
from polyalg import peval
from xiform import build_Fi, corr_matrix, digamma

SPLIT = 100.0
MMAX  = 400

def blist(a, J, ctx):
    out = []
    for j in range(J+1):
        out.append(ctx.mpf(2*j) + ctx.mpf(1)/2 + a)
        out.append(ctx.mpf(2*j) + ctx.mpf(1)/2 - a)
    return out

def precompute(bs, L, deg, ctx, is_iv):
    ser = [b for b in bs if float(_hi(b))*float(_hi(L)) <= SPLIT]
    asy = [b for b in bs if float(_hi(b))*float(_hi(L)) >  SPLIT]
    S = [ctx.mpf(0)]*(MMAX+1)
    pw = [ctx.mpf(1) for _ in ser]
    for m in range(MMAX+1):
        s = ctx.mpf(0)
        for i in range(len(ser)): s = s + pw[i]
        S[m] = s
        for i, b in enumerate(ser): pw[i] = pw[i]*(-b)
    Z = [ctx.mpf(0)]*(deg+3)
    for s in range(1, deg+3):
        t = ctx.mpf(0)
        for b in asy: t = t + b**(-s)
        Z[s] = t
    inv = ctx.mpf(0)
    for b in bs: inv = inv + 1/b
    # rigorous truncation errors of the two chat representations, per unit maxc*L
    tser = ctx.mpf(0)
    for b in ser:
        t = ctx.mpf(1)
        for mm in range(1, MMAX+2): t = t*(b*L)/mm
        tser = tser + abs(t)*2
    # r^k <= L^k e^{k(r/L-1)}  =>  int_L^inf e^{-br} r^k dr <= L^k e^{-bL}/(b-k/L)
    tasy = ctx.mpf(0)
    for b in asy: tasy = tasy + ctx.exp(-b*L)/(b - deg/L)
    return S, Z, inv, tser + tasy

def _hi(x):
    try: return x.b
    except AttributeError: return x

def matrices(T, a, m, J, ctx, is_iv, verbose=False):
    L = 2*T
    Fs = build_Fi(T, a, m, ctx)
    C = corr_matrix(Fs, T, ctx)
    deg = max(len(C[i][k]) for i in range(m+1) for k in range(m+1)) - 1
    bs = blist(a, J, ctx)
    S, Z, inv, errunit = precompute(bs, L, deg, ctx, is_iv)
    fact = [ctx.mpf(1)]
    for k in range(1, deg+2): fact.append(fact[-1]*k)
    m0a = 2*ctx.log(ctx.pi) - digamma(ctx.mpf(1)/4 + a/2, ctx, is_iv) \
                            - digamma(ctx.mpf(1)/4 - a/2, ctx, is_iv)
    lam = {2: ctx.log(ctx.mpf(2)), 3: ctx.log(ctx.mpf(3))}
    prim = []
    for n in (2, 3):
        if n < math.exp(2*float(_hi(T))) - 1e-12:
            ln_ = ctx.log(ctx.mpf(n))
            cn = lam[n]*(ctx.exp(a*ln_) + ctx.exp(-a*ln_))
            prim.append((ctx.log(ctx.mpf(n)), 2*cn/ctx.sqrt(ctx.mpf(n))))
    Q = [[None]*(m+1) for _ in range(m+1)]
    NM = [[None]*(m+1) for _ in range(m+1)]
    for i in range(m+1):
        for k in range(i, m+1):
            c = C[i][k]
            N = c[0]
            I = []
            for mm in range(MMAX+1):
                s = ctx.mpf(0)
                for kk, ck in enumerate(c): s = s + ck*L**(kk+mm+1)/(kk+mm+1)
                I.append(s)
            cs = ctx.mpf(0); f = ctx.mpf(1)
            for mm in range(MMAX+1):
                cs = cs + S[mm]*I[mm]/f
                f = f*(mm+1)
            ca = ctx.mpf(0)
            for kk, ck in enumerate(c): ca = ca + ck*fact[kk]*Z[kk+1]
            maxc = sum(abs(ck)*L**kk for kk, ck in enumerate(c))
            arch = 2*N*inv - 2*(cs + ca)
            if is_iv: arch = arch + ctx.mpf([-1, 1])*2*maxc*L*errunit
            self_maxc = maxc
            q = arch - m0a*N
            for (ln, wt) in prim: q = q - wt*peval(c, ln, ctx)
            Q[i][k] = Q[k][i] = q
            NM[i][k] = NM[k][i] = N
    return Q, NM, C, Fs, m0a
