"""
W-INDEX: el muro como FLUJO ESPECTRAL (indice topologico) del par casi-conmutante (D,T).
T = diag(a) + Loewner(b), [D,T]=beta∧eta rango 2. Camino T(t)=diag(a)+t·Loewner(b), t:0->1.
  t=0: diag(a), todo >0 (kappa=0).   t=1: T (kappa = #autoval<0 = 2·#ceros off-line = muro).
El flujo espectral = #autovalores que cruzan 0 = kappa. RH <=> kappa=0 <=> ningun cruce.
Pregunta-cruce: ¿hay una BARRERA estructural que impide cruces para zeta (diag(a) domina el
camino Loewner) pero no para DH? Indice = discreto, no balancea a residuo.
Tests:
 (1) kappa(zeta)=0? kappa(DH)>0? via #autoval<0 de T.
 (2) flujo espectral: trayectorias de autovalores vs t; donde cruzan (DH) y si zeta evita 0.
 (3) margen minimo a lo largo del camino: min_t lambda_min(T(t)). Para zeta ¿toca 0 solo en t=1?
     (=marginalidad) y se mantiene >=0; para DH cruza a negativo antes.
 (4) la cota: lambda_min(T(t)) >= min(a) - t·||Loewner(b)||_{a-metric}? estructural?
"""
import sys, numpy as np
from engine_cache import get_matrices


def extract_ab(A, idx):
    dim = len(idx); z = idx.index(0)
    a = np.array([float(A[i, i]) for i in range(dim)])
    b = np.array([idx[i] * float(A[i, z]) for i in range(dim)])
    return a, b


def run(lam, N, kind='zeta'):
    La, Lp, Amp, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    A = np.array([[float(Amp[i, j]) for j in range(dim)] for i in range(dim)])
    a, b = extract_ab(A, idx)
    Loe = np.zeros((dim, dim))
    for i in range(dim):
        for k in range(dim):
            if idx[i] != idx[k]:
                Loe[i, k] = (b[i] - b[k]) / (idx[i] - idx[k])
    Da = np.diag(a)
    # flujo espectral
    ts = np.linspace(0, 1, 41)
    mins = []; negcount = []
    for t in ts:
        ev = np.linalg.eigvalsh(Da + t * Loe)
        mins.append(ev.min()); negcount.append(int((ev < -1e-9).sum()))
    kappa = negcount[-1]
    # primer t donde aparece un autovalor negativo
    tcross = next((ts[i] for i in range(len(ts)) if negcount[i] > 0), None)
    print(f"\n{kind} lam={lam} N={N}: kappa(#autoval<0 de T)={kappa}  (RH<=>0)")
    print(f"  flujo espectral: primer cruce a negativo en t={tcross}  (None=nunca, solo marginal en t=1)")
    print(f"  min_t lambda_min(T(t)): {min(mins):+.4f} en t={ts[int(np.argmin(mins))]:.2f}")
    print(f"  lambda_min en t=1 (muro)= {mins[-1]:+.3e}   min(a)={a.min():+.4f}  ||Loewner||={np.linalg.norm(Loe,2):.3f}")
    # cota estructural: ¿min(a) >= ||Loewner||_{a-metric}? (normalizado)
    Dah = np.diag(1/np.sqrt(np.abs(a)))
    Mnorm = Dah @ Loe @ Dah
    lmin_norm = np.linalg.eigvalsh(Mnorm).min()
    print(f"  Loewner normalizado D_a^-1/2 Loewner D_a^-1/2: lambda_min={lmin_norm:+.3f}  "
          f"(muro <=> >=-1; ={lmin_norm:.3f})")
    return kappa, tcross


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E96 — flujo espectral / indice kappa del par casi-conmutante (D,T)")
    for lam, N in grid:
        run(lam, N, 'zeta')
    run(7.0, 14, 'DH')
