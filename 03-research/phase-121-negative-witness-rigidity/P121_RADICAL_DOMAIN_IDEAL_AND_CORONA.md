# P121 -- the radical domain ideal and the Euler--Bohr corona

## 1. The nonlinear object

Let `F in L2(-T,T)` be extended by zero and write `Fhat` for its Fourier
transform.  The maximal physical co-Poisson observation has graph domain

\[
 \operatorname{Dom}S_T^{\max}
 =\{F:\zeta(1/2+i\tau)\widehat F(\tau)\in L^2(\mathbb R)\}. \tag{1.1}
\]

Put

\[
 \mathcal A_0=\mathbb C\,1+\mathcal S(\mathbb R)                 \tag{1.2}
\]

with pointwise multiplication in the Fourier variable, and associate to
`F` its **radical domain ideal**

\[
 \mathfrak I(F)=\{a\in\mathcal A_0:
   a(\tau)\zeta(1/2+i\tau)\widehat F(\tau)\in L^2\}.             \tag{1.3}
\]

The assignment is nonlinear in `F`; it records which source-defined
smoothing multipliers repair the nuclear-domain failure of that particular
physical state.  It introduces no quadratic positivity certificate.

## 2. Exact ideal theorem

### Theorem 2.1

For every compact-window `F in L2`:

1. `I(F)` is an algebraic ideal of `A_0`;
2. `S(R) subset I(F)`;
3. `1 in I(F)` if and only if `F in Dom S_T^max`;
4. if `F` is not in that domain, then

   \[
    \boxed{\mathfrak I(F)=\mathcal S(\mathbb R).}                \tag{2.1}
   \]

Consequently every escaping physical state defines the same quotient

\[
 \mathcal A_0/\mathfrak I(F)\simeq\mathbb C,                    \tag{2.2}
\]

the character at frequency infinity.

### Proof

Compact support and Cauchy--Schwarz give `F in L1`, hence `Fhat` is bounded.
An unconditional polynomial vertical-strip bound for `zeta` is enough to
show that

\[
 s(\tau)\zeta(1/2+i\tau)\widehat F(\tau)\in L^2
 \quad(s\in\mathcal S),                              \tag{2.3}
\]

so `S subset I(F)`.  Linearity is immediate.  If `a in I(F)` and
`b=c+s in A_0`, then `b` is bounded, hence `ba in I(F)`; this proves the
ideal property.  Statement 3 is the definition (1.1).

It remains to prove 4.  Write `a=c+s`.  If `c != 0`, then for sufficiently
large `|tau|`,

\[
 |a(\tau)|\ge |c|/2.                               \tag{2.4}
\]

Thus membership of `a` in `I(F)` implies square integrability of
`zeta Fhat` outside a compact interval.  On the remaining compact interval,
`zeta(1/2+i tau)` is bounded and `Fhat` is bounded, so the product is also
square integrable.  Hence `F` would belong to (1.1).  For an escaping `F`
one must therefore have `c=0`, proving `I(F) subset S`.  Together with
(2.3) this proves (2.1).  The quotient assertion follows.  QED.

## 3. What this proves about failure of row (d)

Combine Theorem 2.1 with the first-loss branch of
`P121_REVERSE_ENGINEERING_AND_ASC_NO_GO.md`.  If row (d) fails, its first
radical vector `F_*` is invisible to every finite-frequency hull test:

\[
 \mathfrak I(F_*)=\mathcal S(\mathbb R),\qquad
 1\notin\mathfrak I(F_*).                            \tag{3.1}
\]

The missing graph seminorm is therefore a corona defect.  The two Tate
zeros are finite spectral data and cannot remove it by an ordinary
hull--kernel or Bezout argument.

This also kills a naive spectral-synthesis proof.  The ideal
`S(R)` has empty hull at finite frequencies but does not contain the unit.
Approximate identities converge on compact frequency sets while their
co-Poisson graph norms can diverge.  This is the exact mean-to-uniform
failure, now expressed as an algebraic quotient rather than an unnamed
topological gap.

## 4. Retaining the Euler phases

The algebra `A_0` deliberately forgets the bounded oscillatory multipliers

\[
 e^{-i\tau\log n}.                                  \tag{4.1}
\]

To retain the exact cross-place phase, enlarge it to

\[
 \mathcal A_E
 =\operatorname{alg}\bigl(\mathcal S(\mathbb R),1,
        e^{-i\tau\log p}:p\text{ prime}\bigr)       \tag{4.2}
\]

in its natural bounded-multiplier completion.  Modulo the vanishing ideal,
the exponentials in (4.1) generate the Bohr compactification of the free
abelian prime group.  Thus the single infinity character of (2.2) resolves,
when the arithmetic phase is retained, into an Euler--Bohr corona.

A first-loss vector can consequently carry a nonzero boundary defect
measure on that corona.  Unique factorization makes its prime coordinates
independent, but does not force the measure to vanish; phase 106 already
shows that the diagonal real-frequency curve and the independent Euler
Bohr measure can even be mutually singular while sharing all one-prime
marginals.

## 5. The corona measure exists for every escaping core limit

### Theorem 5.1

Let `F_j` belong to the smooth primitive core and converge in `L2` to an
escaping vector `F notin Dom S_T^max`.  Put

\[
 M_j=\|\zeta(1/2+i\,\cdot)\widehat F_j\|_2^2.       \tag{5.1}
\]

After passing to a subsequence, `M_j -> infinity`, and the probability
measures

\[
 d\mu_j(\tau)=M_j^{-1}|\zeta(1/2+i\tau)|^2
                   |\widehat F_j(\tau)|^2d\tau      \tag{5.2}
\]

escape every compact subset of the real frequency axis.  Their pushforwards
under

\[
 \tau\longmapsto (e^{-i\tau\log p})_p              \tag{5.3}
\]

have a weak-star convergent subsequence on the compact Euler--Bohr torus.
If the approximants have fixed parity, the limiting probability measure is
invariant under coordinatewise complex conjugation.

### Proof

If `(M_j)` had a bounded subsequence, the closed graph of the maximal
co-Poisson operator, together with weak compactness of bounded sets in its
Hilbert target, would put `F` in its domain.  Hence a subsequence tends to
infinity.  On every fixed compact frequency interval, `zeta` is bounded and
Fourier restriction is bounded from the compact-window `L2` space to
`L2` of that interval.  The numerators of (5.2) therefore remain bounded
there, while `M_j -> infinity`; the normalized mass tends to zero.
Compactness of the Bohr torus gives a weak-star convergent pushforward
subsequence.  Parity sends `tau` to `-tau`, which is coordinatewise complex
conjugation in (5.3), and proves the last assertion.  QED.

### What Theorem 5.1 does not give

The physical first-loss equation converges in the Gamma form topology,
whose high-frequency weight is comparable to `log(2+|tau|)`.  The measures
(5.2), however, are normalized with the much stronger and highly
nonuniform weight `|zeta(1/2+i tau)|^2`.  Therefore

\[
 H_TF_j\longrightarrow0\quad\hbox{in the form dual}               \tag{5.4}
\]

does **not** presently imply any equation for the weak-star limit of
`mu_j`.  Claiming that it does would be the old graph-domain gate in corona
language.  The two Tate moments constrain `Fhat` at the finite points
`tau=+-i/2`; by themselves they impose no condition on a measure which has
escaped to real-frequency infinity.

Thus the corona measure is constructed, but a Gamma--Euler boundary law for
it still has to come from a new source identity with the correct graph
continuity.

## 6. Paper-36 correction: the measure alone is not the state

The transfer audit in `P121_PAPER36_TRANSFER_AUDIT.md` shows that a positive
boundary measure with Real symmetry is too coarse.  A reciprocal off-line
quartet can change the interior divisor while leaving the corresponding
real boundary symbol unchanged.  Therefore the phrase "prove that the
corona measure vanishes" is not, by itself, a valid terminal theorem.

The measure has to be augmented by radial information.  The source-defined
quantity constructed in `P121_WHITE_LIGHT_NORMAL_SLOPE.md` does this: its
first normal derivative is exactly the missing `|zeta|^2` graph seminorm.
Comparison with the full phase-116 v94 audit shows that this is a radial
coordinate on an already known graph-domain gap, not a stronger theorem.
The fractional boundary-transmission statement (3.2) of
`P121_FRACTIONAL_REGULARITY_GATE.md` is now proved by the dyadic bootstrap.
The sharper current target is annular gap transport (358)/(441) of v94.

## 7. A valid but non-preferred terminal theorem

The global square would follow from the following source-side statement,
but the fractional regularity gate is now the more concrete formulation.

### Radical Abel-slope exclusion (proved later in phase 121)

> The exact Gamma--Euler first-loss equation (445), the Real involution and
> the two Tate moments force the normalized white-light radial energy of the
> specific radical to be `O(epsilon)` at the critical wall.

This is not a request for a norm `D*D`, a contraction, a positive state or a
global co-Poisson estimate.  By the finite-slope theorem it puts the radical
in the maximal nuclear domain.  The former statement that this alone
contradicted the first-loss branch was too strong: equality-state annular
gap transport is still required.

The theorem is proved in `P121_WHITE_LIGHT_NORMAL_SLOPE.md`, using
`P121_DYADIC_RADICAL_BOOTSTRAP.md`.  The corona measure remains a useful
record of possible concentration, but it is not sufficient boundary data.

## 8. Comparison objects

* Davenport--Heilbronn has no independent-prime Euler--Bohr algebra, so the
  proposed boundary relation is unavailable before any sign comparison.
* A shifted rank-two pair has a rank-two local corona fibre rather than the
  rank-one prime character; it is a direct falsifier for a boundary relation
  which ignores local rank.
* Dedekind zeta functions have the same place-labelled rank-one corona.
  Therefore a successful exclusion theorem should extend to them and would
  imply GRH for number fields.  This strength is explicit, not hidden.

## 9. Status

The radical-domain ideal theorem and the localization of every possible
escape at the Euler--Bohr corona are proved.  The normal-slope theorem gives
an exact radial refinement, and the radical Abel-slope bound is proved.
Equality-state annular gap transport, and hence the global square, remain
open.
