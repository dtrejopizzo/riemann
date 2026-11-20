# POWER_CONFLUENT_004 — Exact confluent archimedean certificate of order three

Status: PROVED, rational certificate executed and independently reviewed in POWER_AUDIT_004.md§5. No numerical sweep. Papers untouched.

New reason: the density bound of POWER_ARCH_TRIPLE_004 lost .051, but the restriction to THREE poles allows computing exactly the confluent matrix in a Laguerre basis. Pole motion, studied separately, may transfer this case to arbitrary rates; that result is not presupposed here. Antecedents and restrictions consulted in POWER_BRIDGE_002.

## 1. Exact matrix

For u=63/2, take the orthonormal basis in L²(0,infinito)

    phi0=sqrt(2u)e^-uy,
    phi1=sqrt(2u)e^-uy(1−2uy),
    phi2=sqrt(2u)e^-uy(1−4uy+2u²y²).

If p(u)=[psi((u+1/2)/2)−log pi]/2, the archimedean kernel between e^-uy,e^-vy is [p(u)+p(v)]/(u+v). Differentiating k times in u and l times in v, multiplying by (-1)^(k+l), gives the entries between y^k e^-uy and y^l e^-vy. Conjugating by the three polynomials above cancels all derivatives of order >2 and gives

    M=[[d,b,c],[b,d,b],[c,b,d]],
    d=psi(16)−log pi,
    b=(63/4)psi'(16),
    c=b+(3969/16)psi''(16).

In general, before fixing u, d=2p(u), b=2up'(u), c=2u[p'(u)+up''(u)]. This is also checked by integrating the rational Fourier basis; no external spectral data are used.

## 2. Sufficient rational bounds

One proves

    d>159/100,  0<b<51/50,  |c|<1/50.                       (R)

Let H_m=Σ(k=1..m)1/k and

    J_N(r)=2Σ(k=0..N−1) r^(2k+1)/(2k+1),
    E_N(r)=2r^(2N+1)/[(2N+1)(1−r²)].

For 0<r<1, J_N(r)<log((1+r)/(1−r))<J_N(r)+E_N(r), by the integrated geometric series. With N=24, γ<H256−log256 and pi<22/7 give

    d > H15−H256+8J24(1/3)−J24(15/29)−E24(15/29) >159/100.

For the derivatives only the convergent series are used

    psi'(16)=Σ(k>=16)k^-2,
    psi''(16)=−2Σ(k>=16)k^-3.

Set S2=Σ(k=16..255)k^-2, S3=Σ(k=16..255)k^-3. Integral comparison gives

    blo=(63/4)(S2+1/256) < b < (63/4)(S2+1/255)=bhi,
    blo−(3969/8)(S3+1/(2·255²)) < c
       < bhi−(3969/8)(S3+1/(2·256²)).

The four comparisons of R are purely rational and were verified with Fraction. Exact code is attached below. No special functions are rounded.

## 3. Proved margin

The matrix with only b on the two edges of the chain has eigenvalues 0,+sqrt(2)b,−sqrt(2)b; the matrix with c in the corners has norm |c|. Hence

    M >= [d−sqrt(2)b−|c|] I
      > [159/100−(10/7)(51/50)−1/50]I
      > (1/10)I.

One used sqrt(2)<10/7. Thus the ARCHIMEDEAN form is coercive with constant >1/10 on span{e^-31.5y,ye^-31.5y,y²e^-31.5y}.

This is not yet the complete form: the comb and the polar part must be controlled, and distinct rates require the pole-motion proof. In a family of nearby triples, the basis of divided differences converges to this confluent basis in form norm, so the archimedean margin does persist in some neighborhood; no explicit radius is declared.

## 4. Rational verification code

```python
from fractions import Fraction as F
H=lambda n:sum((F(1,k) for k in range(1,n+1)),F())
def J(r):
    return 2*sum((r**(2*k+1)/F(2*k+1) for k in range(24)),F())
def E(r):
    return 2*r**49/(F(49)*(1-r*r))
dlo=H(15)-H(256)+8*J(F(1,3))-J(F(15,29))-E(F(15,29))
S2=sum((F(1,k*k) for k in range(16,256)),F())
S3=sum((F(1,k**3) for k in range(16,256)),F())
blo=F(63,4)*(S2+F(1,256))
bhi=F(63,4)*(S2+F(1,255))
clo=blo-F(3969,8)*(S3+F(1,2*255**2))
chi=bhi-F(3969,8)*(S3+F(1,2*256**2))
assert dlo>F(159,100)
assert 0<blo<bhi<F(51,50)
assert -F(1,50)<clo<chi<F(1,50)
assert F(159,100)-F(10,7)*F(51,50)-F(1,50)>F(1,10)
```
