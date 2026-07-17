"""
E20: Mecanismo del cero cuadratico -> escalera (k+1)^2.

Test honesto del problema generalizado QW vs Gram en la ruta E*E:
    forma = int |zeta(1/2+it)|^2 |f_hat(t)|^2 dt
sobre f time-limited a w in [-T,T].

Construyo la COMPRESION  P_T M P_T  directamente (sin asumir condicion de
borde): M = multiplicar por el peso w(t) en frecuencia. La BC la decide la
compresion, no nosotros.

Piezas:
  (A) peso (t-gamma)^2  (cero cuadratico puro)  -> debe dar Laplaciano.
  (B) peso |zeta(1/2+it)|^2 real cerca de un cero gamma (via modulacion).
  (C) comparo el espectro bajo: ratios (k+1)^2 ?  y BC Dirichlet vs Neumann.
"""
import numpy as np
import mpmath as mp

mp.mp.dps = 25

# ---- grilla ----
T   = 1.0           # semiancho time-limited en w
W   = 12.0          # semiancho de la caja grande (padding) -> resolucion en t
N   = 4096          # puntos en [-W,W]
dw  = 2*W/N
w   = (np.arange(N) - N//2) * dw
# frecuencias t conjugadas (rad/s): t = 2pi * freq
t   = 2*np.pi*np.fft.fftfreq(N, d=dw)
t   = np.fft.fftshift(t)

def inside_of(Tval):
    return np.where(np.abs(w) <= Tval + 1e-9)[0]

print(f"W={W} N={N} dw={dw:.4f}  rango t: +-{t.max():.1f}")

def compression_matrix(weight_t, inside):
    """Devuelve la matriz de  P_T M P_T  donde
       M f = IFFT( weight(t) * FFT(f) ).  weight_t: array sobre la grilla t."""
    Wt = np.fft.ifftshift(weight_t)  # a orden FFT
    Nin = len(inside)
    M = np.zeros((Nin, Nin), dtype=complex)
    for j, idx in enumerate(inside):
        e = np.zeros(N, dtype=complex)
        e[idx] = 1.0
        Fe = np.fft.fft(e)
        Me = np.fft.ifft(Wt * Fe)
        M[:, j] = Me[inside]
    # simetrizar (debe ser hermitica)
    M = 0.5*(M + M.conj().T)
    return M

def low_spectrum(M, k=6):
    ev = np.linalg.eigvalsh(M)
    ev = np.sort(ev.real)
    return ev[:k]

def ratios(ev):
    ev = ev.copy()
    base = ev[0]
    r0 = ev/base if abs(base) > 1e-30 else ev*np.nan
    # tambien quitando un posible modo nulo (Neumann)
    if len(ev) > 1 and abs(ev[1]) > 1e-30:
        r1 = ev[1:]/ev[1]
    else:
        r1 = ev[1:]*np.nan
    return r0, r1

# ============ (A) cero cuadratico puro, centrado en t=0 ============
print("\n(A) peso (t)^2  [cero cuadratico puro] -- (n+1)^2 = [1 4 9 16 25 36 49]")
for Tval in (1.0, 2.0):
    ins = inside_of(Tval)
    MA = compression_matrix((t)**2, ins)
    evA = low_spectrum(MA, 7)
    r0A, _ = ratios(evA)
    print(f"   T={Tval}: ratios e_n/e_0 = {np.array2string(r0A, precision=3)}")

# ============ (B) |zeta|^2 real, modulado al primer cero gamma1 ============
gamma1 = 14.134725141734693
print("\n(B) |zeta(1/2+it)|^2 cerca de gamma1=%.4f  (barrido en T)" % gamma1)
zt = np.empty(N)
for i, ti in enumerate(t):
    zt[i] = float(abs(mp.zeta(mp.mpf('0.5') + 1j*(gamma1 + float(ti))))**2)
for Tval in (1.0, 2.0, 3.0, 4.0, 6.0):
    ins = inside_of(Tval)
    MB = compression_matrix(zt, ins)
    evB = low_spectrum(MB, 7)
    r0B, _ = ratios(evB)
    print(f"   T={Tval}: ratios e_n/e_0 = {np.array2string(r0B, precision=3)}")

zp = complex(mp.zeta(mp.mpf('0.5')+1j*gamma1, derivative=1))
print("   |zeta'(gamma1)|^2 =", abs(zp)**2)
print("   objetivo (n+1)^2 = [1 4 9 16 25 36 49]")
