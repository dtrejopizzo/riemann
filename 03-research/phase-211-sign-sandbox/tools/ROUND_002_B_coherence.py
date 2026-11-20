import numpy as np
from scipy.special import pro_rad1
from scipy.integrate import quad
import sys
c=float(sys.argv[1]); X=float(sys.argv[2])
# H1^w for Lambda: sum_{k<=t} log k / k
def H1(t): 
    k=np.arange(1,int(np.floor(t))+1); return np.sum(np.log(k)/k)
t=np.concatenate([1+np.geomspace(1e-7,1,4000)[:-1], np.linspace(2,X,int((X-2)*c*3))])
R={n:np.array([pro_rad1(0,n,c,x)[0] for x in t]) for n in [0,4,8,12]}
f=np.array([H1(x) for x in t])
def trap(y):
    m=np.isfinite(y); return np.trapz(y[m],t[m])
th=lambda tt: np.arccos(1/tt)
print("nan",sum(~np.isfinite(R[4])))
for (j,k) in [(4,4),(8,8),(4,8),(0,4),(4,12),(0,8),(0,0)]:
    num=trap(f*R[j]*R[k])*c*c*2
    pred=quad(lambda a: H1(1/np.cos(a))*np.cos((j-k)*a),0,th(X),limit=400)[0]
    print(j,k,num,pred)
