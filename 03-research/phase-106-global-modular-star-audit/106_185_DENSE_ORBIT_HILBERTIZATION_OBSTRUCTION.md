# 106.185 — Dense-orbit Hilbertization obstruction

## 1. Purpose

Document 106.184 isolates a possible alternative to an arithmetic Hodge
index theorem: construct a faithful Hilbert majorant on the nonreduced CCM
degree one, make normalized scaling unitary, and recover a compatible
positive complex structure by polar decomposition.  The complete jet-orbit
observation of 106.175 is the most immediate source-defined candidate for
such a majorant.

This note proves that its diagonal Hilbertization cannot work.  The
obstruction is elementary and independent of zero data: the arithmetic
translation group is dense, while invariance forces constant sampling
mass along every orbit.  A nonzero continuous function then has infinite
sampling energy.

The conclusion does not exclude the alternative-polarization branch.  It
shows that any successful majorant on that branch must contain a genuinely
nonlocal kernel (or an equivalent geometric intersection law); rapidly
weighted point and jet samples cannot provide it.

## 2. Dense arithmetic orbit

Put

\[
 G=\log \mathbb Q_+^\times
   =\operatorname {span}_{\mathbb Z}\{\log p:p\text{ prime}\}.
                                                               \tag{1}
\]

It is a countable dense subgroup of \(\mathbb R\).  For
\(f\in\mathcal S(\mathbb R)\), write

\[
 (T_af)(x)=f(x-a),\qquad a\in G.                             \tag{2}
\]

Consider first a positive diagonal sample form

\[
 \|f\|_{w,0}^2=\sum_{g\in G}w_g|f(g)|^2,
 \qquad w_g\ge0.                                             \tag{3}
\]

### Theorem 2.1 — No invariant diagonal sample majorant

If (3) is finite on \(C_c^\infty(\mathbb R)\) and every \(T_a\),
\(a\in G\), is an isometry, then all weights vanish.  In particular,
there is no faithful finite \(G\)-invariant diagonal sample norm on
\(\mathcal S(\mathbb R)\).

#### Proof

Let \(\mu=\sum_{g\in G}w_g\delta_g\).  Finiteness on every compactly
supported smooth function implies that \(\mu\) is a locally finite Radon
measure: choose a smooth function bounded below on any prescribed compact
set.  The isometry identity says

\[
 \int |f(x-a)|^2\,d\mu(x)=\int |f(x)|^2\,d\mu(x)            \tag{4}
\]

for every \(a\in G\).  Polarization and approximation of compactly
supported continuous functions show that \(\mu\) is invariant under all
translations in \(G\).  Since translations act continuously on Radon
measures in the vague topology and \(G\) is dense, \(\mu\) is invariant
under every real translation.  Uniqueness of Haar measure on
\((\mathbb R,+)\) gives \(\mu=c\,dx\).  But \(\mu\) is supported on the
countable set \(G\), whereas \(c\,dx\) has no atoms.  Thus \(c=0\) and
all \(w_g=0\). \(\square\)

## 3. Complete diagonal jet forms

Let

\[
 \|f\|_{w,J}^2
 =\sum_{n\ge0}\sum_{g\in G}w_{g,n}|f^{(n)}(g)|^2,
 \qquad w_{g,n}\ge0.                                      \tag{6}
\]

Translations do not mix derivative order:

\[
 (T_af)^{(n)}(g)=f^{(n)}(g-a).                              \tag{7}
\]

### Corollary 3.1 — Layerwise diagonal jets do not repair the obstruction

Suppose (6) is finite on \(\mathcal S(\mathbb R)\), faithful, and each
derivative-layer form

\[
 q_n(f)=\sum_{g\in G}w_{g,n}|f^{(n)}(g)|^2                 \tag{8}
\]

is translation invariant.  Then no such form exists.

#### Proof

Theorem 2.1 applied to the Radon measure
\(\mu_n=\sum_gw_{g,n}\delta_g\) gives \(\mu_n=0\) for every \(n\).
Hence (6) is the zero form and is not faithful. \(\square\)

Rapid decay in \(g\) makes (6) finite, but then (8) fails and normalized
scaling is not unitary.  This is the exact incompatibility anticipated in
Section 6 of 106.184.

## 4. The required nonlocal replacement

A coordinate-kernel quadratic form on the orbit array which is invariant
under common translation has the form

\[
 q(a)=
 \sum_{g,h\in G}\sum_{m,n\ge0}
 K_{m,n}(g-h)a_{g,m}\overline{a_{h,n}},                    \tag{9}
\]

whenever the displayed sums and kernels are meaningful.  Positivity asks
that the matrix-valued difference kernel \(K\) be positive definite.
Unlike (6), (9) retains correlations between distinct prime-generated
times.  Within the coordinate-kernel class, these off-diagonal
correlations are therefore forced by the conjunction of density,
finiteness, faithfulness, and scale covariance.

There are two possible sources for such a kernel:

1. a source-side arithmetic intersection pairing, whose local and
   archimedean terms produce (9);
2. a direct analytic construction of a positive-definite nonlocal kernel
   from the prime/root/Gamma complex, followed by proof that its null
   space is exactly the CCM restriction range.

The second description is strictly weaker than constructing a full
arithmetic surface.  It is the analytic shadow sufficient for Theorem 3.1
of 106.184.  But defining \(K\) from the Rosati/Weil form or from the zero
divisor would reverse the logical direction; the kernel must be present
before the spectral conclusion.

## 5. Consequence for the two polarization branches

### Fixed Rosati branch

One must prove positivity of the already identified form
\(\operatorname {Re}\mathfrak h_{\rm Ros}\).  A Hodge-index theorem on
an arithmetic square is the natural sufficient mechanism.  The
factorization map \(D\) is equivalent to this positivity and creates no
intermediate step.

### Alternative polarization branch

One need not identify the positive metric with Rosati.  It is enough to
construct a nonlocal kernel (9) which:

* descends faithfully to nonreduced CCM degree one;
* makes normalized scaling unitary;
* represents the descended \(\Omega\) by a boundedly invertible
  skew-adjoint operator.

Then 106.184 constructs \(J'\) and the positive metric.  Theorem 2.1 and
Corollary 3.1 show that the kernel cannot be a layerwise invariant
diagonal form in the faithful dense jet coordinates.

## 6. Status

Proved without RH or zero input:

* impossibility of a finite faithful scale-invariant diagonal sample norm
  on the dense prime-generated orbit;
* the same impossibility for layerwise invariant diagonal complete-jet
  norms;
* necessity of off-diagonal, nonlocal correlations for an analytic
  alternative to the arithmetic-square construction.

Still required:

* construction from prime/root/Gamma data of a positive-definite nonlocal
  kernel of the form (9);
* faithful torsion-sensitive descent and strong nondegeneracy of
  \(\Omega\) for the resulting majorant.
