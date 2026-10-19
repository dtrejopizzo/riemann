import sys, numpy as np, json
from scipy.optimize import brentq
from t2001_typeI_search import data
K=int(sys.argv[1]); step=float(sys.argv[2])
Tg=np.round(np.arange(0.05,1.2001,0.01),4)
def first_zero(key,s2,s3):
    v=[data(T,K,s2,s3)[key] for T in Tg]
    for j in range(len(Tg)-1):
        if v[j]>0 and v[j+1]<=0:
            return brentq(lambda T: data(T,K,s2,s3)[key],Tg[j],Tg[j+1],xtol=1e-10)
    return None
res=[]
S=np.round(np.arange(0,4.0001,step),4)
for s2 in S:
    for s3 in S:
        Ts=first_zero('lam',s2,s3); Tm=first_zero('mu2',s2,s3)
        row=dict(s2=s2,s3=s3,Ts=Ts,Tm=Tm)
        if Ts: row['at_Ts']=data(Ts,K,s2,s3)
        if Tm: row['at_Tm']=data(Tm,K,s2,s3); row['pre_Tm']=data(Tm-1e-4,K,s2,s3)
        res.append(row); print(json.dumps(row),flush=True)
