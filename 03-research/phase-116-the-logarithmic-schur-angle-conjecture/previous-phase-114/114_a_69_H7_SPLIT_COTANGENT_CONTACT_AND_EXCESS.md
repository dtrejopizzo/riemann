# 114.a.69 — H7: the diagonal splits the cotangent contact from the excess

```
+-------------------------------------------------------------------------+
| RETRACTION   Delta^# o p_1^# = id before and after quotient by p.       |
| COTANGENT    Functoriality turns this into a split comparison.          |
| CONTACT      F_p[1] is a canonical retract of the pulled global complex.|
| EXCESS       The complementary fiber E_p measures all failure of LCI.   |
| LCI GATE     H7-LCI-DELTA is exactly E_p = 0.                           |
| GAIN         Lambda contact extraction does not require E_p to vanish.  |
+-------------------------------------------------------------------------+
```

## 1. A split square of quotient arrows

Write locally

\[
 A_X=\mathcal O_X,\quad B_X=A_X/E((p)),\qquad
 A_Y=\mathcal O_Y,\quad B_Y=A_Y/E((p)).                                \tag{1.1}
\]

The first projection and diagonal induce maps of quotient arrows

\[
 i:(A_X\to B_X)\longrightarrow(A_Y\to B_Y),\qquad
 r:(A_Y\to B_Y)\longrightarrow(A_X\to B_X),                           \tag{1.2}
\]

and `r o i=id`, because `p_1 o Delta=id_X` and both maps preserve the
distinguished scalar `p` and its equivalence ideal.

## 2. Cotangent functoriality preserves the retraction

Put

\[
 L_X=\mathbb L\Omega(B_X/A_X),\qquad
 L_Y=\mathbb L\Omega(B_Y/A_Y).                                        \tag{2.1}
\]

Functoriality and derived extension of scalars applied to `i` and `r` give

\[
 s:L_X\longrightarrow
 C_p:=L_Y\otimes^{\mathbf L}_{B_Y}B_X,qquad
 \rho:C_p\longrightarrow L_X.                                        \tag{2.2}
\]

The composite is

\[
 \rho\circ s=\mathrm{id}_{L_X}.                                 \tag{2.3}
\]

Indeed, the composite morphism of quotient arrows is the identity, and the
unit/associativity isomorphisms for derived scalar extension identify the
composite cotangent map with the identity.  No flatness and no
H7-PRIME-REG are used here.

### Theorem 2.1 (split cotangent contact)

There is a split distinguished triangle

\[
 E_p\longrightarrow C_p
 \mathop{\longrightarrow}^{\rho}L_X
 \longrightarrow E_p[1],                                             \tag{2.4}
\]

where `E_p=hofib(rho)`.  Hence

\[
 C_p\simeq L_X\oplus E_p.                                             \tag{2.5}
\]

### Proof

Equation (2.3) is a section of `rho`.  In every triangulated category, the
fiber triangle of a split epimorphism splits, giving (2.5).  QED.

## 3. The canonical finite contact

By the ordinary computation of `a_68`,

\[
 L_X|_{x_p}\simeq\mathbb L_{\mathbb F_p/\mathbb Z}
 \simeq\mathbb F_p[1].                                                 \tag{3.1}
\]

Therefore

\[
 H_1(C_p)\simeq\mathbb F_p\oplus H_1(E_p),                             \tag{3.2}
\]

with canonical split projection `H_1(rho)` onto `F_p`.  Define the reduced
diagonal contact to be this distinguished retract, equivalently the pair

\[
 \mathbb F_p[1]
 \mathop{\longrightarrow}^{s}C_p
 \mathop{\longrightarrow}^{\rho}\mathbb F_p[1].                      \tag{3.3}
\]

This construction is canonical from `p_1` and `Delta`; it is not an
arbitrary deletion of an unknown summand.

For prime powers the distinguished generators multiply as in `a_67`; for
distinct primes the reduced contacts tensor to zero.  Consequently the
reduced contact system has

\[
 \log\#\Gamma(\mathcal C_n^{red})=\Lambda(n)                           \tag{3.4}
\]

without requiring the excess complexes to vanish.

## 4. Exact meaning of H7-LCI-DELTA

The comparison `rho` is a quasi-isomorphism if and only if

\[
 E_p\simeq0.                                                          \tag{4.1}
\]

Thus H7-LCI-DELTA is no longer needed to **find** the finite contact.  It is
exactly the no-excess theorem asserting that the pulled global conormal has
nothing beyond that contact.

This distinction mirrors the earlier Witt analysis: the desired local term
can be a canonical retract even when the unreduced fixed/intersection object
has horizontal excess.

## 5. Remaining compatibility gate

At the time of this construction, promotion of (3.3) required:

> **H7-EXCESS-MULT.** The split projectors for all prime powers are compatible
> with the proposed correspondence convolution and with pro-level
> restrictions, so that the reduced contacts form the monoidal system of
> `a_45`--`a_46` geometrically.

The arithmetic multiplication of the retracts is the exact ordinary
calculation of `a_67`.  The subsequent construction `a_70` supplies a
Picard-decorated diagonal-span category and defines the reduced contact as a
monoidal shadow on its arithmetic kernel submonoid.  Thus H7-EXCESS-MULT is
closed for that stated decorated subcategory.  Compatibility for arbitrary
decorated spans, or for a stronger undecorated Chow correspondence category,
is not asserted.

## 6. Verification scope

`114_a_69_h7_split_cotangent_verify.py` checks the source/functorial anchors,
split-chain-complex algebra, homology decomposition and the exact
`Lambda(n)` reduced-contact law.  It does not assert `E_p=0` or construct
dynamic convolution.

Primary sources: [Haran, arXiv:1709.05831](https://arxiv.org/abs/1709.05831),
[Haran, arXiv:1508.04636](https://arxiv.org/abs/1508.04636).
