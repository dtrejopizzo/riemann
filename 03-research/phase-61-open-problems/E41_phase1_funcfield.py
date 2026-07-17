"""
FASE 1: detector funcion-campo (ground truth: Weil probo positividad via Hodge).
Curva C/F_q genero g, Frobenius alpha_j=sqrt(q) e^{i theta_j} (|alpha|=sqrt q = RH-FF).
Forma de Weil A_{nm}=sum_{j=1}^{2g} alpha_j^{(n-m)}/q^{(n-m)/2} = Toeplitz t_{|n-m|},
  t_k = 2 sum_{j=1}^g cos(k theta_j)  (t_0=2g),
y t_k = (q^k+1-N_k)/q^{k/2} con N_k=#C(F_{q^k}) (conteo de puntos = divisores efectivos).
Positividad A>=0 <=> Herglotz (t_k momentos de medida positiva en el circulo) <=> RH-FF (Weil).
Sub-tarea: Cholesky A=B^*B; estructura de B. Y caso RH-FALSO (|alpha|!=sqrt q): rompe PSD.
"""
import numpy as np
np.set_printoptions(precision=4, suppress=True, linewidth=120)

def toeplitz_from_angles(thetas, radii, q, L):
    # eigenvalues: para cada (theta,radio r): alpha=r*sqrt(q) e^{i theta} y conjugado.
    # t_k = sum_j (alpha_j^k + conj)/q^{k/2}  (normalizado por q^{k/2})
    g=len(thetas); dim=L+1
    def tk(k):
        if k==0: return 2.0*g  # 2g eigenvalues, normalizados a modulo r; t_0=sum 1 = 2g si r=1
        s=0.0
        for th,r in zip(thetas,radii):
            # alpha=r sqrt(q) e^{i th}; alpha^k/q^{k/2}=r^k e^{i k th}; +conjugado
            s+= 2*(r**k)*np.cos(k*th)
        return s
    A=np.array([[tk(abs(n-m)) for m in range(dim)] for n in range(dim)])
    return A, [tk(k) for k in range(dim)]

def report(name, A):
    ev=np.linalg.eigvalsh(A)
    neg=np.sum(ev<-1e-10)
    print(f"  {name}: dim={A.shape[0]}  eig[min,max]=[{ev.min():.4f},{ev.max():.4f}]  #neg={neg}  {'PSD (Weil ok)' if neg==0 else 'NO PSD (RH-FF violado)'}")
    return ev,neg

# --- curva concreta genero 2, q=2, angulos de Frobenius reales (RH-FF) ---
q=2; g=2; L=8
thetas=[2*np.pi/5, 2*np.pi/7]   # dos angulos (genero 2): 4 eigenvalues +-theta_j
radii_RH=[1.0,1.0]              # |alpha|=sqrt(q) <=> r=1 (RH-FF)
print(f"Curva C/F_{q} genero {g}, angulos Frobenius theta={[round(t,3) for t in thetas]}, ventana L={L}\n")

print("(1) RH-FF (|alpha|=sqrt q): la forma de Weil DEBE ser PSD (Weil/Hodge index):")
A_RH,tks=toeplitz_from_angles(thetas,radii_RH,q,L)
report("A_RH", A_RH)
print(f"     t_k (k=0..{L}) = {[round(t,4) for t in tks]}")
print(f"     N_k=#C(F_(q^k)) = q^k+1 - q^(k/2) t_k:")
for k in range(1,6):
    Nk=q**k+1-(q**(k/2.0))*tks[k]
    print(f"       N_{k} = #C(F_{{{q}^{k}}}) = {Nk:.3f}")

print("\n(2) El certificado de positividad: A_RH = V V^* (Vandermonde en los Frobenius):")
rank=np.linalg.matrix_rank(A_RH, tol=1e-9)
print(f"     rank(A_RH)={rank} = 2g (={2*g}); nucleo dim={A_RH.shape[0]-rank} -> PSD singular (rank-deficiente).")
zs=[np.exp(1j*t) for t in thetas]+[np.exp(-1j*t) for t in thetas]   # los 2g ceros (|.|=1)
V=np.array([[z**n for z in zs] for n in range(L+1)])  # (L+1) x 2g, Vandermonde en los ceros
A_vander=(V@V.conj().T).real
print(f"     A_RH == V V^* ? maxdif = {np.abs(A_vander-A_RH).max():.2e}")
print(f"     => el certificado de positividad es la factorizacion B=V^* indexada por los CEROS (Frobenius).")
print(f"        B es Vandermonde en e^{{i theta_j}}; es PSD PORQUE los theta_j son REALES (|alpha|=sqrt q),")
print(f"        que es el teorema de Weil (indice de Hodge sobre CxC). NO hay nada que probar aqui: es ground truth.")

print("\n(3) RH-FALSO (mover un par fuera: |alpha|=sqrt(q) e^{b}, b>0) -> rompe PSD?:")
for b in [0.0,0.1,0.3]:
    radii=[np.exp(b),1.0]  # primer par off-circle
    Af,_=toeplitz_from_angles(thetas,radii,q,L)
    report(f"b={b}", Af)
print("\n  -> la positividad funcion-campo es EXACTAMENTE Herglotz: PSD sii los alpha en |.|=sqrt q (RH-FF).")
print("     Analogo limpio de DH, SIN confound (no hay 'falta de polo': el budget esta en t_0=2g).")
