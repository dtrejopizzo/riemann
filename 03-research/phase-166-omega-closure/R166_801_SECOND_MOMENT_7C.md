# R166_801 — Cell 7C: second moment of the explicit formula over the translates of the witness

* No numerics. No other file edited. No label of record moves.*
*Inputs: R166_190 (rounds 9–11, requirements (G),(N)), R166_501 Thm A, R163_401 (1.1), Lemma 3.1, R162_2300 §6 item 46 (7C "correlación exacta de pares", never formulated as a route).
Corpus check (grep "pair correlation|correlación de pares|Montgomery"): phase-7-weil-carleson-sine-kernel P7b (sine-kernel Gram = pair correlation at second order; "pair correlation describes, does not force", RH-conditional); R163_602 §4.3 (Montgomery–Vaughan mean-value/Landau duality, used for mollifiers, NO-GO); phase 161 (squares of the Weil operator, sign-blind); phases 8/21/45/137/138/58 mention Montgomery only as context. **No memo writes the second moment of (1.1) over the translation family of the witness.** This memo does, and closes it.*

## Outcome

| # | statement | label |
|---|---|---|
| 1.1 | translate identity Z(a) = Arch(a) + Pol(a) − S(a), S(a) = 2Σ_{n<X}Λ(n)n^{-1/2}h(log n)cos(a log n) | PROVED (from (1.1), Lemma 3.1(b)) |
| 1.2 | exact second-moment identity (2.3); for A ≥ A₀(X) only the integer diagonal survives, weight Λ(n)² = Λ(n)log p | PROVED |
| 1.3 | the zero-side pair kernel is B(t,t') = ∫w(a)G²(t−a)G²(t'−a)da; pairs are NOT restricted to \|γ−γ'\| ≲ 1/A (brief's claim FALSE): w fixes the height window, the pair scale is that of K = G²*G² (O(1), Fourier support [−4T,4T]) | PROVED |
| 2.1 | quartet self-block = 2Re∫w(t_q−y)G(y)⁴dy + 2∫w(a)\|G(t_q−a)\|⁴da: **phase-blind**; the e^{4iφ} term of the brief integrates out (Cauchy shift); dependence on δ only through w at complex argument, O(δ²/A²) | PROVED |
| 2.2 | pointwise Z(a)² carries cos²2φ = ½(1+cos4φ): the square of the first moment, no independent equation | PROVED (trivial) |
| 3 | **Theorem 7C (E1/f_t).** Every w-moment of the translate family is a functional of window data; holds verbatim for M_m (its own witness) and f_t; no contradiction possible | PROVED |
| 3a | Λ² = Λ log p enters only as a rewriting of a fixed finite number; no inequality violated by β_m (β_m's contribution to the mean square per unit length → 0, Wiener/Bohr) | PROVED |
| 3b | A > X adds nothing beyond the window: S(a) has only n < X for every A | PROVED |
| 4 | "fourth-moment node identity" (4.1): new as a written identity, gives a positive (not sign-defective) quartet contribution; constrains neither ω(E) nor φ beyond Rem 4.8a | PROVED (identity) / NO-GO (as route) |
| small gaps | Σ over pairs with \|γ−γ'\| ≤ 1 in height window [H,H+A]: ≪ ‖K‖_∞ A log²H unconditionally (N(t+1)−N(t) ≪ log t); nothing better for gaps < e^{−2T} is known | PROVED-CITED (Titchmarsh 9.2) |
| cell 7C | **CLOSED negative**, wall E1/f_t (fails (N)) and (G) (phase-blind) | — |
| row D, (★_cell) | | OPEN |

## §1 The translate family

F real, supp F ⊂ [−T,T], T = T_c, G real-rooted, (F̂F̂^#)(z) = G(z)² (Lemma 3.1(b)). For a ∈ ℝ put F_a(u) = F(u)e^{iau}. Then F̂_a(z) = F̂(z−a) and, a being real, F̂_a^#(z) = F̂^#(z−a). Hence (1.1) for the complex test F_a reads

  W_T(F_a) = Σ_ρ F̂_a(t_ρ)·conj F̂_a(conj t_ρ) = Σ_ρ G²(t_ρ − a) =: Z(a).          (1.1a)

Z(a) is real: the multiset {t_ρ} is closed under t ↦ conj t (ρ ↦ 1−ρ̄) and G² is real on ℝ. Prime side: the autocorrelation of F_a is h_a(u) = e^{iau}h(u), h = F*F̃ (real, even, supp [−2T,2T], ĥ = G²). So

  Z(a) = Arch(a) + Pol(a) − S(a),  S(a) := 2Σ_{n<X} Λ(n)n^{−1/2} h(log n) cos(a log n),  X = e^{2T},       (1.2)

Arch(a) = ∫G²(τ−a)Ω(τ)dτ (Ω the Γ-density, ~ (2π)^{-1}log(|τ|/2π)), Pol(a) = G²(a−i/2)+G²(a+i/2)-type (entire, bounded). At a = 0, Z(0) = 0 is the witness equation (3.1).

## §2 The second moment

Weight: w(a) = w₀((a−H)/A) real, ŵ₀ ≥ 0 supported in [−1,1] (so ŵ is supported in [−1/A,1/A], w entire of type 1/A).

**(2.1) Prime side.** ∫w S² da = Σ_{n,m<X} (Λ(n)Λ(m)/√(nm)) h(log n)h(log m) · [Re e^{iH(log n−log m)}ŵ(log n−log m) + Re e^{iH log nm}ŵ(log nm)] (up to the normalisation of ŵ). For distinct n,m < X, |log n − log m| ≥ log(1+1/X) > 1/(2X); log nm ≥ log 2. Hence for A ≥ A₀ := max(2X, 1/log 2) **only n = m survives**:

  ∫w S² = ŵ(0)·Σ_{n<X} Λ(n)² n^{−1} h(log n)² = ŵ(0)·Σ_{n<X} Λ(n)·log p_n · n^{−1} h(log n)²,       (2.2)

with ŵ(0) = A·ŵ₀(0) (same constant in all lines below).

**(2.2) Zero side.** By (1.2), ∫w(Z − Arch − Pol)² = ∫w S². Expanding,

  Σ_{ρ,ρ'} B(t_ρ,t_ρ') − 2∫w Z(Arch+Pol) + ∫w(Arch+Pol)² = ŵ(0)·Σ_{n<X} Λ(n)log p_n n^{−1}h(log n)²,   (2.3)

  B(t,t') := ∫w(a)G²(t−a)G²(t'−a)da.

This is the exact "second moment at the witness" (Montgomery's F(α) in the band-limited, unconditional range |α| < 1, written at T_c without RH). Absolute convergence: Lemma 3.0 of R163_401 per factor.

**(2.3) The pair kernel (correction to the brief).** By Fourier in a, B(t,t') = ∫∫h(u)h(u')ŵ(u+u')e^{−iut−iu't'}du du'. For A large, w varies slowly and B(t,t') ≈ w(γ)·K(t−t'), K = G²*G² (entire; K̂ = h² supported in [−2T,2T]·2). So pairs are weighted by K at gap scale O(1), restricted in **height** to |γ−H| ≲ A; they are not restricted to |γ−γ'| ≲ 1/A. The brief's "only pairs with gap ≲ e^{−2T_c}" is FALSE: the 1/A-localisation acts on log n − log m, whose dual on the zero side is the height, not the gap.

**Small gaps.** With K ≪ (1+s²)^{−1} (true when h ∈ C², e.g. F ∈ H¹; ARGUED for the general witness in 𝒟_T), Σ_{|γ−H|≤A}Σ_{ρ'}|B| ≪ ‖w‖_∞ A log²H via N(t+1)−N(t) ≪ log t (Titchmarsh 9.2, CITED). Unconditionally nothing better is known for gaps < e^{−2T}; pairs at gap ≤ η contribute at most K(0)·#{pairs} ≤ K(0)·A log²H, and these enter (2.3) with the positive weight K(0) = ∫G⁴ > 0 at the limit — they are invisible as signs.

## §3 The quartet in the second moment (question (2))

Let q have t_q = γ_q − iδ, c = conj t_q (and the mirror pair at −γ_q, outside the window when H > 0, A < H). The quartet's self-block in Σ B is B(t_q,t_q)+B(c,c)+2B(t_q,c).

- B(t_q,c) = ∫w(a)|G²(t_q−a)|²da ≥ 0, since G²(c−a) = conj G²(t_q−a) (G real on ℝ).
- B(t_q,t_q) = ∫w(a)G(t_q−a)⁴da = ∫w(t_q−y)G(y)⁴dy (shift y = t_q − a to ℝ: w(t_q−·)G⁴ is entire and integrable on the strip |Im| ≤ δ < ½, Phragmén–Lindelöf). So 2Re B(t_q,t_q) = 2∫Re w(γ_q−y−iδ)G(y)⁴dy = 2∫w(γ_q−y)G⁴dy + O(δ²A^{−2}‖w₀″‖∫G⁴).

**Proposition 3.1 (PROVED).** The quartet's contribution to (2.3) is positive up to O(δ²/A²) and contains no phase of G(t_q): the e^{±4iφ} term of the brief (pointwise G(t_q)⁴) is averaged over a and becomes ∫G⁴ by Cauchy. The a-average that produces the integer diagonal is the same average that erases the phase.

**Pointwise (a fixed).** Z(a)² contains (2Re G²(t_q−a))² = 4|G|⁴cos²2φ = 2|G|⁴(1+cos4φ): the square of the first-moment term, no independent equation (2.2). The only genuinely new equations are Z(a) = Arch+Pol−S for each a, i.e. the first-moment family itself; any second moment is a quadratic functional of that family.

So the answer to (2) is: no independent cos4φ equation; the pair (cos2φ, cos4φ) is never constrained jointly.

## §4 Theorem 7C (question (3)) — predicted failure CONFIRMED

**Theorem 7C. PROVED.** Let Σ be any configuration (ζ, M_m, f_t, f_χ, P_{a,c}) whose explicit formula (1.1) holds on 𝒟_{T} for its own prime side, and let F be its witness at T_c. Then for every weight w and every A, (2.3) holds for Σ with its own prime side, and its right side depends only on Σ's prime side restricted to (−2T_c, 2T_c).

*Proof.* 𝒟_T is closed under u ↦ e^{iau}F(u) (support unchanged). (1.1) for F_a gives (1.2) pointwise in a for Σ; (2.3) is ∫w(·)² of (1.2). The prime side of F_a is the measure P_Σ paired with e^{iau}h(u), h supported in [−2T_c,2T_c]. ∎

(a) **Integrality.** For M_m, P = P_ζ|_{atomic} + β_m(u)du on the window. Then S_m(a) = S(a) + ∫β_m(u)h(u)cos(au)du, and the β-part is the Fourier transform of an L¹ function: its w-mean square is ≤ ‖w‖_∞‖β_m h‖²_{L²} = O(1), while the atomic diagonal is ≍ A. So per unit length the continuous density contributes **0** (Wiener: the Bohr mean square sees only atoms). This is a structural difference (atomic vs continuous), but both sides of (2.3) for M_m are computed with M_m's own data and agree identically; there is nothing to violate. Λ(n)² = Λ(n)log p rewrites one fixed finite sum. Any inequality built on it (Λ² ≤ Λ log X, Cauchy–Schwarz (ΣΛn^{−1/2}|h|)² ≤ (ΣΛ/n·…)(Σ…)) bounds window numbers that are the same for ζ and for M_m's atomic part: E1. Upper bounds are sieves (drop-term principle, R163_602 (b)).
(b) **A > X.** S(a) involves n < X for every A, since h_a is supported in [−2T_c,2T_c]. Larger A only deletes off-diagonal pairs. (N) fails.
(c) **(G).** By Prop 3.1, the second moment is phase-blind (and the first-moment phase is already E1 by R166_201 Thm 1.3).

Hence cell 7C is the Parseval transform of the first-moment family: wall **E1/f_t**, with M_m passing (it has its witness and satisfies (2.3)). Montgomery's pair-correlation range |α| ≥ 1 (pairs n ≠ m beyond the window) would need tests of type > 2T_c, where F_a is no longer the witness: that is a different T, i.e. the λ_T flow, already E1 (R165_202).

## §5 What is new (question (4))

**(4.1) Fourth-moment node identity (PROVED).** For A ≥ A₀(X), with H inside the height range:

  Σ_{ρ on-line}Σ_{ρ'} B + Σ_q [2∫w(γ_q−y)G⁴(y)dy + 2∫w(a)|G(t_q−a)|⁴da + cross terms] + O(Σ_q δ_q²/A²)
   − 2∫w Z(Arch+Pol) + ∫w(Arch+Pol)² = A ŵ₀(0) Σ_{n<X} Λ(n) log p_n n^{−1} h(log n)².

On-line diagonal: Σ_ρ B(γ,γ) = Σ ∫w G(γ−a)⁴ ≥ 0. Every term attached to a single quartet is ≥ 0 at leading order; off-line zeros raise, not lower, the zero-side second moment. So (4.1) carries no sign defect, does not see ω(E) (it is a height average, not a statement at the node set X), and adds nothing to Rem 4.8a. It is recorded as a tool: the unconditional band-limited Montgomery identity at the witness.

## §6 Falsifiers

| model | (1.2) | (2.3) | quartet phase visible | first failing requirement |
|---|---|---|---|---|
| ζ | yes | yes | no | — |
| M_m | yes (own P, β_m) | yes; β_m invisible per unit length, identity exact | no | (N): window only |
| f_t | yes (same window) | identical to ζ's right side | no | (N) |

## §7 Grid entry (R162_2300, cell 7C, item 46)

7C "correlación exacta de pares": **formulated and CLOSED negative (R166_801).** Second moment of (1.1) over translates F_a = Parseval of the first-moment family; diagonal Λ² = Λ log p is a rewriting (E1); A > X adds nothing (prime side only n < X); the a-average erases the quartet phase (Prop 3.1). Tool: identity (4.1). Corrected brief errors: (i) pairs localised in height, not in gap; (ii) no e^{4iφ} term survives the average.
