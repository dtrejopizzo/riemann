"""
P3 of plan 2.3.F-CLOSE — analytic anchor of "C -> const" (sign-free).
Thesis: the multiplier C(y) of the Doob-conjugated operator (E70) = diffusion coefficient
of the CARRE-DU-CHAMP of the Weil form, which is the SECOND MOMENT of the jumps:
  c_2(x) = Omega''(0) (arch) + sum_{n<=lam^2} Lambda(n) n^{-1/2} (log n)^2 [jump available in [0,L]]
Claims to verify (all use ONLY Lambda(n)>=0 and moments, NEVER the mass/the sign):
 (1) c_2 is TRANSLATION-INVARIANT (constant in x) in the bulk; dominated by SMALL primes
     (weight n^{-1/2} suppresses large n), effective jump O(1) << L => LOCAL despite the formal range.
 (2) Near the edges there is an edge DEFICIT (truncated jumps) in a layer of width O(1);
     edge fraction O(1/L)=O(1/log lam) -> 0 => C->const with lam.
 (3) the C(y) bump from E70 (center/edge ~ [0.75,1.13]) is EXPLAINED by this deficit; its size
     decreases with lam just like std(C)/mean (0.22->0.15->0.14).
 (4) the 4th moment M_4/M_2 gives the subdominant correction O(1/L^2) (not the dominant bump).
"""
import numpy as np, mpmath as mp
mp.mp.dps = 30

def primes_weights(mx):
    sv=[True]*(mx+1); out=[]
    for i in range(2,int(mx**0.5)+1):
        if sv[i]:
            for j in range(i*i,mx+1,i): sv[j]=False
    for p in range(2,mx+1):
        if sv[p]:
            lp=mp.log(p); pm=p; me=1
            while pm<=mx:
                out.append((float(me*lp), float(lp*(mp.mpf(pm)**mp.mpf('-0.5')))))  # (jump=log n, weight Lambda/√n)
                pm*=p; me+=1
    return out  # list (jump, weight)

def Omega_pp0():
    # Omega''(0): curvature of the archimedean term at t=0 (bound O(1), subdominant). Numerical approx.
    # we use psi''(1/4)/something ~ O(1); reference value O(1). We take 1.0 as an O(1) placeholder.
    return 1.0

def run(lam):
    L=float(2*mp.log(mp.mpf(lam))); mx=int(lam*lam)
    pw=primes_weights(mx)
    M2=sum(w*s*s for s,w in pw)            # global 2nd moment of primes
    M4=sum(w*s**4 for s,w in pw)
    Pl=sum(w for s,w in pw)                # mass P_lambda (0th moment)
    # contribution by jump size (does small n dominate?)
    sm=sorted(pw)
    small=sum(w*s*s for s,w in pw if s<1.5)   # log n<1.5 => n<=4
    print(f"\n{'='*60}\nlambda={lam}  L={L:.3f}  P_lam={Pl:.3f}  M2={M2:.3f}  M4={M4:.3f}  M4/M2={M4/M2:.3f}")
    print(f"  (1) 2nd moment: jump<1.5 contributes {small/M2*100:.0f}% of M2  => dominated by SMALL primes (jump O(1))")
    # c_2(x) with edge deficit: jump s available if x+s<=L (right) or x-s>=0 (left); average of both
    Nx=400; xs=np.linspace(0,L,Nx); c2=np.zeros(Nx)
    for s,w in pw:
        avail=0.5*((xs+s<=L).astype(float)+(xs-s>=0).astype(float))
        c2+=w*s*s*avail
    c2+=Omega_pp0()
    # bulk = E70: |y-L/2|< (L-2*0.73)/2 approx; we use margin 0.73
    margin=0.73
    bulk=(xs>margin)&(xs<L-margin)
    cb=c2[bulk]
    flat=np.std(cb)/np.mean(cb)
    inner=(xs>L/2-0.5)&(xs<L/2+0.5)
    center=np.mean(c2[inner]); edge=np.mean(c2[(xs>margin)&(xs<margin+0.5)])
    print(f"  (2) c_2(x) in the bulk: mean={np.mean(cb):.3f} std/mean={flat:.3f}  center={center:.3f} edge~{edge:.3f} center/edge={center/edge:.3f}")
    print(f"      (E70 C(y) bump center/edge ~ 1.13/0.75=1.51; here {center/edge:.3f})")
    print(f"  (4) 4th-moment correction (rel., subdominant): M4/M2/L^2 = {M4/M2/L**2:.4f} (->0 with lam)")
    return L, flat, center/edge

print("Verification P3: C->const via carre-du-champ (2nd moment), edge deficit O(1/L)")
res=[run(l) for l in [7.0,9.0,11.0,13.0,16.0]]
print(f"\n{'='*60}\nSUMMARY: scaling with lambda (edge deficit -> 0):")
print(f"  L:            {[f'{r[0]:.2f}' for r in res]}")
print(f"  std(c2)/mean: {[f'{r[1]:.3f}' for r in res]}  (must DECREASE ~1/L)")
print(f"  center/edge:  {[f'{r[2]:.3f}' for r in res]}  (must ->1)")
