import numpy as np, mpmath as mp, sys, json, pickle
from cache import get
from wext import Combo, evaluate, D4, wfun
from gauge import project
mu=int(sys.argv[1]); cases=sys.argv[2].split(','); Vs=[float(x) for x in sys.argv[3].split(',')]
D=get(mu); c=D['c']; lam=mp.sqrt(mu)
def core_coef(ks):
    # f = Σ a_k λ^{-1/2}ψ_k(x/λ): f(0)=0, f(λ)=0, f̂(0)=0 (f̂(0)=Σ a_k λ^{1/2} μ_k ψ_k(0)); last only if len(ks)==4
    mp.mp.dps=200
    rows=[[D['k'][k]['psi0'] for k in ks],[D['k'][k]['psi1'] for k in ks]]
    if len(ks)==4: rows.append([lam*D['k'][k]['muk']*D['k'][k]['psi0'] for k in ks])
    A=mp.matrix(rows); n=len(ks)
    # null vector: fix a_0=1 and solve
    Ar=mp.matrix([[A[i,j] for j in range(1,n)] for i in range(A.rows)]); rhs=mp.matrix([-A[i,0] for i in range(A.rows)])
    x=mp.lu_solve(Ar,rhs); a=[mp.mpf(1)]+[x[i] for i in range(n-1)]
    nr=mp.sqrt(mp.fsum(t*t for t in a)); a=[t/nr for t in a]
    fh0=mp.fsum(a[i]*lam*D['k'][k]['muk']*D['k'][k]['psi0'] for i,k in enumerate(ks))
    return dict(zip(ks,a)),fh0
res={}
for case in cases:
    if case=='psi4': coef={4:mp.mpf(1)}
    elif case=='psi0': coef={0:mp.mpf(1)}
    elif case=='fstar2': coef={0:mp.mpf('1.106365'),4:mp.mpf('-1.821723')}
    elif case=='fstar4': coef={0:mp.mpf('1.106365'),4:mp.mpf('-1.821723'),8:mp.mpf('3.3400e-5'),12:mp.mpf('-2.4993e-9')}
    elif case=='core3': coef,fh0=core_coef((0,4,8))
    elif case=='core4': coef,fh0=core_coef((0,4,8,12))
    C=Combo(D,coef)
    # leak (two-sided) from exact 1-λ_k and from the exterior integral
    leak_exact=mp.fsum(coef[k]**2*D['k'][k]['one_minus'] for k in coef) if len(coef)==1 else None
    rows=[]
    for V in Vs:
        o,_=evaluate(C,V=V)
        rows.append(o)
    o=rows[-1]
    scale=C.scale  # ρ_true = scale·ρ_num
    leak2=2*float(lam)*o['R2']*scale**2               # two-sided ‖r‖² = 2λ∫_1^∞ρ²
    Wext=float(lam)*o['Qform']*scale**2
    # gauge projection
    pj={}
    for J in (20,40,80):
        P=project(C.t,C.Y,J); pj[J]=P
    P=pj[80]; R2pi=o['R2']-P['rem2']/2
    Pw_pi=np.trapz(wfun(C.t[1:],mu)*P['prho'][1:]**2,C.t[1:])
    Pw_pi+=o['Pw']-np.trapz(wfun(C.t[1:],mu)*C.Y[1:]**2,C.t[1:])   # far part unchanged
    out=dict(case=case,mu=mu,coef={k:mp.nstr(v,12) for k,v in coef.items()},b0_rel=o['b0'],
             Q_by_V=[(r['V'],r['Qform'],r['ratio'],r['arch'],r['prime'],r['pole'],r['N2'],r['parseval'],r['arch_tail']) for r in rows],
             ratio_W_over_onesided=o['ratio'], kappa_leak=o['ratio']/2, pred_D_actual=o['pred'],
             R2=o['R2'], rem2_J={J:pj[J]['rem2'] for J in pj}, condG=P['condG'],
             ratio_Pi=o['Qform']/R2pi, pred_Pi=Pw_pi/R2pi,
             Wext_abs=mp.nstr(mp.mpf(Wext),8), leak2_abs=mp.nstr(mp.mpf(leak2),8),
             leak_exact=mp.nstr(leak_exact,8) if leak_exact is not None else None,
             D4=D4(mu), half_D4=D4(mu)/2, log2mu=np.log(2*mu))
    if case.startswith('core'): out['fhat0']=mp.nstr(fh0,5)
    print(json.dumps(out,default=str,indent=1),flush=True)
    res[case]=out
json.dump(res,open(f'res_mu{mu}_{"_".join(cases)}.json','w'),default=str,indent=1)
