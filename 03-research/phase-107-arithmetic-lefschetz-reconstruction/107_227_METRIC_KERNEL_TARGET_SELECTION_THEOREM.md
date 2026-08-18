# 107.227 -- The metric-kernel target-selection theorem

## 1. Exact scope

Let the archimedean divisor direction be

\[
 A_\infty=\mathbb R\{\infty\}.
\]

Suppose a tensor-compatible realization assigns to \(a\in\mathbb R\)
a metrized object \(\overline L_a\), with

\[
 \overline L_{a+b}\simeq \overline L_a\otimes\overline L_b.
 \tag{1.1}
\]

This result concerns realizations whose **algebraic shadow** factors
through a finitely generated abelian group \(N\), such as a finite-rank
Neron--Severi group, an integral topological Chern-class group, or the
ordinary rank/length Euler data of a fixed finite family of perfect
complexes. It does not assert that an arithmetic Picard group of
metrized line bundles is finitely generated.

## 2. Algebraic-shadow no-go

### Theorem 2.1

Every additive algebraic shadow

\[
 c_{\rm alg}:A_\infty\longrightarrow N
 \tag{2.1}
\]

is zero. Consequently, no invariant which factors only through
\(c_{\rm alg}\) can recover the Connes--Consani Riemann--Roch variation
along \(A_\infty\).

### Proof

The additive group \(\mathbb R\) is divisible, so its image under
\(c_{\rm alg}\) is a divisible subgroup of \(N\). A finitely generated
abelian group has no nonzero divisible subgroup. Hence
\(c_{\rm alg}=0\).

For \(a\geq0\), put \(n=\lfloor e^a\rfloor\). The published
Connes--Consani dimension is

\[
 \kappa(a)=\left\lceil\log_3(2n+1)\right\rceil.
 \tag{2.2}
\]

It takes the values \(1,2,3,4\) at \(n=1,4,13,40\), while every
invariant factoring through (2.1) is constant. Such a factorization is
therefore impossible. \(\square\)

This combines the mechanism of 107_223 and 107_224 without enlarging
their scope: ordinary flat Euler data and finite-rank Chern data are
excluded as the complete target, not as valid algebraic shadows.

## 3. The surviving tensor-compatible channel

The no-go does not kill tensor-compatible metrized objects. If a fixed
algebraic line bundle is equipped with a metric weight \(a g\), then

\[
 (L,a g)\otimes(L',b g)=(L\otimes L',(a+b)g).
 \tag{3.1}
\]

Thus the metric kernel contains a nonzero additive copy of
\(\mathbb R\), represented by Green functions, logarithmic metric
weights, mass bounds, or tolerance radii. It is not a finitely
generated algebraic target.

The integer dimension is then a nonlinear invariant of that real
channel. This nonlinearity is forced, not optional. Even after
normalization at \(a=0\), (2.2) is not additive: for \(a=\log4\),

\[
 [\kappa(2a)-\kappa(0)]=3
 \ne2=2[\kappa(a)-\kappa(0)].
 \tag{3.2}
\]

### Corollary 3.1 (target selection)

A Phase 107 square compatible with the published integer-dimensional
Riemann--Roch theorem must retain a real metric/tolerance kernel before
taking integer dimension. A construction may carry finite-rank
algebraic Chern data as a quotient, but it cannot factor the
archimedean divisor direction through that quotient.

Equivalently, the admissible shape is

\[
 0\longrightarrow \mathcal M_{\mathbb R}
 \longrightarrow \widehat{\operatorname{Pic}}
 \longrightarrow \operatorname{Pic}_{\rm alg}
 \longrightarrow 0,
 \tag{3.3}
\]

with the \(A_\infty\)-variation nontrivial in
\(\mathcal M_{\mathbb R}\), followed by a nonlinear bounded/tolerant
dimension. Searching for another integral \(c_1\), finite-rank
Neron--Severi target, or ordinary \(K_0\)-Euler characteristic cannot
close row (a).

## 4. Consequence for the open construction

The next unresolved gate is not the choice of another cohomological
target. It is the geometric support theorem isolated in 107_155:
for every finite-support divisor, the metric/tolerant square must admit
only finitely many monomial rays. The rooted cyclotomic sector of
107_158 proves this only on one finite subsystem.

No further candidate for \(c_1\), ordinary Euler characteristic, or
finite metric torsion is admissible before that support theorem is
settled. This is a restriction of the search space, not a construction
of the arithmetic surface.

## 5. Exact falsifier

107_227_metric_kernel_target_selection_theorem.py checks the fixed CC
controls, the nonadditivity witness (3.2), a nonzero additive metric
channel, and finite-rank divisibility windows. It includes mutated
algebraic and metric channels, so it returns VERDICT: NO if either the
no-go or the surviving-channel assertion is weakened.

