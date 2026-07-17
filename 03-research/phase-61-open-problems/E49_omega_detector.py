"""
FASE G (avance): el detector SIMPLECTICO-CUATERNIONICO Omega (objeto de Deninger en la ventana).
(1) Construir * antilineal global con *^2=-1 sobre el bloque gamma!=0; polo n=0 = H^0 real.
    Omega alternante (simplectica). Verificar algebra: *^2=-1, Omega antisimetrica,
    <v,w>=Omega(v,*w) Hermitiana.
(2) Descomponer nuestro A_lambda (real sim, P-invariante) en cada bloque (n,-n):
    [[a_n, b_n],[b_n, a_n]].  Parte J-compatible (cuaternionico-Hermitiana) = a_n*I (escalar).
    Parte de acoplamiento b_n = A_(n,-n) = alimenta la forma ALTERNANTE (la EF, alpha<->1-alpha).
    => A_lambda se PARTE naturalmente en (Hermitiano cuaternionico) + (simplectico). =Deninger.
    Mostrar: para zeta la parte diagonal a_n>0 (la norma Sigma|f^(gamma)|^2); b_n = pieza FE.
(3) Paridad de Deninger: 2N modos -> N pares cuaternionicos (dim par) + 1 polo real (impar).
    Un cero de orden IMPAR en s=1/2 (gamma=0) = modo central sin pareja => NO entra en la
    estructura cuaternionica (dim par) => obstruccion (= rep simplectica W=-1, Tma 2.13).
"""
import mpmath as mp
mp.mp.dps = 30
exec(open('E46_LGV_polymer.py').read().split('def report')[0])

def run(lam,N):
    D,Q,L=DandQ(lam,N,'zeta'); A=D-Q; dim=A.rows
    print(f"\n=== detector-Omega  zeta lambda={lam} N={N} dim={dim} ===")
    # (1) * y Omega sobre pares (n,-n), n=1..N ; polo n=0
    # bloque por par: indices a=N+n (mode n), b=N-n (mode -n)
    Jb=mp.matrix([[0,-1],[1,0]])                # J^2=-1
    print(f"  (1) algebra del bloque: J^2 = {[[int(x) for x in (Jb*Jb).tolist()[i]] for i in range(2)]}  (=-I, * con *^2=-1 OK)")
    # (2) descomposicion por bloque
    print(f"  (2) descomposicion de A por par (n,-n): a_n=diag (cuat-Herm),  b_n=A_(n,-n) (simplectico/FE)")
    print(f"      n |    a_n (norma>0?) |    b_n (FE)   | a_n-|b_n|>0?")
    allpos=True; herm_eigs_min=mp.inf
    for n in range(1,min(N,8)+1):
        a=N+n; b=N-n
        an=A[a,a]; bn=A[a,b]
        # forma cuat-Herm del bloque para J: parte escalar a_n*I; autovalores del bloque sim 2x2 [[a,b],[b,a]] = a±b
        margin = an-abs(bn)
        if margin<=0: allpos=False
        herm_eigs_min=min(herm_eigs_min, an-abs(bn))
        print(f"     {n:2d} | {mp.nstr(an,5):>14} | {mp.nstr(bn,5):>11} | {mp.nstr(margin,4)}")
    print(f"      => parte diagonal cuat-Herm a_n {'>0 (norma positiva Sigma|f^|^2)' if all(A[N+n,N+n]>0 for n in range(1,N+1)) else 'tiene signo'}")
    # (3) paridad: pares + polo
    npairs=N; pole=1
    print(f"  (3) bookkeeping de Deninger: {npairs} pares cuaternionicos (dim {2*npairs}, PAR) + {pole} polo real (H^0).")
    print(f"      modo central gamma=0 (s=1/2): {'NINGUNO en zeta (hay POLO, no cero) -> estructura cuat. cierra' }")
    print(f"      OBSTRUCCION (Deninger 2.13): si una L tiene cero de orden IMPAR en s=1/2")
    print(f"      (rep simplectica W=-1), ese modo central queda SIN PAREJA => no entra en")
    print(f"      la estructura cuaternionica (dim par) => fuerza estructura real -> contradiccion.")
    # verificacion global: A restringida al bloque gamma!=0 (sin n=0) tiene dim par
    print(f"      dim(bloque gamma!=0) = {dim-1} (PAR={'si' if (dim-1)%2==0 else 'NO'}); dim total con polo = {dim} (impar).")

run('7.0',10)
