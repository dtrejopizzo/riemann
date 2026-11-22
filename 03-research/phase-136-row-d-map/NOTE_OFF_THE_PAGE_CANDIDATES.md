# Note (written before reading the five maps): candidates outside the painted squares

Status: hypotheses for the plan, not claims.

## 0. The wall, stated as a growth rate

Row D is now one function `h⁰` with (a),(b′),(c) (Paper 47 Thm 12.3). Requirement (c) at
`E = mK` forces `h⁰(mK) ≥ ¼m² + O(m)`. Every count the corpus or Connes–Consani can
define grows **logarithmically or linearly** in the degree:
* CC on the curve `Spec Z̄`: `dim_S H⁰(D) = ⌈(deg D + log 2)/log 3⌉` — **linear** in `deg`
  (a genuine curve behaviour: `h⁰(D) ~ deg D`).
* Paper 47 §13 on the square, one-parameter lattice of translates of `ΠK`: `O_Q(log m)`.
So the wall is: **where does the second factor of `m` come from?** In geometry
`h⁰(nD) ~ n²D²/2` on a surface because sections of a line bundle on a surface restricted to
a moving curve give rank `~ n` on each of `~ n` independent fibres. In Arakelov geometry the
same quadratic growth is a theorem (arithmetic Hilbert–Samuel, Gillet–Soulé) and it is the
input of the **arithmetic Hodge index theorem** (Faltings–Hriljac). The corpus audited that
theorem (P122.007) and correctly ruled out *importing* it: our square is not an arithmetic
surface. It never asked whether its **mechanism** can be rebuilt on the `S`-square.

## 1. Candidate D-HS ("Hilbert–Samuel on the F1-square") — the leading off-the-page idea

**Shape.** Treat `X := Spec Z̄ ×_S Spec Z̄` as a fibration over the second factor. A class `E`
(radial, i.e. supported on graphs `Γ_{Frob_n} = {(x, nx)}` in the adele class space, smeared by
`h(log n)`) restricts to each fibre `{y = y₀}` as an Arakelov divisor `E|_{y₀}` on the curve
`Spec Z̄`, whose CC-cohomology `H⁰(E|_{y₀})` has `dim_S` **linear** in `deg(E|_{y₀})`.
Define sections of `E` on the square as **compatible families of fibre sections**, i.e. an
`S`-module `H⁰_X(E)` fibred over the base, and
`h⁰(E) := dim_S H⁰_X(E)` (CC's generator count) or `log #` of its integral points.
The expected growth is (number of fibres where `E|_{y₀}` has positive degree) × (fibre
dimension) `~ m × m` for `E = mK`: **the two linear factors multiply.**

**Where unimodularity enters (the falsifier test, built in).** Compatibility of fibre sections
across the base is transport by the Frobenius: a section over the fibre at `y₀` is carried to
the fibre at `ny₀` by `Frob_n`, and the compatibility condition is that transport be
**isometric for the adelic norms** — which is exactly `Frob_n ⋆ Frob_n^† = Δ^{(n)}` (Paper 44
Thm 3ter.6(ii)), the datum `Ξ_a` lacks (`(n^a + n^{−a})Δ^{(n)}`: transport scales norms by
`n^{±a}`, so compatible families exist only up to a growing defect). This is the first
candidate in the corpus in which unimodularity enters the **definition** of a nonnegative
invariant rather than a comparison.

**Kill tests (pure mathematics, in order).**
 T1. Define `H⁰_X(E)` for `E` supported on finitely many graphs and prove it is an
     `S`-module with `dim_S` finite. (If not definable: dead.)
 T2. Compute `h⁰(mK)` or a lower bound; the target is `≳ m²/4`. (Logarithmic or linear:
     dead, and the reason recorded.)
 T3. Prove (b′): `h⁰(E) > 0 ⇒ E ≡ E' ≥ 0 mod 𝓝_∞`.
 T4. Check RR (c) on `E = mK` and `E = K − nF` symbolically (no numerics needed if T2 gives an
     explicit formula).
 T5. Run the same definition for `Ξ_a` (rank-2 bundle `O(a) ⊕ O(−a)` on `Spec Z̄`, four Tate
     poles): (c) **must** fail there, and the failure must be traceable to the non-isometric
     transport. If (c) holds for `Ξ_a`, the construction is wrong (Thm 12.4).

**Why this is not a painted square.** P122.007 rejected the *import*; phases 15–16 rejected the
*elliptic-curve arithmetic surface* (heights ≠ zeros). Neither built `H⁰` on the `S`-square by
fibre-wise CC cohomology plus Frobenius transport. Connes–Consani built `H⁰` on the **curve**
only and state that the diagonal's self-intersection on the square is unsolved (AUDIT_CONSOLIDATED §3).

## 2. Candidate D-θ (Bost-type theta invariant on the square) — secondary

Replace `dim_S` by `h⁰_θ(E) := log Σ_{v ∈ Λ_E} e^{−π‖v‖²_E}` over an integral structure
`Λ_E` (Bost / van der Geer–Schoof). Exact RR via Poisson summation is automatic on the curve;
on the square the Poisson mechanism *is* the explicit formula (Paper 45 Thm 9.4), which would
turn (c) into an identity rather than an inequality. Its risk: real-valued "dimensions" (CC's
objection, NO-GO R16) — but Thm 12.3 needs only `h⁰ ≥ 0`, not integrality. **This candidate
survives R16 as restated in Paper 47.** Kill test: the lattice `Λ_E` on the square must have
rank growing linearly in `m` for `E = mK`; the Paper 47 §13 lattice does not.

## 3. Candidate D-K (Krein index / definitizability) — a reformulation, not a construction

`I_∞` on `D^W` is a Krein-space form whose negative index counts off-line zero pairs plus the
polar plane. Pontryagin's theorem (a `J`-self-adjoint operator on `Π_κ` has at most `κ`
non-real eigenvalue pairs) turns "finitely many off-line zeros" into "finite negative index of
`−I_∞` beyond the polar plane". Not a route to the sign; possibly a route to **structure
theorems** (e.g. a definitizing polynomial). Low priority; record.

## 4. What to reject before starting

Any candidate whose definition is model-uniform in `Z` (Restatement 12.4a): convex-set
dimensions, Galerkin counts, Gram determinants, entropies of the form alone. Any candidate that
needs `Σ_ρ |Φ(ρ)|²` or the symbol's sign (P122 §1). Any candidate on the colimit rather than the
Weil completion (Paper 47 Thm 14.3).
