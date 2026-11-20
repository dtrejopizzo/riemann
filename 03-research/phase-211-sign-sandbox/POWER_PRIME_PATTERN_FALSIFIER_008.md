# POWER_PRIME_PATTERN_FALSIFIER_008 — In the same family, low contacts can also worsen the deficit

Status: PROVED (explicit vector, zero polar, archimedean deficit and harmful sign of each contact <=1024). Negativity of the full form is not claimed. Papers untouched.

## 1. Antecedents and declared difference

Read POWER_POLYNOMIAL_003, POWER_ARITHMETIC_WITNESS_006, POWER_POLE_MOVEMENT_004 and Paper47, theorem of sub-comb negativity (§Partial prime combs); searches for Laguerre, Levinson, finite differences and Toeplitz prime in index, grid and crossword. The necessity of the arithmetic and the failure of monotonicity when adding contacts are already recorded. No new global NO-GO is proposed. The exact difference is a closed test in the SAME fixed confluent family used by the certificates: in 006 all contacts help and 2 repairs; here ALL contacts up to 1024 harm a direction with polar exactly zero and negative archimedean part. No matrix search or numerical campaign is done.

## 2. Explicit rational vector in the confluent space

Fix u=63/2, n=2^17 and

    g(y)=y^{n-1}exp(-uy)1_{y>0},
    f(y)=(d²/dy²-1/4)g(y).

Since n>3, g(0)=g'(0)=0 and the integrations by parts have no boundary terms. Both g and all necessary derivatives decay exponentially at infinity. The Laplace transform is

    F(s)=(n-1)!(s²-1/4)/(s+u)^n.

It is a FIXED rational numerator of degree two in the confluent space of n poles u, so f belongs to the span of the first n Laguerre functions e^-uy L_j(2uy). There is no need to print n coefficients: the differential formula determines them exactly.

The polar moments are exactly

    A(f)=F(-1/2)=0, B(f)=F(1/2)=0.

Thus the polar vanishes. The normalised spectral density is proportional to

    (tau²+1/4)²/(u²+tau²)^n.                              (S)

## 3. Rational bound on the second spectral moment

First use the base probability proportional to (u²+tau²)^-n. If M_{2k} is its moment, integration by parts or the beta integral give

    M2=u²/(2n-3),
    M4=3u^4/[(2n-3)(2n-5)],
    M6=15u^6/[(2n-3)(2n-5)(2n-7)].

For n=2^17, u²<1024 and each denominator of the three products is greater than n. Hence

    M2<1/128, M4<3/128², M6<15/128³.

Weighting by (tau²+1/4)², the second moment of (S) is

    E_f tau²=[M6+(1/2)M4+(1/16)M2]
                  /[M4+(1/2)M2+1/16]
             <=16M6+8M4+M2
             <1231/131072<1/100.                         (M)

All comparisons are rational; no large factorials are estimated.

## 4. Strict archimedean deficit

The positive series of the multiplier gives, for a_k=k+1/4,

    m(tau)-m(0)
      =Σ [(tau²/4)/(a_k(a_k²+tau²/4))]
      <=(tau²/4)Σ a_k^-3 <17tau².

The last bound uses Σ_{k>=1}(k+1/4)^-3<=104/125, summing the first term and comparing with an integral; the term k=0 contributes 64. Moreover m(0)=-gamma-pi/2-3log2-logpi<-4 (in fact <-9/2), using gamma>0, pi>3, log2>2/3 and logpi>1. By (M),

    Arch[f]/||f||² <-4+17/100=-383/100.

The polar is zero, so Arch+Polar is strictly negative on this test, without any numerical diagnostic.

## 5. ALL low contacts harm the sign

By cos x>=1-x²/2 and Parseval,

    c_f(t)/||f||²=E_f cos(tau t)
                 >=1-(t²/2)E_f tau² >1-t²/200.

For each integer q with 2<=q<=1024, logq<=10log2<10. Hence

    c_f(logq)>||f||²/2.

Each nonzero prime-power contact of that interval contributes

    -2Lambda(q)q^-1/2 c_f(logq)
       <-Lambda(q)q^-1/2 ||f||² <0.

In particular adding contact 2 worsens the deficit; adding 3 also worsens it; and the same happens with all prime powers up to 1024. It is the opposite behaviour to the dimension-twelve vector of POWER_ARITHMETIC_WITNESS_006, where all help. The pattern depends on the autocorrelation of the vector, not on a universal sequence of repairing primes.

## 6. Concrete arithmetic inequality required by this test

The full series of the comb converges absolutely, since c_f(t) is exponential e^-ut times a finite polynomial. If the full form is nonnegative on this test, the segment q>1024 necessarily satisfies

    -Σ_{q>1024}2Lambda(q)q^-1/2 c_f(logq)/||f||²
       >383/100 + Σ_{2<=q<=1024}Lambda(q)q^-1/2.           (TAIL)

This is an explicit obligation on the tail of the SAME vector: the low segment cannot produce its repair. (TAIL) is not used as proof of its own sign, nor is it claimed to be proved here. The necessary arithmetic property must keep the sum with autocorrelations of both signs; the favourable contributions of a concrete vector do not transfer to the whole subspace.

W[f]<0 is not claimed: precisely the tail q>1024 remains unevaluated. The result refutes no full certificate of the paper or of this phase; it only refutes the universal pattern «low contacts always repair the negative arch+polar directions» within the fixed confluent family.
