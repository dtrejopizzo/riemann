import mpmath as mp
mp.mp.dps=40
def arch_iv(tau):
    return mp.re(mp.digamma(mp.mpf(1)/4+mp.mpc(0,1)*tau/2))-mp.log(mp.pi)
def sig(tau,terms):
    return arch_iv(tau)-2*sum(w*mp.cos(tau*mp.log(n)) for n,w in terms)
L2=mp.log(2)/mp.sqrt(2); L3=mp.log(3)/mp.sqrt(3)
cases={'0.5log3':(mp.log(3)/2,[(2,L2)]), 'log2':(mp.log(2),[(2,L2),(3,L3)])}
for lab,(T,tm) in cases.items():
    x=mp.pi/(2*T)
    print(f"{lab}: pi/(2T)={mp.nstr(x,15)}  sigma_T(pi/2T)={mp.nstr(sig(x,tm),15)}  sigma_T(0)={mp.nstr(sig(0,tm),15)}")
# interval check with mpmath.iv
mp.iv.dps=30
def arch_v(tau):
    # Re psi(1/4+i tau/2) - log pi via series: -gamma + sum_{k>=0} (1/(k+1) - (k+1/4)/((k+1/4)^2+ (tau/2)^2)) - log pi
    y=tau/2; s=mp.mpf(0)
    K=200000
    tot=mp.mpf(0)
    for k in range(K):
        a=mp.mpf(k)+mp.mpf(1)/4
        tot+= mp.mpf(1)/(k+1) - a/(a*a+y*y)
    # tail estimate
    return -mp.euler+tot-mp.log(mp.pi), (y*y)/(mp.mpf(K)**2)  # crude tail bound
for lab,(T,tm) in cases.items():
    x=mp.pi/(2*T)
    v,tail=arch_v(x)
    s=v-2*sum(w*mp.cos(x*mp.log(n)) for n,w in tm)
    print(f"{lab}: series value of sigma(pi/2T) = {mp.nstr(s,15)}  (tail bound {mp.nstr(tail,4)})")
# prolate lambda_0(c)
import numpy as np
def lam0(c):
    x,w=np.polynomial.legendre.leggauss(400)
    K=np.sinc((np.subtract.outer(x,x))*c/np.pi)*c/np.pi
    W=np.sqrt(w)
    M=W[:,None]*K*W[None,:]
    return np.linalg.eigvalsh(M)[-1]
for lab,T,t0 in [('0.5log2',0.5*np.log(2),6.289836),('0.5log3',0.5*np.log(3),3.305011),('log2',np.log(2),2.277506)]:
    c=T*t0
    print(f"{lab}: c=T*tau_0={c:.6f}  lambda_0(c)={lam0(c):.8f}  elementary bound 2c/pi={2*c/np.pi:.6f}")
print("lambda_0 for far wells at log2 (half-widths):")
for l,r in [(4.8160,7.2717),(9.6662,11.9658),(16.2511,18.4938),(27.5578,28.9380),(45.1491,46.1291)]:
    c=np.log(2)*(r-l)/2
    print(f"  [{l},{r}] c={c:.4f} lambda_0={lam0(c):.6f}")
