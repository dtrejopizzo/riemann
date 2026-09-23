# R154.000 — Lead blueprint, phase 154 (row D): the law of the body — an analytic form for λ_min(M_0 − v·S) on P_T

*Lead of record: Fable 5.1. Opened 2026-09-20. Owner directive: construct it to completion; new mathematics; corpus-check every idea.*

## 0. Target
`A_T(v) := M_0 − Σ_n v_n (S_{log n} + S_{−log n})` on `P_T ⊂ L²(−T,T)`, `M_0 = G_{Γ,T} − m_0`, contacts `n < e^{2T}`.
Phase 153 proved: `λ_min(A_T(v))` is NOT given by axis projections (body ≠ box), NOT by pointwise symbol bounds (Bochner), NOT by
term-by-term variation (D.133), NOT by uncertainty alone (round 5). **Goal: an analytic expression or a proved analytic lower bound
for `λ_min(A_T(v))`, valid at `T = ½log3` and `T = log 2`, sharp enough to reproduce `λ_min(A_T(w_ζ)) > 0` by hand (mesh-free),
and displaying how the joint constraints between `c_F(log 2)`, `c_F(log 3)` and the Gamma energy produce the sign.**

## 1. The one exact structure not yet used: the orbit fibration of the shift part
`Σ_n v_n(S_{log n}+S_{−log n})` commutes with the Z²-action `t ↦ t + k log 2 + l log 3` and decomposes as a direct integral over
orbit representatives `s ∈ Σ_T` of finite weighted graphs `Γ_s`: vertices = orbit points in `[−T,T]`, edges of weight `v_2` (differ by
`log 2`) and `v_3` (differ by `log 3`). Because `log 3/log 2 ∉ Q`, orbits are finite for every `T` but their size and shape vary with `s`
(Lemma 3.1 of R153_019 is the one-shift case: chains of length `⌈2T/a⌉`, eigenvalues `2cos(πk/(m))`). Tasks:
(A1) describe `Γ_s` completely at `T = ½log3` (only `n=2`: chains) and at `T = log 2` (`n = 2,3`): the finitely many graph types, their
measure in `s`, their adjacency spectra (PROVED, explicit). The spectral measure of the shift operator on `L²(−T,T)` follows.
(A2) The Gamma part `M_0` is a compressed Fourier multiplier; it does not respect the fibration. Write `M_0` in the fibre coordinates
`(s, vertex)`: the coupling between fibres is a kernel `K(s, s')` (explicit from the digamma kernel — find the closed form of the
archimedean Weil kernel in `t`: it is the `−log|2 sinh(t/2)|`-type kernel of Bombieri/Burnol; cite exactly, do not guess).
(A3) The problem `λ_min(A_T(v))` becomes: minimise `⟨M_0 f,f⟩ − Σ_s ⟨Adj(Γ_s; v) f_s, f_s⟩` over `f ∈ P_T`. Lower bounds: (i) decouple by
Schur/Feshbach across fibres (corpus: Feshbach is the certificate's tool — reuse the *idea*, not the mesh); (ii) exploit that the graph
spectra are bounded by `2(v_2 + v_3)cos(π/(m+1))`-type values while `M_0` is large on high frequencies: an exact splitting of
`L²(−T,T)` into "graph-coherent" low modes and the rest, with the Gamma energy of the coherent modes computed analytically.
(A4) **Test at `½log3` first** (one shift, chains): can `λ_min(A_{½log3}(w_2)) > 0` be proved by hand this way? Its value is `≈ 10⁻³`
(R153_012), so the argument needs three digits of the Gamma energy of the chain-coherent modes. Then `log 2` (needs `10⁻⁷`: say honestly
whether the method reaches it, and what the exact shortfall is).

## 2. Second line: the law in `v`
`λ(v) := λ_min(A_T(v))` is concave in `v` (inf of affine functions) — trivial, record it. The admissible region `{λ ≥ 0}` is convex.
(B1) Compute the *exact* Hessian of `λ` at `w_ζ` from second-order perturbation theory (the minimiser is a simple eigenvector, R153_019)
and express it in terms of the resolvent `(A_T − λ)^{-1}` on the orthogonal complement: this is the curvature datum of (P153.16)
(apex offset `8.5·10⁻⁶`, 12× first order). Derive the apex location analytically to first order and compare (DIAGNOSTIC).
(B2) Is there a *scaling law*: how does `λ(w_ζ; T)` behave in `T` between thresholds in terms of the fibration data (the graph types
change only at `T` where a new orbit shape appears — compute those breakpoints: they are `T` such that `2T ∈ {k log 2 + l log 3}`,
i.e. `e^{2T} ∈ {2^k 3^l}` — the **3-smooth numbers**!). State as a theorem: the fibration type of `A_T` for contacts `{2,3}` changes
exactly at `T = ½ log N`, `N` 3-smooth (PROVED if true). Check against the measured `c(T)` kinks (R153_012: kinks at `½log2, ½log3`;
are there kinks at `½log4 = log 2`, `½log6`, `½log8`, `½log9`? — for `T > log 2` other contacts enter; separate the effects).

## 3. Rules
Corpus-check every idea (grep 03-research, 04-papers: "orbit", "fibration", "direct integral", "sinh", "Bombieri kernel", "3-smooth",
"Jacobi chain"); labels PROVED / RESTATEMENT / DIAGNOSTIC-NUMERIC / OPEN; FATAL rule; no sign for ζ beyond `T ≤ log 2` (a hand proof
re-proves the certified endpoint; that is its point); numerics only to check identities and to test candidate formulas; scripts in
`scripts/`. Deliverable round 1: `R154_001_BUILDER_ROUND1.md` (≤ 5000 words). Hostile audit follows. The phase continues until the
target of §0 is reached or an exact obstruction theorem replaces it.

## 4. Amendment of 2026-09-20 (owner's directive, sent to the round-1 builder mid-round)
The target is to **create** the object, not to locate `λ_min` among known closed forms. Define `Λ_T(v)` from the fibration data
(graph types `Γ_s`, their spectral measures, the Gamma coupling kernel `K(s,s')`) such that: (i) `λ_min(A_T(v))` is exactly expressed
through `Λ_T` (theorem); (ii) `Λ_T` has an independent characterization — exact recursion/functional equation across the 3-smooth
breakpoints `T = ½ log N`, a variational or integral definition, a differential/difference equation in `T`, or a duality with the symbol
`σ_T` — at least one, proved; (iii) at `½log3` and `log 2` it reproduces the value and the sign by structure. A weaker bound with a
genuine object beats a sharper bound without one. R154_001 must contain a section "The object".
