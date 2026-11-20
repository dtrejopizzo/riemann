# POWER_CONTACT_BALANCE_021 — Cancellation scale in a single atom k1

Status: **PROVED** negative balance using only contacts2,3,4 and positive bound of the WHOLE tail q>300. **NUMERICAL** balance up to300 with ARCH by quadrature. The sign of W is not decided. Papers untouched; audit020 not modified.

## 1. Object and limited authorization

FAIL2 of SIGNED_BALANCE020 is continued in ONE single atom, F(s)=s/(s+63/2)^212, N211,k1. Read STATE019, ARITHMETIC_DIFFERENCES019, SIGNED_BALANCE020 and its review; index/grid/crossword antecedents are those declared in020. The difference is to measure a few repairing contacts, check the residual scale and bound its tail analytically, not to launch a campaign in N nor optimize fixed rows. By019 ALL contacts are favorable, but their joint magnitude is the obligation.

All energies below are divided by norm². ARCH, POLAR and P_q keep the normalization020. Composite q that are not prime powers contribute0.

## 2. Exact result with three contacts

The bound U020 proves ARCH<−.74. The exact polar satisfies POLAR<−.36. For each prime power q=p^a,

    P_q=2log(p) q^(−32) K_N r_N((63/2)log q),
    K_N=N2^(N−1)/[N!binom(2N−2,N−1)].

This includes both q3 and q4, without approximating Λ nor forgetting the powers. Rational evaluation by Horner proves

    0<P_2+P_3+P_4<.89,
    ARCH+POLAR+P_2+P_3+P_4<−.21.                             (FAIL234)

Hence ignoring the magnitude of ALL remaining contacts does not certify this atom. FAIL234 is not the value of W: the contacts q>=5 are still present and positive.

## 3. NUMERICAL scale diagnostic, not a sign certificate

A single evaluation of the atom, mpmath at45 and65 digits; at65 digits:

    ARCH = −1.0941773847418061369452382637632905
    POLAR= −0.36603632954956029193069220397307442

The integral uses t=tau/u and the exact beta probability

    (2/B(3/2,N−1/2)) t²(1+t²)^(−N−1)dt, t>0,

against m(ut). The quadrature is split at0,.025,.05,.1,.2,.4,1,infinity. The prime powers up to300 are evaluated by the previous polynomial formula. There is no sweep of other parameters.

| Last contact included | ARCH+POLAR+sum P_q, NUMERICAL |
|---|---:|
|2|−1.3854051001619002770|
|4|−.57144083561183200587|
|5|−.22565929156781364596|
|13|−.0046372288392951004140|
|31|−.000029369239646495296493|
|97|−.0000000062920938255926665143|
|293 (all q<=300)|−6.0812131368147274153·10^(−14)|

The45/65 computations agree in the displayed digits relevant for the scale, but there is no quadrature error certificate. It is not claimed that the COMPLETE sum is negative or zero, nor is a sign inferred from the difference of nearly equal quantities. The enumeration stops here: no500/1000 verification nor massive precision is forced to chase a margin.

## 4. Analytic bound of the COMPLETE tail, without additional enumeration

Write r_N(x)=sum_j r_j x^j with known rational coefficients. Using Λ(q)<=log q,

    0<sum_(q>300)P_q
      <=2K_N sum_(j=0)^N |r_j|u^j sum_(q>300)q^(−32)(log q)^(j+1).

For ell>=1, f_ell(x)=x^(−32)(log x)^ell is nonnegative and unimodal on[300,infinito). Panel comparison on the two branches gives

    sum_(q>300)f_ell(q)<=int_300^infty f_ell(x)dx+sup_(x>=300)f_ell(x).

Moreover (log f_ell)'=−32/x+ell/(x log x)>=−32/300. If x0 is a maximum, integrating the bound f_ell(x0+t)>=f_ell(x0)e^(−32t/300) proves sup f_ell<=(32/300)int f_ell. Hence the previous sum is <=(83/75)I_ell, where

    I_0=1/(31·300^31),
    I_ell=300^(−31)(log300)^ell/31+(ell/31)I_(ell−1).

The recurrence uses only positive summands. Substituting the rational upper bound of log300, summing absolute coefficients and operating with Fraction proves

    0<sum_(q>300)P_q<5·10^(−13).                             (TAIL)

The intermediate bound is approximately4.47·10^(−13); only the rational inequality TAIL is used as a theorem. It is a bound of the comb, independent of the numerical computation of ARCH. It does not turn the NUMERICAL table of§3 into a certified interval for W.

## 5. Result and remaining step

FAIL234 and TAIL are exact proofs. The diagnostic locates a cancellation of order-1 components down to a scale of at least10^(−13) in this partial sum. The favorable tail still matters at that scale. The attempt obtains neither W>0 nor W<0 and eliminates no admissible region.

The useful information for the next construction is that the favorable sign of the comb requires keeping its joint cancellation with ARCH and POLAR. Separating those components via coarse bounds no longer settles the balance. This describes the scope of these bounds on this atom; it does not constitute a NO-GO for other arithmetic inequalities or for all finite combs.

Reproduction:

    python3 03-research/phase-211-sign-sandbox/tools/power_contact_balance_021_verify.py
    python3 03-research/phase-211-sign-sandbox/tools/power_contact_balance_021_diagnostic.py 65

The first script is Fraction/exact intervals and PASS. The second is explicitly NUMERICAL, depends on mpmath and certifies no quadrature error.


## Follow-up032: candidate decided

POWER_CONTACT_DECISION_032 and POWER_CONTACT_AUDIT_032 settle this same atom via ARCH without quadrature and contacts up to512 with complete tail: 3.4e−15<W/norm²<4.5e−15. The negative partial up to300 of this note was not total W; the difference comes from omitted favorable contacts, not from a previously proved negative global sign. This note is kept as the historical record of021.
