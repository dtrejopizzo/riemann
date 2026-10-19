# N_BUILD_013 — (E_γ, C): the packet limit is exactly critical, and the constant buys nothing

Pen and paper. F_T = F_T^γ the spectral-derivative family (Paper 47 §17), normalized ‖F_T‖ = 1; 𝓕_T Chebyshev fluctuation
(N_BUILD_001); target of N_BUILD_012 §5: (E_γ, C) limsup_T [𝓕_T(F_T) − 𝔞^♯(F_T)] ≤ C·g_κ(γ) (κ > κ*).

## Corpus check
Paper 47 prop:wit-Egamma, lem:wit-conc, rem:wit-cheb, prop:wit-coh(ii) (quartet vs degenerate limit), cor:void; R186_051 item 4
("(E_γ) for one γ ⇔ absence of quartets at all heights", zero side, Prop 3.3); R186_050 §4.3; L2_BUILD_010 (the centre γ = 0 is
exactly critical: C₀ = m(0) = −2ζ′/ζ(½), G2_B1_R1 Lemma 2). grep "Riesz|Abel|summab|boundary value|exactly critical|ξ′/ξ": the
centre-value identity exists (γ = 0); the identity at every γ and its consequence for constant-weakened (E_γ) are not in the record.

## 1. The limit object (PROVED, inputs CITED: functional equation, Hadamard product of ξ)
(a) Prime side. With w_T := c_{F_T}, lem:wit-conc (p = cos(τu) for each fixed u, dominated) gives w_T(u) → cos(γu) locally
uniformly, and w_T(u) = cos(γu)k(u/T) + o(1)-type with a fixed even profile k (the normalized autocorrelation of the window
derivative profile, k(0) = 1, supp k ⊂ [−2,2]). So 𝓕_T(F_T) is a smoothed (typical-means, scale T) partial sum of
 Re Σ_n 2Λ(n)n^{−½−iγ} minus its polar part, i.e. of Re(−2ζ′/ζ(s) − 2/(s−1)) at s = ½ + iγ.
(b) Boundary value. For γ not an ordinate of a zero, ξ(½+iγ) is a nonzero real multiple of a fixed phase, so Re(ξ′/ξ)(½+iγ) = 0
(ξ(½+it) is real; CITED). With ξ′/ξ = 1/s + 1/(s−1) − ½log π + ½ψ(s/2) + ζ′/ζ and Re(1/s + 1/(s−1)) = 0 on the line:
 **Re(−2ζ′/ζ − 2/(s−1))(½+iγ) = m(γ) + 1/(¼+γ²) = m^♯(γ).**
(c) Consequence. Whenever the smoothed sums of (a) converge to the boundary value of (b),
 lim_T 𝓕_T(F_T) = m^♯(γ) = lim_T 𝔞^♯(F_T)  (lem:wit-conc with p = m^♯),
so lim [𝓕_T − 𝔞^♯](F_T) = 0: **(E_γ) holds with equality; the packet limit is exactly critical at every γ** (γ = 0 is
L2_BUILD_010). There is no slack at any frequency for a constant C to use.

## 2. The alternative: divergence (CITED + ARGUED)
The smoothed sums of 1(a) are typical (Riesz-type) means of a Dirichlet series. By the Hardy–Riesz theory (CITED), summability of
such means at one point s₀ = ½ + iγ implies summability in the whole half-plane Re s > ½ to the analytic continuation, i.e.
that −ζ′/ζ − 1/(s−1) is analytic there. So existence of the limit at a single γ is a half-plane statement about ζ′/ζ. If it fails,
the means do not converge; by the Mellin/contour computation (shift past the singularities), the divergent part consists of
terms T·k̃(T(ρ − ½ − iγ)) with Re ρ > ½, of size up to e^{2T(Re ρ − ½)} times (T|Im ρ − γ|)^{−N}: exponential in T, oscillating
in sign (ARGUED: standard contour shift, not written out). No constant C bounds an exponentially growing oscillation; and since the
oscillation takes both signs, the limsup is +∞ in that case.
Sign check: a term with real part of either sign appears with growing modulus along T; limsup of the real part is +∞ unless the
phase is frozen, which is not the case when Im ρ ≠ γ or as T varies through the oscillation (ARGUED).

## 3. Theorem (PROVED modulo the CITED/ARGUED inputs of §1–§2): (E_γ, C) ⟺ (E_γ) for every C ≥ 0 and every γ
(⇐) trivial. (⇒) if (E_γ, C) holds, the limsup is finite, so we are not in the divergent case of §2; hence the means converge
and §1(c) gives equality, in particular (E_γ). ∎
**NO-GO for (Ω_{t₀}) via single frequencies:** packets cannot separate t_∞ > 0 from t_∞ = 1. Note cor:void does NOT obstruct
(E_γ, C) by the finite modifications (they shift the limit by a bounded amount, e.g. Λ + cδ₂ shifts it by c√2cos(γlog 2)), but §2
shows the constant-weakened statement at one γ is still a half-plane summability statement — of the same strength as (E_γ) itself
(R186_051 item 4).

## 4. What classical one-sided results give (coordinator's item (2))
(a) Hadamard-product lower bounds for Re(ζ′/ζ)(σ+iγ), σ > 1 (e.g. −Re ζ′/ζ ≤ ½log γ + Σ_ρ Re 1/(s−ρ) with all terms ≥ 0 for
σ > 1): they live in σ > 1, where the Dirichlet series converges absolutely; transported to the window they cost e^{(σ−½)·2T}.
Class C_PNT/C_zeros — and in any case not at σ → ½. (b) Montgomery–Vaughan mean values: mean-square in γ, no sign (W-coh, the
paper's own exclusion). (c) Selberg's lemma on ζ′/ζ near the line (approximating ζ′/ζ(σ+iγ) by a Dirichlet polynomial plus a sum
over nearby zeros): an identity, sign carried by the zero term, which is the content. None gives (E_γ, C). NO-GO (CITED inputs).

## 5. Where t_∞ > 0 could still be weaker
By §3 the uniform constant in (Ω_{t₀}) cannot be gained on concentrating packets. On frozen tests (support fixed) the ratio is a
fixed finite number (finite window). So the only regime where (Ω_{t₀}) could be strictly weaker than (N) is intermediate: tests whose
support grows with T but whose spectral measure does not concentrate at a point (spread spectra, e.g. |F̂|² approximating a fixed
smooth density h(τ)dτ as T → ∞). For such F, 𝓕_T(F) → (1/2π)∫ h(τ)·[boundary value m^♯(τ)]dτ if the means converge in L¹(h) —
again critical — or diverges otherwise. **Conjecture-level observation (ARGUED): (Ω_{t₀}) and (N) coincide on every family whose
spectral measures converge weakly; any gap between them would have to come from families with non-convergent spectral measures.**

## Self-review
1. §1(b) is classical and correct: ξ(½+it) = real function times nothing (Riemann's Ξ is real); Re(1/s + 1/(s−1)) at ½+iγ:
½/(¼+γ²) + (−½)/(¼+γ²) = 0. Re of −2/(s−1) = 1/(¼+γ²). So the boundary value is m^♯. Correct.
2. §1(a) "smoothed partial sum": the window profile k depends on η and on T only through u/T up to o(1); the polar part is handled
on P_T by N_BUILD_001 (A). Correct at the level of limits.
3. §2: Hardy–Riesz summability implication CITED; the divergence description ARGUED. §3's (⇒) depends on §2: label CONDITIONAL on
the CITED theory and the ARGUED contour description.
4. §2–§3 speak only of summability of
Dirichlet series and of the inequality (E_γ, C) itself.
5. Coordinate: nothing here duplicates Problem (A) (track L2).
No sign contact; no negative value certified.
