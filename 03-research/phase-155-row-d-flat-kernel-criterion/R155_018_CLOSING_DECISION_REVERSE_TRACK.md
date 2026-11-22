# R155_018 — Closing decision: reverse-engineering track, cycle 2

Inputs: R155_011/012 (D for 1000 zeros + audit), R155_013/017 (decay tail lemma + audit),
R155_014/015 (row D for Z_1000 + audit), R155_016/019 (comb-vanishing LP + audit, 019 received: R155_016 survives with five edits, no retraction). end goal of record: deliver, in pure mathematics,
the row D that with rows A/B/C gives "RH for the universe of the first 1000 zeros".

## 1. Answer of record to the end goal

**Delivered, PROVED, in Paper 46 §7 (Prop. 7.12 prop:finuniv, Thm 7.9 thm:finZ, Cor. 7.11 cor:infinite):**

1. *Row D for Z_1000 exists, is unique among symmetric measures, and is the zero measure itself.*
 W_N(F⋆F̃) = Σ_{j≤N}|F̂(γ_j)|² ≥ 0; the dual certificate in the sense of programme (D) is
 μ_N = Σ_j δ_{±γ_j}; the toy "prime side" is g_N = μ̂_N = Σ 2cos(γ_j u), positive definite by Bochner.
 Rows A and B have no statement on a finite set of reals (no idele class group, no Frobenius family);
 row C transfers only as a definition.
2. *Theorem (no finite zero set carries a flat-top certificate).* For every T > 0, every finite symmetric
 multiset Z ⊂ ℝ∖{0} with |Z| ≥ 2 and every even continuous integrable w with w ≡ 1 on [−2T,2T] and
 w → 0, the function Σ_{γ∈Z} ŵ(τ−γ) takes negative values. (Proof: w·g_Z positive definite ⇒ rank-r
 Toeplitz block inside the window ⇒ recursion ⇒ w·g_Z = g_Z on a lattice ⇒ contradiction with decay.)
3. *Corollary: row D in the form of Theorem Z is intrinsically infinite.* Theorem Z certificates for ζ
 exist, when they exist, only through infinitely many zeros; a finite zero table evaluates f_w and never
 certifies it; the negativity of a truncation to |γ| ≤ Γ sits at |τ| ≳ Γ/2.

So the honest reading of "the D for 1000 zeros" is: the D that satisfies exactly those zeros is trivial
(their own spectrum) and does not exist in the programme's certificate form; the programme's D is a
property of the whole zero set, equivalently (Bochner on the prime side) of the whole prime comb.

## 2. Labels of record (this cycle)

| statement | label |
|---|---|
| Prop finuniv (trivial row D of a finite universe; uniqueness among symmetric measures) | PROVED |
| Thm finZ (no finite zero set carries a flat-top certificate; multiplicities via distinct values) | PROVED |
| Cor infinite (row D intrinsically infinite; truncation negativity at |τ| ≳ Γ/2) | PROVED |
| Prop 2.7/Cor 2.8 (location of negativity for finite edge regularity; phase (−1)^k i^{−(k+2)}; w^{(j)} → 0) | PROVED under hypotheses |
| Theorem D (decay tail bound: ν̂_w + 2ĝ₀ = 2Ŵ + Ψ_w − atoms; f_w ≥ m − A_T − E_at − multipliers − Dτ⁻²) | PROVED (extension of Lemma T) |
| Cor D.2 (comb-vanishing ⇒ E_at = 0, τ_stop ≤ max{2πe^{A_T+1+…}, √D+2}) ; Cor D.3 (bounded profile) | PROVED (display repaired) |
| Remark 2.5 (ℋ(E_N) dimension, Kreĭn determinacy, "obstruction disappears for ζ") | HEURISTIC |
| Zeros-to-find / primes-to-prove protocol; 1000-zero utility threshold; residual 10/100/1000 zeros | DIAGNOSTIC |
| +1.3486e−3 at ½log3 on [0,16.75] (dense enclosure) with f = −7.3 at τ = 17.4 | DIAGNOSTIC, not a certificate |
| Bounded-profile LP (P3): negative at all four windows, worse than unconstrained | DIAGNOSTIC |
| Comb-vanishing LP: negative at all four windows with τ_stop < 200 and positive tail bound — failure on all of ℝ for the returned weights (subject to R155_019: comb residual tolerance folded into E_at) | DIAGNOSTIC |
| "λ^P − λ^W is the whole value", "12 lobes", first-lobe = zero gap, TK ceiling applied to flat-top class, "above Theorem N", "no path at any T" unconditional | WITHDRAWN |

Row-D label unchanged. Endpoint of record unchanged: λ_min(A_{½log3}) ≥ 8.8577e−5. No sign for ζ beyond log 2.

## 3. What the track established about the shape of D for ζ (necessary, proved)

- never termwise in the zeros (lem:Rrig); never carried by finitely many zeros (thm:finZ);
- contacts of f_w on the class Nyquist comb 2π/U (band-limit + Theorem O equioscillation);
- tail of f_w governed by edge regularity paired with Σ_ρ e^{−2iTγ_ρ}, i.e. by prime-side data at the
 window edge; entry law (E), Theorem SC (positivity is a property of the complete initial segment);
- tail control needs either TV (Prop env, 10^18–10^40 for the weights found) or comb-vanishing
 (Theorem D, τ_stop ~ 10²); comb-vanishing forces effectively bounded support;
- with the tail controlled by comb-vanishing, the binding obstruction moves to τ ≈ 4–8 (the same LP without
 the comb has its minimum near τ ≈ 43): the small-τ failure is comb-induced (R155_019). The all-ℝ statement
 holds for the returned weights subject to a ~30 % margin on the quadrature of D(w); E_at ≤ 2e−14.

## 4. Decision

The reverse-engineering track has reached its end goal in the only form in which it is a theorem
(§1) and has exhausted its constructive side (bounded profile, comb-vanishing: negative on ℝ). It is
CLOSED as a constructive route to a new endpoint. Its proved by-products are in Paper 46.
Remaining pure-math items go to round 3 of the phase: (i) a Toeplitz-type ceiling for
min_{τ≤10} f_w over the compactly supported flat-top class (would close that class by proof);
(ii) the graded/decay hybrid; (iii) enclosures of Ceil(24,0.68) < 0, Ceil(24,log2) < 0;
(iv) λ^P version of Theorem 3.3; (v) Problem A lower bound.
