# R155_035 — Hostile audit of R4c (Li/Báez-Duarte dictionary)

**Date** 2026-09-22 · **Target** `R155_034_BUILDER_ROUND4C_LI_DICTIONARY.md`, `scripts/r4c/li_phi_check.py`
(rerun, 40 s, reproduces its JSON bit-for-bit). **Verdict: L1 stands; §2.2 contains a material false
claim; L2/L3 stand with a correction; L4 is mis-sourced and mis-labelled; the §4.4 numerics do not
measure what the text says they measure.**

## 1. Theorem L1 — **CONFIRMED**
`B(γ)=(2iγ−1)/(2iγ+1)`, `B(−γ)=B(γ)^{−1}`, `1−1/ρ=(γ+i/2)²/|γ+i/2|²` (L1 proof, `:96`) all check.
`θ=2arctan(1/2γ)=2arg(γ+i/2)`: `arg(2iγ−1)−arg(2iγ+1)=π−2arctan2γ=2arctan(1/2γ)` ✓; `Φ_n=1−cos nθ≥0`
on `ℝ` ✓; `½(Bⁿ+B^{−n})=1−n²/2γ²+O(γ^{−4})` ✓, so `Φ_n∈L¹`, the pairing sum is absolutely convergent
and the "1" produces **no** `δ_0` (the `k=0` binomial terms cancel it exactly). The inversion is
available in closed form and should be stated rather than left implicit:
`w_n(u) = −½ e^{−|u|/2} L_n'(|u|)`, i.e. `P_n = −½L_n'`, `deg P_n = n−1`
(`n=1`: `w_1=½e^{−|u|/2}`; `n=2`: `w_2=(1−|u|/2)e^{−|u|/2}`). Free strengthening.
*Defect (minor, `:83` vs `:95`)*: L1(2) states the pairing as `ρ↔\barρ`, the proof uses `ρ↔1−ρ`.
Only the latter gives `B↔B^{−1}` unconditionally; they coincide only on the critical line. Fix `:83`.

## 2. §2.2 — **FALSE as labelled `PROVED`** (`:28`, `:122`, `:130`, and L4 at `:281`)
`Σ_m Λ(m)P_n(log m)/m` is **not** absolutely convergent and not convergent: `P_n` is a degree-`n−1`
polynomial and `Σ_{m≤X}Λ(m)(log m)^{j}/m ≍ (log X)^{j+1}/(j+1)`. For `n=1` the "prime side" is
`−Σ_mΛ(m)/m ~ −log X`. Reproduced: truncations at `X=10²,10³,10⁴,2·10⁵` give
`−3.986, −6.329, −8.635, −11.629` against `−(log X−γ_E)=−11.639`. Divergent, as predicted.
Root cause, which is the *sharp* form of L2(b): `δ=0` means `ŵ_n(±i/2)=Φ_n(±i/2)=∞` (pole of order
`n` on the boundary of the admissibility strip) **and** the prime sum diverges; the two divergences
cancel. So `w_n` is not an admissible test for the explicit formula at all and `λ_n` is **not** a
Weil-functional evaluation in the sense of `thm:Z` — it is only the zero-sum half of one.
Required edits: downgrade §2.2 to `FORMAL` (an identity between two divergent series), delete
"absolutely convergent" at `:28`/`:130`, and move this into L2(b) where it is a strength.
L1 itself is untouched by this (it never uses the explicit formula).

## 3. Theorem L2 — **CONFIRMED**; Proposition L3 — **as scoped, partly heuristic**
(a) correct conditional use of `lem:Rrig` (`main.tex:1239`, hypotheses even+continuous+`L¹`+`w≡1`: `w_n`
meets all but the flat top, so the reading "if it were flat-top" is right); (b) correct against
`def:W` (`main.tex:1116`, `δ>0` required for `|u|≥2T`) and should carry §2 above; (c) correct.
L3's first sentence ("not derivable through Theorem Z") is proved; asymmetries (i) and (ii) (`:181–186`)
are motivation, not proof — label them `REMARK`, not part of the `PROVED` scope.

## 4. Theorem L4 — **mis-sourced hypothesis and wrong label**
- `ng:envelope` (`04-papers/36-obstruction-ledger/main.tex:1082–1086`) states that
`|λ_n^{prime}|≤c√n log n` is **an RH-strength sufficient route** (bound ⟹ RH) and *withdraws* the
former reduction; Paper 36 never defines `λ_n^{prime}`. It is **not** a source for "under RH,
`λ_n = (n/2)(log n+γ_E−1−log2π)+O(√n log n)`". That asymptotic must be cited to
Bombieri–Lagarias/Coffey. Fix `:269`, `:276–279`, `:339`.
- Label: with `λ_n^{(S)}` defined as at `:281` (explicit archimedean term minus a finite explicit
sum), eventual positivity of `λ_n^{(S)}` is **unconditional** — it is arithmetic about an explicit
sequence, with no zeros in it. RH is needed *only* for the sentence "differs from `λ_n` by
`o(n log n)`". Split the statement; `PROVED under RH` (`:339`) over-conditions the part that matters.

## 5. §4.4 numerics — **the script measures no prime sum** (`scripts/r4c/li_phi_check.py:5–29`)
The "residue" column is `λ_n(10⁴ zeros + tail model) − archimedean asymptotic`; it contains the
**tail-model error**, which the text does not mention. At `n=1000` the tail is `134.7` (5.8 % of
`λ_n`), built on the Riemann–von Mangoldt density with relative error `O(1/G)` per zero plus the
counting-function error — an absolute uncertainty of order the quoted residue `2.545` itself. Hence
"the entire prime contribution" (`:307`), "`≈0.1 %`" and "two orders of magnitude below `√n log n`"
are **not established by this run**. `λ_1…λ_4` to 6–7 digits reproduce exactly; `n=5` to 4 digits,
as stated.
Fix available at no cost: the `{2,3}` sub-comb prime side is directly computable from
`w_n=−½e^{−u/2}L_n'(u)`. Computed here (`p^k≤10⁶`):
`n=1: −1.2425`, `n=10: +0.6305`, `n=100: −0.3098`, `n=1000: −1.6374`.
Small, bounded, and it supports L4's conclusion — but it is `−1.64`, not `2.5`. Replace the residue
column's interpretation with this column, and keep the residue only as a consistency check.

## 6. Interpretation (`:149–154`, `:311–317`) — **fair, with one required qualification**
"`λ_n≥0 ∀n` is the termwise strategy" is proved (L1(3)) and the contrast with `cor:nontermwise`
is exact. But `{λ_n≥0 ∀n}` is *equivalent* to RH, so the claim at `:316` must be stated as: *for the
computed range `n≲10⁵` the arithmetic content of `λ_n` is a lower-order correction to a growing
archimedean main term* — an assertion about the finite data, not about the criterion's strength. As
written ("not evidence of the same kind") it is interpretive; label the sentence `INTERPRETIVE`.

## 7. §3 (Nyman–Beurling / Báez-Duarte) — **no overclaim**
The Hilbert-space dual `d_N=sup{⟨1,φ⟩:‖φ‖≤1, φ⊥V_N}` is correct, the direction of the two duals is
correctly opposed, and `HEURISTIC` is the right label. No change.

## 8. Readiness for Paper 47 (§6 of R155_034)
- **Items 1–2 (L1+L2 after `cor:nontermwise`): READY after the §2 fix.** Include the closed form
`w_n=−½e^{−|u|/2}L_n'(|u|)` and state L2(b) in its sharp form (`ŵ_n(±i/2)=∞`, prime sum divergent ⟹
`w_n` is not an admissible explicit-formula test). Do **not** carry §2.2's convergence sentence in.
- **Item 3 (L4 remark after `cor:SC1`): NOT READY.** Re-source the asymptotic to Bombieri–Lagarias,
split conditional from unconditional (§4), and drop or re-qualify the `10⁵`-evidence sentence (§6).
- **Items 4–5: READY** (analogy label and the `Open` edit are accurate).
- `P4 CLOSED` as a route: **sustained.**

## Labels after audit
`L1 PROVED` · `§2.2 FORMAL (was PROVED — error)` · `L2 PROVED` · `L3 PROVED as scoped + REMARK` ·
`§2.6, §4.1–4.3 PROVED as scoped` · `L4 PROVED (sub-comb, unconditional) + CONDITIONAL comparison,
citation to be fixed` · `§4.4 table DIAGNOSTIC, under-determined` · `§3 HEURISTIC`.
