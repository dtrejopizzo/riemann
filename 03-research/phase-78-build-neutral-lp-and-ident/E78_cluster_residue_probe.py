from pathlib import Path
import sys, json
import mpmath as mp
B76=Path('/mnt/data/phase76/phase-76-normalized-adjugate-arithmetic-lock')
B77=Path('/mnt/data/phase77/phase-77-weyl-limit-point')
sys.path[:0]=[str(B76),str(B77)]
from P76_002_mp_entry_audit import build_mp, vec_norm
from E77_3c_two_generator_ident_probe import GAMMA, right_transfer_data

def section(Hmax,idxmax,maxN,N):
    off=maxN-N
    return Hmax[off:Hmax.rows-off,off:Hmax.cols-off],idxmax[off:len(idxmax)-off]

def row(z,idx,L):
    return mp.matrix([[1/(z-2*mp.pi*n/L) for n in idx]])

def run(label,plant,maxN=12,dps=60):
    mp.mp.dps=dps
    Hmax,idxmax,L=build_mp(6,maxN,dps,planted=plant)
    out=[]
    for N in [6,8,10,12]:
        H,idx=section(Hmax,idxmax,maxN,N)
        mu,A,db_idx,inner,x=right_transfer_data(H,idx)
        vals,vecs=mp.eighe(A)
        order=sorted(range(len(vals)),key=lambda j: abs(vals[j]))
        b=mp.matrix([[H[j+1,H.cols-1]] for j in range(H.rows-2)])
        rz=row(1j,inner,L)
        rz2=row(2j,inner,L)
        rows=[]
        for k in [1,2,3,4,6,8]:
            if k>len(order): continue
            Pb=mp.matrix(A.rows,1)
            for jj in order[:k]:
                coeff=mp.fsum(mp.conj(vecs[t,jj])*b[t] for t in range(A.rows))
                for t in range(A.rows): Pb[t]+=vecs[t,jj]*coeff
            alpha=(rz*Pb)[0]
            pn=vec_norm(Pb)
            if abs(alpha)>mp.mpf('1e-100'):
                v=Pb/alpha
                vn=vec_norm(v)
                prof=(rz2*v)[0]
            else:
                vn=mp.inf; prof=mp.nan
            rows.append({'k':k,'alpha':mp.nstr(abs(alpha),12),'Pbnorm':mp.nstr(pn,12),'vnorm':mp.nstr(vn,12),'profile2':mp.nstr(prof,12)})
        out.append({'N':N,'mu':mp.nstr(mu,12),'rows':rows})
        print(label,'N',N)
        for r in rows: print(' k',r['k'],'alpha',r['alpha'],'Pb',r['Pbnorm'],'vnorm',r['vnorm'],'prof2',r['profile2'],flush=True)
    return out

allout={}
for label,plant in [('zeta',None),('plant',(GAMMA,'0.30','5.0'))]:
    allout[label]=run(label,plant)
Path('/mnt/data/E78_149_cluster_residue_results.json').write_text(json.dumps(allout,indent=2))
