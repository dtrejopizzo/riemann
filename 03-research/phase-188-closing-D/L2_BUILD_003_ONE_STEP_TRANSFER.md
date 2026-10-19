# L2_BUILD_003 — One-step coercivity transfer Φ: NO-GO and why

Notation from L2_BUILD_002: c_k := c(T,k) > 0, W' := E_k ⊖ E_{k/2} ⊂ V_{k/2} = V_k ⊕ W',
s := s_{T,k}, K the Schur coupling of thm:coer-schur at level k. N_BUILD files: none existed at
time of writing; nothing used from (N).

## Corpus check
grep "one-step", "coercivity transfer", "renormaliz", "multiscale", "Haynsworth", "quotient formula"
over 03-research (all phases), 04-papers, 05-meta: phase-118 SPEC / phase-78/88 use "one-step" in
unrelated senses (LP steps, parity-scale split); Paper 47 uses Haynsworth for parity Schur
(thm:parityschur) only. No multiscale Tate-block tower or Φ-transfer was found. Not a repeat; but
§3 shows it is a restatement.

## 1. Exact one-step formula (PROVED)
For v ∈ V_k ∩ D_T, w ∈ W': 𝔞(v+w) = 𝔞(v+Kw) + s(w) (eq:coer-schur). Hence
  c_{k/2} = inf { [𝔞(u) + s(w)] / (‖u − Kw‖² + ‖w‖²) : u ∈ V_k, w ∈ W' },  (u := v + Kw)
and, sharply (thm:coer-schur(ii) at this level),
  min{c_k, λ_s}/(1+‖K|_{W'}‖)² ≤ c_{k/2} ≤ min{c_k, λ_s},  λ_s := λ_min(s|_{W'}).

### Proof of §1
V_{k/2} = V_k ⊕ W' (002, same argument as Lemma 2 with k/2 in place of k). Every element of
V_{k/2} ∩ D_T is v + w with v ∈ V_k ∩ D_T, w ∈ W' (W' ⊂ E_k ⊂ D_T, lem:coer-decomp(iv)). eq:coer-schur
applied to e = w ∈ E_k gives 𝔞(v+w) = 𝔞(v+Kw) + s(w); the substitution u = v + Kw is a bijection
of V_k ∩ D_T for fixed w, and since W' ⊥ V_k and v = u − Kw ∈ V_k,
‖v + w‖² = ‖u − Kw‖² + ‖w‖². Hence the exact formula is
  c_{k/2} = inf { [𝔞(u) + s(w)] / (‖u − Kw‖² + ‖w‖²) },
The two-sided bound is the sandwich
eq:coer-sandwich of thm:coer-schur applied to the pair (V_k, W') in place of (V_k, E_k); its proof
uses only the decomposition and c_k > 0. ∎

## 2. Theorem (NO-GO, PROVED): no Φ in the class 𝒞_scal
𝒞_scal := lower bounds c_{k/2} ≥ Φ(c_k, λ_s) valid for every closed semibounded form with these two
data. Then Φ ≤ 0 on (0,∞)².
*Proof (falsifier).* On ℝ² = V ⊕ W take 𝔞_b = [[c, b],[b, λ + b²/c]]. Its V-coercivity is c, its
Schur complement on W is λ, and λ_min(𝔞_b) = ½[(c+λ+b²/c) − √((c+λ+b²/c)² − 4cλ)] ≤ cλ/(c+λ+b²/c)
→ 0 as b → ∞. Details: the V-coercivity of 𝔞_b is its (1,1) entry c > 0; the Schur complement
onto W is (λ + b²/c) − b²/c = λ > 0; det 𝔞_b = cλ and tr 𝔞_b = c + λ + b²/c, so
λ_min = det/λ_max ≤ det/(tr/2) = 2cλ/(c+λ+b²/c) → 0. If Φ(c,λ) > 0 for some (c,λ), choose b with
2cλ/(c+λ+b²/c) < Φ(c,λ): contradiction. So any valid Φ(c,λ) ≤ 0. ∎
The form 𝔞_b embeds in the setting of thm:coer-schur (V one-dimensional, W one-dimensional); the
NO-GO is for the declared class 𝒞_scal (Φ valid for all such forms).
Consequence: positive transfer requires the coupling K (equivalently the angle between W' and V_k in
the 𝔞-metric). Any bound through ‖K‖ is a fixed-frame norm bound (thm:posext / lem:half class).

## 3. Theorem (PROVED): the sign transfer is tautological
c_{k/2} > 0 ⟺ λ_s > 0 (given c_k > 0) — 002 RG_k. Iterating from k₀ to 1:
λ_A > 0 ⟺ ∧_levels [S_{T,k_ℓ}|_{W'_ℓ} ≻ 0], and the conjunction is equivalent to S_{T,k₀} ≻ 0 by
Haynsworth additivity. So the tower decomposes the inertia of S_{T,k₀} into level pieces; it
cannot produce a sign without input at some level. "Minimizer geometry" at level ℓ is the vector
w_e minimizing s_{T,k_ℓ}(e+w) — itself defined by the sign problem at that level.

## 4. Review
- Falsifier in §2 is abstract (2×2), not a Weil form: the NO-GO is for the declared class 𝒞_scal
  (two-scalar Φ valid for all forms), which is exactly what "Φ(c, S|_W)" meant. Valid.
- §3 is correct and shows that the multiscale scheme of 002 has content only if some level is
  decided by a mechanism that is NOT itself a Schur sign. Verdict: Φ route closed as stated
  (NO-GO in 𝒞_scal; tautology otherwise). Move to a localization that does not use Tate blocks:
  L2_BUILD_004.
