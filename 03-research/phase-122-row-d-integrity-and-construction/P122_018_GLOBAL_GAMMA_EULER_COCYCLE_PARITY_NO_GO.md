# P122 -- the symmetric global Gamma--Euler determinant cocycle vanishes

## Status

`PROVED-IN-REPOSITORY` as a no-go theorem.  Enlarging the scalar loop
algebra so that it contains both the quarter-Gamma scattering and the
finite Euler scatterings does not, by itself, create their missing mixed
anomaly.  The normalized phases are odd, so every symmetrically regularized
bilinear determinant cocycle between them is zero.

A nonzero coupling must be causal/window-relative.  Its failure to be a
global cocycle is then the incoming boundary history already isolated in
phase 121.

## 1. Normalized scattering phases

Write

\[
 b_\infty(\tau)=\pi^{-i\tau}
 {\Gamma(1/4+i\tau/2)\over\Gamma(1/4-i\tau/2)}
 =e^{i\phi_\infty(\tau)},                          \tag{1.1}
\]

using the continuous phase normalized by `phi_infinity(0)=0`.  Since
`b_infinity(-tau)=conjugate(b_infinity(tau))`,

\[
 \phi_\infty(-\tau)=-\phi_\infty(\tau),qquad
 \phi_\infty'(-\tau)=\phi_\infty'(\tau).          \tag{1.2}
\]

For a prime, put

\[
 c_p(\tau)={1-r_pe^{-ia_p\tau}\over
                 1-r_pe^{ia_p\tau}}
 =e^{i\phi_p(\tau)},qquad
 r_p=p^{-1/2},\quad a_p=\log p,                    \tag{1.3}
\]

with `phi_p(0)=0`.  Again

\[
 \phi_p(-\tau)=-\phi_p(\tau),qquad
 \phi_p'(-\tau)=\phi_p'(\tau).                    \tag{1.4}
\]

The exact derivatives are

\[
 \phi_\infty'=g_\Gamma-m_0,qquad
 \phi_p'=a_p(P_p-1).                               \tag{1.5}
\]

## 2. Symmetric relative cocycle

Let `chi_R` be any even compactly supported cutoff, or any even Abel/heat
regularizer for which the following integrals exist.  Define the regulated
bilinear loop cocycle

\[
 \Omega_R(\phi,\psi)
 =\int_{\mathbb R}\chi_R(\tau)
        \phi(\tau)\psi'(\tau)\,d\tau.             \tag{2.1}
\]

Boundary counterterms depending only on the even asymptotic jets are also
allowed, provided the renormalization preserves the Real involution
`tau -> -tau`.

### Theorem 2.1 -- exact mixed vanishing

For every prime `p` and every `R`,

\[
 \boxed{
 \Omega_R(\phi_\infty,\phi_p)=0,qquad
 \Omega_R(\phi_p,\phi_\infty)=0.}                 \tag{2.2}
\]

The same holds for every finite Euler phase
`phi_S=sum_(p in S) epsilon_p phi_p`.

#### Proof

By (1.2)--(1.4), each integrand in (2.1) is odd: an odd phase multiplied by
an even derivative and an even cutoff.  Its integral over the real line is
zero.  Every Real-symmetric boundary subtraction has the same parity and
cannot change the mixed value.  Linearity gives the finite-product
statement.  QED.

This proof is independent of convergence at infinity: it holds at every
finite symmetric cutoff before a limit is taken.

## 3. No hidden anomaly in the completed scalar product

The finite completed scattering is

\[
 \Theta_T=b_\infty\prod_{p\in S_T}c_p^{-1},qquad
 \phi_T=\phi_\infty-\sum_{p\in S_T}\phi_p.         \tag{3.1}
\]

The bilinear central-extension calculation contains:

1. local inside/outside Euler polarization terms from P122.015;
2. no cross-prime terms, by P122.017;
3. no symmetric Gamma--Euler term, by Theorem 2.1.

Therefore a scalar global determinant central extension supplies no new
mixed conservation law beyond the already known separate factors.  Its
logarithmic derivative still gives the exact Green identity, but the
curvature/sign of its compact primitive compression remains `q_T` as in
P122.014.

## 4. Why causal regularization is different but still open

A one-sided cutoff, for example `1_(-infinity,T]`, destroys the parity
argument.  Integration by parts then produces a boundary term.  On the
physical co-Poisson carrier this is not an unspecified anomaly: v94
(451)--(453) and the phase-121 audits identify it as

\[
 \mathcal L_{T,-}(F)(t)
 =\sum_{\substack{n\ge2\\t-\log n\le-T}}
 n^{-1/2}(\mathcal A_\infty F)(t-\log n).          \tag{4.1}
\]

Thus the alternatives are exhaustive:

```text
Real-symmetric global cocycle -> mixed Gamma--Euler term is zero;
causal/window cocycle         -> mixed term is the incoming history L_(T,-).
```

Declaring the causal boundary term zero is the annular transport/F2
statement, not a consequence of determinant functoriality.

## 5. Consequence for the architecture of D

The relative correspondence requested in P122.016--P122.017 must do more
than make both multipliers members of one regularized algebra.  It must
carry two layers simultaneously:

1. a causal determinant connection, whose boundary defect is exactly
   (4.1); and
2. a Real gluing theorem proving, specifically on a primitive first-contact
   section, that this one-sided defect cancels the Tate forcing and makes
   the local annular observation vanish.

The second layer is the genuinely new theorem.  Neither the symmetric
central cocycle, the semifinite index, nor algebraic reciprocity supplies
it.  This identifies the only determinant-geometric form in which the
remaining equality law can be nonzero without being inserted by hand.
