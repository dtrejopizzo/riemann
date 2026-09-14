# A125.011 — row A on the graph sector without the tangential complex: the conditional `(*)` discharged

Status: `PROVED-IN-REPOSITORY`.  This note removes the single conditional
input `(*)` that A125.001, A125.003, A125.004 and A125.008 shared.  After
A125.006 the tangential complex `Ω_dR` is not load-bearing on `G`; every
clause is rebuilt here directly on the realized graph category.

## 1. The realized graph category

By P123.064, `C_tw(A)` is the dg category of bounded cochain complexes whose
terms are finite sums of twists `E_β={}_1A_β` and whose differentials are
intertwiner matrices, with the complete dg Hom complex as its topological
enrichment; cones, shifts and finite sums are actual objects.  By P123.082,
after choosing one lift per external class,

\[
 \operatorname{Hom}_{A\text{-}A}(E_{\beta_a},E_{\beta_b})
 =\begin{cases}\mathbb C\,U_\gamma,& a=\gamma b,\ \gamma\in\Gamma_S,\\ 0,&\text{otherwise,}\end{cases}
 \tag{1.1}
\]

a topological identification.  Hence `G:=C_tw(A)` is, up to the lift
isomorphisms, the category of bounded complexes of finite-dimensional graded
vector spaces indexed by external idele classes, and P123.082 records the
consequence: cones create no new indecomposables.

The faithful kernel realization is P123.073, `T_{b,a}f(x)=\sum_\gamma
b_\gamma(x)f(a^{-1}\gamma^{-1}x)`, and its half-density version P123.074 (1),
`\Pi(b,a)=|a|_S^{-1/2}T_{b,a}`, with

\[
 \Pi(b,a)\Pi(c,d)=\Pi(b\beta_a(c),ad),
 \qquad
 \Pi(b,a)^{*}=\Pi(\beta_a^{-1}(b^{*}),a^{-1}).                    \tag{1.2}
\]

## 2. A.4 on `G` from the Hilbert adjoint alone

**Definition 2.1.**  On generators put `E_a^{\dagger}:=E_{a^{-1}}`, realized
by (1.2).  On a morphism `v=\lambda U_\gamma:E_a\to E_{\gamma a}` put
`v^{\dagger}:=\bar\lambda\,U_{\gamma^{-1}}:E_{\gamma^{-1}a^{-1}}\to
E_{a^{-1}}`, the Hilbert adjoint of the realized operator.  Extend to
`C_tw(A)` by conjugate transposition of intertwiner matrices with the standard
Hom-complex signs, `(d_K)^{\dagger}` becoming the differential of the dual
complex.

**Theorem 2.2.**  `†` is a continuous, antilinear, contravariant involution on
`G` with `(K\star L)^{\dagger}\cong L^{\dagger}\star K^{\dagger}` and
`\Delta^{\dagger}=\Delta`.  It is source-defined and uses no later scalar
form.

*Proof.*  Contravariance and `†^2=\mathrm{id}` hold on generators and
morphisms because (1.2) is the Hilbert adjoint on the faithful image, and the
adjoint of an adjoint is the operator.  By (1.1) every morphism of `C_tw(A)` is
a finite matrix of scalars times lift unitaries, so conjugate transposition is
well defined and continuous for the finite-product topology of P123.064 §1,
and it commutes with the dg differential up to the standard sign, hence passes
to cones and shifts.  Antimultiplicativity is (1.2): `E_a\star E_d\cong E_{ad}`
by P123.064 §3, and `(E_{ad})^{\dagger}=E_{d^{-1}a^{-1}}=E_d^{\dagger}\star
E_a^{\dagger}`.  `\Delta=E_1` is fixed.  QED

Nothing here uses `Ω_dR`, internal Homs or profile objects.  Those were
needed in A125.001 because that note aimed at the localized ideals, and
A125.001 Corollary 3.2 shows the ideals are not self-dual; the graph classes
are, as a family.  The obstruction `Hom_{U-bimod}(U,N)=0` never touches `G`
because `N\notin G`.

## 3. A.5 on `G` from the cyclic shadow alone

**Definition 3.1.**  `Corr_A^{tr}(G):=\{K\in G:\ \mathrm{Tr}_A(K)$ is a
bounded complex with locally constant finite ranks$\}`, where `\mathrm{Tr}_A`
is the cyclic shadow of P123.122 (4) computed as the corner bar of
P123.096–097.  `T_A:=\mathbb Z^{\pi_0(B_q)}`, `\mathrm{Tr}_A^{\chi}:=\chi\circ
\mathrm{Tr}_A`.

**Theorem 3.2.**  `Corr_A^{tr}(G)=G`.  On it `\mathrm{Tr}_A^{\chi}` is
additive on triangles, vanishes on acyclics, is cyclic, is cutoff independent,
and agrees with the degree of the determinant of the shadow.

*Proof.*  By A125.006 Theorem 1.1 the shadow of every generator is acyclic or
`B[0]` of rank `r`; shadows of finite sums, shifts and cones are the
corresponding finite sums, shifts and cones by exactness of `\mathrm{Tr}_A`
(P123.122 §4), so every object of `G` has a perfect shadow.  Additivity and
vanishing on acyclics are properties of `\chi`; cyclicity is P123.122 (5);
cutoff independence is P123.095 §4; the determinant identity is P123.095 (4).
QED

## 4. A.8 on `G` from the determinant of the shadow

**Definition 4.1.**  `\lambda_{RR}(K):=\mathrm{Det}_e(\mathrm{Tr}_A(K))`, the
graded determinant line of the perfect shadow, P123.095 (2), with degree
`\deg\lambda_{RR}(K)`.

**Theorem 4.2.**  `\lambda_{RR}` satisfies convergence, biextension
(the cone law P123.095 (3)), principal invariance (isomorphism invariance
plus cutoff independence), restriction compatibility, and the equality

\[
 \deg\lambda_{RR}(K)=\mathrm{Tr}_A^{\chi}(K),\qquad K\in G .        \tag{4.1}
\]

*Proof.*  (4.1) is P123.095 (4) applied to the shadow complex; the other
properties are P123.095 §§2–4 verbatim.  QED

**Remark 4.3 (relation to the analytic determinant).**  A125.008 used the
coupled relative determinant germ of P123.109–110 as `\lambda_{RR}`.  That
germ and Definition 4.1 agree on the ruling plane by `A_MIXED_METRIC_WORK` (6)
together with A125.004 Theorem 3.3, and agree in degree on `G` by (4.1) and
the Lefschetz identity of P123.009.  The analytic germ carries a metric that
Definition 4.1 does not; the metric refinement is a strengthening, not a
requirement of A.8, and is not needed for the equality clause.

## 5. The declared completion

**Definition 5.1.**  The declared completion of `G` is the compact-section
Fell completion of P123.016 §5 restricted to sections whose coefficient at
each external class is a scalar multiple of the chart unit.  Restriction
`j_{P,T}` of P123.121 (11) multiplies the coefficient by `\prod_{\ell\in
T\setminus P}\chi_\ell`, the unit of the added coefficient factors, so it
preserves this class; its convolution is the continuous extension of
pull–tensor–push, not a product declared on labels.

**Proposition 5.2.**  `G` with this completion is closed under `\star`, `†`,
restriction and the operations of §§2–4, all of which are continuous.

*Proof.*  `\star` and `†` act on the scalar coefficients by convolution and
conjugate inversion on the idele class group, both continuous for the rapid
topology; restriction is coefficient-unital as stated; `\mathrm{Tr}_A^\chi`
and `\lambda_{RR}` are continuous by P123.095 §1.  QED

## 6. Consequence

Every appeal to `(*)` in A125.001 §6, A125.003 §5, A125.004 and A125.008 is
now removed on `G`.  The de Rham constructions of A125.001 and A125.003 are
retained as valid constructions for the ideal sector, where they remain the
right tool, but they carry no load in the A.1–A.10 audit on `G`.

| clause on `G` | before | after |
|---|---|---|
| A.4 | `CONDITIONAL` on `(*)` | `PROVED` unconditionally, Theorem 2.2 |
| A.5 | `CONDITIONAL` on `(*)` | `PROVED` unconditionally, Theorem 3.2 |
| A.8 | `CONDITIONAL` on `(*)` | `PROVED` unconditionally, Theorem 4.2 |
| A.2 declared completion | implicit | explicit, Definition 5.1 |
