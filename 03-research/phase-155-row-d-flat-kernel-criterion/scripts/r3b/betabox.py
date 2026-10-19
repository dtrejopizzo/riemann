import sys
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-155-row-d-flat-kernel-criterion/scripts')
import numpy as np, json
import r2_c_beta_bound as bb
out={}
AT=2*np.log(2)/np.sqrt(2.0)+2*np.log(3)/np.sqrt(3.0)
for nm,T in [("0.68",0.68),("log2",float(np.log(2)))]:
    r=bb.run(T,AT); out[nm]=r
    print(nm,"A_T=%.8f r0=%.6e V*=%.6f inside=%s B=%.1f"%(r['A_T'],r['r0'],r['Vstar'],r['zero_inside'],r['B_c_ge_0']))
json.dump(out,open('r3b_beta_box.json','w'),indent=1)
