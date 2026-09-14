# A125.007 — effectivity, its descent, and properness of the cone (clause A.7)

Status: `PROVED-IN-REPOSITORY` on the graph sector `\mathcal G` of A125.006.
Clause A.7 asks for a functorial cone or exact positive class constructed from
the source geometry, descending to the numerical theory to the extent Riemann
–Roch needs, and **not** defined using positivity of the Weil form.  No
RH-side input is used.

## 1. A recorded refutation that does not apply

Ledger row `C1` is `REFUTED`: source squares are not effective graph cycles,
with an explicit two-point counterexample (P123.021).  That refutation has
been carried in the audits as an obstruction to A.7.  It is not one.

What `C1` refutes is the **identification**

\[
 \mathrm{Eff}\ \overset{?}{=}\ \overline{\{\textstyle\sum_iX_i^{\dagger}X_i\}},
 \tag{1.1}
\]

i.e. the attempt to define effectivity as a sum-of-squares cone.  Clause A.7
never asks for (1.1); it asks for a cone constructed from the source geometry
and explicitly forbids defining it from a form's sign, which is exactly what
(1.1) would smuggle in.  So `C1` is evidence **for** the route taken here, not
against it.  P123.074 makes the same point in its own words: the cone
constructed there "is intrinsic to the represented graph measures, rather than
selected from an eventual quadratic-form sign", and it is "not the
positive-semidefinite operator cone", the witness being the effective
permutation kernel exchanging two points, which is self-adjoint with
eigenvalues `1` and `-1`.

## 2. The cone

**Definition 2.1.**  A graph element `b=(b_\gamma)` is **effective** if every
coefficient `b_\gamma` is a real nonnegative function.  Let
`\mathrm{Eff}_A\subseteq\mathcal G` be the set of objects representable by a
bounded complex whose terms are effective, with `\mathrm{Eff}_A` extended to
`\mathcal G` by finite sums and nonnegative real scaling.

**Theorem 2.2 (IMPORTED, hypotheses checked).**  `\mathrm{Eff}_A` is

1. intrinsic: positivity of all half-density row measures is equivalent to
   coefficient nonnegativity, on the dense set where the atoms are distinct
   and hence everywhere by continuity;
2. closed in the rapid topology, and closed under addition and nonnegative
   real scaling;
3. preserved by composition, since each crossed coefficient is a convergent
   sum of products of nonnegative functions;
4. preserved by the dagger, by the half-density adjoint formula
   `\Pi(b,a)^{*}=\Pi(\beta_a^{-1}(b^{*}),a^{-1})`;
5. preserved by gauge changes and by the repaired coefficient chart maps.

*Proof.*  This is P123.074, whose statements (1)–(5) are exactly the above.
Its half-density normalization is the one fixed in A125.001 (4.1)–(4.2), so
(4) is the dagger of this campaign and not a different involution.  QED

**Proposition 2.3.**  Every graph class lies in the cone:
`E_w\in\mathrm{Eff}_A` for every external idele class `w`.

*Proof.*  In the kernel realization of P123.073, `E_w` is `T_{1,w}`, with the
single coefficient `b_1=1`, a nonnegative constant function, and all other
coefficients zero.  QED

## 3. Descent to the numerical theory

**Theorem 3.1.**  The image of `\mathrm{Eff}_A` in `N_A=\mathcal G/\mathcal N`
is a closed convex cone, stable under `\star` and `†`.

*Proof.*  Convexity and stability are Theorem 2.2(2)–(4), and the quotient map
is linear, continuous and open onto its image.  The image is closed because
`\mathcal N` is closed (A125.004 Theorem 2.2(1)) and the cone is closed and
invariant under translation by `\mathcal N`: if `b\in\mathrm{Eff}_A` and
`n\in\mathcal N` then pairing `b+n` against any test reproduces the pairing of
`b`, so membership of the class is well defined.  QED

## 4. Properness

P123.010 left properness of the effective cone after the numerical completion
open.  On the graph sector it is now a consequence of the fixed-point
dichotomy.

**Theorem 4.1.**  The image of `\mathrm{Eff}_A` in `N_A` is a **proper** cone:
it contains no line.  Equivalently, if a class and its negative are both
effective, the class is zero.

*Proof.*  By A125.006 (1.2) the pairing on graph classes is

\[
 \langle E_u,E_v\rangle=\delta(uv^{-1})
 =\begin{cases} r,& uv^{-1}\ \text{acts with fixed points},\\
 0,&\text{otherwise},\end{cases}
 \qquad r>0 .                                                  \tag{4.1}
\]

Let `x=\sum_va_v[E_v]` with all `a_v\ge0` be effective, and suppose `-x` is
also effective, so `x` and `-x` are both nonnegative combinations.  Pair `x`
against a single graph class `E_w`:

\[
 \langle x,E_w\rangle=r\sum_{v\,\in\,w\cdot\ker}a_v\ \ge\ 0 ,
\]

while the same computation for `-x` gives `\le0`.  Hence every such sum
vanishes, and since all `a_v\ge0` and `r>0`, every `a_v=0`.  Therefore `x=0`
in `N_A`.  QED

**Corollary 4.2 (clause A.7).**  On `\mathcal G` there is a functorial,
source-defined, closed, `\star`- and `†`-stable effective cone, containing all
graph classes, descending to `N_A` and proper there.  It is constructed
without using positivity of the Weil form, and the recorded refutation `C1`
does not apply to it.

## 5. What is not claimed

Properness is not a Hodge-index statement and implies no sign for any
primitive class: (4.1) is a computation of a Gram matrix on the graph
classes, not an assertion about the mixed sector's signature, and clause A.7
explicitly does not supply a sign.  Row D's obligations are untouched.

Nor is `\mathrm{Eff}_A` claimed to be the set of all classes with nonnegative
pairing against everything effective, i.e. no self-duality of the cone is
asserted; that would be a further theorem and is not needed by A.7.

Finally, the descent proved here is "to the extent needed by Riemann–Roch"
only once A.8 fixes what Riemann–Roch needs.  That is A125.008.

## 6. Ledger

| statement | status |
|---|---|
| §1 `C1` refutes the sum-of-squares identification (1.1), not the cone | `PROVED-IN-REPOSITORY` |
| Thm 2.2 cone intrinsic, closed, `⋆`- and `†`-stable, chart invariant | `IMPORTED` from P123.074, hypotheses checked |
| Prop. 2.3 graph classes are effective | `PROVED-IN-REPOSITORY` |
| Thm 3.1 descent to `N_A` | `PROVED-IN-REPOSITORY` |
| Thm 4.1 properness; closes the P123.010 open item on `\mathcal G` | `PROVED-IN-REPOSITORY` |
| Cor. 4.2 clause A.7 on `\mathcal G` | `PROVED-IN-REPOSITORY` |
| cone self-duality; A.8 | `OPEN` |
