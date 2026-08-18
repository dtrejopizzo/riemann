# 114.a.68 — H7: cotangent conormal exists; diagonal LCI comparison is the gate

> **Refinement (`a_69`).** The comparison map has a canonical section because
> `Delta^# o p_1^#=id`, before and after quotient by `p`. Hence `F_p[1]` is
> already a canonical retract of the pulled complex. H7-LCI-DELTA is needed
> only to prove that the complementary excess complex vanishes, not to extract
> the finite contact or `Lambda(n)`.

```
+-------------------------------------------------------------------------+
| SOURCE      Haran defines A-mod, Kahler differentials and L Omega.      |
| GLOBAL      N^der_p := H_1(L Omega_{O_Vp/O_Y}) is correctly typed.      |
| ORDINARY    L_{F_p/Z} = F_p[1], so its H_1 is the contact F_p.          |
| MAP         Derived base change supplies a comparison along Delta.      |
| EXACT GATE  Prove that comparison is a quasi-isomorphism.               |
| NO CLAIM    PRIME-REG alone is not asserted to imply this LCI theorem.  |
+-------------------------------------------------------------------------+
```

## 1. The source-level derived object

Haran Section 6 makes `A-Mod` an abelian category.  Equations (6.6)--(6.7)
construct Kahler differentials and their transitivity sequence, and the text
immediately following (6.7) constructs the Quillen cotangent complex

\[
 \mathbb L\Omega(B/A)\in D(B\text{-Mod}).                              \tag{1.1}
\]

This is the correct place to seek a conormal **abelian module**.  It does not
identify the generalized-ring operation sets with modules.

The fuller primary treatment, arXiv:1508.04636, Section 7.8, globalizes this
construction for a map of generalized schemes as an object of the derived
category of sheaves of modules. Thus the following local formula glues in the
source's cotangent-bundle formalism.

Let `A=O_Y` locally and

\[
 B=\mathcal O_{V_p}=A/E((p))                                          \tag{1.2}
\]

using the principal quotient proved in `a_67`.  Define

\[
 \mathcal N^{der}_p:=H_1\!\left(\mathbb L\Omega(B/A)\right)
 \in B\text{-Mod}.                                                     \tag{1.3}
\]

Thus a global derived conormal object is now **constructed and typed**.  Its
local freeness, rank and relation to the completed lattice are not automatic.

## 2. The ordinary target on the diagonal

Base change of (1.2) along the diagonal has ordinary finite-prime chart

\[
 \mathbb Z\longrightarrow\mathbb F_p=\mathbb Z/(p).                   \tag{2.1}
\]

The standard one-element regular presentation gives

\[
 \mathbb L_{\mathbb F_p/\mathbb Z}simeq
 (p)/(p^2)[1]\simeq\mathbb F_p[1].                                   \tag{2.2}
\]

Consequently

\[
 H_1(\mathbb L_{\mathbb F_p/\mathbb Z})\simeq\mathbb F_p,
 \qquad H_i=0\ (i\ne1).                                               \tag{2.3}
\]

This is exactly the ordinary diagonal layer of `a_67`.

## 3. The canonical comparison and exact missing theorem

Functoriality of cotangent complexes gives a derived base-change comparison

\[
 \mathbf L\Delta^*\mathbb L\Omega(B/A)
 \longrightarrow
 \mathbb L_{\mathbb F_p/\mathbb Z}.                                   \tag{3.1}
\]

The desired global-to-contact statement is precisely:

> **H7-LCI-DELTA.** For every prime `p`, (3.1) is a quasi-isomorphism on the
> relevant pro-chart, compatibly with restriction maps and the distinguished
> generator `p`.

Under H7-LCI-DELTA, (2.2) gives the correctly derived statement

\[
 H_1\!\left(\mathbf L\Delta^*\mathbb L\Omega(B/A)\right)
 \simeq\mathbb F_p.                                                    \tag{3.2}
\]

and the graded multiplication/mixed-prime calculation of `a_67` recovers the
entire contact system `M_n` and `Lambda(n)` from the pulled global cotangent
complex. We do not interchange `H_1` with derived pullback; such an
interchange would require an additional degeneration or flatness theorem.

## 4. Why this is independent of the denominator proof

H7-PRIME-REG says that multiplication by `p` is injective on generalized
operation sets and makes `1/p` admissible in the Section-11 fraction sheaf.
H7-LCI-DELTA instead says that the quotient square is homotopically
Tor-independent along `Delta` in Haran's **module-derived** theory.

The first statement does not formally imply the second.  Proving the
implication would require a theorem that a regular unary scalar in a
commutative generalized ring defines a homotopy-regular quotient, or a direct
simplicial resolution of `A/E((p))`.  Neither is supplied in the source or
proved in phase 114.

Thus the former vague “global conormal theory” gap is replaced by one exact
map (3.1).

## 5. Status contribution

The Cartier/type chain is now:

1. `V_p=A/E((p))`: **closed** (`a_67`);
2. principal right act and completed `1/p` lattice: **conditional on
   H7-PRIME-REG**;
3. global derived conormal `N_p^der`: **constructed unconditionally** by
   (1.3);
4. its ordinary contact retract: **closed** by `a_69`;
5. absence of complementary derived excess: **conditional on
   H7-LCI-DELTA**;
6. dynamic correspondence convolution: still independent and open.

## 6. Verification scope

`114_a_68_h7_cotangent_lci_gate_verify.py` checks the source anchors, the
ordinary regular-quotient cotangent homology, the `F_p` layer and the exact
logical separation between PRIME-REG and LCI-DELTA.  It does not assert the
quasi-isomorphism (3.1).

Primary source: [Haran, arXiv:1709.05831](https://arxiv.org/abs/1709.05831).
