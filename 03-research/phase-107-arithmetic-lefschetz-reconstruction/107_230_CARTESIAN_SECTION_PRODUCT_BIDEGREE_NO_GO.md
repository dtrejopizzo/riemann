# 107.230 -- Cartesian products of periodic sections have zero bidegree density

## 1. Fixed published controls

Let \(p,q\) be primes and let

\[
 X_{p,n}(\alpha)=H^0(\alpha\{1\})^{p^n},
 \qquad
 X_{q,m}(\beta)=H^0(\beta\{1\})^{q^m},
\]

where \(\alpha\in\mathbb Z[1/p]_{>0}\) and
\(\beta\in\mathbb Z[1/q]_{>0}\). For all sufficiently large depths,
the exact calculation in Connes--Consani, *Geometry of the Scaling
Site*, Lemma 6.19, gives

\[
 d_{p,n}:=\mathrm{tdim}\,X_{p,n}(\alpha)
 =\alpha p^n-p+1,
 \tag{1.1}
\]

\[
 d_{q,m}:=\mathrm{tdim}\,X_{q,m}(\beta)
 =\beta q^m-q+1.
 \tag{1.2}
\]

The topology is uniform convergence on the compact fundamental
interval, so these are separable metric spaces.

## 2. Exact Cartesian-product dimension

### Proposition 2.1

For sufficiently large \(n,m\),

\[
 \mathrm{tdim}
 \bigl(X_{p,n}(\alpha)\times X_{q,m}(\beta)\bigr)
 =d_{p,n}+d_{q,m}.
 \tag{2.1}
\]

### Proof

The product theorem for Lebesgue covering dimension on separable metric
spaces gives the upper bound

\[
 \mathrm{tdim}(X\times Y)
 \leq\mathrm{tdim}\,X+\mathrm{tdim}\,Y.
\]

For the reverse inequality, the proof of Connes--Consani Lemma 6.19
constructs inside \(X_{p,n}(\alpha)\) a parameter cell of dimension
\(d_{p,n}\): after restricting the free additive parameter and the
open simplex parameters to compact subboxes, its continuous injection
is a topological embedding because the source is compact and the
uniform-function target is Hausdorff. The same holds in the \(q\)
factor. Their product is a compact cell of dimension
\(d_{p,n}+d_{q,m}\) embedded in \(X\times Y\). Monotonicity of covering
dimension gives the lower bound. \(\square\)

## 3. Bidegree no-go

### Theorem 3.1

The Cartesian product has zero normalized two-ruling dimension:

\[
 \lim_{n,m\to\infty}
 p^{-n}q^{-m}
 \mathrm{tdim}
 \bigl(X_{p,n}(\alpha)\times X_{q,m}(\beta)\bigr)=0
 \tag{3.1}
\]

along every cofinal path.

### Proof

By (1.1), (1.2), and (2.1), the normalized dimension is

\[
 \frac{\alpha p^n-p+1}{p^nq^m}
 +\frac{\beta q^m-q+1}{p^nq^m}.
\]

Its absolute value is bounded by

\[
 \alpha q^{-m}+\beta p^{-n}
 +(p-1)p^{-n}q^{-m}+(q-1)p^{-n}q^{-m},
\]

which tends to zero independently of the relative rates of \(n,m\).
\(\square\)

### Corollary 3.2 (forced mixed channel)

A two-ruling \(H^0\) construction whose local section space is merely
the Cartesian product of the published one-ruling section spaces cannot
carry a nonzero bidegree-two RR coefficient. The same is true for a
finite disjoint union of such products with the number of components
bounded independently of depth.

To retain the nonzero product density \(\alpha\beta\) constructed at
the support level in 107_229, the square must contain
\(\Theta(p^nq^m)\) independent **mixed** parameters. In categorical
terms, it needs a tensor/convolution section object, not a Cartesian
pair of one-variable sections.

## 4. Relation to the desired intersection term

The conclusion is the dimension-theoretic analogue of the classical
distinction

\[
 H^0(L)\times H^0(M)
 \quad\text{versus}\quad
 H^0(L\boxtimes M).
\]

The first has additive parameter dimension; the second can have
multiplicative dimension. A surface RR term such as
\(\tfrac12 c_1(L)^2\), or the desired two-ruling intersection, requires
the latter behavior.

This selects the next construction sharply: define a tropical or
tolerant external tensor product whose finite-level mixed cells have
dimension asymptotic to
\(\alpha\beta p^nq^m\), and prove descent and cofinal independence.

## 5. Scope

This theorem closes only the Cartesian-product realization. It does
not prove that a suitable tropical tensor product exists, that its
dimension is multiplicative, or that it is the divisor sheaf on the
Scaling-Site square. It also does not construct \(H^1\), RR, or an
intersection pairing.

The statement is nevertheless universal for every candidate which
uses the published one-ruling topologies and combines them only by
Cartesian product: no change of cofinal path or finite boundary
correction can repair its zero bidegree density.

## 6. Exact verifier

107_230_cartesian_section_product_bidegree_no_go.py evaluates the
published exact dimensions on the fixed prime pairs
\((2,2),(2,3),(3,5),(5,7),(7,11)\), checks the additive product
dimension and its explicit cofinal bound along balanced and unbalanced
paths, and retains a mixed-product dimension as a negative control. It
returns NO if the Cartesian model acquires a nonzero bidegree limit or
if the mixed control is also erased.

