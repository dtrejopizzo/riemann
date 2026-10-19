# P122 -- the explicit two-prime finite Green complex

## Status

`PROVED-IN-REPOSITORY`.  This is the finite calculation requested in
P122.020 and P122.024: two prime fibres joined through the additive Gamma
successor path.  The complex has an exact positive Dirichlet-to-Neumann
form whose kernel is precisely the transverse seam.  Nothing in the affine
relations or the first-contact scalar equation forces that energy to be
zero.  Thus Gate S remains the whole missing horizontal theorem, not a
consequence of the carrier.

## 1. The finite Gamma path complex

Fix integers `2<=p<q` (primality is used only when the endpoint data are
interpreted as Frobenius fibres) and put

\[
 b_n=\log{n+1\over n},\qquad p\leq n<q.            \tag{1.1}
\]

For an arbitrary Hilbert coefficient space `K`, define

\[
 C^0_{p,q}(K)=K^{\{p,p+1,\ldots,q\}},\qquad
 C^1_{p,q}(K)=K^{\{p,p+1,\ldots,q-1\}},            \tag{1.2}
\]

and

\[
 (d_{p,q}u)_n=b_n^{-1/2}(u_{n+1}-u_n).             \tag{1.3}
\]

This differential is determined by the positive successor commutator
`S^*HS-H` of P122.027.  It is defined before any Weil-form comparison.

## 2. Exact Green formula

Write

\[
 j_n(u)=b_n^{-1}(u_{n+1}-u_n).                     \tag{2.1}
\]

Discrete summation by parts gives

\[
 \begin{aligned}
 \langle d_{p,q}u,d_{p,q}v\rangle
 ={}&\sum_{n=p+1}^{q-1}
   \langle j_{n-1}(u)-j_n(u),v_n\rangle\\
 &+\langle j_{q-1}(u),v_q\rangle
   -\langle j_p(u),v_p\rangle .                   \tag{2.2}
 \end{aligned}
\]

Thus the interior Laplacian is

\[
 (L_{p,q}u)_n=j_{n-1}(u)-j_n(u),                  \tag{2.3}
\]

and the oriented boundary flux is `(-j_p,j_(q-1))`.

## 3. Dirichlet-to-Neumann form

### Theorem 3.1 -- exact two-prime effective energy

For prescribed endpoints `u_p=x`, `u_q=y`, there is a unique minimizer of
`||d_(p,q)u||^2`.  It is harmonic, has constant flux

\[
 j_n(u)={y-x\over\log(q/p)},                       \tag{3.1}
\]

and its energy is

\[
 \boxed{
 \mathcal E_{p,q}^{\rm eff}(x,y)
 ={\|y-x\|^2\over\log(q/p)}.}                     \tag{3.2}
\]

#### Proof

The Euler--Lagrange equation is `L_(p,q)u=0`, hence the flux (2.1) is
constant.  Since

\[
 \sum_{n=p}^{q-1}b_n=\log(q/p),                   \tag{3.3}
\]

summing `u_(n+1)-u_n=b_nj` gives (3.1).  Substitution into

\[
 \|d_{p,q}u\|^2=\sum_{n=p}^{q-1}b_n\|j\|^2        \tag{3.4}
\]

proves (3.2).  Strict convexity modulo constants gives uniqueness for fixed
endpoints.  QED.

In particular,

\[
 \mathcal E_{p,q}^{\rm eff}(x,y)=0
 \quad\Longleftrightarrow\quad x=y.                \tag{3.5}
\]

## 4. Substitution of the physical prime traces

Let

\[
 x=E_{p,T}\mathfrak h_F,\qquad
 y=E_{q,T}\mathfrak h_F                            \tag{4.1}
\]

in their common coefficient Hilbert space (or after the canonical direct
embedding used by the phase-120 seam bank).  Then

\[
 \mathcal E_{p,q}^{\rm eff}(F)
 ={\|(E_{q,T}-E_{p,T})\mathfrak h_F\|^2
   \over\log(q/p)}.                                \tag{4.2}
\]

At first contact, phase 121 proves

\[
 \mathcal E_{p,q}^{\rm eff}(F)=0\quad\Longrightarrow\quad F=0. \tag{4.3}
\]

So the finite Gamma path supplies a canonical positive detector of exactly
Gate S, including its coefficient.

## 5. Decisive kernel audit

For every pair `(x,y)`, not only for matching pairs, Theorem 3.1 supplies a
harmonic extension.  Horizontality in the sense `L_(p,q)u=0` therefore does
**not** imply `x=y`; it only makes the flux constant.  Equality of the
endpoints is equivalent to the additional zero-flux/zero-energy condition.

The universal affine relations also hold for every source vector.  They do
not set the boundary flux in (2.2) to zero.  Finally, the scalar
first-contact equation says that the compressed Weil form has a null
vector; no comparison currently identifies that nullity with
`mathcal E_(p,q)^eff(F)=0`.

Consequently the desired implication

\[
 P_T\mathcal A_\infty F=0
 \quad\Longrightarrow\quad
 \mathcal E_{p,q}^{\rm eff}(F)=0                  \tag{5.1}
\]

is not proved by the finite complex.  Adding (4.2) as a positive summand to
an asserted Green decomposition would prove the sign only if the remaining
term were positive; P122.014 shows that constructing that positive
comparison from Gram columns is equivalent to row (d).

This is the exact sense in which Gate S is a wall rather than a peer of
Gate R: its detector and its full finite Green complex are explicit, but
the zero-flux law is still the independent global sign-bearing theorem.

## 6. Consequence for the programme

The two-prime test does not justify adding more primes or another carrier.
It returns the following final finite diagram:

```text
affine/Gamma successor data
        -> canonical two-prime Green complex       CONSTRUCTED
        -> DtN = seam norm / log(q/p)               PROVED
first-contact nullity
        -> zero DtN flux                            NOT CONSTRUCTED
zero DtN flux
        -> seam zero -> F=0                         PROVED
```

Future work on S is admissible only if it introduces an independent input
that proves the missing middle arrow.  Relations derived solely from
`log p`, `p^(-1/2)`, `N` and `Gamma` cannot be cited as such an input: those
data already define both sides of the scalar explicit formula.
