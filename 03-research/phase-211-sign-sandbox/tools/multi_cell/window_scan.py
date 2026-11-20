# Positivity window of the split R-cell form. usage: pickle mode [args]
#  mode 'c'   : uniform scaling w_n = c (all prime powers)          -> c_-, c_+
#  mode 'p:K' : only prime powers of the prime K scaled (others 1)   -> window in the factor
#  mode 'a:K' : only the atom n = K scaled
#  mode 'P:K' : a_P, prime powers of primes < K deleted (report bottom values only)
# Prints bottom of Q/l_g and Q/|F|^2 on V_R (transported constraints); endpoints by bisection (sign of Q/|F|^2 bottom).
import sys, pickle, mpmath as mp
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-211-sign-sandbox/tools')
import galerkin_mp as Gm
d=pickle.load(open(sys.argv[1],'rb')); dps=d['dps']; mp.mp.dps=dps
tm=lambda rows: mp.matrix([[mp.mpf(x) for x in r] for r in rows])
Q0=tm(d['Q0']); Qn={n:tm(d['Qn'][n]) for n in d['Qn']}; C=tm(d['C']); L=tm(d['L']); Nb=Q0.rows
Qf,_=mp.qr(C,mode='full'); V=Qf[:,4:Nb]
sym=lambda M:(M+M.T)/2
A0=sym(V.T*Q0*V); An={n:sym(V.T*Qn[n]*V) for n in Qn}; Lv=sym(V.T*L*V)
Li=mp.inverse(mp.cholesky(Lv))
def A(w): 
    M=A0.copy()
    for n in An: M-=w.get(n,1)*An[n]
    return M
def bot(w):
    M=A(w); e1=min(mp.eigsy(M,eigvals_only=True)); e2=min(mp.eigsy(sym(Li*M*Li.T),eigvals_only=True)); return e1,e2
mode=sys.argv[2]
if mode=='info':  # bottom pairs at w=1 and first-order slopes K = <F, sum_n A_n F> per eigvector, per atom
    M=A({}); E,U=mp.eigsy(M); idx=sorted(range(len(E)),key=lambda i:E[i])
    for r_ in idx[:3]:
        u=U[:,r_]; K=sum(((u.T*An[n]*u)[0] for n in An),mp.mpf(0))
        per={n:mp.nstr((u.T*An[n]*u)[0],4) for n in An}
        print(f"INFO {sys.argv[1]} eig {mp.nstr(E[r_],6)}  K=sum_n<A_n> {mp.nstr(K,5)}  eig/K {mp.nstr(E[r_]/K,5)}  per-atom {per}",flush=True)
    sys.exit()
def wof(x):
    if mode=='c': return {n:x for n in An}
    k,K=mode.split(':'); K=int(K)
    if k=='p': return {n:(x if Gm._Lam(n)==K else 1) for n in An}
    if k=='a': return {n:(x if n==K else 1) for n in An}
def psd(M):
    try: mp.cholesky(M); return True
    except Exception: return False
def bisL(lo,hi,it=90):  # f(lo)<0<=f(hi)
    for _ in range(it):
        m=(lo+hi)/2
        if psd(A(wof(m))): hi=m
        else: lo=m
    return lo,hi
def bis(lo,hi,it=90):  # f(lo)>=0>f(hi) in l_g ratio
    for _ in range(it):
        m=(lo+hi)/2
        if psd(A(wof(m))): lo=m
        else: hi=m
    return lo,hi
if mode.startswith('P:'):
    K=int(mode[2:]); w={n:(0 if Gm._Lam(n)<K else 1) for n in An}
    e1,e2=bot(w); print(f"{sys.argv[1]} a_{K}: Q/|F|^2 {mp.nstr(e1,4)} Q/l_g {mp.nstr(e2,5)}"); sys.exit()
grid=[mp.mpf(x) for x in sys.argv[3].split(',')] if len(sys.argv)>3 else [mp.mpf(x) for x in ('0','0.5','0.9','0.99','1','1.01','1.1','1.5')]
vals={}
import os
FAST=os.environ.get('FAST')
for x in grid:
    if FAST:
        vals[x]=1 if psd(A(wof(x))) else -1; print(mode,'x=',mp.nstr(x,6),'psd' if vals[x]>0 else 'NOT psd',flush=True); continue
    e1,e2=bot(wof(x)); vals[x]=e2
    print(f"{mode} x={mp.nstr(x,6)}: Q/|F|^2 {mp.nstr(e1,4)}  Q/l_g {mp.nstr(e2,5)}",flush=True)
one=mp.mpf(1)
if vals.get(one,-1)<0: print('NOT POSITIVE AT x=1'); sys.exit()
ups=[x for x in grid if x>1 and vals[x]<0]; dns=[x for x in grid if x<1 and vals[x]<0]
cp=bis(one,min(ups)) if ups else None; cm=bisL(max(dns),one) if dns else None
r=lambda t: None if t is None else mp.nstr((t[0]+t[1])/2-1,6)
print(f"RESULT {sys.argv[1]} {mode}: x_- = {r(cm)}  x_+ = {r(cp)}",flush=True)
