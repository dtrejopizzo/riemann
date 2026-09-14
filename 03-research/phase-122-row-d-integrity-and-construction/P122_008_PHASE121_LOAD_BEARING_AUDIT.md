# P122.008 — phase-121 load-bearing audit

## Verdict

Phase 121 constructed several faithful coordinates for the missing
equality-state obstruction.  It did not construct a theorem which
annihilates any of them.  The green results below remain useful; the single
red arrow remains equivalent in force to row D after first-contact
attainment.

## Status table

| component | exact conclusion | status | limitation |
|---|---|---|---|
| first-contact attainment | failure after `log2` gives a nonzero parity radical at a first crossing | `PROVED` by P122.002, conditional on the surviving base certificate replay | does not constrain the oriented residue |
| fractional graph regularity | equality states lie in every `H^s`, `s<1/2`, with the stated maximal graph domain | `PROVED-IN-REPOSITORY` | endpoint `H^(1/2)` is false in general, even after two Tate moments |
| completed incoming current | the renormalized current exists uniquely and is the Tate-forced completed boundary | `PROVED-IN-REPOSITORY` | existence is not vanishing |
| local critical trace | a Cauchy residue `c` has normalized `H^(-1/2)` mass `2 pi |c|^2`; the antisymmetric pair has `8 pi |c|^2` | `PROVED` | detector only; sublogarithmic growth is equivalent to residue cancellation |
| critical-square faithfulness | zero mass at the simple critical family implies `F=0` | `PROVED`, using Conrey 1989 plus Cartwright | no 2026 preprint needed; does not show the mass is zero |
| relative local `K_2` | tame symbols split into scalar and oriented coordinates `(-K_F,+K_F)` | `PROVED-FORMAL-LOCAL` | the split exact subgroup is locally defined to have one Euler-normal ramification; it supplies no global reciprocity |
| cofinal Euler germ | first harmonics accumulating at the Tate point determine the analytic germ | `PROVED`, essentially the identity theorem | the recipient is defined as sequences already arising from a germ; this is faithfulness, not existence of a lift |
| Rees--Poisson normal | frozen-source normal equals `ZF`, and the Euler logarithmic connection reads the local `K_2` regulator | `PROVED` under Meyer's Poisson-space identities | horizontality/unramifiedness of the equality-state inclusion is open |
| active Euler-ideal overdensity | preservation for active primes with total log mass `>2T` forces `F=0` | `PROVED` | deriving preservation from the scalar null equation is the missing theorem |
| parabolic monodromy detector | critical monodromy coefficient is `2 pi i m_rho K_F(i gamma)` and opposite-metric defect detects its square | `PROVED-ALGEBRAICALLY` | ordinary Real covariance preserves only the automatic metric, not the opposite one |
| Riccati quantization | reduced pole order for `F` and `iF` forces the residue to vanish | `PROVED-CONDITIONALLY` | no source theorem gives reduced pole order; P122.006 shows a negative eigenvalue does not appear in principal parts |
| F2 / oriented equality law | scalar first contact forces sparse or zero antisymmetric residue | `OPEN` | exact remaining row-D arrow |

## Independent checks of the two analytic counts

### Critical Cauchy constant

With Fourier convention

\[
 \widehat f(\xi)=\int f(x)e^{-ix\xi}\,dx,
\]

one has

\[
 \widehat{(\sigma+ix)^{-1}}(\xi)
 =2\pi e^{\sigma\xi}\mathbf1_{\xi<0}.
\]

Therefore

\[
 \|(\sigma+i\cdot)^{-1}\|_{H^{-1/2}}^2
 =2\pi\int_0^\infty {e^{-2\sigma t}\over\sqrt{1+t^2}}dt
 =2\pi\log(1/\sigma)+O(1).
\]

A smooth local cutoff changes only lower order terms.  Distinct pole
ordinates contribute bounded oscillatory cross terms, so the finite-window
sum of squared residues is correct.

### Active-prime density

For distinct primes the nonzero lattices

\[
 {2\pi\over\log p}\mathbb Z
\]

are disjoint by unique factorization.  Their combined zero density is

\[
 {1\over\pi}\sum_{p\in S}\log p,
\]

while a transform supported in `[-T,T]` has Cartwright upper density
`2T/pi`.  Thus the strict condition `sum log p>2T` is the correct finite
overdensity threshold.

## The single unresolved diagram

All currently sound terminal routes factor through

```text
scalar first-contact equation
   -> [OPEN: pre-scalar oriented compatibility]
   -> residue/ideal/seam/Riccati detector vanishes
   -> [PROVED: faithful descent]
   -> F=0.
```

The middle detectors are equivalent coordinates after their own hypotheses;
accumulating more detectors does not weaken the open arrow.  P122.005 proves
why it cannot be reconstructed from the port-blind scalar quotient alone.

## Decision

Gate 1 is complete as an integrity classification.  Further work should
not revisit local detector construction.  It must either construct the
pre-supertrace mixed D object specified in `P122_D_SPECIFICATION.md`, or
prove a new global equality-state identity whose input is not the scalar
form alone.
