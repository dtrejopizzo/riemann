# CA_B_004 — The on-line symbol carries no ζ; the matched σ-transport J(σ) (phase 193)

 Pen and paper. **No negative value for ζ produced or claimed; no sign contact.**

## 1. Proposition 1 (the symbol on the line; PROVED)
Let γ(s) = π^{−s/2}Γ(s/2), X ≥ 2 and, for any real comb a, Z_{<X,a}(s) := exp Σ_{n<X}a(n)n^{−s}/log n (entire, zero-free). The window symbol
σ_a(τ) := ½m(τ) − Re P_{a,X}(½+iτ), P_{a,X}(s) = Σ_{n<X}a(n)n^{−s}, satisfies for every τ ∈ ℝ
  σ_a(τ) = ½ ∂_σ log|γ(s)Z_{<X,a}(s)|² |_{s=½+iτ}.                                                        (1.1)
For a = Λ also σ_Λ(τ) = Re R_X(½+iτ) = −½∂_σ log|ζ/Z_{<X}|² (off the zero ordinates).
Proof. ∂_σ log|γ|² = Re ψ(s/2) − log π = m at σ=½; ∂_σ log|Z_{<X,a}|² = −2Re P_{a,X}. For ζ: log|ζ/Z_{<X}| = log|γζ| − log|γZ_{<X}| and
∂_σ log|γζ|(½+iτ) = 0 by FE + reality (P46 rem:fe, D_{1/2} = 0). ∎
**Reading.** On the critical line the symbol is the σ-log-derivative of an entire, zero-free function built from Γ and the finite comb;
ζ enters only through ∂_σ log|ξ₀| = 0, i.e. the FE, which Epstein/DH also have (O10). Any "same ζ on both sides" coupling evaluated at σ = ½
is therefore vacuous on the symbol side; it must live at σ ≠ ½ or in the test.

## 2. Pre-screen of J(σ) against NT_013/NT_014, Target E, L2_026/027
J(σ) := ∫ω(τ)|g_X(σ+iτ)|²dτ, ω := F̂₀²|Z_{<X}(½+iτ)|² (frozen), g_X := ζ/Z_{<X}. Identity (CA_B_001 (1.3)): I_ζζ = −(1/2π)J'(½).
| obstruction | does J escape? | reason |
|---|---|---|
| NT_014 part (b) (transport across (1,3/2] needs zero-free information) | **YES** | NT_013/014 concern continuity in σ of the *symbol* (a log-derivative, poles at the zeros) and absolute convergence of ζ'/ζ, which holds only for σ > 3/2. J transports |g_X|², a holomorphic mean square: g_X is holomorphic on σ ≥ ½ except the pole at 1, polynomially bounded (CITED), so J ∈ C^∞(½,2) and J' = 2∫ωRe(ḡ g') with no zero denominators. Nothing is transported through ζ'/ζ |
| Target E inconsistency (Euler object absolute only for σ > 3/2) | **YES** | J uses the Euler product only as boundary data at σ = 2 (coefficients of g_X vanish on 1 < n < X) |
| L2_026 / rem:fe (FE antisymmetry; symmetrizations void) | **YES** | ω|g_X(σ)|² is not invariant under σ ↦ 1−σ (frozen ω, and |χ|² appears on reflection); J is never symmetrized |
| L2_027 (no conjugation) | not used | |
| **lem:shape-ident (B″), key test** | **NO** | by Prop 1, for ANY comb a with the test kept equal to ζ: g_a := ζ/Z_{<X,a}, ω_a := F̂₀²|Z_{<X,a}|² give I^a_ζζ = −(1/2π)J_a'(½) exactly. The identity is comb-generic. The only ζ-specific datum is the boundary: g_X = 1 + Σ_{n≥X}b(n)n^{−s}, b ≥ 0 (Euler × Λ), whereas g_a has nonzero coefficients on 1 < n < X |
| covers the window form? | **NO** | J sees only I_ζζ; I_pp, I_ζp, I_ρ (EI_002 (3.1)) dominate at bounded height |

## 3. The Green identity for J (PROVED)
Cauchy–Riemann gives ∂²_σ|g|² = 4|g'|² − ∂²_τ|g|²; integrating against ω (rapidly decreasing, ζ polynomial) and by parts twice:
  J''(σ) = 4∫ω|g_X'(σ+iτ)|²dτ − ∫ω''(τ)|g_X(σ+iτ)|²dτ,                                                     (3.1)
  I_ζζ = (1/2π)[ −J'(2) + 4∫_½^2∫ω|g_X'|² − ∫_½^2∫ω''|g_X|² ]  (σ ∈ [½,2] avoiding σ=1 in the principal-value sense; the pole contributes an explicit residue term, CONDITIONAL on writing it).    (3.2)
J'(2) = −2Σ_{m,n} b(m)log m · b(n)(mn)^{−2}ω̂(log(m/n)), with b(1) = 1, b = 0 on (1,X): O(X^{−1}log X)·‖ω̂‖_∞ (PROVED, crude).
The square 4∫∫ω|g'|² ≥ 0 is non-linear in Λ and helps the sign; the term ∫∫ω''|g|² has no sign (ω'' changes sign). So
  I_ζζ ≥ 0 ⟸ J convex on [½,2] and J'(2) ≤ 0  ⟸ (W_σ) ∫ω''|g_X(σ+·)|² ≤ 4∫ω|g_X'(σ+·)|² for σ ∈ [½,2].        (3.3)
(W_σ) is a weighted Wirtinger inequality for g_X. It cannot hold for all holomorphic g (take g = e^{λs}·bump-free, λ→0: LHS fixed sign of ∫ω'',
which is 0; take g with |g|² concentrated where ω'' > 0 — possible since ω'' > 0 somewhere). Status: OPEN for g_X; ARGUED false as a
comb-generic statement.

## 4. Verdict
J escapes the part-(b)/Target-E/antisymmetry obstructions (column "transport crosses (1,3/2]": NO-obstruction, PROVED by the holomorphy of
|g_X|²). It does **not** escape (B″): the identity is comb-generic; the ζ-specific content is only the Euler-tail boundary at σ = 2, whose size
is O(X^{−1}), far below what (R)(6),(7) need — the sign would have to come from (W_σ), which is a pointwise-in-σ positivity statement of the
same type as the target and covers only the piece I_ζζ. **YES→NO moves:** "the transport uses that test and symbol come from the same ζ" → NO
(Prop 1: at σ = ½ the symbol has no ζ; off the line the coupling reduces to boundary data at σ = 2). Switched to CA_B_003 strengthened (CA_B_005).

## 5. Self-review
- Prop 1: correct, one line; it is prop:boundary + rem:fe rewritten with a zero-free primitive. Not new mathematics; new as a screen. ✓
- (3.1): requires ω ∈ Schwartz (F̂₀ Schwartz, |Z_{<X}|² bounded on the line) ✓; the pole at s = 1 lies in (½,2): (3.2) must be split at 1
  with the residue term — flagged CONDITIONAL, not used for any sign. ✓
- The claim "(W_σ) false comb-generically" is ARGUED (a construction sketch), not PROVED. ✓

## 6. Post-review FIX (accepted)
The pole of ζ at s = 1 makes J(1) = ∞. The chain (3.3), "J convex on [½,2] and J'(2) ≤ 0 ⇒ I_ζζ ≥ 0", is therefore false as written.
Ledger: "J-convexity across σ = 1" → NO (PROVED). (3.1) holds on [½,1) and on (1,2] separately; any transport must handle the residue.
Prop 1 and the (R)(4) observation (transport of g, not log g, is zero-free) are unaffected.
