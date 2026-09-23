import math,sys,numpy as np,core
K=int(sys.argv[1]); a=float(sys.argv[2]); b=float(sys.argv[3]); n=int(sys.argv[4])
Ts=np.linspace(a,b,n); L=[]
for T in Ts:
    l,p,_=core.lam_min(T,K); L.append(l); print(f"{T:.5f} {l: .10e} {p}"); sys.stdout.flush()
L=np.array(L); lg=np.log(L)
print("# c(T) central differences")
for i in range(1,n-1):
    print(f"{Ts[i]:.5f}  c={-(lg[i+1]-lg[i-1])/(Ts[i+1]-Ts[i-1]):.3f}")
