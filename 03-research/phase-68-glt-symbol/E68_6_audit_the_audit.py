"""
E68.6 -- audit the audit (E68.5). Was the symbol's 'false negative' a detector failure,
or edge contamination in the NAIVE full-band average (mean over ALL positions incl. corners)?

Compare, for zeta at gauges where E68.5 failed:
  naive band symbol      : t_d = mean_{all j} M[j,j+d]
  interior band symbol   : t_d = mean_{j in [trim, N-1-trim-|d|]} M[j,j+d]   (drop corners)
Ground truth: ind_-(A_N-P_lambda)=0 at all gauges (verified). A faithful symbol should be >= 0.
"""
import os,sys,numpy as np,mpmath as mp
H8=os.path.abspath("../../04-papers/P52-riemann-proof-audit"); sys.path.insert(0,H8)
import h8lab as H
mp.mp.dps=40
def mp2np(M): return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)],dtype=complex)
def band_sym(M,th,trim):
    N=M.shape[0]; s=np.zeros(len(th),dtype=complex)
    for d in range(-(N-1),N):
        lo=max(0,-d)+trim; hi=min(N,N-d)-trim
        if hi-lo<1: continue
        s+=np.mean([M[j,j+d] for j in range(lo,hi)])*np.exp(1j*d*th)
    return np.real(s)
def run(t0,N=14):
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf('1'))
    A_N,Plam,J=H.arithmetic_jets(z0,N,None)
    A=mp2np(H.herm(A_N)); P=mp2np(H.herm(Plam))
    th=np.linspace(-np.pi,np.pi,3000)
    Jn=mp2np(H.herm(J)); Jn=0.5*(Jn+Jn.conj().T); k=int(np.sum(np.linalg.eigvalsh(Jn)<-1e-9))
    row=f"t0={t0:4d} ind_-={k} |"
    for trim in (0,2,3,4):
        g=band_sym(A,th,trim)-band_sym(P,th,trim)
        row+=f"  trim{trim}:min={g.min():+8.3f}"
    print(row)
print("min of (sigma_A - sigma_P) for zeta; faithful => >= 0.  ind_- is ground truth (=0).")
for t0 in (30,50,100,200,400): run(t0)
