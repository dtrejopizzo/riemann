# AUDIT_L_SHARP_4 — audit of R_001 and S_001 (+ S_001_endpoint.py, S_001_localized.py) against AUDIT_L_SHARP_3 (C_G)

Phase 199, ,
and
Sources checked: AUDIT_L_SHARP_3 §6–7 ((C_G), constraints 1–13); F_001 (Thm F.1, Thm F.2, Lemma 3.1, Prop F.5); P_001 (P.1);
Q_001 (moment form). Recomputations (mpmath, numpy) were done in a scratchpad and are not stored in the repo.

**Verdict in one line.** R.0, R.1, R.1′, R.2, R.3 and S.0, S.1(a)–(c), S.2, S.6 survive. S.1(d) is formal. S.3, S.5 and the cΛ
threshold are ARGUED, and they are diagonal-only. **New in this audit (§6, PROVED for ρ ∈ C_c^∞(1,∞), NUMÉRICO check):** the
negativity half (C_G)(b) is the *mirror* of the exterior positivity of the dual data c. It is not a reduction:
  Q(G,G) = −𝔔_line[c] + 2𝔅[ρ] − R(1)·G_h(0) + c₀ρ₀² − 2ρ₀ρ₁.
Nothing here is a sign. (★★) OPEN; row D OPEN.

## 1. R.0 and R.1 (priority 1). Survive.
- **R.0 ✓ PROVED.** We have Φ_s = −F_L and Φ_w|_{w=1−s} = −F_log, so ∂_sF = Φ_s − Φ_w = F_log − F_L.
  Counterexample: take supp ρ ⊂ (1,2). Then ζ_X ≡ 1, F_log = 0 and −∂_sF = F_L = ∫ρ log X·X^{−s}dX ≢ 0 ✓.
- **Conventions ✓ (re-derived).** From ζ(s) = χ(s)ζ(1−s), with |χ| = 1 on the line and χ'/χ(s) = log π − ½ψ(s/2) − ½ψ((1−s)/2):
  2Re(ζ′/ζ)(½+iτ) = log π − Re ψ(¼+iτ/2) = −Θ_∞(τ).
  Hence ∂_σ log|ζ(s)|² = −Θ_∞, ∂_σ log|ζ(1−s)|² = +Θ_∞ and ∂_σ log|χ(1−s)|² = 2Θ_∞ ✓.
- **R.1 ✓ PROVED.** We have |ζ(w₀)|²∂_u|Φ/ζ|² = ∂_u|Φ|² − |Φ|²·2Re(ζ′/ζ)(w₀) = −2Re(F̄F_log) + Θ_∞|F|²,
  because w₀ = s̄ and Re(ζ′/ζ)(s̄) = Re(ζ′/ζ)(s).
  - **Continuity at on-line zeros ✓.** The form ∂_u|Φ|² + Θ_∞|Φ|² contains no 1/ζ. Also, Re(ζ′/ζ) is continuous across a
    zero on the line, because the polar part 1/(i(τ−γ)) is purely imaginary there.
  - R.1′ ✓.
  - cΛ bookkeeping ✓.
- **R.2 ✓.** The step is the identity ∂_u|Φ|² = −2Re(F̄F_log). It is the moment form, so it is a reformulation (REF-D level),
  as the memo says.
- **R.3 ✓ PROVED.** Θ_∞(0) = −5.37218. The zero is at τ₀ = 6.28984 (mpmath). Shallow positivity is CITED (Zhu). The NO-GO
  covers only *pointwise* u-monotonicity, which is a narrow class. It is correctly recorded as narrow.
- **R.4 (ARGUED) is consistent with S.3.** The weight 2log k − log(τ/2π), evaluated at τ = 2πkt, equals log(k/t) ✓.

## 2. S.0–S.2 (priority 2)
- **S.0 ✓.** We have ζ − ζ_X = Σ_{n>X}n^{−w} = ∫_X^∞t^{−w}d⌊t⌋. By Poisson, the k = 0 term is −X^{1−w}/(1−w) and the
  remainder is Σ_{k≠0}∫_X^∞e^{2πikt}t^{−w}dt. At w = 1−s this is t^{s−1}, so the exponent t^{s−1} is correct.
- **S.1(a) ✓ PROVED.** Put t = Xe^v. Then X^{−s}t^{s−1}dt = e^{sv}dv, which gives G_k = −∫_0^∞e^{sv}ρ̂(−ke^v)dv. Put ξ = ke^v:
  G_k = −k^{−s}∫_k^∞ξ^{s−1}ρ̂(−ξ)dξ ✓.
  - Pairing ±k gives the factor c ✓.
  - u_k = k^{−1/2}u_1(·+log k) ✓.
- **S.1(b) ✓ PROVED.** Check: conj F_c(s′) at s′ = 1−s̄ = s reproduces ∫c ξ^{s−1}ζ_ξ(s)dξ ✓. The memo's convergence argument
  ("Σ k^{−1/2}O(k^{−3/2})") is a sketch. A clean proof comes from the audit's Poisson lemma (§6, (P)): the time function of
  G − ρ₀/s is −1_{v>0}P_c, with P_c given in closed form, so the series converges absolutely.
  - **Caveat.** c = O(1/ξ) when ρ(1) ≠ 0. So F Thm F.1, which assumes ρ = O(X^{−2}), does not apply verbatim to the dual data.
    §6 avoids this by using only the *line part* 𝔔_line.
- **S.1(c) ✓.**
- **S.1(d) is FORMAL.** At Re s = ½ the sum Σ_k k^{−s} diverges. "Complete parts sum to −F₀" is meaningful only after
  analytic continuation, i.e. Müntz/Poisson. The statement is true as an identity of continued objects (CITED Titchmarsh
  2.1, 2.11), but the display "summed over ±k" should be read that way.
- **S.2 ✓ PROVED.** Re-derived: ∂_s conj F(s) = −conj ∂_sF(s) on the line, and c♮ = c·log ξ + c_L ✓.

## 3. S.3–S.4 (priority 3)
- **Local weight log(k/t) ✓ (ARGUED).** The Θ_∞ term contributes log(kt) and the log-pairing contributes −2log t.
- **Endpoint law ✓ (ARGUED).**
  - c(ξ) = −ρ(1)sin(2πξ)/(πξ) + O(ξ^{−2}), so |u_k|² averages to ρ(1)²e^{−v}/(2π²k²).
  - ∫_0^∞(log k − v)e^{−v}dv = log k − 1.
  - The script's test function ρ = e^{−(X−1)} and its transform c(x) = 2Re(e^{2πix}/(1−2πix)) are correct ✓.
  - The numbers are as reported. Agreement is 13% at k = 1 and 2% at k = 8. So "confirmed to 2% at k = 8" is accurate, but
    only asymptotically.
- **S.4 ✓ (NUMÉRICO, ARGUED).** Cross terms are of the same order as the diagonal, with decoupling scale log(l/k), independent
  of μ. On span{k ≥ 3} the matrix is PD (NUMÉRICO). NO-GO 𝒦_S^{harm} stands, as a NUMÉRICO falsifier plus an ARGUED class
  statement.

## 4. S.5 sign constants (priority 4)
- **Constants ✓.**
  - −ζ′(2) − ζ(2) = −0.7073858 (mpmath, 30 digits).
  - γ₁ = −0.0728158.
  - Σ_{k≤N}(2log k − log X̄N)/k = −(γ + log X̄)log N − γ log X̄ + 2γ₁ + o(1) ✓ (re-derived from Σ log k/k = ½log²N + γ₁ + o(1)).
- **Status: ARGUED only, and diagonal-only.** By S.4 the cross terms are of the same order as the diagonal. The endpoint
  "total" therefore does not follow from Σ(log k − 1)/k². The memo's NUMÉRICO total (−0.0660 vs trace −0.0542) includes the
  cross terms, but only at K = 8.
- "The global sign is carried by constants of ℕ" is **not PROVED for any class**. It is a heuristic reading of two model
  computations (endpoint, localized).
- §6 below explains why the sign constants look like ζ(2), ζ′(2), γ: they are the constants of 𝔔[c], i.e. of the
  *mirror* positivity, not an independent source.

## 5. S.6 polar mode (priority 5). Survives.
- c₀ = ψ(3/2) − log π = −1.1082399 ✓. (1/2π)∫Θ_∞/(¼+τ²)dτ = −3.1082399 = c₀ − 2 ✓ (mpmath).
- The log-pairing −2∫u u^{log} over v < 0 equals 2ρ₀² − 2ρ₀ρ₁ ✓.
- The 2×2 form [[c₀,−1],[−1,0]] has determinant −1, so it is indefinite ✓.
- The Schur condition is stated correctly. Under §6 the ℓ-coupling **cancels exactly** (see below).

## 6. THE KEY QUESTION (S-dual). Answer: MIRROR, not reduction (PROVED for ρ ∈ C_c^∞(1,∞); NUMÉRICO check)

Notation:
- P_c(y) := e^{y/2}Σ_{k≥1}c(ke^y) on all of ℝ.
- Ψ̌_c = 1_{y>0}P_c, which is the exterior function of the dual data.
- W_Θ is the Fourier multiplier by Θ_∞.
- 𝔔_line[c] := (1/2π)∫[Θ_∞|F_c|² − 2Re(F̄_cF_{c,log})]dτ, the line part of F.1 for the data c (no 2A_cB_c needed).

**(P) Poisson lemma (PROVED; NUMÉRICO 2e−5).** Since c is the Fourier transform of the even extension ρ_e and ρ_e(0) = 0,
Poisson gives
  P_c(y) = e^{−y/2}Σ_{m≥1}ρ(me^{−y}) − ρ₀e^{y/2} for every y ∈ ℝ.
In particular, **1_{y<0}P_c = RΨ̌_ρ − u_pol** (R: y ↦ −y). The interior of the dual is the reflected exterior of ρ minus the
polar mode. Checked numerically against the direct k-sum for a C_c^∞ test ρ on (1,3): maximum deviation 2e−5 at values
of size 0.47.

**(M) Multiplier lemma (PROVED; mpmath to 1e−16).**
- The Mellin transform of the cosine kernel is M(z) = (2π)^{−z}Γ(z)cos(πz/2). Hence c̃♮(z) = (M′/M)(z)c̃(z).
- The FE ζ(1−z) = 2M(z)ζ(z) gives M′/M(z) = −(ζ′/ζ)(1−z) − (ζ′/ζ)(z). On the line this is **real and equals Θ_∞** exactly.
  Checked at τ = 0.3, 2, 14.1347, 40: imaginary part ≤ 2e−16.
- By Müntz (CITED Titchmarsh 2.11), using ∫_0^∞c = 0 and ∫_0^∞c♮ = −½R(1):
  **P_{c♮} = W_ΘP_c − ½R(1)e^{−y/2}.**
  NUMÉRICO on y ∈ (0,4): agreement to 1e−4. The residual is exactly ∝ e^{−y/2}, i.e. it sits in the rank-one constant, as
  expected from quadrature of R(1).

**(A) Algebra of the log weights (PROVED).** The log-weight of G is log t. With ξ = ke^v we have t = Xe^v, so
log t = log(ξX) − log k. Hence
  u_{G_h}^{log} = −1_+(P_{c♮} − Ψ̌_c^{log}),   G_h := G − ρ₀/s.

**Theorem (S-dual, audit).** For ρ ∈ C_c^∞(1,∞):
  **Q(G,G) = −𝔔_line[c] + 2𝔅[ρ] − R(1)G_h(0) + c₀ρ₀² − 2ρ₀ρ₁,**   𝔅[ρ] := (1/2π)∫Θ_∞Re(F·Ḡ_h)dτ.
Here 𝔅 is the Θ_∞-coupling of F (time support y > 0) with G_h (time support y < 0 in the same convention). Only the
off-diagonal archimedean kernel ν enters it, so it is localised at the interface y = 0.

*Proof.*
1. By (A), Q(G_h,G_h) + 𝔔_line[c] = 2[(1/2π)∫Θ_∞|F_c|² − ⟨Ψ̌_c,Ψ̌_{c♮}⟩].
2. By (M), Ψ̌_{c♮} = 1_+W_ΘP_c − ½R(1)e^{−y/2}1_+. So the bracket equals
   −⟨1_+P_c, W_Θ1_−P_c⟩ + ½R(1)⟨Ψ̌_c, e^{−y/2}⟩.
3. By (P), 1_−P_c = RΨ̌_ρ − u_pol, and Ψ̌_c = −u_{G_h}.
4. So the bracket equals 𝔅 − ρ₀ℓ(G_h) − ½R(1)G_h(0).
5. Add 2Q(G_pol,G_h) = 2ρ₀ℓ(G_h) (S.6) and Q(G_pol,G_pol). **The ℓ-terms cancel.** □

*Extension* to PW tails (ρ = O(X^{−2}), ρ(1) ≠ 0, c = O(1/ξ)) is CONDITIONAL on the Müntz step for c♮, which has a log
singularity at 0 and slow decay. The audit believes it holds but has not checked it.

**Consequences.**
- (i) **(C_G)(b) is self-dual, a mirror.** It reads 𝔔_line[c] − 2𝔅 + R(1)G_h(0) − c₀ρ₀² + 2ρ₀ρ₁ ≥ κμ^{−A}dist²(ρ,𝒢̄₁).
  This is exterior positivity of the Poisson-dual data plus interface, residue and polar terms. It is a statement of the
  same type as (★★), so it does **not** reduce L′♯.
- (ii) It explains P.4's NUMÉRICO observation 𝔔 ≈ −Q(G,G) as 𝔔[ρ] ≈ 𝔔[c] (Poisson self-duality of ℤ), up to interface
  terms (ARGUED reading).
- (iii) The residue term −R(1)G_h(0) is the same ½R(1) residue as constraint 13.
- (iv) **cΛ.** With the prime part ×c, the identity acquires +2(1−c)·(1/2π)∫Θ_∞|F_c|². The mirror is exact **only at c = 1**,
  because Re M′/M = Θ_∞ ties weight 1 to Γ_ℝ. So c = 1 is detected by the *exactness of the mirror*, not by the sign of (b).
  This refines S.7(iii).
- (v) **Beurling.** There is no Poisson formula, so there is no (P) and no mirror ✓ (S.7(i)).
- (vi) The S.5 constants (ζ(2), ζ′(2), γ) are constants of the mirror form 𝔔[c] evaluated on endpoint or localized dual
  data. They are not a second source of sign.

## 7. cΛ threshold (priority 7)
½(1 − ζ′(2)/ζ(2)) = 0.784980 ✓ (arithmetic correct). Status: **ARGUED, weak**. It uses only the diagonal law, while by S.4
the cross terms are of the same order. The exact cΛ statement is §6(iv): the mirror defect is 2(1−c)∫Θ_∞|F_c|²/2π, whose
sign depends on the data.

## 8. Updated consolidated statement and constraints
**(★★) unchanged** = (★★_u) = (★★_EM) = (★★_St) = (★★_P) = L′♯. (C_G) is OPEN. Part (b) now has the exact mirror form
(C_G)(b)^∨ of §6(i). Constraints 1–13 stand. Added:
- **14. Harmonics are dilations of a single function; there is no per-harmonic sign.** u_k = k^{−1/2}u_1(·+log k)|_{v>0}, with
  coefficients forced ≡ 1. The diagonal is positive for k ≥ 3 (endpoint law), and the matrix is PD on span{k ≥ 3}
  (NUMÉRICO). Any proof must use the forced coefficients globally.
- **15. (C_G)(b) is self-dual.** By Poisson self-duality of ℤ, −Q(G,G) = 𝔔_line[c] + interface (𝔅), residue (R(1)G_h(0)) and
  polar (c₀ρ₀² − 2ρ₀ρ₁) terms. Proving (b) is proving exterior positivity for the dual data c. Any argument for (b) must
  therefore either work for 𝔔 itself on the class {c}, or exploit the interface terms. It cannot be counted as a reduction.
  The mirror is exact only at weight c = 1 (cΛ).
**Do not retry:** per-harmonic sign; PW-type decoupling; free harmonic amplitudes; treating (C_G)(b) as a reduction of
(★★); ℕ-constants as an independent sign source (they are 𝔔[c]'s constants).

## 9. Label table
| item | memo | audit |
|---|---|---|
| R.0, R.1, R.1′ | PROVED | PROVED (conventions re-derived; continuity at zeros ✓) |
| R.2 | PROVED | PROVED, REF-D |
| R.3 NO-GO 𝒦_R^{pt} | PROVED | PROVED (narrow class); τ₀ = 6.28984 |
| R.4 | ARGUED | ARGUED; equals S.3's log(k/t) |
| S.0, S.1(a)–(c), S.2 | PROVED | PROVED; S.1(b) convergence via the audit's Poisson lemma |
| S.1(d) | PROVED | FORMAL (Σk^{−s} divergent at Re s = ½; valid after continuation) |
| S.3 endpoint law | ARGUED/NUMÉRICO | ARGUED; 13% at k = 1, 2% at k = 8 |
| S.4 NO-GO 𝒦_S^{harm} | ARGUED/NUMÉRICO | stands |
| S.5 ℕ-constants carry sign | ARGUED | ARGUED, diagonal-only; not PROVED for any class; reinterpreted as 𝔔[c] constants |
| S.6 | PROVED | PROVED; ℓ-coupling cancels in the mirror identity |
| cΛ 0.785 | ARGUED | ARGUED weak; exact replacement §6(iv) |
| (S-dual) | OPEN | **RESOLVED: mirror** (PROVED for C_c^∞(1,∞); CONDITIONAL on PW tails; NUMÉRICO lemma checks) |
| (★_S), (C_G) | OPEN | OPEN |

No sign is claimed. (★★) OPEN. Row D OPEN.
