import sys,json
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts')
import numpy as np
from scipy.linalg import toeplitz
import tk_common as tk
d=json.load(open('r3b_enclosure_0.68_M24.json'))
T=d['T']; M=d['M']; t0=d['tau0']
q=np.array(d['q_re'])+1j*np.array(d['q_im'])
parts=tk.make_S_parts(T)[:3]
for nf in (1<<16,1<<18,1<<20):
    cs=tk.coeff_families(T,M,t0,nf,parts)
    Ms=[toeplitz(np.conj(c),c) for c in cs]
    print(nf,"|c| g0 max %.3e  g1 max %.3e"%(np.abs(cs[1]).max(),np.abs(cs[2]).max()),
          " a=%.8e b0=%.6e b1=%.6e"%(np.vdot(q,Ms[0]@q).real,np.vdot(q,Ms[1]@q).real,np.vdot(q,Ms[2]@q).real))
print("norm q",np.linalg.norm(q))
