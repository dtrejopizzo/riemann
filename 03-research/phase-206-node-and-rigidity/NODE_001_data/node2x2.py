# NODE_001: bloque par {k=1,3} en T=½log3 y T=½log5. Descompone 𝔄 = 𝔪 + 𝔢 − 2ccᵀ + Φ y prueba el nodo en c^⊥. NUMÉRICO (mpmath 30).
import mpmath as mp, sys
mp.mp.dps=30
def Lam(n):
    from sympy import factorint
    f=factorint(n); return mp.log(list(f)[0]) if len(f)==1 else mp.mpf(0)
C0=mp.digamma(0.25)-mp.log(mp.pi)
K=lambda u:1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2))
tail=lambda T:mp.log(mp.coth(T/2))+2*mp.atan(mp.exp(-T))
def cfun(k,kp,u,T):
    a=mp.pi*k/(2*T); b=mp.pi*kp/(2*T); L=2*T-u
    if k==kp: return (L*mp.cos(b*u)-(mp.sin(2*b*L+b*u)-mp.sin(b*u))/(2*b))/2
    return ((mp.sin((a-b)*L-b*u)+mp.sin(b*u))/(a-b)-(mp.sin((a+b)*L+b*u)-mp.sin(b*u))/(a+b))/2
def cs(k,l,u,T): return (cfun(k,l,u,T)+cfun(l,k,u,T))/2/T   # normalizada (e_k = s_k/√T)
def block(T,ks,lam=Lam,cfac=1):
    n=len(ks); Mm=mp.matrix(n,n); M=mp.matrix(n,n); C=mp.matrix(n,n)
    for i in range(n):
        for j in range(n):
            k,l=ks[i],ks[j]
            Mm[i,j]=(C0+tail(T))*(1 if i==j else 0)+mp.quad(lambda u:((1 if i==j else 0)-cs(k,l,u,T))*K(u),[0,T/8,T/2,T,2*T])
            M[i,j]=-2*mp.quad(lambda u:mp.exp(u/2)*cs(k,l,u,T),[0,T,2*T])
            m=2
            while mp.log(m)<2*T:
                L_=lam(m)
                if L_: C[i,j]-=cfac*2*L_/mp.sqrt(m)*cs(k,l,mp.log(m),T)
                m+=1
    c=[mp.quad(lambda x:mp.cosh(x/2)*mp.sin(mp.pi*k*(x+T)/(2*T)),[-T,T])/mp.sqrt(T) for k in ks]
    cc=mp.matrix(n,n)
    for i in range(n):
        for j in range(n): cc[i,j]=c[i]*c[j]
    e=M+2*cc; Phi=C-M; A=Mm+C
    return dict(m=Mm,e=e,c=c,Phi=Phi,A=A,M=M,C=C)
def show(T,ks,**kw):
    d=block(T,ks,**kw); print('T=',mp.nstr(T,8),'ks',ks,kw)
    for nm in ['m','e','Phi','A']: print(nm,[[mp.nstr(d[nm][i,j],8) for j in range(len(ks))] for i in range(len(ks))], 'eig',[mp.nstr(x,8) for x in mp.eigsy(d[nm])[0]])
    print('c',[mp.nstr(x,10) for x in d['c']])
    me=d['m']+d['e']; print('m+e eig',[mp.nstr(x,8) for x in mp.eigsy(me)[0]])
    c=d['c']; v=mp.matrix([-c[1],c[0]]) if len(ks)==2 else None
    if v is not None:
        v=v/mp.norm(v)
        q=lambda Q:(v.T*Q*v)[0]
        print('F ⊥ c: (m+e)(F)=',mp.nstr(q(me),10),' Phi(F)=',mp.nstr(q(d['Phi']),10),' Z(F)=',mp.nstr(q(me+d['Phi']),10))
        print('   Phi split: comb(F)=',mp.nstr(q(d['C']),10),' -main M(F)=',mp.nstr(-q(d['M']),10))
    return d
for T in [mp.log(3)/2, mp.log(5)/2]:
    show(T,[1,3]); show(T,[1,3],cfac=mp.mpf('1.2')); show(T,[1,3],lam=lambda n: (Lam(n) if n%2 else 0))

# --- per-n contributions at ½log5 on F ⊥ c, and c-threshold
if __name__=='__main__' and len(sys.argv)>1:
    T=mp.log(5)/2; ks=[1,3]; d=block(T,ks); c=d['c']; v=mp.matrix([-c[1],c[0]]); v=v/mp.norm(v)
    print('F = %s e1 + %s e3'%(mp.nstr(v[0],10),mp.nstr(v[1],10)))
    for n in [2,3,4]:
        cf=sum(v[i]*v[j]*cs(ks[i],ks[j],mp.log(n),T) for i in range(2) for j in range(2))
        print('n=',n,' c_F(log n)=',mp.nstr(cf,10),' contrib -2Λ(n)n^-1/2 c_F =',mp.nstr(-2*Lam(n)/mp.sqrt(n)*cf,10))
    print('c_F(0)=',mp.nstr(sum(v[i]**2 for i in range(2)),5))
    for cf in ['0.8','0.99','0.9924','1.5','2','3']:
        dd=block(T,ks,cfac=mp.mpf(cf)); ev=mp.eigsy(dd['A'])[0]; print('cfac',cf,'eigs A',[mp.nstr(x,6) for x in ev])
