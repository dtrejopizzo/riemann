#!/usr/bin/env python3
"""E.02 verifier — R1: exactitud del paso entre potencias primas consecutivas.

Sea  2=q_1<q_2<... la sucesion de potencias primas y  tau_j = (1/2) log q_j.

Se verifica:
  R1.a  la lista de contactos {n : 2 <= n < e^{2T}} es constante en (tau_j, tau_{j+1}]
  R1.b  el nacimiento es nulo: el contacto entrante q_j tiene shift log q_j = 2 tau_j,
        exactamente el ancho de la ventana vieja, luego <S F, F> = 0 para F sop en I_{tau_j}
  R1.c  el canal Gamma es independiente de la ventana sobre funciones extendidas por cero
  R1.d  CONSECUENCIA: A_{tau_{j+1}} comprimido al old core transportado es EXACTAMENTE
        A_{tau_j}.  El bloque viejo no recibe correccion del contacto recien nacido.
  R1.e  estructura de la corona: A = C^perp dentro de P_{tau_{j+1}} consiste en las
        funciones primitivas soportadas en el anillo MAS a lo sumo 2 direcciones de Tate
        soportadas en el core.
"""
import numpy as np
from sympy import factorint

CHECKS = 0
def check(cond, label):
    global CHECKS
    assert cond, f"FALLO: {label}"
    CHECKS += 1
    print(f"  ok  {label}")


def prime_powers(limit):
    out = []
    for n in range(2, limit + 1):
        if len(factorint(n)) == 1:
            out.append(n)
    return out

QS = prime_powers(60)
print(f"potencias primas: {QS[:14]} ...\n")

# ---------------------------------------------------------------- R1.a
print("R1.a  la lista de contactos es constante en (tau_j, tau_{j+1}]")
ok = True
for j in range(len(QS) - 1):
    qj, qj1 = QS[j], QS[j + 1]
    tj, tj1 = 0.5 * np.log(qj), 0.5 * np.log(qj1)
    base = None
    for frac in [1e-9, 0.01, 0.25, 0.5, 0.75, 1.0]:
        T = tj + frac * (tj1 - tj)
        # comparar en espacio log: n < e^{2T}  <=>  log n < 2T.  Evita que exp() redondee
        # por encima de q_{j+1} justo en el endpoint T = tau_{j+1}.
        contacts = tuple(q for q in QS if np.log(q) < 2 * T)
        if base is None:
            base = contacts
        elif contacts != base:
            ok = False
    # y debe ser exactamente {q_1..q_j}
    if base != tuple(QS[:j + 1]):
        ok = False
check(ok, f"constante e igual a {{q_1..q_j}} en los {len(QS)-1} pasos probados")

# ---------------------------------------------------------------- R1.b
print("R1.b  el nacimiento es nulo (soportes trasladados disjuntos)")
def overlap_measure(T, a):
    """medida de  (-T,T) inter (-T-a, T-a)  = soporte donde <S_a F, F> puede ser != 0."""
    lo, hi = max(-T, -T - a), min(T, T - a)
    return max(0.0, hi - lo)

ok = True
for j in range(len(QS)):
    tj = 0.5 * np.log(QS[j])
    a = np.log(QS[j])                      # shift del contacto entrante = 2 tau_j
    if overlap_measure(tj, a) > 1e-12:
        ok = False
check(ok, "log q_j = 2 tau_j  =>  overlap nulo en el instante del nacimiento")

# y el overlap se abre estrictamente despues
ok = all(overlap_measure(0.5 * np.log(QS[j]) + 1e-3, np.log(QS[j])) > 0
         for j in range(len(QS)))
check(ok, "el overlap se abre estrictamente para T > tau_j")

# verificacion numerica directa del producto interno, no solo de los soportes
def shift_form(T, a, n=800):
    """<S_a F, F> + c.c. para F=indicadora de una subcelda, en la ventana (-T,T)."""
    h = 2 * T / n
    grid = -T + (np.arange(n) + 0.5) * h
    k = a / h
    k0, frac = int(np.floor(k)), k - int(np.floor(k))
    S = np.zeros((n, n))
    for i in range(n):
        for (kk, w) in ((k0, 1 - frac), (k0 + 1, frac)):
            if 0 <= i + kk < n:
                S[i, i + kk] += w
    return (S + S.T) * h

worst = 0.0
for j in range(len(QS)):
    tj = 0.5 * np.log(QS[j])
    M = shift_form(tj, np.log(QS[j]))
    worst = max(worst, np.abs(M).max())
check(worst < 1e-12, f"forma de shift identicamente nula en T=tau_j (max |.| = {worst:.2e})")

# ---------------------------------------------------------------- R1.c
print("R1.c  el canal Gamma no depende de la ventana sobre funciones extendidas por cero")
# <G_{Gamma,T} F, F> = (1/2pi) int g(tau) |FT(Ftilde)(tau)|^2 dtau  -- solo depende de Ftilde.
# Se confirma comparando la forma calculada en dos ventanas distintas para el mismo F.
try:
    from scipy.special import psi as _psi          # vectorizado sobre complejos
    def g_gamma(tau):
        return np.real(_psi(0.25 + 0.5j * np.abs(tau))) - float(_psi(0.25).real)
except ImportError:                                 # fallback lento
    import mpmath as mp
    mp.mp.dps = 25
    _p0 = float(mp.digamma(mp.mpf(1) / 4))
    def g_gamma(tau):
        return np.array([float(mp.re(mp.digamma(mp.mpf(1)/4 + 1j*abs(t)/2))) - _p0
                         for t in np.atleast_1d(tau)])

def gamma_form(F, x, L, nfft=1 << 13):
    """(1/2pi) int g_Gamma(tau) |hat F(tau)|^2 dtau  via FFT sobre [-L,L]."""
    h = x[1] - x[0]
    pad = np.zeros(nfft); pad[:len(F)] = F
    Fh = np.fft.fft(pad) * h
    tau = 2 * np.pi * np.fft.fftfreq(nfft, d=h)
    dtau = abs(tau[1] - tau[0])
    return float((g_gamma(tau) * np.abs(Fh) ** 2).sum() * dtau / (2 * np.pi))

rng = np.random.default_rng(7)
T_small, T_big = 0.5 * np.log(5), 0.5 * np.log(7)
n_small = 600
h = 2 * T_small / n_small
xs = -T_small + (np.arange(n_small) + 0.5) * h
Fvals = rng.standard_normal(n_small)
# misma F, embebida en la ventana chica y en la grande (extension por cero)
n_big = int(np.round(2 * T_big / h))
xb = -T_big + (np.arange(n_big) + 0.5) * h
Fbig = np.zeros(n_big)
i0 = int(np.round((xs[0] - xb[0]) / h))
Fbig[i0:i0 + n_small] = Fvals
v1 = gamma_form(Fvals, xs, T_small)
v2 = gamma_form(Fbig, xb, T_big)
rel = abs(v1 - v2) / max(abs(v1), 1e-30)
check(rel < 1e-10, f"forma Gamma identica en ambas ventanas (dif. relativa {rel:.2e})")

# ---------------------------------------------------------------- R1.d
print("R1.d  CONSECUENCIA: el old core block es exactamente A_{tau_j}")
# A_{T'} - A_T sobre funciones sop. en I_T  =  - sum_{e^{2T} <= n < e^{2T'}} w_n (S+S*)
# El unico n en ese rango con Lambda(n)!=0 es q_j, y su forma es nula por R1.b.
ok = True
for j in range(len(QS) - 1):
    qj, qj1 = QS[j], QS[j + 1]
    extra = [n for n in range(qj, qj1) if len(factorint(n)) == 1]
    if extra != [qj]:
        ok = False
check(ok, "el unico contacto que entra en [q_j, q_{j+1}) es q_j")
check(worst < 1e-12,
      "y su forma se anula sobre el core  =>  A_old = A_{tau_j}  SIN correccion")

# ---------------------------------------------------------------- R1.e
print("R1.e  estructura de la corona A = C^perp dentro de P_{tau_{j+1}}")
def primitive_basis(T, n):
    """base ortonormal de P_T = ker M_- ∩ ker M_+ en la malla de n celdas."""
    h = 2 * T / n
    x = -T + (np.arange(n) + 0.5) * h
    M = np.vstack([np.exp(-x / 2), np.exp(x / 2)]) * h        # los dos funcionales de Tate
    # nucleo de M
    U, s, Vt = np.linalg.svd(M)
    return Vt[2:].T / np.sqrt(h), x, h                        # ortonormal en L^2

for (qj, qj1) in [(4, 5), (5, 7), (7, 8), (8, 9)]:
    tj, tj1 = 0.5 * np.log(qj), 0.5 * np.log(qj1)
    # Elegir la malla para que el core sea un numero ENTERO de celdas de la malla grande:
    # fijar h por el core, y ajustar la ventana externa a n_out*h (difiere de 2*tau_{j+1}
    # en menos de una celda).  Sin esto el nesting solo es exacto a O(h).
    n_in = 700
    h = 2 * tj / n_in
    n_out = int(np.round(2 * tj1 / h))
    if (n_out - n_in) % 2:
        n_out += 1                                             # core centrado
    tj1_grid = n_out * h / 2
    Pbig, xb, hb = primitive_basis(tj1_grid, n_out)
    # old core transportado: primitivas de la ventana chica, extendidas por cero
    Psmall, xs2, hs = primitive_basis(tj, n_in)
    i0 = (n_out - n_in) // 2
    C = np.zeros((n_out, Psmall.shape[1]))
    C[i0:i0 + n_in, :] = Psmall
    # proyectar C sobre P_big (deberia estar ya adentro: nesting)
    coeff = Pbig.T @ C * hb
    resid = np.abs(C - Pbig @ coeff).max()
    # dimension de la corona dentro de P_big
    dimP, dimC = Pbig.shape[1], np.linalg.matrix_rank(coeff, tol=1e-8)
    # funciones primitivas soportadas en el anillo
    ann = np.zeros((n_out, 0))
    mask = np.ones(n_out, bool); mask[i0:i0 + n_in] = False
    Ann = np.eye(n_out)[:, mask]
    Mt = np.vstack([np.exp(-xb / 2), np.exp(xb / 2)]) * hb
    K = Mt @ Ann
    ns = np.linalg.svd(K)[2][2:].T
    dim_ann_prim = ns.shape[1]
    print(f"     q_j={qj}->{qj1}:  dim P={dimP}  dim C={dimC}  dim A={dimP-dimC}"
          f"  dim(anillo∩P)={dim_ann_prim}  extra={dimP-dimC-dim_ann_prim}"
          f"  resid_nesting={resid:.1e}")
    check(resid < 1e-8, f"  q_j={qj}: nesting isometrico, C subset P_{{tau_{{j+1}}}}")
    check(dimP - dimC - dim_ann_prim == 2,
          f"  q_j={qj}: dim A = dim(anillo∩P) + 2  (las dos direcciones de Tate)")

print(f"\nVERDICT: {CHECKS} checks OK — R1 se verifica.")
print("El salto q_j -> q_{j+1} es un paso exacto: el old core block no recibe")
print("correccion del contacto entrante, y la corona = (anillo ∩ P) + 2 modos de Tate.")
