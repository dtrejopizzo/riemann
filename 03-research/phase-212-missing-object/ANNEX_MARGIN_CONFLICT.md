# Annex: the conflict over the margin of λ_A(T)

Reference note. It resolves the contradiction recorded in `05-meta-and-planning/ROUTES-MASTER-INDEX.md`
(l.66, l.590–592, l.833–837, l.4351, l.4484, l.4724, l.4849, l.4979, l.5306) between the doubly
exponential bound and the simply exponential bound for the bottom `λ_A(T) = λ_min(a_T|P_T)`. Where a source
mentions the famous statement, «[H]» is written.

Notation of Paper 46 (P46): `a_T(F) = C₀‖F‖² + 𝔈(c_F) − Σ_n v_n c_F(log n)`, `P_T = {A(F) = B(F) = 0}`,
`A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`, `W_T = a_T + 2AB` (def:W, eq:W), `λ_A = λ_min(a_T|P_T)` («restricted
primitive» bottom), `λ_P` = bottom on the cone `K_prim` (def:PD), `λ_W = λ_min(W_T)` on the whole
domain («complete» bottom). Normalization: `‖·‖ = L²(I_T)`.

---

## §1 Exact statements

**(S1) R160_M4_R1, Theorem B(i)** (`03-research/phase-160-row-d-infinite-T/R160_M4_R1.md`, l.334–336):

> «There are absolute effective constants `C, c, T₀` such that for every `T ≥ T₀`:
> (i) *(upper)* `𝔤̃_ev(T), 𝔤̃_odd(T) ≤ Ce^{cT}e^{−2πe^{2T}}`, and
> `λ^W_T ≤ λ^prim_T ≤ λ^A_T ≤ Ce^{cT}e^{−2πe^{2T}}` [both].»

Quantity: `λ^A_T = λ_min(A_T|P_T)` with the definitions of P46 «verbatim» (l.157–161; same `a_T`, same
`P_T`, `L²` norm). Range: `T ≥ T₀` (not explicit). Label: PROVED, «unconditional» (table l.54).
Record note R1 (l.62, Remark B4 l.393–398): the doubly exponential law «is already in 106.09 Thms 2–3».

**(S2) Panel R160_PC_R1** (`R160_PC_R1.md`, l.198–202):

> «Thm B(i): `X_T = Mχ_T − a u_ev ∈ P_T` (even, `ℓ_ev = 0`), `𝔞_T(X_T) = W_*(X_T − M) = W_*(−E^M_T − a u_ev)
> ≤ Ce^{cT}e^{−2πe^{2T}}`, `‖X_T‖ ≥ ½‖M‖`. Verified. Hence `λ^A_T ≤ Ce^{cT}e^{−2πe^{2T}}`, unconditional.»

**(S3) G2_B6_R2, Theorem M / Corollary M1** (`03-research/phase-159-row-d-two-front-construction/G2_B6_R2.md`,
l.15–17, l.191–194):

> «Theorem M (PROVED, unconditional, new): for every `ε > 0` and every `T ≥ T₀(ε)`,
> `λ^W_T ≤ λ^P_T ≤ λ_min(A_T|P_T) ≤ exp(−e^{(2−ε)T})`.»

Same quantity `λ_min(A_T|P_T)`. Label PROVED. (It is not rederived here: (S1) contains and improves it.)

**(S4) 106_09, Theorem 3** (`03-research/phase-106-global-modular-star-audit/106_09_NEAR_RADICAL_CLUSTER_AND_GAP_COLLAPSE.md`,
l.291–301, §6 l.410–416):

> «For all sufficiently large `L`, `μ⁺_{1,L} ≤ ε_L`, `μ⁻_{0,L} ≤ ε_L`», `ε_L = Cλ^M e^{−cλ²}`, `λ = e^L`;
> «Unconditional: the truncated Riemann-kernel derivative spaces have Weil matrices `O(λ^M e^{−cλ²})`».

Quantity: eigenvalues (second even, first odd) of the complete form `QW` on `[−L, L]`, not `λ_A`
directly. Own label: unconditional. Remark B4 of (S1) states that the test space
`span{v₀, v₂}` contains a vector with `ℓ_ev = 0`, which transfers the bound to `λ^A`.

**(S5) Paper 46, thm:margin and cor:margin1** (`04-papers/46-row-d-sign-radial-intersection-form/main.tex`, l.3530–3580):

> «For every `T ≥ 1`, `λ_W ≤ λ_P ≤ λ_A ≤ 4·10⁹ T e^{−15.449 T}`.»

Quantity: `λ_A` of P46. Range `T ≥ 1`. PROVED (proof via the explicit formula on `P_T`, lem:roughEF,
with a test vector that annihilates only the first zero; footnote: «a property of that family, not a sharp
rate»). rem:moriceiling (l.3582–3591): cites a bound `exp(−4π e^{2T})` of Mori **for `λ_W`**, «plausible,
unverified»; «It bounds `λ_W ≤ λ_A` and so does not replace Corollary cor:margin1 as a bound on `λ_A`.»

**(S6) Paper 48 §subsec:margin** (`04-papers/48-routes-to-weil-positivity/main.tex`, l.265–276):

> «A doubly exponential upper bound `exp(−e^{(2−ε)T})` for `λ_A` is *not* proved; earlier versions of this
> map stated it as a theorem, and that statement is withdrawn.»

Declared source of the withdrawal (table l.945): «index correction after the shape theorem of P46». No
step of (S1) or (S3) is pointed out as failing.

**(S7) Index 06, entry [margin]** (`ROUTES-TRIED-INDEX/06_OPEN_RESIDUES_DEAD_SUBROUTES.md`, l.19 at HEAD):

> «The doubly exponential estimate cited in P46 rem:moriceiling concerns λ_W, is recorded there as
> unverified, and must not be transferred to λ_A (λ_W≤λ_A has the wrong direction for that transfer).»

---

## §2 Is it the same quantity?

(S1), (S2), (S3), (S5), (S6) all speak of `λ_A(T) = λ_min(a_T|P_T)` with the normalization of P46.
(S1) declares that it uses the definitions of P46 verbatim, and its `𝔞_*` (D3) restricted to `𝒟_T` coincides with
`a_T` (`Σ (v_n/2)[c(log n) + c(−log n)] = Σ v_n c(log n)` by symmetry of `c_F`).

(S7) speaks of **another** estimate: Mori's, cited in rem:moriceiling, which bounds `λ_W`. The relation is
`λ_W ≤ λ_P ≤ λ_A` (P46 rem:Kprim: `W_T = a_T` when `A·B̄` is purely imaginary, and `P_T ⊂ K_prim`; CITED,
P46). Hence an upper bound for `λ_W` gives nothing for `λ_A`; (S7) is right **about Mori**.

The error is in the propagation: the master index (l.592, l.4351, l.4484, l.5306) and P48 applied the
correction of (S7) to Theorem M and to (S1), which do not go through `λ_W`: both build a test vector
**inside `P_T`** and bound `a_T` directly. The two doubly exponential bounds of the corpus are
therefore distinct: Mori's (`λ_W`, CITED unverified) and that of (S1)/(S3) (`λ_A`, memo PROVED).

---

## §3 The proof of (S1) and its check

Objects (R160_M4_R1 §1): `K_Pó(t) = Σ_n (4π²n⁴e^{9t/2} − 6πn²e^{5t/2}) e^{−πn²e^{2t}}`, with `Φ_{K_Pó} = ξ`
(P47 Def–Thm 11.7, (11.9)); `M := −K_Pó″ + ¼K_Pó`, so that `Φ_M(s) = s(1−s)ξ(s)`, `A(M) = B(M) = 0`,
`M` even and nonzero. Cutoff `χ_T ∈ C_c^∞(I_T)`, `χ_T = 1` on `[−T+θ, T−θ]`, `θ = e^{−2T}`. Tail
`E := M(1−χ_T)`. `u_ev ∈ C_c^∞(−½,½)` even with `ℓ_ev(u_ev) = 1`; `a := −ℓ_ev(E)`.

**Test vector:** `X_T := Mχ_T − a u_ev ∈ C_c^∞(I_T)`, even, `ℓ_ev(X_T) = 0`, hence `A = B = 0`: `X_T ∈ P_T`.

Steps and check:

1. **`W_*` on the radical (Lemma 2(a),(c)).** For `X, Y` in the Weil class `D^W`,
   `W_*(X,Y) = Σ_ρ Φ_X(ρ)Φ_Y(1−ρ)` (explicit formula, P47 Thm 11.3; CITED). Since `Φ_M` vanishes at every
   zero of `ξ` **wherever it is**, `W_*(M, ·) ≡ 0`. It uses no information about the position of
   the zeros: correct. The extension to `Z ∈ 𝒟_T` uses density of `C_c^∞(I_T)` and bound 2(b).
   *Check:* for `Z ∈ C_c^∞(I_T) ⊂ D^W` the identity is direct; 2(b) is Cauchy–Schwarz plus
   `m ≤ C₀ + c(1+|τ|)` and Plancherel. Correct.
2. **Coincidence of forms.** For `X_T ∈ C_c^∞(I_T)`, `c_{X_T}(log n) = 0` if `log n ≥ 2T`, so the
   sum over all `n ≥ 2` of `W_*` coincides with the truncated sum of `a_T`; and `W_T(X_T) = a_T(X_T)` because
   `AB = 0`. It is the same identity that P46 uses in step (2) of thm:margin (lem:roughEF). Correct.
3. **Reduction to the tail.** `X_T − M = −(E + a u_ev) =: −Y`, `Y ∈ D^W`, even, `ℓ_ev(Y) = 0`. By step 1,
   `a_T(X_T) = W_*(X_T) = W_*(Y) = W_*(E) + 2a W_*(u_ev, E) + a² W_*(u_ev)`. Correct (bilinearity).
4. **Size of the tail (Lemma 3).** `|K_Pó^{(j)}(t)| ≤ c_j e^{(9/2+2j)|t|} e^{−πe^{2|t|}}`; on the support of
   `E`, `e^{2|t|} ≥ e^{2T} − 2`, and `|χ_T^{(k)}| ≤ c_k e^{2kT}`. Hence `‖E‖_{H¹}, ∫|E|e^{|t|/2}, |a| ≤
   Ce^{cT}e^{−πe^{2T}}`. *Check:* correct; the factor `θ^{−k}` is only `e^{2kT}`, absorbed in `e^{cT}`.
5. **`|W_*(E)| ≤ Ce^{cT}e^{−2πe^{2T}}`.** Term `2AB(E)`: product of two quantities `O(e^{cT}e^{−πe^{2T}})`.
   Archimedean term: `≤ C‖E‖²_{H¹}`. Primes with `log n ≤ 2T+1`: `Σ v_n ≤ Ce^T` times `‖E‖²`. Primes with
   `log n > 2T+1`: `|c_E(log n)| ≤ ‖E‖_{L¹} sup_{|s| ≥ (log n)/2}|E(s)|`, and the supremum is `≤ e^{−πn^{…}}`;
   the memo writes «`O(e^{−πe^{2T+1}})`» for the sum, which is careless (the factor `‖E‖_{L¹}` is missing),
   but with that factor the term is `≤ Ce^{cT}e^{−πe^{2T}}·e^{−πe^{2T+1}} ≤ Ce^{cT}e^{−2πe^{2T}}`; and even
   without it, `e^{−πe^{2T+1}} ≤ e^{−2πe^{2T}}` because `e > 2`. Correct.
6. **Cross terms.** `|W_*(u_ev, E)| ≤ Ce^{T/2}‖u_ev‖ 𝔪_T(E)` (Lemma 2(b)) and `|a| ≤ Ce^{cT}e^{−πe^{2T}}`
   give `O(e^{cT}e^{−2πe^{2T}})`; `a² W_*(u_ev)` likewise (`u_ev` fixed). Correct.
7. **Normalization.** `‖X_T‖ ≥ ‖M‖ − ‖E‖ − |a|‖u_ev‖ ≥ ½‖M‖` for `T ≥ T₀`, hence
   `λ_A ≤ a_T(X_T)/‖X_T‖² ≤ 4Ce^{cT}e^{−2πe^{2T}}/‖M‖²`. Correct.

**Which step P48 or another source declares failing:** none. P48 withdraws the statement without pointing to a step; its
only declared source is the index correction (S7), which refers to Mori's bound on `λ_W`.
No later memo located objects to Lemma 2, Lemma 3 or the vector `X_T`.

**Weakest step, according to this check:** Lemma 2(a) applied to pairs in `D^W` without compact support: the
explicit formula for functions with decay `O(e^{−(1+ε)|t|})` with two derivatives, with the prime sum
over all `n` and the sum over zeros absolutely convergent. It is the standard version of Weil's explicit
formula (P47 Thm 11.3, (11.2), (E3d)); absolute convergence of `Σ_ρ Φ_X(ρ)Φ_Y(1−ρ)` for
`X, Y ∈ D^W` follows from `Φ_{g″}(s) = (s−½)²Φ_g(s)` (two integrations by parts) and from the density of
zeros. I consider it correct; it remains a CITED dependence on P47, not rederived here line by line.
The constants `C, c, T₀` are not explicit: the bound is not numerically usable in a given window.

---

## §4 Verdict and consequences for OBJECT_SPEC

**Verdict: (b).** For `λ_A(T)` on `P_T` as defined by P46, it is proved (memo R160_M4_R1,
Theorem B(i); verified by the panel R160_PC_R1; rechecked step by step in §3):

  `λ_A(T) ≤ C e^{cT} e^{−2π e^{2T}}`  for `T ≥ T₀`, with effective absolute constants not made explicit.

Honest label: **PROVED (in the memo corpus), dependent on P47 Thm 11.3 (CITED)**, not integrated
in P46. What P46 contains as a theorem of the paper is only the simple bound (S5), PROVED with explicit
constants for `T ≥ 1`. The withdrawal in P48 and the index entries saying «doubly exponential not
proved for `λ_A`» come from transferring to (S1)/(S3) a correction written for Mori's bound on
`λ_W` (S7); that transfer is incorrect. (S7) remains correct regarding Mori. Theorem M
(S3) is superseded by (S1) and is not rederived here. 106_09 (S4) is an eigenvalue bound for the complete
form; its transfer to `λ_A` depends on Remark B4 (vector with `ℓ_ev = 0` in the test space),
which is not rechecked here and is not necessary, because (S1) directly gives the vector `X_T ∈ P_T`.

As long as P46 does not incorporate (S1), what is citable in a paper is (S5); in the notes of phase 212 (S1) is used.

**Consequences for the object.**

- With (S1): an identity «`a_T = non-negative expression + remainder`» intended to give the sign must control
  the remainder with relative precision below `Ce^{cT}e^{−2πe^{2T}}` in the window `T`; already at `T = 2`
  that is of order `e^{−340}`. Every coarser perturbative, compactness or gap bound does not decide the
  sign. In particular the «manifestly non-negative» term cannot have a minimum on `P_T` bounded
  below by anything larger; it has to vanish (at that scale) on the truncation `Mχ_T` of the Riemann
  kernel, which is an explicit near-null vector of the object. This is a useful internal falsifier: the
  object must evaluate `X_T` within `O(e^{cT}e^{−2πe^{2T}})`.
- With only (S5): the threshold would be `4·10⁹Te^{−15.449T}`, much more permissive; designing with that threshold
  would underestimate the precision needed on a doubly exponential scale. By (S1), the correct design
  threshold is the doubly exponential one.
- (S1) is only an upper bound: it gives no information about the sign (B(ii) of the same memo gives the
  reverse direction only up to a defect `e^{cT}e^{−πe^{2T}}`, without sign).

**Pending correction (for whoever edits the index and P48, not done here):** entries l.592, l.837,
l.4351, l.4484, l.5306 of the master index and P48 l.275–276 must distinguish Mori's bound (`λ_W`, CITED
unverified) from that of R160_M4_R1 B(i) (`λ_A`, PROVED in memo, not integrated in P46).
