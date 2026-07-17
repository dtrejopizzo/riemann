"""
ATAQUE LADO ARITMETICO: construir el * cuaternionico de Deninger DESDE el flujo de escala
(Connes-Consani), NO desde los ceros. La inversion u->1/u (=s->1-s, EF) es aditivamente
u->L-u (paridad P). El * natural sobre el espacio de escala:
   (*f)(u) = i * sgn(u-L/2) * conj( f(L-u) )
En base de modos V_n=e^{2 pi i n u /L}:  conj(f(L-u)) = sum conj(c_n) V_n  (indices fijos),
   luego multiplicar por sgn (operador Sigma), luego por i.  => * = i * Sigma * K  (K=conjugacion).
   *^2 = Sigma conj(Sigma). Si Sigma imaginaria-antisimetrica y Sigma^2=I => *^2 = -I.  (cuaternionico!)
theta = generador de escala = d/du : diag(2 pi i n / L).  Test: *^2=-1, [*,theta], y si la
Gram <V_n,V_m>=Omega(V_n,*V_m) (Omega alternante de la EF) reproduce la forma de Weil A_lambda.
TODO construido desde la geometria de escala; los ceros son OUTPUT (espectro), no input.
"""
import mpmath as mp
mp.mp.dps = 30
I=mp.mpc(0,1)
exec(open('E46_LGV_polymer.py').read().split('def report')[0])  # DandQ para A_lambda

def sigma_matrix(N,L):
    # Sigma_{nm} = (1/L) \int_0^L sgn(u-L/2) e^{2 pi i (n-m) u /L} du
    dim=2*N+1; idx=list(range(-N,N+1)); S=mp.zeros(dim)
    for a in range(dim):
        for b in range(dim):
            k=idx[a]-idx[b]
            if k==0:
                S[a,b]=0   # sgn impar -> media 0
            else:
                # \int_0^L sgn(u-L/2) e^{2 pi i k u/L} du/L
                # = (1/L)[ \int_0^{L/2}(-1)e.. + \int_{L/2}^L(+1)e.. ]
                w=2*mp.pi*I*k/L
                def F(u): return mp.e**(w*u)/w
                val=(-(F(L/2)-F(0))+(F(L)-F(L/2)))/L
                S[a,b]=val
    return S,idx

def run(lam,N):
    L=2*mp.log(mp.mpf(lam)); dim=2*N+1; idx=list(range(-N,N+1))
    print(f"\n=== arithmetic-star CORRECTO  lambda={lam} N={N} dim={dim} ===")
    # * V_n = i sgn(n) V_{-n}  (Hilbert transform sgn(n) + inversion-EF + conj). theta-compatible por construc.
    # matriz lineal Sstar con *v = Sstar conj(v):  Sstar e_n = i sgn(n) e_{-n}
    Sst=mp.zeros(dim)
    for a in range(dim):
        n=idx[a]; sg=mp.mpf(0 if n==0 else (1 if n>0 else -1))
        b=idx.index(-n); Sst[b,a]=I*sg
    # (1) *^2 = Sst conj(Sst) = -1 ? (n=0 queda como 0 -> el modo central/polo, slot real)
    Sc=mp.zeros(dim)
    for i in range(dim):
        for j in range(dim): Sc[i,j]=mp.conj(Sst[i,j])
    st2=Sst*Sc
    # en n!=0 debe ser -1; en n=0 es 0 (modo real, H^0)
    err=mp.mpf(0)
    for a in range(dim):
        tgt = mp.mpf(0) if idx[a]==0 else mp.mpf(-1)
        err=max(err, abs(st2[a,a]-tgt))
    offd=max(abs(st2[i,j]) for i in range(dim) for j in range(dim) if i!=j)
    print(f"  (1) *^2=-1 en gamma!=0, =0 en n=0(polo): max err diag={mp.nstr(err,2)}  offdiag={mp.nstr(offd,2)}  => {'EXACTO' if err<1e-25 and offd<1e-25 else 'no'}")
    # (3) [*,theta]=0 con theta=diag(2 pi i n/L). *theta v = Sst conj(theta v)=Sst conj(theta)conj(v)
    #     = Sst(-theta)conj v.  theta* v = theta Sst conj v.  conmuta <=> -Sst theta = theta Sst <=> theta Sst+Sst theta=0
    th=mp.zeros(dim)
    for i in range(dim): th[i,i]=2*mp.pi*I*idx[i]/L
    comm=th*Sst+Sst*th
    cerr=max(abs(comm[i,j]) for i in range(dim) for j in range(dim))
    print(f"  (3) [*,theta]=0: max|theta Sst+Sst theta|={mp.nstr(cerr,2)}  => {'CONMUTA EXACTO (* compat con flujo de escala)' if cerr<1e-25 else 'no'}")
    # (4) relacion con A_lambda: la forma de Weil. <v,w>=Omega(v,*w). Verificamos que A es *-real:
    #     A debe conmutar con la estructura: A J = J A con J el J-real (P) ya visto; aqui chequeamos
    #     si A es cuaternionica-Hermitiana: A(*v,*w)=conj A(v,w) (compatibilidad con *).
    D,Q,_=DandQ(str(float(lam)),N,'zeta'); A=D-Q
    EA,_=mp.eigsy(A); naA=sum(1 for i in range(dim) if EA[i]<-1e-14)
    # test compat: M = Sst^H A Sst  deberia = conj(A)=A (A real) si A es *-compatible
    M=Sst.H*A*Sst
    compat=max(abs(M[i,j]-A[i,j]) for i in range(dim) for j in range(dim))
    print(f"  (4) A_lambda *-compatible? max|Sst^H A Sst - A|={mp.nstr(compat,3)}  => {'A respeta la estructura cuaternionica' if compat<1e-9 else 'A NO *-compat (mezcla gamma!=0 con polo)'}")
    print(f"      A_lambda (prime-side) #autoval<0 = {naA} (=0 <=> RH a esta lambda)")

run('7.0',8)
run('9.0',8)
