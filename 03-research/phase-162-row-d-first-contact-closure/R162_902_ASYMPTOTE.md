# R162_902 — The terminal value of the resolvent flow (Conjecture 6.1 of R162_802)

Pure mathematics, no numerics. Notation: Paper 47 (eq:form, eq:W, thm:parityschur,
prop:polarcap, thm:KEP3), R162_504 (f_par, μ_k, ψ_T), R162_703 (g_par, h_par), R162_802 (the flow).

**Status.**
- Conjecture 6.1 cannot be proved unconditionally, because it is equivalent to RH (§4). **NO-GO**
  as an unconditional target.
- The terminal value is pinned from one side unconditionally: lim_T g̃_par(T) ≤ 0, equivalently the
  flow never stops short of the asymptote. **PROVED** (§2). This was **already on record**:
  R160_M4_R1 Thm B(i), with a doubly exponential rate, and Thm A(iii) (𝔊_∞ = 0, S^Sch_∞ = −J).
  R162_802 §6 missed it in its corpus check. §2 gives an elementary second proof so that the
  falsifier lines can be read off.
- The exact expansion of f_par(∞) − f_par(T) (Sherman–Morrison) is **PROVED** (§3). Its leading
  term is g_par(T)/4. The sign of that term is the sign of the complete Weil form on the Tate slice,
  so it is RH at the window T (E1).
- "No overshoot" is automatic once the limit equals the threshold and there are no extra poles.
  So overshoot ⟺ limit ≠ threshold, which is **PROVED** and trivial (§4). No mechanism forces the
  sign (§5). **NO-GO**, with falsifiers DH, Λ1_{n≥5} and κ-models.

No sign is claimed. Gate 1 remains OPEN.

## 1. The right monotone object

Per parity, put

  g̃_par(T) := inf{ W_T(F) : F ∈ D_T^par real, ℓ_par(F) = 1 } ∈ [−∞, ∞).

(L1 of R160_M4_R1, restated here.)
- g̃_par is nonincreasing in T. Extension by zero preserves ℓ_par and W_T; this is the argument of
  R162_703 Lemma 2.1, and it needs no hypothesis on λ_par.
- g̃_par(T) ≥ 0 ⟺ W_T ≥ 0 on D_T^par. For ⇒: scaling handles ℓ ≠ 0, and for G ∈ ker ℓ we use
  W(G) = lim_{δ→0} W(G + δH₀) with ℓ(H₀) = 1.
- Hence **RH ⟺ g̃_ev(T), g̃_odd(T) ≥ 0 for all T** (Weil's criterion, parity splitting
  thm:parityschur(o)).
- When λ_par(T) > 0 and A_T^par is invertible with f_par(0;T) ≠ 0, thm:parityschur(a3) and
  R162_703 Thm 2.2 give g̃_par = g_par = 1/f_par(0;T) + 2ε_par. If W_T^par is invertible, then also
  g_par = 1/w_par, where w_par(T) := ⟨(W_T^par)⁻¹φ_par, φ_par⟩ (R156_001 §1). Under RH, w_par is the
  pole reproducing kernel of the window space (R160_M4 Cor B1).

So Conjecture 6.1 in its intrinsic form is lim_T g̃_par(T) = 0, for both parities.

## 2. The unconditional half — PROVED (on record: R160_M4_R1 Thm B(i))

**Theorem 2.1.** lim_{T→∞} g̃_par(T) ≤ 0 for both parities, unconditionally.

R160_M4_R1 Thm B(i) is sharper: g̃_par(T) ≤ C e^{cT} e^{−2π e^{2T}}. That proof uses the Riemann
kernel K_Pó (Φ = ξ), which lies in the radical of the extended form. Here is an elementary proof that
exposes which property of ζ is used.

*Proof (elementary).*
- Write Φ_F(½ + iz) = F̂(z). Then ℓ_par(F) = Φ_F(1) = F̂(−i/2) for F of parity par. This holds
  because A = B for even F and A = −B for odd F.
- Even sector. Take ε < T/2 and F_ε = 1_{[−ε,ε]} ∗ 1_{[−ε,ε]}, normalised by its value at the pole.
  Then F̂_ε(z) = (2 sin εz / z)², supp F_ε ⊂ I_T, F_ε is Lipschitz and F̂_ε = O(|z|⁻²). So the
  explicit formula applies (lem:roughEF). Put F := F_ε / F̂_ε(−i/2), where F̂_ε(−i/2) = (4 sinh(ε/2))².
- For a zero ρ = β + iγ, write y = β − ½. Using |sin εz| ≤ e^{ε|Im z|}:

  |Φ_F(ρ) Φ_F(1−ρ)| ≤ e^{4ε|y|} / (γ⁴ · 16² sinh⁴(ε/2)) ≲ e^{−2ε(1 − 2|y|)} / γ⁴.

- Every nontrivial zero has |y| < ½. This uses ζ(s) ≠ 0 for Re s ≥ 1, i.e. Euler product plus
  Hadamard–de la Vallée Poussin.
- So each term tends to 0 as ε → ∞. The terms are dominated by C/γ⁴, and Σ_ρ γ⁻⁴ < ∞. Dominated
  convergence gives W(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) → 0.
- Therefore g̃_ev(T) ≤ W_T(F_{T/2−}) → 0.
- Odd sector. Take F̂(z) = z (sin εz / εz)³, which is odd, with support 3ε < T. Normalise by
  F̂(−i/2). The same estimate gives |Φ(ρ)Φ(1−ρ)| ≲ e^{−3ε(1−2|y|)} / γ⁴ → 0.
- Monotonicity turns lim sup into lim. ∎

In the resolvent language (§1), wherever WP holds at large T:
- lim f_ev(0;T) ≥ −½, and lim f_odd(0;T) ≥ ½, or f_odd hits a pole.
- So the flow never stops short of the asymptote. The asymptote is set by the polar term 2ε_par,
  since a_T(h_par) → −2ε_par, which is S^Sch_T → −J (R160_M4 Thm A(iii)).

**How the pole of ζ enters.**
- On the even sector, A^ev = W^ev − 2φ_evφ_ev* exactly (parity splitting). The rank-one term is the
  PNT main term of the comb (R162_504 §5(i)).
- Its size is 2‖φ_ev‖² = 2(sinh T + T) ~ e^T. This is what produces the Perron eigenvalue
  μ₁ ≍ −e^T of R162_504.
- In the flow, the Perron–Tate structure matters only through this rank-one term. Nothing about ψ_T
  beyond Sherman–Morrison (§3) is needed for the limit.

## 3. Exact expansion — PROVED (algebra)

Suppose W_T^par and A_T^par are both invertible.
- Even sector. From A = W − 2φφ*, Sherman–Morrison gives f = w/(1 − 2w). So

  f_ev(∞) − f_ev(T) = −½ − f_ev(T) = g_ev / (2(2 − g_ev)) = g_ev/4 + O(g_ev²).

- Odd sector. From A = W + 2φφ*, we get f = w/(1 + 2w). So

  f_odd(∞) − f_odd(T) = ½ − f_odd(T) = g_odd / (2(2 + g_odd)) = g_odd/4 + O(g_odd²).

What this means:
- The leading term of the gap is g_par(T)/4 = 1/(4 w_par(T)), the inverse pole kernel.
- Its sign is the sign of W_T on the Tate slice. That is RH at the window T (§1), so the statement is
  E1.
- Under RH the gap is ≤ C e^{cT} e^{−2π e^{2T}} (R160_M4 B(i)), so the approach is doubly
  exponential.
- The primes enter g only through W_T = Σ_ρ. So the "PNT error structure" of the leading term is the
  zero sum itself. We could not find an independent sign for it from the Euler product. Every rewriting
  of Σ(Λ(n) − 1)-type errors passes back through the explicit formula to the same quantity (R162_504
  §5(i)).

## 4. Conjecture 6.1 ⟺ RH — PROVED; unconditional proof NO-GO

**Theorem 4.1.**
- (a) In the intrinsic form, lim_T g̃_par(T) = 0 for both parities ⟺ RH.
- (b) In the resolvent form, [f_ev(∞) = −½, f_odd(∞) = ½, and no crossing other than the Perron
  crossing T_P] ⟺ RH.

*Proof of (a).*
- ⇐: RH gives g̃ ≥ 0 (§1). Thm 2.1 gives lim ≤ 0.
- ⇒: if RH fails, W_{T₁}^par has a negative direction for some T₁ and some parity. Then g̃_par(T₁) < 0.
  By monotonicity, lim g̃_par ≤ g̃_par(T₁) < 0 (possibly −∞).

*Proof of (b).*
- ⇐: RH gives WP and g ∈ [0, doubly exponentially small], so f → ∓½ by §1 and §3. There are no
  crossings besides T_P (R162_802 §3.4).
- ⇒: without poles, f is nondecreasing, so f(T) ≤ f(∞) for every T. This gives f_ev ≤ −½ and
  f_odd ≤ ½ for every T. In particular f_ev never reaches 0, so ι ≡ 0 (R162_802 §3.2), and R162_802
  §3.4 (⇐) gives RH. ∎

**Consequences.**
- The only unconditional content of the conjecture is the inequality of §2, which is already on
  record.
- The equality half is RH. An unconditional proof of Conjecture 6.1 would be a proof of RH through
  Thm 4.1. No independent route is available (§5).

**The overshoot question.** A first overshoot does contradict monotonicity plus the limit, but
trivially:
- If f_ev(T₁) > −½ and there is no later pole, then lim f_ev ≥ f_ev(T₁) > −½.
- So "no overshoot" is the equality half of the conjecture, not a separate step.
- Overshoot is permanent in g̃ (monotone). It is fully consistent with the unconditional
  lim g̃ ≤ 0, which only says the limit is at or below 0.
- So monotonicity plus the unconditional half cannot exclude overshoot. Both sides of the dichotomy
  are compatible with every unconditional law of the flow.

Residual (O902.1). Without the no-crossing clause, (b) ⇒ needs a further step. Suppose there is a
crossing after T_P, followed by convergence of f to ∓½ with λ_par < 0. Then W_T(h_T), the critical
(non-minimal) value on an indefinite slice, would tend to 0. This is not excluded here. It does not
affect (a).

## 5. Search for a one-sided mechanism — NO-GO

Each candidate is listed with the line where it fails.

1. **Leading term of §3.**
   - g/4 is the inverse pole kernel, and its sign is RH at T (E1).
   - The Euler product enters the unconditional half only through |β − ½| < ½ (the line in §2). That
     is a location statement for zeros, which gives an upper bound on g̃ and never a lower bound.
2. **Pole matching / Perron.**
   - The asymptote −2ε_par comes from the rank-one term 2φφ* = the PNT main term.
   - Every a ≥ 0 comb with the same residue has the same asymptote (M, F3). See the falsifiers below.
3. **Exterior-capacity comparison.**
   - R160_M4 Thm A(ii) writes g̃ = inf{a_*(G) : G primitive, G = −N_par off I_T}.
   - A lower bound needs a comparison principle for (a_T|P_T)⁻¹ on positive sources, and that
     principle does not exist (R160_M4 §8.2(b); phase 106 wall). EQUIV per window.
4. **Two-sided pinning under RD_T.**
   - R160_M4 B2(2) gives g ≥ −C e^{cT} e^{−π e^{2T}} ‖h_par‖² when λ_par > 0.
   - So f → ∓½ follows from [RD_T for all large T and ‖h_T‖² = o(e^{π e^{2T}})]. But "RD_T for all T"
     is already RH (Paper 47, primitive Weil criterion). E1.

**Falsifier lines.**
- **Deletion a = Λ1_{n≥5}.**
  - Thm 2.1 holds verbatim. The finite comb change adds Σ_{n=2,3,4} v_n c_F(log n), which is at most
    ‖F‖² in absolute value. That is → 0, because F̂ is O(e^{−ε}) on ℝ after normalisation.
  - So lim g̃(a) ≤ 0. But λ_W(a) < 0 on [0.4608, 0.58] (cor:convfail), so lim g̃_odd(a) < 0.
  - This is the overshoot: f_odd(a) crosses ½ at 0.4608.
  - Hence every law used in §§2–3 (monotonicity, the rank-one polar term, the Sherman–Morrison
    expansion, the upper half) holds for a model where the conjecture fails. **F3.**
- **κ-models (R162_702).** These are finite comb changes too, so the same line applies. **F3.**
- **DH.**
  - The elementary proof of §2 breaks at |y| < ½, because DH has zeros with β > 1, where
    e^{2ε(2|y|−1)} blows up.
  - The radical proof (R160_M4 E(ii), HEURISTIC) would still give the upper half through DH's own
    functional equation.
  - DH has off-line zeros, so g̃_DH → −∞ eventually and the conjecture fails.
  - So a proof of the equality half must use the Euler product beyond zero-free-on-Re s = 1. That is a
    positivity input, and no such input is known. **DH line.**

## 6. Verdict for R162_590 §1c

- Terminal value of the resolvent flow (Conj 6.1): equivalent to RH (Thm 4.1). The unconditional
  half, lim g̃ ≤ 0, is R160_M4_R1 B(i) (doubly exponential), with an elementary proof in §2.
- The expansion gap = g/4 + O(g²) is E1.
- "No overshoot" = the equality half itself.
- Killed by F3 (Λ1_{n≥5}, κ-models) and DH. **E1.**
- Record note: R162_802 §6 did not cite R160_M4_R1 Thms A(iii), B(i) and B2. Its "heuristic" is a
  theorem on record.
