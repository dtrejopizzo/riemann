# 106.102 — The heat-localized compensated-source gate

## 1. Purpose

The relative-heat observable of 106.100 keeps the ordinary-prime and Gamma
energies inside one positive trace-class state, while 106.66 puts the sharp
threshold into the same displacement coordinate as those two sources.  This
note combines the two identities before making any estimate.

The result is an exact signed formula.  It gives a genuinely weaker
cofinal target than rowwise positivity: it is enough to prove the signed
source estimate along one unbounded sequence of heat times.  It also shows
that neither heat smoothing nor positivity of the individual source
energies creates any hidden slack.  A hypothetical subthreshold state makes
the same signed source integral negative by a fixed normalized amount.

No zero sum and no zero-location statement is used in the derivation.

## 2. Setup

Retain the notation

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C},
 \qquad S=A+\frac12I,
\]

inside the even sector used by the full-kernel displacement identity,
and the injective positive trace-class heat-core boost \(V\) of 106.100.
For \(s\in[0,1]\) and \(t>0\), put

\[
 S_s=S+sV,
 \qquad
 \Gamma_{s,t}=e^{-tS_s/2}V e^{-tS_s/2},
 \qquad
 \overline\Gamma_t=\int_0^1\Gamma_{s,t}\,ds.
 \tag{1}
\]

Then

\[
 A_V(t)=\operatorname {Tr}\overline\Gamma_t,
 \qquad
 E_V(t)=\operatorname {Tr}(A\overline\Gamma_t).
 \tag{2}
\]

For a positive trace-class operator
\(\Gamma=\sum_j\gamma_j|r_j\rangle\langle r_j|\), with its range in the
form domain, define

\[
 \mathcal J_u[\Gamma]
 =\sum_j\gamma_j
 \int_{\mathbb R}K(x)K(x-u)
 |r_j(x)-r_j(x-u)|^2\,dx.
 \tag{3}
\]

The value is independent of the chosen positive spectral decomposition,
because it is the trace of the closed positive jump form at displacement
\(u\).

The compensated physical measure is

\[
\boxed{
 d\sigma(u)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
       \delta_{\log n}(du)
 +\left\{\frac{e^{-u/2}}{1-e^{-2u}}
          -2\cosh(u/2)\right\}du.}
 \tag{4}
\]

It retains the ordinary von Mangoldt atoms, Gamma, and the polar threshold
in one signed measure.

## 3. Exact heat-localized source identity

### Theorem 1

For every \(t>0\), define

\[
 \mathcal J_t(u)=\mathcal J_u[\overline\Gamma_t].
 \tag{5}
\]

Then

\[
\boxed{
 E_V(t)-\frac12A_V(t)
 =\int_0^\infty \mathcal J_t(u)\,d\sigma(u).}
 \tag{6}
\]

#### Proof

Every vector in \(\mathscr C\) is orthogonal to the constant function.
Consequently, for each \(r_j\in\mathscr C\),

\[
 \operatorname {Var}_{\mu_K}(r_j)=\|r_j\|_{\mu_K}^2.
 \tag{7}
\]

The full-kernel identity of 106.31 and the common-displacement formula of
106.66 therefore give

\[
 \langle r_j,(A-\tfrac12I)r_j\rangle
 =\int_0^\infty\mathcal J_u(r_j)\,d\sigma(u).
 \tag{8}
\]

First apply (8) to finite-rank positive truncations of
\(\overline\Gamma_t\), using a common Gamma and prime cutoff.  The positive
prime and Gamma pieces pass to the limit by monotone convergence, while the
polar term passes by trace-norm convergence.  This proves

\[
 \operatorname {Tr}\{(A-\tfrac12I)\overline\Gamma_t\}
 =\int_0^\infty\mathcal J_u[\overline\Gamma_t]\,d\sigma(u).
\]

Equation (2) now gives (6).  \(\square\)

The order of this proof matters.  The positive prime and Gamma traces and
the polar trace are assembled before the signed measure is formed; no
conditionally convergent pieces are separated.

### Boost-free form

The single-state flow of
106_103_CLEAN_HEAT_RAYLEIGH_FLOW_GATE.md removes the \(sV\) average.
With

\[
 \Gamma_t=e^{-tS/2}Ve^{-tS/2},
 \qquad
 Z_V(t)=\operatorname {Tr}\Gamma_t,
 \qquad
 \mathcal E_V(t)=\operatorname {Tr}(A\Gamma_t),
 \tag{8a}
\]

the same trace argument gives the cleaner identity

\[
\boxed{
 \mathcal E_V(t)-\frac12Z_V(t)
 =\int_0^\infty\mathcal J_u[\Gamma_t]\,d\sigma(u).}
 \tag{8b}
\]

Moreover,

\[
\boxed{
 \lim_{t\to\infty}
 \frac{\displaystyle\int_0^\infty
               \mathcal J_u[\Gamma_t]\,d\sigma(u)}
      {Z_V(t)}
 =\alpha-\frac12.}
 \tag{8c}
\]

Thus every statement below also holds without the perturbation average,
after replacing
\((\overline\Gamma_t,A_V,E_V)\) by
\((\Gamma_t,Z_V,\mathcal E_V)\).

## 4. Exact exponent and the weakest heat target

Let

\[
 \alpha=\inf\sigma(A).
 \tag{9}
\]

The source-rate theorem of 106.100 gives

\[
 \lim_{t\to\infty}\frac{E_V(t)}{A_V(t)}=\alpha.
 \tag{10}
\]

Combining (6) and (10) proves the normalized signed-source limit

\[
\boxed{
 \lim_{t\to\infty}
 \frac{\displaystyle\int_0^\infty
                  \mathcal J_t(u)\,d\sigma(u)}
      {A_V(t)}
 =\alpha-\frac12.}
 \tag{11}
\]

### Corollary 2 — Cofinal heat-source criterion

The following are equivalent.

1. \(A\ge\frac12I\) on \(\mathscr C\).
2. The integral in (6) is nonnegative for every \(t>0\).
3. There is an unbounded sequence \(t_k\to\infty\) and numbers
   \(\varepsilon_k\downarrow0\) such that

   \[
   \boxed{
   \int_0^\infty\mathcal J_{t_k}(u)\,d\sigma(u)
   \ge-\varepsilon_k A_V(t_k).}
   \tag{12}
   \]

#### Proof

The implication \(1\Rightarrow2\Rightarrow3\) is immediate from (6).
If 3 holds, divide by \(A_V(t_k)>0\) and use (11).  It follows that
\(\alpha-1/2\ge0\), proving 1.  \(\square\)

Thus a strict surplus on every heat row is unnecessary.  One cofinal
vanishing-tolerance estimate in the literal source coordinate suffices.

## 5. The off-line falsifier survives heat localization

Assume hypothetically that \(\alpha<1/2\).  The proved essential threshold
makes \(\alpha\) an isolated finite-multiplicity eigenvalue.  Since \(V\)
is injective, the heat state sees its eigenspace.  Equation (11) gives

\[
 \frac{\int\mathcal J_t\,d\sigma}{A_V(t)}
 \longrightarrow-\left(\frac12-\alpha\right)<0.
 \tag{13}
\]

In particular, for all sufficiently large \(t\),

\[
 \boxed{
 \int_0^\infty\mathcal J_t(u)\,d\sigma(u)
 \le-\frac12\left(\frac12-\alpha\right)A_V(t).}
 \tag{14}
\]

This is the precise hidden-circularity test for a proposed localizing
estimate.  Any argument claiming (12) from only

* positivity of \(\Gamma_{s,t}\),
* positivity of each prime or Gamma jump form,
* heat regularization,
* mean periodicity, or
* the exact threshold radical,

would also apply in the subthreshold heat/mean-periodic model of 106.99,
where (14) is false in the claimed direction.  In the actual Riemann
system, an off-line orbit supplies the analogous negative mean-periodic
state by 106.64 and 106.94.  Therefore a valid proof must use a genuinely
signed placement property of the literal measure (4).

## 6. Finite-part localizing form on translation-smooth hybrid rows

Heat smoothness in powers of the abstract generator does not, by itself,
imply two classical derivatives in the displacement variable.  Therefore
the following reformulation is asserted only on a translation-smooth
hybrid row (or after a common spatial mollification for which the limit in
(6) is retained).

If, for a fixed \(t>0\), the corresponding profile has the boundary
regularity

\[
 \mathcal J_t(0)=\mathcal J_t'(0)=0,
 \qquad
 \mathcal J_t(u),\mathcal J_t'(u)\longrightarrow0
 \quad(u\to\infty).
 \tag{15}
\]

then, with \(S_2\) the canonical second finite-part primitive of \(\sigma\)
from 106.66, finite-part integration by parts gives

\[
\boxed{
 E_V(t)-\frac12A_V(t)
 =\int_0^\infty \mathcal J_t''(u)S_2(u)\,du.}
 \tag{16}
\]

The heat mixture does not make \(u\mapsto\mathcal J_t(u)\) convex or
concave.  Each nonconstant constituent starts quadratically at zero, is
nonnegative, and returns to zero; hence its first and second derivatives
have both signs.  Formula (13) shows more: under a subthreshold mode the
full heat-localized pairing in (16) has the wrong sign by a fixed relative
amount.  Consequently a pointwise sign of a finite-part primitive, or a
separate absolute estimate of the prime and Gamma pieces, cannot prove
(12).

## 7. Minimal remaining lemma

After heat-core exhaustion, radical anti-shorting, and assembly of all
physical sources, the weakest remaining arithmetic statement is:

> **Cofinal signed heat-alignment lemma.**  For the literal compensated
> measure (4) and the heat states (1), there exist \(t_k\to\infty\) such
> that
> \[
>  \int_0^\infty\mathcal J_{t_k}(u)\,d\sigma(u)
>  \ge-o(A_V(t_k)).
> \]

By Corollary 2 this lemma proves the physical surplus.  Conversely, (11)
shows that a subthreshold state violates it by a fixed normalized margin.
The lemma must therefore be obtained from a signed, nonlocal alignment of
the actual ordinary-prime locations with Gamma and the pole; it cannot be
deduced from the positive heat calculus alone.

## 8. Status

Proved here:

* the exact heat-localized ordinary-prime--Gamma--polar identity (6);
* its boost-free version (8b)--(8c);
* the normalized source limit (11);
* the cofinal vanishing-tolerance equivalence (12);
* the fixed-margin off-line falsifier (14);
* the finite-part localizing representation (16) on
  translation-smooth hybrid rows.

Not proved here:

\[
 \int_0^\infty\mathcal J_{t_k}(u)\,d\sigma(u)
 \ge-o(A_V(t_k))
\]

for an unbounded sequence of physical heat times.  This is the remaining
literal signed source estimate.
