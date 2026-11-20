import sys, pickle, math, mpmath as mp
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import galerkin_mp as G
T=float(sys.argv[1]); Nb=int(sys.argv[2]); dps=int(sys.argv[3])
D=G.build(T,Nb,dps=dps,verbose=False); mp.mp.dps=dps+20
P=pickle.load(open(f'cache/eproj_T{T}_N{Nb}.pkl','rb'))
V=[mp.matrix([mp.mpf(x) for x in r]) for r in P['C']]; nrm=[mp.mpf(x) for x in P['nrm']]
M=D['Arch']-D['Pi']; A=D['A']; B=D['B']
def dot(a,b): return mp.fsum(a[i]*b[i] for i in range(Nb))
def q(v): return dot(v, M*v)
Pr=G.projector(D)
lamA,par,res=G.lambda_A(D); u=res['ev'][1]; u=u/mp.sqrt(dot(u,u))
print(f"T={T} N={Nb} lambda_A(ev)={mp.nstr(res['ev'][0],4)} lambda_A(odd)={mp.nstr(res['odd'][0],4)}")
for k,v in enumerate(V[:4]):
    cap=dot(v,v)/nrm[k]
    ev=sum(v[j]**2 for j in range(0,Nb,2))/dot(v,v)  # sine index j+1 odd -> even fn
    pv=Pr*v; 
    W=(q(v)+2*dot(A,v)*dot(B,v))/dot(v,v)
    cosu=abs(dot(u,v))/mp.sqrt(dot(v,v)); cosup=abs(dot(u,pv))/mp.sqrt(dot(pv,pv))
    print(f" psi_{2*k}: captured {mp.nstr(cap,6)}, even-part {mp.nstr(ev,6)}, |Pv|/|v|={mp.nstr(mp.sqrt(dot(pv,pv)/dot(v,v)),4)}, W_T(Ev)/|v|^2={mp.nstr(W,4)}, a_T(Pv)/|Pv|^2={mp.nstr(q(pv)/dot(pv,pv),4)}, angle(u,v)={mp.nstr(mp.acos(cosu),4)}, angle(u,Pv)={mp.nstr(mp.acos(cosup),4)}")
# Ritz on P_T ∩ span{v_0..v_2m}
for m in range(1,len(V)):
    S=mp.matrix(Nb,m+1)
    for i in range(m+1):
        for j in range(Nb): S[j,i]=V[i][j]
    Q=Pr*S
    # orthonormalise columns of Q (drop rank deficiency)
    U,s,Vt=mp.svd_r(Q)
    r=[i for i in range(len(s)) if s[i]>s[0]*mp.mpf(10)**(-(dps-5))]
    Ub=U[:, :len(r)] if False else mp.matrix([[U[a,b] for b in r] for a in range(Nb)])
    H=Ub.T*M*Ub; E,W_=mp.eigsy(H); i0=min(range(len(E)),key=lambda i:E[i]); w=Ub*W_[:,i0]
    ang=mp.acos(min(1,abs(dot(u,w))/mp.sqrt(dot(w,w))))
    # angle u to span
    pu=Ub*(Ub.T*u); angs=mp.acos(min(1,mp.sqrt(dot(pu,pu))))
    print(f" Ritz P_T∩span(Epsi_0..Epsi_{2*m}) dim {len(r)}: bottom={mp.nstr(E[i0],4)}, ratio to lambda_A={mp.nstr(E[i0]/res['ev'][0],4)}, angle(u,bottom)={mp.nstr(ang,3)}, angle(u,span)={mp.nstr(angs,3)}, sing min/max={mp.nstr(s[len(s)-1]/s[0],3)}")
