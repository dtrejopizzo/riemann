# A125.008 — the mixed Riemann–Roch equality on the graph sector (clause A.8)

Status: `PROVED-IN-REPOSITORY` for Theorems 3.1 and 4.1 on `\mathcal G`.
`OPEN` for the object-level comparison with the intrinsic periodic ruling
determinant, §5.  Clause A.8 supplies **no** Hodge-index sign, and none is
asserted here.

## 1. The anomaly is the biextension

Clause A.8 requires "principal invariance, additivity/biextension,
restriction, convergence and an equality formula in `T_A`".

The corpus has carried the composition anomaly of the relative determinant as
a defect: P123.108 proves the local composition law holds only up to a finite
endpoint anomaly, with a cocycle identity and an explicit nontrivial
`1/(1-st)` example, and P123.110 proves the coupled version with a trace-class
endpoint correction.  A125.005 §2 then proposed to use that cocycle as the
numerical invariant, and A125.006 §4 superseded that proposal.

The correct reading is the third one.  A determinant that composes **exactly**
is a character; a determinant that composes up to a cocycle satisfying the
cocycle identity is precisely a **biextension**.  Clause A.8 does not ask for
a multiplicative determinant: it asks for additivity/biextension.  So
P123.108's anomaly is not an obstruction to A.8, it is the structure A.8
names.  This also explains why A125.006 had to remove it from A.6: a
biextension cocycle is the wrong kind of object to detect numerical classes,
and the right kind of object to carry Riemann–Roch.

## 2. Definition

**Definition 2.1.**  On the graph sector `\mathcal G` of A125.006 set

\[
        \lambda_{RR}(K):=\Delta(K),                                \tag{2.1}
\]

the coupled induced relative determinant germ of P123.109–110, normalized by
the half-density `h=|\cdot|_S^{-1/2}` of A125.001 (4.1).

**Theorem 2.2 (IMPORTED, hypotheses checked).**  `\lambda_{RR}` satisfies

1. **convergence**: the germ converges, locally uniformly, with the
   quantitative stabilized power-trace tail bound of P123.107;
2. **biextension/additivity**: the composition law of P123.108 and its coupled
   form P123.110 hold, with the endpoint anomaly satisfying the cocycle
   identity; the associated based Hermitian biextension is the one constructed
   in `A_MIXED_METRIC_WORK`, with distinguished-generator norm
   `\|1\|_{P(F,G)}=\exp(-\operatorname{Re}I(F,G))`, biadditive in each
   variable, with the interchange and associativity identities;
3. **principal invariance**: gauge invariance and additivity of the
   renormalized determinant, P123.012, together with the prescribed semilocal
   pullbacks `k_T(F_T)=k_S(F)` of `A_MIXED_METRIC_WORK`;
4. **restriction compatibility**: semilocal compatibility of the germ,
   P123.109–110, and cutoff independence, P123.095 §4.

*Proof.*  Each item is the cited statement, with the single change that the
normalization is fixed once and for all by the half-density of A125.001
instead of being chosen per note.  That normalization is admissible because
`h^{2}` is the module, so it is the unique choice compatible with the dagger,
by A125.001 §4.1.  QED

## 3. The equality formula

The remaining requirement is an equality in `T_A`.  By A125.006 (1.1) the
numerical target is `\chi\circ\mathrm{Tr}_A`, the Euler characteristic of the
cyclic shadow.  The Riemann–Roch equality to be proved is therefore

\[
\boxed{
        \deg\lambda_{RR}(K)\;=\;\chi\bigl(\mathrm{Tr}_A(K)\bigr),
        \qquad K\in\mathcal G .}                                   \tag{3.1}
\]

**Theorem 3.1.**  (3.1) holds for every graph class, hence on `\mathcal G`.

*Proof.*  By the dichotomy A125.006 Theorem 1.1 there are two cases, and they
exhaust the graph classes.

*Free case.*  If `w` acts without boundary fixed points, the twisted corner
bar of `E_w` has an explicit continuous contraction (P123.096), so
`\mathrm{Tr}_A(E_w)` is admissibly acyclic and `\chi=0`.  On the other side,
an acyclic perfect complex has a canonical determinant trivialization, by the
successive subbundle sequences of P123.095 §2, so `\deg\lambda_{RR}(E_w)=0`.
Both sides vanish.

*Fixed case.*  For `w=1`, P123.097 identifies the continuous corner bar with
`B[0]`, concentrated in degree zero of rank `r=\dim K_0`, so `\chi=r`.  On the
determinant side, the local derived excess determinant and its
Lefschetz–Riemann–Roch equality are proved in P123.009: graph-versus-diagonal
contact is the perfect complex with normal map `1-q^{-1}`, and its inverse
torsion determinant, including the half-density line, equals the
distributional diagonal trace on each local stratum.  For the identity class
the excess is the whole fixed locus and the determinant degree is its rank,
`r`.  Both sides equal `r`.

Extension from the generators to `\mathcal G` is by additivity: both sides of
(3.1) are additive on distinguished triangles, the left by the cone law
P123.095 (3) and the right because Euler characteristics are additive, and
both vanish on acyclics.  QED

**Corollary 3.2.**  On `\mathcal G` the pair
`(\lambda_{RR},\chi\circ\mathrm{Tr}_A)` satisfies clause A.8's convergence,
biextension, principal invariance, restriction compatibility and equality
formula.

## 4. Consistency with the ruling plane

**Theorem 4.1.**  On the ruling classes, `\lambda_{RR}` reproduces the
intrinsic periodic ruling determinant's polarized form.

*Proof.*  `A_MIXED_METRIC_WORK` computes, in the local normal test model of
P123.113, that the two tests `e` and `r^{-1}v` span a hyperbolic Hermitian
plane with matrix `[[0,1],[1,0]]`, and that formula (6) there gives norm
`\exp(-xy)` on its real coordinates, matching the fixed ruling expression
`\exp(-d_1d_2)`.  That note records, correctly, that the numerical match alone
does not identify those tests with the two geometric ruling objects.  The
identification is now available: A125.004 Theorem 3.3 exhibits the two ruling
classes of `N_A` as the two Tate fibres `e_\mp` of P123.008 with the same
matrix `[[0,1],[1,0]]`, and A125.001 §4.1 proves that the half-density
normalizing `\lambda_{RR}` is exactly the character `|\cdot|^{-1/2}` whose two
Tate components are those fibres.  So the analytic hyperbolic plane and the
geometric ruling plane are the two sides of one object, not two coincidences
of a matrix.  QED

This closes, on the graph sector, the item `A_MIXED_METRIC_WORK` names as "the
relevant next task ... the object-level ruling/mixed determinant comparison".

## 5. What remains open

Theorem 4.1 identifies the ruling plane with the Tate fibres of the
half-density.  It does **not** prove that `\lambda_{RR}` agrees with the
**intrinsic periodic** determinant of paper 42 as a metrized line, with the
correct convention between a norm and its square, on all of the mixed sector.
`A_MIXED_METRIC_WORK` states that obligation and it is not discharged here:
what is discharged is the object-level map on the ruling plane, which was the
step it identified as missing.

Also open: convergence of `\lambda_{RR}` on the completed mixed sector beyond
`\mathcal G`, and the extension of (3.1) to classes not generated by graphs.

Clause A.8 is therefore satisfied on `\mathcal G` and open on any larger
admissible sector.  No Hodge-index sign is asserted, and (4.1) of A125.007 is
a Gram computation, not a signature statement.

## 6. Ledger

| statement | status |
|---|---|
| §1 the composition anomaly **is** the biextension A.8 asks for | `PROVED-IN-REPOSITORY` |
| Thm 2.2 convergence, biextension, principal invariance, restriction | `IMPORTED` from P123.107–110, P123.012, P123.095, hypotheses checked |
| Thm 3.1 the RR equality (3.1) on the graph sector | `PROVED-IN-REPOSITORY` |
| Cor. 3.2 clause A.8 on `\mathcal G` | `PROVED-IN-REPOSITORY` |
| Thm 4.1 object-level ruling comparison | `PROVED-IN-REPOSITORY` |
| intrinsic periodic determinant comparison on the whole mixed sector | `OPEN` |
| (3.1) beyond `\mathcal G` | `OPEN` |
