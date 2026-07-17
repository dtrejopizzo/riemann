"""
W-LOEWNER: la forma de Weil T=QW^N_lambda tiene (CCM Lemma basicexpli) la forma
   tau_ii = a_i (a_{-j}=a_j),   tau_ij = (b_i-b_j)/(i-j)  (b_{-j}=-b_j).
La parte off-diagonal es una MATRIZ DE LOEWNER de la secuencia b en nodos j.
Teorema de Loewner: Loewner(b) PSD <=> b = valores de una funcion de PICK (Nevanlinna).
=> el muro T>=0 conecta con interpolacion de Nevanlinna-Pick (teoria clasica).

Pasos:
 (1) verificar que A_lambda (engine) TIENE esta forma: extraer b_i = i*tau_{i,0}, a_i=tau_{ii},
     y chequear (b_i-b_j)/(i-j) == tau_ij a maquina.
 (2) separar T = diag(a) + Loewner(b). Firmas de cada parte.
 (3) la pregunta de Pick: ¿Loewner(b) es PSD? ¿el diag(a) lo arregla/rompe? signaturas.
 (4) DH: ¿b_DH NO es Pick (Loewner indefinida con mas neg)?
"""
import sys, numpy as np
from engine_cache import get_matrices


def extract_ab(A, idx):
    dim = len(idx); z = idx.index(0)
    a = np.array([A[i, i] for i in range(dim)])
    # b_i = i * tau_{i,0}  (b_0=0, b_{-j}=-b_j)
    b = np.array([idx[i] * A[i, z] for i in range(dim)])
    return a, b


def run(lam, N, kind='zeta'):
    La, Lp, Amp, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    A = np.array([[float(Amp[i, j]) for j in range(dim)] for i in range(dim)])
    a, b = extract_ab(A, idx)
    # (1) verificar la forma CCM
    maxerr = 0.0
    for i in range(dim):
        for j in range(dim):
            if idx[i] != idx[j]:
                pred = (b[i] - b[j]) / (idx[i] - idx[j])
                maxerr = max(maxerr, abs(pred - A[i, j]))
    # (2) Loewner(b) + diag(a)
    Loe = np.zeros((dim, dim))
    for i in range(dim):
        for j in range(dim):
            if idx[i] != idx[j]:
                Loe[i, j] = (b[i] - b[j]) / (idx[i] - idx[j])
    Dg = np.diag(a)
    evA = np.linalg.eigvalsh(A)
    evL = np.linalg.eigvalsh(Loe)
    evD = np.sort(a)
    sig = lambda ev: (int((ev > 1e-9).sum()), int((abs(ev) <= 1e-9).sum()), int((ev < -1e-9).sum()))
    print(f"\n{kind} lam={lam} N={N} dim={dim}")
    print(f"  (1) forma CCM tau_ij=(b_i-b_j)/(i-j): max err = {maxerr:.2e}  => {'CONFIRMADA' if maxerr<1e-9 else 'NO'}")
    print(f"      b_j (sine-coef EF): {[round(float(x),3) for x in b]}")
    print(f"  (2) firma A=diag(a)+Loewner(b): A={sig(evA)}  Loewner(b)={sig(evL)}  diag(a)={sig(evD)}")
    print(f"      min eig A = {evA.min():+.3e}  (=mu_lambda; >=0 <=> RH a esta lambda)")
    print(f"      min eig Loewner(b) = {evL.min():+.3e}   diag(a) min = {a.min():+.3e}")
    # (3) ¿el diag(a) es el que aporta positividad o la rompe?
    print(f"      a_j (cos-coef EF): {[round(float(x),3) for x in a]}")
    return a, b, evL, evA


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E93 — forma de Loewner/Pick de la forma de Weil")
    for lam, N in grid:
        run(lam, N, 'zeta')
    run(7.0, 14, 'DH')
