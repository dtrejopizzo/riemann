import sys; sys.path.insert(0,'..')
import align_band as A, numpy as np
from multiprocessing import Pool
from scipy.optimize import minimize_scalar
def w(a):
    T,t0=a; ts=np.arange(t0-0.1,t0+0.1001,0.02); mv=[A.margin(T,t,0.25)[0] for t in ts]; j=int(np.argmin(mv))
    r=minimize_scalar(lambda t:A.margin(T,t,0.25)[0],bounds=(ts[max(j-1,0)],ts[min(j+1,len(ts)-1)]),method='bounded',options={'xatol':2e-5})
    return T,t0,r.x,r.fun,A.margin(T,r.x,0.125)[0]
jobs=[(3.75,26777.34),(3.75,28327.24),(4.0,28327.255),(4.0,33874.77),(4.0,25227.29),(3.5,18301.58)]
with Pool(6) as p:
    for r in p.imap_unordered(w,jobs): print(r,flush=True)
