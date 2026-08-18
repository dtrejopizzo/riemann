# 107.226 -- Dimension-sensitive tolerance growth on the full Minkowski torus

## 1. Setup

Let

\[
 T=V/\Lambda
\]

be a real Euclidean torus of dimension \(d\), with the metric normalized
so that \(\operatorname{vol}(T)=1\).  Give \(T\) the Connes--Consani
tolerance relation at radius \(\lambda>0\).

For a cyclotomic component the canonical instance is

\[
 V=K_\mathbb R,
 \qquad \Lambda=\mathfrak D_K^{-1},
 \qquad \|x\|^2=\operatorname{Tr}_{K/\mathbb Q}(x\bar x),
\]

followed by covolume-one normalization.

## 2. Volume theorem

Let \(v_d=\pi^{d/2}/\Gamma(d/2+1)\) be the volume of the Euclidean unit
ball.

### Theorem 2.1

The tolerant integer dimension satisfies

\[
 \boxed{
 \dim_{\mathbb S[\pm1]}(T,d)_\lambda
 \ge
 \max\left(0,
 \left\lceil\log_3{1\over v_d\lambda^d}\right\rceil
 \right).}
 \tag{2.1}
\]

### Proof

If a generating set has \(k\) elements, it has at most \(3^k\) signed
subset sums.  Condition 2 in the CC definition says that the radius
\(\lambda\) balls around those sums cover \(T\).  The image in \(T\) of
one Euclidean radius-\(\lambda\) ball has volume at most
\(v_d\lambda^d\), even beyond the injectivity radius.  Therefore

\[
 1=\operatorname{vol}(T)
 \le3^k v_d\lambda^d,
\]

which gives (2.1). \(\square\)

In particular,

\[
 \liminf_{\lambda\to0}
 {\dim(T,d)_\lambda\over-\log\lambda}
 \ge {d\over\log3}.
 \tag{2.2}
\]

## 3. Recovery of the CC slope

For \(K=\mathbb Q\), one has \(d=1\), \(T=\mathbb R/\mathbb Z\), and
\(v_1=2\).  Formula (2.1) becomes

\[
 \dim U(1)_\lambda
 \ge
 \left\lceil{-\log\lambda-\log2\over\log3}\right\rceil,
\]

which is exactly the lower bound saturated by the balanced-ternary
generators in the published CC theorem.

For cyclotomic degree \(d\), (2.2) multiplies the leading slope by
\(d\), as expected under a degree-\(d\) finite cover.  Thus the full
Minkowski torus repairs the bounded-capacity failure of 107_225 and
retains the correct one-dimensional normalization.

## 4. Exact scope

This is a necessary lower bound, not a Riemann--Roch formula.  To close
the metric construction one still needs a basis-independent family of
balanced generators proving a matching upper bound

\[
 \dim(T,d)_\lambda
 \le {d\over\log3}(-\log\lambda)+O_K(1),
\]

with the CC exact formula when \(K=\mathbb Q\).  It must then be placed
on the divisor-dependent three-term complex and shown compatible with
the codifferent duality.

## 5. Falsifier

`107_226_minkowski_torus_tolerance_lower_bound.sage` loads the actual
cyclotomic fields of conductors 8, 10, and 9, computes their degrees and
codifferent covolumes, normalizes them to volume one, and evaluates the
fixed lower bounds at \(1/2,1/6,1/18\).  A dimension-blind mutation that
uses \(d=1\) on every component must disagree with the real bounds.

