# POWER_POLAR_MOVEMENT_005 — Pole transport with the polar term: identity, favourable sector and real obstruction

Status: PROVED (identities, sector P<=0, general falsifier, order one in the high range and uniform positive derivative of order four at confluence); OPEN (global sign transport of order four for rates>=63/2). Papers untouched.

## 1. Antecedents and new reason

Consulted the ROUTES-TRIED-INDEX index, grid and crossword (polar movement, pole filter, positive polar, confluent), as well as POWER_POLE_MOVEMENT_004, POWER_CONFLUENT_004 and its audit. The archimedean part already has an exact transport. The new difference is to keep the POSITIVE polar, which turns out to be essential in order four: the confluent diagnostic has archimedean minimum close to -.17005, while arch+polar has minimum close to +.32259. The polar is not treated as a uniform loss and the archimedean movement is not extrapolated.

## 2. Exact identity with fixed rational numerator

For rates v_j>=u_j>1/2, let H(s)=Π_j(s+u_j)/(s+v_j), fhat_new=H(i tau)fhat_old. Define

    R(tau)=|H(i tau)|²=Π_j(u_j²+tau²)/(v_j²+tau²),
    r0=H(-1/2)H(1/2)=Π_j(u_j²-1/4)/(v_j²-1/4).

Normalise f_old to norm one, and use the probability dμ=|fhat_old|²d tau/(2pi). Let Aold=Eμ m and Pold=2A(f)B(f), both Rayleigh quotients with the old norm. Then

    Enew-Eold=[Covμ(m,R)+(r0-EμR)Pold]/EμR.               (F)

All polar factors are positive reals, and if at least one pole increases,

    0<r0<R(0)<=R(tau)<=1.

The first strict inequality comes from (u²-1/4)/(v²-1/4)<u²/v² for u<v. Hence the archimedean covariance remains favourable, but the second term has sign OPPOSITE to Pold.

### Sector that does transport

For every numerator with Pold<=0, (F) proves Enew>=Eold. The sign of the polar is preserved under pole movement because it is multiplied by r0>0. This includes the subspaces A=0 or B=0. For Pold>0 the identity alone gives no comparison: it is exactly the sector that can rescue a negative archimedean direction.

## 3. Falsifier of the general transport, without touching the high range

The following exact counterexample was obtained. In order one, fixed numerator 1, rate u>1/2, the arch+polar quotient is

    E(u)=psi((u+1/2)/2)-log pi+4u/(u²-1/4).

For u=1 and v=2, the reflection and recurrence identities of psi give

    E(2)-E(1)=(4-pi)+(32/15-16/3)=4/5-pi<0.

Thus the general theorem «arch+polar increases when poles increase» is FALSE even in dimension one. The sites lie outside the range u>=63/2; it does NOT refute sign transport or monotonicity in the relevant range of order four.

## 4. Order one in the high range: PROVED

There is an elementary proof of the full transport for n=1 and u>=8. By the trigamma series and integral comparison, psi'(x)>=1/x. Hence

    E'(u)>=1/(u+1/2)-4(u²+1/4)/(u²-1/4)².

For u>=8, the first term is >=16/(17u). The second is less than 5/u², since u²+1/4<=(257/256)u², u²-1/4>=(255/256)u², and 4*(257/256)/(255/256)²<5. Finally 16/(17u)>5/u² for u>=8. Thus E'>0 in that range, including all rates of the project. The falsifier §3 does not automatically extend to the high range.

## 5. Exact confluent derivative for order four

An additional reduction keeps the coupling. Fix u and use the orthonormal Laguerre basis with transforms

    F_j(s)=sqrt(2u)/(s+u)*[(s-u)/(s+u)]^j, j=0,...,3.

The arch+polar matrix is Toeplitz, M_ij=m_|i-j|. With g(s)=[psi((s+1/2)/2)-log pi]/2 and r=(u+1/2)/(u-1/2), its exact entries are

    m0=2g(u)+4u/(u²-1/4),
    mk=Σ_{j=1}^k g^(j)(u)(2u)^j binom(k-1,j-1)/j!
          +[2u/(u²-1/4)](-1)^k(r^k+r^-k), k>=1.

Moving ONE pole with fixed numerator multiplies the transform by (s+u)/(s+u+delta). At delta=0, its time derivative is -(F_j-F_{j+1})/(2u), since 1/(s+u)=(1-z)/(2u). For a real normalised vector x of four coordinates, put c_k=Σ_j x_jx_{j+k}. The derivative of the full quotient satisfies exactly

    u E'=m1+m2 c1+(m1+m3)c2+(m2+m4)c3
             -2c1(m1 c1+m2 c2+m3 c3).                       (D4)

The term m0 cancels against the derivative of the norm; omitting it produces an incorrect result. This is a concrete quartic inequality in four variables, not an abstract equivalence with the global target.

## 6. Uniform positive derivative of order four at u=63/2: PROVED

For every nonzero numerator of degree less than four, when ONE pole increases from the confluent configuration (u,u,u,u), u=63/2, the arch+polar quotient satisfies

    dE/dv_j >3/(40u)=1/420.

It is proved by a single finite rational SOS identity, not by eigenvector optimisation. The new reason relative to the arithmetic SOS registered in the corpus is that here an explicit quartic in FOUR numerator coefficients is certified, at ONE declared point of rates; no universal factorisation of the arithmetic form is sought.

First, the polygamma series at the integer 16, with tails bounded by integrals, prove

    |m1-8887/10000|<1/10000,
    |m2-1116/10000|<1/10000,
    |m3-2213/10000|<1/10000,
    |m4-1126/10000|<1/10000.

Let Dbar be the homogeneous quartic (D4) using those four rational centres and N=Σx_i². With z=(x0²,x0x1,x0x2,x0x3,x1²,x1x2,x1x3,x2²,x2x3,x3²), the exact identity is

    Dbar-(2/25)N²=z^t Q z,

where Q is the following matrix divided by 10000:

```text
 8087   558  5550  1121 -5250  -358 -1663  1687   558   937
  558  8900  -200  5000   558 -4324  1005 -1358 -2787   558
 5550  -200 12800     0 -7900   800 -7200  5550  1005 -1663
 1121  5000     0 14300 -1000 -10000    0 -1000  5000  1121
-5250   558 -7900 -1000  8087   558  5550 -5450 -1358  1687
 -358 -4324   800 -10000 558  9300   800   558 -4324  -358
-1663  1005 -7200     0  5550   800 12800 -7900  -200  5550
 1687 -1358  5550 -1000 -5450   558 -7900  8087   558 -5250
  558 -2787  1005  5000 -1358 -4324  -200   558  8900   558
  937   558 -1663  1121  1687  -358  5550 -5250   558  8087
```

Exact LDL elimination of Q gives TEN pivots greater than 1/5. Hence it is positive definite; it is equivalent to a sum of ten squares of rational combinations of the monomials z, with positive rational coefficients. Since |c_k|<=N, the sensitivities of D4 with respect to m1,m2,m3,m4 are bounded respectively by 4N²,4N²,3N²,N². The loss from substituting the four coefficients is less than (12/10000)N². Therefore

    D4>(2/25-12/10000)N²>(3/40)N².

For N=1, this proves the declared derivative bound. All four intervals, the identity of 35 quartic coefficients, the ten pivots and the final inequality are verified using only `Fraction` in `tools/polar_derivative_sos_005.py`; the verifier contains no optimiser, no floating point and no numerical special functions.

Command: `python3 03-research/phase-211-sign-sandbox/tools/polar_derivative_sos_005.py`. An optimisation of the single concrete quartic served to discover the Gram; it plays no role in the final proof and no sweep of rates was made.

### Elementary structure of the dominant term

The following observation explains the underlying coercivity: let J be the path matrix on four vertices with entries 1/2 off the immediate diagonal. Then

    N²+c2 N-2c1²
      =2[||Jx||²N-<Jx,x>²]+(x0²+x3²)N/2 >=0.

The first term is a variance and the second a boundary energy. The certificate Q retains enough margin of this structure while incorporating m2,m3,m4 and their errors. It is not claimed that the other three contributions are positive separately.

### Scope of the local transport

The derivative bound holds for EVERY numerator of degree less than four at the confluent point, not only for the lowest eigenvector. Since the sphere of numerators is compact and the kernels depend continuously on the rates, there exists a neighbourhood of (u,u,u,u) in which all individual derivatives remain positive. No explicit radius is declared. This proves a local transport of quotients and eigenenergies; it does not by itself allow traversing the whole orthant of rates>=u.

## 7. Precise residue

For a sign of order four an absolute bound on |polar| is not enough: it eliminates the positive contribution that compensates the negative archimedean minimum. One needs to dominate in (F) the loss (EμR-r0)Pold by the covariance when Pold>0, or to prove directly a weaker sign transport. This note proves neither of those two inequalities in order four. The general counterexample §3 prevents asserting them without range and dimension hypotheses; the high case n=1 and the sector Pold<=0 are closed by proof.
