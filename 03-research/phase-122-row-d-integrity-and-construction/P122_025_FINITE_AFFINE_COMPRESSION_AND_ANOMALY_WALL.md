# P122 -- finite affine compression and the regularized-anomaly wall

## Status

`PROVED-IN-REPOSITORY`.  This note tests the affine carrier P122.024 at the
finite arithmetic cutoff relevant to a support window.  Its defining
affine relation survives compression exactly, while its Gauss `log p`
connection anomaly is a zeta-regularized infinite-rank effect.  Neither
fact supplies Gate S at finite first contact.

## 1. Natural finite arithmetic compression

Let

\[
 Q_N\mathcal H_{\rm aff}
 =\operatorname {span}\{e_0,\ldots,e_{N-1}\},     \tag{1.1}
\]

corresponding to the integers `1,...,N`.  Put

\[
 S_N=Q_NSQ_N,qquad V_{m,N}=Q_NV_mQ_N.             \tag{1.2}
\]

The support cutoff `n<e^(2T)` is of this form, up to the harmless strict
endpoint convention.

### Proposition 1.1 -- affine covariance has no finite boundary defect

For every `m>=1`,

\[
                     V_{m,N}S_N=S_N^mV_{m,N}.      \tag{1.3}
\]

#### Proof

Both sides send `e_k` to `e_(m(k+2)-1)` if
`m(k+2)<=N`, and to zero otherwise.  The intermediate truncations introduce
the same final inequality on both sides.  QED.

Thus the most natural curvature candidate
`V_(m,N)S_N-S_N^mV_(m,N)` vanishes identically.  It cannot be the
transverse seam detector.

## 2. The partial-isometry index is also zero

The compressed multiplication map has rank `floor(N/m)` and

\[
 \begin{aligned}
 V_{m,N}^*V_{m,N}
   &=\text{projection onto }\{1\leq n\leq N/m\},\\
 V_{m,N}V_{m,N}^*
   &=\text{projection onto multiples of }m\text{ not exceeding }N.
                                                               \tag{2.1}
 \end{aligned}
\]

Both projections have the same rank.  Consequently

\[
 \operatorname {Tr}
 (V_{m,N}^*V_{m,N}-V_{m,N}V_{m,N}^*)=0.            \tag{2.2}
\]

The much larger individual defects have equal dimension.  Their positive
rank is the already-refuted Fock defect of D.194, not `Lambda(m)`.

## 3. Finite residue determinants have no `log p` normal anomaly

Partition `0,...,N-1` into residue classes modulo `p`.  Let

\[
 N_r=\#\{0\leq j<N:j\equiv r\pmod p\},
 \qquad \alpha_r={r+a\over p}.                    \tag{3.1}
\]

The literal finite determinant identity is

\[
 \boxed{
 \prod_{j=0}^{N-1}(j+a)
 =p^N\prod_{r=0}^{p-1}
       \prod_{k=0}^{N_r-1}(k+\alpha_r).}           \tag{3.2}
\]

Differentiating in `a` gives only the tautological partition

\[
 \sum_{j=0}^{N-1}{1\over j+a}
 ={1\over p}\sum_{r=0}^{p-1}
       \sum_{k=0}^{N_r-1}{1\over k+\alpha_r}.      \tag{3.3}
\]

There is no `log p` term because the finite scaling exponent `N` is
independent of `a`.

In contrast, zeta scaling replaces `N` by

\[
 \sum_{r=0}^{p-1}\zeta_H(0,\alpha_r)=\frac12-a.   \tag{3.4}
\]

Differentiation of `p^(1/2-a)` is exactly the `-log p` anomaly of
P122.024.  Therefore that coefficient is a genuine regularized-dimension
anomaly at the infinite Gamma end; it is not a finite determinant boundary
term hidden in (3.2).

## 4. Two-prime compression does not force seam matching

For distinct primes `p,q`, the ranges of `V_(p,N)` and `V_(q,N)` intersect
on multiples of `pq`.  Their complements and intersection are completely
determined by elementary divisibility, but (1.3) provides no equality
between the normalized physical outputs `E_(p,T)h` and `E_(q,T)h`.

Indeed, the affine relations hold for every input vector, whereas equality
of one transverse seam on a nonzero first-contact state is impossible by
the phase-121 first-cell theorem.  If the algebraic relations alone implied
that equality, they would already force every input to vanish, a
contradiction.

What can still be sought is a **nontrivial horizontal equation** involving
the Gamma resolvent/connection, not merely the universal relations of the
carrier.  Its boundary term would have to distinguish first-contact
sections from arbitrary vectors and be proved before the scalar Weil
comparison.

## 5. Consequence

The affine carrier remains a useful part of `D_candidate`: it is the first
common, noncommutative Gamma--Euler source algebra and explains `log p` by
Gauss descent.  But its current exact identities divide sharply into:

```text
finite affine relations                 exact and boundary-free;
infinite zeta-determinant anomaly       nonzero and cofinal;
finite first-contact seam law           not supplied by either.
```

Importing the cofinal anomaly into a fixed finite support window without a
restriction theorem would repeat the inactive-prime error already excluded
in phase 121.  The next admissible object is a relative finite/infinite
transgression whose boundary is computed explicitly; it cannot be inferred
from (3.4) alone.
