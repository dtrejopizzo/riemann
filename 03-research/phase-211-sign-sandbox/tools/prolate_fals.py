import sys, pickle, mpmath as mp
sys.path.insert(0,__import__('os').path.dirname(__import__('os').path.abspath(__file__)))
import galerkin_mp as G
T=float(sys.argv[1]); Nb=int(sys.argv[2]); dps=int(sys.argv[3])
D=G.build(T,Nb,dps=dps,verbose=False); mp.mp.dps=dps+20
P=pickle.load(open(f'cache/eproj_T{T}_N{Nb}.pkl','rb')); V=[[mp.mpf(x) for x in r] for r in P['C']]
Pr=G.projector(D); m=4
S=mp.matrix(Nb,m+1)
for i in range(m+1):
    for j in range(Nb): S[j,i]=V[i][j]
U,s,_=mp.svd_r(Pr*S); Ub=mp.matrix([[U[a,b] for b in range(len(s))] for a in range(Nb)])
Ar=Ub.T*D['Arch']*Ub; Pi=Ub.T*D['Pi']*Ub
E,W=mp.eigsy(Ar-Pi); i0=min(range(len(E)),key=lambda i:E[i]); w=W[:,i0]
pis=(w.T*Pi*w)[0]; print(f"T={T}: block bottom {mp.nstr(E[i0],4)}, Pi(F_block)={mp.nstr(pis,5)}, Arch(F_block)={mp.nstr((w.T*Ar*w)[0],5)}")
for c in ['0.9','0.99','0.9999','1.0001','1.01','1.1']:
    Ec=mp.eigsy(Ar-mp.mpf(c)*Pi,eigvals_only=True); print(f"  c={c}: block bottom {mp.nstr(min(Ec),4)}")
