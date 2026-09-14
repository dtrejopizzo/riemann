# A125.003 — the trace-class domain `Corr_A^tr` and the determinant target `T_A` (clause A.5)

Status: `CONSTRUCTED` for Definitions 2.1–2.3 and `PROVED-IN-REPOSITORY` for
Theorem 3.1.  `CONDITIONAL` on the source-pushforward comparison of §5, which
is shared with A125.001.  Nothing here uses `Λ(n)`, a distinguished `Γ_n`,
Meyer's formula, a zero of zeta, RH or positivity of `B_nuc`.

> **Correction (A125.005).**  Definition 2.3's identification of `T_A` with
> graded line bundles on `B_q` is RETRACTED: A125.005 Theorem 1.1 proves it
> degenerates on graph classes.  The domain `Corr_A^tr` of Definition 2.2 and
> all parts of Theorem 3.1 are unaffected.  See
> [A125.005](A125_005_CORRECTION_DETERMINANT_TARGET_MUST_RETAIN_THE_TWIST.md).


Clause A.5 asks for `Tr_A:Corr_A^{tr}\to T_A`, additive, cyclic, compatible
with restriction and determinant, with a finite scalar degree wherever one is
asserted.  Before this note **neither** `Corr_A^{tr}` **nor** `T_A` had a
definition anywhere in the corpus: both occur only as requirements in the
acceptance specification and in the phase-123 plan.  The ingredients existed
in three disconnected places.  This note connects them.

## 1. The three available ingredients and the one obstruction

* A determinant target exists, but only on the boundary corner.  P123.095
  constructs, on bounded complexes in the corner-perfect category `P_e(J)`
  over `B=eJe=C(B_q)`,
  \[
   \mathrm{Det}_e(K)=\bigotimes_i(\det E^i)^{(-1)^i},
   \qquad
   \deg(K)=\sum_i(-1)^i\operatorname{rank}E^i,                     \tag{1.1}
  \]
  with the cone law `\mathrm{Det}_e(\mathrm{Cone}f)=\mathrm{Det}_e(L)\otimes
  \mathrm{Det}_e(K)^{-1}`, a canonical trivialization on acyclics, the
  source-trace identity `\sum_i(-1)^i\mathrm{Tr}_{\rm source}(\mathrm{id})=\deg`,
  the Jacobi identity for logarithmic derivatives, and cutoff independence.
  Its recorded gap is that it "does not prove that the diagonal of the
  designated mixed correspondences lies in this perfect domain".
* A cyclic shadow exists on all of the sector.  P123.122 (4)–(5) gives
  `\mathrm{Tr}_A(M)=\mathrm{Tot}[M\hat\otimes A^{\hat\otimes n}]` with
  `\mathrm{Tr}_A(M\star N)\cong\mathrm{Tr}_A(N\star M)`, degreewise nuclear,
  and explicitly disclaims any determinant of an unbounded complex.
* Trace ideals exist: `J_{orb}` (P123.092) and `J_V` (P123.085), with their
  integrable traces, stability and inverse-closedness.

The obstruction to simply taking "perfect kernels" as the domain is proved in
`A_DUALITY_WORK.md`: `R=B` is perfect over `B`, but
`R\hat\otimes^L_SR=B\hat\otimes S`, whose base change along a continuous
character of `B` is `S` in degree zero with infinite-dimensional cohomology.
So the perfect sector is **not closed under composition**.  The same file names
the repair: "put the differential in, so the middle factor is finite up to
homotopy".

## 2. Definitions

**Definition 2.1 (de Rham twist).**  For an object `K` of the localized sector
put `K_{dR}:=K\hat\otimes\Omega_{dR}`, where
`\Omega_{dR}=(S\xrightarrow{D}S\,dt)` is the tangential complex in degrees
`0,1`, with orientation trace `t(f\,dt)=\int_Yf\,dx`.

This is the same twist that already appears inside the dagger (4.7) of
A125.001.  The two clauses therefore use one normalization, not two.

**Definition 2.2 (the trace-class domain).**
\[
\boxed{
 Corr_A^{tr}:=\{\,K\ \text{in the localized sector}\ :\
 K_{dR}\ \text{is perfect over the outer algebra}\,\}, }              \tag{2.1}
\]
"perfect" meaning homotopy equivalent, `B`-linearly, to a bounded complex of
finite projective modules, i.e. an object of `P_e(J)` in the sense of
P123.095 §1.

**Definition 2.3 (the target and the trace).**
\[
 T_A:=\{\text{graded line bundles on }B_q\}\times\mathbb Z^{\pi_0(B_q)},
 \qquad
 \mathrm{Tr}_A(K):=\bigl(\mathrm{Det}_e(K_{dR}),\ \deg(K_{dR})\bigr).  \tag{2.2}
\]

## 3. The properties required by A.5

**Theorem 3.1.**  With Definitions 2.1–2.3:

1. **Nonvacuity, and the diagonal is in the domain.**  `Δ=U` lies in
   `Corr_A^{tr}`: indeed `U_{dR}=M_{dR}=B\hat\otimes\Omega_{dR}\simeq_B
   B^{r}[0]\oplus B^{r}[-1]` is perfect, with an explicit `B`-linear homotopy.
2. **Closure under composition.**  `Corr_A^{tr}` is closed under `\star`, and
   under finite sums, shifts, cones and retracts.
3. **Additivity.**  `\mathrm{Tr}_A(\mathrm{Cone}f)=\mathrm{Tr}_A(L)\otimes
   \mathrm{Tr}_A(K)^{-1}`, and acyclic objects are canonically trivialized, so
   `\mathrm{Tr}_A` descends through quasi-isomorphisms of the domain.
4. **Cyclicity.**  `\mathrm{Tr}_A(M\star N)\cong\mathrm{Tr}_A(N\star M)`.
5. **Determinant and source-trace compatibility.**  `\mathrm{Tr}_A` is by
   construction a determinant, and its degree component satisfies
   `\deg(K_{dR})=\sum_i(-1)^i\mathrm{Tr}_{\rm source}(\mathrm{id})` together
   with the Jacobi identity for logarithmic derivatives.
6. **Restriction compatibility and finiteness.**  `\mathrm{Tr}_A` is
   independent of the normalized compact cutoff, coherently for triples, and
   `\deg` is a locally constant integer-valued function on `B_q`.

*Proof.*  (1) is the perfectness of `M_{dR}` proved in `A_DUALITY_WORK.md`
together with the finite retract `H=K_0\otimes\Lambda(dt)`, `r=\dim K_0<\infty`
from P123.119.  It is exactly the statement that the recorded gap of P123.095
§5 is repaired for the diagonal by the tangential differential: without the
differential the middle factor is `S`, with it the middle factor is the finite
`H`.

(2) For a composition the middle variables contribute
`\Omega_{dR}^{\hat\otimes n}`, and `A_DUALITY_WORK.md` proves
`\Omega_{dR}^{\hat\otimes n}` is homotopy equivalent to `H^{\otimes n}`, the
contraction being built successively from the individual contractions and
projections with the graded tensor signs, with only finitely many factors, so
every map is continuous.  A finite tensor of perfect complexes over `B` is
perfect.  Stability under sums, shifts, cones and retracts is (1.1)'s cone law
together with the stability of `P_e(J)` under those operations (P123.095 §1).
This is precisely where the counterexample of §1 is avoided: the failure there
was the non-perfect middle factor `S`, replaced here by `H`.

(3) is the cone law and the acyclic trivialization of P123.095 §2, whose proof
uses that images are subbundles with locally constant rank and no closed-image
assertion for arbitrary Fréchet complexes.

(4) is P123.122 (5) transported through `\mathrm{Det}_e`: the cyclic rotation
is an isomorphism of the underlying complexes, and (3) makes
`\mathrm{Det}_e` invariant under isomorphism.

(5) is P123.095 (4)–(5) verbatim; (6) is its §4 cutoff independence, which
uses the partial isometries `V_{d,c},V_{c,d}` of P123.090 lying in the
orbit-decay ideal by P123.092.  QED

**Corollary 3.2.**  Clause A.5 holds on `Corr_A^{tr}` in the exact sense it
demands: a declared trace-class domain, a determinant/perfect-complex target,
additivity, cyclicity, restriction and determinant compatibility, and a finite
scalar degree.  The value on a future `Γ_n` is not part of the clause and is
not asserted.

## 4. Compatibility with A.4 and A.3

The dagger of A125.001 and the domain (2.1) use the same de Rham twist, and
`\Omega=M_{dR}` is the dualizing object of both.  Hence `Corr_A^{tr}` is
`†`-stable in the following sense: if `K_{dR}` is perfect then
`[K_{dR},\Omega]` is perfect, because a dual of a perfect complex over `B` is
perfect and `\Omega` is perfect by Theorem 3.1(1).  Therefore

\[
        K\in Corr_A^{tr}\ \Longrightarrow\ K^{\dagger}\in Corr_A^{tr},
\]

and `\mathrm{Tr}_A(K^{\dagger})\cong\mathrm{Tr}_A(K)^{-1}` by the cone law
applied to the dualizing pairing.

The interaction with A125.002 is less comfortable and is stated plainly.
Theorem 3.2 of that note gives two-sided excision on the ideal-generated
sector but not on the profile objects.  Since `Corr_A^{tr}` is `†`-stable, it
contains profile objects whenever it contains the corresponding ideals.  The
two clauses are therefore simultaneously satisfied only on

\[
        Corr_A^{tr}\ \cap\ \{\text{objects with }
        (-)\hat\otimes_UI_O\hat\otimes_U(-)\ \text{killed by }B_O\},
\]

and proving that this intersection is large enough to carry rows B and C is an
obligation this note does not discharge.  It is the sharpest form of the
tension recorded in A125.002 §4.

## 5. The one conditional input

Definition 2.1 uses the tangential complex on the boundary as the middle
factor.  Treating `\mathrm{Tr}_A` as the shadow of the **source**
correspondences presupposes the comparison that `A_DUALITY_WORK.md` states as
outstanding: "prove that a specified source pushforward is computed by this
relative complex and that its dualizing normalization and determinant agree
with the arithmetic category".  Until that is proved, Theorem 3.1 is a theorem
about the de Rham-twisted objects, and its reading as the diagonal shadow of
the source is `CONDITIONAL`.  This is the same single conditional input as in
A125.001 §6; the two notes do not multiply hypotheses.

## 6. Ledger

| statement | status |
|---|---|
| Def. 2.1–2.3: first definition of `Corr_A^tr` and `T_A` in the corpus | `CONSTRUCTED` |
| Thm 3.1(1): the diagonal lies in the domain; repairs the P123.095 §5 gap | `PROVED-IN-REPOSITORY` |
| Thm 3.1(2): closure under composition; avoids the perfect-kernel counterexample | `PROVED-IN-REPOSITORY` |
| Thm 3.1(3)–(6): additivity, cyclicity, determinant/source-trace, restriction, finite degree | `PROVED-IN-REPOSITORY` |
| Cor. 3.2: clause A.5 on `Corr_A^tr` | `PROVED-IN-REPOSITORY`, `CONDITIONAL` on §5 |
| `†`-stability of the domain | `PROVED-IN-REPOSITORY` |
| joint A.3/A.5 domain large enough for B and C | `OPEN` (§4) |
| source-pushforward comparison | `OPEN`, shared with A125.001 |
