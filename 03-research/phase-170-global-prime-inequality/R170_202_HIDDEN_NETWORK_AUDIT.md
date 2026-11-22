# R170_202 — Can a network with hidden vertices recover the budget?

**Class obstruction proved; explicit precedent
in phase 106.13. Not a no-go for general Hilbert spaces.**

## 1. Second candidate construction

After R170_201, a natural repair is to replace independent channels
by a network with internal variables z and define the effective energy as

$$E_{\rm eff}(x)=\inf_z E(x,z),\qquad
E(y)=\sum_{i<j}c_{ij}|y_i-y_j|^2+\sum_i\kappa_i|y_i|^2,
\quad c_{ij},\kappa_i\ge0.$$

Minimization reduces energy and preserves positivity. It might seem to
cheapen the constant compensation without losing the square. However,
this class imposes an additional property that the target form violates.

## 2. A property that survives removing vertices

For real data, ||a|−|b||≤|a−b| implies E(|y|)≤E(y). Taking infima over
the internal variables gives

$$E_{\rm eff}(|x|)\le E_{\rm eff}(x).\tag{1}$$

The minimum need not be attained: the argument applies to a minimizing
sequence. If x=f−g with f,g≥0 of disjoint support, |x|=f+g; for a
quadratic energy (1) is equivalent to

$$E_{\rm eff}(f,g)\le0.\tag{2}$$

This also holds for infinite networks when the same variational
definition and the modulus stability are justified. We do not claim
those requirements for an arbitrary formal limit of networks.

## 3. Explicit counterexample for W inside the certified range

Take the real polarization W_T(f,g). For f,g smooth with disjoint
supports, separated by distances less than log 2, there are no prime or
diagonal terms. The remaining kernel is

$$h(u)=2\cosh(u/2)-\frac{e^{-u/2}}{1-e^{-2u}},\qquad u>0.\tag{3}$$

This formula is derived in `106_13_BRANCH_SELECTION_NO_GO`, §1, directly
from the polar term and the digamma function. We use this computation
from the record, importing no claim about the zeros.

At the multiplicative-rational distance u₀=log(3/2), one gets exactly

$$h(u_0)=\sqrt{3/2}-\frac45\sqrt{2/3}
=\frac7{10}\sqrt{2/3}>0.\tag{4}$$

Choose two nonnegative, nonzero bumps centered at −u₀/2 and u₀/2.
By continuity of h they can be made narrow enough that all distances
between their supports lie in (0,log 2) and h is positive there.
Both fit, for instance, in (−1/2,1/2). Then

$$W_{1/2}(f,g)=\iint f(t)g(s)h(|t-s|)\,dt\,ds>0,$$
$$W_{1/2}(|f-g|)-W_{1/2}(f-g)=4W_{1/2}(f,g)>0.\tag{5}$$

This contradicts (1), not the positivity of W. In fact T=1/2 lies within
the certified range of Paper 46. A positive form need not be a network
energy with positive conductances.

**Conclusion.** No scalar network of this class, even with hidden
vertices eliminated variationally, represents W in the physical
coordinates while preserving the pointwise modulus. Allowing prior
transformations that do not preserve that modulus, matrix channels with
phases, or signed couplings, lies outside the scope of the argument; its
positivity would need a separate proof.

## 4. Relation to prior work

Phase 106.13 already proves the obstruction of positivity preserved by
the full semigroup. This note does not sell it as a new discovery:
it applies it to the concrete repair by hidden networks and gives the
exact value (4), located inside an already certified window.

Together with R170_201, the exercise produces two different diagnoses:

1. Orthogonal prime channels: preserve the current but require a
   divergent constant compensation.
2. Scalar networks with variable elimination: allow reducing energy, but
   impose a modulus inequality that the polar term violates.

The global problem remains open. Neither of these results licenses the
claim that every analytic, matrix, or geometric strategy is impossible.
</content>
