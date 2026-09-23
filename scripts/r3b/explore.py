import sys, time, json
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts')
import numpy as np
from scipy.linalg import toeplitz
from scipy.optimize import minimize
import tk_common as tk

def ceiling(T,M,ntau,nfft=1<<16):
    parts=tk.make_S_parts(T)[:3]
    P=np.pi*M/T
    grid=np.linspace(-2.2*P,0.2*P,ntau)
    MT=[[toeplitz(np.conj(c),c) for c in tk.coeff_families(T,M,t0,nfft,parts)] for t0 in grid]
    f=lambda b: -min(np.linalg.eigvalsh(Ms[0]+b[0]*Ms[1]+b[1]*Ms[2])[0] for Ms in MT)
    best=None
    for st in ([2.0,0.0],[2.0,-0.02]):
        r=minimize(f,st,method='Nelder-Mead',options={'xatol':1e-9,'fatol':1e-14,'maxiter':400})
        if best is None or -r.fun>best[0]: best=(-r.fun,r.x)
    c,b=best
    vals=[np.linalg.eigvalsh(Ms[0]+b[0]*Ms[1]+b[1]*Ms[2])[0] for Ms in MT]
    i=int(np.argmin(vals))
    return c,b,grid[i],MT[i],np.array(vals)

if __name__=='__main__':
    T=float(eval(sys.argv[1])); M=int(sys.argv[2]); ntau=int(sys.argv[3]); B=float(sys.argv[4])
    t=time.time()
    c,b,t0,Ms,vals=ceiling(T,M,ntau)
    print("T=%.8f M=%d ntau=%d  Ceil=%+.6e beta=(%.6f,%.6f) tau0=%.5f  %.1fs"%(T,M,ntau,c,b[0],b[1],t0,time.time()-t),flush=True)
    C0,C1,C2=Ms
    w,V=np.linalg.eigh(C0+b[0]*C1+b[1]*C2)
    print(" eigs:",w[:4],flush=True)
    res={'T':T,'M':M,'ntau':ntau,'Ceil':c,'beta':list(map(float,b)),'tau0':float(t0),'B':B}
    bestall=None
    for r in (2,3,4,6):
        U=V[:,:r]
        A0=U.conj().T@C0@U; A1=U.conj().T@C1@U; A2=U.conj().T@C2@U
        def obj(x):
            z=(x[:r]+1j*x[r:]); n=np.vdot(z,z).real
            if n<1e-12: return 1e9
            a=np.vdot(z,A0@z).real/n; b0=np.vdot(z,A1@z).real/n; b1=np.vdot(z,A2@z).real/n
            return a+B*(abs(b0)+abs(b1))
        best=None
        for seed in range(8):
            rng=np.random.default_rng(seed); x0=np.zeros(2*r); x0[0]=1.0
            if seed: x0=rng.standard_normal(2*r)
            rr=minimize(obj,x0,method='Nelder-Mead',options={'maxiter':8000,'maxfev':8000,'xatol':1e-13,'fatol':1e-18})
            if best is None or rr.fun<best.fun: best=rr
        z=best.x[:r]+1j*best.x[r:]; z/=np.linalg.norm(z)
        a=np.vdot(z,A0@z).real; b0=np.vdot(z,A1@z).real; b1=np.vdot(z,A2@z).real
        q=(U@z)
        print("  r=%d: a=%+.8e b0=%+.4e b1=%+.4e  bound=%+.8e"%(r,a,b0,b1,a+B*(abs(b0)+abs(b1))),flush=True)
        if bestall is None or a+B*(abs(b0)+abs(b1))<bestall[0]:
            bestall=(a+B*(abs(b0)+abs(b1)),r,a,b0,b1,q)
    res['best']={'bound':bestall[0],'r':bestall[1],'a':bestall[2],'b0':bestall[3],'b1':bestall[4],
                 'q_re':list(bestall[5].real),'q_im':list(bestall[5].imag)}
    json.dump(res,open('explore_T%s_M%d.json'%(sys.argv[1].replace('/','_'),M),'w'),indent=1)
