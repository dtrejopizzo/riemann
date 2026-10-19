# R131.012 — Audit of round 4 (F1 repair, L1–L4)

Independent of the
audit R131.011 (in progress when this was written).

## 1. Re-derived and found correct

| statement | check |
|---|---|
| F1 repair, Cor 8bis.1d | off-diagonal archimedean indicator `∏_{s∉F}1[s^N \| (n−m)]` vanishes for large `N`; Frobenius Gram form = `W_fin` off the diagonal ✓ (review's own confirmation before round 4) |
| Thm 8bis.1b(iii) | probability Haar on `Z_r^×`: `vol(1+r^jZ_r) = 1/((r−1)r^{j−1})`, strata `r^{−j}` (`j≥1`), `(r−2)/(r−1)` (`j=0`), sum 1; integrand `r^j` constant on strata; packet `−(\log r)[(r−2)/(r−1)+(N−1)]` ✓; numerics slope `−Σ_{r∤n}\log r` reproduced (`n=2`: `4.653960`) ✓ |
| Thm 8bis.1b(iv) | split at `t=ε`: `(0,ε)` contributes `O(1)` uniformly (`(1/2ε²)∫_0^ε t\,dt = 1/4`), `(ε,∞)` gives `−\log(1/ε)+O(1)` ✓ — the construction's press point (2) is settled |
| Thm 8bis.1e | `Γ_m^{rad}⋆(Γ_n^{rad})^† = Γ_{m/n}^{rad}` (level sets compose on `R_{>0}`), profiles convolve, Thm 3bis.7 gives `W_fin+ω_∞` with trivial indicators by `K^♮`-invariance ✓; diagonal = Thm 8bis.2 ✓ |
| Thm 8bis.1′ | correct reading of the complementary-slice dichotomy as a statement on Gram forms; this is the new content and it passes the renaming test |
| Thm 8bis.4(i)–(iii),(v),(vi) | honest; (iii) labelled `CLASSICAL` with the sentence "Weil's criterion carried by row A's trace, not new" ✓ |
| Thm 8bis.8, Cor 8bis.8a, Rem 8bis.8b | `ζ_p(s) = c_p/(1−p^{−s})`, residue `c_p/\log p`; `ζ_∞ = 1/s`; agreement iff `c_p = \log p` ✓. The construction's refutation of the review's chart-invariance route is **correct**: the total residue `∓i(\|S_f\|+1)` is chart-dependent and no statement of Paper 43 makes it invariant. The theorem is a uniqueness theorem given the named requirement (universal Tate residue per place); the requirement is stated, not smuggled. Accepted. |
| §6bis.1 | additive `Sh_Z`, degree additivity with shift rule, trivial cyclicity said openly, (a) `REFUTED` ✓ |
| F4, F5, F6, F8, F9, F10 repairs | ✓ as described in R131.010 §3 |
| scripts | `verify_131_contacts.py`: ALL CHECKS PASS + ROUND-4 CHECKS PASS (re-run by the review) |

## 2. Findings (all inside the quarantined §8bis.3–8bis.4; none touches B.1–B.9)

**LF1 (MAJOR) — Lemma 8bis.6 is false for a general bump `ρ` of mass 1.**
The proof asserts `Σ_n gap_n ρ_{ε_n}(t−\log n) = 1 + O(e^{−L/2})`. For a
uniform grid of spacing `s` and `ε = s` this is `Σ_k ρ(x−k) = Σ_m \hat ρ(2πm)e^{2πimx}`
(Poisson), which is **not** `≡ 1` for a general `ρ` of mass 1 — take `ρ` a
narrow spike supported in `[−0.1,0.1]`: the sum vanishes on most of the line.
*Repair:* choose `ρ ∈ C_c^∞([−1,1])` with `Σ_k ρ(x−k) ≡ 1` (a smooth partition
of unity; mass 1 is then automatic), and prove the non-uniform statement by the
slow variation of the gaps: with `x = e^t`, `(t−\log n)/gap_n = (x−n)(1+O(1/n))`,
so `Σ_n ρ((t−\log n)/gap_n) = 1 + O(‖ρ'‖_∞/n) = 1 + O(e^{−L/2})` on `[L/2,L]`.
The rest of the lemma then stands.

**LF2 (MAJOR) — Thm 8bis.7, primitivization step is false.** "Primitivity can be
enforced by altering two coefficients near `\log n ≈ L/2` by `O(e^{−L})`" — no:
`λ_+(g_L) = ∫g_Le^{s/2}ds ≍ L e^{L/2}` for `g_L` supported in `[L/2,L]`, and a
correction at `\log n ≈ L/2` has `λ_+`-weight `gap_n n^{1/2} ≍ e^{−L/4}`, so the
coefficient change would be `≍ L e^{3L/4}`, not `O(e^{−L})`. Worse, the import
**(W)** as stated ("Tate terms are `O(L²e^{\|β−1/2\|L})`") is **false**: the
polar terms of `g_L⋆g_L^†` are `≍ L²e^{L}`, which dominates `e^{2\|β−1/2\|L}`
since `\|β−1/2\| < 1/2`. Weil's argument works because the criterion is stated
with the polar terms on the geometric side, i.e. on the primitive sector.
*Repair (closes):* (a) primitivize **exactly** with Paper 45 Thm 10.4's
operator `Π = −∂_t² + 1/4`: `\widehat{Πg}(ρ) = ρ(1−ρ)\hat g(ρ)` vanishes at the
Tate points, keeps the support in `[L/2,L]`, and multiplies each zero's
contribution by the constant `\|ρ(1−ρ)\|²`; restate **(W)** for the primitive
tests `\tilde g_L = Πg_L`, with **no** Tate terms (`I_∂ = −Σ_ρ\hat h(ρ)` exactly
on the primitive sector, `CLASSICAL`), as: "`Σ_ρ \hat h_L(ρ)` has a fixed sign
and modulus `≍ L²e^{2\|β−1/2\|L}`". (b) The Riemann-sum approximant `g_D` of
`\tilde g_L` is not primitive; correct it inside the finite-dimensional space
`V_L` of Dirichlet-polynomial profiles by the **minimal-norm** correction along
approximants of `e^{±s/2}χ_{[L/2,L]}`: the mismatch is
`λ_+(e) = O(L)`, `λ_−(e) = O(Le^{−3L/4})`, and the correction is
`a v_+ + b v_-` with `a ≍ Le^{−L}`, `b ≍ Le^{−L/4}`, hence `O(Le^{−L/2})` in
`C^1` — the same size as `e`, so every estimate of the theorem survives.
Write this out; do not leave the two-coefficient sentence.

**LF3 (MAJOR) — Thm 8bis.4(iv) overclaims.** "The sign of the pure Frobenius
Gram form is NOT RH — `PROVED`" is not what the proof shows. It shows that the
two forms differ by `∫\|\hat h\|²\,\hat ω_∞`, with `\hat ω_∞` indefinite. That
does not prove the two positivity statements are inequivalent: in a fixed
chart **both** forms are indefinite (Paper 43 Thm 14.1 applies to either), and
in the colimit the equivalence question for `W_fin` alone is a statement about
zeros (classically the archimedean density `\log\|τ\|/2π` compensates the
zero density, which is why `W_fin` alone is expected to take both signs on the
primitive sector — but that is a `CLASSICAL` heuristic, not a theorem here).
*Repair:* re-label (iv) as `PROVED` for "the Frobenius Gram form is not the
Weil form; the two differ by a form of indefinite symbol", and `CLASSICAL
remark` for the expectation that `W_fin` alone has no fixed sign on the
primitive sector; delete "NOT RH" as a proved claim. The conclusion (vi)
("the object whose Hodge index is RH is the Gram form of `Frob⋆Δ^{rad}`")
stands on (iii), not on (iv).

**LF4 (MINOR) — Lemma 8bis.5** sums over all `k ≤ e^R`, i.e. it is a statement
about the colimit trace `T_∞` (Paper 43 Thm 8A.7c), and it uses Chebyshev's
`ψ(X) ≤ cX` — a classical arithmetic import (weaker than (W), but an import).
Say both; the section is quarantined anyway.

## 3. Interim ruling

The F1 repair is correct and is the real content of round 4: the Weil kernel
is the Gram form of `Frob⋆Δ^{rad}`; the Frobenius family carries the finite
half; the diagonal is computed and has no limit. R5 is now answered in the
form that is true, and honestly labelled. R4 is answered by a uniqueness
theorem with a named requirement; the review accepts that this is the most the
carrier can say, and records that the requirement (universal Tate residue) is
an axiom of the carrier, not a theorem.

LF1–LF3 are errors in `PROVED`-labelled steps of the quarantined converse and
of a negative statement; they must be repaired before any label is granted,
because the closure rule does not allow a false `PROVED` anywhere in the paper.
None affects B.1–B.9.
