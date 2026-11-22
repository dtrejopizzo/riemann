# R166_502 — Pre-check of the join P7 + Q25 (Dirichlet square × identity-level Λ = μ*log)

Phase 166, requested by R166_405 ("P7+Q25, after checking against phase 161 and W-TK").
Labels: PROVED / PROVED-CITED (corpus) / ARGUED / OPEN. Read-only survey plus one short computation (§5).
Files read: E70_10, E70_11, E70_12 (phase 70); phase-161 README, R161_000, R161_001, R161_002, R161_004;
R166_301 §1–5; R157_002 #30, #55 and §4; grid R162_2300 §3 (walls) and the entries for F54 / phase-70 / F36.

## Verdict (short)

**REPEAT. Not admissible as a round.** The join was already made in phase 70 itself:
E70_11 builds the prime current through Λ = μ*log as the Möbius connection V = Z⁻¹δZ, and E70_12 computes
its Riccati identity, which *is* Selberg's identity Λ·log + Λ*Λ = μ*log². E70_12 records "no free lunch":
every term is Euler-side, and the remaining statement (Gamma–Euler connection bound) is AHM = Ω₇, i.e. **E1**.
The new computation in §5 shows why Selberg cannot reach the ratio comb: Selberg rewrites the **convolution**
square V² (support log ℕ). The Hermitian square V*V lives on log ℚ₊. Its non-integer ratio part is exactly the
**cross-prime** sum Σ_{p≠q} V_p*V_q. Möbius inversion does not act on it. The join evades no wall.
Killers: E70_12 (E1), E70_10 (F2/W4), P121 CMO no-go via R161_004 Cor 3.1, R157_002 #55 (F3).

## Status table

| # | Statement | Label | Source |
|---|---|---|---|
| 1 | (I−V)*(I−V) = I − T_Λ + V*V. So A − T_Λ is this square iff A = I + V*V | PROVED (algebra) | E70_10 |
| 2 | V*V = c₁I + Σ_{r∈ℚ,r>1} c_r(S_{log r}+S_{log r}*), c_r = (ab)^{-1/2-ε}Σ_j Λ(aj)Λ(bj) j^{-1-2ε} ≥ 0, c₁ divergent as ε→0 | PROVED | E70_10 |
| 3 | Linear Dirichlet-square no-go (wall F2 / W4, grid F54) | PROVED (structural) | E70_10 |
| 4 | Sum×product square (PC): S_N A_M 𝓕 = {X,E_N} − L*E_N − JH − H𝓕. Its square ‖S_N A_M 𝓕F‖² is even in A_M | PROVED | R161_001 Thm 3.1, R161_002 Thm 1.1 |
| 5 | The phase-161 square ≠ the P7 square (it squares A_M, not V) | PROVED (by inspection) | here §2 |
| 6 | P7 is a one-sided (half-line Hardy/Wiener–Hopf) Toeplitz object, not truncated. V*V = T_{\|D_ε\|²} exactly | PROVED | here §3 |
| 7 | W-TK(a) (truncation) and W-TK 4.1 (kernel sign-blindness) do not apply to the factorization statement. The factorization is equivalent to the pointwise symbol identity m = 1 + \|D_ε\|², which is false | PROVED | here §3 |
| 8 | Q25 = "identity-level use of Λ = μ*log at a load-bearing step": a region with no object and no statement | PROVED-CITED | R157_002 #30, §4 |
| 9 | The identity-level object for P7 already exists: V = Z⁻¹δZ (E70_11); its curvature is Selberg's identity (E70_12) | PROVED | E70_11, E70_12 |
| 10 | Exact support of V*V: the non-integer ratio part = Σ_{p≠q} V_p*V_q (j = 1 only); the integer part is the prime-power atoms c_{p^k} | PROVED | here §5 |
| 11 | Selberg / Möbius / log ζ / full Z / μ-weighted variants do not remove term 10 | PROVED | here §5 |
| 12 | Join P7+Q25 admissible | **NO: REPEAT** (E1 via E70_12; F2 via E70_10; F3 via #55; CMO no-go) | — |

## 1. Phase 70: the operator identity and wall F2

**Set-up (E70_10).** The space is the additive Hardy model L²(ℝ₊), with S_a f(t) = 1_{t≥a} f(t−a), a unilateral isometric shift.
- T_Λ = Σ_{n≥2} Λ(n) n^{-1/2}(S_{log n} + S_{log n}*) is the prime-shift operator.
- A is the Gamma/polar (archimedean) operator.
- The target is AHM: A − T_Λ ⪰ 0, which is Ω₇.

The candidate square is V = Σ Λ(n) n^{-1/2} S_{log n} (Abel version V_ε with n^{-1/2-ε}), with V + V* = T_Λ:

  (I−V)*(I−V) = I − T_Λ + V*V.

So the square proves AHM only if **A = I + V*V**. More generally, A − T_Λ = (G−V)*(G−V) contains V*V.

**How V*V gives the comb.** Use S_a*S_b = S_{b−a} (b ≥ a), = S_{a−b}* (a > b). Then V*V = Σ_{m,n} b_m b_n S_{log m}*S_{log n} contains shifts at log(n/m). After grouping r = a/b in lowest terms:

  c₁(ε) = Σ Λ(n)² n^{-1-2ε} (→ ∞),  c_r(ε) = (ab)^{-1/2-ε} Σ_{j≥1} Λ(aj)Λ(bj) j^{-1-2ε} ≥ 0.

**Wall F2 (grid §3, W4 "wrong sign / orientation").** In the grid, F54 (E70_10) is DEAD [F2] and annotated "manufactures Euler ratio-comb terms; a viable factor needs a grading/quotient cancelling the Euler square". The grid's phase-70 entry is DEAD [F2; per-prime positivity insufficient], with residue "open Euler–Möbius connection identity".
- F2 in general: unconditional positivities give lower bounds, while RH is an upper bound. A positive square adds positive mass of the wrong orientation.
- Here concretely, A is canonical and zeta-free, so it carries no ratio-comb channel log(p^k/q^l). The comb has nonnegative coefficients and cannot cancel inside V*V.
- Putting the comb into A makes A non-archimedean. That is the forbidden circular insertion (Euler/KMS into the archimedean side).
- c₁(ε) also diverges, giving incoherent critical mass. This is the S_abs ceiling of phase 67 / E70_5–7.
- E70_10's own conclusion: only a graded/supersymmetric cancellation, a nilpotent Euler differential, or a nonlinear Euler–Gamma identity could survive.

## 2. Phase 161: the sum×product square

**What it is.** R161_001 Thm 3.1 (PROVED) gives the finite Poisson–Chebyshev anomaly identity (PC):

  S_N A_M 𝓕 = {X, E_N} − L_M* E_N − J H_{M,N} − H_{M,N} 𝓕,

with:
- S_N = Σ_{n≤N} n^{-1/2} τ_{log n} (Müntz);
- E_N = S_N 𝓕 − J S_N (finite Poisson defect);
- H_{M,N} = L_M S_N − K_N (hyperbola), which has no coefficient at k ≤ N because Λ*1 = log (Thm 2.1);
- A_M = M − (L_M + L_M*), the finite Weil operator.

The canonical square is Q = ‖S_N A_M 𝓕F‖².

**Relation to V*V.** It is a **different square**.
- Phase 161 squares the *Weil operator* A_M after multiplying by the Müntz operator. Arithmetic enters linearly, through Λ*1 = log in H.
- P7 squares the *prime current* V alone, and A is supposed to absorb V*V.
- They share one feature: the oriented pairing ⟨A_M G, S_N*S_N G⟩ (R161_002 (OR)) contains S_N*S_N. That is the Müntz analogue of V*V, also on the ratio set log(n/m). R161_002 notes that its positivity "does not make (OR) nonnegative".

**Verdict and killer.**
- Thm 1.1 (PROVED): Q is invariant under A_M ↦ −A_M, so it is **sign-blind** (orientation gate fails).
- Uncompressed oriented pairings reduce to the window shift (R160_D4_R2 Thm 5.1).
- §8: the positive-weight tail is killed.
- R161_004 closes the scalar Stieltjes continuation (Paper 41 C4–C5, negative square) and the divisor-fibre continuation (phases 104/106, zero gap).
- R161_004 also closes **unitriangular Möbius elimination** (P121_CMO_SOURCE_MATRIX_NO_GO): the logarithmic connection Z∂Z⁻¹ is strictly lower triangular. The derivation that creates Λ annihilates the identity diagonal (Cor 3.1).
- The grid lists F54 as "supersedes_or_dup: R161_001–004". W4 records "the sum×product square contains the truncated Weil square (R161_002)".

**Relevance to the join.** R161_004 Cor 3.1 already forbids a "Möbius history" repair of the square. That is precisely the Q25 move applied to P7.

## 3. W-TK vs P7: truncated or full line? Kernel or factorization?

- **P7 is one-sided, not truncated.** It lives on L²(ℝ₊), with no window projection P_T. For isometric unilateral shifts, S_a*S_b is exact, and since D_ε(s) = Σ Λ(n)n^{-s-ε} is "analytic" (a positive-frequency symbol), T_{D̄}T_D = T_{|D|²}. Hence V*V = T_{|D_ε(½+iτ)|²} exactly (no Hankel defect), and T_Λ = T_{2Re D_ε}.
- **W-TK(a) does not apply.** Truncation and the 2×2 matrix symbol [[Θ̄,0],[σ,Θ]] arise only after compression to PW_T ≅ K_Θ (R166_301 §2.1). P7 has no Θ. R166_301 §2.2(b) is the one-sided statement, and it is about *kernels* (ker T_σ = 0 for real nonconstant σ).
- **W-TK 4.1 does not apply.** Sign-blindness ker A_σ = ker A_{−σ} is a statement about kernels. A factorization X = Y*Y is a sign-carrying statement. Replacing A − T_Λ by its negative destroys it.
- **What decides P7 instead.** The symbol map φ ↦ T_φ is injective, so A − T_Λ = (I−V)*(I−V) holds iff the symbols agree pointwise: m_A(τ) = 1 + |D_ε(½+iτ)|². This is false. |D_ε|² has Fourier support on the ratio set log ℚ₊ (the comb), while m_A is archimedean. Also |D_ε|² blows up near ordinates as ε→0.
- So P7 is killed by its own **symbol identity** (= F2). W-TK is not needed and not applicable.
- One more point. On the full one-sided H², T_σ ⪰ 0 ⟺ σ ≥ 0 a.e., which is a symbol-sign question. For finite truncations it is false (R161_002 §2: the sharp semilocal bottom is negative). The row-D content needs window compression, and there W-TK *does* apply, but only to kernel formulations.

## 4. Q25 exactly

R157_002 #30 and §4 (amended by R157_004): "The identity-level use of Λ = μ*log (#30) … [is a] region not excluded by any proved statement, but [has] no object and no statement." Specifically, #30 is "the exact Vaughan/Heath-Brown identity for Λ = μ*log at a load-bearing step", which "is what P47 T2 already demands (invoke A7/A8) and has no formulation".
- Per window: EXCL by F1 (estimates fall under cor:void).
- Globally: EQUIV (P47 Thm 27.10).
- The positivity variant **#55 (Selberg Λ₂ = μ*log² ≥ 0, Möbius as positive adjoint) is EXCL [F3]** (Paper 37).
- Grid neighbours: Q11 (Gamma–Selberg tail, *identifies*), Q14 (cross channel Λ(a)Λ(b), *class*), Q30 (W₂ with Λ*Λ block, formal only).

**Open statement, exactly:** there is no open statement. Q25 is an un-instantiated region. For P7 it **was** instantiated in E70_11/12 (§5.1), and the instance reduces to E1.

## 5. The join analysed

### 5.1 It already exists (E70_11–12, PROVED there)

In the semigroup algebra e_n = n^{-1/2}S_{log n}, with Z_ε = Σ n^{-ε}e_n, M_ε = Σ μ(n)n^{-ε}e_n, M_εZ_ε = e₁ and δe_n = (log n)e_n, Λ = μ*log gives

  V_ε = M_ε δ(Z_ε) = Z_ε⁻¹ δZ_ε  (E70_11).

The Riccati identity δ(V) + V² = Z⁻¹δ²Z, in coefficients, is

  **Λ·log + Λ*Λ = μ*log²**  (Selberg; E70_12).

E70_12 diagnosis: "every term is an Euler convolution term … no Gamma/polar positivity enters". The residue, the Gamma–Euler connection bound 2Re⟨Z⁻¹δZ f,f⟩ ≤ ⟨G_Γ f,f⟩, is AHM = Ω₇, i.e. **E1**. The task's proposed computation is this one.

### 5.2 Why Selberg cannot touch the ratio comb (new, PROVED)

Write V = Σ_p V_p with V_p = Σ_{k≥1} log p · p^{-k(1/2+ε)} S_{k log p}.

**Lemma (support of V*V).** Let r = a/b in lowest terms, r ≠ 1.

- (i) If a, b ≥ 2: Λ(aj)Λ(bj) ≠ 0 forces j = 1, a = p^k, b = q^l, p ≠ q.
  *Proof.* If a prime ℓ divides j, then aj and bj are both powers of ℓ. Then a and b are powers of ℓ, which contradicts coprimality. Hence c_{p^k/q^l} = Λ(p^k)Λ(q^l)(p^kq^l)^{-1/2-ε}.
- (ii) If b = 1: j = p^γ (γ ≥ 1) and a = p^k, so c_{p^k} = log²p · p^{-k(1/2+ε)}/(p^{1+2ε} − 1). These are atoms on log ℕ (prime powers only).

Therefore

  V*V = Σ_p V_p*V_p  [diagonal + atoms on log p^k]  +  Σ_{p≠q} V_p*V_q  [the whole non-integer ratio comb],

while the Selberg-side object is

  V² = Σ_p V_p² + Σ_{p≠q} V_pV_q = Σ_n (Λ*Λ)(n) n^{-1/2-ε} S_{log n}  [atoms on log ℕ].

The two squares differ, prime pair by prime pair, by S_{log q^l} ↦ S_{log q^l}*, i.e. products p^kq^l ↦ ratios p^k/q^l. On the line this is D(s)² vs D(s)D(s̄) = |D|². Selberg's identity is a statement in the Dirichlet (convolution) algebra of ℕ. The Hermitian square lives in the group algebra of ℚ₊^×. Möbius inversion is an identity of the first algebra and has no action on the cross-prime ratio part. Hence:

- **Selberg rewrite.** Σ_{p≠q}V_p*V_q is not expressible through μ*log² − Λlog. That expression rewrites V², not V*V. No ratio cancels, and the comb stays.
- **Square of log ζ instead** (W = Σ Λ(n)/log n · n^{-1/2}S). Same lemma with weights Λ/log, so the same cross-prime ratio comb (all coefficients ≥ 0).
- **Full semigroup Z** (all n). Z*Z has c_r = (ab)^{-1/2-ε}ζ(1+2ε) at every r ∈ ℚ₊, which is worse (dense, divergent).
- **Möbius-signed factor** (M*M, coefficients Σ_j μ(aj)μ(bj), signed, so cancellation is possible). Its cross term is M + M*, not T_Λ. Getting T_Λ needs V = M δZ, and on the commutative group algebra V*V = |M|²|δZ|² = |ζ′/ζ|² as a symbol. No cancellation.
- **Connection square ∇ = δ + V (E70_11).** ∇*∇ = δ*δ + δ*V + V*δ + V*V. It still contains V*V. Gauge-removing V needs the Gamma–Euler bound (E1). The P121 CMO no-go shows the unitriangular Möbius gauge kills the identity diagonal (R161_004 §3).
- **Every positive-coefficient** current on log ℕ has a nonnegative cross-prime comb (Lemma (i)). So cancellation must come from a *signed second sector*. That is E70_10 option 1 (graded cancellation), and Q25 does not supply it.

### 5.3 Structural reading

The ratio comb is exactly the **cross-prime impurity** Σ_{p≠q}V_p*V_q. The per-prime squares V_p*V_p are the "semi-globally pure" local squares of grid F36 (E70_7, DEAD "impurity collective"). So P7's F2 death and F36's death are the same term. Q25's Möbius structure is multiplicative inside ℕ and cannot reach it.

## 6. Verdict

**P7+Q25 is a REPEAT; not admissible.**
- The join was built in E70_11 (Möbius connection) and E70_12 (Riccati = Selberg), and lands on **E1** (Gamma–Euler connection bound = AHM = Ω₇).
- The ratio comb it was meant to treat is untouched: by §5.2 it is the cross-prime Hermitian part, which Selberg/Möbius (convolution algebra) cannot address. That is **F2/W4** (E70_10).
- Möbius-history repairs are separately closed by P121 CMO / R161_004 Cor 3.1.
- Selberg positivity μ*log² ≥ 0 is EXCL [F3] (R157_002 #55).
- W-TK is **not** the killer: P7 is one-sided, and a factorization is not sign-blind. Its own symbol identity m = 1 + |D|² kills it.
- Phase 161's square is a different square (of A_M; sign-blind by Thm 1.1). It is relevant only through R161_004's Möbius stop-gate.

Wall evaded: **none**. The only surviving shape is E70_10 option 1, a signed second sector that cancels Σ_{p≠q}V_p*V_q exactly. It would have to be built **before** any join, and it must name which of E1/F2 it evades. Q25 does not provide it.

## Grid cells (for the editor)

- 4C / 4E: add "P7+Q25 join (R166_502) = E70_11/12, REPEAT [E1; F2]". No symbol change.
- 2A (tool, PROVED): Lemma §5.2 (V*V = Σ_p V_p*V_p + Σ_{p≠q}V_p*V_q; the non-integer ratio comb is j = 1, cross-prime only).
- R166_405: update the Q25 row from "OPEN" to "instantiated for P7 in E70_11/12 → E1"; next join in order is P1/P5+Q1.
