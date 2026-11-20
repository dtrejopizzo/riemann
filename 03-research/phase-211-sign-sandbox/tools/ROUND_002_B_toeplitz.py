import numpy as np
from sympy import factorint
Jmax=200000
def Lam(n):
    f=factorint(n); 
    return np.log(list(f)[0]) if len(f)==1 else 0.0
L=np.zeros(Jmax+1)
for n in range(2,Jmax+1): L[n]=Lam(n)
def W_of(w):  # (w*1)(n)
    W=np.zeros(Jmax+1)
    for q in range(2,Jmax+1):
        if w[q]: W[q::q]+=w[q]
    return W
def cellints(Wn):
    # H1^w(t)=sum_{k<=t}W(k)/k ; Toeplitz entries (2/pi) int_0^{pi/2} 2 H1(sec th) cos(4 d th) dth ; d=0..K
    n=np.arange(Jmax+1); Hc=np.cumsum(np.where(n>0,Wn/np.maximum(n,1),0))
    th=np.arccos(1/np.arange(1,Jmax+2))  # theta at t=J, J=1..Jmax+1
    out=[]
    for d in range(0,5):
        if d==0: prim=lambda a: a
        else: prim=lambda a: np.sin(4*d*a)/(4*d)
        seg=prim(th[1:])-prim(th[:-1])   # cell [J,J+1), J=1..Jmax
        out.append((2/np.pi)*2*np.sum(Hc[1:Jmax+1]*seg))
    return np.array(out)
def mat(e,K=4): return np.array([[e[abs(i-j)] for j in range(K)] for i in range(K)])
cases={'Lambda':L,'0.5Lambda':0.5*L,'a_3 (p=2 deleted)':np.where([n%2==0 for n in range(Jmax+1)],0,L),
       'a_7':np.array([0 if any(n%p==0 for p in (2,3,5)) else L[n] for n in range(Jmax+1)]),
       '1.5Lambda':1.5*L}
for k,w in cases.items():
    e=cellints(W_of(w)); M=mat(e)
    print(k,np.round(e,4),'eig',np.round(np.linalg.eigvalsh(M),4))
# comb-free: H and H log(2/sin 2th)
from scipy.integrate import quad
def Hsec(a):
    t=1/np.cos(a); return np.sum(1/np.arange(1,int(t)+1))
for name,g in [('T0=H',lambda a:Hsec(a)),('arch O(1)',lambda a:Hsec(a)*np.log(2/np.sin(2*a)))]:
    e=[(2/np.pi)*sum(quad(lambda a:g(a)*np.cos(4*d*a),np.arccos(1/J),np.arccos(1/(J+1)),limit=50)[0] for J in range(1,3000)) for d in range(5)]
    print(name,np.round(e,4),'eig',np.round(np.linalg.eigvalsh(mat(e)),4))
