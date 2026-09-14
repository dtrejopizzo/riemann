# Phase 121 -- Euler backshift and radical-transport audit

## Status

A degree-one Euler factor gives an exact operation which can shorten
support.  It preserves one Tate zero and destroys the information at the
other; compactness of its inverse is equivalent to vanishing of the full
mean-zero periodic seam trace.  Applying the same inverse to the
first-contact equation also imports the exterior causal history.  Hence
Euler backshift does not transport a radical to a smaller window without
three additional conditions, two of which are already the moving-Tate and
annular defects.

## 1. The causal Euler divisor

Let

\[
 (V_aF)(t)=F(t-a),\qquad a=\log p,qquad r=e^{-a/2},
\]

and put

\[
                         E_p^+=I-rV_a.              \tag{1.1}
\]

On the full line its causal inverse is

\[
 (E_p^+)^{-1}F=\sum_{j\geq0}r^jV_{ja}F.            \tag{1.2}
\]

The sum is locally finite for compactly supported `F`.  It is precisely the
un-normalized prime Poisson state already present in row (c).

### Proposition 1.1 -- compact inverse iff the periodic seam vanishes

Let `F` be supported in `[L,R]` and let `G=(E_p^+)^{-1}F`.  Then the
following are equivalent:

1. `G` is compactly supported;
2. the stabilized right seam of the prime Poisson state is zero on every
   residue class modulo `a`;
3. `G(t)=0` for `t>R-a`.

When these conditions hold,

\[
                         F=E_p^+G,qquad
 \operatorname {diam}\operatorname {supp}G
 \leq\operatorname {diam}\operatorname {supp}F-a. \tag{1.3}
\]

#### Proof

For `t>R`, equation `E_p^+G=F` becomes

\[
                         G(t)=rG(t-a).              \tag{1.4}
\]

On each class modulo `a`, (1.4) is a geometric tail.  Its stabilized
coefficient is exactly the periodic seam trace.  The tail is compact iff
that coefficient is zero.  If it is zero, backward use of (1.4) gives
`G=0` on `(R-a,infinity)`.  Conversely (3) plainly gives compactness and
zero seam.  The left endpoint is unchanged by the causal inverse, proving
(1.3).  QED.

Thus a compact Euler backshift would contradict minimal first contact if it
also transported primitivity and the radical equation.  Neither transport
is automatic.

## 2. Exact loss of one Tate condition

For

\[
 K_F(z)=\int_{\mathbb R}F(t)e^{-zt}\,dt,
\]

equation (1.1) gives

\[
 K_F(z)=(1-re^{-az})K_G(z).                         \tag{2.1}
\]

Since `r=e^(-a/2)`,

\[
 1-re^{-a/2}=1-e^{-a}\ne0,
 \qquad
 1-re^{a/2}=0.                                      \tag{2.2}
\]

Consequently

\[
 K_F(1/2)=0\Longrightarrow K_G(1/2)=0,              \tag{2.3}
\]

whereas `K_F(-1/2)=0` holds for every `G` and contains no information about
`K_G(-1/2)`.  Differentiating (2.1) at `-1/2` gives

\[
 K_F'(-1/2)=aK_G(-1/2).                             \tag{2.4}
\]

Hence the shortened source is primitive exactly when, in addition to the
original two Tate zeros, the resonant moving Tate jet in (2.4) vanishes.
This is the same jet exposed by the Tate--Volterra formula
`BC_TP=2DB_1'`.

The opposite causal divisor interchanges `1/2` and `-1/2`; it does not
avoid the loss.

## 3. The radical equation acquires a secular and an exterior term

Let `A` be the global translation-invariant Gamma--Euler operator.  It
commutes with `E_p^+`.  If `F=E_p^+G`, then globally

\[
                         AF=E_p^+AG.                \tag{3.1}
\]

At first contact only the restriction

\[
 AF=\alpha e^{-t/2}+\beta e^{t/2}quad(t\in[L,R])  \tag{3.2}
\]

is known.  Causal inversion of (3.2) has two defects.

First, `e^(-t/2)` is the resonant homogeneous mode killed by `E_p^+`.
Unless `alpha=0`, its inverse is a secular multiple of
`t e^(-t/2)`, not a Tate normal vector.  Thus the Lagrange multiplier in
the resonant Tate direction must vanish separately.

Second, evaluating `(E_p^+)^(-1)AF` at a point of the smaller interval
uses `AF(t-ja)` for arbitrarily large `j`.  Those points eventually lie to
the left of `[L,R]`, where (3.2) gives no value.  Their contribution is the
incoming exterior history of v94 (451)--(455).  Dropping it is the usual
compression error.

Therefore a genuine radical backshift requires all of

\[
\begin{array}{ll}
\text{(B1)}&\text{zero full periodic seam, so that }G\text{ is compact};\\
\text{(B2)}&K_F'(-1/2)=0,\text{ so that }G\text{ is primitive};\\
\text{(B3)}&\alpha=0,\text{ so the inverted forcing has no secular mode};\\
\text{(B4)}&\text{zero incoming exterior history on the smaller window}.
\end{array}                                                     \tag{3.3}
\]

Under (B1)--(B4), `G` is a primitive zero mode on a strictly shorter
interval, contradicting the definition of first contact.  This implication
is valid but does not help unless (B1)--(B4) are derived independently.

## 4. Why Bohr orthogonality cannot extract (B1) from the window current

The mean-zero prime seams for distinct primes have disjoint Bohr spectra:

\[
 {2\pi\over\log p}\mathbb Z\cap
 {2\pi\over\log q}\mathbb Z=\{0\}\qquad(p\ne q).   \tag{4.1}
\]

It is therefore tempting to combine the strong first-contact identity

\[
 \mathcal L_{T,-}(F)=-\mathcal Z_{T,+}r_\varepsilon
 \quad\hbox{in }L^2(-T,T)                           \tag{4.2}
\]

with Bohr orthogonality and conclude that every mean-zero seam vanishes.
This inference is not defined.  The seams live in the Besicovitch quotient
`B_ap^2(R)`, whereas (4.2) is an equality of restrictions to one bounded
interval.  A compactly supported modification has Besicovitch seminorm
zero, so there is no restriction map

\[
                         B_{ap}^2(\mathbb R)
                         \longrightarrow L^2(-T,T) \tag{4.3}
\]

compatible with representatives.  Conversely, an `L2` identity on one
window determines no Bohr Fourier coefficient.

Even in the smaller class of continuous periodic functions, vanishing on
an interval does not imply global vanishing without an additional
quasianalytic law.  The actual seam has only the sub-half-Sobolev
regularity inherited from the radical, not such a law.

Thus Bohr orthogonality would become decisive only after proving a
**global seam identity** whose mean-zero part equals zero in `B_ap^2`.
Constructing that global identity from (4.2) is exactly the missing
local-to-annular transport.  The strong graph current fixes the local
representative but does not globalize it.

## 5. Verdict

The cross-scale idea does not create a free induction.  It repackages the
terminal obstruction with unusually sharp bookkeeping:

* (B1) is the complete mean-zero Frobenius seam, not one scalar moment;
* (B2)--(B3) are the moving Tate jet and its resonant multiplier;
* (B4) is equality-state annular transport.

The full-line Blaschke/inner normalization of `E_p^+` removes the norm
defect but has an infinite one-sided tail and therefore leaves the
compact-window category.  Truncating it restores compact support and
reintroduces (B1) and (B4).  This agrees with the phase-64 colligation and
the phase-101 shifted-source obstruction, while the exact package (3.3)
was not found stated in phases 1--120.

Euler backshift is therefore rejected as an automatic radical transport.
No paper-42 change follows.
