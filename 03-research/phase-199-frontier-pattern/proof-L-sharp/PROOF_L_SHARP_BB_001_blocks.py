# BB_001 step 3 (NUMÉRICO, double): off-diagonal blocks Q·X·P_V for X = G, C, Ar (singular values), i.e. how strongly the
# comb and the archimedean part separately, and the full form, couple V_50 to V_50^⊥. Double precision: G-block values
# below ~1e-15 are at the rounding floor (the p-direction value 1.7e-35 is from step 1, arb).
import os,numpy as np,json
from pathlib import Path
SP=Path(os.environ['SP'])/'bb'; G=np.load(SP/'G.npy'); C=np.load(SP/'C.npy'); B=np.load(SP/'Bas.npy'); Ar=G+C
U,_=np.linalg.qr(B); d=G.shape[0]; Z=np.linalg.svd(np.eye(d)-U@U.T)[0][:,:d-B.shape[1]]
o={nm:[float(x) for x in np.linalg.svd(Z.T@X@U,compute_uv=False)[[0,1,2,4,9,19,29,49]]] for nm,X in (('G',G),('C',C),('Ar',Ar))}
o['sv index']=[1,2,3,5,10,20,30,50]; json.dump(o,open(SP/'blocks.json','w'),indent=1); print(o)
