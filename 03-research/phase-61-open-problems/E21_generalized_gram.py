"""
E21: problema generalizado  QW_lambda v = rho * G v,  G = Gram E*E = int |zeta|^2 |f_hat|^2.

A = matriz QW del engine (forma de Weil validada, base modos e^{2pi i n u/L} en [0,L]).
G = Gram E*E en LA MISMA base:
    G_{mn} = int |zeta(1/2+it)|^2 * 4 sin^2(tL/2) / [(k_m-t)(k_n-t)] dt,  k_n = 2 pi n / L.

Comparamos:
  - espectro ORDINARIO de A           (ya da (k+1)^2, control)
  - espectro GENERALIZADO (A, G)      (la pregunta de Connes)
Sanidad: con |zeta|^2 -> 1, G debe dar 2*pi*L * I (ortogonalidad en [0,L]).
"""
import numpy as np
import mpmath as mp
from scipy.linalg import eigh

mp.mp.dps = 30
GAMMA = mp.euler; LOG4PI = mp.log(4*mp.pi)

# ---------- engine QW (igual que E11) ----------
def q_func(m, n, L):
    if m == n: return lambda y: 2*(1-y/L)*mp.cos(2*mp.pi*n*y/L)
    c = 1/(mp.pi*(n-m))
    return lambda y: (mp.sin(2*mp.pi*m*y/L)-mp.sin(2*mp.pi*n*y/L))*c

def QW_entry(m, n, L, lam):
    q = q_func(m, n, L); q0 = q(mp.mpf(0))
    W02 = mp.quad(lambda y: q(y)*(mp.e**(y/2)+mp.e**(-y/2)), [0, L])
    def wr(y):
        if y < mp.mpf('1e-12'):
            h = mp.mpf('1e-8'); return ((q(h)-q0)/h+q0/2)/2
        return (mp.e**(y/2)*q(y)-q0)/(2*mp.sinh(y))
    WR = (LOG4PI+GAMMA)*q0/2 + mp.quad(wr, [0, L]) + q0*mp.log(mp.tanh(L/2))/2
    arith = mp.mpf(0); mx = int(lam*lam); sv = [True]*(mx+1)
    for i in range(2, int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i, mx+1, i): sv[j] = False
    for p in range(2, mx+1):
        if sv[p]:
            lp = mp.log(p); pm = p; me = 1
            while pm <= mx:
                arith += lp*(mp.mpf(pm)**mp.mpf('-0.5'))*q(me*lp); pm *= p; me += 1
    return W02 - WR - arith

def build_A(lam, N):
    L = 2*mp.log(lam); dim = 2*N+1; idx = list(range(-N, N+1))
    A = np.zeros((dim, dim))
    for a in range(dim):
        for b in range(a, dim):
            v = float(QW_entry(idx[a], idx[b], L, lam)); A[a, b] = v; A[b, a] = v
    return A, float(L), idx

# ---------- Gram E*E ----------
def build_G(L, idx, zt, tgrid, use_one=False):
    dim = len(idx)
    k = np.array([2*np.pi*n/L for n in idx])
    weight = np.ones_like(tgrid) if use_one else zt
    num0 = 4*np.sin(tgrid*L/2)**2
    G = np.zeros((dim, dim))
    # precompute 1/(k_m - t) con cuidado en nodos (numerador ~ (t-k_m)^2 cancela)
    for a in range(dim):
        da = k[a] - tgrid
        for b in range(a, dim):
            db = k[b] - tgrid
            integ = weight * num0 / (da*db)
            val = np.trapz(integ, tgrid)
            G[a, b] = val; G[b, a] = val
    return G

def low_ratios(ev, kk=8):
    ev = np.sort(ev.real); ev = ev[:kk]
    return ev, ev/ev[0]

# ================= correr =================
lam = mp.mpf('7.0'); N = 8
print(f"lam={lam} N={N} (dim={2*N+1})  construyendo A (engine QW)...", flush=True)
A, L, idx = build_A(lam, N)
print(f"L={L:.4f}", flush=True)

# grilla t y |zeta|^2
Tmax = 110.0; Nt = 9000
tgrid = np.linspace(-Tmax, Tmax, Nt)
# evitar nodos exactos k_n: linspace generico no los toca
print(f"calculando |zeta(1/2+it)|^2 en {Nt} puntos, |t|<={Tmax} ...", flush=True)
zt = np.empty(Nt)
for i, ti in enumerate(tgrid):
    zt[i] = float(abs(mp.zeta(mp.mpf('0.5') + 1j*float(ti)))**2)
print("listo zeta.", flush=True)

# sanidad: G con peso 1 -> 2 pi L I
G1 = build_G(L, idx, zt, tgrid, use_one=True)
diag = np.diag(G1); off = G1 - np.diag(diag)
print(f"\nSANIDAD (peso 1): 2*pi*L = {2*np.pi*L:.4f}")
print(f"  diag(G1) media={diag.mean():.4f} min={diag.min():.4f} max={diag.max():.4f}")
print(f"  |off-diag| max = {np.abs(off).max():.4f}  (debe ser ~0)")

# Gram real
G = build_G(L, idx, zt, tgrid, use_one=False)
# chequear PD
gev = np.linalg.eigvalsh(G)
print(f"\nGram E*E: autovalores min={gev.min():.4e} max={gev.max():.4e} (PD si min>0)")

# espectro ORDINARIO de A (control: debe dar (k+1)^2)
evA = np.linalg.eigvalsh(A)
eA, rA = low_ratios(evA)
print("\nORDINARIO  espec(A):")
print("  eig:", np.array2string(eA, precision=4))
print("  ratios e_k/e_0:", np.array2string(rA, precision=3))

# espectro GENERALIZADO (A, G)
evG = eigh(A, G, eigvals_only=True)
eG, rG = low_ratios(evG)
print("\nGENERALIZADO  A v = rho G v:")
print("  eig:", np.array2string(eG, precision=4))
print("  ratios rho_k/rho_0:", np.array2string(rG, precision=3))
print("\n  objetivo (k+1)^2 =", [(k+1)**2 for k in range(8)])
