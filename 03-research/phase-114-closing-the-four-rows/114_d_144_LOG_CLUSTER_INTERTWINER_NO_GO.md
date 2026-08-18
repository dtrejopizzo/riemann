# D.144 — Log-cluster obstruction to a global label--Gamma intertwiner

## Verdict

Separating the half-Tate factor from the label norm removes the elementary
scaling obstruction of D.142, but it still does not permit a global bounded
equivariant map from the commutative label Hilbert space to the Gamma
translation space.

Let

\[
 H_{\rm lab}=\ell^2(\mathbb N),\qquad
 \widetilde L_m e_n=e_{mn},                            \tag{0.1}
\]

and let (U_t) be any strongly continuous unitary group.  If a bounded
operator (T:H_{\rm lab}\to H_\infty) satisfies

\[
 T\widetilde L_m=U_{\log m}T\qquad(m\geq1),           \tag{0.2}
\]

then

\[
 \boxed{T=0.}                                         \tag{0.3}
\]

Unlike the central-weight argument, this result does not use norm decay of
the label shifts.  It follows from the clustering

\[
 \log(N+j)-\log N\longrightarrow0
\]

on arbitrarily long consecutive blocks.  A nonzero strongly continuous
unitary orbit along ({\log n}) is never a Bessel sequence, while the
image of an orthonormal basis under a bounded operator must be Bessel.

Consequently the prime--Gamma comparison required by D cannot factor as a
single bounded equivariant map on a global label Hilbert space, even after
the half-Tate character is kept as a separate metric line.  The viable
comparison must be support-local, distributional, or carry a nontrivial
boundary cocycle.  This agrees with the threshold behavior in D.137 and
the annular cocycle in D.81.

No sign of (B_{\rm nuc}), zero of \(\xi\), or RH is used.  The paper is
not modified.

## 1. A unitary log-orbit is not Bessel

Recall that a sequence ((x_n)) in a Hilbert space is Bessel if there is
(B<\infty) such that, for every finitely supported scalar sequence (c),

\[
 \left\|\sum_nc_nx_n\right\|^2
 \leq B\sum_n|c_n|^2.                                 \tag{1.1}
\]

Let (h\ne0) and put

\[
 x_n=U_{\log n}h.                                     \tag{1.2}
\]

Fix an integer (r\geq1).  Strong continuity at zero gives a
(\delta_r>0) such that

\[
 |t|<\delta_r
 \quad\Longrightarrow\quad
 \|(U_t-I)h\|<{1\over2}\|h\|.                       \tag{1.3}
\]

Choose (N) so large that

\[
 0\leq\log(N+j)-\log N<\delta_r
 \qquad(0\leq j<r).                                  \tag{1.4}
\]

For (c_{N+j}=r^{-1/2}) and all other (c_n=0), unitarity gives

\[
\begin{aligned}
 \left\|{1\over\sqrt r}\sum_{j=0}^{r-1}
 U_{\log(N+j)}h\right\|
 &=\left\|{1\over\sqrt r}\sum_{j=0}^{r-1}
 U_{\log(1+j/N)}h\right\|\\
 &\geq \sqrt r\,\|h\|
 -{1\over\sqrt r}\sum_{j=0}^{r-1}
   \|(U_{\log(1+j/N)}-I)h\|\\
 &>{1\over2}\sqrt r\,\|h\|.                       \tag{1.5}
\end{aligned}
\]

The coefficient vector has norm one.  Hence any Bessel bound would satisfy

\[
 B>{r\over4}\|h\|^2                                  \tag{1.6}
\]

for every (r), which is impossible.  We have proved:

> **Log-cluster lemma.**  For every nonzero vector of a strongly continuous
> unitary group, the sequence ((U_{\log n}h)_{n\geq1}) is not Bessel.

The proof uses only consecutive integers, which are present in the full
row-B correspondence family.  It also survives restriction to the prime
labels: for every fixed (r), the prime number theorem gives
(p_{N+j}/p_N\to1) uniformly for (0\leq j<r), so the same log-cluster
argument applies to (r) consecutive primes.  Since the prime-power
contact family contains all primes, discarding mixed composite contacts or
changing their multiplicities does not repair the obstruction.  A sparse
single-prime tower is different, but it is not the complete A--B--C label
family.

## 2. Proof of the intertwiner theorem

The vector (e_1) is cyclic for the semigroup in (0.1), since

\[
 \widetilde L_ne_1=e_n.                               \tag{2.1}
\]

Let (h=Te_1).  From (0.2),

\[
 Te_n=T\widetilde L_ne_1=U_{\log n}h.                 \tag{2.2}
\]

Because ((e_n)) is orthonormal and (T) is bounded, its image sequence
is Bessel with bound (|T|^2):

\[
 \left\|\sum_nc_nTe_n\right\|^2
 \leq\|T\|^2\sum_n|c_n|^2.                           \tag{2.3}
\]

The log-cluster lemma forces (h=0).  Equation (2.2) then gives
(Te_n=0) for every (n), so (T=0).  This proves (0.3).

The same argument applies to any Hilbert target on which the A--B--C label
(n) acts by the strongly continuous logarithmic translation
(U_{\log n}), including the full-line Gamma screw and its ordinary
translation-covariant dilations.

## 3. Why a rigged map is not a Hilbert contraction

On the nuclear test algebra, distributional maps may intertwine the label
action with translations.  The log-cluster lemma does not forbid them,
because their images need not be Bessel and the map need not extend to the
middle Hilbert spaces.

This distinction is essential.  A distributional intertwiner can preserve

* every point mass (delta_{p^k});
* the Mangoldt functional;
* both Tate boundary characters; and
* the Gamma translation law,

but it cannot be cited as the contractive map

\[
 C_T:\overline{X_T(\mathcal P_T)}\to\mathcal Y_T.     \tag{3.1}
\]

The latter is a bounded Hilbert operator after the graph completion of a
fixed support window.  Moving from the rigged map to (3.1) requires a
support-dependent regularization, and its norm-one estimate remains a
separate assertion.

## 4. Compatibility with the finite-window construction

For fixed (T), only finitely many translations (k\log p\leq2T) occur
in the explicit feature maps.  A finite family is automatically Bessel,
so the theorem does not obstruct the algebraic comparison

\[
 C_T^0(X_TF)=Y_TF.                                    \tag{4.1}
\]

It obstructs promoting all those finite comparisons to one global bounded
operator that is equivariant for every label.  This is exactly what is
seen at prime-power birth thresholds:

* the signed cross-effect (B_{\rm nuc}) is compatible under support
  enlargement;
* the separate positive channels jump in operator norm; and
* a new annular boundary component must be stabilized at every threshold.

Therefore the correct global object, if constructed, must be a directed
system of support-local contractions with explicit threshold cocycles.  It
cannot be a constant global contraction tensored with the label module.

## 5. Consequence for the live route

Together D.142--D.144 exclude both naive Hilbert factorizations:

\[
\begin{array}{c|c}
\text{label norm}&\text{failure of a global Gamma intertwiner}\\ \hline
\|L_m\|=m^{-1/2}&\text{unitary covariance forces }T=0
                  \text{ by norm decay}\\
\|\widetilde L_m\|=1&\text{strong continuity forces }T=0
                  \text{ by log clustering}.
\end{array}                                             \tag{5.1}
\]

The remaining construction must therefore solve the support-local
prime--Gamma boundary cocycle and prove a uniform norm bound on the
resulting directed maps.  The exact acceptance condition is still

\[
 C_TX_T=Y_T,qquad\|C_T\|\leq1,                       \tag{5.2}
\]

but (5.2) can no longer be sought as a global tensor-factor intertwiner.
