# INTEGRATION_204_001 — Integration into Paper 46 of the phase-204 inputs

Phase 204. Backup: `04-papers/46-row-d-dual-certificates/main_pre_204.tex`.
Compilation: `pdflatex` ×2, 0 errors, 0 undefined references, **189 pages**.

## Summary (≤200 words)
The five inputs passed verification against the paper's definitions and were incorporated. Lemma T3 →
`rem:inertiatower` after thm:coer-schur (PROVED; stated in n_−, n_0; the hypothesis "0 ∉ spec(𝔞|𝒫_T)" reduces to
S_{T,k} nonsingular). P1.A → paragraph after the proof of thm:sos, presented as a direct extension (PROVED). Lemma 2.7
→ `rem:sosatoms` with the annihilator step via the construction of prop:cone(ii) written out explicitly (PROVED). PC-2
→ sentence in rem:polarcapdiag (PROVED; 9·10⁻⁸ NUMERICAL). Lemma WT → `prop:WT` after prop:polarcap, **PROVED also in
infinite dimension**: a direct proof was found (decomposition 𝒟^par = 𝒬^par ⊕ ℝh_par + (a2)) that only uses
0 ∉ spec(𝔄_par) and q ≠ 0, and which moreover proves 0 ∉ spec(𝔞|𝒬^par); Haynsworth remains as a finite-dimensional
remark. Finding: the formula 𝔞_T(h_par)=1/q was already in P46 (prop:wh-polarres, with stronger hypotheses); prop:WT
cites it and weakens it. Nothing was left out.

## Verification (P46 conventions)
- 𝔄 = full form 𝔞_T (archimedean + comb) on 𝒟^par_T without the Tate condition; χ_par, ℓ_par, ε_ev=+1, ε_odd=−1,
  𝒬^par = ker ℓ_par (l.≈4160). W_T|𝒟^par = 𝔄 + 2ε ℓ² (thm:parityschur(o)).
- **WT**: g=𝔄⁻¹χ; 𝔞(g,·)=ℓ; kernel of 𝔞|𝒬 is {αg: αq=0}=0; h=g/q; n_−(𝔄)=n_−(𝔞|𝒬)+[q<0], n_−(W)=n_−(𝔞|𝒬)+[𝔤<0],
  𝔤=(1+2εq)/q. Difference: even −[q<−½], odd +[q>½]. Radical: 𝔤=0 ⟺ q=−ε/2. Compact resolvent ⇒ bottom>0 ⟺ n_−=n_0=0.
  Matches the audit's statement. Finite-dimension check with a bordered matrix (Haynsworth at both pivots): matches.
  PROVED.
- **T3**: thm:parityschur(c) + eq:coer-schur (bijection (w,e)↦w−Ke+e). PROVED.
- **P1.A**: the proof of thm:sos only uses Σ|D_i|² ≥ 0. PROVED (trivial).
- **2.7**: c_{F+}−c_{F−} = 2(c_φ(·−a)+c_φ(·+a)); w→0 isolates the atom. log(3/2) ∉ log ℕ, < 2T for T ≥ ½log3. PROVED.
- **PC-2**: (a3) at T + extension by zero; λ^par_A(T)>0 at T suffices. PROVED. Number: NUMERICAL.
- Numbers of prop:WT: q_ev+½ ≈ −2·10⁻⁸ (from 𝔤_ev≈9·10⁻⁸), q_odd ≈ ½−2.5·10⁻⁴ (from 𝔤_odd≈10⁻³), n_−(𝔄_ev)=1
  (rem:wh-index) — NUMERICAL.

## Changes in main.tex (later numbering)
- l.4356–4410: new `prop:WT` + proof + reading paragraph and numbers (after the paragraph following prop:polarcap).
- l.5299–5316: new `rem:inertiatower` (after the proof of thm:coer-schur).
- l.8332–8360: paragraph P1.A + new `rem:sosatoms` (after the proof of thm:sos).
- l.≈11247–11254: PC-2 sentence added at the end of rem:polarcapdiag.
All cite the phase-204 memos (L2_INTERLACE_001, P1_BBSTAR_001, POLAR_CAP_001, AUDIT_204_CLOSURES_001).

## Not integrated
Nothing planned. (Lemma J, F⁻, P2-S.* out of scope, per the audit.)
