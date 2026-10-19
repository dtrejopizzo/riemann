# R183.028 — Synthesis of the Sonin route (rounds 1–2)

Files: R183_017 (goal), 018–019 (construction + NO-GO), 020 (review),
021 (semilocal Sonin), 022 (frequency multiplier), 023 (relative bound and
finite index), 024 (Connes later-route inventory, conjecture C_T),
025 (lemma L1), 026 (archimedean band falsifier), 027 (review).

## 1. What was proved (PROVED, verified)

1. **Exact identity** E_S = Son + R_{S,T} for every T and admissible S (018 §3).
2. **NO-GO for the entire Sonin trace**: for T>½log 2 with a prime in the
   window, n₋(R_{S,T}) = ∞ on primitives and in ker ∫h (018 Thm 5.1,
   019 Thm 4.1, two independent proofs; 020).
3. **Relative bound 0**: the prime term is Son-bounded with relative bound 0 and
   a compact remainder (023). With any fraction η>0 of Son given up, the negative
   index is finite, N(η,T) ≲ 4T·e^{2A/η} (023 Thm 3.1). Point 2's NO-GO is
   exactly the case η=0.
4. **Obligation 3 ≡ positivity with a gap on ker ℓ** (019 Cor. 3.2): there is no
   separate alignment condition.
5. **Exact spectrum of B_2** in ½log2<T<½log3: {0, ±log2/√2}, infinite
   multiplicity (023, verified by 027).
6. **ε is not positive definite** (026 §1): it is the symmetrization of a
   cross coefficient; ε̂>0 for |s|<s_m≈6.29 and ε̂~−2ε'(1⁺)/s²<0 at high
   frequency. The editor's Bochner reading is withdrawn.
7. **CC's "single negative direction" lives in the ξ metric** (H^{-1} type
   in h), not in L² nor in Son+L² (026 §2). Corrects 018 §6 and 024's N_T.
8. **Two-edge model at all orders** (025 Thm 2): the anticausal twist of the
   Fourier condition by ∏(1−p^{−1/2+is}) produces
   exactly −2 log p Σ_k p^{−k/2} Re c_h(k log p); the factor log p is the
   real length of the defect. 021's Christoffel heuristic (CF-S) is
   false in the model.

## 2. What was refuted or downgraded

* **CC's rank-one archimedean mechanism beyond |I|≈1.61**
  (026 §3, non-certified numerical Rayleigh–Ritz): #{λ(K_{I_T})>1} ≈ 4T−2;
  one direction up to T≈0.596 (matches phase 155's threshold), two
  from T≈0.803. With no primes. It is the structural reason CC stop at
  log 2; prime 2 is not the first obstacle.
* **(L-Son) with η uniform in T**: false (027, low-band falsifier,
  conditional on RH): since there are no zeros in (−γ₁,γ₁) and Son's density is
  positive there, n₋(E_S−(1−η)Son) ≥ 2γ₁T/π − O(log T) − 3, hence η_1(T)→1.
* **Frequency multiplier** (022): NO-GO or a strictly stronger version than
  D_T; Thm 3.3 downgraded to CONDITIONAL(RH); Rem 3.2 deals with a
  different object from (L-Son).
* **CCM's semilocal Sonin as a rigorous object**: CCM do not build the
  semilocal prolate nor prove semilocal positivity; only the strategy
  (024 inventory, negative 2020–2026 search in the local corpus).

## 3. What remains open, in decision order

1. **(E′)** (025): that the interaction density r_p between the support
   edge and the Fourier layer be in L²(ds). With no primes. With (Λ) (CC
   Thm 4.7's scaling law for λ≠1, routine) it gives L1′: Son_S − Son_∞ =
   (prime term) + Hilbert–Schmidt remainder. It decides the only point of
   disagreement between 021 and 024: whether F^{−1}[2π(ρ_S−ρ_∞)] has an atom
   −log2/√2 at ±log 2. 024's case is the stronger one.
2. **N_T** (024, in the ξ metric): inertia of the semilocal remainder. It
   carries all the arithmetic content (it is blind to deletion only via
   I_S, not via N_T).
3. **Structural requirement for every T** (026 §4, 027): any partition
   E_S = Son_{S(T)} + remainder with bounded-inertia remainder requires that
   the spectral density of Son_{S(T)} tend to 0 in the zero gap
   (−γ₁,γ₁), and in general that it concentrate on the zeros. That is, the
   positive part must "know" the zeros: the Sonin route carried to every T
   converges to the explicit formula itself (Connes–Moscovici 2022: the
   UV prolate spectrum matches the zeros). This is a reformulation
   of D, not an independent mechanism.

## 4. Editor's verdict

The Connes–Consani route is a genuine mechanism only in the
archimedean window T ≤ 0.80 (one or two certifiable negative directions).
Beyond that, every version of the mechanism (entire Sonin, uniform
fraction, frequency multiplier, semilocal Sonin) is either NO-GO or
equivalent to D in the window with an additional condition. We have not found an
idea giving positivity; we have found the exact necessary condition that
any extension must satisfy (§3.3) and the zero-free lemma that
decides whether semilocal Sonin is even a candidate (§3.1).

If Connes has a proof, based on what is seen here it must contain (i) a
semilocal positive part whose density vanishes in the zero gap, and (ii) a
control of the remainder's inertia using that S contains every p<e^{2T}.
Neither appears in the local 2020–2026 sources.

## Status

```text
Identity E_S = Son + R; NO-GO entire Sonin; relative bound 0; spectrum B_2   PROVED
ε not positive definite; CC's index in the ξ metric                          PROVED
two-edge model (exact prime term with log p)                                 PROVED (model)
#{λ(K_{I_T})>1} ≈ 4T−2, two directions from T≈0.80                           NUMERICAL, not certified
(L-Son) uniform η: false                                                     CONDITIONAL(RH)
L1 (semilocal Widom)                                                         CONDITIONAL (Λ)+(E′)
C_T ∀T without zero density in (−γ₁,γ₁)                                     false CONDITIONAL(RH)
N_T, row D                                                                   OPEN
```
