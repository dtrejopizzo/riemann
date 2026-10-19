# R183.033 — Synthesis of round 3 (R183_029–032)

Goal: develop what decides the new route (semilocal Sonin) toward closing D.
Three builders and one review.

## 1. Proved (PROVED, verified in R183_032)

1. **Scaling law (Λ)** (029 Thm A): for b ≤ 1,
   Tr ϑ(f)(Π_{S(1,b)} − Π_{S(1,1)}) = log(1/b)·f(1) + ∫f ε'_b, with ε'_b
   explicitly continuous. Sign and normalization match CC (43). With
   this, R183_025's semilocal identity (3.1) holds with no hypothesis:
   **Son_S − Son_∞ = (exact prime term) + ∫c_h ε'_p + (1/2π)∫|φ|² r_p**,
   with r_p = ρ_E − μ_D, μ_D ≥ 0 a measure, hence r_p ≤ a(1+ε)/(1−ε).
2. **The prolates are not the obstacle** (029): Y = Y_0 + Y_pro with
   ‖Y_pro‖₁ ≤ 8/p; r_p's tail comes from the Paley–Wiener projection
   compressed to the geometric layer.
3. **Semilocal form in the ξ metric** (030): c_h = (¼−∂²)c_ξ, with no
   cross terms; an interlacing lemma on arenas.
4. **Gap in the full form up to ½log5** (030 Prop 3.1, given Paper 47's
   thm:log5A, normalization verified): E ≥ 6.25e-13‖ξ‖² on primitives;
   with S = S(T) there is no negative direction in that window, and the
   rank-one correction is unnecessary (a = 0).
5. **Gap requirement, under RH** (031 Thm 1): every positive-multiplier
   part with bounded-inertia remainder ∀T has a limiting density
   supported on the zeros.

## 2. Numerical (not certified, reproduced by 032)

* Archimedean alone on primitives: one negative direction from
  T₁ < 0.5956, two from T₂ < 0.8027 (not converged in M; the proximity to
  ½log5 is an artifact).
* Fixed S = {∞,2}: positivity breaks at T ≈ 0.567; the negative direction
  is not aligned with ℓ.
* S = S(T): n₋ = 0 at every T tested up to 0.80; the gap on ker ℓ
  falls off superexponentially (4.2 → 0.22 → 4e-4 → 6.5e-8). Beyond
  T ≈ 0.9 double precision cannot decide.
* **Observed structural identity**: λ₁(archimedean form on ker ℓ) =
  λ₂(form on primitives) to 8 digits for every M. That is, ℓ's
  representative is exactly an eigen-direction. OPEN, to be proved.

## 3. Downgraded or refuted

* 031's "only theorem ⟺ RH": only ⟹ finite index. Under RH the
  condition is trivial with P_T = 0: the gap requirement is not a
  mechanism, it is a consequence.
* Global (E′) is probably false (oscillating amplitude ≍ |s|^{-1/2});
  (E′_loc) suffices, reduced to the microlocal hypothesis (M) with no primes
  (029 Thm C). (M) does not hide zeros, but only gives Hilbert–Schmidt R'_S.
* 029 §3.5 had (Δ) inverted; corrected: under (M) the atom at ±log 2 exists and
  the prime term is absorbed into Son_S (R183_024's branch).
* Modulation-invariance NO-GO (031): HEURISTIC.

## 4. Status of the route after three rounds

```text
Son_S − Son_∞ = prime term + ∫c_h ε'_p + ∫|φ|² r_p   PROVED (029 + 025)
(M) ⟹ R'_S Hilbert–Schmidt (018's NO-GO does not apply)  PROVED; (M) OPEN
full form S(T): gap up to ½log5                          PROVED (Paper 47)
n₋ = 0 for S(T) up to 0.80; superexponential gap          NUMERICAL
one aligned direction ∀T                                  DOES NOT EXIST (030 §7)
zero directions ∀T                                        ⟺ D (restatement)
archimedean λ₁(ker ℓ) = λ₂(prim)                          OPEN (observed identity)
row D                                                     OPEN
```

## 5. Editor's verdict

The semilocal Sonin route, carried as far as the sources allow,
produces an exact identity and a compact remainder (conditional on (M)),
but no new positivity. The only sign statement that
survives for every T is "the full form has no negative
directions," which is D. The superexponential gap in T is the TK ceiling of
phase 155 seen from the Sonin side. We have not found the mechanism
Connes claims to have; we have delimited that, if it exists, it must produce
a positive part whose density concentrates on the zeros without using the
zeros, and no construction from the source does this.

The only new and cheap thing left to prove: the identity λ₁(ker ℓ) = λ₂(prim)
(§2), which would explain why evaluation ℓ exactly removes CC's
direction. It is rank-one mathematics on K_I and does not touch D.
