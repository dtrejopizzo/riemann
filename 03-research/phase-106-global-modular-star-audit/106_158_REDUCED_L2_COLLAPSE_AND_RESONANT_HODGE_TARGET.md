# 106.158 — Reduced \(L^2\) collapse and the resonant Hodge target

## 1. Purpose

The CCM degree-one object is a cokernel in a nuclear cyclic category.  A
natural first attempt at the missing polarization is to complete the source
and target of the adelic summation map in their Haar \(L^2\) norms and to use
the quotient norm.  That construction is positive and the half-density
scaling action is unitary.  This note proves that it cannot be the desired
polarization: its reduced degree one is zero.

The calculation fixes the category in which a genuine arithmetic Hodge star
must live.  It must act on the unreduced resonant cohomology retained by the
CCM Schwartz/Meyer topology.  It cannot be a bounded Hodge star obtained from
the ordinary Plancherel completion.

No zero location is assumed below.  Only discreteness of the zero divisor of
a nonzero holomorphic \(L\)-function is used.

## 2. A dense-range lemma

Let \((X,\mu)\) be a sigma-finite measure space and let \(m:X\to\mathbb C\)
be measurable and nonzero almost everywhere.  Denote by \(M_m\) the maximal
multiplication operator

\[
 M_m f=mf,
 \qquad
 \mathcal D(M_m)=\{f\in L^2(X):mf\in L^2(X)\}.
 \tag{1}
\]

### Lemma 2.1 — Multiplication by an a.e. nonzero function has dense range

\[
 \boxed{\overline{\operatorname {Ran}M_m}=L^2(X).}
 \tag{2}
\]

#### Proof

For \(h\in L^2(X)\), put

\[
 E_N=\{x:N^{-1}\le |m(x)|\le N\},
 \qquad h_N=h\mathbf1_{E_N}.
 \tag{3}
\]

Since \(m\ne0\) a.e., \(E_N\uparrow X\) modulo null sets and
\(h_N\to h\) in \(L^2\).  Moreover

\[
 g_N=m^{-1}h_N\in L^2(X),
 \qquad M_mg_N=h_N.
 \tag{4}
\]

Thus every \(h\) is an \(L^2\)-limit of range vectors. \(\square\)

The same proof works on every character component of a direct integral.

## 3. Mellin form of the adelic reduction

Fix a character \(\chi\) of the compact norm-one idele class group.  After
the half-density normalization, Mellin--Plancherel identifies the unitary
scaling line with

\[
 \mathcal H_\chi=L^2(\mathbb R,d\gamma).
 \tag{5}
\]

On a common Schwartz core, adelic summation followed by restriction has the
standard Tate multiplier

\[
 m_\chi(\gamma)
 =G_\chi\!\left(\frac12+i\gamma\right)
  L\!\left(\frac12+i\gamma,\chi\right),
 \tag{6}
\]

where the completed local factor \(G_\chi\) is meromorphic and is nonzero
away from its explicitly removed polar/trivial channels.  The multiplier in
(6) is not the definition of the CCM cokernel; it is the Plancherel image of
the same reduction map after ordinary Hilbert completion.

On every compact interval avoiding the finitely many polar points,
\(m_\chi\) is the boundary value of a nonzero meromorphic function.  Its zero
set is discrete and hence has Lebesgue measure zero.  Removing the polar
channels does not change the following conclusion.

### Theorem 3.1 — The reduced Plancherel cokernel vanishes

Let

\[
 H^1_{(2),\chi}
 :=\mathcal H_\chi/
   \overline{\operatorname {Ran}M_{m_\chi}}.
 \tag{7}
\]

Then

\[
 \boxed{H^1_{(2),\chi}=0.}
 \tag{8}
\]

Consequently the direct sum over \(\chi\) also vanishes.

#### Proof

The completed \(L\)-function is not identically zero.  Its boundary zero set
on the critical line is discrete, hence null.  Lemma 2.1 applies to
\(m_\chi\) and proves (8). \(\square\)

This theorem explains why the closure used by CCM cannot be replaced by
Hilbert closure.  In the nuclear Schwartz/Meyer topology, evaluation and
jets at isolated Mellin zeros are continuous distributions and survive in
the cokernel.  In \(L^2(d\gamma)\), a discrete set is invisible.

## 4. Exact local form of the resonant pairing

The preceding collapse does not depend on whether RH is true.  To see what
the nuclear topology retains, consider a finite simple zero orbit under

\[
 \rho\longmapsto\bar\rho,
 \qquad
 \rho\longmapsto1-\rho.
 \tag{9}
\]

For a Mellin test function \(F\), the sharp involution satisfies

\[
 \widehat{F^\sharp}(\rho)
 =\overline{\widehat F(1-\bar\rho)}.
 \tag{10}
\]

Hence the contribution of the pair
\(\{\rho,1-\bar\rho\}\) to the CCM trace form is, up to the positive
multiplicity normalization,

\[
 q_\rho(F)
 =\widehat F(\rho)
   \overline{\widehat F(1-\bar\rho)}
 +\widehat F(1-\bar\rho)
   \overline{\widehat F(\rho)}.
 \tag{11}
\]

If \(\rho=1-\bar\rho\), (11) collapses to a positive square.  If the two
points are distinct, the Hermitian matrix of (11) is

\[
 \begin{pmatrix}0&1\\1&0\end{pmatrix},
 \tag{12}
\]

and has inertia \((1,1)\).

### Proposition 4.1 — A compatible positive Hodge star is a local
exclusion theorem

Let \(V_\rho\) be the resonant two-plane in (11), and let normalized scaling
act with eigencharacters

\[
 e^{(\rho-1/2)t},
 \qquad e^{(1/2-\bar\rho)t}.
 \tag{13}
\]

There is no positive definite Hermitian form on \(V_\rho\) for which this
action is unitary unless \(\Re\rho=1/2\).

#### Proof

If \(v\ne0\) is an eigenvector with exponent
\(\lambda=\rho-1/2\), unitarity gives

\[
 \|v\|^2=\|e^{t\lambda}v\|^2
 =e^{2t\Re\lambda}\|v\|^2
 \quad(t\in\mathbb R).
 \tag{14}
\]

Positivity makes \(\|v\|^2>0\), so (14) forces
\(\Re\lambda=0\), equivalently \(\Re\rho=1/2\). \(\square\)

Thus the missing polarization is not a bounded change of metric on the
Plancherel quotient.  It must simultaneously retain the resonant jets and
prove that their normalized scaling is unitary.

## 5. The correct chain-level target

Let

\[
 \mathfrak C_{\rm rel}
 =\operatorname {Cone}
 \bigl(
 \mathscr S(\mathcal G_{\mathbb Q})^\natural_0
 \xrightarrow{\rho^\natural}
 \mathbf S^\natural(C_{\mathbb Q},\mathcal L^1(\mathcal H_x))
 \bigr)
 \tag{15}
\]

be the actual relative cyclic cone.  The Fourier--Weyl operator of 106.156
supplies a positive chain metric before passage to resonant cohomology.  A
global arithmetic Hodge theorem must now construct an unbounded chain star

\[
 \star_{\rm ar}:\mathfrak C_{\rm rel}\supset\mathcal D
 \longrightarrow\mathfrak C_{\rm rel},
 \tag{16}
\]

on a common nuclear core such that

\[
 \begin{aligned}
 &\star_{\rm ar}^2=-1 &&\text{in relative degree one},\\
 &\star_{\rm ar}d=d\star_{\rm ar},\\
 &\Omega(c,\star_{\rm ar}c)\ge0,\\
 &\Omega(c,\star_{\rm ar}c)=0
   \Longrightarrow[c]=0,\\
 &\star_{\rm ar}\vartheta_t=\vartheta_t\star_{\rm ar}.
 \end{aligned}
 \tag{17}
\]

The fourth line is the faithful-descent clause.  It is exactly what the
ordinary \(L^2\) construction loses by Theorem 3.1.  The first three lines
are already available on the Fourier--Weyl chain model; the remaining work
is to prove that its star preserves, and is nondegenerate on, the
distributional resonant cohomology rather than only on the reduced
Plancherel cohomology.

## 6. Consequences for the construction programme

Theorem 3.1 closes three tempting but incorrect shortcuts.

1. A quotient norm on the Haar \(L^2\) completion is positive but has no
   degree-one classes.
2. Replacing the CCM closure by Hilbert closure changes the cohomology and
   discards the spectral realization.
3. A bounded chain map from CCM degree one into the reduced \(L^2\)
   cohomology cannot be faithful, because its target is zero.

The viable target is therefore narrower than “find a positive Hilbert
completion”.  One must construct the unbounded resonant star (16) and prove
the faithful-descent statement in (17) using the arithmetic localization on
the Abel--Jacobi fibers.  That statement is the next theorem to attack.

## 7. Status

Proved here:

* dense range of the Tate multiplier in every Plancherel character sector;
* vanishing of the reduced \(L^2\) version of CCM degree one;
* exact signature of one off-line resonant pair;
* impossibility of a positive scaling-compatible metric on such a pair;
* the precise unbounded chain-star target which avoids the \(L^2\) collapse.

Not proved here:

* existence and faithful descent of \(\star_{\rm ar}\) on the resonant CCM
  cohomology.
