# Compressed Euler diamonds satisfy a cocycle law, not flatness

## 1. Question

Before scalar trace, prime correspondences commute:

\[
 \Gamma_p\Gamma_q=\Gamma_q\Gamma_p.
\]

Could this source-level diamond identity force the transverse prime seam or
the inactive mixed return to vanish after restriction to the physical
window?  The exact answer is no.  Compression turns the representation law
into a nonzero Toeplitz defect.  Associativity says that this defect is a
2-cocycle; it does not annihilate the cocycle.

## 2. Exact compression cocycle

Let `P=P_T` be the orthogonal projection onto `L^2(-T,T)` (with zero
extension understood), let `U_a` be translation by `a`, and put

\[
 T_a:=PU_aP.                                        \tag{2.1}
\]

Define the multiplicative compression defect

\[
 \Omega_T(a,b):=T_aT_b-T_{a+b}.                    \tag{2.2}
\]

### Proposition 2.1 -- boundary-defect formula

\[
 \boxed{
 \Omega_T(a,b)=-PU_a(I-P)U_bP.}                   \tag{2.3}
\]

#### Proof

Insert `P=I-(I-P)` between the two global translations:

\[
 PU_aPU_bP=PU_aU_bP-PU_a(I-P)U_bP.
\]

Since `U_aU_b=U_(a+b)`, this is (2.3).  QED.

### Proposition 2.2 -- exact associativity cocycle

For all real `a,b,c`,

\[
 \boxed{
 T_a\Omega_T(b,c)-\Omega_T(a+b,c)
 +\Omega_T(a,b+c)-\Omega_T(a,b)T_c=0.}             \tag{2.4}
\]

#### Proof

Expand every `Omega` using (2.2).  All terms cancel in pairs; equivalently,
(2.4) is the equality `(T_aT_b)T_c=T_a(T_bT_c)` written in defect
coordinates.  QED.

Thus global associativity produces a closed cocycle after compression, not
a zero cocycle.

## 3. Commuting diamonds

Global translations commute, but their compressions need not.  From (2.2),

\[
 [T_a,T_b]=\Omega_T(a,b)-\Omega_T(b,a).             \tag{3.1}
\]

Hence the compressed form of the global diamond identity is precisely

\[
 \Omega_T(a,b)-\Omega_T(b,a)=[T_a,T_b],            \tag{3.2}
\]

which is an identity for the boundary anomaly.  Neither side is forced to
vanish.  In particular, replacing decorated prime words by their commuting
global product before compression discards the two different exterior
histories appearing in (2.3).

## 4. Inactive opposite orientations are maximally nonflat

Suppose `a,b>2T`.  Then `T_a=T_{-b}=0`, while

\[
 \Omega_T(a,-b)=-T_{a-b}.                           \tag{4.1}
\]

For consecutive primes `p_n,p_(n+1)`, take

\[
 a_n=\log p_{n+1},\qquad b_n=\log p_n.
\]

Both are inactive for large `n`, and the prime number theorem gives
`a_n-b_n -> 0`.  Strong continuity of translations then yields

\[
 \boxed{
 \Omega_T(a_n,-b_n)\longrightarrow -I
 \quad\hbox{strongly on }L^2(-T,T).}               \tag{4.2}
\]

Therefore the global commuting Euler diamond becomes asymptotically the
**maximal** compression defect on precisely the consecutive-prime sequence
used by inactive-pair rigidity.  Flatness before compression cannot be
invoked to set that defect to zero.

## 5. Consequence for the source search

Any proposed argument of the form

```text
prime correspondences commute globally
 -> their compressed diamond has zero holonomy
 -> one seam or mixed return vanishes
```

is false at the middle arrow.  What survives from the global product law is
the cocycle equation (2.4), already satisfied by every source.  To kill a
first-contact state one would need an additional **trivialization** of this
cocycle on that state.  Declaring such a trivialization is exactly the
missing boundary-current law; it is not furnished by unique factorization,
commutativity or associativity.

This also explains why a free/noncommutative lift does not help by itself.
It may remember the two paths separately, but descent to the physical
window still produces the nonzero coboundary term (2.3).  An admissible
source theorem must control that boundary term rather than rename the
global diamond.

## 6. Corpus audit

The phase-121 option matrix rejected prime-diamond holonomy on typing
grounds, and the inactive-pair theorem computed one mixed return.  The
explicit cocycle (2.3)--(2.4), its commutator form (3.1), and the strong
limit (4.2) were not found in phases 1--120.  They give the exact algebraic
reason the prime-diamond source proposal cannot annihilate the physical
boundary defect.
