# Analytic attack on inequality (1): what exactly is δV? Pure mathematics on the last GAP of the cascade. No steps skipped.
**[P]** proved · **[O]** open · **[!]** conclusion that must be stated clearly. --- ## 1. The two definitions of V₀ and their agreement at leading order The cascade defines **V₀ = Kφ₀/φ₀** (ground-state potential, FLS side).
On the other hand, the **PNT average of the prime well** is another object. Let us see that they
agree at leading order. **Average of the well.** The well is V_λ = Σ_{n≤λ²} (Λ(n)/√n) · [mass at u=log n].
For a smooth test function f, by PNT (Σ_{n≤x} Λ(n) ~ x):
``` Σ_n (Λ(n)/√n) f(log n) ≈ ∫ (1/√x) f(log x) dx [x=e^u, dx=e^u du] = ∫ e^{u/2} f(u) du.
```
⟹ **The smooth average of the prime well is the density e^{u/2} du** — which is
exactly the weight of the pole functional ℓ. **[P]** (it is PNT). **Agreement.** At leading order the Weil balance Kφ₀ ≈ V_λ φ₀ holds (it is the
c=2 cancellation). Then V₀ = Kφ₀/φ₀ ≈ (V_λ applied to φ₀)/φ₀ ≈ smooth average of V_λ = e^{u/2}.
**⟹ V₀ ≈ e^{u/2} (the PNT mean), at leading order.** Consistent with φ₀ = pole mode. --- ## 2. So δV is the FLUCTUATION of the primes — and that is the zeros ``` δV = V_λ − V₀ ≈ Σ_{n≤λ²}(Λ(n)/√n) δ_{log n} − e^{u/2} du = (prime measure) − (its PNT mean) = PNT ERROR TERM.
``` By the **Riemann–von Mangoldt explicit formula**, the PNT error term
is a sum over the zeros:
``` ψ(x) − x = − Σ_ρ x^ρ/ρ − log(2π) − ½log(1−x^{−2}).
``` Passing to the fluctuation of Λ(n)/√n (Abel summation, as in
weil-remainder-attack §2):
``` δV(u) ~ − Σ_ρ e^{(ρ−½)u} / ρ + (smooth). ``` **[!] δV is NOT a "pure density" object: its oscillatory part IS the sum over the
zeros Σ_ρ.** The mean (e^{u/2}) is density; the fluctuation is position. The audit had
flagged this risk ("δV might retain an echo of Σ_ρ") — upon carrying out the computation, **the echo
is the whole fluctuation**. --- ## 3. The bound we need, and its size We needed: ∫ δV |g|² ≤ β_λ ‖g‖² on ℓ^⊥, g band-limited of type L=2logλ. For g band-limited, |g|² is smooth with transform supported in [−L, L]. Pairing it
with the zero sum:
``` ∫ δV |g|² ~ − Σ_ρ \widehat{|g|²}(ρ)/ρ (projected onto ℓ^⊥, without the pole s=1).
``` The band-limited window only "sees" zeros below the horizon γ_ρ ≲ λ² (Lemma 2). On
the critical line the modulus of each term is
``` | e^{(ρ−½)u} | = (λ²)^{β−½}, β = Re ρ.
``` ⟹ **the bound is of order (λ²)^{Θ−½}, with Θ = sup_ρ Re ρ.** - **Θ = ½ (RH):** the fluctuation is O(1)·(smooth) → δV ≪ β_λ, (1) closes. But Θ=½ **is RH**.
- **Unconditional:** only Θ ≤ 1, giving (λ²)^{½} = λ → **δV can be ≫ β_λ ~ λ^{−2}.** **[!] The bound on δV is RH-equivalent in strength.** It is exactly the same wall
(Θ=½) that already appeared in weil-remainder-attack (the remainder R_λ) and in the
constant c=2 of Objective A. **The hope that "δV is the density side" (audit §2) was optimistic: once
computed, the fluctuation is the sum-over-zeros.** --- ## 4. Do the projection onto ℓ^⊥ or the smoothing save anything? Three escape attempts, all three honestly fail: - **Projection onto ℓ^⊥:** only removes the pole s=1 (the mean), not the oscillations of the zeros. The fluctuation lives in ℓ^⊥. Does not help.
- **Band-limited smoothing:** limits the sum to γ_ρ ≤ horizon, but each zero below the horizon still contributes (λ²)^{β−½}. Does not kill the dependence on β.
- **Zero density (not zero-free regions):** density theorems (Selberg, Bohr–Landau) say that *almost all* zeros are close to the line — this would control δV on average. BUT a **single** off-line zero ρ₀ below the horizon allows constructing g concentrated at γ₀ with A_λ(g,g) < 0. Positivity is sensitive to **individual** zeros, not to the average. ⟹ density is not enough. --- ## 5. Frank verdict of the pure-mathematics attack **[!] Inequality (1), attacked with the explicit formula, is RH-hard.** δV is the
PNT error term = the sum over the zeros; its bound is (λ²)^{Θ−½}, tight at
Θ=½ = RH. The projection onto ℓ^⊥ and the smoothing do not break the dependence on the position
of the zeros, and the sensitivity to individual zeros blocks the density argument. **This does NOT contradict the previous advances — it refines them:**
- **[P]** Schur + FLS are correct: the non-locality was resolved, the deficit was isolated to the pole mode, the complement has a 4× margin (real Brezis–Vázquez).
- **[!]** But the isolated residue (δV on ℓ^⊥) **is** the positivity of the explicit formula = RH. The cascade **localizes the wall with unprecedented cleanliness** (a single prime-fluctuation bound), but **does not cross it**. ### What this means for the strategy The cascade is the **best reduction available**, but its last link is RH-equivalent,
not PNT-derivable. The "density side" of δV (audit §2) was the mean (e^{u/2}); the
RH content is the fluctuation, and the fluctuation is the zeros. **The Θ=½ wall is the same as
always, now with the program's best localization.** **Frankness (a repeated lesson):** just as with "ε₀ density vs position", the explicit
computation shows that the candidate non-circular object contains, once computed, the
information of the zeros. This is not a failure of the CCM program (which is solid and has given
real unconditional results) — it is that **localized Weil positivity is
RH-equivalent, and no regrouping (Schur, FLS, pole) changes that**: they shift the
wall, isolate it cleanly, but the wall is the prime fluctuation = Σ_ρ. --- ## 6. What genuinely remains open (without self-deception) 1. **Is there ANY functional of δV that is insensitive to individual zeros and still sufficient?** (Unlikely: positivity ⟺ no off-line zeros ⟺ sensitive to individual ones.)
2. **The real unconditional piece:** everything that is NOT the δV bound — Link 1, FLS, improved-Hardy structure, ε₀^frame ~ C₀/λ² — are genuine theorems on the density side. The program delivers them; RH (the fluctuation) remains out of non-circular reach. **Final verdict of the analytic front:** attacked with full power (exact Schur, classical
FLS, explicit formula), Link 2 reduces to a single bound on the prime
fluctuation over ℓ^⊥, and that bound is RH-equivalent (Θ=½). The CCM program gives
the cleanest known localization of the wall, not its demolition.
