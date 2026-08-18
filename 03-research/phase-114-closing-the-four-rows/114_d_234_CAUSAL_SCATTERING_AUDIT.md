# D.234 — Causal scattering audit of the D.190 gate

## Verdict

The source-defined transport requested by D.190 can be expressed as a
causality problem for the completed prime--Gamma scattering operator.  This
is a useful reformulation, but causality (or half-plane innerness) may not be
used as an input: in the zeta setting it contains the same zero-free
information as row D.

Thus a candidate proof must construct causality from an arithmetic dilation,
martingale, or positive realization which exists before the sign theorem.  A
formal Hardy factorization of the completed zeta quotient is circular.

## Operator dictionary

Let (U) be the Mellin/Fourier realization in which translations by
(k\log p) become multiplication by the local phases and the Gamma kernel
becomes the archimedean scattering factor.  The completed scattering
multiplier (S) is unitary on the symmetry line by the functional equation.
For a support half-space projection (P_+), its failure of causality is the
Hankel block

\[
 H_S=(I-P_+)M_SP_+=[P_+,M_S]P_+ .                  \tag{0.1}
\]

After localization to an old cell and a born shell, (0.1) is the same type
of support commutator as

\[
 P_OQ_TP_E=[P_O,Q_T]P_E                             \tag{0.2}
\]

in D.190.  The two Tate equations change this by finite rank only and cannot
remove the full Gamma Hankel block.

If (S) extends as an inner multiplier to the relevant Hardy half-plane,
then (M_S) preserves the incoming Hardy space and the forbidden Hankel
block vanishes (or, after the finite localization, is transported by the
canonical defect operator).  Conversely, a causal Lax--Phillips realization
for an exhaustive support filtration supplies precisely the supported
Douglas contractions of D.190.  Hence this route is admissible only if the
causal realization is constructed independently of the desired zero-free
region.

## Circularity test

The boundary modulus (|S|=1) is unconditional; it follows from the
functional equation and conjugation symmetry.  Boundary unitarity does not
imply half-plane innerness.  Poles or zeros in the wrong half-plane obstruct
the analytic Hardy realization.  Therefore the implication

\[
 |S|=1\text{ on the boundary}
 \Longrightarrow S\text{ inner/causal}              \tag{0.3}
\]

is not available.  Assuming (0.3) would insert the missing RH information
under operator-theoretic terminology.

This agrees with Burnol's Lax--Phillips analysis for function fields, where
the Riemann hypothesis is equivalent to causality of the associated
scattering system; causality is not obtained merely from unitarity
(`arXiv:math/9911175`).  The semilocal prolate/Sonin programme of
Connes--Consani--Moscovici supplies a canonical operator framework but states
the remaining Weil-positivity problem rather than proving the required
global sign (`arXiv:2310.18423`).  Their later finite Euler-product spectral
triples produce self-adjoint approximants; convergence to the completed zeta
object remains the theorem whose proof would establish RH
(`arXiv:2511.22755`).

## Admissible next theorem

A noncircular causal closure must provide all of the following:

1. a Hilbert space (mathcal K) and a source-defined unitary or isometric
   colligation built from the Gamma place and every (p^k);
2. incoming/outgoing support subspaces defined without zeros;
3. a compression whose off-diagonal block is exactly (0.2), including the
   two Tate corrections;
4. a conservation identity whose defect operator gives the D.190 Douglas
   contraction with constant one;
5. compatibility under every prime-power birth and exhaustion of support.

Boundary unitarity alone proves item 1 only in the unlocalized ambient
space.  Items 2--4 are the missing support theorem.

## Classification

* support-commutator identity: **ALGEBRAIC/OPERATORIAL** (D.190);
* boundary unitarity of completed scattering: **PROVED** from the functional
  equation;
* equivalence between exhaustive sharp Douglas factorization and row D:
  **PROVED** (D.190);
* causality/innerness for the completed zeta scattering: **OPEN / NOT AN
  INPUT**;
* row D and RH consequence: **OPEN**.
