# P122 -- finite successor paths realize Frobenius lengths

## Status

`ELEMENTARY/CLASSICAL CONSTRUCTION + PROVED PROGRAMME APPLICATION` as a
finite positive bridge inside the affine carrier.  The telescoping path and
kernel `log min(m,n)` are elementary Brownian-covariance facts; novelty is
claimed only, provisionally, for testing this combination against R/S.  Its
unavoidable cross-prime Gram terms are not present in row C, so the bridge
is pre-scalar data rather than a positive realization of the Weil form.  No
Gate R/S theorem is claimed.

## 1. A positive discrete Gamma differential

On the affine integer Hilbert space of P122.024, let

\[
 B=S^*HS-H.                                         \tag{1.1}
\]

Since `H e_(n-1)=log n e_(n-1)`, one has

\[
 \boxed{
 Be_{n-1}=b_ne_{n-1},
 \qquad b_n=\log{n+1\over n}>0.}                   \tag{1.2}
\]

Thus `B` is positive, bounded and compact.  It is not trace class because
its partial traces telescope to `log(N+1)`.

Let `E_edge=ell^2(N)` with basis `epsilon_n`, and define the path from the
integer `1` to the integer `m` by

\[
 g_m=\sum_{n=1}^{m-1}\sqrt{b_n}\,\epsilon_n,
 \qquad g_1=0.                                      \tag{1.3}
\]

### Theorem 1.1 -- exact logarithmic path metric

For positive integers `m,n`,

\[
 \boxed{
 \begin{aligned}
 \|g_m\|^2&=\log m,\\
 \langle g_m,g_n\rangle&=\log\min(m,n),\\
 \|g_m-g_n\|^2&=|\log m-\log n|.
 \end{aligned}}                                      \tag{1.4}
\]

#### Proof

The supports in (1.3) are nested and

\[
 \sum_{j=1}^{m-1}b_j
 =\sum_{j=1}^{m-1}\log{j+1\over j}=\log m.         \tag{1.5}
\]

The other two formulas follow by taking the common initial segment and its
complement.  QED.

For a prime, the endpoint is exactly the Frobenius vacuum image:

\[
 V_pe_0=e_{p-1},\qquad \|g_p\|^2=\log p.           \tag{1.6}
\]

Hence the Frobenius length is the energy of the unique additive successor
path joining the Gamma vacuum to its multiplicative image.  This is finite;
it does not use the zeta-regularized dimension anomaly of P122.024.

## 2. Prime-power normalization

The local generator path `g_p` is reused along the Frobenius tower.  Put

\[
                 \eta_{p,j}=p^{-j/4}g_p.           \tag{2.1}
\]

Then

\[
 \boxed{
 \|\eta_{p,j}\|^2={\log p\over p^{j/2}}.}         \tag{2.2}
\]

Thus the exact coefficient `Lambda(p^j)p^(-j/2)` is the squared norm of a
source-defined affine path vector.  Reusing `g_p`, rather than using the
long path `g_(p^j)`, is essential: the latter has squared norm `j log p`
and repeats the Fock-depth error of D.194.

## 3. Cross-prime information and its cost

For distinct primes,

\[
 \langle\eta_{p,j},\eta_{q,k}\rangle
 =p^{-j/4}q^{-k/4}\log\min(p,q).                  \tag{3.1}
\]

These entries are nonzero.  Therefore the bridge retains genuine
cross-place information before scalar trace, unlike an orthogonal direct
sum of local Euler lines.

But row C is a **linear** sum of prime-power contacts.  Taking the ordinary
positive norm of a superposition gives

\[
 \left\|\sum_{p,j}c_{p,j}\eta_{p,j}\right\|^2
 =\sum_{p,j}|c_{p,j}|^2{\log p\over p^{j/2}}
 +\sum_{(p,j)\ne(q,k)}
 c_{p,j}\overline{c_{q,k}}
 p^{-j/4}q^{-k/4}\log\min(p,q),                  \tag{3.2}
\]

and the second sum has no counterpart in the explicit formula.

Consequently one cannot identify (3.2) with the Weil form.  The cross terms
must live in a pre-scalar graded complex and cancel under its
degree/supertrace while still controlling equality states.  Orthogonalizing
the prime paths would recover the scalar coefficients but erase exactly the
new affine coupling.

## 4. What the bridge adds to D

The data

\[
 (\mathcal H_{\rm aff},S,H,V_p,g_p,\eta_{p,j})     \tag{4.1}
\]

provide a literal finite Gamma--Euler incidence object:

* `S,H` define the positive additive Gamma edge energy;
* `V_p` selects its Frobenius endpoint;
* the path energy is `log p`;
* modular half-density gives `p^(-j/2)`;
* overlaps retain cross-prime incidence.

This object is independent of `B_nuc` positivity and fails to reduce to a
mere scalar loop cocycle.  Its missing operation is now precise: construct
a graded boundary differential whose supertrace removes the cross terms in
(3.2), agrees with row C, and whose horizontal null equation implies the
sharp-window transmission of P122.020.

The last clause is not supplied by path exactness.  Since each `g_m` is the
gradient of the scalar `log m`, its ordinary loop curvature is zero.  A
nonzero oriented law must involve the physical causal/window boundary, not
only the integer path metric.

```text
finite Gamma successor differential                 CONSTRUCTED
path 1 -> p has energy log p                         PROVED
prime-power half-density coefficient                 PROVED
cross-prime pre-scalar Gram                          NONZERO
ordinary positive Gram equals row C                  FALSE
graded causal transgression controlling equality    OPEN
```
