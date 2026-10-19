# F0_TEST_001 step 5: pure gauge elements phi in G_T (radical of the form). Checks (i) Theorem D / thm:ext-half gives
# W_ext[r_phi] = Arch + 2AB - F'(0) = 0, an exact-zero test of the pipeline; (ii) sign of F''_phi(0) and of the cross term
# with r*, i.e. whether Lemma F can hold on the whole gauge class or only on the min-leak representative. Double precision
# (r_phi is O(1), no cancellation). NUMERICO.
import json,math,sys
import numpy as np
import step3_F as s3
lam=math.sqrt(15)
v,wv=np.polynomial.legendre.leggauss(3000)       # v = lam*u in [-1,1]
def make_phi(k):
    # phi(v) = (1-v^2)^4 (v^2 - kappa v^{2k}), phi(0)=0, int phi = 0, C^3 at |v|=1
    b=(1-v**2)**4; kap=np.sum(wv*b*v**2)/np.sum(wv*b*v**(2*k)); return b*(v**2-kap*v**(2*k))
def rho_of(ph):
    def f(om):
        out=np.empty_like(om)
        for i in range(0,len(om),2000):
            o=om[i:i+2000]; out[i:i+2000]=(np.cos(2*np.pi*lam*o[:,None]*v[None,:]/lam)*(wv*ph)[None,:]).sum(1)/lam
        return out
    return f
eps=[0.0,0.01,-0.01,0.1,0.186]
res={}
for k in [2,3]:
    ph=make_phi(k); f=rho_of(ph)
    for X in [30,60]:
        o=s3.run(X,eps,dy=1.5e-5,rhof=f)
        print(f"phi_k={k} X={X} F0={o['F0']:.6e} F'={o['F1']:.6e} F''={o['F2']:.6e} arch={o['arch']:.6e} 2AB={o['twoAB']:.6e} W_ext={o['W_ext']:.3e} (W_ext/F0={o['W_ext']/o['F0']:.2e})",flush=True)
        res[f'{k}_{X}']={kk:o[kk] for kk in ['F0','F1','F2','arch','twoAB','W_ext','A','B']}
json.dump(res,open('step5_gauge.json','w'),indent=1)
