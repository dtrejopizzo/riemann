# Round 24, memo B — Near-null block of 211 = near-radical family `{Π_T(M∗φ)}`?

Question (index, Part V, 212-22-A, «(d) OPEN»): is the near-null block of phase 211 the same object as the
family `{Π_T(M∗φ)}` of ROUND_021_A/022_A? Labels: PROVED / CITED / ARGUED / OPEN / NUMERICAL.

## 0. Cross-check
- Opened: `ROUND_021_A.md` (in full), `ROUND_022_A.md` §§Part 1–3, `ANNEX_COTEJO_NULLDIR.md` §1.2 and §5;
  211 `ROUND_008_E.md` §§0–2.2, `ROUND_009_B.md` §0, §§2.4–2.6, `ROUND_005_C.md` §1 (Def. 1), `ROUND_017_A.md` (headings
  only); P46 `def:ext` (l.9867), `thm:ext-half` (l.9913), `prop:ext-gauge` (l.9946); index 212-22-A.
- Not opened: P2_SCHUR_001 (only via citation in 021_A), 211 ROUND_005_B, ROUND_007_B, ROUND_009_A, R160_D4_R2, P47.
- Grep («Π_T(M», «prolat», «casi nul», «near-null», «E_T» in 211/212): no memo writes down the identification. The
  ANNEX_COTEJO_NULLDIR §5(c) separates «E(prolates)», «family of responses E_T» and S_T without relating them to M∗φ.
  Hence it does not stop at the cross-check. No sign mechanism is proposed; it is an identification question.

## 1. Literal definitions
**212 (ROUND_021_A §1; ROUND_022_A Obs. 1.1).** `0<η<δ<T`, `χ` smooth even cutoff (=1 on `|t|≤T−η`, support in `I_T`),
`φ ∈ L¹∩L²` with support in `[−(T−δ),T−δ]`, `F_φ = M∗φ`, `Π_T(φ) := χF_φ − A(χF_φ)u_+ − B(χF_φ)u_−`. Moreover
`M∗φ = S_ζ(g∗φ)` with `S_ζh(t) = Σ_{n≥1} n^{−1/2}h(t+log n)`, `g = (−∂²+¼)g_0`, `g_0(t)=(2π²e^{9t/2}−3πe^{5t/2})e^{−πe^{2t}}`.
Identity (1.1): `a_T(Π_Tφ) = 𝔡_T(φ)` doubly-exponentially small (PROVED in 021_A).

**211, low block (ROUND_008_E §2.2; ROUND_009_B §2.5; P46 def:ext).** `λ=e^T`, `N=e^{2T}`, `c=2πN`, `ψ_k` prolates of
`[−λ,λ]`, `d_k = 1−χ_k(c)`, `Ef(x) = e^{x/2}Σ_n f(ne^x)` on `I_T`. Block: `Π_T E·span{ψ_0,ψ_4,ψ_8,…}` (class `+1` in the
even sector; in the odd one, class swapped, floor `d_10`). Law: `λ_j^{ev} ≈ κ_j d_{4j+8}`, `κ_j∈[0.85,2]`, for `4j+8 ≲ 4N`
(NUMERICAL); the minimizer is at angle `10⁻⁴` from `Π_T E span{ψ_0,…,ψ_8}` (NUMERICAL).

**211, «high block» (ROUND_009_B §2.4(iii)).** `k > 4N`, `d_k ≈ 1`; the quotient `M/D → 0` because the high range contains
approximations of the gauge `𝒢_T` (support in `(−1/λ,1/λ)`), on which `E ≈ 0` (ARGUED there).

**211, family `E_T` (ROUND_005_C Def. 1).** `E_T := N′ ⊕ P_𝒞Π(𝒩_η+𝒯)`: block of modes with `s_q ≤ 0` plus responses of the
comb; `dim E_T ≤ 2|𝒩|+2`, block 11/41/125 at `½log5+ε, 1, 1.25` (NUMERICAL there).

## 2. Bridge lemma (PROVED, one line)
Let `ι f(t) := e^{t/2} f(e^t)`. Then `E = S_ζ ∘ ι`:
`S_ζ(ιf)(x) = Σ n^{−1/2} e^{(x+log n)/2} f(ne^x) = e^{x/2}Σ f(ne^x) = Ef(x)`. ∎
With `f_0 := ι^{−1}g_0`, `f_0(u) = (2π²u⁴ − 3πu²)e^{−πu²}` (even, Gaussian times polynomial) and `g∗φ = ι(f_φ)`,
`f_φ(u) := ∫ f_g(ue^{−s}) e^{−s/2}φ(s)ds` (multiplicative convolution, `f_g := ι^{−1}g`). Thus:
- 211 (both blocks) `= Π_T S_ζ ι(f)`, `f` even with support in `[−λ,λ]` (prolates);
- 212 `≈ Π_T S_ζ ι(f_φ)` (with the cutoff `χ`), `f_φ` Gaussian dilations at scales `e^{s}`, `|s| ≤ T−δ`;
- gauge `= S_ζ ι(φ)`, `φ ∈ 𝒢_T`, identically zero on `I_T` (P46 prop:ext-gauge: `Φ_φ` supported in `(−∞,−T]`).
All three are images of the same operator `S_ζ`; they differ in the input class. This is (U) of 022_A with `h = ιf`.

## 3. Approximate inclusion 212 ⊂ low block of 211 (ARGUED; constants not written)
(i) Concentration. For `|s| ≤ T−δ`, `f_g(ue^{−s})` is a Gaussian of scale `e^{s} ≤ λe^{−δ}`: the mass outside `[−λ,λ]` is
`≲ poly(λ)e^{−πe^{2δ}}`; by Gaussian self-duality the transform is a Gaussian of scale `e^{−s} ≤ λe^{−δ}` and the band
outside `[−λ,λ]` is of the same order. Hence `f_φ` is `ε_δ`-concentrated in time and band in `[−λ,λ]²`,
`ε_δ ≍ poly(λ)e^{−πe^{2δ}}‖φ‖_{L¹}` (ARGUED; it is the «localization» that 022_A attributes to self-duality).
(ii) Landau–Pollak (CITED, classical): a function `ε`-concentrated in time and band lies at distance `≲ ε/√(1−χ_K)` from the span of
`ψ_0,…,ψ_K` if `K` is the last index with `d_K` bounded away from 1; here `K ≈ 4N − O(log c · log(1/ε_δ))`.
(iii) `E` on `I_T` sums `≤ N` terms: `‖Ef‖_{L²(I_T)} ≤ poly(N)‖f‖`. With `Π_T` and `χ` bounded:
**`Π_T(M∗φ) ∈ Π_T E·span{ψ_k : k ≲ 4N} + O(poly(N)e^{−πe^{2δ}}‖φ‖)`** (ARGUED).
That is: the family of 212 lives in the image of the LOW prolate block (`k ≲ 4N`), not the high one.
(iv) Correction to ROUND_021_A §2(c): the sentence «cluster = high prolate block (P211-9B: the gauge vectors live in the high
block)» conflates two things. What vanishes in the high block is `E` on inputs close to `𝒢_T` (kernel of the
input), whose images in `P_T` are ≈ 0, not near-null directions of `a_T`. The gauge contributes no direction to the
cluster in `P_T` (PROVED by prop:ext-gauge: image identically zero on `I_T`). The «near-null block» of 211 that can
coincide with `{Π_T(M∗φ)}` is the LOW one.

## 4. What is NOT identified
(a) `E_T` of ROUND_005_C is not this object (PROVED by definition): it is the negative-index block of `a_T` on `L²(I_T)`
plus responses of the comb, built with the values of `Λ`, of dimension `≤ 2|𝒩|+2`; it is not an image of `S_ζ` nor near
null (it contains directions with `s_q<0`). It stays outside the identification.
(b) Reverse inclusion (low block of 211 ⊂ 212): OPEN. `ιψ_k` has Mellin transform analytic only in a half-plane (support
`(−∞,T]`); being in `{g∗φ}` requires `𝓜(ιψ_k)/Φ_g` of exponential type `≤ T−δ`, and `Φ_g ∝ s(s−1)π^{−s/2}Γ(s/2)·(¼−s²…)`
decays like `e^{−π|τ|/4}`: the division grows exponentially. There is no exact inclusion; the approximate one is not proved.
(c) Class selection. In 211 only the class `ε_k = +1` (even sector) is near null; the class `−1` is not
(ROUND_009_B Thm. 1.2: Fourier defect in `[2,4]` in the opposite class; NUMERICAL 008_E §2.2: the bottom of
`Π_T E span{ψ_0,ψ_2}` is `0.108` at `T=0.8`). **Explicit separating vector (NUMERICAL):** `Π_T Eψ_2` is in the image
of the low prolate span of §3(iii) but has Rayleigh quotient `≥ 0.108` (bottom of the two-dimensional span, 008_E §2.2),
hence is not close to the cluster. Consequence: the inclusion of §3 is into the FULL low prolate span; to fall into the
near-null block of 211 one would need `f_φ` to inherit the class `+1`. Since dilation conjugates `ℱ` with the inverse
dilation, `f_φ` is not an eigenfunction of `ℱ` for general `φ`; that its class `−1` projection is small follows only from
near-radicality (1.1) plus the NUMERICAL fact that the class `−1` is not near null. As a structural statement: OPEN.

## 5. Counts
- 212: `N_T(ε) ≳ (4/(πe))e^{2T} ≈ 0.47e^{2T}` (ARGUED in 021_A, (2.1) missing).
- 211 low block: Landau (CITED) gives `≈ 4N` indices with `χ_k ≈ 1`, `≈ 2N` even, `≈ N` of class `+1`; with the law
  `λ_j^{ev} ≈ κ_jd_{4j+8}` (NUMERICAL) one gets `≈ N − 2` even and `≈ N − 2` odd directions below fixed `ε`, i.e.
  `≈ 2e^{2T}` in total (ARGUED: the law is measured only for `j ≤ 4`, `T ≤ 1.2`). Down to threshold `ε = e^{−πe^{2T}}` the count
  drops by `O(log c · πe^{2T}/log…)`; not computed.
- 211 `E_T`: 11, 41, 125 (NUMERICAL), another object (§4a).
- Common upper bound: `exp(2e^T)` (P211-6C, CITED in 021_A). Both counts are `≍ e^{2T}` and compatible with the
  family of 212 being a subspace of fractional dimension (`≈ 0.24`) of the low block of 211; not decided.

## 6. What changes
- If they are the same (low block of 211 = `{Π_T(M∗φ)}` to margin precision): the low block of 211 inherits the description
  «image of `S_ζ` with Gaussian inputs»; the law `d_{4j+8}` would be the prolate reading of the Gaussian localization of
  022_A; the count (2.2) of 021_A would be replaced by Landau (CITED) plus the law of 211, and the pending step (2.1) of
  021_A would become superfluous. All sign attempts of 211 on the low block become attempts on the
  class closed by R160_D4_R2 Thm. 5.1 (Dirichlet convolution on tests); no new sign step.
- If they are not the same (the inclusion of §3 is strict, or the class is not inherited): two near-null families of
  size `≍ e^{2T}` coexist inside the same span `Π_T E(low prolates)`; their difference would be the class/constraint part, which
  is `Λ`-free (ROUND_009_B §3: Thm. 1.1–1.2 hold verbatim for every weight). No sign mechanism appears either.
- In both cases the sign remains in the cluster–complement coupling (021_A §3, P211-17A), not in the cluster.

## Verdict
- `E = S_ζ ∘ ι`: PROVED (one-line computation). Both objects are images of `S_ζ`; compactly supported inputs in
  `[−λ,λ]` (211) versus Gaussian dilations (212); gauge with zero image on `I_T` (PROVED, prop:ext-gauge).
- `{Π_T(M∗φ)} ⊂ Π_T E(span ψ_k, k ≲ 4N) + O(poly(N)e^{−πe^{2δ}})`: ARGUED (Landau–Pollak CITED; constants not written).
- The correct identification is with the LOW prolate block, not the high one; corrects ROUND_021_A §2(c): ARGUED on a PROVED base.
- Inclusion in the near-null block of class `+1` and the reverse: OPEN. `E_T` of 005_C: distinct object (PROVED by definition).
- Counts: 212 `≳0.47e^{2T}` (ARGUED), 211 `≈2e^{2T}` (ARGUED/NUMERICAL). No sign mechanism in any case.
- Single next operation if one wants to close (d): compute numerically the angle between `Π_T(M∗φ)` (φ prolates of
  `[−(T−δ),T−δ]`) and `Π_T E span{ψ_{4j}}` at `T = 0.8, 1.0`; it is identification, not sign.
