# P121 -- oriented `K_2` localization between rows (b) and (c)

## Status

This note constructs the missing **pre-supertrace localization layer** between
the place-resolved contacts of row (b) and the scalar nuclear character of
row (c).  The construction is independent of the Weil sign and uses no zero
of `xi`.

There are two exact statements.

1.  At every finite Euler divisor, the two causal tame symbols split
    canonically into their scalar supertrace and their oriented residue.
    These two coordinates are jointly faithful.
2.  On the cofinal family of first prime harmonics, the oriented residue is
    not merely a sequence: it is the complete analytic germ of the compact
    transform at the Tate point.  Its Taylor-jet map is injective.

Thus the information lost in row (c) is now an explicitly constructed
object, denoted `c^(1)`.  For the frozen-source Euler class it is exactly the
germ of `K_F` at `-1/2`.  Vanishing of `c^(1)` closes first contact and the
global square.

What is **not** proved here is that the first-contact equation makes
`c^(1)` vanish.  Exactness identifies that assertion as the sole remaining
compatibility theorem; exactness alone cannot infer it from the vanishing of
the scalar supertrace.

## 1. Local relative symbols

Put

\[
 a=-\frac12,\qquad
 e_p(z)=1-p^{-1/2-z},\qquad
 u_h(z)=1+\epsilon h(z),\qquad \epsilon^2=0,
\tag{1.1}
\]

where `h` is holomorphic near the points under consideration.  The Euler
zeroes are

\[
 \lambda_{p,k}=a+\frac{2\pi i k}{\log p},\qquad k\in\mathbb Z.
\tag{1.2}
\]

For the two normal orientations define

\[
 \kappa_{p,h}^{+}=\{e_p,u_h\},\qquad
 \kappa_{p,h}^{-}=\{e_p,u_h^{-1}\}
                 =\{e_p,1-\epsilon h\}.
\tag{1.3}
\]

They belong to relative Milnor `K_2` of the dual-number meromorphic ring.
At a simple zero `lambda_(p,k)`, the tame-symbol formula gives

\[
 \partial_{p,k}\kappa_{p,h}^{+}=1-\epsilon h(\lambda_{p,k}),
 \qquad
 \partial_{p,k}\kappa_{p,h}^{-}=1+\epsilon h(\lambda_{p,k}).
\tag{1.4}
\]

Use the infinitesimal logarithm

\[
 \ell(1+\epsilon c)=c.
\tag{1.5}
\]

With the physical ordering `(+,minus)` of (1.3), the oriented logarithmic
tame vector is therefore

\[
 r_{p,k}(h):=
 \left(\ell\partial_{p,k}\kappa_{p,h}^{+},
       \ell\partial_{p,k}\kappa_{p,h}^{-}\right)
 =\bigl(-h(\lambda_{p,k}),h(\lambda_{p,k})\bigr).
\tag{1.6}
\]

This is the `K_2` realization of the two frozen causal jets constructed
earlier in phase 121.

### Proposition 1.1 -- finite relative `K_2` localization

Let `K_(p,k)` be the completed meromorphic local field at
`lambda_(p,k)`, let `O_(p,k)` be its valuation ring, and extend both by
dual numbers.  Denote by

\[
 K_{2,p,k}^{\rm Eul}
 :=K_2^M(O_{p,k}[\epsilon],(\epsilon))
   +\left\langle\{e_p,1+\epsilon c\}:c\in\mathbb C\right\rangle
 \subset K_2^M(K_{p,k}[\epsilon],(\epsilon))
\tag{1.7}
\]

the relative subgroup with at most one Euler-normal ramification.  Then

\[
 0\longrightarrow K_2^M(O_{p,k}[\epsilon],(\epsilon))
 \longrightarrow K_{2,p,k}^{\rm Eul}
 \xrightarrow{\ \ell\partial_{p,k}\ }\mathbb C
 \longrightarrow0
\tag{1.8}
\]

is split exact.  Relative to the row-(b) Euler equation `e_p=0`, a section
is

\[
 \sigma_{p,k}(c)=\{e_p,1-\epsilon c\}.
\tag{1.9}
\]

#### Proof

The tame symbol is trivial on relative symbols of two units, hence on the
left term.  Formula (1.4) gives

\[
 \ell\partial_{p,k}\sigma_{p,k}(c)=c,
\]

so the last map is surjective and split.  Every generator in (1.7) differs
from the corresponding section of its tame coordinate by an unramified
relative symbol.  Therefore its kernel is exactly the left term.  QED.

Taking finite direct sums of (1.8), and then taking the two normal copies,
gives the finite place-resolved `K_2` localization sequence

\[
 0\to\mathcal K_{2,D}^{\rm nr,\leftrightarrow}
 \to\mathcal K_{2,D}^{\rm Eul,\leftrightarrow}
 \xrightarrow{\ell\partial_D^{\leftrightarrow}}
 \mathcal R_D^{\leftrightarrow}\to0.
\tag{1.10}
\]

Unlike an abstract choice of a uniformizer, its splitting is fixed here by
the actual row-(b) factor `e_p`.

## 2. The oriented localization sequence

For a finite set `D` of labelled Euler zeroes, put

\[
 \mathcal R_D^{\leftrightarrow}
   =\bigoplus_{(p,k)\in D}(\mathbb C\oplus\mathbb C),\qquad
 \mathcal R_D=\bigoplus_{(p,k)\in D}\mathbb C.
\tag{2.1}
\]

Define at every label

\[
 \operatorname{str}(x_+,x_-)=x_++x_-,\qquad
 \operatorname{or}(x_+,x_-)=\frac{x_--x_+}{2}.
\tag{2.2}
\]

The first map is the scalar Real supertrace used by row (c).  The second
retains the normal orientation before that supertrace.

### Theorem 2.1 -- split oriented exactness

There is a canonically split exact sequence

\[
 0\longrightarrow \mathcal R_D
 \xrightarrow{\ \iota_{\rm an}\ }
 \mathcal R_D^{\leftrightarrow}
 \xrightarrow{\ \operatorname{str}\ }
 \mathcal R_D\longrightarrow0,
\tag{2.3}
\]

where

\[
 \iota_{\rm an}(y)=(-y,y),\qquad
 s(x)=(x/2,x/2),\qquad
 \operatorname{or}\circ\iota_{\rm an}=\operatorname{id}.
\tag{2.4}
\]

Equivalently, the map

\[
 (\operatorname{str},\operatorname{or}):
 \mathcal R_D^{\leftrightarrow}\longrightarrow
 \mathcal R_D\oplus\mathcal R_D
\tag{2.5}
\]

is an isomorphism, with inverse

\[
 (c,o)\longmapsto(c/2-o,c/2+o).
\tag{2.6}
\]

#### Proof

All assertions are componentwise.  The kernel of `str` consists exactly of
pairs `(-y,y)`.  Equations (2.4)--(2.6) follow by direct substitution.  QED.

### Corollary 2.2 -- the missing first character

For the relative Euler pair (1.3),

\[
 \operatorname{str}r_{p,k}(h)=0,\qquad
 \operatorname{or}r_{p,k}(h)=h(\lambda_{p,k}).
\tag{2.7}
\]

Thus row (c) vanishes on this normal class for every source, while the
oriented character recovers it exactly.  Define

\[
 \boxed{\quad c^{(1)}_{p,k}(h):=\operatorname{or}r_{p,k}(h)
 =h(\lambda_{p,k}).\quad}
\tag{2.8}
\]

This definition is prior to the spectral expression of row (c), is
place-resolved, and uses only the row-(b) Euler factor and its two Real
orientations.

## 3. Compatibility with the row-(b) contact coefficient

The tangent regulator of the positive symbol is

\[
 \operatorname{bl}(\kappa_{p,h}^{+})
 =h(z)\frac{de_p}{e_p}
 =h(z)\sum_{j\ge1}\frac{\log p}{p^{j/2}}
       e^{-jz\log p}\,dz
\tag{3.1}
\]

on `Re z>1/2`.  Hence the coefficient and displacement are exactly

\[
 \frac{\Lambda(p^j)}{\sqrt{p^j}},\qquad j\log p,
\tag{3.2}
\]

the self-dual determinant contact of row (b).  Reversing `epsilon` gives
the other causal orientation.  Applying `str` gives the scalar cancellation
seen after the Real supertrace; applying `or` gives (2.8).  Therefore
(2.3) is not an abstract duplicate of row (c): it is a split localization
of the exact row-(b) Euler contact before row (c) forgets its normal framing.

## 4. Why the cofinal divisor needs a new topology

For fixed `p`, the divisor (1.2) is discrete.  Across all primes, however,

\[
 \lambda_{p,1}=a+q_p,\qquad
 q_p:=\frac{2\pi i}{\log p}\longrightarrow0.
\tag{4.1}
\]

Thus the union of Euler divisors is not locally finite at the Tate point
`a`.  The ordinary direct-sum Gersten boundary is consequently the wrong
cofinal recipient.  It either discards the accumulating first harmonics or
forces an illegitimate unweighted Hilbert sum.

The correct recipient retains their analytic germ.  Let `O_0` be the ring
of holomorphic germs at `q=0`, and define

\[
 \mathcal A_\omega:=
 \left\{(b_p)_{p\gg1}:\text{ there is }g\in\mathcal O_0
 \text{ with }b_p=g(q_p)\right\}/\text{finite tails}.
\tag{4.2}
\]

The evaluation map is

\[
 \operatorname{ev}_\omega:\mathcal O_0\longrightarrow\mathcal A_\omega,
 \qquad g\longmapsto(g(q_p))_p.
\tag{4.3}
\]

### Theorem 4.1 -- cofinal analytic exactness

The map `ev_omega` is an isomorphism.  Its inverse is given intrinsically
by the recursive cofinal divided differences

\[
 \begin{aligned}
 a_0&=\lim_{p\to\infty}b_p,\\
 a_m&=\lim_{p\to\infty}q_p^{-m}
 \left(b_p-\sum_{r<m}a_rq_p^r\right),\qquad m\ge1,
 \end{aligned}
\tag{4.4}
\]

and reconstructs the germ `g(q)=sum_(m>=0) a_m q^m`.

#### Proof

Surjectivity is the definition of `A_omega`.  If two germs have the same
cofinal samples, their difference has zeroes at the distinct points `q_p`
accumulating at zero; the identity theorem makes the germs equal.  This
proves injectivity.  Taylor's formula gives (4.4) successively, and the
resulting coefficients are those of the unique germ.  QED.

The theorem can be displayed as the exact cofinal localization row

\[
 0\longrightarrow\mathcal O_0
 \xrightarrow{\operatorname{ev}_\omega}
 \mathcal A_\omega\longrightarrow0,
\tag{4.5}
\]

where the nontrivial content is faithfulness at the non-locally-finite
Euler accumulation point.

## 5. The oriented `K_2` boundary at the Tate point

For a primitive compact source put `h(q)=K_F(a+q)`.  The Tate condition is
`h(0)=0`.  Equations (1.6), (2.8), and (4.3) define the cofinal oriented
boundary

\[
 \boxed{
 \partial_\omega^{\rm or}(\widetilde\kappa_F)
 :=\operatorname{ev}_\omega(h)
 =\left(K_F\left(-\frac12+\frac{2\pi i}{\log p}\right)\right)_{p\gg1}
 \in\mathcal A_\omega.}
\tag{5.1}
\]

Its scalar companion is identically zero:

\[
 \partial_\omega^{\rm str}(\widetilde\kappa_F)=0.
\tag{5.2}
\]

### Theorem 5.1 -- faithfulness of the oriented boundary

For compactly supported `F` satisfying the resonant Tate condition, the
following are equivalent:

\[
 \begin{aligned}
 &(i)\quad \partial_\omega^{\rm or}(\widetilde\kappa_F)=0,\\
 &(ii)\quad K_F\text{ has zero Taylor germ at }-1/2,\\
 &(iii)\quad K_F\equiv0,\\
 &(iv)\quad F=0.
 \end{aligned}
\tag{5.3}
\]

It is enough in (i) that the cofinal samples be flat to every order:

\[
 K_F(a+q_p)=O_N(|q_p|^N)\quad\text{for every }N.
\tag{5.4}
\]

#### Proof

Theorem 4.1 proves `(i)<=>(ii)`.  An entire function with zero germ is zero,
so `(ii)=>(iii)`; the converse is immediate.  Fourier--Laplace injectivity
proves `(iii)<=>(iv)`.  If (5.4) held for a nonzero germ, its first nonzero
Taylor coefficient would contradict (5.4) with a larger `N`.  QED.

This theorem is the exactness needed after an oriented boundary vanishing
law: there is no further cofinal or Cartwright step hidden behind it.

### Corollary 5.2 -- the oriented boundary is the full Tate-moment tower

Writing the germ in (5.1) as

\[
 K_F(a+q)=\sum_{m\ge0}\mu_m(F)q^m,
\tag{5.5}
\]

one has the source formula

\[
 \boxed{
 \mu_m(F)=\frac{K_F^{(m)}(a)}{m!}
 =\frac{(-1)^m}{m!}\int_{-T}^{T}t^m e^{t/2}F(t)\,dt.}
\tag{5.6}
\]

Consequently the ordinary Tate condition is only `mu_0(F)=0`, whereas
oriented cofinal descent is the simultaneous law

\[
 \mu_m(F)=0\qquad(m=0,1,2,\ldots).
\tag{5.7}
\]

#### Proof

Differentiate the compactly supported Laplace integral under the integral
sign and evaluate at `a=-1/2`.  The factorial normalization is Taylor's
formula.  QED.

This identifies exactly what a lift of first contact has to do: it must
promote the two zeroth Tate moments to the complete oriented moment tower,
using the Euler localization rather than an a priori moment estimate.

### Theorem 5.3 -- tame/seam comparison

Let `T_pF` be the stabilized periodic prime seam of phase 120, normalized
on the circle of length `log p`.  Its Fourier coefficients are

\[
 \widehat{T_pF}(k)
 =\frac{\sqrt{1-p^{-1}}}{\log p}\,
 G_F\left(\frac{2\pi k}{\log p}\right),
 \qquad
 G_F(\omega)=\int e^{t/2}F(t)e^{-i\omega t}\,dt.
\tag{5.8}
\]

Then the first oriented tame coordinate and the first physical seam
coordinate agree exactly:

\[
 \boxed{
 c^{(1)}_{p,1}(F)
 =K_F\left(-\frac12+\frac{2\pi i}{\log p}\right)
 =\frac{\log p}{\sqrt{1-p^{-1}}}\widehat{T_pF}(1).}
\tag{5.9}
\]

Consequently the diagram

\[
 \begin{array}{ccc}
 \widetilde\kappa_{p,F}&\xrightarrow{\ \ell\partial^{\rm or}_{p,1}\ }&
 \mathbb C\\[2mm]
 \downarrow\operatorname{bl}&&\Vert\\[2mm]
 T_pF&\xrightarrow{\ {\log p\over\sqrt{1-p^{-1}}}\widehat{(\cdot)}(1)\ }&
 \mathbb C
 \end{array}
\tag{5.10}
\]

commutes.

#### Proof

At `omega=2 pi/log p`, the definition of `G_F` gives

\[
 G_F(2\pi/\log p)
 =K_F(-1/2+2\pi i/\log p).
\]

Substitution in (5.8) proves (5.9).  The upper arrow is (2.8), so the same
identity proves commutativity of (5.10).  QED.

This comparison is important logically: cofinal `K_2` descent is not a new
surrogate for annular transport.  It is the multiplicative localization of
the already constructed physical exterior seam, before its prime labels and
orientation are erased.

## 6. The precise `(b -> c)` diagram

At finite level and at the cofinal Tate point the construction is summarized
by

```text
row-(b) relative Euler K_2 symbols, with +/- normal framing
                  |
                  | logarithmic tame localization
                  v
        R^<->  --(str,or)-->  R  +  R
                    |            |
                    |            +--> c^(1): complete Tate germ of K_F
                    +---------------> row-(c): scalar nuclear character
```

The horizontal arrow is an isomorphism by Theorem 2.1.  Row (c) is the
first coordinate.  The second coordinate is the minimal missing refinement;
it is not chosen by matching the Weil form.

For the frozen source, the class lies in the antidiagonal kernel of `str`:

\[
 r_F=(-K_F,+K_F),\qquad
 \operatorname{str}(r_F)=0,\qquad c^{(1)}(r_F)=K_F.
\tag{6.1}
\]

Therefore

\[
 \boxed{
 \operatorname{str}(r_F)=0\ \text{and}\ c^{(1)}(r_F)=0
 \quad\Longleftrightarrow\quad F=0.}
\tag{6.2}
\]

## 7. What remains for first contact

The new layer reduces the source theorem to one sharply typed assertion:

\[
 \boxed{
 F\in\mathcal P_T,\quad P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \partial_\omega^{\rm or}(\widetilde\kappa_F)=0.}
\tag{7.1}
\]

By Theorem 5.1, (7.1) immediately gives `F=0`; the proved nesting and
cofinal arguments then give the global square and row (d).

Equation (7.1) is **not** a consequence of (5.2): Theorem 2.1 proves that
the scalar and oriented coordinates are independent.  A proof of (7.1)
must therefore lift the first-contact equation to the pre-supertrace
localization diagram.  This is now a compatibility problem between two
already constructed maps, not a request for another positive operator,
inequality, norm, or factorization.

Using Theorem 5.3, the same remaining assertion has the entirely physical
form

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \widehat{T_pF}(1)=O_N((\log p)^{-N})
 \quad\text{for every }N.
\tag{7.2}
\]

Thus either exact vanishing on infinitely many primes or cofinal flatness
to all orders closes the oriented `K_2` boundary.  No summability of the
all-prime seam is required.

## 8. Exact range form of oriented descent

Let

\[
 \Delta_T=P_T\mathscr A_TP_T
\tag{8.1}
\]

on the primitive Hilbert space, and define the projected Tate jets

\[
 v_m=P_T\left(\frac{(-t)^m}{m!}e^{t/2}\right),
 \qquad m\ge0.
\tag{8.2}
\]

For a primitive source,

\[
 \mu_m(F)=\langle F,v_m\rangle.
\tag{8.3}
\]

Notice that `v_0=0`; the first new coordinate is `v_1`.

### Theorem 8.1 -- range/descent equivalence at first contact

Assume `Delta_T` is self-adjoint and nonnegative and let
`N_T=ker Delta_T` be its first-contact space.  For every `m`, the following
are equivalent:

\[
 \begin{aligned}
 &(a)\quad \mu_m(F)=0\quad(F\in N_T),\\
 &(b)\quad v_m\perp N_T,\\
 &(c)\quad v_m\in\overline{\operatorname{Ran}\Delta_T}.
 \end{aligned}
\tag{8.4}
\]

If zero is an isolated eigenvalue of `Delta_T`, the closure in `(c)` may be
removed.  Consequently complete oriented `K_2` descent is equivalent to

\[
 \boxed{
 v_m\in\overline{\operatorname{Ran}\Delta_T}
 \qquad(m=0,1,2,\ldots).}
\tag{8.5}
\]

#### Proof

Equation (8.3) gives `(a)<=>(b)`.  For every densely defined self-adjoint
operator,

\[
 (\operatorname{Ran}\Delta_T)^\perp=\ker\Delta_T,
\]

so taking orthogonal complements proves `(b)<=>(c)`.  If zero is isolated,
the spectral theorem makes the range on `N_T^perp` closed.  QED.

### Corollary 8.2 -- analytic range certificate

Put

\[
 v(q)=P_T(e^{-(a+q)t})
     =\sum_{m\ge1}q^m v_m,qquad a=-1/2.
\tag{8.6}
\]

An analytic family `g(q)` satisfying

\[
 \Delta_Tg(q)=v(q)                                  \tag{8.7}
\]

near `q=0`, constructed without an inverse on the first-contact space,
implies (8.5) coefficient by coefficient and therefore closes the oriented
boundary.  Conversely, the first obstruction to solving (8.7) is exactly

\[
 \langle F,v_1\rangle=\mu_1(F),\qquad F\in N_T,    \tag{8.8}
\]

and the successive obstructions are the higher tame/Tate coordinates
`mu_m(F)`.

Thus (8.7) is the concrete form of the required source-defined oriented
range certificate.  Defining `g(q)` by a pseudoinverse would be circular;
an admissible construction must come from the row-(b) Euler connection and
the row-(c) Poisson extension.

## 9. Ledger

```text
local relative K_2 symbols with two orientations          PROVED
exact split into scalar trace and oriented residue         PROVED
compatibility with row-(b) weights and displacements       PROVED
cofinal analytic recipient at the Tate accumulation        CONSTRUCTED
cofinal evaluation/jet exactness                           PROVED
oriented boundary vanishing <=> F=0                        PROVED
first contact -> oriented boundary vanishing               OPEN (7.1)
global square and row (d)                                  OPEN
```

No modification of paper 42 follows until (7.1) is proved.
