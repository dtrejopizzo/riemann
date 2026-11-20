import os; HERE=os.path.dirname(os.path.abspath(__file__))
import numpy as np, pickle, scipy.special as sp, scipy.linalg as sl, mpmath as mp, sys
P=pickle.load(open(''+HERE+'/coef08.pkl','rb')); De=P['De']; kl=np.array(P['kl']); lam=P['lam']; T=0.8; c=2*np.pi*lam**2
Z=np.load(os.environ['NPZ']); GH,DH,Cb,Jn,kH=Z['GH'],Z['DH'],Z['Cb'],Z['Jn'],Z['kH']
SMAX=float(sys.argv[1]) if len(sys.argv)>1 else 200.
fmax=2*np.pi*lam*SMAX; dt=np.pi/(4*fmax); t=np.arange(np.log(lam),np.log(SMAX),dt); s=np.exp(t); nt=len(t)
L=np.array([(-1)**(l//2)*np.sqrt(l+.5)*2*np.sqrt(lam)*sp.spherical_jn(l,2*np.pi*lam*s) for l in kl]).T  # nt x nl
def uk(k):  # u_k = eps_k * F(psi_k 1)(s), s>lam
    return (-1)**(k//2)*(L@De[k//2])
U={k:uk(k) for k in kH}
print('nt',nt,'check |u_k|^2 = d_k (2*int_lam^inf):',[(k,round(2*np.trapz(U[k]**2*s,t),4),round(DH[i],4)) for i,k in enumerate(kH[:4])])
# m(tau)
tg=np.r_[np.linspace(0,20,4001),np.geomspace(20.01,1.3*np.pi/dt,4000)]; mg=np.array([float(mp.re(mp.digamma(0.25+0.5j*x))-mp.log(mp.pi)) for x in tg])
mm=lambda x: np.interp(x,tg,mg)
NPAD=1<<19
tau=2*np.pi*np.fft.rfftfreq(NPAD,dt); sel=tau<0.5*np.pi/dt; tau=tau[sel]; dtau=tau[1]-tau[0]; mt=mm(tau); TMX=tau[-1]
def chirps(u,NMAX):
    G=np.exp(t/2)*u
    out=[]
    for N in range(1,NMAX+1):
        i0=np.searchsorted(t,np.log(N*lam))
        if i0>=nt-10: break
        g=np.zeros(NPAD); g[:nt-i0]=G[i0:]*dt; g[0]*=.5
        # F_N(x)=N^{-1/2} G(t), t=log N - x ; FT over x  => N^{-1/2} e^{-i tau log N} * int G(t) e^{i tau t} dt
        Fh=np.conj(np.fft.rfft(g))[sel]*np.exp(1j*tau*t[i0])   # int_{t>=t_i0} G e^{i tau t}
        Fh*=N**-0.5*np.exp(-1j*tau*np.log(N))
        J=N**-0.5*G[i0]  # F_N(-T) jump (approximately, grid start)
        out.append((N,Fh,J,i0))
    return out
def ledger(u,NMAX=80,verbose=False):
    ch=chirps(u,NMAX); n=len(ch); G=np.exp(t/2)*u
    A=np.zeros((n,n)); C=np.zeros((n,n)); Atail=np.zeros((n,n))
    for a,(N,F,J,i0) in enumerate(ch):
        for b,(N2,F2,J2,i02) in enumerate(ch):
            if b<a: continue
            v=np.real(F*np.conj(F2)); A[a,b]=(1/np.pi)*np.trapz(mt*v,dx=dtau)
            # tail tau>TMX: |F|^2 ~ J J' cos(tau log(N'/N))/tau^2 ; include only diagonal-ish analytically
            if N==N2: Atail[a,b]=(1/np.pi)*J*J2*(np.log(TMX/2)+1-np.log(np.pi))/TMX
            C[a,b]=(1/np.pi)*np.trapz(v,dx=dtau)+((1/np.pi)*J*J2/TMX if N==N2 else 0)
            A[b,a]=A[a,b]; C[b,a]=C[a,b]; Atail[b,a]=Atail[a,b]
    return ch,A+Atail,C,Atail
def polar(u,NMAX=200):
    # A(Tu)=sum_N int_{N lam}^inf u(s)/s ds ; B(Tu)=sum_N N^{-1} int_{N lam}^inf u(s) ds  (s=e^t, ds=s dt)
    cu1=np.cumsum((u)[::-1])[::-1]*dt; cus=np.cumsum((u*s)[::-1])[::-1]*dt
    A=0;B=0
    for N in range(1,NMAX):
        i0=np.searchsorted(t,np.log(N*lam))
        if i0>=nt: break
        A+=cu1[i0]; B+=cus[i0]/N
    return A,B
