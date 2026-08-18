# 114.a.61 — I7: faithful unit-torsor algebra; completed/contact gates open

> **Type correction (`a_66`).** Replace the former `Pic_qc` claim by the
> unit-torsor category `Pic_tor`. Haran (11.7) supplies right-action sets,
> not Section-6 abelian modules. The normal-layer/derived-pullback calculation
> below is therefore a conditional specification, not a theorem in the cited
> categories.

```
+--------------------------------------------------------------------------+
| BUNDLE      G_n=p_1^*(tensor_p L_p^v_p(n)) on Haran's literal square.   |
| FAITHFUL    deg Delta^*G_n=log n, so G_m=G_n implies m=n.               |
| MONOIDAL    G_m tensor G_n = G_mn canonically.                          |
| CONTACT     If O(V_p)=p_1^*L_p and V_p is effective Cartier, the layer  |
|             I_p^(k-1)/I_p^k pulls back to the F_p contact at Delta.      |
| GLOBAL      Tensoring primitive layers gives M_n and Lambda(n).          |
| OPEN        Prove the Cartier comparison and promote tensor to dynamic  |
|             correspondence convolution.                                |
+--------------------------------------------------------------------------+
```

## 1. An unconditional faithful unit-torsor family

For `n>=1`, let

\[
 L_n:=\bigotimes_{p}L_p^{\otimes v_p(n)}\in\operatorname{Pic}(X),
 \qquad
 \mathcal T_n:=p_1^*T(L_n)
   \in\operatorname{Pic}_{tor}(Y),                                    \tag{1.1}
\]

where `L_p` is the inverse-uniformizer completed line bundle of `a_18` and
`Y=X times_S X` is Haran's literal square. Only finitely many factors occur.

### Theorem 1.1 (faithful abstract torsor lift)

There are canonical symmetric monoidal isomorphisms

\[
 \mathcal T_m\otimes\mathcal T_n\simeq\mathcal T_{mn},
 \qquad \mathcal T_1\simeq 1,                                         \tag{1.2}
\]

and the map

\[
 \mathbb N^\times\longrightarrow\operatorname{Pic}_{tor}(Y),
 \qquad n\longmapsto[\mathcal T_n]                                    \tag{1.3}
\]

is injective.

### Proof

Prime valuations add under multiplication, proving (1.2). If
`T_m\simeq T_n`, pull back by the diagonal. Since `Delta^*p_1^*=id`,

\[
 T(L_m)\simeq T(L_n).                                                   \tag{1.4}
\]

By `a_66`, triviality of the quotient torsor implies triviality of the
completed curve bundle `L_m tensor L_n^{-1}`. Its idelic degree is

\[
 \widehat\deg L_n=\sum_pv_p(n)\log p=\log n.                            \tag{1.5}
\]

Thus `log m=log n`, so `m=n`. QED.

This proves the **faithful abstract torsor label and commutative tensor law**
on the literal square. It does not give a completed lattice/gauge without
H7-PRIME-REG, or identify torsor product with composition of
endocorrespondences.

## 2. The exact Cartier-normal hypothesis

Let `V_p=x_p times_S X` be the left prime ruling of `a_17`. The missing
source-level comparison isolated in `a_18` is:

> **H7-CART-NORMAL.** Each `V_p` is an effective Cartier divisor on the
> relevant pro-site, with invertible ideal `I_p`, and
> \[
>  \mathcal O_Y(V_p)\simeq p_1^*L_p.                                    \tag{2.1}
> \]
> Its intersection with `Delta` is regular and its conormal generator is
> the ordinary prime uniformizer `p`.

This is stronger than the already proved closed incidence
`Delta times_Y V_p=Spec F_p`; generalized closed subschemes need not be
Cartier.

Assume a future typed H7-CART-NORMAL formalism for the rest of this section.
For `k>=1`, formally define the
primitive normal layer

\[
 \mathcal N_{p,k}:=I_p^{k-1}/I_p^k.                                    \tag{2.2}
\]

Since `I_p` is invertible, multiplication induces canonical isomorphisms

\[
 \mathcal N_{p,a}\otimes_{\mathcal O_{V_p}}\mathcal N_{p,b}
 \simeq \mathcal N_{p,a+b-1}.                                           \tag{2.3}
\]

Equivalently, with zero-based layers

\[
 \mathcal Q_{p,k}:=I_p^k/I_p^{k+1}\quad(k\ge0),
 \qquad
 \mathcal Q_{p,a}\otimes\mathcal Q_{p,b}\simeq\mathcal Q_{p,a+b}.       \tag{2.4}
\]

## 3. Conditional geometric recovery of the contact shadow

### Conditional specification 3.1 (not a theorem in the cited categories)

Under H7-CART-NORMAL,

\[
 L\Delta^*\mathcal Q_{p,k}\simeq(i_p)_*\underline{\mathbb F_p}
 =\mathcal M_p                                                         \tag{3.1}
\]

as an additive contact sheaf, for every `k>=1`; the uniformizer fixes the
trivialization. For

\[
 \mathcal C_n:=\bigotimes_{p^k\parallel n}^{\mathbb Z}
 L\Delta^*\mathcal Q_{p,k},                                             \tag{3.2}
\]

one obtains

\[
 \mathcal C_n\simeq\mathcal M_n,
 \qquad
 \log\#\Gamma(Y,\mathcal C_n)=\Lambda(n).                              \tag{3.3}
\]

### Formal calculation

Such a regular Cartier intersection would identify the pulled-back graded layer with
`p^k Z/p^(k+1)Z`, canonically one-dimensional over `F_p`. Multiplication by
the distinguished uniformizer `p` identifies it with the preceding primitive
layer `p^(k-1)Z/p^kZ` of `a_44`. For different primes the
supports `Z_p,Z_q` are disjoint and their tensor is zero. Equal-prime layers
multiply by (2.4). Therefore (3.2) is `M_p` for a prime power and zero for a
mixed-prime label, exactly as in `a_45`--`a_46`. QED.

`a_67` subsequently proves the **ordinary diagonal shadow** of this
calculation without assuming a global conormal module: it restricts the
principal filtration first and obtains the candid ordinary modules
`p^k Z_(p)/p^(k+1) Z_(p)`. Thus equations (3.2)--(3.3) are theorems for that
restricted shadow. The displayed global object `LDelta^*Q_{p,k}` remains
unconstructed.

`a_68` constructs the global cotangent conormal, and `a_69` proves that its
pulled complex contains the ordinary `F_p[1]` contact as a canonical retract.
Thus the finite contact is now tied to a global derived object without a
`Tor` identification; only the complementary excess and dynamic
compatibility remain open.

The family `T_n` remembers all exponents faithfully, whereas its proposed normal
contact (3.2) has exactly the required nonfaithful shadow. This explains the
loss in `a_47` geometrically rather than by external decoration.

## 4. What this does not yet construct

Even after H7-CART-NORMAL, (1.2) is product of unit torsors,
not convolution/composition of correspondences in `X times_S X`. The prime
rulings themselves fail span composition by `a_48`.

The remaining dynamic gate at this stage was:

> **H7-PIC-TO-DYNAMIC.** Promote the faithful effective-Cartier family
> underlying `T_n` to kernels `Gamma_n` whose convolution satisfies
> `Gamma_m compose Gamma_n=Gamma_mn`, and prove that the normal-contact
> construction (3.2) agrees with their derived diagonal intersection.

Thus `a_61`, corrected by `a_66`, gives a faithful **abstract unit-torsor**
lift unconditionally. Its completed realization requires H7-PRIME-REG; its
principal-act/ordinary-diagonal contact realization is supplied by `a_67`
conditional on PRIME-REG. `a_68`--`a_69` supply the global conormal/contact
retract, and `a_70` promotes the torsors to genuine Picard-decorated diagonal
spans with compositional kernels. A stronger undecorated Chow-cycle lift
remains open. Thus `a_61` alone did not claim I7 complete.

`a_62`, corrected by `a_66`, reduces only the **fraction-denominator** part
to H7-PRIME-REG. It does not reduce the entire Cartier/module comparison to
that condition.

## 5. Verification scope

`114_a_61_i7_faithful_picard_lift_verify.py` checks valuation-additive torsor
labels, degree faithfulness and the separate finite contact algebra. The
normal-layer calculation is not counted as a proved source-geometric claim.
