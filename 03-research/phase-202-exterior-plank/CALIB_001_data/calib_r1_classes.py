# CALIB_R1: clases de razón q=a/b (coprimos, ordenados) para <Zr, Z^X_log r> = Σ_{(a,b)} Σ_k L_X(kb)/k · λ∫_k ρ(at)ρ(bt)dt,
# (m,n)=(ka,kb); Q_j(a,b)=λ∫_j^{j+1}ρ(at)ρ(bt)dt (corte max(a,b)·t ≤ X). Simpson, dω ≤ 0.004/2. NUMÉRICO.
import json,math,os,time
import numpy as np
from multiprocessing import Pool
exec(open('calib_r1.py').read().split('# ---------- combs')[0].split("print('tables'")[0])
X=float(os.environ.get('XC','240'))
def pair(ab):
    a,b=ab; M=max(a,b); tmax=X/M; out=[]
    j=1
    while j<tmax:
        hi=min(j+1,tmax); n=max(8,2*int(math.ceil((hi-j)*M/0.002/2)))
        t=np.linspace(j,hi,n+1); f=rho_f(a*t)*rho_f(b*t); h=(hi-j)/n
        out.append(lam*h/3*(f[0]+f[-1]+4*f[1:-1:2].sum()+2*f[2:-1:2].sum())); j+=1
    return (a,b,out)
if __name__=='__main__':
    t0=time.time()
    prs=[(a,b) for a in range(1,int(X)+1) for b in range(1,int(X)+1) if math.gcd(a,b)==1 and max(a,b)<X]
    with Pool(20) as P: R=P.map(pair,prs,chunksize=50)
    json.dump({f'{a},{b}':q for a,b,q in R},open(f'classes_Q_X{int(X)}.json','w'))
    print(len(prs),time.time()-t0)
