# A125.006 — the fixed-point dichotomy proves the mixed sector is nonzero (clause A.6)

Status: `PROVED-IN-REPOSITORY`.  This note closes the crux identified in
A125.005 and in the phase README, and it **supersedes** Requirement 3.1 of
A125.005 by exhibiting a target that works.  It also resolves the A.3/A.4
tension of A125.002 §4 by identifying the right generating sector.

No `Λ(n)`, no `Γ_n`, no explicit formula, no zero of zeta, no RH and no
positivity of `B_nuc` is used (clause A.10).

## 1. The invariant was the wrong one, and the right one already exists

A125.005 Theorem 1.1 proved that `\mathrm{Det}_e((E_u)_{dR})` is trivial for
every idele class `u`.  The reason given there is correct but incomplete: the
de Rham twist equalizes the ranks in degrees `0` and `1`, so **every**
rank- or determinant-level invariant of the twisted object is blind.

The invariant that is not blind is the one clause A.5 actually names first:
the **cyclic shadow** `\mathrm{Tr}_A` of P123.122 (4), before any de Rham
twist.  Its Euler characteristic is a Lefschetz number, and the corpus already
computes it, in two complementary notes that were written for other purposes
and never combined.

**Theorem 1.1 (fixed-point dichotomy; IMPORTED, hypotheses checked).**  Let
`w` be an external idele class acting on the compact boundary `B_q`.

1. If `w` has **no boundary fixed points**, the full twisted corner bar of
   `E_w` admits an explicit continuous contraction; hence
   `\mathrm{Tr}_A(E_w)` is admissibly acyclic.  *(P123.096.)*
2. For the **fixed** case the continuous corner bar is `B[0]` up to strict
   quasi-isomorphism, by bounded character averages and exact convergent cycle
   fillings.  *(P123.097.)*

Define

\[
        \delta(w):=\chi\bigl(\mathrm{Tr}_A(E_w)\bigr)
        \ \in\ \mathbb Z^{\pi_0(B_q)} ,                        \tag{1.1}
\]

the Euler characteristic of the cyclic shadow, which is defined because in
both cases of Theorem 1.1 the shadow is a bounded complex with locally
constant finite ranks.  Then

\[
\boxed{
 \delta(w)=0\ \ \text{if $w$ acts freely},
 \qquad
 \delta(1)=r\neq0 .}                                           \tag{1.2}
\]

**Scope of the import.**  P123.096 and P123.097 are proved for the corner bar
of the constructed boundary carrier, with its orbit-decay trace ideal.  Two
things are used below and nothing else: that a freely acting external class
gives an acyclic shadow, and that the identity gives `B[0]` of rank `r>0`.  The
argument of Theorem 2.1 needs only one freely acting class of module one, so
it is insensitive to how large the family of such classes is, and does not
require the dichotomy for every idele class.

*Proof of (1.2).*  An admissibly acyclic complex has vanishing Euler
characteristic, giving the first equality.  For the second, `E_1=\Delta` and
P123.097 identifies its corner bar with `B[0]`, concentrated in degree zero of
rank `r=\dim K_0>0` by P123.119.  QED

**Lemma 1.2 (free unit classes exist).**  Every `w\neq1` in the image of the
external action on `B_q` acts freely on `B_q`, and there are such `w` with
`|w|=1`.

*Proof.*  `B_q` is a compact group and the external dilation acts on it by
translation, by the construction of the boundary in P123.090–094.  A
translation of a group by a nonidentity element has no fixed point.  The
kernel of `|\cdot|` surjects onto a nontrivial subgroup of `B_q`, since `B_q`
is the boundary of the unit-level quotient; any nonidentity element of that
subgroup is a free unit class.  QED

## 2. The graph classes are not in the ruling span

**Theorem 2.1.**  The classes `[E_w]` do not all lie in the span of the two
ruling classes `e_\pm` of A125.004 Theorem 3.3.  Consequently `N_A` contains a
nonzero mixed sector.

*Proof.*  Suppose every `[E_w]` lies in `\mathrm{span}\{e_-,e_+\}`, say
`[E_w]=\alpha(w)e_-+\beta(w)e_+`.  Pairing against `e_\pm` and using
P123.008 (2.3), where `E_w` acts on the two Tate fibres by
`D_w=\mathrm{diag}(|w|^{-1/2},|w|^{1/2})`, the coefficients `\alpha(w)` and
`\beta(w)` are determined by `|w|` alone.  With the hyperbolic matrix (3.1) of
A125.004 this gives

\[
 \delta(w)=\langle E_w,E_1\rangle
 =\alpha(w)\beta(1)+\beta(w)\alpha(1),
\]

a function of `|w|` alone.  In particular `\delta(w)=\delta(1)` for every `w`
with `|w|=1`.  By Lemma 1.2 choose such a `w\neq1`; it acts freely, so
`\delta(w)=0` by (1.2), whence `\delta(1)=0`.  This contradicts
`\delta(1)=r\neq0` in (1.2).  QED

Theorem 2.1 is the arithmetic counterpart of a familiar classical fact, and
the analogy is worth stating because it confirms the typing.  On a curve over
a finite field, the graph classes `\Gamma_{F^k}` have intersection numbers
`q^{k}+1-\sum_i\alpha_i^{k}`: the first two terms are the ruling contribution,
depending only on the "module" `q^{k}`, and the remaining sum is exactly the
mixed part.  A class lying in the ruling span would have no such term.  Here
the same separation is obtained without any eigenvalue input, purely from the
dichotomy: freely acting classes contribute nothing, the identity contributes
`r`, and no function of `|w|` alone can do both.

## 3. The graph sector is the right generating sector

The tension recorded in A125.002 §4 and A125.003 §4 — that closing A.4 by
adjoining the duals of the localized ideals breaks the excision proof — does
not arise for the graph classes.

**Theorem 3.1.**  Let `\mathcal G` be the stable sector generated by
`\{E_w\}_{w}` under finite sums, retracts, shifts and cones.  Then

1. `\mathcal G` is `†`-closed, with `E_w^{\dagger}\cong E_{w^{-1}}`, and needs
   no profile objects;
2. `\mathcal G\subseteq Corr_A^{tr}`;
3. two-sided excision holds on `\mathcal G`, and more generally on the sector
   generated by `\mathcal G` together with the localized ideals;
4. `\mathcal G` carries the nondegenerate pairing `(u,v)\mapsto\delta(uv^{-1})`
   of (1.1).

*Proof.*  (1) is A125.004 Theorem 4.1 (4.1), i.e. P123.016 (4.2) with the
half-density normalization of A125.001 (4.1)–(4.2); the dual of a graph class
is again a graph class, so unlike the localized ideals the sector is closed
under `†` without enlargement.  This is the structural point: A125.001
Corollary 3.2 showed the ideals are not self-dual, and that is what forced the
profile objects; the graph classes are self-dual as a family.

(2) is A125.004 Theorem 4.1.

(3) By A125.002 Theorem 2.1 it suffices that
`B_O\hat\otimes M\hat\otimes I_O\hat\otimes N\hat\otimes B_O=0` for `M,N` in
the sector.  For `M=E_u`, `N=E_v` and a Čech term `I_{J_T}`, the twists are
invertible, so `E_u\hat\otimes I_{J_T}\hat\otimes E_v\cong I_{J_T,\,uv}` up to
relabelling of the open by the dilation, which preserves every
coordinate-nonzero open by P123.124 §5.  Lemma 3.1 of A125.002 then annihilates
it against `B_O`.  Exactness in each variable and the finite Čech resolution
give the general case.

(4) is Theorem 2.1 together with (1.2).  QED

**Corollary 3.2 (clause A.6).**  On `\mathcal G` the numerical radical is
closed, a two-sided ideal and `†`-stable (A125.004 Theorem 2.2, whose proof
used only the cone law and cyclicity and is unaffected by the change of
target); `N_A=\mathcal G/\mathcal N` is Hausdorff with continuous descending
`\star` and `†` (A125.004 Theorem 3.2); it contains the ruling plane with
intersection matrix `[[0,1],[1,0]]` (A125.004 Theorem 3.3) and, by
Theorem 2.1, a nonzero mixed sector.  Clause A.6 is satisfied on `\mathcal G`.

## 4. Corrections to the earlier notes of this campaign

| item | correction |
|---|---|
| A125.005 Requirement 3.1 | `SUPERSEDED`.  The numerical target is the Euler characteristic of the cyclic shadow (1.1), not the de Rham determinant and not the anomaly cocycle.  A125.005 Theorem 1.1 stands as a no-go for the de Rham determinant. |
| A125.003 Def. 2.3 | `T_A` is `\mathbb Z^{\pi_0(B_q)}` via (1.1); the graded determinant `Det_e` is retained only as the boundary-corner determinant, not as the numerical target. |
| A125.004 Def. 1.1 | replaced by `\langle K,L\rangle=\chi(\mathrm{Tr}_A(K\star L^{\dagger}))`.  Lemma 1.2 and Theorems 2.2, 3.2, 3.3, 4.1 of that note are unaffected: their proofs use the cone law, cyclicity and the adjunction (1.2), all valid for the shadow. |
| A125.002 §4 and A125.003 §4 open items | `RESOLVED` on `\mathcal G` by Theorem 3.1: the profile objects are not needed, because the graph sector is already `†`-closed. |
| phase README "single crux" | `RESOLVED`.  The anomaly cocycle is not required for A.6.  It remains the natural object for A.8, where a determinant-level statement is genuinely needed. |

## 5. What this does not do

Theorem 2.1 proves the mixed sector is nonzero.  It does **not** compute it,
and it gives no information about its rank, its topology as a completed
sector, or any sign.  Clause A.6 asks only for a nonzero completed mixed
sector, and that is what is proved.

It also does not supply A.7 or A.8.  Effectivity must still be constructed
from the source geometry and shown to descend to `N_A`, and mixed
Riemann–Roch still needs the determinant-level statement for which the anomaly
cocycle of P123.107–110 remains the right object.  Those are the next two
notes.

## 6. Ledger

| statement | status |
|---|---|
| Thm 1.1 fixed-point dichotomy | `IMPORTED` from P123.096/097 with hypotheses checked; scope note in §1 |
| (1.2) `δ(w)=0` for free `w`, `δ(1)=r≠0` | `PROVED-IN-REPOSITORY` |
| Lemma 1.2 free unit classes exist | `PROVED-IN-REPOSITORY` |
| Thm 2.1 graph classes leave the ruling span; mixed sector nonzero | `PROVED-IN-REPOSITORY` |
| Thm 3.1 `\mathcal G` is `†`-closed, trace-class, excisive, nondegenerate | `PROVED-IN-REPOSITORY` |
| Cor. 3.2 clause A.6 on `\mathcal G` | `PROVED-IN-REPOSITORY` |
| computation of the mixed sector; A.7; A.8 | `OPEN` |
