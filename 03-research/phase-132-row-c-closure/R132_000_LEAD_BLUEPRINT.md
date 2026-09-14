# R132.000 — Lead blueprint for the closure of row C (Paper 45)

Author: session lead (Fable 5.1). Date: 2026-09-12. Status: `BLUEPRINT` (to be
proved by the builder, attacked by the hostile auditor). Owner's instruction of
this date: build row C to `WEIL-STRENGTH-COMPLETE` **and** to the level the RH
proof requires, connected by theorem number to the closed rows A (Paper 43,
phase 130) and B (Paper 44, phase 131). Protocol as in phases 130–131: builder
(Opus) → hostile audit (Opus) + lead audit → repair rounds → lead decision by
grep-verified record.

## 0. The diagnosis

Paper 45 (1330 lines; label `ASSEMBLED AND NORMALIZATION-COMPATIBLE, NOT
LOCALIZED` after D128.003) is written against the **old** row A: Fell
completion, sections `K_h` with coefficients at "external classes" `E_u`,
`Γ_n = E_{a_S(n)}`, the zero-count filtration `Z_J` with corner strata,
`χ_A` assembled term by term from P123.042/046/035, Theorem 5.4 (irrationality
of `log p/log q`) withdrawn, §11 "discharging" an `n−1` obligation that Paper 44
(phase 131, W1–W3) proved never existed. **None of the objects Paper 45 uses is
the declared carrier any more.** Since phases 129–131 the carrier is

* Paper 43: `C_S ≅ R^× × ∏_{p∈S_f}Z_p^×` (Lemma 3.3), `D_A = C_c^∞(C_S)`,
  `T = Σ_v W_v` with `c := 0` (Def 8A.7d), `I_A(F,G) = T(F⋆G^†)` (Def 9.2),
  chart maps `j_p, j_∞` (9.5b), Thm 8.8 (absolute convergence off the
  identity), (8.5∞) with counterterm, symbol `T̂` (Thm 9.7, 9.7b: Mittag–Leffler
  form, Tate poles at `τ=∓i/2` with universal residue `∓i`, total
  `∓i(|S_f|+1)`), `𝓝 = 0` (Thm 9.8), `N_A^{dist}` with rulings `e_±` as limits
  of spread Tate characters (9.14a–c′), colimit trace `T_∞` (Thm 8A.7c),
  `𝓐_tr` (8A.7b), Thm 14.1 (no Hodge-index shape on `N_A`), Thm 10.8b (Mertens,
  `CLASSICAL`: colimit ruling pairing `= 1`);
* Paper 44: radial classes `Γ_h ∈ D_A^{rad} ⊂ D_A` (Def 3bis.6, Lemma 3bis.6a),
  norm class `Γ_n^{rad}`, Thm 3bis.7 (`T(Γ_h) = Σ_{p,k}(\log p)p^{−k/2}[h(k\log p)
  + h(−k\log p)] + ∫K(|t|)h`), Frobenius family `Frob_n` (§3ter), Thm 3ter.10
  and 3ter.12 (composite labels vanish because the support meets no stratum),
  integral shadow (§6bis), the two Gram forms (Thm 8bis.1e: the Weil kernel is
  the Gram form of `Frob⋆Δ^{rad}`), Thm 8bis.4 (the interface, `CLASSICAL`),
  Thm 8bis.4a, conditional Thm 8bis.7, Thm 8bis.8, conventions (C1) colimit
  and (C2) normalization, Thm 9.1 (the prime packet).

Row C must therefore be **rebuilt on the true carrier**, and on it most of what
was hard in Paper 45 becomes either a theorem of A/B cited by number or a
non-problem. What remains for C — and is genuinely C's — is listed in §2.

## 1. What each clause of the contract (Paper 45 §2, PLAN §7) becomes

| clause | on the true carrier |
|---|---|
| C.1 test class, `K_h` inside row A | **`Γ_h ∈ D_A^{rad} ⊂ D_A`**, a genuine element of the declared test algebra (Paper 44 Def 3bis.6, Lemma 3bis.6a: `Γ_h⋆Γ_g = Γ_{h⋆g}`, `Γ_h^† = Γ_{h^∨}`); no completion, no compact-section argument (D128 C8 dissolves). Point classes `Γ_n^{rad}, Frob_n ∈ N_A^{dist}` (Paper 44 Thm 8.3, 3ter.14). State which statements are on `D_A^{rad}` and which on `N_A^{dist}` |
| C.2 realization; two Tate terms | Paper 43's boundary `M = (λ_−,λ_+)`, hyperbolic `B_T`, rulings `e_± ∈ N_A^{dist}` (9.14a), Tate characters; Paper 45 Thm 8.1 (kept, confirmed by D128) with `z(F) = M(Γ_F)`; primitivity `= M(Γ_F) = 0 = ` two linear conditions (Paper 44 (8bis.9)); the Tate packet is `β_T(M,M)` (Paper 45 Thm 8.1, Paper 44 8bis.4) |
| C.3 trace identity, one kernel, finite + archimedean + identity | `I_A(Γ_F,Γ_G) = T(Γ_{F⋆G^†}) = Σ_p W_p + W_∞` with the identity term handled by (8.5∞), `c := 0`: Paper 43 Thm 8.8 + Paper 44 Thm 3bis.7. **The localization question of D128 C2/C3 is answered by row A's construction, not by C**: `T` is row A's declared trace (clause A.5: Thms 8A.3–8A.4 cyclic, 8A.7b nuclear, 8A.9 Euler characteristic of the shadow at unit shells with a *declared* half-density–Lefschetz normalization at non-unit shells, O-A5-5 "no stronger statement claimed"). Say exactly that. The corner-strata problem **disappears with the carrier**: `C_S` is a group, the strata are the shells `j_p(p^kZ_p^×)`, and composite labels vanish by Paper 44 Thm 3ter.12 (support meets no stratum) — Paper 45's Thm 5.4 stays withdrawn and is now **unnecessary**; §5 is to be replaced, with a withdrawal ledger |
| C.4 prime term, Gamma term, poles in ONE comparison | all three are read off **one object, the symbol `T̂_S` on `𝔠_0`** (Paper 43 Thm 9.7, 9.7b): finite Mittag–Leffler part = prime terms; `Ŵ_∞ = \log π − Re ψ(¼+iτ/2)` = Gamma term (Paper 45 Thms 7.2–7.4 kept as computations, C5 honesty: `det_ζ` gives `Γ(s/2)` up to `2^{½−s/2}`, `\log π` comes from the finite part); the poles at `τ = ∓i/2` = Tate points, residue `∓i` per place. **New theorem required (§2.2): the polar packet of the explicit formula from the colimit** |
| C.5 order of limits | convention (C1): every statement about all primes is a colimit statement (`T_∞`, Paper 43 Thm 8A.7c(e): charts stabilize on compact windows); `Γ_h` compactly supported ⇒ prime sum finite; archimedean integral absolutely convergent; zero sum in symmetric order. No interchange. Redo Paper 45 §9.4 on the true carrier |
| C.6 `I_A = B_nuc`; sufficiency | first half: identity of the **declared trace on radial classes** with the corpus Weil form `B_nuc` in the fixed sign convention `q = −B_nuc` (P123.036, paper 42) — this is Paper 44 Thm 8bis.4(i) with the conventions matched; state it as **C's comparison theorem on the true carrier** and prove the convention matching line by line. Second half: Paper 45 Thm 10.4 (kept; D128 confirmed) with the C10 fix (`(a,b) ↦ a + b s_0²` is an `R²→C` isomorphism, coefficients stay real; injectivity by analyticity) |
| C.7 no zero position for any sign | as before; Paper 43 Thm 14.1 and Paper 44 Thm 8bis.4a make it concrete: no sign is available on `N_A` or on the pure Frobenius form; the only sign statement is Weil's criterion, `CLASSICAL` |
| C.8 no analytic black box | **strong form, §2.1**: prove the explicit formula in the repository |
| C.9 compatibility with A and B; handoffs | by theorem number (§3). Delete §11 (the `n−1` obligation never existed: Paper 44 §9bis W1–W3, Lemma 3bis.1); replace by the true handoffs |

## 2. What is genuinely row C's — new theorems to prove

**2.1 The explicit formula, PROVED-IN-REPOSITORY (clause C.8 in its strong
form).** D128 C4 broke Paper 45's sketch (an illegitimate contour shift across
the zeros). The correct classical proof does not need it, and the builder must
write it in full:

* `ξ(s) = ½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`, entire of order 1, `ξ(s) = ξ(1−s)`, zeros
  = nontrivial zeros of `ζ` (IMPORTED facts about `ζ`, each named: functional
  equation, Hadamard order, `N(T) = O(T\log T)`, Euler product `ζ'/ζ(s) =
  −ΣΛ(n)n^{−s}` for `Re s>1`, Stirling for `ψ`);
* for `g(s) = Φ_F(s)Φ_F(1−s)`, `F ∈ C_c^∞` real: `Σ_ρ g(ρ) = (1/2πi)[∫_{(c)}
  − ∫_{(1−c)}] g\,ξ'/ξ\,ds` by the argument principle on rectangles whose
  horizontal sides avoid zeros (density), symmetric order `|Im ρ| ≤ X`;
* on `Re s = c > 1` expand `ξ'/ξ = 1/s + 1/(s−1) − ½\log π + ½ψ(s/2) + ζ'/ζ`;
  the polar terms give `g(0)+g(1) = 2Φ_F(0)Φ_F(1)`; **each prime term**
  `∫_{(c)} g(s)n^{−s}ds` has an **entire** integrand of rapid decay and may be
  shifted to `Re s = ½` individually (no zeros are crossed because `ζ'/ζ` has
  already been expanded) giving `Λ(n)n^{−1/2}⟨(S_{\log n}+S_{−\log n})F,F⟩`;
  the Gamma term likewise, giving `(1/2π)∫|F̂|²[Re ψ(¼+iτ/2) − \log π]dτ`;
* absolute convergence of the prime sum for compactly supported `F` (finite
  sum); the `(1−c)` line by `g(1−s) = g(s)`.

Then the **comparison theorem**: `T_∞(Γ_{F⋆F^†}) = I_A(Γ_F,Γ_F) = −Σ_ρ
Φ_F(ρ)Φ_F(1−ρ) + β_T(M(Γ_F),M(Γ_F))` (signs to be fixed against P123.036 and
Paper 44 8bis.4(ii)), with the polar packet identified with the ruling form
(Thm 8.1). State it as **"the spectral side is the symbol of the colimit
trace"**: at each finite chart `T̂_S` is a real-analytic function on `𝔠_0`
(Paper 43 Thm 9.7); in the colimit it is **not a function** (Paper 44 numerics
(E): `Ŵ_fin^∞(0) = +∞`) but a distribution on radial tests, and the explicit
formula computes it: `T̂_∞ = −Σ_ρ δ_{γ_ρ}` (under RH) plus the polar
distribution, or in general the linear functional `|F̂|² ↦ −ΣΦ_F(ρ)Φ_F(1−ρ) +
polar`. Prove exactly what is true here (distributional convergence of `T̂_S`
as `S` grows, on `|F̂|²` for `F ∈ C_c^∞`, is the explicit formula plus (C1)).

**2.2 The polar packet from the colimit (clause C.4, poles "in the same
comparison").** At a finite chart the symbol's total Tate residue is
`∓i(|S_f|+1)` (Paper 43 Thm 9.7b(c)), chart-dependent and divergent as
`S ↑`; the explicit formula's polar packet is the fixed `2Φ_F(0)Φ_F(1) =
β_T(z,z)`. Reconcile them exactly. Route: (i) the rulings `e_±` are
`I_A`-null along admissible approximations (Paper 43 Thm 9.14c′), so the
per-chart Tate residues never enter `I_A` on primitive tests; (ii) on
non-primitive tests the Tate packet of `I_A` is `β_T(M,M)` with a coefficient
that Paper 43 Thm 10.8b computes **in the colimit as 1, via Mertens**
(`Σ_{p≤x}(\log p)/p = \log x + O(1)`). Prove: *the polar packet of the explicit
formula is the colimit ruling pairing*, and say precisely where Mertens enters
(the finite-place residues sum to a divergence that is exactly the archimedean
growth, leaving coefficient 1). Label the Mertens step `CLASSICAL`, quarantined
exactly as Paper 43 Thm 10.8b; if the reconciliation needs more than Mertens,
say what. This is the one place where the Tate poles of the local symbols meet
the poles of `ζ`.

**2.3 The Gamma factor (clause C.4).** Keep Paper 45 Thms 7.2–7.4 as
computations, with D128 C5's honesty (`det_ζ(N_Γ+s−½) = √(2π)2^{½−s/2}/Γ(s/2)`;
the `π^{−s/2}` is not spectral; `N_Γ` is defined by its spectrum). Connect to
Paper 43: `Ŵ_∞(0,τ) = \log π − Re ψ(¼+iτ/2)` is Paper 43 Thm 9.7(b) and (9.12a);
`K(t) = e^{−t/2}/(1−e^{−2t}) = Tr e^{−tN_Γ}` is Paper 44's archimedean density
(Thm 3bis.7); the counterterm `(γ+\log 4π)h(0)` is (8.5∞) with `c := 0`. Then
prove the **archimedean Tate residue**: `Res_{τ=i/2}Ŵ_∞ = −i` (Paper 43
9.7b(b)) equals the residue of the local Tate zeta `∫_{|x|≤1}|x|^s dx/(2|x|) =
1/s`, matching Paper 44 Thm 8bis.8 — this is the archimedean half of "poles in
the same comparison".

**2.4 Sufficiency (C.6 second half) and what D inherits.** Keep Thm 10.4 with
the C10 fix; connect `Π = −∂_t²+¼` to Paper 44 (8bis.9), Thm 8bis.4a Step 2 and
Thm 8bis.7 (which use it). State the Hodge-index reading honestly: by Paper 43
Thm 14.1 there is **no** Hodge-index shape on `N_A`; by Paper 44 Thm 8bis.4a the
pure Frobenius form fails positivity at every chart; the only positivity
statement equivalent to RH is Weil's criterion on the primitive radial sector
in the colimit (Paper 44 (8bis.10), `CLASSICAL`), which row C now **proves** as
the comparison theorem rather than cites. Row D's target is `I_∂ ≤ 0` on
primitive radial classes of `D_A^∞`, and nothing else.

**2.5 A.6 for the intersection form on the radial sector (Paper 45 Thm 12.4,
redone).** On `D_A^{rad}` at a chart, `I_A(Γ_F,Γ_G) = ∫F̂\bar Ĝ\,T̂_S\,dτ/2π`;
the scalar radical is `{F : F̂\,T̂_S = 0}` = `0` since `T̂_S` is real-analytic and
not identically zero (Paper 43 Thm 9.7). So `𝓝_∩ = 0` on radial tests at every
chart; the rulings live in the completion (Paper 43 9.14a). Prove and connect
to Paper 43 Thm 9.8 (`𝓝 = 0`) and Thm 9.14c (scalar radical = ruling plane in
`N_A^{dist}`). Delete Paper 45's `G_rad` construction in favour of `D_A^{rad}`.

## 3. Connections to A and B — by theorem number, both directions

**From A (Paper 43), used:** Lemma 3.3; Def 8A.7d (`c:=0`); Thm 8.8; (8.5),
(8.5∞), Rem 8.6a; Def 9.2; Thm 9.1 (`M` continuous); Thm 9.7, 9.7b; Thm 9.8;
Thm 9.14, 9.14a–c′; Thm 8A.7c (colimit); Thm 8A.7b; Thm 10.8b (Mertens);
Thm 14.1; §14.0a (carrier). **Handed by A to C** (Paper 43 §14.1a): Thm 10.8b,
Thm 14.1, the window statement 8A.7c — each must be *used* or explicitly
*declined* with a reason.

**From B (Paper 44), used:** Def 3bis.6, Lemma 3bis.6a, Thm 3bis.7,
Def–Thm 3bis.8, Thm 3ter.10, 3ter.12, Cor 3ter.10b, Thm 8bis.1e, Thm 8bis.4,
8bis.4a, 8bis.7 (conditional), 8bis.8, conventions (C1),(C2), Thm 9.1 (the
prime packet), §9bis W1–W3 (the `n−1` obligation never existed). **Handed by B
to C** (Paper 44 §9, R131.019 §5): Thm 9.1; the two-slice theorem; Thm 8bis.1e;
(C1). Each used or declined.

**Consistency checks the builder must run and record** (these are the
"connected well" the owner asked for): (a) Paper 45's `𝒯 = C_c^∞(R_{>0}^×)` in
multiplicative coordinates equals Paper 44's radial profiles `h ∈ C_c^∞(R)` in
`t = \log|x|`, with `F(t) = e^{t/2}f(e^t)` — fix the dictionary once, with the
half-density; (b) the three sign conventions (`q = −B_nuc`; Paper 43's
`I_A(F,F) = ∫|F̂|²(T̂+c)`; Paper 44's `I_∂ = −Q` (8bis.14e)) agree — one table;
(c) the archimedean constants: Paper 43 (14.2) `\log π − ψ(¼) ≈ 5.372`,
Paper 45 (7.4), P123.035 (4.1) — one table; (d) `vol(Z_p^×) = \log p` — Paper 44
Thm 8bis.8 is the theorem, Paper 45 Lemma 6.1 becomes a corollary; (e) the
Fourier/Mellin conventions `Φ_F(s) = ∫F(t)e^{(s−½)t}dt` vs Paper 44
(8bis.14a) and Paper 43's `F̂(τ)` on `𝔠_0` — one dictionary.

## 4. What must be withdrawn from Paper 45, with a ledger (§9bis-style)

Thm 5.4 (already withdrawn) and all of §5.3–5.6, Cor 5.5, 5.7; Cor 6.2's
conditionality (now unconditional via Paper 44 Thm 3ter.12 on the new
carrier); Lemma 6.1 → corollary of Paper 44 Thm 8bis.8; Prop 3.2 and Def 3.1
(old completion) → `Γ_h ∈ D_A^{rad}`; §11 entirely (the `n−1` obligation);
§12.1's `G_rad` → `D_A^{rad}`; Thm 12.5/Cor 12.6 (deepest-stratum index
`n^{−1/2}(n−1)`) → withdrawn as referring to a lift artifact (Paper 44
Lemma 3bis.1); §0.2's "four new theorems" rewritten; §13 verdict re-issued.
Everything kept must be re-proved on the true carrier or cited by number.

## 5. Labels, closure rule, renaming test for C

Labels as in Papers 43/44. Closure rule: every clause `PROVED` on the declared
carrier and the audit of record finds that **no clause is satisfied by a
definition** (D128 C3's failure mode: additivity inherited from a definition)
— for C the adversarial test is: each clause is a theorem about row A's
declared objects, cited by number; the explicit formula is proved, not cited;
every classical import (facts about `ζ` only) is named in §11 with the clause
it serves. Imports allowed for C: the functional equation and Hadamard theory
of `ξ`, `N(T) = O(T\log T)`, the Euler product, Stirling/Lerch, Paley–Wiener,
Mertens (quarantined). Not allowed: any statement about the location of zeros
in a sign proof; any spectral realization imported as a black box (Meyer).

## 6. Deliverables

Paper 45 `main.md` rebuilt (banner, §0, contract table, all sections listed in
§4 rewritten; new §§ for 2.1–2.5; §9bis-style withdrawal ledger; §13 verdict
re-issued; §14 dependencies by theorem number), `README.md`,
`scripts/verify_132_explicit_formula.py` (numerical check of the explicit
formula on the carrier for a few compactly supported `F` against the first
zeros of `ζ` — illustration only — and of every convention table),
`R132_001_BUILDER_ROUND1.md` listing every claim of this blueprint refuted,
with the counterexample. Do not claim a sign, `𝓝_∞ = 0`, or anything about
zeros outside the comparison theorem; do not grant or claim the label.
