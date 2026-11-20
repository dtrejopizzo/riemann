import os; HERE=os.path.dirname(os.path.abspath(__file__))
import sys, numpy as np
Rarg=sys.argv[1]; Nbarg=sys.argv[2]; p=int(sys.argv[3])
exec(open(''+HERE+'/tail.py').read())
sys.argv=['x',Rarg,Nbarg,'0.8']; exec(open(''+HERE+'/cellR.py').read().split("print(f'R=")[0])
C=np.array([np.trapz(E*(wt*fun[k])[None,:],z,axis=1) for k in ["f(0)","f(lam)","A","B"]]).T
Qn=sl.null_space(C.T); ev,V=np.linalg.eigh(Qn.T@Q_@Qn); Fz=(Qn@V[:,0])@E
xs=xi[::-1]; ut=(xi**-0.5*Fz)[::-1]
x=np.linspace(0,lam,2001)
f0=np.array([2*np.trapz(ut*np.cos(2*np.pi*xs*q),xs) for q in x])*(1-(x/lam)**2)**p
gs=[(1-(x/lam)**2)**3*(x/lam)**(2*j) for j in range(4)]
Tv=0.8
def funcs(f):
    fi=lambda y: np.interp(y,x,f,right=0)
    out=[f[0], 2*np.trapz(f,x)]
    xx=np.linspace(-Tv,Tv,8001); Ef=np.zeros_like(xx)
    for n in range(1,6): Ef+=fi(n*np.exp(xx))
    Ef*=np.exp(xx/2)
    out+= [np.trapz(Ef*np.exp(xx/2),xx), np.trapz(Ef*np.exp(-xx/2),xx)]
    return np.array(out), xx, Ef
M=np.array([funcs(g)[0] for g in gs]).T; r=funcs(f0)[0]
coef=np.linalg.solve(M,-r); f=f0+sum(cj*g for cj,g in zip(coef,gs))
cons,xx,Ef=funcs(f)
# Levy a_T on window
dz=xx[1]-xx[0]; n=len(xx); c=np.correlate(Ef,Ef,'full')*dz; c=c[n-1:]; u_=np.arange(n)*dz
Kf=lambda u:1/(2*np.sinh(u/2))+1/(2*np.cosh(u/2)); Kt=lambda q:-np.log(np.tanh(q/4))+np.pi-2*np.arctan(np.exp(q/2))
arch=-5.3721834*c[0]+np.trapz(np.r_[0,(c[0]-c[1:])*Kf(u_[1:])],u_)+c[0]*Kt(u_[-1])
comb=sum(2*np.log(q)/np.sqrt(q**a)*np.interp(a*np.log(q),u_,c) for q in [2,3] for a in range(1,3) if a*np.log(q)<u_[-1])
aT=arch-comb
# tail
ff=lambda q: 2*np.trapz(f*np.cos(2*np.pi*q*x),x)
uu=np.array([ff(q) for q in s]); nu=2*np.trapz(uu**2*s,t)
ch,A_,C_,At=ledger(uu,40); Ns=np.array([q[0] for q in ch]); lN=np.log(Ns); B=A_-(lN[:,None]+lN[None,:])*C_
PA,PB=polar(uu); print("polar A,B",PA,PB,"lam*(W+2AB)",lam*(B.sum()+2*PA*PB))
print(f"R={Rarg} p={p} cell mu={ev[0]:.4f} | constraints(f0,intf,A,B)={np.round(cons,6)} corr coef {np.round(coef,3)} | a_T(Ef)={aT:.5f} |Ef|^2={c[0]:.4f} a/|Ef|^2={aT/c[0]:.4f} | |u|^2={nu:.4f} W[Tu]={B.sum():.5f} lam*W={lam*B.sum():.5f} B11={B[0,0]:.4f}")
