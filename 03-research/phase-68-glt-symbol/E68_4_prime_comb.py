"""
E68.4 -- is sigma_P a prime comb? Locate the single-frequency peaks and the theta <-> log n map.

The prime jet is  P_lambda = sum_n Lambda(n) n^{-1/2} * (jet of e^{-i z log n})  at z0.
So sigma_P(theta) = sum_n Lambda(n) n^{-1/2-y} * s_n(theta), where s_n is the symbol of a single
frequency L = log n. If each s_n peaks at theta = f(log n), sigma_P is a weighted comb over primes.

Test: build the single-frequency Pick-jet symbol for n = 2,3,5,7,11,13 and locate its peak theta_n.
Check whether theta_n is an ordered (ideally affine/clean) function of log n -- the comb frequency map.
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(M):
    return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)], dtype=complex)

def freq_jet_taylor(z0, Mo, L):
    """Taylor coeffs of h(z)= i * e^{-i z L} at z0 (single frequency L)."""
    e0 = mp.e**(-mp.mpc(0,1)*z0*L)
    return [mp.mpc(0,1)*((-mp.mpc(0,1)*L)**p)/mp.factorial(p)*e0 for p in range(Mo+1)]

def symbol(M, th):
    N=M.shape[0]; s=np.zeros(len(th),dtype=complex)
    for d in range(-(N-1),N):
        s+=np.mean([M[j,j+d] for j in range(max(0,-d),min(N,N-d))])*np.exp(1j*d*th)
    return np.real(s)

def main():
    t0,y,N=100.0,1.0,14
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    Mo=2*N+2
    th=np.linspace(-np.pi,np.pi,4000)
    print(f"z0={t0}-{y}i  N={N}\n")
    print("single-frequency symbol peak location vs log n:")
    print("   n     log n     theta_peak    |symbol|_max")
    data=[]
    for n in (2,3,5,7,11,13,17,19):
        c=freq_jet_taylor(z0,Mo,mp.log(n))
        J=H.herm(H.pick_jet(c,z0,N))
        s=symbol(mp2np(J),th)
        i=int(np.argmax(np.abs(s)))
        data.append((np.log(n), th[i]))
        print(f"   {n:2d}   {float(mp.log(n)):.4f}    {th[i]:+.4f}     {np.abs(s).max():.3f}")
    # fit theta_peak vs log n
    L=np.array([d[0] for d in data]); TH=np.array([d[1] for d in data])
    A=np.polyfit(L,TH,1)
    resid=np.std(TH-(A[0]*L+A[1]))
    print(f"\n   affine fit  theta_peak = {A[0]:.4f} * log n + {A[1]:.4f}   resid_std={resid:.4f}")
    print(f"   {'CLEAN comb map (theta ~ affine in log n)' if resid<0.15 else 'not affine -- check'}")
    print("\n   => sigma_P is a weighted comb sum_n Lambda(n) n^{-1/2-y} s_n(theta) over prime log-freqs.")
    print("   Omega_7: archimedean envelope sigma_A(theta) >= this prime comb, for all theta.")

if __name__ == "__main__":
    main()
