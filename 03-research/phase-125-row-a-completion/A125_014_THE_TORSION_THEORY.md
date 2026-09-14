# A125.014 — additive numerics are degenerate; the Weil-strength theory is the torsion theory

Status: `PROVED-IN-REPOSITORY` for Theorems 1.1, 3.1(a)–(b), 5.1, 6.1 and
7.1; `IMPORTED` with hypothesis maps for the local computations of
Theorem 3.1(c)–(d) and for the regularization of §4, each anchored to an
explicit proved model in phase 123.  This note supersedes the gate `(F)` of
A125.012 and is the closure of row A on `G`.

No `Λ(n)`, no distinguished `Γ_n` beyond its realization as a twist, no
explicit formula, no zero of zeta, no RH and no positivity of `B_nuc` is used.

## 1. The full shadow is acyclic on every nontrivial class

A125.012 proposed to repair the boundary theory by passing to the full
relative cyclic shadow `\mathrm{Tr}_A` of P123.122 (4) and asked, as gate
`(F)`, for its perfectness and fixed-point decomposition.  The decomposition
is proved below (Theorem 3.1), and it yields a stronger and more useful fact
than `(F)` anticipated.

**Theorem 1.1.**  For every external idele class `w\notin\Gamma`, the full
shadow `\mathrm{Tr}_A(E_w)` is admissibly acyclic over `\mathbb C`.  Hence
`\chi(\mathrm{Tr}_A(E_w))=0`, and more generally **every** numerical invariant
of `E_w` that factors through the isomorphism class of the complex, its
cohomology, ranks or Euler characteristic vanishes identically on
`G\setminus\{\text{shifts and sums of }\Delta\}`.

*Proof.*  By Theorem 3.1 below, `\mathrm{Tr}_A(E_w)` is a rapid direct sum
over `\gamma\in\Gamma` of complexes each of which is a completed tensor over
places of local complexes for the dilation `\sigma=\gamma w`.  For
`w\notin\Gamma` every `\sigma=\gamma w` is a nontrivial external class, so
either it is nontrivial at some finite place, where the local complex is the
transverse fixed complex `[\mathbb C\xrightarrow{\sigma_p-1}\mathbb C]`,
contractible because `\sigma_p\neq1`; or it is trivial at all finite places
and hence has `|\sigma|_\infty\neq1`, where the real local complex is the
boundary corner bar of a free translation, contractible by P123.096.  A
completed tensor with a contractible factor is contractible with the tensor
of the contractions, and a rapid direct sum of contractible complexes with
uniformly bounded contractions is contractible.  QED

**Corollary 1.2 (no additive numerical theory is Weil-strength).**  Any
numerical pairing on `G` defined through `\chi`, ranks, or the isomorphism
class of the shadow — including the gate `(F)` of A125.012 and the boundary
theory `A^\partial` — is identically zero off the diagonal.  The
Euler-characteristic dichotomy of A125.006 is the special case of
Theorem 1.1 in which only the boundary summand is retained.

Corollary 1.2 is the exact form of the complaint recorded in P123.037 and
P123.038, "complexification still kills the finite torsion", now proved for
the whole shadow functor rather than observed on a model.  It also explains
P123.084 (degree-zero continuous shadows vanish away from the origin) and
P123.070 (the unit's shadow is infinite, never perfect): the only classes with
nonacyclic shadow are the diagonal and its multiples, and there the shadow is
infinite-dimensional.

## 2. The invariant that survives complexification

An acyclic bounded complex of finite-dimensional spaces `V^\bullet` with
**fixed bases** has a nonzero scalar invariant, its torsion
`\tau(V^\bullet)\in\mathbb R_{>0}`, the alternating product of the
determinants of the differentials in the given bases.  For a two-term complex
`[\mathbb C\xrightarrow{m}\mathbb C]` with standard bases, `\tau=|m|`.
Complexification of `[\mathbb Z\xrightarrow{m}\mathbb Z]` kills
`H^0=\mathbb Z/m` but not `\tau=|m|=\#H^0`.  This is the observation the
corpus already made in one instance, P123.039 (1.1):

```text
det(1-T|V_n)=Phi_n(1)>0,     log #H^0(D_n)=log det(1-T|V_n),
```

"after complexification `D_n` is acyclic, but its integral model still
specifies the torsion determinant.  Its ordinary categorical supertrace is
zero."

The bases are not a choice here.  Every local complex of Theorem 3.1 is a
Koszul complex for the fixed locus of a dilation, and its terms carry the
canonical half-density normalization `|\cdot|^{-1/2}` of P123.074 — the same
half-density that fixes the dagger (A125.001 §4.1, A125.011 §2).  With that
normalization the torsion of the transverse fixed complex at a finite place
`p` for a dilation `\sigma_p\neq1` is

\[
\boxed{
 \tau_p(\sigma)=\frac{|\sigma_p|_p^{1/2}}{|1-\sigma_p|_p},}          \tag{2.1}
\]

the "analytic normal Jacobian" of P123.060 §2, equal to `p^{-k/2}` for
`\sigma_p=p^{k}`.  The numerator is the half-density, the denominator is the
determinant of the fixed differential.  P123.060 §4 identifies (2.1) as
"exactly what the local Fourier trace sees transversely".

**Definition 2.1.**  The Weil-strength numerical invariant of row A is the
half-density-normalized **log-torsion** of the full shadow,

\[
 T(K):=\log\tau\bigl(\mathrm{Tr}_A(K)\bigr),
\]

made precise in §4.  It is multiplicative where `\chi` is additive: on a
direct sum of acyclic complexes torsions multiply, so `T` adds; on an acyclic
complex `T` is the log-determinant, not zero.

## 3. The decomposition theorem

Let `U=(E_P\oplus\mathbb C1)\rtimes\Gamma_P` with
`E_P=E_{\mathbb R}\hat\otimes\bigotimes_pE_p` (P123.121 (6),(8)), and let
`w` be an external class; `\beta_w` commutes with the lattice action.

**Theorem 3.1.**  There are natural isomorphisms in the relative derived
category, with rapid direct sums and completed tensors:

*(a) label splitting.*
\[
 \mathrm{Tr}_A(E_w)\ \cong\ \widehat{\bigoplus_{\gamma\in\Gamma}}\
 \mathcal K_\Gamma\ \hat\otimes\ HH\bigl(E_P^u,\ (E_P^u)_{\gamma w}\bigr),
 \tag{3.1}
\]
where `HH(C,C_\sigma)` is the relative Hochschild complex of the coefficient
algebra with coefficients twisted by `\sigma`, and `\mathcal K_\Gamma` is the
deck Koszul complex of `\Gamma\cong\mathbb Z^{d}`.

*(b) Künneth over places.*
\[
 HH\bigl(E_P^u,(E_P^u)_\sigma\bigr)\ \cong\
 HH(E_{\mathbb R},(E_{\mathbb R})_{\sigma_\infty})\ \hat\otimes\
 \widehat{\bigotimes_p}\ HH(E_p,(E_p)_{\sigma_p}).                    \tag{3.2}
\]

*(c) finite places.*  If `\sigma_p=1`, `HH(E_p,E_p)\simeq E_p[0]`.  If
`\sigma_p\neq1`, `HH(E_p,(E_p)_{\sigma_p})\simeq[\mathbb C\xrightarrow{\sigma_p-1}\mathbb C]`
concentrated at the fixed point `x_p=0`, contractible, with half-density
torsion (2.1).

*(d) the real place.*  If `\sigma_\infty=1`,
`HH(E_{\mathbb R},E_{\mathbb R})\simeq(E_{\mathbb R}\xrightarrow{D}E_{\mathbb R}\,dt)`,
the tangential de Rham complex.  If `\sigma_\infty` is a translation by
`\log|\sigma|\neq0`, the complex is the boundary corner bar of P123.094 and
is contractible by P123.096.

*Proof.*  (a) An elementary tensor of `E_w\hat\otimes U^{\hat\otimes n}` has a
total label, the product of its lattice labels; since `\Gamma` is abelian and
`\beta_w` fixes each `U_\gamma`, the Hochschild boundary — including the
cyclic term, which moves the last factor through `\beta_w` — preserves the
total label.  So the complex is the rapid direct sum of its total-label
pieces.  On the label-`\gamma` piece, the standard reduction collapses the
group factors onto a single `U_\gamma`, leaving the coefficient complex with
coefficients twisted by `\gamma w` tensored with the group homology of
`\Gamma`; for `\Gamma=\mathbb Z^{d}` the latter is the finite deck Koszul
complex, which is the "coefficient deck descent for every semilocal zero
stratum" of `A_DUALITY_WORK` and P123.121.  Continuity of the collapse maps is
the crossed comparison of P123.123 (8)–(11).

(b) `E_P^u` is a completed projective tensor of nuclear Fréchet algebras
(P123.121), the bar complexes are K-flat on either side (P123.122 §3), and
`\sigma` acts coordinatewise; the Eilenberg–Zilber shuffle map is a continuous
homotopy equivalence between the bar of the tensor and the tensor of the bars
under these hypotheses, giving (3.2).

(c) `HH(C,C_\sigma)=C\hat\otimes^L_{C\hat\otimes C}C_\sigma` is the derived
intersection of the diagonal with the graph of `\sigma`.  P123.066 constructs
the continuously contracted relative bar and the completed derived diagonal;
P123.060 (1.1) computes the derived intersection of the diagonal with the
graph of a dilation by its one-term Koszul resolution: the fixed scheme is cut
out by `(\sigma_p-1)x_p`, giving `[\,\cdot\xrightarrow{\sigma_p-1}\cdot\,]`
supported at `x_p=0`, with the half-density factor from the dilation action,
i.e. (2.1).  For `\sigma_p=1` the graph is the diagonal and the locally
constant coefficient algebra has no higher Hochschild homology, since it is
the completion of a union of finite-dimensional semisimple algebras with
uniformly continuous contractions; this is the finite-place half of
P123.118's vanishing `H_n=0`, `n\ge2`.

(d) The identity case is the Hochschild–Kostant–Rosenberg computation proved
for the smooth boundary source in P123.118, `H_0=S`, `H_1=S\,dt`, `H_n=0` for
`n\ge2`, with P123.119's strict projection to the tangential de Rham complex.
The translation case is the corner-bar contraction of P123.096, with the
identification of the boundary shadow as `C(B_q)` from P123.094.  QED

**Remark 3.2 (the tangential complex was Hochschild homology all along).**
The complex `\Omega_{dR}=(S\to S\,dt)` that A125.001 introduced as a
dualizing object, and whose relation to the source A125.001 §6 flagged as the
conditional `(*)`, is by (d) the Hochschild homology of the real coordinate.
The conditional was not an extra hypothesis but an instance of HKR, and
A125.011 had already removed it from the load-bearing path.

## 4. The torsion invariant and its regularization

By Theorem 3.1, for `w\notin\Gamma`,

\[
 T(E_w)\ =\ \sum_{\gamma\in\Gamma}\ \sum_{v}\ \log\tau_v(\gamma w),   \tag{4.1}
\]

a sum over the lattice of local log-torsions, each finite-place term given
by (2.1) and the real term by the boundary corner torsion.  The lattice sum
does not converge absolutely and requires regularization; this is the
renormalized relative determinant of P123.012 and P123.105–110.

**Definition 4.1.**  `T(E_w)` is the logarithm of the coupled induced relative
determinant germ of P123.109–110 evaluated on the twist `\beta_w`, normalized
by the half-density.  `T(\Delta)` is the logarithm of the renormalized relative
determinant at the identity, P123.012 and P123.105.  On `G`, `T` extends by
`T(K\oplus L)=T(K)+T(L)`, `T(K[1])=-T(K)`, and by the cone law.

**What is proved about Definition 4.1 and by whom.**

* Existence and locally uniform convergence of the germ, with a quantitative
  tail: P123.107.  Composition law with endpoint anomaly, cocycle identity,
  adjoint and semilocal compatibility: P123.108, P123.110.
* That its local factors are the torsions (2.1): P123.060 §2–4, "exactly what
  the local Fourier trace sees transversely: the fixed differential `1-n`,
  together with the dilation half-density".
* That the finite-orbit truncations of the lattice sum (4.1) are computed by
  cyclic finite traces and equal the corresponding integral torsion
  determinants: P123.039 §§1–2, with its stated scope "proved on the orbit
  lattices of P123.038".
* That these truncations converge to the germ: this is the "logarithmic trace
  limit" of P123.039 §3–4 together with the tail bound of P123.107.

The regularization has an ambiguity, and it is harmless in a precise sense:
two admissible regularizations of a lattice sum of local Jacobians differ by
a character of the idele class group of the form `c\log|w|`, i.e. by a
**ruling-plane** term (A125.004 Theorem 3.3).  Hence `T` is well defined on
`G` modulo the ruling plane, which is exactly where the numerical theory
needs it; the composition anomaly of P123.108 is well defined outright and is
the biextension of A.8 (A125.008 §1).

## 5. The mixed sector is nonzero, by an exact computation

**Theorem 5.1.**  Let `p` be a finite place of the chart and let `u,u'` be
unit classes supported at `p` only, `u_p,u'_p\in\mathbb Z_p^\times\setminus\{1\}`,
with `v_p(1-u_p)\neq v_p(1-u'_p)`.  Then `|u|=|u'|=1`, the two classes have
identical pairings with the ruling plane, and

\[
\boxed{
 T(E_u)-T(E_{u'})\;=\;\log\frac{|1-u'_p|_p}{|1-u_p|_p}
 \;=\;\bigl(v_p(1-u_p)-v_p(1-u'_p)\bigr)\log p\ \neq\ 0 .}              \tag{5.1}
\]

Consequently `[E_u]\neq[E_{u'}]` in `N_A`, neither lies in the ruling span,
and the mixed sector of clause A.6 is nonzero.  **No regularization enters
(5.1)**: the lattice sums cancel term by term.

*Proof.*  In (4.1) the two classes differ only at the place `p`.  For
`\gamma\in\Gamma` with `\gamma_p\neq1`, `|\gamma_pu_p|_p=|\gamma_p|_p\neq1`
so `|1-\gamma_pu_p|_p=1`, and likewise for `u'`; those terms coincide.  For
`\gamma_p=1` the two local factors are `|u_p|^{1/2}/|1-u_p|_p=1/|1-u_p|_p`
and `1/|1-u'_p|_p`.  All real-place and other finite-place terms are
identical since the classes agree there.  So the difference of the two
lattice sums is the difference of the two `\gamma_p=1` terms, which is (5.1),
and this holds for every regularization, since the regularization acts on the
common part.  The ruling pairings agree because they depend only on `|u|`
(P123.008 (2.3)), and the ruling plane cannot separate two classes whose
pairing with it is the same while their mutual pairing differs.  QED

Theorem 5.1 replaces A125.006 Theorem 2.1 with a statement that is not only
nonvanishing but **explicit**: the mixed numerics of two unit classes at one
prime is the `p`-adic distance of the units to `1`, in units of `\log p`.
That is the arithmetic content Theorem 1.1 proves invisible to every additive
invariant.

**Remark 5.2 (the arithmetic family is seen).**  For `\Gamma_n=E_{a_S(n)}`
with `n=p^{k}`, the `\gamma_p=1` local factor at `p` is (2.1) with
`\sigma_p=p^{k}`, namely `p^{-k/2}`, so `T(\Gamma_n)` carries the term
`-\tfrac k2\log p` at `p` together with the `|1-p^{k}|_q` contributions at the
primes `q\mid p^{k}-1`.  It is nonzero.  The boundary theory's vanishing on
`\Gamma_n` (A125.012 Theorem 1.2) is repaired exactly here.  What these
numbers equal in terms of `\Lambda(n)` is a theorem of rows B and C, not of A
(clause A.10), and the ramification contact of P123.037 is a different
integral operation whose relation to the fixed torsion is the deformation of
P123.061; A hands both rows a nonzero, structured value and no name for it.

## 6. Effectivity is proper in the torsion theory

**Theorem 6.1.**  The effective cone of A125.007 Definition 2.1 descends to
`N_A` in the torsion theory and is proper.

*Proof.*  Descent and closure are A125.007 Theorem 3.1, whose proof used only
closedness of the radical and stability of the cone under `\star` and `†`.
For properness, pair an effective class `x=\sum_ua_u[E_u]`, `a_u\ge0`, with
the ruling class `e_+`: by P123.008 (2.3) the pairing is
`\sum_ua_u|u|^{1/2}c_+` with `c_+>0` the normalization of the Tate fibre.  If
`-x` is also effective this sum is `\le0` as well, forcing every `a_u=0`.  The
argument of A125.007 Theorem 4.1 used the sign of the boundary pairing; this
one uses only the positivity of the Tate character and is independent of the
sign of `T`.  QED

## 7. Clauses A.5–A.8 in the torsion theory

**Theorem 7.1.**  With `\mathrm{Tr}_A` the full shadow, `G` its domain,
`T_A=\mathbb R` via `T`, and `\lambda_{RR}=\exp T` the coupled relative
determinant germ:

* **A.5.**  `\mathrm{Tr}_A` is defined on all of `G`; it is acyclic off the
  diagonal (Theorem 1.1) and its value on the diagonal is the regularized
  determinant (P123.012, P123.105).  `T` is additive on triangles by the cone
  law, cyclic by P123.122 (5), cutoff independent by P123.095 §4 and P123.110,
  and is a determinant by construction.  Its value on `\Gamma_n` is not
  asserted.
* **A.6.**  `\langle E_u,E_v\rangle:=T(E_{uv^{-1}})`, well defined modulo the
  ruling plane (§4).  The radical is closed (intersection of kernels of
  continuous functionals), a two-sided ideal (the group structure of the
  classes and the adjunction `\langle E_u\star E_m,E_v\rangle=\langle E_u,
  E_v\star E_{m^{-1}}\rangle`), and `†`-stable (`T(E_{w^{-1}})=T(E_w)` because
  the half-density adjoint (1.2) of A125.011 carries the fixed complex of `w`
  to that of `w^{-1}` with the same torsion, `|w^{-1}|^{1/2}/|1-w^{-1}|
  =|w|^{1/2}/|1-w|`).  `N_A` is Hausdorff, contains the ruling plane
  (A125.004 Theorem 3.3) and a nonzero mixed sector (Theorem 5.1).
* **A.7.**  Theorem 6.1.
* **A.8.**  Convergence, biextension (the anomaly cocycle), principal
  invariance and restriction are P123.107–110 as in A125.008 Theorem 2.2; the
  equality formula is the decomposition (4.1), i.e. Theorem 3.1 together
  with the local identification (2.1); the ruling comparison is A125.008
  Theorem 4.1.  No Hodge sign is asserted.

*Proof.*  Assembled from the cited statements as indicated.  QED

## 8. Ledger

| statement | status |
|---|---|
| Thm 1.1 full shadow acyclic off the diagonal; Cor. 1.2 no additive theory is Weil-strength | `PROVED-IN-REPOSITORY` |
| §2 torsion survives complexification; (2.1) local torsion = half-density Jacobian | `PROVED-IN-REPOSITORY` (P123.039 (1.1), P123.060 §2) |
| Thm 3.1(a) label splitting with deck Koszul | `PROVED-IN-REPOSITORY` (P123.121, P123.123, A_DUALITY_WORK deck descent) |
| Thm 3.1(b) Künneth over places | `IMPORTED` (Eilenberg–Zilber for nuclear Fréchet algebras); hypotheses: nuclearity P123.121, K-flatness P123.122 §3 |
| Thm 3.1(c) finite places | `PROVED-IN-REPOSITORY` on the explicit model (P123.060 (1.1), P123.066); the passage to the Fréchet coefficient algebra is `IMPORTED` with the vanishing of higher HH for locally constant algebras |
| Thm 3.1(d) real place | `PROVED-IN-REPOSITORY` (P123.118–119 HKR; P123.094, P123.096) |
| Rem. 3.2 the tangential complex is HKR; `(*)` was never an extra hypothesis | `PROVED-IN-REPOSITORY` |
| Def. 4.1 regularized `T`; well defined modulo the ruling plane | `CONSTRUCTED` (P123.012, P123.105–110); finite-orbit truncations `PROVED` (P123.039 §§1–2); limit `IMPORTED` from P123.039 §§3–4 + P123.107 |
| Thm 5.1 mixed sector nonzero, exact, regularization-free | `PROVED-IN-REPOSITORY` |
| Rem. 5.2 `T(Γ_n)≠0` | `PROVED-IN-REPOSITORY` |
| Thm 6.1 properness via the Tate character | `PROVED-IN-REPOSITORY` |
| Thm 7.1 A.5–A.8 in the torsion theory | `PROVED-IN-REPOSITORY` with the imports above |
