# POWER_MOVING_BALANCE_036 — Mass window and real energy window

Status: **PROVED**, independent review approved in POWER_FRONTIER_AUDIT_036.md and verifier PASS reproduced. FIXED rate u=63/2. Papers untouched.

Main result to review: although the Abelgamma law P_d concentrates mass at m~sqrt(N), its tilts by the COMPLETE polar and arithmetic contributions concentrate energy at

    m/(N−1)->1/32.

Exact positive representations and uniform exponential bounds are given. It is not claimed that the SIGNED functional t_m has that same window: its internal cancellation may modify it. No total sign of W is claimed.

## 1. Corpus and precise difference

Read directly ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md and STATE035; also SIGNED_TRANSFORM035, JOINT_SCALE016, LOW_TABLE018, COEFFICIENT_BALANCE033 and their audits. The failure of uniform exponential weights at fixed rate016 and the insufficiency of absolute budgets018 are antecedents, not new conclusions here.

The difference is to study the SPECIFIC POSITIVE law035 and its tilts by REAL components of the form, including the WHOLE Lambda comb. Where its energy goes is proved, not only where the probability of an auxiliary measure goes. The lower arithmetic comparison is elementary and is proved, without assuming a fine error bound for psi_Lambda. No prime weight is changed and no campaign over N is made.

The obstruction is limited to the following erroneous step: "the tail outside Csqrt(N) has small probability, so the polar and prime contributions there may be omitted separately". That step is false for the real components. A signed compensation performed BEFORE separating them is not ruled out.

## 2. Exact law and positive components

Let d=N−1>=2. Keep035:

    a0=a1=1, a_(m+1)/a_m=2(d−m)/(2d−m), a_(d+1)=0,
    delta_v_m=v_m−v_(m+1), v_m=a_m/(2d−m),
    P_d(m)=m(m+1)delta_v_m/2, sum_m P_d(m)=1,
    t_m=T_m/[m(m+1)/2], A_N=W[g_N]/norm²=sum_m P_d(m)t_m.

For S_j(y)=e^(−uy)sum_(l=0)^j(uy)^l/l!, write p_j>0 for its linear polar contribution and pi_j>0 for the MODULUS of its comb (its sign in W is negative). Let

    p_m^T=[sum_(j=1)^m j p_j]/[m(m+1)/2],
    pi_m^T=[sum_(j=1)^m j pi_j]/[m(m+1)/2].

They are components of the same profiles defining t_m, without altering their contacts. By linearity of finite mixtures,

    P_N=sum_m P_d(m)p_m^T,
    Pi_N=sum_m P_d(m)pi_m^T,

where P_N is the REAL normalized polar part of g_N and Pi_N is the modulus of its REAL COMPLETE comb. Define the EXACT tilts

    Q_d^P(m)=P_d(m)p_m^T/P_N,
    Q_d^Pi(m)=P_d(m)pi_m^T/Pi_N.                         (ENERGY)

Both are normalized positive laws. They are not the sign law of the complete functional.

## 3. A base tilt with exact binomial representation

Set

    r=u/(u−1/2)=63/62, s=u/(u+1/2)=63/64,
    A_d(r)=sum_(m=0)^d a_m r^m,
    Qtilde_d(m)=a_m r^m/A_d(r).

The term a0 is INCLUDED. The beta integral gives exactly

    A_d(r)=(2d+1)int_0^1 q(t)^d dt,
    q(t)=(1−t)[1+(2r−1)t].                              (BETA)

Indeed a_m=(2d+1)binom(d,m)2^m int_0^1 t^m(1−t)^(2d−m)dt; summing the binomial proves BETA.

More precisely Qtilde is the mixture of a Binomial(d,p(t)) law against the density proportional to q(t)^d on[0,1], where

    p(t)=2rt/[1+(2r−1)t].                                (BINOMIAL)

Multiplying the density by the binomial probability reconstructs each a_m r^m. It is an exact POSITIVE representation, not a formal stationary-point argument.

For the REAL values present,

    tau=1/64,
    lambda=3969/3968=(1−1/3969)^(-1),
    alpha=(64/63)^2,
    q(t)=lambda[1−alpha(t−tau)^2],
    p(tau)=1/32.                                        (MODE)

The maximum is unique. lambda is EXACTLY the exponential base of the gamma polar part, not just a Gaussian approximation.

## 4. Uniform quantitative localization of Qtilde

For d>=4096, the interval |t−tau|<=63/(128sqrt(d)) is contained in(0,1). There q(t)^d>=lambda^d(1−1/(4d))^d>=3lambda^d/4. Hence

    int_0^1q(t)^d dt>=189lambda^d/[256sqrt(d)].

Outside |t−tau|<eta, the numerator is bounded by lambda^d exp(−alpha d eta²). Thus the mixture satisfies

    Prob(|t−tau|>=eta)
      <=(256/189)sqrt(d)exp(−alpha d eta²).

Moreover |p'(t)|<=2r<3. If |t−tau|<epsilon/6, then |p(t)−1/32|<epsilon/2. The elementary binomial Chernoff bound gives Prob(|M/d−p(t)|>=epsilon/2)<=2exp(−d epsilon²/2). One obtains

    Qtilde_d(|M/d−1/32|>=epsilon)<=B_d(epsilon),
    B_d(epsilon)=(256/189)sqrt(d)
                  exp(−1024d epsilon²/35721)
                       +2exp(−d epsilon²/2),             (CONCENTRATION)

for d>=4096 and0<epsilon<=1/16. A proof of the binomial bound uses the second derivative of the logarithm of the Bernoulli mgf, which is a variance<=1/4, and then optimizes Chernoff; it needs no normal approximation.

## 5. The real POLAR energy has the same localization

The polar contribution of S_j is exactly

    p_j=4[r^(j+1)−s^(j+1)]<=4r^(j+1).

Since delta_v_m<=a_m/d and m<=d,

    P_d(m)p_m^T=delta_v_m sum_(j=1)^m j p_j
      <=C0 a_m r^m,
    C0=4r²/(r−1).

We used sum_(j=1)^m j r^(j+1)<=m r^(m+2)/(r−1). On the other hand, the Laplace integral of rho_N gives

    P_N=2A_d(r)/(u−1/2)+2A_d(s)/(u+1/2)
        >=2A_d(r)/31.

Hence for ANY set of indices B,

    Q_d^P(B)<=3969 Qtilde_d(B).                           (POLAR-DOM)

The factor3969 is obtained exactly from C0·31/2. Combined with CONCENTRATION, this proves M/d->1/32 under the REAL polar energy, without computing new N.

The exact gamma formula confirms the exponential scale:

    P_N=(4sqrt(pi)/u) Gamma(N)/Gamma(N−1/2) lambda^N.

The Jensen bounds sqrt(N−1)<=Gamma(N)/Gamma(N−1/2)<=sqrt(N−1/2), together with BETA, give log(P_N)/N->loglambda and log(A_d(r))/d->loglambda. Only a phase comparison is used, not a relative precision between prime and polar.

## 6. ELEMENTARY lower arithmetic bound, proved

Let psi_Lambda(x)=sum_(q<=x)Lambda(q). For integer n, each valuation of binom(2n,n) is bounded by the number of powers of that prime<=2n, since each difference of floors in Legendre's formula is0 or1. Hence

    psi_Lambda(2n)>=log binom(2n,n)
                   >=2nlog2−log(2n+1).

The second inequality uses that the central coefficient is the maximum among2n+1 coefficients whose sum is4^n. For real x>=32 take n=floor(x/2). Thus

    psi_Lambda(x)>=(x−2)log2−log(x+1)>=x/2.

The last comparison holds at32 because30log2−log33>16, and its difference from x/2 has derivative log2−1/2−1/(x+1)>0 for x>=32. One may use log2>2/3 and log33<4 to verify it. For1<=x<=32, the trivial positivity of psi gives, on the WHOLE half-line,

    psi_Lambda(x)>=x/2−16.                              (CHEB)

This bound is not cited without proof nor inferred from a table of primes.

With w_N=x^(-1/2)rho_N(logx), H_N=−w_N'>0 and w_N(1)=1, complete integration by parts gives

    Pi_N=2int_1^infty H_N(x)psi_Lambda(x)dx
         >=int_1^infty xH_N(x)dx−32
         =Lplus_N−31,
    Lplus_N=int_0^infty e^(t/2)rho_N(t)dt.

Since P_N=2(Lplus_N+Lminus_N) and Lminus_N<=2 by rho_N<=1,

    Pi_N>=P_N/2−33.                                     (PRIME-LOWER)

This uses the REAL Lambda and its WHOLE comb. For ALL N>=2^20, P_N>132 and hence Pi_N>=P_N/4. A sufficient minorant for the threshold is verified without evaluating the datum W: P_N>=(4/u)lambda^N and the positive expansion lambda^N>=[N(N+1)/(2·3969²)] already exceeds132 at the threshold, growing afterwards.

## 7. Localization of the COMPLETE arithmetic energy

No fine arithmetic upper bound is needed. The trivial inequality psi_Lambda(x)<=xlogx and the decreasing character of w_j=x^(-1/2)S_j(logx) prove

    pi_j=2int w_j dpsi_Lambda
      <=2int_0^infty(t+1)e^(t/2)S_j(t)dt
      <=4[1+(j+1)/31]r^(j+1).

The integrations by parts have vanishing boundary terms; the last integrals are finite gamma sums. Thus

    P_d(m)pi_m^T<=C0[1+(d+1)/31]a_m r^m.

For N>=2^20, PRIME-LOWER and P_N>=2A_d(r)/31 imply

    Q_d^Pi(B)
      <=15876[1+(d+1)/31]Qtilde_d(B).                    (PRIME-DOM)

The factor15876 is2·31·C0. CONCENTRATION dominates this polynomial factor: M/d->1/32 ALSO under the energy of the REAL COMPLETE arithmetic comb. Lambda has not been truncated or modified.

Moreover Pi_N lies between P_N/4 and C0[1+(d+1)/31]A_d(r), so

    log(Pi_N)/N->log(3969/3968).

The exponential phase of the two components coincides. Neither Pi_N/P_N->1 nor a bound on the signed residue is deduced from this equality of phases.

## 8. Precise obstruction and return to compensation

For any fixed C, the window M<=Csqrt(d) lies outside |M/d−1/32|<1/64 when d>=(64C)². POLAR-DOM/PRIME-DOM and CONCENTRATION prove

    Q_d^P(M<=Csqrt(d))->0,
    Q_d^Pi(M<=Csqrt(d))->0.

By contrast, P_d has scale sqrt(d) by035. Hence the mass law does NOT allow omitting the tails of these two energies after separating them: almost all of the polar energy and almost all of the real comb lie in the LINEAR band m~N/32.

ARCH remains uniformly bounded: the time profiles of the mixture lie between e^(-ut) and1, so their ARCH lies between m(0) and the exponential energy a(u). The two phase components lambda^N cannot be treated as small errors deduced from the tail probability of P_d.

This is an obstruction to the separated procedure indicated in§1, not to the complete average t_m. A cancellation INSIDE t_m before averaging could recover a different window; that is not refuted. If prime and polar are separated, their real compensation must be preserved in the energy band m~N/32, with the magnitudes quantified here. The previous identity018 cancelling the main term is not sold as a new solution: it leaves a signed arithmetic residue that still has to be bounded.

Neither negative nor positive W for all N, a new data region nor closure of Paper47 is claimed. No campaign of indices is continued. The useful result is to localize quantitatively where the probabilistic discard fails and where the cancellation must be preserved.

## 9. Verification

The script tools/power_moving_balance_036_verify.py compares exactly the MODE constants, exponents, domination prefactors, the CHEB endpoint and a sufficient monotone threshold. It does not compute W at new N, does not enumerate primes nor traverse profiles. Result PASS. The uniform localization and the arithmetic comparisons are proved analytically above. The independent audit confirms the representations, constants, arithmetic bound and the scope limited to components. Papers untouched.
