# R162_1502 — The comb spill through the torsion cocycle; ratio law for ΔQ_m against Δ(1/λ) — **PARTIAL (identities PROVED) + NO-GO (PROVED)**

Note. No new numerics; §6 quotes the uncertified float table of R162_1402 §7
as guidance only.
Inputs: README (F1–F4), R162_590, R162_1402 (Thms 1–3, residual §8), R162_1001 Thm 3.1 + Prop 3.2 with the R162_1190
fixes (failure at every p | n₀; Λχ₂ fails at every p with χ(p) ≠ 1; Beurling statement definitional on ℝ/ℤ only;
factor 2 in Prop 3.2), R162_802 Thm 2.1, R162_1401 (Thms 3, 4, 6), R162_903 Thm 3.2 (with the R162_1190 fix: operator
identities hold modulo ker M_T).

**Labels.**
- Lemma 1 (collar spill = conjugated position operator: C_N u = −Z X Z⁻¹u on the collar, Z = M(1)) PROVED. **New form.**
- Prop 2 (this identity, for all u and all collars, characterises a = Λ; it is the torsion cocycle (3.1) for all p
  read on the collar) PROVED.
- Prop 3 (general weights: C_a u = −Z_{a′}XZ_{a′}⁻¹u on the collar with a′ = exp_*(a/log), for every a, including
  Beurling) PROVED.
- Thm 4 (ground-state ledger: the pairing of the spill with the bottom vector ψ_{T′} is fixed by bottom data alone,
  independently of a) PROVED. **New.**
- Thm 5 (ratio law: ΔQ_m/Δ(1/λ) → |x_m(F)|² at a gapped simple first contact; the target inequality integrates to
  the trivial bound Q_m ≤ ‖e_m‖²/λ unless its constant tends to 0, and "constant → 0" ⟺ Gate 1) PROVED
  (gap hypothesis as in R162_1402 Thm 3(b)).
- Thm 6 (NO-GO: every use of Lemma 1 in the collar law is inert; the only inequality it supplies (Z_{a′} ≥ 0) holds
  for deletion and Beurling) PROVED.
- §6 square-root caveat: the rate target is FALSE with a T-uniform constant for ζ (guidance from the float data plus
  monotonicity), and consistent only in the local, counterfactual form, where it is Gate 1.
Gate 1 OPEN. No label moves.

## 0. Corpus check

I grepped "spill", "comb spill", "Z X Z", "ZXZ", "conjugat", "torsion", "cocycle", "1/λ", "ratio" in phase 162 and
R160_D4.
- The comb spill C_N u is defined only in R162_1402 Thm 2(iii).
- ZXZ⁻¹ = X + M_T(Λ) is R162_502 B2.1 / R162_903 Thm 3.2. On the Gamma rays it is R162_1401 Thm 4.
- The torsion cocycle is R162_1001 Thm 3.1.
- Not found: the pointwise collar form of the conjugation (Lemma 1), the ground-state ledger (Thm 4), or the ratio law
  (Thm 5).

## 1. Failing lines, stated first

The step that uses Λ is Lemma 1 / Prop 2. It needs a′ := exp_*(a/log) ≡ 1, that is, the collar spill is the Möbius
conjugate of the position operator with **unit** coefficients. This is (3.1) for every p.

| model | the step "a′ ≡ 1" fails at | what survives (Prop 3) | downstream |
|---|---|---|---|
| deletion Λ1_{n≥5} | a′(2) = a′(3) = 0 and a′(4) = 0 ≠ 1; (3.1) fails at p = 2, 3 | C_a u = −Z_{a′}XZ_{a′}⁻¹u with a′ ≥ 0 | Thm 4 and Thm 5 verbatim; first contacts with x_m ≠ 0 exist |
| Λχ₂ (any nontrivial χ) | a′ = χ, so a′(p) = χ(p) ≠ 1; (3.1) fails at every p with χ(p) ≠ 1 | same, with Z_χ (signed) | verbatim |
| DH | a′ = DH Dirichlet coefficients ≠ 1 (and signed); (3.1) fails at some p | same | verbatim; first contacts with x_m ≠ 0 exist |
| Beurling | torsion form undefined on ℝ/ℤ (R162_1001 Thm 3.1(c)). The **operator** form holds: a′ = 1 on 𝒩_B | Lemma 1 verbatim with M_B(1) | verbatim |

So the step fails, in the torsion/cocycle form, for all four falsifiers. It fails in the operator form for three of them;
Beurling passes the operator form. In every case the step is **inert**: nothing downstream reads a′ (Thm 6).

## 2. The spill as a conjugated position operator

Notation, from R162_1402 §§1, 3:
- T < T′ < T_*, and C = I_{T′} ∖ I_T = C₊ ∪ C₋, with C₊ = [T,T′) and C₋ = (−T′,−T].
- u = H_T⁻¹e_m^T ∈ P_T is supported in I_T.
- w_n = Λ(n)n^{−½}, and C_N u = C⁺u + C⁻u, where C^±u(t) = Σ_n w_n u(t ∓ log n).
- Untruncated Dirichlet multipliers on functions on ℝ: (M(α)g)(t) = Σ_n α(n)n^{−½}g(t − log n). Z := M(1),
  Z⁻¹ = M(μ), and (Xg)(t) = t g(t).

On C₊ only C⁺ survives, since t + log n > T. On C₋ only C⁻ survives. By parity it suffices to treat C₊.

**Lemma 1.** For t ∈ C₊, put v := Z⁻¹u, i.e. v(s) = Σ_j μ(j)j^{−½}u(s − log j). Then

  (C⁺u)(t) = (M(log)v)(t) = −(Z X Z⁻¹u)(t).                                                    (2.1)

Every sum is finite: only n < e^{t+T} contribute.

*Proof.*
- M(log)v(t) = Σ_N log N·N^{−½}Σ_j μ(j)j^{−½}u(t − log Nj) = Σ_M M^{−½}u(t − log M)·Σ_{Nj=M} μ(j)log N. The inner sum
  is Σ_{Nj=M} μ(j)log N = (μ*log)(M) = Λ(M).
- (ZXv)(t) = Σ_N N^{−½}(t − log N)v(t − log N) = t(Zv)(t) − M(log)v(t) = t·u(t) − M(log)v(t).
- For t ∈ C₊ we have u(t) = 0, because supp u ⊂ I_T. ∎

Reading.
- The spill across the collar edge is the Möbius-conjugated position operator, evaluated where X itself vanishes on u.
- The secular X of R162_1401 does meet the arithmetic on the collar: Z X Z⁻¹ is exactly X + (the comb). But it meets
  it only on the Möbius transform v, which is not window-supported. v lives on (−T,∞).

**Prop 2 (Λ-characterisation = cocycle for all p).** Let a be real with a(1) = 0. Suppose that for every T′ ≤ T₀ and
every u ∈ L²(I_T) the spill Σ_n a(n)n^{−½}u(t − log n) equals M(log)M(1)⁻¹u(t) on C₊. Then a(n) = Λ(n) for all
n < e^{2T₀}. Conversely, (2.1) holds for a = Λ.

This is equivalent to (3.1) of R162_1001 holding for every prime p, restricted to indices k < e^{2T₀}.

*Proof.*
- The identity is linear in u. Let u run through an approximate identity at s₀ ∈ I_T. The coefficient of
  δ(t − s₀ − log n) gives a(n)n^{−½} = (μ*log)(n)n^{−½} for every n with log n ∈ (t − T, t + T), t ∈ C₊, T′ ≤ T₀. That
  covers every n < e^{2T₀}.
- a = μ*log ⟺ a*1 = log ⟺ (3.1) for all p (R162_1001 Thm 3.1(a),(b)). The corrected failing set is every p | n₀. ∎

**Prop 3 (general weights).** For every real a, including a Beurling Λ_B on its own integers, put
a′ := exp_*(a/log), with a′(1) = 1 and inverse a′^{*−1}. Then

  Σ_n a(n)n^{−½}u(t − log n) = −(Z_{a′}XZ_{a′}⁻¹u)(t)  on C₊,  where Z_{a′} = M(a′).

*Proof.*
- The derivation D = ·log satisfies D(exp_* b) = (Db)*exp_* b. With b = a/log this gives a′·log = a*a′.
- The computation of Lemma 1 then yields Z_{a′}XZ_{a′}⁻¹ = X − M((a′log)*a′^{−1}) = X − M(a).
- Evaluate on C₊, where u vanishes. ∎

Values of a′:
- a′ = 1 for Λ.
- a′ = χ for Λχ.
- For deletion, a′ = exp_*(Σ_{n≥5}Λ(n)/log n·n^{−s}), which has **nonnegative** coefficients and a′(2) = a′(3) =
  a′(4) = 0. (Correction to R162_1401 Thm 6(a), which calls these coefficients "signed". The product
  ζ(s)exp(−2^{−s} − 3^{−s} − ½4^{−s}) equals the exponential of a series with nonnegative coefficients.)
- For DH, a′ is the DH Dirichlet coefficient sequence.

## 3. Ground-state ledger (Thm 4)

Let ψ′ = ψ_{T′} be a normalised bottom eigenvector of H_{T′}, with λ′ = λ(T′). Let r be the collar residual of
R162_1402 Thm 2: r(G) = h_{T′}(ũ,G) − x_m(G).

**Thm 4.**
(a) r(ψ′) = λ′⟨ũ,ψ′⟩ − x_m(ψ′), exactly.

(b) Write ψ′ = ψ′1_{I_T} + ψ′1_C. Let τ(G) be the Tate-direction correction of Thm 2(iii), which is linear in the two
Tate moments of G|_C. Put Γ_C(ψ′) = Σ_k x_k(u)∫_C e^{−a_k|t|}ε_k ψ′, and x_m^C(ψ′) = ∫_C e^{a_m t}ψ′. Then

  ⟨C_N u, ψ′⟩_C = x_m(ψ′) − λ′⟨ũ,ψ′⟩ − x_m^C(ψ′) − Γ_C(ψ′) + τ(ψ′).                             (3.1)

(c) By Lemma 1, the left side equals −⟨ZXZ⁻¹u, ψ′1_{C₊}⟩ − (mirror on C₋). In torsion form, with the R162_1190 factor-2
convention, it equals ⟨Φ_Λ, h_{u,ψ′}⟩, where h_{u,ψ′} is the trigonometric polynomial built as in Prop 3.2 from the
cross-correlation n ↦ n^{−½}∫_C u(t − log n)ψ′(t)dt.

(d) The right side of (3.1) contains no w_n and no a′. By Prop 3 the same identity holds for every weight a, with its own
u, ψ′ and λ′.

*Proof.*
- (a): ψ′ lies in the form domain, so h_{T′}(ũ,ψ′) = λ′⟨ũ,ψ′⟩.
- (b): r kills P_T, so r(ψ′1_{I_T}) is the Tate correction. The Tate moments of ψ′1_{I_T} are minus those of ψ′1_C,
  because ψ′ ∈ P_{T′}. On ψ′1_C apply Thm 2(iii) and rearrange.
- (c): Lemma 1, and R162_1001 Prop 3.2 applied to a cross-correlation instead of an autocorrelation. The proof there
  uses only bilinearity.
- (d): read off. ∎

Consequence. The only term of the collar law of Q_m that sees the bottom at order 1/λ′ is the ground part of the
increment:

  ΔQ_m ≥ |r(ψ′)|²/λ′ = |x_m(ψ′) − λ′⟨ũ,ψ′⟩|²/λ′.

This comes from ΔQ_m = ⟨H_{T′}⁻¹r,r⟩ = Σ_j |r(φ_j)|²/λ_j. In this term the spill is **determined** by (3.1): it is
whatever the bottom data leave over. So controlling the spill independently would control r(ψ′). By (a), that is
controlling x_m(ψ′) against λ′⟨ũ,ψ′⟩, which is the square-root law itself.

## 4. Ratio law (Thm 5)

**Thm 5.** Assume N = ker H_{T_*} = ℂF is simple, with a gap λ₂ ≥ γ > 0 on (T_* − η, T_*), as in R162_1402 Thm 3(b).
Let T_* − η < T < T′ < T_*. Then:

(a) ΔQ_m = |x_m(ψ′)|²/λ′ − |x_m(ψ)|²/λ + O(‖e_m^{T_*}‖²/γ).

(b) Since x_m(ψ_T) → x_m(F) (norm convergence of the ground projections) and 1/λ ↑ ∞:
    ΔQ_m = (|x_m(F)|² + o(1))·Δ(1/λ) + O(1). Hence lim ΔQ_m/Δ(1/λ) = |x_m(F)|² along any T < T′ ↑ T_* with
    Δ(1/λ) → ∞.

(c) A collar inequality ΔQ_m ≤ C_m Δ(1/λ) + D_m, with constants valid on (T_* − η, T_*), holds for every C_m > |x_m(F)|².
    Integrated, it gives only Q_m ≤ C_m/λ + O(1). That is the trivial bound Q_m ≤ ‖e_m‖²/λ up to constants.

(d) Gate 1 at m ⟺ (c) holds with C_m = 0 (equivalently, for every C_m > 0) ⟺ x_m(F) = 0.

*Proof.* (a) is R162_1402 Thm 3(a),(b) at T and at T′. (b) is Thm 3(d) together with the gap. (c) and (d) follow
from (b). ∎

So the requested inequality is either trivial (C_m > 0 fixed) or is Gate 1 (C_m → 0). The spill cannot be the term that
decides between these, because it enters the 1/λ-coefficient only through (3.1), whose right side is weight-free.

## 5. NO-GO (Thm 6)

**Thm 6.** Every argument of the following shape is valid verbatim for deletion Λ1_{n≥5}, Λχ₂, DH and Beurling:
- (i) write the collar residual of Thm 2 of R162_1402;
- (ii) express its comb spill by Lemma 1 or Prop 3 (in torsion form (3.1) of R162_1001 for Λ);
- (iii) bound ΔQ_m by any combination of Cauchy–Schwarz in h_{T′}, spectral decomposition, min–max, positivity of
  Z_{a′}, and the Chebyshev/Mertens size of a;
- (iv) sum over collars.

Deletion and DH have gapped first contacts with x_m(F) ≠ 0 (R162_102, R162_702, thm:finmod). So no such argument yields
C_m → 0.

*Proof.*
- (ii) holds for every a with its own a′ (Prop 3).
- (iii): Thm 4(d) shows that the 1/λ-coefficient is weight-free.
- The only a′-dependent inequality available, Z_{a′} ≥ 0 (positivity preserving), holds whenever a ≥ 0: deletion,
  κ-models, Beurling. It fails for Λχ₂ and DH, so it separates in the wrong direction and leaves deletion in.
- Chebyshev/Mertens sizes are shared by deletion (R162_1401 Thm 6).
- The exact value a′ ≡ 1 can enter only through identities. By R162_1001 Thm 5.1, every identity pairing Φ_Λ with the
  window data (u, ψ′ supported in I_{T′}) reads finitely many values log k. It is continuous in them, and linear in the
  cross-correlation.
- R162_1402 Thm 3(d) gives the divergence for deletion and DH. ∎

**Exact obstruction.** Lemma 1 shows that the arithmetic does reach the secular X on the collar, as Z X Z⁻¹. But it
acts on v = Z⁻¹u, which is **not** window-supported. On C it is evaluated where Xu = 0. The resulting pairing with the
bottom vector is pinned by the eigen-identity (3.1), whose right side involves only x_m, x_k(u), λ′ and Tate moments.

So the cocycle for all p relates the spill to itself under a change of Z, and nothing forces the 1/λ-coefficient
|x_m(F)|² to vanish. A closing mechanism would need an identity in which a′ ≡ 1 enters **nonlinearly** in (u, ψ′). An
example would be a test that is not band-limited: v paired against ψ′ outside I_{T′}, i.e. data at T = ∞. That is
subject to Theorem M dilution (R162_801 L5).

Falsifiers:
- F1: Thm 4 uses the eigen-equation but holds for λ′ > 0 as well. Thm 5(d) is bottom-only (a restatement).
- F2: quadratic, with no orientation.
- F3: fails at the use step (Thm 6), although passed at the object step (§1).
- F4: finite T, exact.

## 6. Square-root-law caveat (honest consistency check)

R162_1402 Thm 3(c) gives the target |x_m(ψ_T)|² ≤ C_m λ(T). Facts:

1. For ζ there is no known T_*. λ(T) > 0 on (0,½log5] (certified, R162_303). λ is nonincreasing (min–max), and it
   collapses doubly exponentially (Theorem M; float table λ: 7e−1 → 4.4e−7, certified 2.5e−12 at ½log5).
2. Float guidance (R162_1402 §7):
   - the ground share is gs ≈ 0.99 for T ≥ 0.7;
   - |x_m(ψ_T)|²/‖e_m^T‖² ≈ 0.2–1, and ‖e_m^T‖² grows like e^{2a_mT}.
   So |x_m(ψ_T)|² is bounded **below**, not small.
3. Hence, with a **T-uniform** constant the target is false for ζ in the regime where λ → 0:
   - Any admissible C_m must be at least Q_m(T) − ‖e_m‖²/γ. That is ≳ 5·10⁵ at ½log5 from the float Galerkin lower
     bound, and ≳ 10¹¹ with the certified λ.
   - Along T → ∞, C_m would have to grow like 1/λ(T), unless x_m(ψ_T) decays at the √λ rate. The data show no such
     decay.
   This is guidance only (uncertified float), but the direction is robust: Galerkin Q is a lower bound, and Galerkin λ
   is an upper bound.
4. The **consistent** reading is local and counterfactual. At a hypothetical gapped first contact T_*:
   sup_{T<T_*}|x_m(ψ_T)|²/λ(T) < ∞ ⟺ x_m(F) = 0 (Thm 5(d)).
   - Then x_m(ψ_T) → 0, which is **not** what the ζ data show on (0,½log5]. That is no contradiction, because no
     contact occurs there.
   - Any **effective** C_m (depending only on m and a window bound T₀) would give λ(T) ≥ |x_m(ψ_T)|²/C_m > 0 near T_*,
     whenever the ground state carries Gamma data. So an effective version is at least as strong as "λ ≥ c > 0 near
     T_* on the Gamma-visible branch", i.e. as the absence of such a contact.
   - It is false for DH and deletion, as F3 requires.
5. Conclusion. The rate target is consistent only as the qualitative statement Gate 1. It carries no checkable
   quantitative content on ζ. The phrase "λ → 0 for ζ" must be read as "λ → 0 as T → ∞ (doubly exponentially)", not
   "λ reaches 0". Along that route the uniform-constant target is refuted by the data, not supported.

## 7. Verdict and residual

**PARTIAL + NO-GO (PROVED).**
- Proved:
  - the comb spill across the collar edge is exactly −ZXZ⁻¹u there (Lemma 1);
  - this identity, for all collars, is the torsion cocycle for all p and characterises Λ (Prop 2);
  - it has a weight-general form (Prop 3);
  - its pairing with the bottom is fixed by weight-free data (Thm 4);
  - ΔQ_m/Δ(1/λ) → |x_m(F)|² (Thm 5).
- Fails: every bound built on the spill is inert in a′ (Thm 6). The target inequality is trivial for fixed C_m > 0
  and is Gate 1 for C_m → 0. With T-uniform constants it contradicts the ζ data (§6).

**Residual.** An identity in which a′ ≡ 1 enters nonlinearly in (u, ψ′). By Lemma 1 the natural carrier is the Möbius
transform v = Z⁻¹u outside the window, paired with the bottom vector. Deciding whether ⟨Xv, Z*(ψ′1_C)⟩ admits a
finite-T evaluation that is not band-limited is the concrete form of the R162_1001 §7 residual.

Add to R162_590 §1c: "Comb spill via torsion cocycle; ΔQ vs Δ(1/λ) — R162_1502 — spill = −ZXZ⁻¹u on collar
(Λ-characterising), but its bottom pairing is weight-free (3.1); ratio → |x_m(F)|²; rate target consistent only as
Gate 1 | E1, F3".

Files edited: this file only.
