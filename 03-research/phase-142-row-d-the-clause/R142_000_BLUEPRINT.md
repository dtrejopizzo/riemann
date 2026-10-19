# R142.000 — Blueprint, phase 142: the clause (b′)⁺ — necessary conditions, then sufficiency

residue R12), `R141_001` §D.30 (definitions, Thms D.30.1–16 with the blueprint's C5 correction), `R141_004`
(C4: the necessary side of O-18 is not exhausted; (C4.1); Q-A/Q-B split). Plan of reference:
`ROW-D-COMPLETION-PLAN.md` (phase 142 = assembly or obstruction theorem — now: decide the clause).*

Standing rules as in R139_000–R141_000 (labels; zero-free definitions; three falsifiers; corpus check per
idea; numerics only to certify constants). **FATAL rule from line one:** (b′)⁺ ⟹ RH (Thm D.30.10) and
(b′)⁺ is **false for `Ξ_a`** while (a), (c) and the whole frame hold there (Thm D.30.16). Any argument for
(b′)⁺ for `ξ` must therefore name the line where A3 (equimodularity) is used, and — since T2 requires it —
where A7/A8/A9 is used; an argument that runs verbatim for `Ξ_a` is wrong.

## The object
`R(E) := ½I_∞(E,E) − ¼deg E` (`χ = 0`). `S_0 := {E ∈ D^W : deg E > 0, R(E) > 0}`.
**(b′)⁺:** `E ∈ S_0 ⟹ ∃E' ∈ D^W, E' ≥ 0, E' ≢ 0, E − E' ∈ 𝓝_∞.`
**(b′)⁺_st (stable form, D.30.11):** the same with `E` replaced by `nE` for some `n ≥ 1` (the "big divisor"
form); Thm 12.3 survives it and (b′)⁺_st ⟹ RH without A7 (C10).
Equivalent zero-free form: `T(S_0) ⊆ 𝔐` (traces of `S_0` lie in the moment cone of nonnegative classes).

## Q-A — Consistency with every known necessary condition (cheap, refutation-capable; do this first)
1. **(C4.1).** Thm 11.14(ii) gives `|I_∞(E',X)| ≤ C_X·deg E'` for every nonnegative `E'` and every `X`.
   If `E ∈ S_0` and `E' ≥ 0` is as in (b′)⁺, then `I_∞(E',F) = I_∞(E,F)` for every `F` (since
   `E − E' ∈ 𝓝_∞` is in the radical) and `deg E' = deg E`. Hence (b′)⁺ forces: for all `E ∈ S_0` and all
   `F`, `|I_∞(E,F)| ≤ C_F·deg E`. Take `F` primitive and `E = F + tK`-type classes to derive the auditor's
   condition **(C4.1): `C_F ≥ √(−I_∞(F,F)/2)` under RH** (re-derive it exactly: which `E ∈ S_0` gives
   the sharpest bound; the Cauchy–Schwarz step). Then **decide (C4.1)**: `C_F` is the spectral constant
   `C_F ≤ |Φ_F(0)| + |Φ_F(1)| + Σ_ρ|Φ_F(1−ρ)|` (Thm 11.14); under RH `−I_∞(F,F) = Σ_ρ|Φ_F(ρ)|²` for
   primitive `F`; so (C4.1) reads `Σ_ρ|Φ_F(ρ)| ≥ (Σ_ρ|Φ_F(ρ)|²/2)^{½}`-type — check whether it is an
   `ℓ¹ ≥ ℓ²` inequality (true whenever the sequence has an entry `≤ 1`… work it out precisely, including
   the exact constant `C_F` of Thm 11.14, not its upper bound). Outcome: (C4.1) TRUE (necessary condition
   passed) or FALSE (then (b′)⁺ is refuted **under RH**, i.e. strictly stronger than RH, and the phase moves
   to the modification).
2. **All other necessary conditions.** List every unconditional constraint on `𝔐` in the corpus:
   `|Φ_{E'}(ρ)| ≤ (deg⁻E')^{β}(deg⁺E')^{1−β}` (R140 D.24), both rulings `> 0`, `Φ_{E'}(σ) ∈ (0, deg E']`
   on `[0,1]` (R137 D.11.1), the bounds from Thm 11.14 for every `X`, positivity of `E' ⋆ g^∨` for `g ≥ 0`
   (`t_n(E') = PRIME − ARCH` of a nonnegative function — extract the sign information, if any). For each,
   check whether `S_0` satisfies it (under RH where the condition itself is RH-dependent, unconditionally
   otherwise). Any failure refutes (b′)⁺ (or shows it stronger than RH). Record the outcome as a table.
3. **The modification, if needed.** If some necessary condition fails on `S_0`, find the largest
   `S ⊂ S_0` (or the right `χ < 0`, or the stable form, or an extra gate on the rulings) on which all
   necessary conditions pass, such that Thm 12.3's proof still runs (the proof uses `E = rF + K` with `F`
   primitive and `r` large — the modified clause must still cover those). State the modified clause.

## Q-B — Sufficiency: the exponential moment problem (only after Q-A passes)
1. Formulate the problem exactly: given `(a,b) ∈ R_{>0}²` and `z = (z_ρ)_ρ ∈ ℓ¹`-type data satisfying the
   necessary conditions, find `E' ≥ 0` in `D^W` with `deg⁻E' = a`, `deg⁺E' = b`, `Φ_{E'}(ρ) = z_ρ` for all
   zeros `ρ` (order-one). This is a moment problem for the exponential system `{e^{(ρ−½)t}} ∪ {e^{±t/2}}`
   on `R` with a positive measure `E'(t)dt` of prescribed decay.
2. Corpus and literature check (grep first): Krein–Nudelman *Markov moment problem*, Boas, Akhiezer;
   moment problems for exponential systems with complex frequencies; Carleman-type conditions
   (auditor: unavailable here — verify why); Pólya-type kernels as extremal solutions. Which classical
   sufficiency criteria apply to a countable set of complex frequencies `ρ − ½` accumulating at `∞`
   along `Re = 0` (under RH) and what they require of the data.
3. **Where A3 and A8 enter.** For `Ξ_a` the same moment problem has frequencies at `Re = ±a` and the clause
   is false; identify the exact property of the frequency set `{ρ − ½}` (on `Re = 0` under RH — but that
   is the conclusion, not usable) or of the data (the traces are `PRIME − ARCH` of `E ⋆ (τg)^∨`: the prime
   sum has nonnegative atoms `Λ(n)n^{−1/2}` — A8/A4) that a sufficiency proof would use. Honest outcome
   expected: the sufficiency criterion needs the frequencies on a line, i.e. RH — if so, prove that (b′)⁺
   is **equivalent** to RH (closing O-18 positively), which is itself a theorem of record; if some data
   condition replaces it, that is the new mathematics.
4. If (b′)⁺ ⟺ RH is proved: state row D's final reduction as "RH ⟺ the Riemann–Roch-defined `h⁰`
   satisfies effectivity", and assess against T2 what a proof of effectivity would have to use.

## Falsifier protocol (every theorem)
`Ξ_a`: the clause is false; every necessary-condition computation must be run for `Ξ_a` too and the
condition must either fail there (good: it is a candidate A3-line) or pass (then it is not where A3
enters). `Ξ_Q`: frame broken by A7 — record which statements still make sense (D.30.15 says (a),(c) do).
`ζ_K`: every statement must hold verbatim for `ξ_K`.

## Deliverables and rounds
`R142_001_ROUND1.md` (Q-A complete with the table and the decision on (C4.1); Q-B items 1–3;
item 4 if reached; corpus check per idea; paper-facing list; open list; label), README; audit
`R142_002`, repairs `R142_003`, confirmation `R142_004`, closing decision `R142_005`. Scripts only to certify a
constant (e.g. `C_F` for a specific `F` if (C4.1)'s decision needs a number — prefer proof).

## Warnings
* Do not prove (b′)⁺ by an argument valid for `Ξ_a`. Do not define anything through zeros.
* If Q-A refutes (b′)⁺ under RH, that is a result, not a failure: report it and build the modification.
* Keep `χ = 0` unless Q-A forces `χ < 0`; record the reason.
