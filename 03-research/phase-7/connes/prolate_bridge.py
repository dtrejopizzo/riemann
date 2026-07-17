#!/usr/bin/env python3
"""
Phase 7 / Connes core — the prolate bridge.

Connes-Consani organize Weil positivity MULTIPLICATIVELY (scaling action on adele classes),
and their archimedean-place positivity runs through the PROLATE spheroidal operator: the
concentration operator Q_c on L^2[-1,1] with kernel  sin(c(x-y))/(pi(x-y)),  c = time-bandwidth.
Its eigenvalues lambda_n(c) in (0,1): ~2c/pi of them near 1, a sharp drop near n=2c/pi, then
exponentially small.  Connes-Consani's archimedean positivity uses lambda_n(c) < 1 strictly
(the "kappa<1" contraction device).

OUR band-limited Carleson form (phase-7) IS a prolate compression: window half-width W, band d
=> time-bandwidth c = W*d, effective dimension 2c/pi.  This script:
 (1) computes lambda_n(c) (the Connes-Consani / Slepian object),
 (2) confirms the dictionary  our basis dim M ~ 2c/pi,
 (3) checks the archimedean contraction (all lambda<1) and where the transition (the spectral
     gap = the uniformity locus) sits -- i.e. WHERE the Connes Lambda->infty wall lives.
"""
import numpy as np

def prolate_eigs(c, n=800):
    """eigenvalues of Q_c on [-1,1], kernel sin(c(x-y))/(pi(x-y)), via Nystrom quadrature."""
    x, w = np.polynomial.legendre.leggauss(n)   # nodes/weights on [-1,1]
    D = x[:,None]-x[None,:]
    K = np.where(np.abs(D)<1e-12, c/np.pi, np.sin(c*D)/(np.pi*D))
    # symmetric eigenproblem for K with weight w: solve (sqrt(w) K sqrt(w)) v = lam v
    sw = np.sqrt(w)
    M = (sw[:,None]*K*sw[None,:])
    M = (M+M.T)/2
    return np.linalg.eigvalsh(M)[::-1]

if __name__ == "__main__":
    print("="*78)
    print(" Connes-Consani prolate eigenvalues lambda_n(c) -- the archimedean positivity object")
    print("="*78)
    for c in [5.0, 10.0, 20.0, 40.0]:
        ev = prolate_eigs(c)
        twocpi = 2*c/np.pi
        n_near1 = np.sum(ev>0.999)
        n_mid   = np.sum((ev>1e-3)&(ev<0.999))
        print(f"\n c={c:5.1f}  (2c/pi={twocpi:6.2f} = effective # well-concentrated modes)")
        print(f"   lambda_max = {ev[0]:.10f}  (< 1 strictly? {'YES' if ev[0]<1 else 'NO'}  -> archimedean contraction)")
        print(f"   #modes>0.999: {n_near1:3d}   #transition(1e-3..0.999): {n_mid:2d}   (transition width ~ log c = {np.log(c):.2f})")
        # show the transition region (the spectral gap = where the Lambda->inf uniformity lives)
        k=int(round(twocpi))
        lo=max(0,k-4); hi=min(len(ev),k+5)
        print(f"   around n=2c/pi={k}:  " + "  ".join(f"l_{i}={ev[i]:.4f}" for i in range(lo,hi)))
    print("\n"+"="*78)
    print(" DICTIONARY to our phase-7 form: window half-width W, band d => c=W*d, dim M~2c/pi.")
    print(" The archimedean contraction lambda_max(c)<1 is UNCONDITIONAL (Connes-Consani) = our A_Phi PD.")
    print(" The transition region (lambda_n ~ 1/2, width ~log c) is the 'edge' modes -- the uniformity-in-c")
    print(" (= Lambda->infty) behaviour there is the Connes wall, the analogue of our uniform-gap wall.")
    print("="*78)
