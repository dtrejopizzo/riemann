# A125.012 — why the boundary theory is not Weil-strength, and the single theorem that would make it so

Status: `PROVED-IN-REPOSITORY` for Theorem 1.2 (a no-go) and Theorem 3.1
(a conditional closure).  `OPEN` for the gate statement `(F)` of §3.  This
note is the answer to the request to lift row A to `WEIL-STRENGTH-COMPLETE`:
it shows exactly what stands between the proved theory and that label, and
that it is one theorem.

## 1. A no-go for the letter-satisfying theory

Write `A^{\partial}` for the theory of A125.006–011: the graph sector `G`
with the **boundary** cyclic shadow `\mathrm{Tr}^{\partial}` computed by the
corner bar of P123.094–097, numerical target `\chi\circ\mathrm{Tr}^\partial`.
A125.010–011 show `A^\partial` satisfies the letter of A.1–A.10 on `G`
without conditional input.

**Lemma 1.1 (the arithmetic family lies in `G`).**  By P123.038 §1, for a
chart `S` containing `\infty` and the primes of `n`, the arithmetic
correspondence of row B is the twisted bimodule `E_{\beta_{a_S(n)}}` with
`a_S(n)=(1\text{ at }\infty,\ n\text{ at each finite place of }S)`, of
normalized class `h_S(n)` with Tate modulus `1/n`, composing as
`E_m\star E_n\cong E_{mn}` and transporting literally across charts,
`L_{ST}(a_S(n))=a_T(n)`.  Hence `\Gamma_n:=E_{a_S(n)}\in G`.

**Theorem 1.2 (no-go).**  In `A^\partial`, `\mathrm{Tr}^{\partial}(\Gamma_n)`
is acyclic and `\chi(\mathrm{Tr}^\partial(\Gamma_n))=0` for every `n>1`.
Consequently no theory built on `A^\partial` can have the explicit formula, or
any nonzero value on `\Gamma_n`, as a theorem of rows B/C: the trace that A.5
hands to B/C is identically zero on the arithmetic family.

*Proof.*  `h_S(n)` has module `1/n\neq1`, so on the orbit-decay boundary,
whose coordinate is the real orbit parameter, it acts by the translation
`t\mapsto t+\log n`, which is free.  A125.006 Theorem 1.1(1), i.e. P123.096,
gives the contraction.  QED

Theorem 1.2 is the precise content of P123.082's judgment that the twist-only
sector "did not produce the geometrically mixed sector required by A.2, A.6
and A.8".  But it also corrects that judgment's prescription.  P123.082 asked
for "additional noninvertible/localized bimodules".  Lemma 1.1 shows the
arithmetic correspondences are already present and invertible; what is
missing is not an object but a **shadow**: the boundary shadow sees only the
free translation and is blind to the interior.  The non-invertibility of row B
lives in the *contact*, not in the correspondence, exactly as P123.037/060/061
compute it: the ramification complex `[\mathbb Z\xrightarrow{n}\mathbb Z]` and
the fixed complex `[\mathbb Z\xrightarrow{n-1}\mathbb Z]` are data of the
diagonal shadow of an invertible map, not of a non-invertible object.

So `A^\partial` must **not** receive the label, for a reason sharper than the
one recorded: it satisfies every clause and is useless to B/C.  The
specification's adversarial audit exists to catch exactly this, and it does.

## 2. The full shadow

The remedy is fixed by A.5 itself, which names "a trace/shadow on a declared
trace-class domain".  The shadow of P123.122 (4) is the **full** relative
cyclic shadow

\[
 \mathrm{Tr}_A(M)=\mathrm{Tot}\bigl[M\hat\otimes A^{\hat\otimes n}\bigr]_{n\ge0},
 \tag{2.1}
\]

of which the corner bar is the boundary sector only.  For a graph class
`E_w`, (2.1) is the twisted relative Hochschild complex of the crossed
product, and it decomposes over the fixed-point strata of `w` on the carrier:

\[
 \mathrm{Tr}_A(E_w)\ \simeq\ \mathrm{Tr}^{\rm int}(E_w)\ \oplus\
 \mathrm{Tr}^{\partial}(E_w),                                     \tag{2.2}
\]

where `\mathrm{Tr}^{\rm int}` collects the contributions of interior fixed
points.  For `w=a_S(n)` the interior fixed scheme is computed integrally in
P123.060 (1.1): `R[z]/((n-1)z)`, supported on the `(n-1)`-torsion, with
transverse fixed complex `[R\xrightarrow{n-1}R]`, contractible at `p\mid n`
and with analytic normal Jacobian `|n|_p^{1/2}/|1-n|_p=p^{-k/2}` for
`n=p^k`, which is the half-density weight of P123.042–059.  The boundary
contribution is the free translation of Theorem 1.2 and vanishes.  So
`\chi(\mathrm{Tr}_A(\Gamma_n))` is carried entirely by torsion fixed points
weighted by the half-density, which is the shape of a finite Euler factor
and not of a boundary rank.  That value is a theorem of B/C, as A.5
prescribes; A's obligation is only that the functor be defined and finite.

## 3. The gate

**Statement `(F)`.**  For every external idele class `w`, the full relative
cyclic shadow `\mathrm{Tr}_A(E_w)` of (2.1) is a bounded complex with locally
constant finite ranks, and (2.2) holds with `\mathrm{Tr}^{\rm int}(E_w)`
computed by the fixed-point strata of `w` with their transverse complexes and
half-density weights.

**Theorem 3.1 (conditional closure).**  Assume `(F)`.  Then, with `\mathrm{Tr}_A`
of (2.1) in place of `\mathrm{Tr}^\partial` throughout, every statement of
A125.006, A125.007, A125.008 and A125.011 holds verbatim on `G`, and the
resulting theory satisfies A.1–A.10 with:

* the mixed sector of A.6 nonzero (A125.006 Theorem 2.1 goes through, since
  for a free unit class both summands of (2.2) vanish while
  `\chi(\mathrm{Tr}_A(\Delta))\ge r>0`);
* the numerical pairing `\langle E_u,E_v\rangle=\chi(\mathrm{Tr}_A(E_{uv^{-1}}))`
  now **nonzero on the arithmetic family**, so that its values on `\Gamma_n`
  are available to B/C;
* effectivity proper (A125.007 Theorem 4.1: the proof used only
  nonnegativity of coefficients and `\chi(\mathrm{Tr}_A(E_w))\ge0`, which
  holds because every stratum contributes a rank);
* Riemann–Roch `\deg\lambda_{RR}=\chi\circ\mathrm{Tr}_A` (P123.095 (4) on the
  perfect full shadow), whose fixed-point form is the Lefschetz–RR equality of
  P123.009 now globally.

*Proof.*  Each cited proof used exactly four properties of the shadow:
exactness on triangles, cyclicity (P123.122 (5)), perfectness on `G`, and
vanishing on freely acting classes.  Under `(F)` the first three hold for
(2.1), and the fourth holds for classes free on the whole carrier; for
classes with interior fixed points the vanishing is replaced by the
stratified value, which only strengthens the separation from the ruling span
in A125.006 Theorem 2.1, since a function of `|w|` alone cannot reproduce a
value depending on the `(n-1)`-torsion.  QED

**Corollary 3.2.**  `WEIL-STRENGTH-COMPLETE` for row A is equivalent, given
A125.001–011, to statement `(F)`.

## 4. Why `(F)` is one theorem and where its pieces are

`(F)` is the A-side half of ledger row `B4`, "integral multiplicative
correspondences in common `A` with diagonal contact `B1`", which P123.024
marks `OPEN` with no proof.  Its ingredients are all constructed:

| piece of `(F)` | where |
|---|---|
| the shadow functor (2.1), exact, cyclic | P123.122 §4 |
| boundary sector of (2.2) and its dichotomy | P123.094, P123.096–097 |
| interior fixed scheme of `a_S(n)`, transverse complex, Jacobian | P123.060 |
| integral deformation joining power maps to normal dilations | P123.061 |
| induced normal boundary traces recovering the local relative character | P123.043, P123.046 |
| local derived excess determinant and Lefschetz–RR equality | P123.009 |
| finite translation traces recover the integral contact determinant | P123.039 |

What is not proved is the **decomposition (2.2) as a statement about the
full complex (2.1)**: that the relative Hochschild complex of the twisted
crossed product splits, up to admissible acyclics, into the interior
fixed-point contributions and the boundary corner bar, each perfect.  This is
a localization theorem for the shadow along the fixed-point stratification of
`w`, of the same type as the one-sided derived localization already proved in
P123.125, now applied to the *cyclic* complex rather than to a module.  The
two-sided excision of A125.002 is the tool that makes such a localization
compose, and it is proved on `G`.

The deformation of P123.061 is the natural route: it joins the power map,
where the interior contact is the ramification complex, to the normal
dilation, where it is the fixed complex, inside one integral family, and the
question is precisely whether the shadow (2.1) is constant along it up to
perfect excess.  P123.061 §5 states that constancy as the open comparison in
the same words.

## 5. Ledger

| statement | status |
|---|---|
| Lemma 1.1 arithmetic family `Γ_n=E_{a_S(n)}∈G` | `PROVED-IN-REPOSITORY` (P123.038) |
| Thm 1.2 boundary shadow vanishes on `Γ_n`, `n>1` | `PROVED-IN-REPOSITORY` |
| §1 correction of P123.082's prescription: shadow, not objects | `PROVED-IN-REPOSITORY` |
| (2.2) fixed-point decomposition of the full shadow | `OPEN` = `(F)` |
| Thm 3.1 `(F)` ⇒ A.1–A.10 Weil-strength on `G` | `PROVED-IN-REPOSITORY` (conditional) |
| Cor. 3.2 `WEIL-STRENGTH-COMPLETE ⟺ (F)` given A125.001–011 | `PROVED-IN-REPOSITORY` |
| `(F)` | `OPEN`; A-side half of ledger `B4` |
