# A125.005 — correction: the boundary determinant degenerates on graph classes, and what `T_A` must be

Status: `PROVED-IN-REPOSITORY` for Theorem 1.1 (a degeneration theorem, i.e. a
no-go).  It **corrects** A125.003 Definition 2.3 and A125.004 Definition 1.1,
which are hereby restricted, and it identifies the corrected target.  No
RH-side input is used.

## 1. The degeneration

A125.003 proposed `T_A=\{\text{graded line bundles on }B_q\}` with
`\mathrm{Tr}_A(K)=\mathrm{Det}_e(K_{dR})`, and A125.004 built the numerical
pairing from it.  That target is too coarse.

**Theorem 1.1.**  For every external idele class `u`,

\[
        \mathrm{Det}_e\bigl((E_u)_{dR}\bigr)\ \cong\ \mathcal O_{B_q},
        \tag{1.1}
\]

the trivial graded line.  Consequently `\delta` of A125.004 (4.2) is constant,
every graph class is numerically equivalent to the diagonal, and the whole
graph sector lies in the radical `\mathcal N`.

*Proof.*  By A125.003 Theorem 3.1(1),
`\Delta_{dR}=M_{dR}\simeq_BB^{r}[0]\oplus B^{r}[-1]` with `r=\dim K_0`, a
`B`-linear homotopy equivalence.  Hence

\[
 \mathrm{Det}_e(\Delta_{dR})
 =(\det B^{r})\otimes(\det B^{r})^{-1}\cong\mathcal O_{B_q},
\]

the two degrees contributing inverse lines because they have equal rank, which
by A125.004 Remark 1.1a is forced by the degree-one perfect pairing (4.4) of
A125.001.  For `E_u`, untwisting along `\beta_u` is an exact equivalence
carrying `(E_u)_{dR}` to `\Delta_{dR}`, over the automorphism of `B_q` induced
by the dilation.  Determinant lines pull back along that automorphism, and the
pullback of a trivial line is trivial, giving (1.1).  The remaining assertions
follow from A125.004 (4.2) and Definition 2.1 there.  QED

**Corollary 1.2.**  With the target of A125.003 Definition 2.3, the quotient
`N_A` of A125.004 carries no nonzero graph class.  The mixed-sector
requirement of clause A.6 cannot be met inside that target.

## 2. Why it degenerates, and what survives

The failure is structural and worth naming precisely, because it disqualifies
a whole family of candidate targets rather than one formula.

`\mathrm{Det}_e` is a class of a bundle on the compact boundary `B_q`.  An
arithmetic twist `\beta_u` acts on `B_q` by an automorphism.  Any invariant of
a complex that is defined as an isomorphism class of bundles is therefore
transported, not changed, by the twist: it can only see the geometry of the
graph, and every graph is isomorphic to the diagonal.  So no isomorphism-class
invariant of bundles on `B_q` can separate `E_u` from `\Delta`.

What does **not** degenerate is the part of the corpus's determinant theory
that was built to have an anomaly:

* P123.107 constructs the full normal relative determinant germ with
  quantitative convergence;
* P123.108 proves its composition law **with a finite endpoint anomaly**,
  establishes the cocycle identity and exhibits an explicit nontrivial
  `1/(1-st)` example;
* P123.110 proves the coupled analytic composition law via a trace-class
  endpoint correction, with cocycle, adjoint and semilocal compatibility;
* P123.111 computes the mixed anomaly as an exactly stabilized endpoint trace,
  with a Hermitian cutoff-escape interpretation.

The distinguishing datum is exactly the **anomaly cocycle**: it is the failure
of the relative determinant to be multiplicative under composition, and it is
what a pullback along an automorphism does not kill, since it is attached to
the composition law and not to an object.  P123.108's explicit nontrivial
example is the proof that this cocycle is not a coboundary in general.

## 3. The corrected requirement on `T_A`

Everything proved in A125.003 Theorem 3.1 about additivity, cyclicity,
restriction compatibility, finite degree, `†`-stability and closure of
`Corr_A^{tr}` under composition stands: those statements do not use which
determinant target is chosen, only the cone law and the finite middle factor.
What is withdrawn is the identification of the target.

**Requirement 3.1 (corrected `T_A`).**  `T_A` must be a target in which the
relative determinant germ of P123.107–110 lands **together with its anomaly
cocycle**, i.e. a determinant torsor over the composition law, not a group of
isomorphism classes of bundles.  It must satisfy:

1. the cone law and acyclic trivialization, so that A125.003
   Theorem 3.1(3)–(4) survive verbatim;
2. the composition law of P123.108 including its endpoint anomaly, so that
   `\langle E_u,E_v\rangle` depends on `uv^{-1}` through the cocycle and not
   only through the graph geometry;
3. compatibility with the half-density normalization of A125.001 (4.1), so
   that `†` acts on it by the Rosati swap of P123.008;
4. cutoff independence in the sense of P123.095 §4.

Under Requirement 3.1, A125.004 (4.2) is replaced by: the mixed numerics of
the graph sector is the **anomaly class** of `\delta`, and the mixed sector is
nonzero if and only if that cocycle is not a coboundary on the idele class
group.  P123.108's nontrivial `1/(1-st)` example is evidence that this is the
right place to look; it is not yet a proof for the semilocal cocycle, which
P122.017 separately proved splits prime by prime for the **native** Bohr
determinant cocycle.  The two statements are about different cocycles and must
not be conflated: P122.017 concerns the finite Euler determinant carrier with
no Gamma coupling, while Requirement 3.1(2) concerns the coupled relative
determinant of P123.110, whose anomaly is an endpoint trace.

## 4. Status changes

| item | before | after |
|---|---|---|
| A125.003 Def. 2.3 target `T_A=Det_e` | `CONSTRUCTED` | `RETRACTED` as the numerical target; retained as a valid determinant on the boundary corner |
| A125.003 Thm 3.1 (1),(2),(3),(4),(5),(6) | `PROVED` | unchanged; independent of the target's identification |
| A125.003 Def. 2.2 domain `Corr_A^tr` | `CONSTRUCTED` | unchanged |
| A125.004 Def. 1.1 pairing | `CONSTRUCTED` | `CONDITIONAL` on Requirement 3.1 |
| A125.004 Thm 2.2, 3.2 (radical closed/ideal/`†`-stable; `N_A` Hausdorff) | `PROVED` | unchanged; the proofs use only the cone law and cyclicity |
| A125.004 Thm 3.3 ruling plane | `PROVED` | **restricted**: it is proved for the finite Tate realization `ρ_T` into `B_T=C⊕C` of P123.008, which is a different target from `Det_e`; its transport into the corrected `T_A` is `OPEN` |
| A125.004 Thm 4.1 graph classes in the domain | `PROVED` | unchanged |
| A125.004 Cor. 4.2 mixed sector reduces to one line | superseded | replaced by: reduces to the anomaly cocycle of the coupled relative determinant |
| clause A.6 | partially constructed | `OPEN` at the mixed sector, with the target now specified by Requirement 3.1 |

The campaign is not left worse off.  Before this note the mixed sector was an
unlocated gap; after it, the gap is located in a single object that the corpus
has already constructed and proved nontrivial in an explicit local example.
What changed is that the correct invariant is a **cocycle attached to the
composition law**, not a class attached to an object.  Theorem 1.1 is the
proof that no object-level invariant on the boundary can serve.
