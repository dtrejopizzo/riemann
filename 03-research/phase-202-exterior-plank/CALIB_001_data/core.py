# núcleo común CALIB_R1: splines de ρ, ρ_pro, Δr_out; grilla y = log s; forma bilineal de 𝒲 por par de dilatados. NUMÉRICO.
import json,math,os
import numpy as np
from scipy.interpolate import CubicSpline
from scipy.special import digamma
F0='/home/trabajo/Documentos/research/riemann/03-research/phase-200-sign-object/F0_TEST_001_data/'
lam=math.sqrt(15); binf=float(digamma(0.25))-math.log(math.pi)
Rs=json.load(open(F0+'rho_sigma.json')); nS=len(Rs['rho']); sg=Rs['dsig']*np.arange(nS)
R1=json.load(open(F0+'rho.json')); n1=len(R1['rho']); o1=R1['omega0']+R1['dom']*np.arange(n1)
R2=json.load(open(F0+'rho_60_240.json')); n2=len(R2['rho']); o2=R2['omega0']+R2['dom']*np.arange(n2)
RHO=np.concatenate([np.array([float(x) for x in R['rho']])*1e35 for R in (Rs,R1,R2)])
PRO=np.load(os.path.join(os.path.dirname(os.path.abspath(__file__)),'rho_pro.npy'))
def make(vals):
    a,b,c=vals[:nS],vals[nS:nS+n1],vals[nS+n1:]
    sS,s1,s2=CubicSpline(sg,a),CubicSpline(o1,b),CubicSpline(o2,c)
    def f(x):
        x=np.asarray(x,float); out=np.zeros_like(x)
        m=(x>=1)&(x<2); out[m]=sS(np.sqrt(x[m]-1)); m=(x>=2)&(x<=60); out[m]=s1(x[m]); m=(x>60)&(x<=240); out[m]=s2(x[m]); return out
    return f
FUN={'rho':make(RHO),'pro_all':make(PRO[:,0]),'pro04':make(PRO[:,2]),'dr_out':make(RHO-PRO[:,0]),'dr_out04':make(RHO-PRO[:,2])}
class Grid:
    def __init__(s,X=240.0,DY=1.5e-5):
        s.X=X; s.DY=DY; s.ys=np.arange(0,math.log(X)+DY/2,DY); s.s=np.exp(s.ys)
        wq=np.full(len(s.s),DY); wq[0]=wq[-1]=DY/2; s.wq=wq*s.s; s.sq=np.sqrt(lam*s.s)
        v=np.arange(len(s.s))*DY; nu=np.zeros(len(v)); nu[1:]=np.exp(-v[1:]/2)/(-np.expm1(-2*v[1:])); s.nu=nu
        s.tailnu=sum(math.exp(-(0.5+2*k)*v[-1])/(0.5+2*k) for k in range(200)); s.M=1<<int(math.ceil(math.log2(2*len(v))))
    def dil(s,f,n):  # f(n s) on s>=1 truncated at n s <= X
        a=n*s.s; out=np.zeros(len(a)); k=np.searchsorted(a,s.X,side='right'); out[:k]=f(a[:k]); return out
    def ip(s,a,b): return lam*np.sum(s.wq*a*b)
    def A(s,a): return lam*np.sum(s.wq*a)
    def B(s,a): return np.sum(s.wq*a/s.s)
    def arch(s,a,b):
        fa=np.fft.rfft(s.sq*a,s.M); fb=np.fft.rfft(s.sq*b,s.M)
        c=np.fft.irfft(np.real(np.conj(fa)*fb),s.M)[:len(a)]*s.DY  # symmetrised cross-correlation
        c0=c[0]; integ=(c0-c)*s.nu; integ[0]=0
        return binf*c0+2*(np.sum(integ)-integ[-1]/2)*s.DY+2*c0*s.tailnu
    def bil(s,a,b,la,lb,parts=False):
        ar=s.arch(a,b); po=s.A(a)*s.B(b)+s.A(b)*s.B(a); cb=-(la+lb)*s.ip(a,b)
        return (ar,po,cb) if parts else ar+po+cb
