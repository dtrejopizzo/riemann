# lambda_min of P_a^*P_a + P_b^*P_b on L^2[-T,T] via exact lattice orbits (a,b) in Z^2. UNCERTIFIED float (base-point sweep).
import numpy as np, sys
def stab(T,la,lb,n=2000):
    best=(np.inf,0)
    for u0 in np.linspace(-T,T,n):
        A=range(-int(2*T/la)-1,int(2*T/la)+2); Bb=range(-int(2*T/lb)-1,int(2*T/lb)+2)
        pts=[(a,b) for a in A for b in Bb if abs(u0+a*la+b*lb)<=T]
        N=len(pts); M=np.zeros((N,N))
        for i,(a,b) in enumerate(pts):
            for j,(c,d) in enumerate(pts):
                M[i,j]=(b==d)+(a==c)
        e=np.linalg.eigvalsh(M)[0]
        if e<best[0]: best=(e,N)
    return best
if 0:
    print('T=%.4f {2,3}: lam_min=%.4e (orbit size %d)'%((T,)+stab(T,np.log(2),np.log(3))),' {1.6,3}: %.4e (%d)'%stab(T,np.log(1.6),np.log(3)),flush=True)
def stab_exact(T,la,lb):
    R=range(-6,7); bps=sorted({s*T-a*la-b*lb for a in R for b in R for s in (1,-1) if abs(s*T-a*la-b*lb)<=T})
    mids=[(x+y)/2 for x,y in zip(bps,bps[1:]) if y-x>1e-13]
    best=(np.inf,0)
    for u0 in mids:
        pts=[(a,b) for a in R for b in R if abs(u0+a*la+b*lb)<=T]
        M=np.array([[(p[0]==q[0])+(p[1]==q[1]) for q in pts] for p in pts],float)
        e=np.linalg.eigvalsh(M)[0]
        if e<best[0]: best=(e,len(pts))
    return best
for T in map(float,sys.argv[1:]):
    print('EXACT-orbit T=%.4f {2,3}: %.4e (%d)'%((T,)+stab_exact(T,np.log(2),np.log(3))),' {1.6,3}: %.4e (%d)'%stab_exact(T,np.log(1.6),np.log(3)),flush=True)
