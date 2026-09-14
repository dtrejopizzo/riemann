# A125.004 — the numerical pairing, its radical and the quotient `N_A` (clause A.6)

Status: `PROVED-IN-REPOSITORY` for Theorems 2.2, 3.1 and 3.3, relative to the
constructions of A125.001 and A125.003 and their single shared conditional
input.  `OPEN` for the nonzero completed mixed sector, §4.

> **Correction (A125.005).**  The pairing of Definition 1.1 is CONDITIONAL on
> the corrected target of A125.005 Requirement 3.1; Corollary 4.2's reduction
> to one determinant line is superseded by the reduction to the anomaly
> cocycle of the coupled relative determinant.  Theorems 2.2, 3.2 and 4.1 are
> unaffected.  Theorem 3.3 is restricted to the finite Tate realization.


Clause A.6 requires: numerical equivalence defined as the radical against
**all** trace-class tests; proofs that it is closed and stable under
composition and `†`; and a Hausdorff quotient `N_A` containing the ruling
plane and a nonzero completed mixed sector, with explicit topology and
continuity of all operations.

Earlier numerical constructions in phase 123 (P123.007, P123.017) were built
from the coefficient trace before a trace-class domain existed, and P123.018
reopened them.  The point of this note is that A125.003 supplies, for the
first time, an integer-valued invariant on a composition-closed and
`†`-stable domain, so the radical can be taken against the tests the clause
actually names.

## 1. The pairing

Throughout, `\mathcal C` is the localized sector of P123.124 closed under
`†`, `Corr_A^{tr}\subseteq\mathcal C` is the trace-class domain of A125.003
(2.1), and

\[
 \mathrm{Tr}_A(K)=\bigl(\mathrm{Det}_e(K_{dR}),\deg(K_{dR})\bigr)
\]

is its determinant-valued shadow.  Write `\mathbb Z^{\pi_0}` for the locally
constant integer-valued functions on the compact boundary `B_q`.

**Definition 1.1.**  For `K\in\mathcal C` and `L\in Corr_A^{tr}` with
`K\star L^{\dagger}\in Corr_A^{tr}`, set

\[
\boxed{
 \langle K,L\rangle:=\Bigl[\,\mathrm{Det}_e\bigl((K\star L^{\dagger})_{dR}\bigr)\,\Bigr]
 \ \in\ \mathrm{Pic}(B_q)\times\mathbb Z^{\pi_0},}                \tag{1.1}
\]

the class of the determinant line together with the virtual rank.  It is not a
scalar chosen from a later quadratic form.  By A125.003 Theorem 3.1(2) and
`†`-stability the hypothesis on `K\star L^{\dagger}` is automatic when
`K\in Corr_A^{tr}`.

**Remark 1.1a (the rank component is the wrong invariant, and why).**  The
line component is not a refinement of convenience; on the objects that matter
the rank component vanishes identically.  Indeed A125.003 Theorem 3.1(1) gives
`\Delta_{dR}=M_{dR}\simeq_BB^{r}[0]\oplus B^{r}[-1]`, whose virtual rank is
`r-r=0`, and the same holds after any twist by an automorphism.  This is
forced: the middle pairing (4.4) of A125.001 has total degree one and is
perfect between degrees `0` and `1`, so equal ranks in the two degrees are a
structural consequence of self-duality, not an accident of the model.

The classical comparison is instructive rather than alarming.  There
`L\Delta^{*}` of the diagonal has terms `O_C` and `\Omega_C[1]`, of equal rank
one, and the self-intersection `\Delta\cdot\Delta=2-2g` is **not** the
difference of ranks but the Euler characteristic
`(1-g)-(g-1)`, i.e. a degree of determinant lines.  So the numerical content of
row A must sit in `\mathrm{Det}_e`, never in a virtual rank.  This is also the
first place where the shape of the programme's later masses is visible: those
masses are logarithms of determinants, not dimensions.

**Lemma 1.2.**  `\langle-,-\rangle` is biadditive, continuous in each variable
for the topology of `\mathcal C`, invariant under quasi-isomorphism in the
domain, and satisfies

\[
 \langle K\star M,L\rangle=\langle K,L\star M^{\dagger}\rangle,
 \qquad
 \langle K,L\rangle=\langle L,K\rangle^{\!*},                      \tag{1.2}
\]

where `*` is the involution induced on `\mathbb Z^{\pi_0}` by `†`.

*Proof.*  Biadditivity is the cone law `\mathrm{Det}_e(\mathrm{Cone}f)
=\mathrm{Det}_e(L)\otimes\mathrm{Det}_e(K)^{-1}` of P123.095 (3), which makes
`[\mathrm{Det}_e]` additive on distinguished triangles; quasi-isomorphism
invariance is the canonical trivialization on acyclics, A125.003
Theorem 3.1(3).  For the first identity in (1.2), A125.001 Theorem 5.1(2)
gives `(K\star M\star L^{\dagger})\cong K\star(L\star M^{\dagger})^{\dagger}`
after antimultiplicativity, and `\deg` is invariant under the resulting
isomorphism.  The second follows from cyclicity, A125.003 Theorem 3.1(4),
together with `\mathrm{Tr}_A(K^{\dagger})\cong\mathrm{Tr}_A(K)^{-1}` from
A125.003 §4.  Continuity is that of `\deg` on `P_e(J)`, where rank is locally
constant and the presentation topology is the direct-summand topology of
P123.095 §1.  QED

## 2. Numerical equivalence

**Definition 2.1.**  `K\in\mathcal C` is *numerically trivial* if
`\langle K,L\rangle=0` for every `L\in Corr_A^{tr}`.  Let `\mathcal N` be the
set of numerically trivial objects.

**Theorem 2.2.**  `\mathcal N` is

1. a **closed** subspace of `\mathcal C`;
2. a two-sided **ideal** for `\star`: `K\in\mathcal N` implies
   `K\star M\in\mathcal N` and `M\star K\in\mathcal N` for every
   `M\in\mathcal C`;
3. **stable under** `†`.

*Proof.*  (1) `\mathcal N=\bigcap_{L}\ker\langle-,L\rangle`, an intersection of
kernels of continuous maps by Lemma 1.2, hence closed.

(2) For `K\in\mathcal N`, `M\in\mathcal C` and any test `L`, the first identity
of (1.2) gives `\langle K\star M,L\rangle=\langle K,L\star M^{\dagger}\rangle`.
By A125.003 Theorem 3.1(2) and `†`-stability, `L\star M^{\dagger}` is again a
trace-class test, so the right side vanishes.  The left-hand case is symmetric
using the second identity of (1.2).

(3) If `K\in\mathcal N` then for every test `L`,
`\langle K^{\dagger},L\rangle=\langle L^{\dagger},K\rangle^{*}
=\langle K,L^{\dagger}\rangle^{**}=0`, using (1.2) twice and `†`-stability of
the test class.  QED

Theorem 2.2 is exactly what P123.018 reopened: the earlier radical arguments
used operations whose domain was in question, whereas (2) and (3) here are
proved on the composition-closed, `†`-stable domain of A125.003.

## 3. The quotient and the ruling plane

**Definition 3.1.**  `N_A:=\mathcal C/\mathcal N` with the quotient topology.

**Theorem 3.2.**  `N_A` is Hausdorff, `\star` and `†` descend to it
continuously, and `\langle-,-\rangle` descends to a nondegenerate pairing on
the image of `Corr_A^{tr}`.

*Proof.*  Hausdorffness is Theorem 2.2(1): a quotient of a topological vector
space by a closed subspace is Hausdorff.  Descent of `\star` and `†` is
Theorem 2.2(2)–(3).  Nondegeneracy is Definition 2.1.  QED

**Theorem 3.3 (the ruling plane sits inside).**  The two Tate characters
`|\cdot|^{\mp1/2}` of P123.008 (2.3) define two classes `e_-,e_+` in `N_A`
whose pairing matrix is

\[
 \begin{pmatrix}
 \langle e_-,e_-\rangle&\langle e_-,e_+\rangle\\
 \langle e_+,e_-\rangle&\langle e_+,e_+\rangle
 \end{pmatrix}
 =\begin{pmatrix}0&1\\1&0\end{pmatrix},                            \tag{3.1}
\]

the intersection matrix of the two rulings, and `†` exchanges them.

*Proof.*  P123.008 Theorem 2.1 constructs the continuous unital algebra map
`\rho_T:C_{\mathbb Q}\to B_T=\mathbb C\oplus\mathbb C` with
`\rho_T(\delta_q)=(q^{-1/2},q^{1/2})` and
`\rho_T(c^{\dagger})=\rho_T(c)^{\sharp}`, and P123.008 §5 computes the
Hermitian form `\beta_T(z,w)=z_-\overline{w_+}+z_+\overline{w_-}` on the basis
`e_-=(1,0)`, `e_+=(0,1)`, giving (3.1).  Its §6 shows that base change along
`\rho_T` carries finite-cell perfect modules to finite-cell `B_T`-modules, so
their Knudsen–Mumford determinant lines exist and the two classes land in the
trace-class domain of A125.003; `\deg` of the resulting rank-one modules
reproduces (3.1).  The sharp involution exchanging the two fibres is the
restriction of `†` by A125.001 Theorem 5.1, since the half-density `h` of
A125.001 (4.1) is exactly the character `|\cdot|^{-1/2}` whose two Tate
components are `e_\mp`.  Nondegeneracy of (3.1) implies the two classes are
nonzero in `N_A` and independent.  QED

Theorem 3.3 makes precise, and for the first time inside a numerical quotient
with a declared trace-class domain, the identification that P123.008 could
only state at the level of the internal coefficient model: the half-density
of the dagger and the two ruling degrees are the same datum.

## 4. The mixed sector: the graph classes are in the domain

The localized ideals `I_{J,\beta}` are poor candidates for mixed classes: the
de Rham twist finitizes the middle variable, not an outer ideal, so A125.003
does not place them in `Corr_A^{tr}`.  The right candidates are the graph
bimodules, and they do lie in the domain.

**Theorem 4.1.**  For every external idele class `u`, the graph bimodule
`E_u={}_1A_{\beta_u}` of P123.014/P123.016 lies in `Corr_A^{tr}`, and

\[
 E_u\star E_v\cong E_{uv},
 \qquad
 E_u^{\dagger}\cong E_{u^{-1}} .                                   \tag{4.1}
\]

*Proof.*  `E_u` is `A` with the right action twisted by the automorphism
`\beta_u`.  Untwisting is an exact equivalence of module categories, as used
for the localized twists in P123.124 §5, so `E_u` is relatively projective on
each side and `(E_u)_{dR}` is carried to `\Delta_{dR}=M_{dR}` by that
equivalence.  `M_{dR}` is perfect by A125.003 Theorem 3.1(1), and perfectness
is preserved by an exact equivalence, so `E_u\in Corr_A^{tr}`.  The
composition law is P123.016 (3.2)–(3.3), where pull–tensor–push of the two
graphs is the balanced bimodule tensor `x\otimes y\mapsto x\beta_u(y)`, with
no higher excess term because the graph maps are isomorphisms onto their
images.  The dagger law is P123.016 (4.2), `K_u^{\dagger}\cong K_{u^{-1}}`,
now with the half-density normalization of A125.001 (4.1)–(4.2) rather than
the bare factor swap.  QED

**Corollary 4.2.**  The pairing restricted to graph classes is a function on
the idele class group:

\[
 \langle E_u,E_v\rangle=\delta(uv^{-1}),
 \qquad
 \delta(w):=\bigl[\mathrm{Det}_e\bigl((E_w)_{dR}\bigr)\bigr].       \tag{4.2}
\]

So the whole mixed numerical structure of the graph sector is the single
function `\delta` on idele classes, and `A.6`'s mixed-sector requirement
becomes the question whether `\delta` is nonconstant, equivalently whether
some `E_u` is not numerically equivalent to the diagonal.

**What remains, stated exactly.**  Two cheap tests do **not** decide it, and
recording why keeps the next attempt from repeating them.

* The rank component is useless: it vanishes identically by Remark 1.1a.
* Pairing against the ruling plane is useless: `E_u` acts on the two Tate
  fibres by `D_u=\mathrm{diag}(|u|^{-1/2},|u|^{1/2})` (P123.008 (2.3)), so
  `\langle E_u,e_-\rangle\langle E_u,e_+\rangle` is `|u|^{1/2}|u|^{-1/2}=1`,
  independent of `u`.  The hyperbolic form is exactly blind to the dilation,
  which is the same invariance that makes the ruling plane a ruling plane.

Therefore the mixed sector is nonzero if and only if the determinant line
`\mathrm{Det}_e((E_u)_{dR})` differs from the value predicted by the
hyperbolic ruling span.  This is now a computation of **one line bundle on the
compact boundary** `B_q`, with all inputs constructed: the twist `\beta_u`,
the finite retract `H`, and the cutoff-independent determinant of P123.095.
It is not a search for a new object.

That single computation is simultaneously the missing item of A125.002 §4 and
of A125.003 §4: a graph class outside the ruling span provides the mixed class
whose presence makes the joint A.3/A.5 domain nontrivial.  The three open
items of this campaign are one item.

## 5. Ledger

| statement | status |
|---|---|
| Def. 1.1: integer pairing `⟨K,L⟩=deg((K⋆L^†)_dR)` | `CONSTRUCTED` |
| Lemma 1.2: biadditive, continuous, adjunction (1.2) | `PROVED-IN-REPOSITORY` |
| Thm 2.2: radical is closed, a two-sided ideal, `†`-stable | `PROVED-IN-REPOSITORY` |
| Thm 3.2: `N_A` Hausdorff, operations descend, pairing nondegenerate | `PROVED-IN-REPOSITORY` |
| Thm 3.3: ruling plane `[[0,1],[1,0]]` inside `N_A`, exchanged by `†` | `PROVED-IN-REPOSITORY` |
| Rem. 1.1a: the numerical content is in `Det_e`, not in a virtual rank | `PROVED-IN-REPOSITORY` |
| Thm 4.1: graph classes `E_u` lie in `Corr_A^tr`; composition and `†` laws | `PROVED-IN-REPOSITORY` |
| Cor. 4.2: mixed numerics of the graph sector reduce to one function `δ` on idele classes | `PROVED-IN-REPOSITORY` |
| nonzero completed mixed sector | `OPEN`, reduced in §4 to computing one determinant line; same item as A125.002 §4 and A125.003 §4 |
| all of the above | `CONDITIONAL` on the single source-pushforward comparison of A125.001 §6 |
