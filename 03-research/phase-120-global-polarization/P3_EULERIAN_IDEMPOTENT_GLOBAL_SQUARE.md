# Phase 120 — Eulerian-idempotent global-square candidate

## Status

Corrected after the finite-rank audit.  Sections 2--4 contain exact algebraic
identities.  They do **not** construct a common Euler--Gamma chain complex.
The original Sections 5--6 silently declared its differential and then boxed
a condition equivalent to the desired vanishing.  That claim is withdrawn
below.  The Eulerian idempotent remains a useful simultaneous description of
connected projection and von Mangoldt extraction, but it is not yet a
global-square mechanism.

## 1. The actual obstruction

There are two incompatible operations in every previous positive carrier:

1. tensor multiplication preserves positivity but creates mixed labels
   \(p^iq^j\), \(p\ne q\);
2. the logarithm eliminates those mixed labels and produces von Mangoldt
   support, but was treated as a scalar operation and therefore lost its
   positive Hilbert carrier.

The missing construction is a positive **connected linearization** of the
logarithm. The Witt/Hopf structure already present in rows (a)--(b) supplies
one canonically: the Eulerian idempotent.

## 2. Connected linearization

Work first in a complete connected graded commutative Hopf algebra over
\(\mathbb R\). Let \(\star\) denote convolution on endomorphisms and put

\[
 \mathfrak e
 =\log^\star(\operatorname{Id})
 =\sum_{m\ge1}\frac{(-1)^{m-1}}m
   (\operatorname{Id}-\eta\varepsilon)^{\star m}.    \tag{2.1}
\]

On every finite graded piece the sum terminates. For a group-like element
\(g\),

\[
 \mathfrak e(g)=\log(g)                              \tag{2.2}
\]

in the completed augmentation algebra, and its value is primitive:

\[
 \Delta\mathfrak e(g)
 =\mathfrak e(g)\otimes1+1\otimes\mathfrak e(g).     \tag{2.3}
\]

Thus \(\mathfrak e\) is the canonical connected-part projection. It is
defined before any trace pairing or sign.

## 3. Exact von Mangoldt extraction

At one place introduce the universal symmetric-function/Witt series

\[
 H_p(z)=\sum_{j\ge0}h_{p,j}z^j
       =\exp\!\left(\sum_{j\ge1}\frac{q_{p,j}}jz^j\right),          \tag{3.1}
\]

where the ghost coordinates \(q_{p,j}\) are primitive. Equations
(2.1)--(2.3) give

\[
 \mathfrak e(H_p(z))
 =\sum_{j\ge1}\frac{q_{p,j}}jz^j.                    \tag{3.2}
\]

Let \(\mathcal N=z\partial_z\) be the grading derivation and substitute the
central character \(z=p^{-1/2}\). Then

\[
 (\log p)\mathcal N\mathfrak e(H_p)(p^{-1/2})
 =\sum_{j\ge1}(\log p)p^{-j/2}q_{p,j}.               \tag{3.3}
\]

This is the complete von Mangoldt prime-power current, with no \(1/j\), no
factorial and no extra \(j\).

The required Hopf lift is supplied universally by the two operations of the
big Witt ring. Write \([a]=(1-at)^{-1}\) for a Teichmuller element. Witt
multiplication and the ghost maps satisfy

\[
 [a]\odot[b]=[ab],
 \qquad {\rm gh}_j([a])=a^j.                        \tag{3.3a}
\]

Define

\[
 \iota_p(\Gamma_{p^j})=[x_p^j].                     \tag{3.3b}
\]

Then

\[
 \iota_p(\Gamma_{p^i})\odot\iota_p(\Gamma_{p^j})
 =[x_p^{i+j}]
 =\iota_p(\Gamma_{p^{i+j}}),                         \tag{3.3c}
\]

so coefficient-one Frobenius fusion is retained exactly. On the other hand,
Witt addition is ordinary multiplication of Euler series, and the ghost/log
map makes it additive. Thus fusion and connected linearization use the two
different, canonical Witt operations; no factorial quotient or idempotent
flat join is introduced.

For the local Euler element \([p^{-1/2}V_{\log p}]\), its \(j\)-th ghost is
\(p^{-j/2}V_{j\log p}\). Its connected logarithm carries the coefficient
\(1/j\); the scale derivation contributes \(j\log p\). These factors cancel,
which identifies (3.3) with the literal \(p^j\) contact current.

### Theorem 3.0 — exact Witt lift of row-(b) fusion

Equations (3.3a)--(3.3c) define a faithful lift of every prime-power tower,
intertwine row-(b) composition with Witt multiplication, and send the
connected logarithmic derivative of the local Euler element to the exact
von Mangoldt contact current.

#### Proof

The first two assertions are (3.3a)--(3.3c). The ghost calculation in the
preceding paragraph gives the last assertion. Distinct powers remain distinct
as Teichmuller monomials, so the lift is faithful. QED.

For a finite prime set \(S\),

\[
 \mathfrak e\!\left(\prod_{p\in S}H_p\right)
 =\sum_{p\in S}\mathfrak e(H_p).                     \tag{3.4}
\]

Hence every mixed composite \(p^iq^j\), \(p\ne q\), vanishes before taking a
norm. This is exactly the property the tensor-Casimir carrier left as gate
(5.3).

### Theorem 3.1 — exact connected contact theorem

The operator

\[
 J_{S}^{\rm conn}
 =\sum_{p\in S}\sum_{j\ge1}
   \sqrt{\log p}\,p^{-j/4}\,
   q_{p,j}\otimes (I-V_{j\log p})                   \tag{3.5}
\]

on the algebraic compact core is a positive jump current, is orthogonal
between distinct primitive labels \((p,j)\), and contains no mixed-composite
label. More precisely, with \(w_{p,j}=(\log p)p^{-j/2}\),

\[
 \|(J_S^{\rm conn})F\|^2
 =\sum_{p,j}w_{p,j}\|F-V_{j\log p}F\|^2.            \tag{3.6}
\]

Consequently the connected contact is recovered exactly as

\[
 2\sum_{p,j}w_{p,j}\Re\langle F,V_{j\log p}F\rangle
 =2A_S\|F\|^2-\|(J_S^{\rm conn})F\|^2,              \tag{3.7}
\]

where \(A_S=\sum_{p,j}w_{p,j}\).

#### Proof

Give the primitive ghost coordinates the source-edge metric
\(\langle q_{p,i},q_{q,j}\rangle=\delta_{pq}\delta_{ij}\). Pythagoras gives
(3.6), and expansion of every difference gives (3.7). Equation (3.4) proves
that these are precisely the universal connected labels of the Euler product.
The physical rank-one contact line is the image of their coherent divergence,
not this source-edge metric itself. QED.

The distinction from a Haar/free-product construction is load-bearing:
fusion remains in the ambient Witt algebra, while only its connected trace
current is projected to the one-particle space.

## 4. Archimedean connected current

The Weierstrass expansion of the quarter-Gamma determinant has the same
connected form. With \(\alpha_n=n+1/4\), introduce primitive oscillator
coordinates \(q_{\infty,n}\). The already proved Gamma reservoir is

\[
 J_\infty F
 =\left(
   \alpha_n^{-1/2}\frac{-i\tau}{2\alpha_n-i\tau}
   \widehat F(\tau)
  \right)_{n\ge0},                                  \tag{4.1}
\]

and

\[
 J_\infty^*J_\infty=M_{g_\Gamma}.                   \tag{4.2}
\]

Thus both Euler and Gamma now live in primitive one-particle Hilbert spaces.
The scalar logarithm has disappeared from the construction.

## 5. Correction: the differential was not constructed

Let \(\mathscr P_S\) denote the formal primitive ghost space generated by
the arithmetic labels \(q_{p,j}\) and by a chosen truncation of the Gamma
labels \(q_{\infty,n}\).  Equations (3.5) and (4.1) put positive norms on two
source spaces.  They do not provide a map

\[
 \partial_S:\mathscr P_S\longrightarrow\mathscr V_S.              \tag{5.1}
\]

In particular, neither D.247 nor the two Tate evaluations specify the matrix
entries taking an individual depth label \(q_{p,j}\) to an archimedean
boundary current.  D.247 acts after the prime-power tower has been resummed
into the Hilbert-valued Poisson state

\[
 z_p(F)=\sqrt{1-p^{-1}}\sum_{j\ge0}p^{-j/2}
        V_{j\log p}E_TF,                            \tag{5.2}
\]

and supplies one contact/degree port per place.  The two Tate conditions act
on the profile \(F\), not on the ghost-label space by themselves.  Therefore
the asserted typed comparison and the conclusion that its residual is a
cycle were not established.

There was also a direct logical error in the former boxed condition.  If
\(\partial_SZ_S(F)=0\), then

\[
 \overline{\operatorname{Ran}Z_S}\subseteq\ker\partial_S,
\]

so

\[
 \ker\partial_S\cap\overline{\operatorname{Ran}Z_S}
 =\overline{\operatorname{Ran}Z_S}.
\]

Claiming that this intersection is zero is exactly claiming \(Z_S=0\); it is
not an independent homology theorem.  The former (5.5) and the conclusions
drawn from it are withdrawn.

## 6. The finite \(S=\{2,3,4\}\) rank audit

The arithmetic primitive label space at the first nontrivial gate is

\[
 \mathscr P^{\rm ar}_S
 =\operatorname{span}\{q_{2,1},q_{3,1},q_{2,2}\}.                 \tag{6.1}
\]

There are two distinct levels at which one might try to define a divergence.

### 6.1 Label-only divergence: ruled out

Any divergence which uses only the rank-one contact line at each place
factors as

\[
 \mathscr P^{\rm ar}_S
 \longrightarrow \mathbb C e_2\oplus\mathbb C e_3,
 \qquad q_{p,j}\longmapsto a_{p,j}e_p.             \tag{6.2}
\]

It has rank at most two and hence a nonzero kernel.  If the source-current
normalization of (3.5) is used,

\[
 a_{p,j}=\sqrt{\log p}\,p^{-j/4},
\]

then an explicit surviving class is

\[
 \boxed{
 a_{2,2}q_{2,1}-a_{2,1}q_{2,2}
 =\sqrt{\log2}\left(2^{-1/2}q_{2,1}
                    -2^{-1/4}q_{2,2}\right).
 }                                                   \tag{6.3}
\]

Thus the Eulerian projection followed by the existing rank-one place contact
cannot be injective on primitive ghosts.  This is a dimension theorem, not a
numerical prediction.  Adding two unnamed ``Tate rows'' does not repair it,
because the Tate functionals have not been defined on the independent ghost
labels.

### 6.2 Physical divergence: not a finite label matrix

In the actual Poisson system the summand indexed by \(j\) also carries
\(V_{j\log p}F\).  Distinct depths can therefore remain distinguishable inside
the profile Hilbert space even though they share one place port.  But then the
proposed test is no longer finite-dimensional algebra on the three labels:
one must first construct a depth-sensitive synthesis

\[
 \Sigma_S:
 \bigoplus_{(p,j)\in S}q_{p,j}\otimes\mathcal H_T
 \longrightarrow\mathscr V_{\Gamma,{\rm Tate},T}                  \tag{6.4}
\]

and prove its exact boundary-energy identity.  This is precisely the missing
Euler--Gamma transport, called the physical synthesis map in the earlier
Witt--Fock audit and the positive wiring identity in the four-port reduction.
It cannot be supplied by the Eulerian idempotent, which acts only on labels.

## 7. What a valid homological proof would require

A non-circular proof could still have the following form, but all three
statements must be constructed independently:

1. define explicit operators \(\partial_S\) and \(b_S\) on a common physical
   chain space and prove
   \(\ker\partial_S=\overline{\operatorname{Ran}b_S}\);
2. prove the literal residual belongs to \(\ker\partial_S\);
3. prove the same residual is orthogonal to
   \(\overline{\operatorname{Ran}b_S}\).

Only then does the residual vanish.  At present none of these three claims is
provided by the Eulerian construction.  The first new object required is not
another projection onto primitives, but a canonical depth-sensitive
Euler--Gamma synthesis (6.4).  Its energy identity is the global square, so
it must be proved from additional structure rather than defined from the
target form.

## 8. Counterexample firewall

- Davenport--Heilbronn has no group-like local Witt factor whose Eulerian
  primitive is (3.3).
- The shifted pair gives two primitive ghost coordinates at every
  \((p,j)\). Any future physical synthesis must detect that rank-two local
  input rather than collapse it to the zeta rank-one channel; until that
  calculation is made, the firewall is a required gate rather than a theorem.
- A function-field curve replaces the reduced Witt bar complex by the usual
  polarized \(H^1\) complex.
- Dedekind zeta retains one primitive tower per prime ideal, so a successful
  proof extends to the corresponding GRH.

## 9. Ledger

- Eulerian connected projection (2.1)--(2.3): **PROVED**;
- exact von Mangoldt extraction (3.1)--(3.4): **PROVED**;
- positive connected contact current (3.5): **PROVED**;
- big-Witt lift (3.3a)--(3.3c) of the row-(b) tower: **PROVED
  UNIVERSALLY**;
- positive source norms for Euler and Gamma: **CONSTRUCTED SEPARATELY**;
- common physical chain type: **NOT CONSTRUCTED**;
- label-only divergence on \(S=\{2,3,4\}\): **NON-INJECTIVE BY (6.3)**;
- depth-sensitive synthesis (6.4): **OPEN; THIS IS THE ACTUAL GLOBAL-SQUARE
  INTERFACE**;
- residual cycle and Hodge decomposition: **WITHDRAWN UNTIL (6.4) EXISTS**;
- global square, cofinal limit and row (d): **OPEN**.
