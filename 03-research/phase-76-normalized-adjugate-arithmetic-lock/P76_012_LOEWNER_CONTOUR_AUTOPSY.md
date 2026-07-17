# P76.012 - Loewner contour autopsy

## Canonical contour formula

P76.011 gives

```text
R_S(z)-I_R(z)=D_L(z)G_L^can(z),

G_L^can(z)
=(1/(2 pi i)) int_Gamma
 R_S(zeta)/(D_L(zeta)(zeta-z)) dzeta.
```

This is an exact, zero-independent Lagrange remainder formula.  The hoped-for
mechanism was that `D_L(gamma)G_L^can(gamma)` would be an all-orders tail,
leaving a finite signed cancellation between `m_S` and `I_R`.

## Numerical falsification

At `lambda=6`, the exact identity is

```text
S_L(gamma)c(gamma)
=m_S(gamma)+I_R(gamma)+D_L(gamma)G_L^can(gamma).
```

The multiprecision decomposition gives:

```text
N    |c|       |m_S|      |I_R|       |D G|       |S c|
3    2.7e-8    7.6e-8     8.55e3      8.55e3      1.2e-8
4    4.1e-11   1.5e-8     2.81e4      2.81e4      1.9e-11
5    2.1e-13   7.2e-9     4.74e4      4.74e4      9.4e-14
6    1.6e-15   5.5e-9     4.00e4      4.00e4      7.4e-16
8    7.7e-23   7.5e-7     2.17e2      2.17e2      3.5e-23
9    2.0e-23   3.3e-6     4.43e1      4.43e1      9.2e-24
```

For `N<=8`, `gamma_1` is outside or at the edge of the pole mesh and the
large terms exhibit the expected extrapolation/Runge amplification.  At
`N=9`, `gamma_1` is inside the mesh, but the same mechanism remains: the
canonical interpolation polynomial and contour remainder are individually
of order `10^1`, while their signed sum must be known to roughly 21 digits.

Thus neither `I_R` nor the contour term is a small tail in the resolved
regime.  Bounding either absolutely destroys the cancellation.

## Exact obstruction

The contour formula inserts

```text
R_S(zeta)=S_L(zeta)c(zeta)-m_S(zeta)
```

under the integral.  Any contour estimate sharp enough to recover the
observed critical value must retain the signed eigenline Cauchy cancellation
on the contour.  Replacing it by a norm bound loses factors between `1e21`
and `1e25` in the tested cases.

Consequently:

```text
LOEWNER-CRIT-REM
<=> signed contour cancellation for R_S
<=> EG_LOCK / CRIT-NUM-DIV
```

unless an additional arithmetic identity evaluates the whole contour
integral before estimation.  No such identity is supplied by polynomial
interpolation itself.

## Pick/Padé warning

Standard convergence theorems for Loewner and multipoint Padé approximants
obtain sign, monotonicity, or pole localization from positivity of the
associated Pick/Loewner matrices.  Here

```text
H_L=2 diag(C_L)-(2/L)Loew(S_L)
```

is exactly the finite Weil quadratic form in the CCM cell basis.  Positivity
of these matrices on an exhausting family of meshes is the finite form of
Weil positivity.  Using it uniformly would assume an RH-equivalent input.

Therefore a generic Pick/Padé convergence theorem is not an admissible
closure of Omega7.  It becomes admissible only if a new arithmetic property
strictly weaker than positivity controls the one signed critical channel.

## Verdict

The Loewner identity is retained as a canonical algebraic representation,
but the contour remainder route is closed as an independent forcer:

```text
proved: exact diagonal-Loewner and interpolation identities;
falsified: canonical contour remainder is separately all-orders small;
forbidden: invoke global Pick/Loewner positivity;
open: find a one-channel signed arithmetic identity not equivalent to EG_LOCK.
```
