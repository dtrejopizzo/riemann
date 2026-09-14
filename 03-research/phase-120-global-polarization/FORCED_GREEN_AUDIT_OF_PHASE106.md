# Forced-Green audit of the phase-106 Gamma pushout

Status: exact normalization audit and repaired candidate. This does not prove
the primitive contraction.

## 1. The discrepancy

The phase-106 density is

    c(u)=e^(-u/2)/(1-e^(-2u))
        =sum_(n>=0) e^(-(2n+1/2)u).

For a translation character of frequency `tau`,

    integral_0^infty c(u)(1-cos(tau u))du
      =sum_(n>=0) tau^2 /
        ((2n+1/2)((2n+1/2)^2+tau^2)).

Writing `a_n=n+1/4`, the forced positive Gamma multiplier in paper 42 is

    g_Gamma(tau)
      =sum_(n>=0) (tau/2)^2 /
        (a_n(a_n^2+(tau/2)^2))
      =2 integral_0^infty c(u)(1-cos(tau u))du.

The original 106.198 definition used

    sqrt(2 c(u)) (I-V_u),

whose squared multiplier is `4 integral c(1-cos)`, namely
`2 g_Gamma`. Therefore it fails the forced-Green test by the exact factor
two.

## 2. Geometric origin of the repair

The factor is not repaired by fitting against `B_nuc`. The source is the
change of carrier:

- 106.176 computes the even energy on the two sign components of `R^x`;
- paper 42 works on the positive multiplicative carrier `R_+^x`;
- Connes–Consani identify the periodic orbit as
  `E_p(R)/<-1>`, where `-1` exchanges the two real components.

The orthogonal conditional expectation onto invariants of a finite group is

    P_+ = (1/2)(1+sigma).

With normalized Haar measure, descending a sign-invariant energy from the
two-component cover divides it by two. Hence the corrected boundary gradient
is canonically

    G_Gamma F(u) = sqrt(c(u)) (I-V_u)F,

and its multiplier is exactly `g_Gamma`. This is the correction now recorded
in 106.198 and inherited by 106.199.

## 3. Equivalent Hardy-spin realization

The same correction gives the positive square root

    (W_Gamma F)_n^(hat)(tau)
      = (tau/2)/sqrt(a_n(a_n^2+(tau/2)^2)) F^(hat)(tau),
      a_n=n+1/4.

This realizes the corrected reservoir on the quarter-twisted positive Hardy
tower. The equality of the heat and Hardy realizations follows term by term
from `2a_n=2n+1/2`.

The offset `1/4` has a structural candidate derivation: the unique central
half-density contributes `s=1/2`, and the even real Gamma factor uses `s/2`.
The remaining task is to construct that quarter-twisted Hardy line from the
absolute phase circle, rather than importing the Gamma factor to label it.

## 4. What phase 106 already contributes to P3

After the sign normalization, 106.198 constructs:

- a positive closed Gamma boundary gradient;
- a strictly positive operator `K_Gamma` and its minimum-norm right inverse;
- finite positive pushouts compatible under adjoining places;
- charge-dependent fibers `K_Gamma(E-log q)` which retain prime phases;
- a Hilbert direct limit, as shown in 106.199.

This is stronger than the initial phase-120 audit recognized: it supplies a
positive source and finite/cofinal transition isometries. It is nevertheless
not the physical P3 attachment. The subsequent central-weight audit finds
that its quadratic mass is `log(p)/p^k`, rather than the row-(c) mass
`log(p)/p^(k/2)`, and that its constant compliance is `kappa_infty` rather
than `m_0`. Thus it is a source model to reuse, not a calibrated solution.

It still does not supply the decisive statement. The phase-106 documents
leave open the pullback through the derived CCM localization and equality of
the resulting alternating/intersection form with the nuclear form. In the
phase-120 language, they do not prove that the local load attachment is a
compression of a unitary whose defect is `D_out-y_N y_N^*`.

## 5. Next exact test

Reconstruct the corrected phase-106 pushout on the active charge fibers
`q=2,3` and evaluate its Schur metric in the same finite basis used by the
`T=log 2` certificate. The matrices must agree entrywise with the forced
Gamma compression, without another normalization. If they agree, repeat with
`q=2,3,4` at `T=(1/2)log 5`.

The archimedean half of this test is now complete. On the `T=log 2`,
refinement-4 piecewise-constant mesh, direct quadrature of

    integral_0^infty c(u)(2 Gram-S_u-S_u^*)du

agrees with paper 42's independently assembled forced Gamma matrix with
maximum entrywise error `6.44e-14` and relative Frobenius error `6.64e-14`.
The former two-component normalization misses by `0.982`. This is reproduced
by `scripts/p3_log2_gamma_calibration.py`.

What remains at this gate is not the Gamma multiplier: it is a rebuilt map
with Hodge amplitude `log(p)/sqrt(2pi) p^(-k/4)` carrying the local
contact/Tate loads into this corrected reservoir, and the comparison of its
Schur defect with the physical `D_out-y_N y_N^*`.
