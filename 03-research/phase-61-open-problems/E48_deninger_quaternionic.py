"""
FASE G (post-F): test de la estructura de Deninger (2204.02714) en la ventana finita.
Deninger 2.7/2.13: la forma que forzaria RH es producto escalar <h,h'>=tr(h cup *h'),
  cup ALTERNANTE (simplectica), * ANTILINEAL con *^2=-1 (CUATERNIONICA).
  H^0/polo = unico trozo con estructura REAL (theta=0). NO hay estructura real global.
Nuestra A_lambda es SIMETRICA REAL. Test:
 (1) [A,P]=0 con P=paridad (n<->-n, P^2=+1): A tiene estructura REAL (la 'demasiado simple').
 (2) J = estructura compleja (n<->-n con signo, J^2=-1, cuaternionica) sobre el bloque gamma!=0.
     [A,J]=0  <=>  A_{n,-n}=0 en cada par. Computar A_{n,-n}: si !=0, A NO es J-compatible
     => la forma simetrica real es la sombra equivocada (consistente con Deninger + Fase F).
 (3) El modo n=0 (POLO) queda impar/suelto = H^0 real de Deninger.
 (4) Companion ALTERNANTE Omega (Omega_{n,-n}=A_{n,-n}, antisimetrica): el objeto J-compatible.
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E46_LGV_polymer.py').read().split('def report')[0])  # DandQ, helpers

def test(lam,N):
    D,Q,L=DandQ(lam,N,'zeta'); A=D-Q; dim=A.rows; idx=list(range(-N,N+1))
    # (1) Paridad P: e_n -> e_{-n}
    P=mp.zeros(dim)
    for a in range(dim): P[a,dim-1-a]=1   # idx[a]=-N+a, su -n esta en dim-1-a
    commP=A*P-P*A
    nP=max(abs(commP[i,j]) for i in range(dim) for j in range(dim))
    # (2) couplings n<->-n  (A_{n,-n})
    print(f"\n=== zeta lambda={lam} N={N} ===")
    print(f"  [A,P] (P=paridad, P^2=+1): max|.|={mp.nstr(nP,3)}  => {'A COMMUTA con P (estructura REAL presente)' if nP<1e-12 else 'no'}")
    print(f"  acoplamientos paridad A_(n,-n) (= obstruccion a J-compat, J^2=-1):")
    maxc=mp.mpf(0)
    for n in range(1,N+1):
        a=N+n; b=N-n   # idx a = n, idx b = -n
        c=A[a,b]; maxc=max(maxc,abs(c))
        if n<=6: print(f"    n={n:2d}: A_(n,-n)={mp.nstr(c,4)}")
    print(f"  max_n |A_(n,-n)| = {mp.nstr(maxc,4)}")
    if maxc>1e-9:
        print("  => A_(n,-n) != 0  =>  [A,J]!=0: la forma SIMETRICA REAL NO es J-compatible.")
        print("     (consistente con Deninger: la estructura real es 'demasiado simple'; Fase F)")
    else:
        print("  => A_(n,-n)=0: A seria J-compatible (cuaternionica). Revisar.")
    # (3) modo n=0 = polo, suelto (H^0 real)
    print(f"  modo n=0 (POLO): A_00={mp.nstr(A[N,N],4)}  (= H^0 real de Deninger, theta=0, impar/suelto)")
    # (4) companion alternante Omega_{n,-n}=A_{n,-n}, Omega_{-n,n}=-A_{n,-n}
    #     verificar que Omega es J-compatible: en bloque 2x2 [[0,c],[-c,0]] conmuta con J=[[0,-1],[1,0]]
    print("  companion ALTERNANTE Omega (simplectica): bloque [[0,c],[-c,0]] conmuta con J? (cuaternionico)")
    n=1; a=N+n; b=N-n
    c=A[a,b]
    Jb=mp.matrix([[0,-1],[1,0]]); Ob=mp.matrix([[0,c],[-c,0]])
    comm=Ob*Jb-Jb*Ob
    print(f"    [Omega_block, J] max|.|={mp.nstr(max(abs(comm[i,j]) for i in range(2) for j in range(2)),3)}  => {'Omega J-compatible (objeto cuaternionico)' if max(abs(comm[i,j]) for i in range(2) for j in range(2))<1e-20 else 'no'}")

test('7.0',10)
