# Bottom eigenvectors of Mori's Galerkin form G = A + J (per parity) by subspace inverse iteration in arb.
import json,sys,os,time
from pathlib import Path
from flint import arb,arb_mat,ctx
D=Path(os.environ['SP'])/'mori15'
p=int(sys.argv[1]); K=int(sys.argv[2]) if len(sys.argv)>2 else 6
ctx.prec=720
A=json.load(open(D/f'p{p}_A_mid.json')); J=json.load(open(D/f'p{p}_J_mid.json'))
d=len(A)
G=arb_mat([[arb(A[i][j])+arb(J[i][j]) for j in range(d)] for i in range(d)])
G=(G+G.transpose())/2
t0=time.time(); Gi=G.inv(); print('inv',time.time()-t0,flush=True)
# starting block: first K basis vectors + random mix
import random; random.seed(1)
V=arb_mat([[arb(random.random()) for k in range(K)] for i in range(d)])
def orth(V):
    cols=[[V[i,k] for i in range(d)] for k in range(K)]
    out=[]
    for c in cols:
        for o in out:
            dot=sum(a*b for a,b in zip(c,o)); c=[a-dot*b for a,b in zip(c,o)]
        nrm=sum(a*a for a in c).sqrt(); out.append([a/nrm for a in c])
    return arb_mat([[out[k][i] for k in range(K)] for i in range(d)])
for it in range(10):
    V=orth((Gi*V).mid())
    R=V.transpose()*G*V
    print('it',it,[R[k,k].str(12) for k in range(K)],flush=True)
# diagonalize the KxK Rayleigh matrix by Jacobi in arb
import mpmath as mp
mp.mp.prec=720
Rm=mp.matrix([[mp.mpf(R[i,j].mid().str(200,radius=False)) for j in range(K)] for i in range(K)])
E,U=mp.eigsy(Rm)
order=sorted(range(K),key=lambda k:E[k])
Vm=[[mp.mpf(V[i,k].mid().str(200,radius=False)) for k in range(K)] for i in range(d)]
vecs=[]
for k in order:
    v=[sum(Vm[i][j]*U[j,k] for j in range(K)) for i in range(d)]
    vecs.append(v)
res={'parity':p,'dim':d,'eigs':[mp.nstr(E[k],40) for k in order]}
# residual check on bottom vector
v0=arb_mat([[arb(mp.nstr(x,200))] for x in vecs[0]])
rq=(v0.transpose()*G*v0)[0,0]; r=G*v0-rq*v0
rn=sum(abs(r[i,0]).upper()**2 for i in range(d)).sqrt()
res['rayleigh_bottom']=rq.str(60); res['residual_norm']=rn.str(10)
print(res,flush=True)
res['vectors']=[[mp.nstr(x,120) for x in v] for v in vecs[:3]]
json.dump(res,open(D/f'p{p}_eig.json','w'))
