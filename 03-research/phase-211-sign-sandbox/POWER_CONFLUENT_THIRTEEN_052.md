# POWER_CONFLUENT_THIRTEEN_052 — Real pivot of V13 and adverse contacts in the complementary direction

Status: PROVED, rational certificate PASS and independent review approved in POWER_CONFLUENT_THIRTEEN_AUDIT_052.md. Only confluent V13 of rate63/2; not thirteen arbitrary poles. Papers untouched.

## 1. Result and difference with respect to051

Let u=63/2 and V13={P(s)/(s+u)^13:degP<13}, with causal functions and real coefficients. Keeping ARCH, POLAR and ALL contacts,

    W[f] > ||f||²/4000,   f∈V13 nonzero.                (FULL13)

The additional information is not just another positive block: the pivot complementary to ZERO13 is quantified and the real sign of its contacts2 and3 is identified. In a rational direction minimizing the Schur complement of E2 up to the certified interval error, ARCH+POLAR is positive, while both contacts are adverse. Contact2 consumes almost all of that benefit: it is not a repairing contact in this direction.

Consulted the project rules, ROUTES-TRIED-INDEX, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D, with the Schur/W-lin and STATE051 entries. Reviewed ARITHMETIC_BLOCK007, R12_ENDPOINT048, FULL_TWELVE050 and its audit.051 already deduplicated the abstract Schur formula and showed that positivity in codimension1 does not suffice. The current difference is to evaluate the coupling of THIS real form and its contacts, in the SINGLE next block V13, without sweeping dimensions or rates.

## 2. E2 already positive, but the tail majorant007 does not fit

In the orthonormal Laguerre basis e_0,...,e_12 of048, E2=ARCH+POLAR+contact2 has real Toeplitz matrix T2. The exact certificate proves

    E2[f] > (3/10000)||f||².                             (E2)

The smallest floating eigenvalue, used only to diagnose this single block before certifying it, was approximately0.000305571086. That value is not used in the proof.

The direct adaptation to dimension13 of the tail majorant from3 of007 gives approximately0.002331781986, larger than the previous margin. The new degree12 requires justifying monotonicity with log3>16/15, instead of the bound log3>1 that sufficed for degree11: for 0≤r≤12,

    1/log3 +63r/(63log3−40) < 32.

The bound16/15 is obtained from the first positive atanh terms for log3. This insufficiency of the majorant does not claim that the real tail has that size nor that E2 is insufficient in the complete form.

EXACTLY the next contact3 was then retained, as planned; no other contacts were sought.

## 3. E23 and complete tail from4

Write E23=E2−(2log3/sqrt3)c(log3). The bands of contact n are

    diagonal: −2(logn)n^−32,
    band k≥1: −(logn)n^−32 [L_k(63logn)−L_(k−1)(63logn)],

for n=2,3; the factor sqrt(n) is already absorbed exactly together with exp(−u logn). The logarithm of3 is enclosed by atanh with argument1/2 and positive remainder, without floating exponentials.

The verifier tools/power_confluent_thirteen_052_verify.py extends007 to thirteen bands. ARCH uses the same power sums from16 on and Euler tails with explicit remainder; POLAR is exact rational. The centers of T2 and T23 have denominator10^15 and their operator error is<ε=10^−10, by row sums. Two rational LDLs verify

    Tc2−(3/10000+ε)I>0,
    Tc23−(7/25000+ε)I>0.

Thus E23[f]>(7/25000)||f||²=0.00028||f||².

For the tail n≥4 the polynomial cancellation of007 is kept: all coefficients of

    (−1)^k [L_k(40+y)−L_(k−1)(40+y)], 0≤k≤12,

are nonnegative (L_−1=0). Each term is bounded using Λ(n)≤logn and the first term plus the integral of

    (logx)(63logx−40)^r x^−32, x≥4, 0≤r≤12.

The logarithmic derivative has negative sign because log4>4/3 and

    1/(4/3)+63·12/(63·4/3−40)<32.

With log4<7/5, the integrals are evaluated exactly via the change x=4exp(t) and the moments ∫_0∞t^r exp(−31t)dt=r!/31^(r+1). The result is a rational bound per band; the certified row sum is

    ||tail_(n≥4)|| <1/100000=0.00001.                    (TAIL)

The decimal evaluation of that majorant is approximately0.0000090179619783; the proof uses only fractions. The tail includes ALL remaining primes and prime powers. From E23 and TAIL,

    W[f]>(7/25000−1/100000)||f||²
         >||f||²/4000,

proving FULL13.

## 4. Real complementary pivot and error of its crossings

Let ell_j=(−1)^j and h=ell, with ||h||²=13. The restriction ZERO13 is H=ell⊥, since the Laplace evaluation at0 is a multiple of Σ(−1)^jz_j. Its rational columns are

    C_i=e_i−(−1)^i e_12, i=0,...,11.

For a matrix T, define

    A=CᵀTC, g=CᵀTh, d=hᵀTh,
    sigma(T)=(d−gᵀA^−1g)/13.

It is the minimum of the form on h/√13+H. It is not the smallest eigenvalue of T. The subblock A is positive by the previous results; the computations here also check its pivots when solving it. For central T2:

    d/13 ∈(0.12337,0.12338),
    gᵀA^−1g/13 ∈(0.12296,0.12298).

The cancellation of both terms leaves a small margin. To enclose the pivot of the exact matrix one computes sigma(Tc−εI) and sigma(Tc+εI). The orientation is valid because sigma is the infimum of forms evaluated on the SAME affine space, and the restriction remains positive. The certificate obtains

    0.0004054 <sigma(E2)<0.0004055,
    0.0003834 <sigma(E23)<0.0003836.                     (PIVOTS)

Contact3 reduces the pivot; it does not repair it.

For the complete form, TAIL implies Tc23−(ε+0.00001)I≤TW≤Tc23+(ε+0.00001)I. Applying the same infimum principle gives

    0.0003 <sigma(W)<0.0005.                             (FULL-PIVOT)

This is a real control of the crossing with ALL contacts, not a conclusion drawn only from the codimensional positivity of050.

## 5. Which terms sustain and consume this margin

Let x=h−CA^−1g be the RATIONAL vector defined by the center Tc2, without rounding its coordinates. Its component on ell is h, and the previous minimum is xᵀTc2x/13. Evaluating the original interval components on this SAME vector, the verifier proves

    ARCH[x]/13+POLAR[x]/13 ∈(0.01839,0.01841),
    contact2[x]/13 ∈(−0.01800,−0.01798),
    contact3[x]/13 <0.                                 (COMPONENTS)

These figures are energies of y=x/√13, whose coefficient on the unit complement h/√13 is1; y does NOT have norm1. They are not Rayleigh quotients divided by ||x||². Minimizers of distinct components are not mixed. The fractions and their products are kept exact. The vector minimizes the Schur complement of the CENTER, while PIVOTS encloses the minimum of the exact form; no unproved exact optimality is attributed to x.

The datum reveals two different roles of contact2. ARCH+POLAR is indefinite on V12 by the audited test006, hence also on V13 by inclusion; there arithmetic2 repairs other directions. However, in the complementary direction of this Schur complement,2 is adverse and almost cancels the positive AP.3 is also adverse. Keeping3 exactly improves the certificate by avoiding the excess of the absolute tail majorant007, NOT because3 contributes positive energy.

This requires controlling the crossings and the direction of each contact, instead of assuming that the same prime repairs in all directions. The full margin remains positive thanks to the quantified balance and the small tail from4.

## 6. Scope

The sign of CONFLUENT V13 and its pivot with respect to ZERO13 are decided, with all the arithmetic. The coverage050 for twelve arbitrary poles is kept. Positivity for thirteen arbitrary poles is not inferred: an appropriate complete gain of fourteen poles or an orbit extension not proved here would be missing. V14,V15,... were not pursued nor was a campaign of contacts carried out.
