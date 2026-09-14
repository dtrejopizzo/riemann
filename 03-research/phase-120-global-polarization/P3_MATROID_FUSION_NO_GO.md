# Phase 120 — the matroid fusion no-go

## Status

This note resolves the proposed arithmetic Bergman/configuration carrier
negatively.  The obstruction is algebraic and occurs before Hodge--Riemann,
the Gamma place, numerical approximation or the cofinal limit.  Paper 42 is
not modified.

## 1. Required interface

At a fixed place (p), row (b) supplies a faithful tower

\[
 \Gamma_{p^i}\circ\Gamma_{p^j}\simeq\Gamma_{p^{i+j}},
 \qquad i,j\geq1,                                    \tag{1.1}
\]

and (Gamma_{p^i}\not\simeq\Gamma_{p^j}) for (i\ne j).  The proposed
configuration construction asked for a matroid (M) whose flats encode the
collision strata and whose join encodes fusion.  Thus it requires a map

\[
 \Phi_p:\mathbb N_{\ge1}\longrightarrow L(M)          \tag{1.2}
\]

such that

\[
 \Phi_p(i+j)=\Phi_p(i)\vee\Phi_p(j).                  \tag{1.3}
\]

Faithfulness of row (b) requires (Phi_p) to distinguish all iterate labels.

## 2. Idempotent-fusion theorem

**Theorem.**  There is no injective map (1.2) satisfying (1.3) into the
lattice of flats of any matroid.

**Proof.**  Join in every lattice is idempotent.  Hence, for every (i\ge1),

\[
 \Phi_p(2i)=\Phi_p(i+i)
 =\Phi_p(i)\vee\Phi_p(i)=\Phi_p(i).                   \tag{2.1}
\]

Thus (Phi_p) is not injective.  More generally induction gives
(Phi_p(ki)=\Phi_p(i)) for every (k\ge1).  This contradicts the faithful
Witt/nuclear/metric labels of row (b).  (square)

The proof uses only the type of the proposed interface: a cancellative
iteration law cannot embed into an idempotent join law.  It applies already
to the local pair (2,4) in (S=\{2,3,4\}).

## 3. Why the three apparent repairs do not repair it

### 3.1 Iterates as flats in a flag

One may choose nested flats

\[
 F_{p,1}\subsetneq F_{p,2}\subsetneq\cdots            \tag{3.1}
\]

and label (F_{p,j}) by (Gamma_{p^j}).  This preserves the labels, but
fusion is not join: (F_{p,i}\vee F_{p,j}=F_{p,\max(i,j)}), not
(F_{p,i+j}).  The composition law has become an external decoration.
Adiprasito--Huh--Katz controls the Chow product determined by the flat lattice;
it does not control an additional degree-lowering operation imposed on the
labels.  Therefore its Hodge--Riemann theorem supplies no sign for the row-(c)
pairing.

There is also a type mismatch.  Every boundary-flat generator (x_F) lies in
degree one, while multiplication sends

\[
 x_{F_{p,i}}x_{F_{p,j}}\in A^2(M),                   \tag{3.2}
\]

not to (x_{F_{p,i+j}}\in A^1(M)).  A new operation
(A^1\otimes A^1\to A^1) would be needed, and HR for the Chow multiplication
does not constrain it.

### 3.2 Iterates as configurations of atoms

Representing (Gamma_{p^j}) by a (j)-particle configuration makes fusion
concatenation.  To descend from ordered configurations to the commutative
arithmetic correspondence, distinct orderings have the same product.  For
distinct labels this is exactly D.142's Fock descent:

\[
 \left\|Q{1\over\sqrt{r!}}
   \sum_{\sigma\in S_r}e_{p_{\sigma(1)}\cdots p_{\sigma(r)}}\right\|
 =\sqrt{r!}.                                         \tag{3.3}
\]

The free descent is unbounded; normalized symmetrization changes
multiplication by

\[
 \sqrt{(r+s)!/(r!s!)}.                               \tag{3.4}
\]

Thus the configuration repair is not new relative to the corpus and is
incompatible with the coefficient-one composition and central metric of row
(b).  The obstruction becomes unavoidable cofinally even if the first local
test uses only one repeated prime.

### 3.3 Keep the arithmetic monoid as an external decoration

This is the formal specification already reached in P3: the matroidal carrier
would have HR, while the faithful monoid and the Gamma/Green trace live in a
separate coefficient system.  The missing assertion would then be precisely

\[
 q_{\rm Chow}(D_f,D_g)=B_{\rm nuc}(f,g).              \tag{3.5}
\]

Nothing in the matroid axioms or in AHK constrains the external decoration
enough to prove (3.5).  Postulating the comparison merely relocates row (d).

## 4. The shifted-pair test

For (Xi_a), the two local characters give two iterate towers.  They can be
represented by two copies of any proposed flat/configuration carrier.  AHK
continues to give HR for the resulting finite matroids.  Thus matroidality
itself does not detect local rank one versus rank two.

One may reject (Xi_a) by adding the already known indecomposability clause
``one tower per place''.  That clause is a legitimate discriminator, but it
does not repair Theorem 2: even the single zeta tower cannot encode its
faithful fusion by matroid join.  Hence the (Xi_a) test cannot promote the
candidate.

## 5. Relation to G-125.B and T2

AHK would have supplied the missing finite Hodge--Riemann mechanism and exact
compatible embeddings would have avoided continuity of signatures.  The
present theorem is upstream of both issues: the arithmetic tower cannot enter
the AHK carrier with the required multiplication.

Consequently there is no transition system

\[
 A^*(M_S)\longrightarrow A^*(M_{S'})                 \tag{5.1}
\]

having all three properties simultaneously:

1. faithful iterate labels;
2. fusion induced by the flat/Chow structure;
3. coefficient-one row-(b) composition.

Without such a system, the pointwise-HR persistence lemma is correct but has
no arithmetic input to which it can be applied.

## 6. Verdict

The arithmetic Bergman configuration candidate and the discrete-Morse
variant are **retired**.  Their finite collision conditions

\[
 C_2\circ C_2\to C_4,
 \qquad \operatorname{Res}(C_2\circ C_3)=0,
 \qquad \partial^2=0
\]

remain meaningful as a chain model of P3_loc, but they cannot be the source of
the global Hodge--Riemann sign.  The obstruction is not Babaee--Huh or T2; it
is the more elementary incompatibility

\[
 \boxed{\text{faithful additive iteration}\quad\not\hookrightarrow\quad
        \text{idempotent flat join}.}                 \tag{6.1}
\]

No part of this negative result closes row (d), but it prevents the programme
from rebuilding the already excluded Fock/configuration descent under AHK
terminology.

