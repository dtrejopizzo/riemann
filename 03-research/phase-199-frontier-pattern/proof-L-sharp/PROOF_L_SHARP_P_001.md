# PROOF_L_SHARP_P_001 — Strategy P: rank structure of the coupling 2Q(F₀,G) in (★★_EM)

Phase 199, prover memo. Target: Lemma L′♯ = (★★_u) = (★★_EM) (AUDIT_L_SHARP_2 §7, constraints 1–11).
Notation of memo F (Thm F.1, F.2).

**Outcome.** L′♯ NOT proved. Conjecture (P) ("Q(F₀,G) = rank-2 pole part + part dominated by Q(G,G)") is
**FALSE as stated** (P.1 PROVED + P.4 NUMÉRICO): the coupling contains exactly −Q(G,G), and Q(G,G) is negative
(not positive) on PW data. What survives: (P.2) the F₀–F₀ piece of the pole (constraint 10) is exactly the residue
of the coupling at s = 0 (Γ_ℝ pole) — rank one, cancels identically; (P.3) the exact "reflection" form of (★★_EM).
The residual is not finite-rank (P.4 at μ = 15). No finite determinant reduction exists in this split.

## 0. Corpus check / not a retry
Index read: README l.456–458 (F, J, H), AUDIT_L_SHARP_2 §3.3 + "do not retry: any block argument on (F₀,G) ignoring
2AB"; 04_PHASES l.745 (R161_057–060: "reflection makes causal energies equal, not zero", REF-D) and l.783
(R162_2702c, Q(K·,K·) = −Q index argument, DEAD). Why not a retry: §3.3 forbids blocks *ignoring* 2AB; P keeps 2AB
and computes its exact interaction with the coupling (P.2). P.1 is the exterior-carrier, Mellin-side instance of
the R161_057 "equal energies" phenomenon; it is recorded as such, not used as a sign source.

## 1. Contour form of Q (PROVED)
For pairs (U,U_log) with real Mellin data, on Re s = ½, with γ_ℝ = Γ_ℝ′/Γ_ℝ, Θ_∞ = γ_ℝ(s)+γ_ℝ(1−s):
  Q(U,V) = (1/2πi)∫_(½)[U(1−s)(γ_ℝ(s)V(s) − V_log(s)) + V(1−s)(γ_ℝ(s)U(s) − U_log(s))]ds.
(Θ_∞|U|² = Θ_∞U(s)U(1−s); symmetrise s ↔ 1−s; the integrals are real.) With F₀ = ζ(1−s)R, F₀^log = −ζ′(1−s)R and
the functional equation (ζ′/ζ)(1−s) = −(ζ′/ζ)(s) − Θ_∞(s):
  **Q(F₀,V) = (1/2πi)∫_(½) R(1−s)[−ζ(s)(ζ′/ζ)(1−s)V(s) − ζ(s)V_log(s)]ds**   (agrees with F Thm F.2(iv)).

## 2. Results
**P.1 (reflection identity, PROVED, elementary).** Since Q(F₀,F₀) = 0 and F = F₀ + G:
  Q(F₀,G) = Q(F,G) − Q(G,G),   Q(G,G) = −Q(F,F) + 2Q(F,G),
  **𝔔 = Q(G,G) + 2Q(F₀,G) + 2AB = −Q(G,G) + 2Q(F,G) + 2AB.**
So the part of the coupling "dominated by Q(G,G)" is exactly −Q(G,G) itself, with the sign that turns Q(G,G) into
−Q(G,G). Conjecture (P) can hold in its "domination" form only if Q(G,G) ≥ 0; but then −Q(G,G) ≤ 0 and (★★_EM)
would need 2Q(F,G) + 2AB ≥ Q(G,G) — no gain.

**P.2 (the pole's F₀-piece is a residue, PROVED).** F is analytic on Re s > −1 (Ψ̌_ρ = O(e^{−3y/2})); R(1−s) on
Re s < 2. Shift Q(F₀,F) (= Q(F₀,G) + 0) from Re s = ½ to Re s = c′ ∈ (−½,0): the only pole is s = 0, from
(ζ′/ζ)(1−s) ~ 1/s (equivalently the Γ_ℝ(s) pole of Θ_∞), residue ½R(1)F(0) = −ζ(0)R(1)B. Growth: on Re s = c′,
|ζ(s)| ≪ |τ|^{½−c′}, R(1−s), F, F_log = O(|τ|^{−1}) (one jump at X = 1), integrand O(|τ|^{−3/2−c′}log|τ|).
Since A = F₀(1) + G(1), F₀(1) = ζ(0)R(1):
  **2Q(F₀,G) + 2F₀(1)B = 2J_{c′}(ρ),  J_{c′} := (1/2πi)∫_(c′) R(1−s)[−ζ(s)(ζ′/ζ)(1−s)F(s) − ζ(s)F_log(s)]ds,**
  hence 𝔔 = Q(G,G) + 2G(1)B + 2J_{c′}(ρ).
The pole couples the Q-null vector (constraint 10) through exactly ONE rank-one term, and that term is cancelled
identically by the s = 0 residue of the coupling. Shifting right instead (c ∈ (1,2)) gives Q(F₀,F) =
R(0)[log(2π)·A + F_log(1)] + I_c, residue from ζ(s) at s = 1, (ζ′/ζ)(0) = log 2π. J_{c′}, I_c are full bilinear
forms (no finite rank); they are the explicit-formula contour moved off the line, without sign.

**P.3 (finite-determinant reduction: NO-GO in this split, PROVED modulo P.4).** By P.1, (★★_EM) ⟺
  −Q(G,G) + 2Q(F,G) + 2AB ≥ κμ^{−A}dist²(ρ,𝒢̄₁).
A 2×2/3×3 determinant would need 2Q(F,G) to be finite rank in pole functionals and −Q(G,G) ≥ 0 to be provable;
the latter is (★★) itself up to the cross term (Q(G,G) = −𝔔 + 2AB + 2Q(F,G)): circular.

**P.4 (NUMÉRICO, mpmath/numpy; script PROOF_L_SHARP_P_001_numerics.py).** Basis g_k(t) = t²(μ²−t²)³cos(kπt/μ),
k = 0..9, ρ_k = ĝ_k|_{(1,∞)} L²-normalised (radical/ĝ(0) constraints not imposed: test of the algebra, not of
(★★)); τ ≤ 800 (μ=5), ≤ 1000 (μ=15); X ≤ 41/61. Checks: |Q(F₀,F₀)| ≤ 5·10^{−16}; 𝔔 matrix ≥ 0 at both μ.
| μ | spec 𝔔 | spec Q(G,G) | ‖Q(F,G)‖/‖Q(F)‖ | ‖P⊥Q(F,G)P⊥‖/‖Q(F,G)‖, 6 pole functionals |
|---|---|---|---|---|
| 5 | [≈0 … 12.6] | all ≤ 0, [−12.8 … ≈0] | 0.058 | 5·10^{−9} (basis effectively ~6-dim; inconclusive) |
| 15 | [1·10^{−7} … 7.30] | all ≤ 0, [−7.30 … −4·10^{−7}] | 0.0011 | 0.22 (not finite-rank) |
Pole functionals: A, B, ρ₀ = R(0), R(1), R′(0), F_log(1). Q(F₀,G) restricted to their kernel K is 0.55× its norm
(μ=15). Reading: on PW data 𝔔 ≈ −Q(G,G) to 0.1%, i.e. the window positivity is numerically the *negativity of the
line form on the Euler–Maclaurin defect G* (Poisson remainder below the window + quasi-mode), the cross term
Q(F,G) being small but not pole-controlled. Convergence: μ=5 values move ≤ 10% between τ ≤ 200 and τ ≤ 800;
μ=15 at τ ≤ 200 was NOT converged (spurious negative 𝔔), at τ ≤ 1000 consistent. NUMÉRICO only.

## 3. Residual (OPEN)
(★★_P)  −Q(G(ρ),G(ρ)) + 2Q(F(ρ),G(ρ)) + 2A(ρ)B(ρ) ≥ κμ^{−A}dist²(ρ,𝒢̄₁) on PW_μ,
with G ↔ ρ₀e^{−y/2}1_{y>0} − (Ψ_full − ρ₀e^{−y/2})1_{y<0} (AUDIT_2 §3.2). Its content is a sign of Q on the defect;
by P.1 this is the same statement, not a reduction. Falsifier status: P.1, P.2 are generic (FE + one pole); they hold
for cΛ/a_P/Beurling-with-FE (residue term changes), F-DH has no s=0 residue term (no pole) — not decisive (N_018).

## 4. Labels
PROVED: §1, P.1, P.2 (both shifts), P.3 as stated. NUMÉRICO: P.4. NO-GO: conjecture (P) in the form "rank-2 pole
part + remainder dominated by Q(G,G)" (sign of Q(G,G) wrong, remainder not finite-rank at μ=15); any finite
determinant reduction of (★★_EM) through the (F₀,G) split. OPEN: (★★_P) = L′♯. No sign is claimed. Row D OPEN.
