"""r6a_02: accuracy of the node-only sign rule as a function of |J|, and the
arena bound N*(T) = #{k : lambda_{2k+1} <= A_T} from the PROVED ceiling
lambda_{2k+1}(A_inf|P_T) <= m((2k+3)pi/2T).  Reads r6a_01.json."""
import json, os, numpy as np
from scipy.special import psi as digamma
HERE=os.path.dirname(os.path.abspath(__file__))
d=json.load(open(os.path.join(HERE,'r6a_01.json')))
m=lambda tau: np.real(digamma(0.25+0.5j*tau))-np.log(np.pi)
out={}
for key in d:
    if key=='growth': continue
    v=d[key]; rec={}
    for n,a in v['atoms'].items():
        J=np.abs(np.array(a['J'])).ravel(); S=np.sign(np.array(a['J'])).ravel(); P=np.array(a['pred']).ravel()
        ok=(S==P)
        rows=[]
        for thr in [0.0,0.02,0.05,0.10,0.15,0.20]:
            sel=J>=thr
            rows.append([thr,int(sel.sum()),int((ok&sel).sum()),float((ok&sel).sum()/max(1,sel.sum()))])
        rec[n]=dict(by_threshold=rows,
                    massfrac_correct=float(J[ok].sum()/J.sum()))
    out[key]=rec
# arena bound
for T, AT in [(np.log(2), 0.98026+1.26864), (0.5*np.log(3), 0.98026)]:
    # A_T = sum of v_n over the contact set N_T = {n : 0 < log n < 2T}
    # (at T = 1/2 log 3 the only contact is n = 2; log 3 = 2T is excluded)
    # count k>=0 with m((2k+3)pi/(2T)) <= A_T  (proved ceiling)
    ks=[k for k in range(0,200) if m((2*k+3)*np.pi/(2*T))<=AT]
    out['arena_T%.6f'%T]=dict(A_T=AT, kmax=(max(ks)+1 if ks else 0),
        tau_star=float(np.exp(AT)*2*np.pi), note='#even modes with lambda<=A_T is >= kmax')
json.dump(out,open(os.path.join(HERE,'r6a_02.json'),'w'),indent=1)
print(json.dumps(out,indent=1))
