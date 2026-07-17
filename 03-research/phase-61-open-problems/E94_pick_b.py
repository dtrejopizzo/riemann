"""
W-LOEWNER fuerte: el muro <=> D (distribucion EF) positivo-definida.
La matriz de Weil A_{jk}=int q(U_j,U_k) D. Off-diagonal = Loewner(b), b_j=sine-coef de D.
Teorema de Loewner: la matriz de Loewner COMPLETA de b (con diagonal b'(j)) es PSD <=> b es PICK
(operador-monotona, b: H+ -> H+, repr. integral b(x)=a+cx+int(1/(t-x)-t/(1+t^2))dmu, c>=0, mu>=0).

Tests:
 (1) construir Loewner completo de b: L_ij=(b_i-b_j)/(i-j) i!=j, L_ii=b'(i) (deriv simetrica).
     ¿L PSD (b Pick) para zeta? ¿NO para DH? = el muro como propiedad de Pick de b.
 (2) descomponer a_j = b'(j) + c_j, c_j=2 int cos(2pi j y/L) D dy. signo de c_j (extra diagonal).
 (3) A = Loewner_offdiag(b) + diag(a). Comparar autovalores A vs L (Pick).
 (4) la medida de Nevanlinna de b: si b Pick, b(x)=...+int dmu/(t-x); estimar mu>=0?
"""
import sys, numpy as np
from engine_cache import get_matrices


def extract_ab(A, idx):
    dim = len(idx); z = idx.index(0)
    a = np.array([A[i, i] for i in range(dim)])
    b = np.array([idx[i] * A[i, z] for i in range(dim)])
    return a, b


def run(lam, N, kind='zeta'):
    La, Lp, Amp, L, idx = get_matrices(lam, N, kind, dps=40)
    dim = len(idx)
    A = np.array([[float(Amp[i, j]) for j in range(dim)] for i in range(dim)])
    a, b = extract_ab(A, idx)
    js = np.array([float(idx[i]) for i in range(dim)])
    # ordenar por nodo j (idx ya es -N..N creciente)
    order = np.argsort(js); js = js[order]; b = b[order]; a = a[order]
    # b'(j) por diferencia simetrica (extremos: one-sided)
    bp = np.gradient(b, js)
    # (1) Loewner completo de b
    Lo = np.zeros((dim, dim))
    for i in range(dim):
        for k in range(dim):
            Lo[i, k] = (b[i] - b[k]) / (js[i] - js[k]) if i != k else bp[i]
    Lo = (Lo + Lo.T) / 2
    evL = np.linalg.eigvalsh(Lo)
    sig = lambda ev: (int((ev > 1e-9).sum()), int((abs(ev) <= 1e-9).sum()), int((ev < -1e-9).sum()))
    # (2) c_j = a_j - b'(j)
    c = a - bp
    # (3) A signature
    evA = np.linalg.eigvalsh(A)
    print(f"\n{kind} lam={lam} N={N}")
    print(f"  (1) Loewner COMPLETO de b (b'(j) diag): firma={sig(evL)}  min={evL.min():+.3e}  "
          f"=> b {'ES PICK (Loewner PSD)' if evL.min()>-1e-6 else 'NO Pick (neg)'}")
    print(f"  (2) extra-diagonal c_j=a_j-b'(j): min={c.min():+.3f} max={c.max():+.3f}  "
          f"=> {'c>=0' if c.min()>-1e-6 else 'c mixto'}")
    print(f"  (3) A=offdiag-Loewner+diag(a): firma A={sig(evA)} min={evA.min():+.3e}")
    print(f"      b'(j) (diag de Pick): min={bp.min():+.3f} max={bp.max():+.3f}")
    return evL, c, evA


if __name__ == '__main__':
    grid = [(7.0, 14), (11.0, 18), (15.0, 20)]
    if len(sys.argv) > 1:
        grid = eval(sys.argv[1])
    print("E94 — ¿es b una funcion de PICK? (Loewner completo PSD)  zeta vs DH")
    for lam, N in grid:
        run(lam, N, 'zeta')
    run(7.0, 14, 'DH')
