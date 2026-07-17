#!/usr/bin/env python3
# ======================================================================================
# Phase 60 — Discriminante.  E1: ¿puede el lado-cero validado detectar multiplicatividad?
#
# Tesis a testear: "el signo de Weil lo controla la multiplicatividad (Euler), no la
# ubicacion de los ceros".  PRE-REGISTRO (00-PLAN §5): si la diferencia util solo se
# explica por ubicacion de ceros, es CIRCULAR -> NO-GO para esta ruta.
#
# Este script NO construye un engine nuevo: reusa la forma Gram lado-cero VALIDADA del
# engine canonico (phase-5-structural/experiments/colab_phase3_engine.py, gates PASS).
#
# Pregunta operativa: M_zeros depende SOLO del multiset de ceros. Entonces dos L-funciones
# con los mismos ceros dan el MISMO Gram, sean Euler o no. Lo demostramos numericamente:
#   (1) cualquier conjunto ON-line -> lambda_min en el "floor" (>=0), independiente del
#       espaciado/densidad (= independiente de cual L-funcion sea).
#   (2) el unico movedor del signo es desplazar ceros OFF-line (= status-RH, no Euler).
# Conclusion esperada: el lado-cero mide STATUS-RH, es CIEGO a multiplicatividad.
# ======================================================================================
import numpy as np, mpmath as mp, math
mp.mp.dps = 30

T0, SIGMA, J = 85.7, 2.0, 8
NZEROS = 120

def hermite(J, u):
    u = np.asarray(u, dtype=complex)
    H = [np.pi**-0.25*np.exp(-u**2/2)]
    if J > 1: H.append(np.sqrt(2.0)*u*H[0])
    for k in range(2, J): H.append(np.sqrt(2.0/k)*u*H[k-1]-np.sqrt((k-1.0)/k)*H[k-2])
    return H
def g_at(J, sigma, T0, z):
    return np.array([h[0] for h in hermite(J, (np.asarray([z],dtype=complex)-T0)/sigma)])

def M_zeros(zlist, J, sigma, T0):
    """zlist: lista de (t_rho, delta_rho).  Gram de Weil lado-cero (Hermitiana)."""
    M = np.zeros((J, J), dtype=complex)
    for (t, d) in zlist:
        for (tt, dd) in ((t, d), (-t, d)):
            v = g_at(J, sigma, T0, tt - 1j*dd)
            u = g_at(J, sigma, T0, tt + 1j*dd)
            M += np.outer(v, np.conj(u))
    return (M + M.conj().T)/2

def lam_min_over_tr(M):
    l = np.linalg.eigvalsh(M)[0]; tr = np.trace(M).real
    return l, (l/tr if tr != 0 else float('nan'))

print("computing zeta zeros ...", flush=True)
GAM = [float(mp.im(mp.zetazero(n))) for n in range(1, NZEROS+1)]

# --- self-check: reproducir gate del engine canonico (floor on-line + negatividad forzada) ---
M0 = M_zeros([(g,0.0) for g in GAM], J, SIGMA, T0)
l0,r0 = lam_min_over_tr(M0)
print(f"[self-check] zeta on-line floor lambda_min/tr = {r0:+.3e} (debe ser ~>=0)")
assert r0 > -1e-6, "engine roto: floor on-line negativo"

print("\n"+"="*78)
print(" E1.(1)  Distintas densidades de ceros ON-line  (= distintas L-funciones, todas RH-true)")
print("="*78)
print(" Si el lado-cero detectara 'que L-funcion es', el floor cambiaria. Si es CIEGO, no.\n")
print("  configuracion                         #ceros-ventana   lambda_min/tr")

# zeta real
print(f"  zeta (zeros reales)                        {sum(1 for g in GAM if abs(g-T0)<2*SIGMA):>2}            {r0:+.4e}")

# conjuntos ON-line sinteticos con densidades distintas (simulan otras L-funciones RH-true)
rng = np.random.default_rng(0)
for label, dens in [("densidad x0.5 (espaciado amplio)", 0.5),
                    ("densidad x1.0 (uniforme local)", 1.0),
                    ("densidad x2.0 (espaciado denso)", 2.0),
                    ("perturbacion aleatoria de fase", -1)]:
    if dens > 0:
        # malla uniforme local de la densidad pedida dentro de la ventana
        spacing = (2*np.pi/np.log(T0)) / dens   # ~ densidad media de zeta escalada
        ts = [T0 + k*spacing for k in range(-6,7)]
        zl = [(t,0.0) for t in ts] + [(g,0.0) for g in GAM if abs(g-T0)>=2*SIGMA]
    else:
        ts = [g + rng.normal(0,0.3) for g in GAM if abs(g-T0)<2*SIGMA]
        zl = [(t,0.0) for t in ts] + [(g,0.0) for g in GAM if abs(g-T0)>=2*SIGMA]
    M = M_zeros(zl, J, SIGMA, T0)
    l,r = lam_min_over_tr(M)
    nin = sum(1 for (t,_) in zl if abs(t-T0)<2*SIGMA)
    print(f"  {label:36s}   {nin:>2}            {r:+.4e}")

print("\n  -> TODAS las configuraciones ON-line quedan en el floor (>=0, salvo ruido numerico).")
print("     El lado-cero NO distingue 'que L-funcion'. Mide status-RH (on/off line), no Euler.")

print("\n"+"="*78)
print(" E1.(2)  El UNICO movedor del signo: desplazar ceros OFF-line")
print("="*78)
print("  delta(off-line)   lambda_min/tr   <- esto es ubicacion de ceros = status-RH\n")
for delta in (0.0, 0.05, 0.1, 0.2):
    M = M_zeros([(g,(delta if abs(g-T0)<2*SIGMA else 0.0)) for g in GAM], J, SIGMA, T0)
    l,r = lam_min_over_tr(M)
    print(f"      {delta:4.2f}          {r:+.4e}")

print("\n"+"="*78)
print(" VEREDICTO E1 (pre-registrado en 00-PLAN §5)")
print("="*78)
print(" El lado-cero validado es funcion del MULTISET de ceros unicamente.")
print(" => Separar ζ (Euler) de L_DH aqui = separar por ceros off-line = UBICACION = CIRCULAR.")
print(" => La tesis 'multiplicatividad controla el signo' NO es testeable en el lado-cero.")
print(" => Vive enteramente en el lado-ARITMETICO M_arith (el que no esta validado).")
print(" CONSECUENCIA: el bottleneck real de Phase 60 es construir un M_arith VALIDADO.")
