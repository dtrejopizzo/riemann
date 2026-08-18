# 114.a.57 — H7 no-go: persistent finite characteristics cannot cover the global cone

```
+--------------------------------------------------------------------------+
| LOCAL       A moment block in characteristic p evaluates denominators   |
|             only when they are prime to p.                              |
| GLOBAL      The effective cone eventually contains the denominator p.   |
| CONFLICT    A unital map would require 0*epsilon(1/p)=1 in F_p.         |
| RETENTION   a_52 retains every old p-coordinate at every later level.   |
| NO-GO       Its W_j is therefore not defined on all later section sets.  |
| SURVIVES    Fixed rays whose denominator support avoids all chosen p_i.  |
| RESULT      H7-FMD-GLOB and the global h_FM of a_53 are retracted.       |
+--------------------------------------------------------------------------+
```

## 1. The elementary localization obstruction

### Lemma 1.1

There is no unital ring map

\[
 \mathbb Z[1/p]\longrightarrow R                                       \tag{1.1}
\]

to a nonzero ring `R` of characteristic `p`.

### Proof

The image of `p` is zero, while the relation `p(1/p)=1` would give `0=1`.
QED.

More generally, if a prime `p` divides the characteristic of a finite
nonzero ring, `p*1` cannot be a unit. Otherwise multiplication of its inverse
by the relation `char(R)*1=0` contradicts minimality of the characteristic.

The finite twisted-bio evaluation `epsilon_(p,s)` of `a_51` restricts on the
selected scalar ring to reduction modulo `p`. Therefore it evaluates a
rational label `a/Q` only if

\[
 p\nmid Q.                                                               \tag{1.2}
\]

This condition was enforced inside every individual block.

## 2. Failure of the accumulated global target

At height `T_i`, `a_52` chooses a prime `p_i>H_(T_i)` and then defines

\[
 \mathcal W_j=\prod_{i=0}^j\mathbb F_{p_i}^{2R_{T_i}}.                  \tag{2.1}
\]

It claims that (2.1) evaluates every effective pair of norm at most
`H_(T_j)`. Fix the first coordinate prime `p_i`. Since `H_(T_j)->infinity`,
there is a later `j` with

\[
 p_i\le H_{T_j}.                                                        \tag{2.2}
\]

The global cone at that level includes the effective divisor `L_(p_i)` and
the rational scalar label `1/p_i`. But the retained `F_(p_i)` coordinate of
(2.1) would have to extend (1.1), which is impossible.

### Theorem 2.1 (global denominator no-go)

The maps claimed in `a_52` (3.1)--(3.2) are not simultaneously defined on
the complete bounded scalar section sets for all effective finite divisors.
Consequently:

1. H7-FMD-GLOB is **not** closed by `a_52`;
2. retaining earlier finite-field coordinates does not give a global
   presentation-independent quotient;
3. the global `h_FM^Pic` of `a_53`, which uses those accumulated targets,
   is not defined as stated.

### Proof

Choose `i` and then `j` satisfying (2.2). The scalar `1/p_i` is a local
section after twisting by `L_(p_i)`. Projection of the alleged `W_j`
evaluation to its retained `F_(p_i)` factor would be a unital extension of
reduction modulo `p_i` to `Z[1/p_i]`, contradicting Lemma 1.1. QED.

## 3. The obstruction is not specific to fields

Suppose finite quotient rings `R_j` are connected by surjective transition
maps and every old quotient remains visible at later levels. Let `n_i>1` be
the characteristic of a nonzero retained quotient. Some prime `p` divides
`n_i`; once denominator `p` is allowed, its image would have to be a unit in
that quotient, impossible by Lemma 1.1.

For cyclic moduli this says: there is no nontrivial sequence

\[
 M_i\mid M_{i+1},\qquad
 \gcd(M_i,Q)=1\quad\text{for every }Q\le H_i,\qquad H_i\to\infty.        \tag{3.1}
\]

Indeed any prime factor of `M_i` persists in every later modulus and
eventually occurs among the allowed denominators.

Thus replacing fields by nested composite moduli does not repair the global
cone. A characteristic-zero finite ring also cannot help: every nonzero
finite unital ring has positive characteristic.

## 4. What survives and the exact replacement gate

The fixed-ray theorem `a_51` survives. If the ray has finite denominator
support in a fixed integer `Q_0`, choose every controlled prime away from
the prime factors of `Q_0`. Then every denominator `Q_0^t` remains invertible
in every retained block.

The per-degree block construction also survives: for a bounded finite set of
denominators, choose a fresh prime larger than all of them. What fails is
simultaneous persistence over the **whole** effective cone.

The corrected global gate is:

> **H7-DEN-TRANS.** Construct degree-transition data between fresh finite
> targets without retaining a positive-characteristic quotient past the
> point where its characteristic becomes an allowed denominator. Prove that
> the resulting dimension is presentation/principal invariant and compatible
> with tensor products and sheaf restrictions.

Ordinary quotient projections cannot satisfy H7-DEN-TRANS. A span,
correspondence, derived transition, or a non-finite characteristic-zero
object would be required. H7-SEL-MOM from `a_56` remains a valid per-block or
fixed-ray criterion, but it is not yet a global Picard construction.

`a_58` later rules out the ordinary unital span, cross-prime derived fiber
product and Witt inversion/reduction versions. The remaining words
"correspondence" and "characteristic-zero object" must therefore mean a
nonunital/additive or genuinely new adelic/determinant construction.

## 5. Consequences for later notes

- `a_53` still proves the continuous coefficient of the **balanced code**
  and its invariance under the residual `+/-1` transport.
- It no longer proves a globally defined principal-invariant `h_FM`.
- `a_55` remains a valid bounded saturation theorem for each individual
  block. Its no-go applies to any per-block complete-bounded moment image.
- The fixed-ray and per-block quotient classification of `a_56` remains
  valid; global cofinal exactness additionally requires H7-DEN-TRANS.

## 6. Verification scope

`114_a_57_h7_global_denominator_nogo_verify.py` constructs the first retained
prime of the strengthened `a_52` system, finds the later dyadic height at
which its own denominator is allowed, checks that modular inversion fails,
tests the general nested-modulus obstruction, and confirms why fixed-support
rays avoid the collision. The ring-theoretic contradiction is Lemma 1.1,
not a numerical heuristic.
