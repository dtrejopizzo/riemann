# R155.052 — round 8a: the exact negative index of the archimedean form by the multi-band relaxation

*Phase 155, round 8a (item (i) of `R155_056`; order (a) of `R155_060 §4`). Written from the
scripts and certified outputs in `scripts/r8a/` (`README.md`, `r8a_lib.py`, `r8a_01_upper.py`,
`r8a_02_lower.py`, the JSON files). the write-up was cut off before completion; this memo checks
every step against the scripts, fixes one sign and records two further issues (§2.4, §2.3, §3.3), and adds the
structural lemmas (§4) that turn the finitely many certified windows into statements on intervals of `T`.
Inherits Paper 46 `thm:S`, `thm:A`, `prop:arch`, `prop:nodes`, `prop:NC`, `thm:P`, `cor:P1`, `cor:P3`, `rem:P4`,
`thm:J`, `thm:w11` (proof step (c)); `R155_039` (`(H1)`, Theorem J), `R155_047`/`R155_048` (Theorem P, Remark P4
scoped to the two-value relaxation). **Paper 46 and the phase README are not touched.***

**Status.** Labels PROVED / PROVED (machine-verified) / DIAGNOSTIC / HEURISTIC / OPEN. Every
statement is about the **archimedean form `A_∞` alone** (prime comb deleted). **No sign for `ζ` is claimed at
any `T`; no statement about the zeros of `ζ` is made.** Endpoint of record unchanged
(`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, Paper 46 Thm C). No value of `inf W` at `log 2` is asserted.

**Notation (Paper 46 §1, §8, kept exactly).** `I_T = (−T,T)`, `F̂(τ) = ∫F e^{iτt}dt`, `m(τ) = Re ψ(¼+iτ/2) − log π`,
`C₀ = m(0) = ψ(¼) − log π = −γ − 3log2 − π/2 − log π = −5.3721834…`, `τ₀ = 6.28983599` the zero of `m`,
`K(u) = 2Σ_{k≥0}e^{−(2k+½)u}` (`lem:K`), `A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}`, `P_T = {A = B = 0}`,
`Γ_T(F) = (1/2π)∫m|F̂|² = C₀‖F‖² + Lev(c_F)` (`prop:nodes`), `A_∞ = 2AB + Γ_T`, so `A_∞ = Γ_T` on `P_T`;
`λ^P_∞(T)` the bottom of `A_∞` on the unit sphere of `P_T`, `T*_{∞,P} = sup{T : λ^P_∞(T) > 0}` (`prop:arch`).
Legendre basis `e_l(t) = √((2l+1)/2T)·P_l(t/T)`. `S_c = Q_T B_s Q_T` (`c = Ts`) and
`Λ_k(c) = Σ_{j≥k}⟨S_c e_j,e_j⟩ = (2/π)∫_0^c(1 − G_k)` (`thm:P`). Parity: `(RF)(t) = F(−t)`,
`L²_par` the even (`par = 0`) / odd (`par = 1`) functions, `g_0 = cosh(t/2)`, `g_1 = sinh(t/2)` on `I_T`,
`P_T^par := P_T ∩ L²_par`, `λ_par(T)` the bottom of `Γ_T` on its unit sphere, `n_par(T) := n₋(Γ_T|P_T^par)`,
`T*_par := sup{T : λ_par(T) > 0}`. Two constants are kept apart: **`c_* = Tτ_N`** (the Bessel argument, `16` by
default) and **`c_N = m_lo(τ_N)`** (the value of the minorant beyond the last band).

---

## §0 Verdict

1. **(H1) is PROVED at `log 2`: `n₋(A_∞|P_{log2}) = 1` exactly** (Theorem 5.1(iv)): one certified negative
 direction in the even sector, and a certified *absence* of negative directions in the odd sector and of a
 second one in the even sector. The two-value relaxation of Paper 46 floors at `5` there (`rem:P4`, `R155_048`
 Caveat 1); the multi-band relaxation, with 28 bands, returns the exact count.
2. **The whole picture on `(0, 0.90]` is exact up to two thresholds** (Theorem 5.1(iii)):
 `n₋(A_∞|P_T) = 0` for `T < T*_ev`, `= 1` for `T*_ev < T < T*_odd`, `= 2` for `T*_odd < T ≤ 0.90`, with
 **`0.58 ≤ T*_ev ≤ 0.60`** and **`log 2 ≤ T*_odd ≤ 0.81`**, and `T*_{∞,P} = T*_ev`. The glue is a new
 structural lemma: **`λ_ev`, `λ_odd` and `λ^P_∞` are strictly decreasing in `T`** (Lemma 4.3, PROVED — an
 Euler–Lagrange/real-analyticity argument that ends in Weierstrass).
3. **A certified two-sided enclosure of the archimedean threshold: `0.58 ≤ T*_{∞,P} ≤ 0.60`** (Corollary 5.2).
 This is the certified lower bound that round-4 order (d) asked for (`R155_029 §(d)`, `R155_031 §2.C`), to 1.5
 digits rather than 3. It contains the DIAGNOSTIC Galerkin value `0.5958` of Paper 46. As a by-product,
 **`A_∞ > 0` on `P_{½log3}` is now PROVED** (it was DIAGNOSTIC, `λ^P_∞ ≈ +0.083`).
4. **(H1) cannot extend past `T*_odd ≤ 0.81`** (Corollary 5.3): `n₋ = 2` at `0.81, 0.82, 0.90`. This replaces
 the bound `T₂ ≤ 2π/τ₀ = 0.9989426` of `R155_039` by `T₂ ≤ 0.81`. Theorem J gives only `n₋ ≥ 1` at those windows.
5. **OPEN: `n_odd(0.80)`** (hence whether (H1) holds at `0.80`, the right end of the `PATH-TO-D` statement). The
 odd certificate at `0.80` stops at `≤ 1`: the second eigenvalue of the certifying matrix is `−0.0047`. Two
 runs (a finer band grid, 77 bands: `−0.0043`; a longer band range `τ_N = 30`: `−0.0019`) show that the
 residual is set by the constant minorant beyond `τ_N`, not by the band grid (DIAGNOSTIC). A HEURISTIC
 extrapolation says `τ_N ≈ 60` would certify; that run exceeds the 60 s budget and was not attempted.
6. **Script issues found and settled** (§2.3, §2.4, §3.3): a sign error in the border coupling of `r8a_01`
 (fixed; effect on the archived runs `≤ 1.3·10⁻³⁴` against margins `≥ 0.016`, Prop 2.4(d)); the `m''` summand in
 `r8a_lib.m2sup_band` is not `m''`'s but dominates it (valid, conservative, Lemma 2.3); a float rounding in the
 polarisation of `r8a_02` (bounded by `10⁻¹⁰`, Lemma 3.3, and re-certified with `±10⁻⁹` inflation by the new
 `r8a_03_recheck_lower.py`).
 *[amended per R155_061, A1/A2] The audit re-ran the corrected `r8a_01` on all eight archived cases, one at a
 time (13.2–14.0 s each): certificates and margins are **bit-identical** to the archive. The certificates of record
 for the upper bounds are now `scripts/r8a/r8a_01_<T>_par<p>_rerun.json`; Prop 2.4(d) is kept only as a remark.
 The audit also found that `r4a_lib`'s `C₀` guard is not rigorous under `r8a_02`'s import order (error up to
 `≈ 10⁻⁵¹` against a `±10⁻⁵⁵` guard, §3.2); it is absorbed by `r8a_03`'s `±10⁻⁹`, which is therefore the certificate
 of record for every lower bound.*

---

## §1 Corpus check and inputs

`grep -rn "multi-band\|multiband"` (phases 153–155, Paper 46, `05-meta`): only `rem:P4`, `R155_047/048/051/056/060`
and the phase README, all naming the multi-band relaxation as *untested*. `grep "strictly decreas"` over phase 15x
and Paper 46: strict monotonicity of `λ^P_∞` in `T` appears nowhere (`prop:arch(i)` has "nonincreasing" only;
`R153_005` has a strictly decreasing *falsifier* threshold `T*(a)`, a different object). No prior certified lower
bound on `T*_{∞,P}` (`R155_031:117`: "needs a Temple/Kato instrument"). `(H1)`: `R155_029 §1`, `R155_031:106`,
`R155_039` (`HYPOTHESIS`, `T₂ ≤ 0.9989426`), `R155_043:22`.

Inputs used: `thm:S(i)` (`m − C₀ = Σ_k s/(a_k(a_k²+s))`, `a_k = k+¼`, `s = τ²/4`), `lem:mbounds(i)` (`m`
strictly increasing on `τ ≥ 0`), `thm:A` and the Dirichlet-form identity in the proof of `prop:nodes(i)`
(`Lev(c_F) = ¼∬_{I×I}K(|x−y|)|F(x)−F(y)|² + ½∫κ|F|²`, compact embedding of the form domain), `thm:P` (Legendre
diagonal of `S_c`, trace identity), `thm:w11` proof (a)–(f) (the interval Lévy-form enclosure `scripts/r4a/r4a_lib.py`,
valid for `T < arccosh√2 = 0.88137`).

---

## §2 The upper bound `n_par(T) ≤ r` (`r8a_01_upper.py`)

### 2.1 Lemma (bordered inertia). PROVED

Let `q` be a real quadratic form on a real vector space `V` with `n₋(q) < ∞` meaning the supremum of dimensions of
subspaces on which `q` is negative definite, and `ℓ ≠ 0` a linear functional on `V` such that `q(·, v₀)` is finite
for some `v₀` with `ℓ(v₀) = 1`. On `V ⊕ ℝ` put `b(v, ξ) = q[v] + 2ξℓ(v)`. Then `n₋(b) = n₋(q|ker ℓ) + 1`.

*Proof.* Write `v = w + tv₀`, `w ∈ ker ℓ`. Then `b = q[w] + 2t q(w,v₀) + t²q[v₀] + 2ξt`. The substitution
`η = ξ + q(w,v₀)` (invertible, linear) gives `b = q[w] + (t²q[v₀] + 2ηt)`, a `b`-orthogonal direct sum of
`q|ker ℓ` and a non-degenerate binary form of determinant `−1`, inertia `(1,1)`. Negative indices add over
orthogonal direct sums. ∎

It is applied (i) in `r8a_01` with `q = L` (bounded, below) on `V = L²_par(I_T)`, `ℓ = ⟨·, g_par⟩`; (ii) in
`r8a_02` on a 2-dimensional `V`. In both cases `P_T^par = ker ℓ ∩ L²_par`: for even `F`, `A(F) = B(F) = ⟨F, g_0⟩`;
for odd `F`, `A(F) = −B(F) = ⟨F, g_1⟩`.

### 2.2 Lemma (the multi-band minorant). PROVED

Let `0 = τ^{(0)} < τ^{(1)} < … < τ^{(N)} = τ_N` be the band edges (`band_points`, 28 bands by default:
`0.15, 0.3, 0.5, 0.75, 1, 1.3, 1.6, 2, 2.5, …, 8` then 7 geometric edges `9 → τ_N`, `τ_N = c_*/T`). Let `m_lo(τ)` be
the lower end of the interval enclosure `m_interval` (series of `thm:S(i)` to `K₀ = 3000` terms; the tail of the
decreasing summand is bracketed by `½log(1+s/X²)` and `½log(1+s/X²) + f(K₀)`, `X = K₀+¼`). Define `s(τ) = s(|τ|)` by
* `s = C₀` on `[0, τ^{(1)}]` (band 0);
* on band `a ≥ 1`: the chord through `(τ^{(a)}, m_lo(τ^{(a)}))`, `(τ^{(a+1)}, m_lo(τ^{(a+1)}))`, lowered by
 `off_a = max(M2_a, 0)·Δ_a²/8`, where `M2_a ≥ sup_{band} m''` (Lemma 2.3) and `Δ_a` the band width;
* `s = c_N := m_lo(τ_N)` for `|τ| ≥ τ_N`.

Then `s ≤ m` on `ℝ`, `C₀ − (max off) ≤ s ≤ c_N`, and `Γ_T ≥ L := (1/2π)∫s|F̂|²` as forms on the form domain.

*Proof.* Band 0 and the tail: `m` is increasing (`lem:mbounds(i)`), `m(0) = C₀`, `m(τ) ≥ m(τ_N) ≥ c_N`. Band
`a ≥ 1`: the chord `ℓ` through the exact values satisfies `h = m − ℓ`, `h = 0` at the ends, `h'' ≤ M2_a`; if
`M2_a ≤ 0`, `h` is concave, so `h ≥ 0`; if `M2_a > 0`, `h + M2_a(τ−τ^{(a)})(τ^{(a+1)}−τ)/2` is concave and vanishes at
the ends, so `h ≥ −M2_aΔ²/8`. Replacing the exact end values by `m_lo` lowers the chord. `s ≤ c_N` on each band
is asserted at both ends in interval arithmetic (the chord is affine). `Γ_T − L = (1/2π)∫(m−s)|F̂|² ≥ 0`. ∎

*[amended per R155_061, A3/A5] The script's assertion (`r8a_01_upper.py:83`) carries a tolerance `+10⁻³⁰` and so
does not by itself prove `s ≤ c_N`. The inequality holds exactly: every chord end value is `m_lo(τ^{(b)}) − off ≤
m_lo(τ^{(b)})`; the enclosure widths of `m` are `≤ s/X³ ≤ 7·10⁻⁹` while consecutive edge values of the increasing `m`
differ by `≥ 0.03`, so `m_lo` increases along the edges and every end value is `≤ m_lo(τ_N) = c_N`, with near-equality
only at the right end of the last band, whose true value is `c_N − off_N ≤ c_N`. The tolerance only absorbs interval
over-estimation there. Edge count: 20 fixed edges, then the 8 geometric edges `9, …, τ_N` (7 from `geomspace` plus
`τ_N`), 28 bands in all with band 0 = `[0, 0.15]`; `τ_N` is rounded to 6 decimals, so `c_* = Tτ_N ≈ 16`.*

`L` is bounded (`|s| ≤ W + |c_N|`), and `M := c_N − L = Q_T(c_N − s)(D)Q_T` satisfies
**`0 ≤ M ≤ W·S_{c_*}`**, `W := c_N − min s`, because `0 ≤ c_N − s ≤ W·1_{|τ|<τ_N}`. Its matrix in the Legendre
basis is exact moment algebra: for `l − i` even,
`L_{il} = c_Nδ_{il} + (2/π)√((2i+1)(2l+1))(−1)^{(l−i)/2}[Σ_a(α_a ΔI₀^{(il)} + (β_a/T)ΔI₁^{(il)}) − c_N I₀^{(il)}(c_*)]`
with `I_p^{(il)}(c) = ∫_0^c x^p j_i j_l dx` at `c = Tτ^{(a)}` and `s = α_a + β_a|τ|` on band `a` (entries with
`l − i` odd vanish). This is `Lentry` verbatim; the identity is `|ê_i ē̂_l| = 2T√((2i+1)(2l+1))|j_i j_l(τT)|`
with phase `i^{l−i}` (`thm:P` proof). `I_p` comes from the product series `j_ij_l = Σ(−1)^kβ_kx^{i+l+2k}`, `β_k`
exact rationals (`beta_coeffs`, checked against `mpmath` Bessel products to 50 digits); for `k ≥ 2c` the term
ratio is `< 1.5c²/(k+1.5)² < ⅜` (bound `(a+2k)/(a+k) ≤ 2`, `(a+2k+1)/(k+1) < 3`), so the omitted tail is at most
the last term, which is what `BesselMoments` adds.

### 2.3 Lemma (the `m''` bound in the script). PROVED

`m''(τ) = Σ_k a_k(a_k² − 3s)/(2(a_k²+s)³)` (differentiate `Σ s/(a_k(a_k²+s))` twice in `τ`, `s = τ²/4`; checked
against `mpmath.diff` at `τ = 0.1, 1, 3, 6, 10` to 10 digits). `r8a_lib.m2sup_band` sums instead
`u_k(s) = a_k(a_k²/2 − s)/(a_k²+s)³`. For `s ≥ 0`, `u_k(s) − a_k(a_k²−3s)/(2(a_k²+s)³) = a_k s/(2(a_k²+s)³) ≥ 0`,
and `u_k'(s) ∝ 2s − 5a_k²/2`, so `u_k` is decreasing-then-increasing and `sup_{band}u_k` is an endpoint value.
With the positive tail `Σ_{k≥K₀}1/(2a_k³) ≤ 1/(4(K₀−¾)²)`, the returned `M2_a` is `≥ sup_{band}m''`. **The script's
docstring identity is wrong, the bound it computes is valid (conservative).** Kept unchanged for the default
grid; the new `m2sup_band_exact` (exact summand, same endpoint argument: its `s`-derivative is `∝ s − a_k²`) is
used only with `grid=fine`.

### 2.4 Proposition (Haynsworth split, Ky Fan tail, and the certificate). PROVED

Fix `par`, `K = 22`, `K2 = 36`; `E_K = span{e_i : i < K, i ≡ par}`, `Y = E_K^⊥ ∩ L²_par`, `X = E_K ⊕ ℝ`. Write the
bordered form `B(F,ξ) = L[F] + 2ξ⟨F, g_par⟩` in blocks over `X ⊕ Y`.

(a) `B₂₂ = L|_Y = c_N − P_YMP_Y ≥ γ := c_N − W·Λ_K(c_*) > 0`. Indeed `‖P_YMP_Y‖ ≤ W‖P_YS_{c_*}P_Y‖ ≤
W·tr(P^⊥_K S_{c_*} P^⊥_K) = W Σ_{j≥K}⟨S_{c_*}e_j,e_j⟩ = WΛ_K(c_*)`, `P^⊥_K` the projection off *all* `e_j`, `j < K`
(`Y` lies in its range; a positive operator's norm is at most its trace). `Λ_K(c_*) = 2c_*/π − Σ_{j<K}R_j(c_*)`
by the trace identity of `thm:P`, enclosed with both parities (`LamK`), and clipped to `[0, ·]`.
`Λ_{22}(16) ≤ 7.215·10⁻⁶`, so `γ ≥ c_N − 5·10⁻⁵`.

(b) The `Y`-column of `B₁₂` at `e_i` is `−P_YMe_i` (since `⟨c_Ne_i, y⟩ = 0`), at the border it is `+P_Yg`.
Congruence `(x,y) ↦ (x, y + B₂₂⁻¹B₂₁x)` gives `B ≅ S ⊕ B₂₂`, `S = B₁₁ − B₁₂B₂₂⁻¹B₂₁`, so `n₋(B) = n₋(S)`; and
`B₁₂B₂₂⁻¹B₂₁ ≤ γ⁻¹·Gram`, so **`S ≥ R := B₁₁ − γ⁻¹Gram(−P_YMe_i, P_Yg)`**. Entries of `R`:
`R_{ij} = L_{ij} − γ⁻¹⟨P_YMe_i, P_YMe_j⟩`, `R_{iξ} = ⟨e_i,g⟩ + γ⁻¹⟨P_YMe_i, P_Yg⟩`, `R_{ξξ} = −γ⁻¹‖P^⊥_{K}g‖²`.

(c) Tails beyond `K2`: `‖P^⊥_{K2}Me_i‖² = ⟨M^{½}(M^{½}P^⊥_{K2}M^{½})M^{½}e_i, e_i⟩ ≤ ρM_{ii}`, `ρ = WΛ_{K2}(c_*)
≤ 4.0·10⁻²⁰`; hence the `(i,j)` tail is in `±ρ√(M_{ii}M_{jj})` and the `(i,ξ)` tail in `±√(ρM_{ii})‖P^⊥_{K2}g‖`,
exactly as coded. `g_l = √((2l+1)/2T)·2T·i_l(T/2)` from the positive series of `i_l` (ratio `≤ ½` since `T < 1`),
`‖g_par‖² = sinh T ± T` in closed form; `‖P^⊥_{K}g‖² = ‖g‖² − Σ_{l<K}g_l²` exactly.

(d) **The sign.** The archived runs coded `R_{iξ} = ⟨e_i,g⟩ − γ⁻¹⟨P_YMe_i,P_Yg⟩` (wrong sign of the second
term). Since `|⟨P_YMe_i, P_Yg⟩| ≤ W‖P^⊥_{22}g‖` and, from `i_l(z) ≤ z^l e^{z²/2}/(2l+1)!!`,
`‖P^⊥_{22}g‖² ≤ Σ_{l≥22}2T(2l+1)z^{2l}e^{z²}/((2l+1)!!)² ≤ 8.5·10⁻⁷¹` for `T ≤ 0.9` (`z = T/2`), the true `R`
equals a member of the archived interval box plus a matrix `E` supported on the border row/column with
`|E_{iξ}| ≤ 2W‖P^⊥_{22}g‖/γ ≤ 1.3·10⁻³⁴`, `‖E‖₂ ≤ ‖E‖_F ≤ 6·10⁻³⁴`. The script is fixed (`+`); the two new runs
use the fixed code; the archived JSON are kept and are covered by (e).
*[amended per R155_061, A1/A4] The sign `+` was re-derived independently by the audit from the Haynsworth split
(`Y`-columns `v_i = −P_YMe_i`, `v_ξ = +P_Yg`, so `R_{iξ} = g_i − γ⁻¹⟨v_i,v_ξ⟩ = g_i + γ⁻¹⟨P_YMe_i,P_Yg⟩`). Arithmetic:
`‖E‖_F ≤ √22·1.3·10⁻³⁴ = 6.1·10⁻³⁴`; read `≤ 7·10⁻³⁴`. (d) is now a remark only: the corrected script was re-run on
all eight archived cases and the certificates of record are the `_rerun.json` files, which agree with the archive
bit for bit (R155_061 (vi)).*

(e) Certification. `U` = eigenvectors of the midpoint of `R` (float, converted exactly). For `r = 0,1,…` the script
tests, by interval Cholesky of the interval congruence `U_r^TRU_r` (`U_r` = the eigenvectors of index `≥ r+1`),
that every matrix in the box is positive definite, and bisects a certified `μ` with `U_r^TRU_r − μI ≻ 0`. Then
`U_r^TR_{true}U_r ≥ (μ − ‖U_r‖²‖E‖₂)I ≻ 0` (`‖U_r‖ ≤ 1 + 10⁻¹⁴`, `μ ≥ 0.0159` in every run), so `R_{true}` is
positive definite on a subspace of codimension `r+1`, `n₋(R) ≤ r+1`, and

> **`n_par(T) = n₋(Γ_T|P_T^par) ≤ n₋(L|ker ℓ ∩ L²_par) = n₋(B) − 1 = n₋(S) − 1 ≤ n₋(R) − 1 ≤ r`.**

(first inequality: `Γ_T ≥ L`; equality: Lemma 2.1). ∎

*[amended per R155_061, A4] `U` is not "converted exactly": `iv.mpf(repr(float))` encloses the shortest decimal of
each float, and the certificate is for that decimal matrix. `U^TRU ≻ 0` forces `U` injective, so no bound on `‖U‖`
is needed for `n₋(R) ≤ r+1`.*

**Range.** `r8a_01` has no restriction beyond `T < 1` (the `i_l` ratio; asserted in `g_coeffs`). It does not use
`r4a_lib`.

---

## §3 The lower bound `n_par(T) ≥ 1` (`r8a_02_lower.py`)

### 3.1 Proposition (explicit negative plane). PROVED (machine-verified), for `T < 0.88137`

Let `F, h` be the explicit real polynomials of degree `< 18` in `L²_par(I_T)` whose Legendre coefficients are
archived (`F_legendre_coeffs`; `h` = the Legendre truncation of `g_par`; how they were chosen — Galerkin bottom of
the sector, in floats — is irrelevant). If the `3×3` matrix
`B₃ = [[Γ[F], Γ(F,h), ⟨F,g⟩], [Γ(F,h), Γ[h], ⟨h,g⟩], [⟨F,g⟩, ⟨h,g⟩, 0]]` is negative definite on a 2-plane, then
`span{F,h} ∩ ker ℓ` contains a nonzero `F₀ ∈ P_T^par` with `Γ_T[F₀] < 0`, so `n_par(T) ≥ 1` and `λ_par(T) < 0`.

*Proof.* `B₃` is the bordered form of `Γ_T|span{F,h}` with `ℓ = ⟨·,g⟩`. If `ℓ ≠ 0` on the span, Lemma 2.1 in
dimension 2 gives `n₋(Γ|span ∩ ker ℓ) = n₋(B₃) − 1 ≥ 1`; if `ℓ = 0` there, `B₃ = Γ|span ⊕ 0` and `n₋(Γ|span) ≥ 2`.
(Here `⟨h,g⟩ ∈ [0.072, 1.69]` in every run, so the first case holds.) ∎

### 3.2 The enclosures

`Γ_T[F] = C₀c(0) + ∫_0^{2T}(c(0)−c)K + c(0)∫_{2T}^∞K` (`thm:A`, `c = c_F`, supported in `[−2T,2T]`), from `r4a_lib`:
exact interval autocorrelation polynomial; affine sandwich of `K` on 3000 (or 2000) log-spaced panels of `[10⁻⁶,2T]`
(valid because `1/(2sinh(u/2))` is convex and `1/(2cosh(u/2))` concave for `u/2 < arccosh√2`, `thm:w11(c)`; this is
the **range condition `T < 0.88137`**); singular end `K ≤ 1/u + ½`; closed forms for `C₀` and
`∫_{2T}^∞K = log coth(T/2) + π − 2arctan e^T`. **The prime atoms are switched off** (`LF.atoms = []`; `W` loops over
`self.atoms`) and **the pole term is not used** (the script reads `C₀c(0) + INT + c(0)K_tail` from the pieces).
`⟨F, g_0⟩ = (A+B)/2`, `⟨F, g_1⟩ = (A−B)/2` from the exact moment series. `Γ(F,h) = (Γ[F+h] − Γ[F−h])/4`.

*[amended per R155_061, A2/A5] (1) The panels are in the variable `s ∈ [10⁻⁶, 2]` (`u = Ts ∈ [10⁻⁶T, 2T]`). (2)
`r8a_02` imports `r4a_lib` (which sets `iv.dps = 60`, `mp.dps = 80`) and then `r8a_lib` (which resets them to `40`,
`50`); `LevyForm` is built afterwards, so `r4a_lib._constants` forms `iv.mpf(mp.nstr(mp.euler, 60)) ± 10⁻⁵⁵` from a
169-bit `mp.euler`, whose digits are wrong from about the 51st. The `C₀` used by `r8a_02` can therefore miss the true
value by up to `≈ 10⁻⁵¹`, and `r8a_02`'s own `certified_two_negative` flag is **not** by itself a proof. The effect on
every entry is `≤ ‖F‖²·10⁻⁵¹`, covered many times over by `r8a_03`'s `±10⁻⁹` inflation, so the **lower-bound
certificates of record are `r8a_03`'s** (`r8a_03_recheck.json`, re-run by the audit: identical). `iv.dps` inside
`r8a_02` is 40; that affects only widths. (`r8a_lib.C0_interval` itself is rigorous: 45 digits with a `10⁻⁴³` guard.)*

### 3.3 Lemma (float rounding in the polarisation). PROVED

`r8a_02` forms `F ± h` in double precision, so it encloses `Γ[u_±]` with `u_± = fl(F ± h) = F ± h + δ_±`,
`|δ_{±,k}| ≤ 2⁻⁵³|u_{±,k}| ≤ 3·10⁻¹⁶` (all coefficients of `F ± h` are `≤ 2.2` in modulus: `|F_k| ≤ 0.87`, `|h_k| ≤ ‖g‖ ≤ 1.3`). For polynomials of degree `< 18` on
`I_T`, `T ≥ 0.6`: `‖δ‖_∞ ≤ Σ|δ_k|√((2k+1)/2T) ≤ 3·10⁻¹⁴`, `‖δ'‖_∞ ≤ Σ|δ_k|√((2k+1)/2T)·k(k+1)/2T ≤ 4·10⁻¹²`.
By the Dirichlet-form identity (`prop:nodes(i)`) with `K(u) ≤ 1/u + ½`,
`Lev(δ) ≤ ‖δ'‖²_∞T²(2T+2T²) + ½‖δ‖²_∞∫_{I_T}κ ≤ 10⁻²²` (`∫κ = 2∫_0^{2T}∫_d^∞K ≤ 10.7` for `T ≤ 0.9`), and
`|Γ[v+δ] − Γ[v]| ≤ |C₀|(2‖v‖‖δ‖+‖δ‖²) + 2√(Lev(v)Lev(δ)) + Lev(δ) ≤ 2·10⁻¹⁰` with `Lev(v) = Γ[v] − C₀‖v‖² ≤ 50`. So the computed
`Γ(F,h)` is within `10⁻¹⁰` of the true one; `Γ[F]`, `Γ[h]`, `⟨·,g⟩` are enclosed for the exact archived vectors. ∎

`r8a_02` itself certified with the un-inflated box. **`r8a_03_recheck_lower.py`** (new, 0.1 s) rebuilds `B₃`
from every archived JSON, inflates every entry by `±10⁻⁹` (covering Lemma 3.3 and the rounding of the stored
interval ends to double), certifies `−U^TB₃U ≻ 0` over the inflated box by interval Cholesky, bisects a certified
margin `μ`, and re-imposes `T < 0.88137`. Result (`r8a_03_recheck.json`): certified at `0.60`, `0.80`, `log 2`
(even) and `0.81`, `0.82` (odd); `0.90` odd is **out of range** (box certifies, `μ = 0.074`, but the enclosure of
`Γ[F]` is not proved there); `0.75`, `0.78`, `0.80` odd are **not certified** (`Γ[F] > 0`, see §6).

---

## §4 Structural lemmas

### 4.1 Lemma (parity split). PROVED

`P_T = P_T^ev ⊕ P_T^odd`, orthogonal for `⟨·,·⟩` and for `Γ_T`; hence `n₋(A_∞|P_T) = n_ev(T) + n_odd(T)` and
`λ^P_∞(T) = min(λ_ev(T), λ_odd(T))`.

*Proof.* For `F ∈ P_T`: `⟨F_e, g_0⟩ = ⟨F, g_0⟩ = (A+B)/2 = 0` and `⟨F_o, g_1⟩ = (A−B)/2 = 0`, so both parity parts are
in `P_T`; conversely even/odd elements of the two sectors are in `P_T` (§2.1). `m` is even, so
`Γ(F_e, F_o) = (1/2π)∫mF̂_e\bar{F̂_o} = 0` (the integrand is odd). Negative indices add over orthogonal sums. ∎

*[amended per R155_061, A6] Real vs complex. Paper 46 writes `\Ainf` with `2A(F)B(F)`, i.e. on real `F`, while its
`L²(I_T)` is complex. The counts and bottoms are the same either way: for `F = u + iv`, `Γ[F] = Γ[u] + Γ[v]` (`m` even
and real, so the cross term has an odd integrand) and `A`, `B` are real functionals.*

### 4.2 Lemma (monotonicity of the counts). PROVED

For `T < T'`, zero extension embeds `P_T^par` isometrically into `P_{T'}^par` with the same values of `Γ` (`Γ` does
not depend on the window; `A`, `B`, parity unchanged). Hence `n_par` is nondecreasing and `λ_par` nonincreasing in
`T`. In particular an upper bound `n_par(T₁) ≤ r` holds on `(0, T₁]` and a lower bound `n_par(T₀) ≥ 1` on `[T₀, ∞)`,
**without** any range condition at the other windows. ∎

### 4.3 Lemma (strict monotonicity). PROVED

For each `par`, `λ_par` is **strictly** decreasing on `(0,∞)`; so is `λ^P_∞`.

*Proof.* (0) *Attainment.* `Γ` is a closed form on `L²(I_T)`, bounded below by `C₀`, whose domain embeds compactly
(proof of `prop:nodes(i)`). On the closed subspace `P^par_{T'}` a minimising sequence is bounded in form norm, has
an `L²`-convergent subsequence whose limit `F*` lies in `P^par_{T'}` with `‖F*‖ = 1`, and lower semicontinuity gives
`Γ[F*] = λ_par(T')`. (1) Suppose `T' < T` and `λ_par(T) = λ_par(T')`. By Lemma 4.2, `F*` (extended by `0`) is a
minimiser on `P^par_T`, so `Γ(F*, G) = λ⟨F*,G⟩` for all `G ∈ P^par_T` in the form domain. (2) Take
`G₀ ∈ C_c^∞(T',T)` with `∫G₀e^{±y/2} = 0` and `G = G₀ ± RG₀` (sign of the parity). Then `G ∈ P_T^par`,
`⟨F*,G⟩ = 0`, and `Γ(F*,G) = 2Γ(F*,G₀)` (`Γ` is `R`-invariant). Polarising the Dirichlet-form identity, for
disjoint supports `Γ(F*,G₀) = −½∬K(|x−y|)F*(x)G₀(y)dxdy` (absolutely convergent: the supports are at positive
distance). Hence `Φ(y) := ∫K(|x−y|)F*(x)dx` satisfies `∫ΦG₀ = 0` for all such `G₀`, so `Φ = αe^{y/2} + βe^{−y/2}` on
`(T',T)`. (3) For `y > T' ≥ x`, `K(y−x) = 2Σ_ke^{−(2k+½)(y−x)}`, so `Φ(y) = 2Σ_k c_ke^{−(2k+½)y}`,
`c_k = ∫F*(x)e^{(2k+½)x}dx`, `|c_k| ≤ ‖F*‖₁e^{(2k+½)T'}`: a function real-analytic on `y > T'`. The identity
therefore holds on all of `(T',∞)`. As `y → ∞`, `Φ → 0`, so `α = 0`; then `2Σ_kc_kw^k ≡ β` in `w = e^{−2y} ∈
(0,e^{−2T'})`, so `c_k = 0` for `k ≥ 1`; and `c_0 = A(F*) = 0` because `F* ∈ P_{T'}`. (4) With `u = e^{2x}`,
`0 = c_k = ∫ f(u)u^k du` for all `k ≥ 0`, `f(u) = F*(½log u)u^{−3/4}/2 ∈ L¹[e^{−2T'}, e^{2T'}]`; by Weierstrass `f = 0`,
so `F* = 0`, contradicting `‖F*‖ = 1`. The statement for `λ^P_∞` follows from Lemma 4.1. ∎

Consequences. (i) `λ_par(T) < 0` for every `T > T*_par` (take `T' ∈ (T*_par, T)`: `λ_par(T') ≤ 0`, then strict
decrease), and `λ_par(T) > 0` for every `T < T*_par`. (ii) Since the bottom is attained, `λ_par(T) < 0 ⟺ n_par(T) ≥ 1`.
(iii) `T*_{∞,P} = min(T*_ev, T*_odd)`.

### 4.4 Lemma (a certificate `r = 0` gives a strict sign). PROVED

If `r8a_01` certifies `n_par(T) ≤ 0`, then `λ_par(T) > 0`. *Proof.* Then `L ≥ 0` on `ker ℓ ∩ L²_par`. At the
attained minimiser `F*`, `Γ[F*] − L[F*] = (1/2π)∫(m − s)|F̂*|² > 0`, because `m − s > 0` on `0 < |τ| < τ^{(1)}`
(`m` strictly increasing, `s = C₀` there) and `F̂*` is entire and not identically zero. ∎

---

## §5 Results

### 5.1 Theorem (the negative index of `A_∞` on `P_T`, `0 < T ≤ 0.90`). PROVED (machine-verified)

(i) `n_ev(T) ≤ 1` and `n_odd(T) ≤ 1` for `T ≤ 0.90`; `n_ev(T) = n_odd(T) = 0` and `λ^P_∞(T) > 0` for `T ≤ 0.58`;
`n_odd(T) = 0` and `λ_odd(T) > 0` for `T ≤ log 2`.
(ii) `n_ev(T) ≥ 1` for `T ≥ 0.60`; `n_odd(T) ≥ 1` for `T ≥ 0.81`.
(iii) **`0.58 ≤ T*_ev ≤ 0.60`, `log 2 ≤ T*_odd ≤ 0.81`, `T*_{∞,P} = T*_ev`**, and
```
n₋(A_∞|P_T) = 0 for 0 < T < T*_ev,
 = 1 for T*_ev < T < T*_odd,
 = 2 for T*_odd < T ≤ 0.90.
```
(iv) At the listed windows: `n₋(A_∞|P_T) = 0` at `½log3` and `0.58`; **`= 1` at `0.60` and at `log 2`**;
`∈ {1,2}` at `0.80` (`n_ev = 1`, `n_odd ∈ {0,1}`); **`= 2` at `0.81`, `0.82`, `0.90`**.

*Proof.* (i): `r8a_01` certificates `0.58` par 0/1 (`r = 0`), `log2` par 1 (`r = 0`), `0.90` par 0/1 (`r = 1`) — §2.4,
Lemma 2.4(d) for the archived sign — then Lemma 4.2 and Lemma 4.4. (ii): `r8a_02` certificates `0.60` par 0,
`0.81` par 1, re-checked by `r8a_03` (§3.3), then Lemma 4.2. (iii): `λ_ev(0.58) > 0 ⇒ T*_ev ≥ 0.58`;
`λ_ev(0.60) < 0` and monotonicity `⇒ T*_ev ≤ 0.60`; `λ_odd(log 2) > 0 ⇒ T*_odd ≥ log 2`; `λ_odd(0.81) < 0 ⇒
T*_odd ≤ 0.81`; `T*_{∞,P} = min = T*_ev` since `0.60 < log 2`. The count: by Lemma 4.3 consequence (i)–(ii),
`n_par(T) ≥ 1` exactly when `T > T*_par` (off the threshold points), and `≤ 1` on `(0,0.90]` by (i); add over
parity (Lemma 4.1). (iv) is (i)–(iii) at the windows (`½log3 = 0.5493 < 0.58`; `0.60, log 2 ∈ (T*_ev, T*_odd)`
because `T*_ev ≤ 0.60`, `n_ev(0.60) ≥ 1` is certified directly, and `n_odd(log 2) = 0` directly). ∎

*[amended per R155_061, A1/A2] Certificates of record: for (i), the corrected `r8a_01` re-runs
`r8a_01_{0p58,log2,0p90}_par{0,1}_rerun.json` (identical to the archive; the "Lemma 2.4(d)" above means Prop 2.4(d)
and is no longer needed); for (ii), `r8a_03_recheck.json` (not `r8a_02`'s own flag, §3.2).*

The threshold points themselves (`n_par(T*_par) ∈ {0,1}`) are not decided and nothing depends on them.

### 5.2 Corollary (the archimedean threshold, certified). PROVED (machine-verified)

**`0.58 ≤ T*_{∞,P} ≤ 0.60`**, and `λ^P_∞` is strictly decreasing, positive on `(0, T*_{∞,P})`, negative on
`(T*_{∞,P}, ∞)`. In particular **`A_∞ > 0` on `P_{½log3}`** (Paper 46 §8 states this as DIAGNOSTIC,
`λ^P_∞ ≈ +0.083`; the sign is now proved, the value remains DIAGNOSTIC), and `A_∞` is indefinite on `P_{log2}` with
exactly one negative direction. This improves `prop:arch(iv)` (`T*_{∞,P} ≤ 0.74921`) and brackets its DIAGNOSTIC
`0.5958`. The lower half is a certified lower bound on an infimum — the direction a Galerkin value cannot give —
obtained not by Temple/Kato but by an explicit symbol minorant plus an exact finite section plus a Ky Fan-controlled
Schur complement (an "intermediate problem" in the sense of Weinstein–Aronszajn/Bazley; no priority is claimed for
the method). It certifies a **sign**, not a value: a numerical lower bound on `λ^P_∞(0.58)` would need a rerun
with `s` replaced by `s − μ`.

### 5.3 Corollary ((H1) decided on both sides of `log 2`). PROVED (machine-verified)

`(H1)`: `n₋(A_∞|P_T) = 1` on `(T*_{∞,P}, T₂]` holds with `T₂ = log 2` (indeed for every `T₂ < T*_odd`) and fails for
every `T₂ > T*_odd`; so every admissible `T₂` satisfies **`log 2 ≤ sup T₂ = T*_odd ≤ 0.81`**, replacing
`T₂ ≤ 0.9989426` (`R155_039`). Whether `(H1)` holds at `0.80` is `n_odd(0.80) = 0`, which is OPEN (§6). ∎

*[amended per R155_061, A6] Read: `(H1)` holds for every `T₂ < T*_odd` (in particular `T₂ = log 2`) and fails for
every `T₂ > T*_odd`; `T₂ = T*_odd` is undecided. Hence the supremum of the admissible `T₂` is `T*_odd ∈ [log 2, 0.81]`,
which replaces `T₂ ≤ 0.9989426`. (The sentence above conflated `T₂` with this supremum.)*

### 5.4 Comparison with Theorem P / `cor:P3` / `rem:P4` / Theorem J. PROVED (arithmetic of the above)

| `T` | Thm J lower on `P_T` | `cor:P3` upper (quadrature-free / grid, DIAG) | **this memo** |
|---|---|---|---|
| `½log3` | `0` | `5` / `5` | **`0`** |
| `log 2` | `0` | `7` / `6` | **`1`** |
| `0.80` | `1` | `8` / `7` | **`{1,2}`** |
| `0.81`–`0.90` | `1` | — | **`2`** |

`rem:P4` (scoped by `R155_048` Caveat 1): the **two-value** relaxation cannot go below `5` at `log 2`. The
multi-band relaxation with 28 bands reaches the exact value `1`. Honest description of what does the work: the
count is not obtained by counting eigenvalues of `Σ_i(c_i − c_{i+1})S_{T,τ_i}` against a threshold; the multi-band
minorant `L` is handled *exactly* on the first `K = 22` Legendre modes of the sector (a finite interval matrix),
and Ky Fan/`thm:P` enters only through the tail trace `Λ_{22}(c_*) ≤ 7.2·10⁻⁶`, which makes the Schur complement
over the tail a perturbation of size `10⁻⁵`. The prolate/Ky Fan machinery of round 7 is thus used where it is
sharp (the far tail, `k ≫ c`) and not where it is lossy (the plunge region `k ≈ 2c/π`).

---

## §6 The odd sector at `0.80` — OPEN

Certified: `n_odd(0.80) ≤ 1` (`r8a_01`, margin `0.1616`), `n_odd(0.81) ≥ 1` (`r8a_02`). Not certified:
`n_odd(0.80) = 0` and `n_odd(0.80) ≥ 1`.

| attempt | bands | `τ_N` (`c_*`) | `K/K2` | 2nd eigenvalue of `R` (midpoint, DIAGNOSTIC) | runtime |
|---|---|---|---|---|---|
| archived default | 28 | `20` (`16`) | `22/36` | `−0.004690` | `17.8 s` |
| `grid=fine` (new) | 77, `max off = 2.0·10⁻³` | `20` (`16`) | `22/36` | `−0.004331` | `47.3 s` |
| longer range (new) | 28 | `30` (`24`) | `30/44` | `−0.001888` | `18.1 s` |

DIAGNOSTIC reading: refining the grid below `τ_N` (offsets `0.058 → 0.002`) moves the eigenvalue by `3.6·10⁻⁴` only;
extending the bands from `τ_N = 20` to `30` moves it by `2.8·10⁻³`; the earlier `K = 22/26/30` runs at
`c_* = 16` did not move it. So the residual is the **constant minorant `c_N` beyond `τ_N`** — the loss
`(1/2π)∫_{|τ|>τ_N}(m − c_N)|F̂|²`, which for a test with nonzero boundary values decays only like
`τ_N⁻¹` (since `|F̂|² ~ τ⁻²` and `m` grows like `log τ`). HEURISTIC: fitting `e(τ_N) ≈ e_∞ − C/τ_N` to the two
points gives `C ≈ 0.168`, `e_∞ ≈ +0.0037` (compare the DIAGNOSTIC Galerkin value `+0.0033`), hence positivity
for `τ_N ≳ 46`; a safe run is `τ_N ≈ 60` (`c_* ≈ 48`, `K ≈ 60`, `K2 ≈ 75`, and `IVDPS ≥ 70`, because the
alternating Bessel series loses `≈ 2c_*log₁₀e ≈ 42` digits at `c_* = 48`), estimated well over 60 s here, so
**not attempted**. Two cheaper routes, not built: a minorant growing like `c_N + κlog(|τ|/τ_N)` beyond `τ_N`
(needs the moments `∫_{τ_N}^∞ log τ·j_ij_l(Tτ)dτ` on the finite section), or an off-machine run
(`scripts/offmachine/`). DIAGNOSTIC: the `r8a_02` Galerkin bottom of the odd sector is `+0.0684`, `+0.0288`,
`+0.0033` at `0.75`, `0.78`, `0.80` and `−0.0092` at `0.81` (upper bounds on `λ_odd`, so they locate the crossing in
`(0.80, 0.81)` but prove neither sign).

---

## §7 Certified numbers

**Upper bounds (`r8a_01`; `c_* = 16`, `K = 22`, `K2 = 36`, 28 bands unless stated).** `γ ≥ c_N − W·Λ_{22}(16)`,
`Λ_{22}(16) ≤ 7.2150·10⁻⁶`, `ρ ≤ 4.0·10⁻²⁰`, `max off = 0.05791`, entry widths of `R` `≤ 1.7·10⁻¹³`.

| `T` | par | `τ_N` | `c_N` | `W` | `γ ≥` | certified | margin `μ` | midpoint eigenvalues of `R` (DIAG) | runtime |
|---|---|---|---|---|---|---|---|---|---|
| `0.58` | 0 | `27.586` | `1.479384` | `6.8516` | `1.479335` | `n_ev ≤ 0` | `0.015998` | `−2.4127, +0.0160, 0.486` | `88.7 s`* |
| `0.58` | 1 | `27.586` | `1.479384` | `6.8516` | `1.479335` | `n_odd ≤ 0` | `0.047516` | `−0.5052, +0.0475, 0.406` | `87.6 s`* |
| `log 2` | 0 | `23.083` | `1.301146` | `6.6733` | `1.301098` | `n_ev ≤ 1` | `0.420225` | `−2.6833, −0.1573, 0.420` | `106.2 s`* |
| `log 2` | 1 | `23.083` | `1.301146` | `6.6733` | `1.301098` | `n_odd ≤ 0` | `0.041093` | `−0.7042, +0.0411, 0.246` | `21.5 s` |
| `0.80` | 0 | `20.000` | `1.157751` | `6.5299` | `1.157704` | `n_ev ≤ 1` | `0.298000` | `−2.9124, −0.3006, 0.298` | `86.9 s`* |
| `0.80` | 1 | `20.000` | `1.157751` | `6.5299` | `1.157704` | `n_odd ≤ 1` | `0.161624` | `−0.8740, −0.00469, 0.162` | `17.8 s` |
| `0.80` | 1 fine | `20.000` | `1.157751` | `6.5299` | `1.157704` | `n_odd ≤ 1` | `0.162228` | `−0.8708, −0.00433, 0.162` | `47.3 s` |
| `0.80` | 1 (`c_*=24`, `K=30/44`) | `30.000` | `1.563274` | `6.9355` | `1.563078` | `n_odd ≤ 1` | `0.163454` | `−0.8704, −0.00189, 0.163` | `18.1 s` |
| `0.90` | 0 | `17.778` | `1.039940` | `6.4121` | `1.039894` | `n_ev ≤ 1` | `0.185541` | `−3.1091, −0.4203, 0.186` | `87.5 s`* |
| `0.90` | 1 | `17.778` | `1.039940` | `6.4121` | `1.039894` | `n_odd ≤ 1` | `0.144840` | `−1.0218, −0.0934, 0.145` | `89.7 s`* |

\* contended wall clock (§8). The first eigenvalue of `R` is the border's hyperbolic direction (Lemma 2.1), always
negative; `r` counts the others.

*[amended per R155_061, A1] Audit re-runs of the corrected script (default grid, one at a time
23:03–23:05), files `r8a_01_<T>_par<p>_rerun.json`: `0.58` par 0/1, `log 2` par 0/1, `0.80` par 0/1, `0.90` par 0/1
give the same `r` and the same margins `μ` as the rows above to every printed digit, with runtimes 13.2, 14.0, 13.4,
13.5, 13.3, 13.6, 13.7, 13.5 s. These re-runs are the certificates of record.*

**Lower bounds (`r8a_02`, `N = 18`; re-certified by `r8a_03` with `±10⁻⁹` inflation).**

| `T` | par | panels | `Γ_T[F]` enclosure | `⟨h,g⟩` | `μ` (`r8a_03`) | status | runtime |
|---|---|---|---|---|---|---|---|
| `0.60` | 0 | 2000 | `[−0.0070765, −0.0070374]` | `1.23665` | `0.006627` | **`n_ev ≥ 1`** | `27.3 s` |
| `log 2` | 0 | 3000 | `[−0.1542854, −0.1542653]` | `1.44315` | `0.147170` | **`n_ev ≥ 1`** | `55.4 s`* |
| `0.80` | 0 | 2000 | `[−0.3017609, −0.3017216]` | `1.68811` | `0.290056` | **`n_ev ≥ 1`** | `27.4 s` |
| `0.81` | 1 | 2000 | `[−0.0092543, −0.0092091]` | `0.09152` | `0.005124` | **`n_odd ≥ 1`** | `27.8 s` |
| `0.82` | 1 | 2000 | `[−0.0216395, −0.0215943]` | `0.09503` | `0.012368` | **`n_odd ≥ 1`** | `26.4 s` |
| `0.90` | 1 | 2000 | `[−0.1157105, −0.1156653]` | `0.12652` | (`0.07396`) | out of range — not certified (not needed: Lemma 4.2 from `0.81`) | `27.4 s` |
| `0.75` | 1 | 3000 | `[+0.0683709, +0.0683947]` | `0.07232` | — | not certified | `11.0 s` |
| `0.78` | 1 | 3000 | `[+0.0288288, +0.0288527]` | `0.08153` | — | not certified | `10.9 s` |
| `0.80` | 1 | 3000 | `[+0.0032889, +0.0033128]` | `0.08811` | — | not certified | `10.2 s` |

`r8a_02 0.82 par 0` was **not** run: `n_ev(0.82) ≥ 1` follows from `0.60` (or `0.80`) by Lemma 4.2.

---

## §8 Runtime (the 60 s rule)

The archived `r8a_01` runs marked `*` (87–106 s) were launched concurrently (file timestamps 15:32–15:35) and their
`runtime_s` is contended wall clock; they exceed 60 s **as recorded**, and this is a deviation from the rule. The
uncontended cost of the same computation is `17.8 s` (`0.80` par 1, rerun at 22:37) and `21.5 s` (`log2` par 1);
the new runs of this round, made one at a time, took `47.3 s` (`fine`), `18.1 s` (`c_* = 24`) and `0.1 s`
(`r8a_03`). `r8a_02` runs: `10–28 s`; the `55.4 s` of `log2` par 0 is also a concurrent-era figure. No other
computation was made.

*[amended per R155_061, A1] Closed: the audit's sequential re-runs of all eight archived `r8a_01` cases took
13.2–14.0 s each (§7), so every certificate of record was produced within the 60 s rule.*

---

## §9 Labels

| statement | label |
|---|---|
| Lemma 2.1 (bordered inertia) | PROVED |
| Lemma 2.2 (multi-band minorant `s ≤ m`, `0 ≤ M ≤ W S_{c_*}`) | PROVED |
| Lemma 2.3 (`m''` formula; the script's summand dominates it, bound valid) | PROVED |
| Prop 2.4 (Haynsworth split, Ky Fan tail `‖P_YMP_Y‖ ≤ WΛ_K(c_*)`, `K2`-tails, certificate `n_par ≤ r`), incl. (d) the sign correction and its `6·10⁻³⁴` perturbation bound | PROVED *[amended per R155_061: (d) now a remark, bound `≤ 7·10⁻³⁴`; certificates of record = the corrected re-runs `*_rerun.json`, bit-identical]* |
| Prop 3.1 (explicit negative plane ⇒ `n_par ≥ 1`), for `T < 0.88137` | PROVED *[amended per R155_061: machine-verified by `r8a_03` (`±10⁻⁹`); `r8a_02`'s own flag is not a proof, `C₀` guard §3.2]* |
| Lemma 3.3 (polarisation rounding `≤ 10⁻¹⁰`) | PROVED |
| Lemma 4.1 (parity split, counts add) | PROVED |
| Lemma 4.2 (monotonicity of `n_par`, `λ_par`) | PROVED |
| **Lemma 4.3 (strict monotonicity of `λ_ev`, `λ_odd`, `λ^P_∞`)** | **PROVED** (new) |
| Lemma 4.4 (`r = 0` certificate ⇒ strict positivity) | PROVED |
| **Theorem 5.1** (index table on `(0,0.90]`; `n₋ = 1` at `log 2`; `n₋ = 2` on `[0.81,0.90]`) | **PROVED (machine-verified)** |
| **Corollary 5.2** (`0.58 ≤ T*_{∞,P} ≤ 0.60`; `A_∞ > 0` on `P_{½log3}`) | **PROVED (machine-verified)** |
| **Corollary 5.3** (`(H1)` with `T₂ = log 2`; `sup T₂ = T*_odd ∈ [log2, 0.81]`) | **PROVED (machine-verified)** |
| §5.4 comparison table | PROVED (arithmetic) |
| `n_odd(0.80) = 0`, i.e. `(H1)` at `0.80`; `T*_odd > 0.80` | **OPEN** |
| attribution of the `0.80` residual to the tail minorant | DIAGNOSTIC (three runs) |
| extrapolation `e_∞ ≈ +0.0037`, "`τ_N ≈ 60` certifies" | HEURISTIC |
| Galerkin bottoms, midpoint eigenvalues, `T*_ev ≈ 0.5958`, crossing `T*_odd ∈ (0.80,0.81)` | DIAGNOSTIC |
| `r8a_02 0.90` par 1 | not certified (outside `T < 0.88137`); the conclusion `n_odd(0.90) ≥ 1` stands by Lemma 4.2 |

*[amended per R155_061] Audit verdict: all PROVED labels above stand; no FAIL; six AMENDs (A1–A6) applied in place.*

**Row-D label and endpoint of record unchanged** (`λ_min(A_{½log3}) ≥ 8.8577·10⁻⁵`, primitive form). Everything
above concerns the archimedean form with the primes deleted; no sign for `ζ` beyond `T ≤ log 2`, no statement about
zeros.

## §10 Paper 46 proposal (not executed; to be decided after audit)

(1) `prop:arch`: add Lemma 4.3 (strictness; half a page) and Corollary 5.2 (`0.58 ≤ T*_{∞,P} ≤ 0.60`), and turn the
DIAGNOSTIC "archimedean form positive on `P_T` at `½log3`" into a proved sign. (2) After `prop:NC`: replace "the
hypothesis that `n₋ = 1` for `T` above `T*_{∞,P}` is not proved here" by Theorem 5.1 with the §5.4 table. (3)
`rem:P4`: one sentence — the multi-band relaxation, on 28 bands with an exact finite section, returns the exact
count `1` at `log 2`. (4) Remark after `thm:J`: `T₂ ≤ T*_odd ≤ 0.81` in place of `≤ 0.9989426`. (5) Reproduction
section: `scripts/r8a/` (`r8a_01`, `r8a_02`, `r8a_03`), with the range condition of `r8a_02` and the runtime note of
§8. Check every insertion against `def:W`, `eq:W`, the definition of `\PT` and of `\laminfP` (rule
`feedback-check-against-paper-definitions`): in particular the paper's `\laminfP` is the bottom on the unit sphere
of `P_T` with the pole term vanishing, which is `min(λ_ev, λ_odd)` here.

## §11 Weakest points (where to look hardest)

1. **Lemma 4.3.** It carries the interval statements of Theorem 5.1(iii) and Corollary 5.3 (the window statements
 (iv) need only Lemma 4.2). Check: the polarised Dirichlet-form identity for disjoint supports (constant `−½`);
 the Lagrange-multiplier step on `(T',T)` with the *two* constraints `∫G₀e^{±y/2} = 0` (for the sector version only
 one of them is active, the conclusion is the same); analyticity of `Φ` on `y > T'` and the use of `c_0 = A(F*) = 0`.
2. **Prop 2.4(d).** The sign of the border coupling was wrong in the archived runs; confirm the direction of
 `B₁₂` and that the perturbation argument uses a *certified margin* `μ` (it does: the bisection in `r8a_01`).
3. **Lemma 2.3.** The library's `m''` summand is not `m''`'s; confirm domination and quasi-convexity.
4. **Lemma 3.3 / `r8a_03`.** The lower bounds are now certified from the stored float ends with `±10⁻⁹`; the
 stored ends are `float(mpf(x.a))`, `float(mpf(x.b))` (round-to-nearest, not outward) — the inflation covers it.
5. `r8a_02` depends on `r4a_lib` (the `thm:w11` machinery, audited in round 4) with `atoms = []`; confirm that
 `W` is not called for its total (it is called, but only `d['c0']`, `d['INT']` are used, with `LF.C0`, `LF.Ktail`).
6. The Bessel series at `c_* = 16–24` cancels `≈ 14–21` of the 40 interval digits; the intervals stay valid (widths
 `≤ 1.7·10⁻¹³` in `R`), but any rerun at `c_* ≳ 35` needs `IVDPS` raised.
7. `Λ_K` is the Ky Fan tail trace of `thm:P`; in Prop 2.4(a) only "norm ≤ trace" for the positive operator
 `P^⊥_KS_{c_*}P^⊥_K` is used, not the eigenvalue ceiling itself.

*Scripts: `scripts/r8a/` — `r8a_lib.py` (added `m2sup_band_exact`, docstring corrected), `r8a_01_upper.py` (sign
fixed; option `grid=fine`; non-overwriting output names), `r8a_02_lower.py` (unchanged), `r8a_03_recheck_lower.py`
(new), `README.md` (updated). New outputs: `r8a_01_0p80_par1_fine.json`, `r8a_01_0p80_par1_K30_K244_c24.json`,
`r8a_03_recheck.json`. No archived JSON was overwritten.*

*[amended per R155_061] Audit re-run outputs added: `r8a_01_{0p58,log2,0p80,0p90}_par{0,1}_rerun.json` (corrected
sign, sequential, 13.2–14.0 s each, identical to the archive); `r8a_03_recheck.json` regenerated (identical). The
archived JSON are unchanged.*
