# Completeness on squares and perfect powers: sufficiency falsifiers

Status: **PROVED algebraically and by transfer of an existing certificate; independent mathematical and literal audits approved (including section 11).** No new computation is executed. No paper is modified. The conclusion refutes only the sufficiency of the declared hypotheses for the fixed-background form; it does not concern the sign of the original form of Lambda.

Extension in section 11: exact normalization of the residue by means of high factors; mathematical and literal audits approved. Its bound N<=C is distinguished from the condition N<=1 of earlier examples.

## 1. Consultation and exact antecedents

Consulted: the project rules, ROUTES-TRIED-INDEX/README.md and06R7, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md, the ledger C1–C51 of phase211 and POWER_REASSESSMENT.md. Read R186_005 and its logical correction in R186_092, the finite Euler memos of phase197 and L2_BUILD_016_FROBENIUS_DOUBLING of phase188.

The corpus search for the local formulas 1+c_p z, N(n^2)=1, square completeness and variants did not find the continuous family presented here. The endpoint used as a falsifier DID appear: R163_102_BOUNDED_ERROR_VS_LATTICE.md, Cor F, example T={2},Q={4}, records the quotient A(s)=1/(1+2^(-s)); R163_191_AUDIT_101_102.md confirms that example. There the counting error is studied; the primitive negativity used below is not proved. That antecedent is not presented as new.

Phase197 contains Euler classes with coefficients N in {0,1}, of which this endpoint is a member; its conclusions for small defects do not transfer automatically to this parameter. The dilation of 188 treats a transport of windows and their weights, distinct from imposing N(n^2)=1. None of those arguments replaces the following proof. The reused negative certificate is ROUND_007_C, theorem 1; its script is not re-executed.

## 2. Exact family with non-identifying partial completeness

Choose independently 0<=c_p<=1 for each prime and define, with z formal,

    F_p(z)=(1+c_p z)/(1-z^2).

Its local coefficients are

    N_c(p^(2j))=1,
    N_c(p^(2j+1))=c_p, j>=0.

The Euler product determines a multiplicative function N_c and an absolutely convergent series for Re s>1:

    F_c(s)=prod_p F_p(p^(-s))
          =zeta(2s) prod_p(1+c_p p^(-s))
          =sum_n N_c(n)n^(-s).

For n=prod p^k,

    N_c(n)=prod_(k odd)c_p,
    0<=N_c(n)<=1,
    N_c(n^2)=1 for EVERY integer n>=1.             (SQUARES)

Define the logarithmic coefficients ell_c by -F_c'/F_c=sum ell_c(n)n^(-s). Elementary expansion of the two logarithms gives

    log F_p(z)=sum_(k>=1)
       [(-1)^(k+1)c_p^k+2*1_(k even)]z^k/k.

Hence ell_c is supported on prime powers and

    ell_c(p^k)/log p=c_p^k,         k odd,
    ell_c(p^k)/log p=2-c_p^k,       k even.        (ELL)

In particular ell_c>=0 and ell_c<=2Lambda. If all c_p=1 one recovers N_c=1 and ell_c=Lambda. SQUARES does not identify that member: if c_2=0, then N_c(2)=0 and ell_c(2)=0, although N_c(n^2)=1 for all n. It is a concrete family of partial completeness, not an empty hypothesis nor a total identification.

## 3. Already-known finite endpoint and the form being tested

Now fix c_2=0 and c_p=1 for all primes p different from 2. Then

    F_square(s)=zeta(s)/(1+2^(-s)),
    ell_square(2^k)=0 if k odd,
    ell_square(2^k)=2log2 if k even,
    ell_square(p^k)=log p if p different from 2.

This is the endpoint whose quotient with respect to zeta appears in R163_102. Its coefficients N take only 0 and 1, and SQUARES holds on ALL squares.

Moreover F_square has a simple pole at s=1 with residue 2/3, NOT residue 1. It is not claimed that it possesses the functional equation of the original member. The obstruction must not be used for classes that impose those additional hypotheses without checking whether they contain the example.

The tested form is EXACTLY the primitive fixed-archimedean-background form of ROUND_007_C/Paper46, with contact weights

    v_n=2ell(n)/sqrt(n).

For one and the same function F of the primitive carrier P_T, the two Tate moments are zero and the polar term is zero. Only ell is changed at the contacts; the carrier and the archimedean background remain the same. No functional equation compatible with that background is attributed to F_square. No functional equation for the deformation is part of the hypotheses being refuted.

Write C_F(u) for the real autocorrelation of F. The difference between two forms with that same background is exactly the signed difference of their contacts, by the definition of the form.

## 4. Existing certified witness, without new evaluation

Use literally the witness of ROUND_007_C, theorem 1, with

    T0=(log5)/2+1/10000,
    L=2T0=log5+1/5000.

In the coordinate s=t+T0, the function is zero outside [0,L] and

    f(s)=a1 sin(pi s/L)+x sin(3pi s/L)
          +a5 sin(5pi s/L)+a7 sin(7pi s/L),
    a1=-384199/10^6,
    a5=172109/10^6,
    a7=-4131/125000.

The coefficient x is THE SAME real that exactly annihilates the moment A(F). The certificate 007_C proves x>1, more precisely it encloses it in 1.0000005632467671625 +/-4.3*10^(-20). Only odd indices appear, so F is even and the other Tate moment is also zero. x is not replaced by a decimal and the function is not readjusted.

If a_3 denotes the deformation with the prime 2 deleted in ALL its powers, the existing certificate gives

    a_(T0)^(a_3)(F)/||F||^2 <= -0.50528<0.       (CERT007)

The norm is positive. This source USES that certified and audited result; it introduces no new quadrature nor a numerical witness.

## 5. Elementary sign of the additional contact at 4

Put delta=L-log4>0. One has delta<L/7: the inequality is equivalent to

    log(128/125)>3/5000,

and the integral of 1/u between 125 and 128 is greater than 3/128>3/5000. For 0<s<delta, theta=pi s/L satisfies

    0<theta<pi/7<1/2.

Then sin(3theta)=(3-4sin(theta)^2)sin(theta)>2sin(theta), sin(5theta)>0 and sin(7theta)<=7sin(theta). The last inequality follows, for example, from the sum of seven exponentials representing sin(7theta)/sin(theta). With x>1,

    f(s)>[2-384199/10^6-7*4131/125000]sin(theta)
         =(1384465/10^6)sin(theta)>0.             (EDGE)

By parity f(L-s)=f(s). Consequently

    C_F(log4)=int_0^delta f(s)f(s+log4)ds
             =int_0^delta f(s)f(delta-s)ds>0.     (CONTACT4)

It is an analytic sign proof; the autocorrelation has not been evaluated.

## 6. Transfer of the certificate and limited conclusion

In the window T0 the only relevant contacts of ell_square are 3,4,5. Those at 3 and 5 coincide with a_3; at 2 both deformations have weight 0. At 4,

    ell_square(4)=2log2,
    v_4=2ell_square(4)/sqrt4=2log2.

Hence, on the SAME primitive witness and with the SAME background,

    a_(T0)^(ell_square)(F)
      =a_(T0)^(a_3)(F)-2log2*C_F(log4)
      <a_(T0)^(a_3)(F)
      <=-0.50528||F||^2<0.                       (NEGATIVE)

Thus ell_square is a PROVED falsifier of the sufficiency of

    ell>=0, support on prime powers, N_ell multiplicative,
    0<=N_ell(n)<=1 and N_ell(n^2)=1 for EVERY n,
    simple pole at 1, with positive residue NOT imposed equal to 1

to guarantee the non-negativity of this fixed-background form in all windows. The same witness extended by zero gives negativity for all T>=T0, by lemma 2 of 007_C; no additional values are needed.

The new family is non-identifying, but that observation did not make it viable as a sign mechanism: it contains the endpoint NEGATIVE. This does not prove a NO-GO of every imaginable use of partial completeness. An additional hypothesis excluding ell_square would have to be specified and proved separately; in particular no global functional condition for the deformation has been assumed here. The member ell=Lambda is not refuted and the original target is not modified. No new certificate was executed and no paper was touched.

## 7. Imposing residue 1 collapses THIS ansatz to the original member

For a finite number of parameters c_p different from 1, the exact quotient is

    F_c(s)/zeta(s)=prod_p (1+c_p p^(-s))/(1+p^(-s)).

It is analytic and strictly positive at s=1, so that F_c has a simple pole with residue

    R_c=prod_p (p+c_p)/(p+1).

Each factor is positive and at most 1. If some c_p<1, the residue is strictly less than 1. For c_2=0 and the others 1 it gives R_c=2/3.

The same identification conclusion holds for infinite modifications if residue 1 is demanded. For every real sigma>1, the product converges absolutely and all its factors are at most 1. For each fixed prime p0,

    0<F_c(sigma)/zeta(sigma)
       <=[1+c_(p0)p0^(-sigma)]/[1+p0^(-sigma)].

If F_c has residue R_c at 1, letting sigma tend to 1 from the right gives

    R_c<=(p0+c_(p0))/(p0+1).

A single parameter c_(p0)<1 forces R_c<1. Hence R_c=1 implies c_p=1 for ALL primes, and F_c=zeta. It is identification within THIS ansatz, not a new sign proof. That collapse is not claimed for every imaginable class with partial completeness and residue 1.

## 8. Uniform corollary: each fixed order of perfect powers is insufficient

For EACH fixed integer m>=2, replace the prime 2 by 2^m and keep all the other primes. Its exact product is

    F_m(s)=zeta(s)(1-2^(-s))/(1-2^(-ms)).

The local factor at 2 is 1/(1-z^m); the others are the ordinary ones. Thus

    N_m(n)=1 if m divides the valuation of 2 in n, and 0 otherwise,
    N_m(n^m)=1 for EVERY n,
    ell_m(2^k)=m log2 if m divides k, and 0 otherwise,
    ell_m(p^k)=log p for p different from 2.

In particular N_m is multiplicative and takes only 0 and 1, and ell_m>=0. The quotient with respect to zeta belongs to the same family of finite replacements of the antecedent R163_102, Cor F, with T={2},Q={2^m}; that product is not presented as unknown in the corpus.

For m=2 it is the example already treated: the additional contact at 4 makes the form strictly smaller than the form a_3 on the certified witness. For ALL m>=3, the first additional contact of 2 is at 2^m>=8, outside the window T0, whose exponential endpoint is less than 7. Hence on the SAME witness 007_C,

    a_(T0)^(ell_m)(F)=a_(T0)^(a_3)(F)
        <=-0.50528||F||^2<0, m>=3.

It is a uniform identity, not a parameter campaign nor a new evaluation. By extension by zero, negativity also holds in every larger window.

Each F_m has a simple pole at 1 with residue

    R_m=1/[2(1-2^(-m))]<1.

Neither residue 1 nor the functional equation of the original member is attributed to it. The conclusion of THIS corollary is that, for EACH FIXED order m>=2, the completeness N(n^m)=1 on all perfect powers of that order is not enough, together with the declared positive hypotheses, to guarantee the sign of the fixed-background form. This argument by itself does not impose several orders simultaneously; section 9 treats that stronger condition with ANOTHER example.

## 9. All orders simultaneously: falsifier with non-integer coefficients

Consider the local factor at 2

    F_2(z)=1+z/2+sum_(k>=2)z^k
          =(1-z/2+z^2/2)/(1-z),

and keep the ordinary factors at the other primes. The product is

    F_all(s)=zeta(s)[1-2^(-s)/2+2^(-2s)/2].

Its multiplicative coefficients satisfy N_all(2)=1/2 and N_all(2^k)=1 for k>=2; all other local factors are complete. Hence

    0<=N_all(n)<=1,
    N_all(n^m)=1 for ALL n>=1 AND m>=2
      SIMULTANEOUSLY.                          (ALL-POWERS)

It is important that N_all(2) is NOT an integer. Integrality of the coefficients is not attributed to the example.

To check positivity of ALL logarithmic coefficients, write r_+=(1+i sqrt7)/4 and r_-=(1-i sqrt7)/4. They satisfy r_++r_-=1/2, r_+r_-=1/2 and |r_+|=|r_-|=1/sqrt2. The polynomial identity

    1-z/2+z^2/2=(1-r_+z)(1-r_-z)

and the formal series of the logarithms give

    ell_all(2^k)/log2=1-r_+^k-r_-^k.

For k=1 it equals 1/2. For k>=2, |r_+^k+r_-^k|<=2^(1-k/2)<=1, so ell_all(2^k)>=0. In particular ell_all(4)=(7/4)log2. At the other primes ell_all coincides with Lambda. It is a finite algebraic check of a bound uniform in k, not a coefficient search.

The literal corpus search for the polynomial 1-z/2+z^2/2 and its variants did not find this example. Its form is close to the finite Euler return move 1-z^k+z^(k+1) discussed in phase197; the finite Euler mechanism is not presented as new. Here the coefficient 1/2 makes it possible to verify ell>=0 at ALL levels and ALL-POWERS; the following form argument uses the previous certificate.

In the window T0, relative to a_3 only the contacts at 2 and 4 appear, with weights

    v_2=(sqrt2 log2)/2,
    v_4=(7/4)log2.

CONTACT4 is strictly positive. For any translation, Cauchy–Schwarz applied to F extended by zero gives |C_F(u)|<=||F||^2. Thus

    a_(T0)^(ell_all)(F)
      =a_(T0)^(a_3)(F)-v_2 C_F(log2)-v_4 C_F(log4)
      <[-0.50528+v_2]||F||^2.

The bounds sqrt2<10/7 and log2<7/10 imply v_2<1/2. The first is squaring 98<100; for the second, the positive Taylor polynomial of exp(7/10) up to degree 3 is 12013/6000>2. Hence

    a_(T0)^(ell_all)(F)<-0.00528||F||^2<0.        (ALL-NEGATIVE)

No new contact has been evaluated nor the certificate repeated. Extension by zero gives negativity for all T>=T0.

F_all has a simple pole at 1 with residue 7/8, and the functional equation of the original member is not attributed to it. The same background and the same PRIMITIVE carrier of sections 3–6 are kept. Consequently, ALL-POWERS, N multiplicative with 0<=N<=1 and ell>=0 are not enough even imposing ALL orders of perfect powers simultaneously, unless integrality, residue 1 or other hypotheses excluding the example are demanded. It is not a refutation of every class with partial completeness, nor of the original datum.

## 10. If integrality is also demanded, simultaneous powers identify the datum

There is a different conclusion, which is NOT a sign NO-GO. Suppose N multiplicative, N(1)=1,

    N(n^m)=1 for ALL n>=1,m>=2,
    N(p) a non-negative integer for each prime,
    ell(p^k)>=0 for all prime powers,

where ell are the logarithmic coefficients of the formal Euler product of N. Fix a prime and put c=N(p). The first hypothesis gives N(p^k)=1 for all k>=2. Its factor is

    F_p(z)=1+cz+sum_(k>=2)z^k.

The coefficient of z^2 in z F_p'/F_p is 2-c^2. Its non-negativity and c a non-negative integer force c in {0,1}. If c=0,

    F_p(z)=(1-z+z^2)/(1-z)=(1+z^3)/(1-z^2),
    z F_p'/F_p=3z^3/(1+z^3)+2z^2/(1-z^2).

The coefficient of z^6 is 2-3=-1, contradicting ell(p^6)>=0. Hence c=1 for ALL primes; all factors are 1/(1-z), and

    N(n)=1 for EVERY n,
    ell=Lambda.                                 (IDENTIFICATION)

This is exact algebraic identification by hypothesis, without needing to assume residue 1. It does not prove the sign of the form of the identified datum nor make impossible a future inequality that uses it. The non-integer example of section 9 does not belong to this class, and its negativity must not be attributed to it. Three facts are thus distinguished: the declared non-integer conditions admit falsifiers; residue 1 collapses the specific ansatz of section 2; and integrality plus ALL-POWERS and ell>=0 identify the datum by the present elementary proof.

## 11. Exact repair of the residue with high factors invisible to the witness

This extension only refutes another declared class; it does not propose a new route to the sign. The additional search in the corpus and in the three indices did not find the following precise compensating product. There are general antecedents that are kept: R163_102, lemma S, gives the count of zeta multiplied by an absolutely summable series; R163_802 already considers normalizations with value 1 at s=1. No other arguments from that source are invoked. The new check here also preserves ALL-POWERS and ell>=0 in concrete local factors and transfers the SAME negative witness.

### 11.1. Positive local factors that increase the residue

Keep at 2 the factor of section 9, whose quotient with respect to the ordinary one is 1-z/2+z^2/2 and whose relative residue is 7/8. At a prime p>=7 allow a rational parameter 0<=delta_p<=2/5 and replace the ordinary factor by

    F_(p,delta)(z)=[1+delta z-delta z^2]/(1-z).

Then N(p)=1+delta and N(p^k)=1 for ALL k>=2. Hence this modification does not alter ALL-POWERS.

It also preserves positivity of ALL logarithmic coefficients. For delta>0 write

    1+delta z-delta z^2=(1-rz)(1+sz),
    s-r=delta, rs=delta, 0<r<s<1.

The last inequality is obtained from the polynomial s^2-delta s-delta: it is negative at 0 and positive at 1, because 1-2delta>=1/5. For delta=0 one interprets r=s=0. The formal expansion of the logarithms gives

    ell(p^k)/log p=1-r^k+s^k,       k odd,
    ell(p^k)/log p=1-r^k-s^k,       k even.

The odd value is positive. If k>=2 is even,

    r^k+s^k<=r^2+s^2=delta^2+2delta<=24/25,

so that the even value is at least 1/25. At the unmodified primes Lambda is kept; at 2 positivity is already proved in section 9.

The relative residue factor is exactly

    1+delta a_p, a_p=(p-1)/p^2>0.

### 11.2. Finite and rational choice that exactly compensates 7/8

One has sum_(p>=7) a_p=infinity. To recall an elementary proof, if sum_p1/p converged, the finite products prod_(p<=X)(1-1/p)^(-1) would be uniformly bounded, using -log(1-1/p)<=2/p. But each product contains in its positive expansion all the terms 1/n with n<=X, contradicting harmonic divergence. Subtracting the convergent series sum_p1/p^2 does not alter the divergence. Thus the sum of a_p diverges.

The finite products prod_(p>=7)(1+(2/5)a_p) are then unbounded: log(1+(2/5)a_p)>=a_p/5, since (2/5)a_p<1 and log(1+u)>=u/(1+u). Enumerate the primes >=7 as p1,p2,... and choose the first j whose product with all deltas equal to 2/5 reaches or exceeds 8/7. If B is the product of the previous j-1 factors, fix

    delta_(p_i)=2/5 for i<j,
    delta_(p_j)=[8/(7B)-1]/a_(p_j),
    delta_p=0 at the other primes>=7.

By minimality, 0<delta_(p_j)<=2/5. All parameters are rational and

    prod_(p>=7)(1+delta_p a_p)=8/7 EXACTLY.

It is a finite existential choice determined by exact inequalities; no primes are listed, their search is not executed and there is no numerical campaign.

### 11.3. Simultaneous properties and negativity without changes in the window

The resulting product is

    F_norm(s)=zeta(s)R(s),
    R(s)=[1-2^(-s)/2+2^(-2s)/2]
          *prod_(p>=7)[1+delta_p p^(-s)-delta_p p^(-2s)].

R is a FINITE Dirichlet polynomial with rational coefficients and R(1)=(7/8)(8/7)=1. Thus F_norm has a simple pole at 1 of residue EXACTLY 1. Its coefficients N are multiplicative and non-negative; all local powers of level k>=2 still have coefficient 1. Hence

    N(n^m)=1 for ALL n>=1,m>=2 simultaneously,
    ell>=0, supported on prime powers,
    0<=N(n)<=C, C=prod_(p>=7)(1+delta_p)<infinity.

N<=1 is not claimed: one of the high primes has N(p)>1, and N(2)=1/2 remains non-integer. This is the exact difference that avoids the collapse of the ansatz of section 7 and the integral identification of section 10.

Write R(s)=sum_d a_d d^(-s), a finite sum. By multiplying the series and summing coefficients,

    sum_(n<=x)N(n)=sum_d a_d floor(x/d)
                   =x sum_d a_d/d+O(sum_d|a_d|)
                   =x+O(1).

It is precisely the argument of lemma S of R163_102; no novelty is claimed for that counting identity. N is here a non-integer weighted count, not a multiset of integers with integral multiplicities.

All compensating primes are >=7, and their powers also lie outside the window T0 of 007_C. Hence the contacts of F_norm in that window are EXACTLY those of F_all of section 9. With the same primitive F,

    a_(T0)^(ell_norm)(F)=a_(T0)^(ell_all)(F)
                         <-0.00528||F||^2<0.

No additional contact is evaluated, the witness is not readjusted and the quadrature is not repeated. As before, extension by zero preserves this negativity in all larger windows.

### 11.4. Scope and distinction from the antecedents 197

The example proves that residue 1, simple pole, count x+O(1), N multiplicative non-negative and bounded, ALL-POWERS and ell>=0 are not enough for the sign of the fixed-background form unless integrality, N<=1 or another compatibility excluding it is added. Neither the functional equation of the original member nor a small functional defect is attributed to it.

The statement of phase197 on absence of tail compensation corresponds to the Bohr Delta defect, whose factors are >=1. Here ONLY the residue is compensated; neither compensation nor control of that defect is claimed. The relative local factors here are polynomials 1+delta z-delta z^2; this construction is not identified with the specific geometric factors of 197. There is no contradiction with those results nor is a NO-GO deduced on classes demanding their additional hypotheses. The conclusion remains limited to the written hypotheses and does not affect the sign of the original datum.
