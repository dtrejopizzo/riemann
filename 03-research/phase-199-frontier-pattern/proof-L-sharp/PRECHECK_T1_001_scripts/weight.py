import numpy as np
from wext import wfun, D4
om=np.concatenate([1+np.logspace(-8,0,200001)[:-1],np.linspace(2,1e5,4000001)])
for mu in [10,15,20,30]:
    w=wfun(om,mu); i=np.argmin(w)
    print(mu,'min w=%.7f at ω=%.6f  log2μ=%.7f  D4=%.4f  ½D4=%.4f  w(1.05)=%.3f w(1.5)=%.3f w(2)=%.3f w(3)=%.3f w(10)=%.3f'%(w[i],om[i],np.log(2*mu),D4(mu),D4(mu)/2,*wfun(np.array([1.05,1.5,2.0,3.0,10.0]),mu)))
