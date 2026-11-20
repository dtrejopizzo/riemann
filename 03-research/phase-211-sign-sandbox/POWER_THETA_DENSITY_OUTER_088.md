# POWER_THETA_DENSITY_OUTER_088 — Exterior sign of the four-density Wronskian

Status: **PROVED, polynomial/rational certificate exit0/PASS, independent audit and reproductions approved.** See `POWER_THETA_DENSITY_OUTER_AUDIT_088.md`. Only t>=1 for the R4 densities of the real Phi. Neither the global transport, a new W region nor all orders are inferred. Papers untouched; no meshes or numerical theta evaluations.

## 1. Antecedents and specific object

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread 077, 083–087. 086 controls the three R3 densities via N>0 of 077; 087 decides the necessary sign of the R4 Wronskian at the origin, without a global interval. The fourth sign is not inherited from the third.

With real Phi and V=−logPhi, define for t>0

    p=V',q=V'',r=V''',s=V'''',v5=V^(5),v6=V^(6),
    A=p²−q−2p/t, B=p/t, C=(p³−3pq+r)/t,
    W4(t)=W_t(1,A,B,C), G(t)=t⁴W4(t).

The result is the uniform quantitative bound

    G(t)<−4000 t² y⁶,
    W4(t)<−4000 y⁶/t²<0,
    ALL t>=1, y=pi exp(2t).                       (OUTER)

ALL theta modes are kept. The new difference relative to the outer range of 077 is a Wronskian containing derivatives up to order 6; its signs are not included in C, N of 077, which only reach order 4.

## 2. First mode and an exact polynomial

For the first mode set b=2y−3 and g0=exp(5t/2−y), so that Phi1=pi b g0. Use D=partial_t+2y partial_y on polynomials in t,y. Define

    B0=2y−3,
    B_(j+1)=D B_j+(5/2−2y)B_j, j=0,1,2.

Then Phi1^(j)=pi g0 B_j and

    F=(tB0, tB2+2B1, −B1, −B3).

Removing the common factor pi g0 from the Wronskian of the four densities, one obtains exactly

    W4,0=det[D^iF_j]_(i,j=0)^3/(t b)^4.

The determinant of the numerator is

    det[D^iF_j]=−16 y² P(t,y),                       (MODE-POLY)

where P is a rational polynomial. The verifier generates it via the recurrences and the determinant, without any floating-point datum.

The polynomial inequality is checked on the LARGER quadrant

    P(t,y)>4096 t² y⁸, ALL t>=1,y>=21.             (MODE-MARGIN)

Finite proof: substitute t=1+T, y=21+Y in P−4096t²y⁸. Its 27 nonzero coefficients, including the constant, are STRICTLY positive. Therefore the polynomial is positive for T,Y>=0. The relation between t and y is not required for this step.

Since b<2y, MODE-POLY and MODE-MARGIN give

    G0=t⁴W4,0<−65536 t²y^10/b⁴<−4096t²y⁶.          (MODE-BOUND)

For the real datum t>=1, pi>3 and exp2>7 give y>21; exp2>7 is proved with the positive Taylor sum up to degree 5.

## 3. Complete theta tail up to sixth order

Write Phi=Phi1(1+Rtheta), Rtheta=Σ_(m>=2)r_m>0. As in 077/10343, with a=m²−1>=3 and z=ay,

    0<r_m<=(32/9)a²exp(−ay).

Set h=3/(2y)<=1/14. The quotient has logarithm

    log r_m=constant−ay+log(1−h/m²)−log(1−h).

The logy contributions cancel BEFORE differentiating. For 1<=j<=6,

    |D^jlog r_m|
      <=2^j[z+Σ_(n>=1)n^(j−1)h^n]
      <=2^j[z+1]<2^(j+1)z.                         (LOG-TAIL)

The bound on the sum is obtained from the rational identity

    Σ_(n>=1)n⁵h^n
      =h(1+26h+66h²+26h³+h⁴)/(1−h)^6<1 on h<=1/14.

The lower orders are dominated by n⁵ for n>=1. The Bell formula for differentiating exp(log r_m), with the bounds 2^(j+1)z, gives at order 6

    |D^6r_m|/r_m
      <=4096z⁶+30720z⁵+66560z⁴+46080z³+7936z²+128z
      <5000z⁶, z>=63.

The same majorant serves for orders 0,...,5: the complete Bell polynomials with positive arguments here grow with the order, because the first argument 4z is >=1. Therefore

    |D^jRtheta|
      <=(160000/9)y⁶ Σ_(a>=3)a⁸exp(−ay), 0<=j<=6.

The sum over a=m²−1 was extended to ALL integers a>=3; only positive terms were added. The rational Taylor sum of exp3 up to degree 11 proves exp3>20. For y>=21, the consecutive ratio of a⁸exp(−ay) is <=(4/3)^8/20^7<1/2. Moreover y⁶exp(−3y) decreases for y>=21. Thus

    |D^jRtheta|<E, j=0,...,6,
    E=(320000/9)3⁸21⁶/20^21
      =62523502209/6553600000000000000000.            (TAIL)

It is a bound on the COMPLETE tail for each relevant derivative.

## 4. Error of the six derivatives of the potential

Rtheta>=0 ensures denominators 1+Rtheta>=1. The logarithmic derivative formulas and TAIL give, simultaneously for 1<=j<=6,

    |D^jlog(1+Rtheta)|
      <=E+31E²+180E³+390E⁴+360E⁵+120E⁶<2E=:eta.     (LOG-ERROR)

The coefficients are (k−1)!S(6,k); the lower orders are dominated by the same sum. No sign of the error is used, only its modulus.

For the first mode, V0=y−(5/2)t−log(2y−3)−logpi. At order 1, 0<V0'<2y. For orders 2,...,6, the expansion of log(1−h) already used gives

    |V0^(j)|<=2^j(y+1)<68y.

With eta<1 and y>=21, all segments between the exact jets and those of the first mode stay inside the box

    |p|,|q|,|r|,|s|,|v5|,|v6|<=128y.                (BOX)

It is not assumed that the later modes are negligible in high derivatives: LOG-TAIL and Bell pay precisely for those factors.

## 5. Propagation to the generic polynomial of the Wronskian

The same formal differentiation algorithm, now with p'=q, q'=r, r'=s, s'=v5, v5'=v6, proves that

    G=t⁴W_t(1,A,B,C)

is a polynomial of 55 monomials in t,p,q,r,s,v5,v6. Each exponent of t lies between 0 and 2 and each total degree in the six jets lies between 3 and 6. No derivative of v6 appears: the verifier requires it when applying the differentiation.

The sums of absolute coefficients weighted by the jet degree, grouped by that degree, are

    degree6:888, degree5:1580, degree4:644, degree3:66.

By BOX, for t>=1, y>=21, the sum of moduli of the six partial derivatives of the polynomial is <=K t²y⁵, where

    K=888·128⁵+1580·128⁴+644·128³+66·128²
      =30936927338496.

The multivariable mean value theorem and LOG-ERROR prove

    |G−G0|<=eta K t²y⁵.

The exact rational comparison of the verifier is

    eta K=59029694970340794273/100000000000000000
          <96·21<=96y.

With MODE-BOUND,

    G<−4096t²y⁶+96t²y⁶=−4000t²y⁶,

which proves OUTER for ALL t>=1, not a collection of points.

## 6. Finite verifier and output

Run

    python3 03-research/phase-211-sign-sandbox/tools/power_theta_density_outer_088_verify.py

The program uses only integers, Fraction and exact polynomial operations; it needs neither Sympy, FLINT nor evaluating pi or a theta sum at a point. It certifies the 27 positive coefficients, the 55 monomials and K, and all rational inequalities of TAIL/LOG-ERROR/MVT. The final run finished exit0 with the four blocks PASS.

SHA256 of the stable version:

    d2b1e479295cbf9eda602a2786b657cab5c83db1c74dee9a7d00b751723fc8f4.

An earlier auxiliary symbolic check produced the same identities. The final certificate is self-contained in rational operations, not in parameter sampling.

## 7. Transport consequence and limit

086 already proves B'>0 and J=(A'/B')'>0 for ALL t>0. With Eraise=(C'/B')', the identity

    W4=−(B')³J²(Eraise/J)'

implies (Eraise/J)'>0 for ALL t>=1. Rolle in the coordinate B gives the negative sign of the four-density determinant at any four distinct points ALL >=1. The first-mode sign was only used after paying the complete tail.

To apply Andreief to the whole half-line 0<t<infinity the range 0<t<1 is still missing. 087 certifies the sign at the origin and some unquantified neighbourhood, but does not fill that interval. Its contribution is not omitted, nor does one pass from a region of density nodes to the sign of the complete integral.

Neither global PF4 transport, a new W region, five generators, all orders nor a time window is claimed. The global proof for four powers 085 remains independent and valid. The pending structural object is the sign of the new density Wronskian on the remaining compact range.
