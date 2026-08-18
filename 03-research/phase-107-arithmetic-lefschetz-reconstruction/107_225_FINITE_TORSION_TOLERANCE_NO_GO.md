# 107.225 -- Finite cyclotomic torsion cannot carry the CC tolerance growth

## 1. Canonical metric tested

For a cyclotomic component \(K\), 107_221 places the finite middle group

\[
 G_I=I^{-1}\mathfrak D^{-1}/\mathfrak D^{-1}
\]

inside the Minkowski torus

\[
 T_K=K_\mathbb R/\mathfrak D^{-1}.
\]

Give \(K_\mathbb R\) the positive trace norm

\[
 \|x\|^2=\operatorname{Tr}_{K/\mathbb Q}(x\bar x)
\]

and normalize it so that the codifferent lattice has covolume one.  The
quotient metric restricts canonically to \(G_I\).  This is the direct
higher-dimensional analogue of the metric on \(\mathbb R/\mathbb Z\)
used by Connes--Consani.

## 2. Finite-tolerance obstruction

### Theorem 2.1

Let \(G\) be a finite abelian group with any translation-invariant
metric.  Then \(\dim_{\mathbb S[\pm1]}(G,d)_\lambda\) is bounded as
\(\lambda\to0\) and is constant for all sufficiently small positive
\(\lambda\).

### Proof

The finite set of nonzero distances has a positive minimum \(\delta\).
For \(0<\lambda<\delta\), the tolerance relation is equality.  Hence the
dimension is the minimum size of a signed generating set of the finite
group, independent of \(\lambda\), and is at most \(|G|-1\). \(\square\)

By contrast, the published CC formula is

\[
 \dim U(1)_\lambda
 =\left\lceil{-\log\lambda-\log2\over\log3}\right\rceil
 \longrightarrow\infty
 \qquad(\lambda\to0).
 \tag{2.1}
\]

### Corollary 2.2 (finite-torsion no-go)

No fixed finite cyclotomic middle group \(G_I\), even with its canonical
Minkowski metric, can realize the archimedean tolerant \(H^1(D)\) for
all real coefficients of \(D\).

The obstruction persists at a fixed rooted level and fixed finite
support, exactly where cohomological stabilization is required.

## 3. Real-data outcome

The exact tolerant-generator search on the fixed groups gives, at
\(\lambda=1/2,1/6,1/18\),

\[
 \begin{array}{c|c|c}
 G&|G|&\text{dimensions}\\ \hline
 C_2^2&4&(2,2,2)\\
 C_5&5&(2,2,2)\\
 C_3^3&27&(3,3,3).
 \end{array}
\]

Thus the predicted freezing is already visible throughout the CC
control radii.

## 4. Surviving construction

The metric route is not closed.  What is required is the full compact
torus \(T_K\), whose arbitrarily fine points allow tolerance dimension
to grow as \(\lambda\) shrinks.  The finite group \(G_I\) should remain
as a distinguished torsion stratum inside that torus, not replace it.

The next gate is therefore to compute the tolerant dimension of
\((T_K,d)_\lambda\), beginning with the volume lower bound and an
explicit balanced-digit covering lattice.  It must reduce to the CC
circle formula at \(K=\mathbb Q\).

## 5. Falsifier

`107_225_minkowski_tolerance_metric_probe.sage` constructs the actual
codifferent quotient lattices, solves the closest-vector problem with
two independently enlarged search radii, and exhausts all signed
generator subsets of the three finite groups.  It returns `NO` if the
CVP does not stabilize or if the dimensions vary as required by the
rejected finite-group hypothesis.

