"""R153 certificate core.  Exact reduction of the Xi_a Weil form on I_T=(-T,T).

Symbol identity (proved in R153_003 Lemma C1):
   sum_pm Re psi(1/4 pm a/2 + i tau/2) - 2 log pi
     = sum_{j>=0,pm} 2 tau^2 /( a_j^pm ((a_j^pm)^2 + tau^2) )  -  m0a ,
   a_j^pm = 2j + 1/2 pm a,   m0a = 2 log pi - psi(1/4+a/2) - psi(1/4-a/2).
Each multiplier is the symbol of the NON-NEGATIVE energy
   E_b(F) = int_0^inf e^{-b r} || F - S_r F ||^2 dr = 2 N^2 / b - 2 chat(b),
   chat(b) = int_0^{2T} e^{-b r} c(r) dr,  c(r) = int F(t) F(t+r) dt,  N^2 = c(0).
Hence   q_a(F) = sum_{j,pm} E_{a_j^pm}(F) - m0a N^2 - sum_{n<e^{2T}} 2 c_n n^{-1/2} c(log n),
        c_n = Lambda(n) (n^a + n^{-a}).
"""
import math
from polyalg import pmul, padd, pscal, pder, pint, peval, binom

# ---------- test function family -------------------------------------------
# h_i(t) = (T^2-t^2)^4 t^i  (vanishes to order 4 at +-T, so h in C^3_c)
# F_i    = P(D) h_i,  P(D) = (D^2-p^2)(D^2-q^2), p=1/2+a, q=1/2-a
# => int e^{beta t} F_i = 0 for beta in {+-p,+-q}  EXACTLY.
def build_Fi(T, a, m, ctx):
    p = ctx.mpf(1)/2 + a; q = ctx.mpf(1)/2 - a
    s = p*p + q*q; pr = p*p*q*q
    base = [T*T, ctx.mpf(0), -ctx.mpf(1)]          # T^2 - t^2
    w = [ctx.mpf(1)]
    for _ in range(4): w = pmul(w, base, ctx)      # (T^2-t^2)^4
    out = []
    for i in range(m+1):
        h = [ctx.mpf(0)]*i + w
        d2 = pder(pder(h, ctx), ctx)
        d4 = pder(pder(d2, ctx), ctx)
        F = padd(padd(d4, pscal(d2, -s, ctx), ctx), pscal(h, pr, ctx), ctx)
        out.append(F)
    return out

def corr_matrix(Fs, T, ctx):
    """C[i][k](r) = (1/2)[int F_i(t)F_k(t+r) + int F_k(t)F_i(t+r)] dt, poly in r."""
    n = len(Fs)
    raw = [[None]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            raw[i][k] = _cross(Fs[i], Fs[k], T, ctx)
    C = [[None]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            C[i][k] = pscal(padd(raw[i][k], raw[k][i], ctx), ctx.mpf(1)/2, ctx)
    return C

def _cross(Fi, Fk, T, ctx):
    """int_{-T}^{T-r} Fi(t) Fk(t+r) dt  as a polynomial in r."""
    dk = len(Fk)-1
    # bivariate B[pt][pr] = coeff of t^pt r^pr in Fk(t+r)
    B = [[ctx.mpf(0)]*(dk+1) for _ in range(dk+1)]
    for j in range(dk+1):
        fj = Fk[j]
        if fj == 0: continue
        for pt in range(j+1):
            B[pt][j-pt] = B[pt][j-pt] + fj*binom(j, pt, ctx)
    di = len(Fi)-1
    D = [[ctx.mpf(0)]*(dk+1) for _ in range(dk+di+1)]
    for s in range(di+1):
        fs = Fi[s]
        if fs == 0: continue
        for pt in range(dk+1):
            for pr in range(dk+1):
                if B[pt][pr] != 0:
                    D[pt+s][pr] = D[pt+s][pr] + fs*B[pt][pr]
    # antiderivative in t
    A = [[ctx.mpf(0)]*(dk+1) for _ in range(len(D)+1)]
    for pt in range(len(D)):
        for pr in range(dk+1):
            A[pt+1][pr] = D[pt][pr]/(pt+1)
    # evaluate at t = T-r  and at t = -T
    top = [ctx.mpf(0)]
    powr = [ctx.mpf(1)]                       # (T-r)^pt
    tmr = [T, -ctx.mpf(1)]
    for pt in range(len(A)):
        row = A[pt]
        if any(x != 0 for x in row):
            top = padd(top, pmul(row, powr, ctx), ctx)
        powr = pmul(powr, tmr, ctx)
    bot = [ctx.mpf(0)]
    for pt in range(len(A)):
        row = A[pt]
        if any(x != 0 for x in row):
            bot = padd(bot, pscal(row, (-T)**pt, ctx), ctx)
    return padd(top, pscal(bot, -ctx.mpf(1), ctx), ctx)

# ---------- chat(b) = int_0^L e^{-br} c(r) dr  (c polynomial, L=2T) --------
class Chat:
    """Rigorous evaluator.  Series in b for bL<=SPLIT, asymptotic for bL>SPLIT."""
    SPLIT = 150.0
    def __init__(self, c, L, ctx, is_iv, Mmax=520):
        self.c = c; self.L = L; self.ctx = ctx; self.is_iv = is_iv
        self.I = []                      # I_m = int_0^L r^m c(r) dr
        for m in range(Mmax+1):
            s = ctx.mpf(0)
            for k, ck in enumerate(c):
                s = s + ck*L**(k+m+1)/(k+m+1)
            self.I.append(s)
        self.Mmax = Mmax
        self.maxc = sum(abs(ck)*L**k for k, ck in enumerate(c))
        self.fact = [ctx.mpf(1)]
        for k in range(1, len(c)+2): self.fact.append(self.fact[-1]*k)
    def __call__(self, b):
        ctx = self.ctx; L = self.L
        bl = float(_hi(b*L, ctx))
        if bl <= self.SPLIT:
            s = ctx.mpf(0); term = ctx.mpf(1)   # (-b)^m/m!
            M = self.Mmax
            for m in range(M+1):
                s = s + term*self.I[m]
                term = term*(-b)/(m+1)
            # rigorous tail: |sum_{m>M}| <= maxc*L*sum_{m>M}(bL)^m/m!
            t = ctx.mpf(1)
            for m in range(1, M+2): t = t*(b*L)/m
            geo = ctx.mpf(1)/(1 - min(bl/(M+2), 0.5))
            err = self.maxc*L*abs(t)*geo
            return s + ctx.mpf([-1, 1])*err if self.is_iv else s
        else:
            s = ctx.mpf(0)
            for k, ck in enumerate(self.c):
                s = s + ck*self.fact[k]/b**(k+1)
            err = self.maxc*L*ctx.exp(-b*L/2)*ctx.mpf(2)**(len(self.c)+1)
            return s + ctx.mpf([-1, 1])*err if self.is_iv else s

def _hi(x, ctx):
    try: return x.b
    except AttributeError: return x


# ---------- digamma with a rigorous remainder (real z>0) -------------------
_B2 = [1.0/6, -1.0/30, 1.0/42, -1.0/30, 5.0/66, -691.0/2730, 7.0/6]
from fractions import Fraction as _Fr
_B2F = [_Fr(1,6), _Fr(-1,30), _Fr(1,42), _Fr(-1,30), _Fr(5,66), _Fr(-691,2730), _Fr(7,6)]

def digamma(z, ctx, is_iv, K=40, M=5):
    """psi(z) for real z>0.  Recurrence to z+K, then Stirling/Binet with the
    standard alternating-remainder bound |R_M| <= |B_{2M+2}/((2M+2) w^{2M+2})|."""
    w = z + K
    s = ctx.log(w) - 1/(2*w)
    for n in range(1, M+1):
        Bn = ctx.mpf(_B2F[n-1].numerator)/_B2F[n-1].denominator
        s = s - Bn/(2*n*w**(2*n))
    nB = _B2F[M]; Br = ctx.mpf(nB.numerator)/nB.denominator
    rem = abs(Br)/((2*M+2)*w**(2*M+2))
    if is_iv: s = s + ctx.mpf([-1, 1])*rem
    for k in range(K):
        s = s - 1/(z + k)
    return s
