# POWER_PACKET_SCOPE_AUDIT_009 — Rational Tate family, central packets and scope of the bridge

Status: PROVED concentration, identities and bridge audit; OPEN finite arithmetic inequality. No paper is modified and no external spectral reduction is used.

## 1. Concrete antecedents, with their scope

Read ROUTES-TRIED-INDEX/06 (R2 and R5), Paper46 lem:wit-conc, prop:wit-Egamma, prop:Egamma-exact and rem:critical; phase188/L2_BUILD_008_GROUND_STATE_AND_T0.md, L2_BUILD_009_ARITHMETIC_INPUT_FOR_T0.md, L2_BUILD_010_REGULARIZED_CENTRE_VALUE.md and N_BUILD_013_E_GAMMA_C_COLLAPSES.md. Only their formulations of form and fluctuation are considered; arguments of another nature are not used to dismiss routes.

R2 works with a compact function clamped by window, ground/near-ground of an archimedean form. R5 works with compact packets concentrating at one frequency. The present family f_n=(D²-1/4)y^(n-1)e^(-uy), u31.5 fixed, is not identical to either of them for finite n: it has an exponential half-line, rational poles and autocorrelation exponential times polynomial. However its central limit and the fluctuation threshold are of the same type E0 already recorded; no new asymptotic slack appears.

## 2. Proved central concentration and coinciding threshold

Its spectral probability p_n is proportional to (tau²+1/4)^2/(u²+tau²)^n. The beta formulas for the base measure of POWER_PRIME_PATTERN_FALSIFIER_008 show, for fixed u and large n,

    E_n tau² = u²/(2n)(1+O(1/n)),
    E_n tau^4 = O(n^-2).

This is obtained by expanding the exact moments M2,M4,M6 (and M8 for the second line) in the reweighting quotients. In particular p_n converges weakly to delta0, and

    rho_n(t)=c_fn(t)/||f_n||² ->1

locally uniformly: 0<=1-rho_n(t)<=t² E_n tau²/2. The global inequality m0<=m(tau)<=m0+17tau² gives Arch_n->C0; the bounded multiplier 1/(tau²+1/4) gives e_n->4.

The Tate identity eliminating the main term also holds here, because the exponential integrals converge absolutely and A=B=0. If S_n is the normalized comb and Fcal_n its fluctuation relative to density2e^(t/2), then

    S_n=Fcal_n-e_n,
    W_n=Arch_n+e_n-Fcal_n.

Hence the threshold of the limit problem is C0+4, exactly the centre E0 of R2/R5. The necessary sign condition produces limsup Fcal_n<=C0+4. It is not proved here that this limit condition suffices for the finite signs, nor that the arithmetic mean converges. The local convergence of rho_n to1 does not allow interchanging the infinite comb sum: its weights are not uniformly summable in n. That is a real mathematical obligation, not a reason to abandon the finite case.

## 3. Different finite lever: an exact recurrence that still requires a sign

For n sufficiently large define

    J_n(t)=integral_R exp(i tau t)(tau²+1/4)^2/(u²+tau²)^n d tau,
    rho_n(t)=J_n(t)/J_n(0), w(tau)=1/(u²+tau²).

Normalization and differentiation under the integral give

    p_(n+1)=w p_n/E_n[w],
    J_(n+1)(t)=-(1/(2nu)) partial_u J_n(t),
    rho_(n+1)(t)-rho_n(t)
        =-partial_u rho_n(t)/[2nu E_n(w)].

The step in n is therefore explicit, with normalization constants rational in u thanks to the beta integrals. For the archimedean part,

    Arch_(n+1)-Arch_n=Cov_n(m,w)/E_n(w)<=0,

because m increases and w decreases in |tau|. For the complete form,

    W_(n+1)-W_n
       =Arch_(n+1)-Arch_n
        -sum_(q>=2)2Lambda(q)q^-1/2[rho_(n+1)(logq)-rho_n(logq)].

Each sum at finite n converges absolutely by the exponential-times-polynomial decay. It has no automatic sign. A one-sided inequality controlling this difference, or a renormalized ratio preserving nonnegativity, would be a different advance from the mere limit value E0. The targeted searches did not find a previous proof of this exact step for the present rational family. This novelty is local and limited; the reweighting and covariance identities are elementary and known.

It is not proposed to require W_n to be increasing: the appropriate direction of an induction must be proved and compatible with its margins. Nor would the sign of this single chain by itself control all numerators of each degree.

## 4. Re-audit of the bridge: no defect found

POWER_BRIDGE_002 was reviewed again along its two routes. In the norm B, the translations G(y+logn) are contractions of the intrinsic norm H^(1/4), and the coefficients n^-5/4 are summable. Z is not differentiated term by term: the potentially divergent series of derivatives is avoided. Extension by zero for t<1/2 is standard and controls the jump at the endpoint; the fractional Hardy constant is invoked explicitly as a known tool.

For PW_N C² data, two integrations by parts in h and xh give rho,rho'=O(X^-2); the difference split proves membership in B without assuming a third derivative. The C1 approximation after z=e^-y uses smooth compact functions and produces exactly exponents32+k; it converges strongly in B. Continuity of gamma, comb and moments is controlled separately.

For an arbitrary smooth compact test F, translating it to support(0,L) preserves the complete form: the autocorrelation is invariant and the two moments are multiplied by reciprocal factors. The inversion u(y)=sum mu(n)n^-1/2 h(y+logn) is FINITE, and applying Z the divisor sum is also finite, so that Zrho=h exactly. The inverse datum is smooth up to0 and compact on the half-line, so it belongs to B. It is not required to vanish at0. This whole step holds without assuming the sought sign.

Thus positivity for ALL sizes of the fixed ladder would indeed suffice for all compact tests and, by the form kernel in each window, for the relevant domain. It extends from real to complex tests by separating real and imaginary parts, since the form has a real kernel. The bridge does not supply the sign of the ladder, does not justify extrapolating V12 to more modes and does not make dense the union of small planes already positive.
