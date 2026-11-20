# POWER_SIGNED_BALANCE_020 — The first contact does not suffice for the balance k1

Status: **PROVED**, concrete quantitative obstruction to the balance with only contact2; sign of the FULL form at this point **not decided here**. Papers untouched.

## 1. Corpus and new reason

Consulted the project rules, STATE019, ARITHMETIC_DIFFERENCES019 and its audit, TABLE_DESCENT018, the routes index (Euler/Möbius/moments), master grid and CROSSWORD-TO-D.md (rounds018/019, test repaired by contact2 in006). The positive sign of the WHOLE comb for k1,N<=211 is proved in019. That sign does not give its magnitude. Nor is the particular vector006, where contact2 did repair an archimedean-polar loss, extrapolated.

The specific difference consists in confronting that magnitude with an analytic bound of ARCH for an atom of the SAME signed column. An obstruction is proved to the concrete lemma «the first positive contact suffices to repair ARCH+POLAR along the column k1 up to211». No prohibition is proved on all finite combs nor on other arithmetic inequalities. There is no certificate campaign nor new root counts: a single point is used, N=211,u=63/2,k=1, with the whole rest of the comb kept as positive.

## 2. An analytic archimedean bound useful at variable N

Let F_(N,1)(s)=s/(s+u)^(N+1), N>=2, and normalize its Fourier density to a probability. Write T=tau/2. The beta integral gives exactly

    E T² = V_N = 3u²/[4(2N−3)].                              (V)

For a>0, the elementary Euler summation formula for psi on Re z=a gives

    psi(z)=log z−1/(2z)+R(z),   |R(z)|<=1/(2a).               (EM)

For example R is, up to sign, the integral of ({t}−1/2)/(z+t)²; its modulus is bounded by (1/2)int_0^infty(a+t)^(-2)dt. No sign of complex R is needed.

Translating four steps from 1/4+iT to a+iT with a=17/4, taking real parts and using (EM),

    Re psi(1/4+iT)
    <= (1/2)log(a²+T²) − a/[2(a²+T²)] + 1/(2a)
       − sum_(j=0)^3 b_j/(b_j²+T²),     b_j=j+1/4.

The functions log(A+x) and −b/(b²+x) are concave for x>=0. Jensen and (V) prove, UNIFORMLY for N>=2,u>0,

    ARCH_(N,1)/norm² <= U_N(u)
      := (1/2)log(a²+V_N) − a/[2(a²+V_N)] + 1/(2a)
         − sum_(j=0)^3 b_j/(b_j²+V_N) − log pi.              (U)

This is a real one-sided bound of the archimedean energy, not a gaussian approximation. At N=211,u=63/2, rational verification of logarithms gives

    U_211(63/2)<−74/100.                                    (A)

## 3. Exact magnitude of contact2

Use the polynomials and normalization already proved in019:

    p_N(x)=sum_j (2N−j)!x^j/[2^(N−j)(N−j)!j!],
    r_N=p_N−2p_N'+p_N'',
    C_(N+1)''(t)=e^(−ut)r_N(ut)/[2^(N+1)u^(2N−1)N!].

The beta norm of the atom is

    norm²=binom(2N−2,N−1)/[N 2^(2N)u^(2N−1)].               (NORM)

Define K_N=N2^(N−1)/[N!binom(2N−2,N−1)]. The normalized autocorrelation is −e^(−ut)K_Nr_N(ut). At u=63/2 the contact q=2 simplifies EXACTLY, since 2^(−u)=2^(−31)/sqrt2:

    P_2/norm²
      = [log2/2^31] K_N r_N((63/2)log2).                    (P2)

There is no radical nor tail remainder in (P2). The identity COEF019 gives all rational coefficients of r_N. Evaluating (P2) via rational intervals for log2 proves, at N=211,

    0<P_2/norm²<75/1000.                                   (B)

The computation uses Horner with rational endpoints WITHOUT rounding at each step. Prematurely rounding factorially small coefficients before raising x to degree211 would lose information; the verifier avoids that loss. Only the final evaluation returns to the intervals of003.

## 4. Exact balance and scope

For k=1 the polar is strictly negative:

    POLAR=2F(−1/2)F(1/2)=−1/[2(u²−1/4)^(N+1)]<0.

Combining (A),(B), on this concrete atom,

    [ARCH+POLAR+P_2]/norm² < −.74+.075 < −.66.               (FAIL2)

By019, for N211,u31.5 ALL other contacts are positive. The identity that keeps the full real obligation is

    W = ARCH+POLAR+P_2 + sum_(q>=3) P_q,
    P_q>=0,   sum_(q>=3)P_q absolutely convergent.

FAIL2 does not say that W is negative and does not allow erasing the contacts q>=3. It proves exactly that a lower bound based only on P_2 and on ignoring the other favourable summands can NOT repair this atom: even the real value of the form with only that contact is negative. Any positive balance here must use more quantitative information from the remaining comb. This distinguishes the situation from case006 repaired by contact2.

No new W sign row is recorded nor is table coverage extended. The next substantive step requires a one-sided bound of several contacts or of their joint mass that keeps the compensations with ARCH and the polar. The argument does not turn an identity into that bound.

Verifier: tools/power_signed_balance_020_verify.py, Fraction arithmetic and exact intervals inherited from003; PASS. A single evaluation N211, not a sweep. The bound U is proved for variable N, but the obstruction FAIL2 is only claimed at the declared point.
