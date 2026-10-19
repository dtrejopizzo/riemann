# PROOF_L_SHARP_W_001 — Strategy W: zero-killing uncertainty

Phase 199, prover memo. Pen and paper. NUMÉRICO only from the shipped MORI15 data
(`MORI15_EXTREMAL_001_data/p{0,1}_zeros_*.log`) plus a two-line evaluation of a WKB minimum. Row D is an independent
target. No zero location is assumed: the explicit formula is used
only as the identity W_T(g) = Σ_ρ Φ(ρ)Φ(1−ρ), summed over all nontrivial zeros with multiplicity, and the pairs are kept
as written.
Constraints 1–18 of AUDIT_L_SHARP_1–6 were checked. This memo uses no sector reduction (constraint 18). The gauge is
handled through the gauge falsifier (AUDIT_199).

**Outcome in one line.** (i) There is a new reason relative to L30/L102. (ii) t* is **not** a degrees-of-freedom count. It
is the **caustic of the prolate continuation**, t* ≈ 2c − (2k+1)/2 = 4πμ − (2k+1)/2 with c = 2πμ. For μ = 15 and k = 4
this gives t* = 183.9. The data show a peak of |Fg*(γ_n)| at n = 72 (γ = 185.6) in **both** parity sectors. This is ARGUED
from WKB and matches the NUMÉRICO data. (iii) The BRS/Gram comparison ends in REF-D. The pair form minus any Gram/diagonal
form is a sum over off-line pairs, so the route stops there. (iv) PROVED: an unconditional Carleson-type sampling
inequality at the zeros. This is the "leakage ≥ κ·Σ|Φ_ℓ(ρ)|²" direction, with κ⁻¹ = O(log t*). The converse direction is
false, as the gauge falsifier shows. A corollary gives an upper bound on |W_T|. **L′♯ / (★★) OPEN. Row D OPEN.**

## 0. Corpus / index check; new reason vs L30 (task i)
- Sources read: the index entries L30 (BRS 2005.02996, Guinand–Weil, quasicrystals), L102 (Lysen: "zeros are inputs",
  P2 only), and SURVEY_MODERN l.25 (Fourier interpolation closed/low). Also S3 item 3 ("fails (1),(4); zeros are inputs"),
  AUDIT_L_SHARP_6, MORI15 §5, A_001 Thm 1.1, C_001 Prop 1.1/1.2 and Thm 2.1, and AUDIT_199 (gauge falsifier).
- **Why this is new.** In L30/L102 the zeros are interpolation nodes, used to reconstruct a function. Here the question is
  quantitative: if a window datum has a transform that is small at the zeros up to height t*, how much out-of-band energy
  must it carry? The question only uses that the zeros are a set of nodes with known counting function. It does not use
  their location or BRS's modular machinery as a sign source. §3 shows that the BRS reconstruction route itself cannot go
  beyond REF-D, so the only surviving content is §4, which does not use BRS.

## 1. Setting (from C_001, PROVED there)
For admissible f, with g = Ef and the window split ζ(s)f̃(s) = Φ_g(s) + Φ_ℓ(s):
- Φ_g is entire of exponential type T in s − ½.
- Φ_ℓ(s) = ∫_{−∞}^{−T} H(e^y)e^{sy}dy, where H is the aliasing tail Z r_f below the window.
- Φ_g(ρ) = −Φ_ℓ(ρ) at every nontrivial zero.
- W_T(g) = Σ_ρ Φ_ℓ(ρ)Φ_ℓ(1−ρ) (Prop 1.2).

On the data, Fg*(γ) means Φ_g(½+iγ).

## 2. Task (ii): what fixes t*

**2.1 The counting guesses fail (NUMÉRICO + elementary).**
- Zeros below 185: N(185) ≈ 72.
- Landau/prolate count of "cheap" modes: 2c/π = 4μ = 60.
- Equal local densities, (1/2π)log(t/2π) = 2T/2π: t = 2πμ = 94.
- Equal cumulative counts, N(t) = Tt/π: t = 2πeμ = 256.

None of these is t*. The general ratio N(2c)/(2c/π) = ½log(2μ/e) depends on μ, so there is no identity of the form
"N(t*) = number of cheap modes".

**2.2 The zero-killing below t* is structural, not a tuning (PROVED identity + ARGUED mechanism).** At every zero,
Φ_g(ρ) = −Φ_ℓ(ρ) (C_001 Prop 1.1(c)): the factor ζ·f̃ vanishes there. So |Fg*(γ)| at a zero is the size of the *tail
transform* Φ_ℓ at that zero. Between zeros, Fg* is set by the ζf̃ part. This explains why the two are 10⁻⁴⁴…10⁻¹² apart
(MORI15 §5).

By A_001 and MORI15 §2, Φ_ℓ(½+it) = Σ_n n^{s−1}R_{nλ}(s). The dominant n = 1 term is the Mellin transform of the exterior
datum ρ*(ω) = r*(λω), ω > 1. That datum is the continuation of the prolate ψ_k (k = 4), whose WKB local wavenumber is
κ(ω) = √((c²ω² − χ_k)/(ω² − 1)), with χ_k ≈ c(2k+1). Against ξ^{−it}, the stationary phase is at t = ω·κ(ω).

The function ω ↦ ωκ(ω) on (1,∞) has a single minimum:
- For χ = 0: the minimum is at ω = √2, with value 2c.
- In general: t_c = 2c − χ/(2c) + O(χ²/c³) = 4πμ − (2k+1)/2 + ….

For the terms n ≥ 2 (ω ≥ n), t ≥ (4/√3)c, which is larger. Below t_c, Φ_ℓ has no stationary point. It is therefore
smaller than any power (Airy-dark side), down to the level of the boundary layer at the window edge (≈ 10⁻³⁶). At t_c
there is an Airy caustic peak. Above t_c the values sit at a generic oscillatory level.

**2.3 Check (NUMÉRICO, shipped data; zeros used only as evaluation points).**
- μ = 15, c = 30π, k = 4: t_c = 183.88 (numerical minimum of ωκ, χ = 9c). For comparison, 2c = 188.50.
- Even sector: |Fg*(γ_n)| grows smoothly up to 9·10⁻³⁷ (n = 68–70). It then **peaks at n = 71, 72** (γ = 184.87, 185.60;
  3.6·10⁻³⁶ and 4.6·10⁻³⁶) and falls back to a plateau of (0.3–2)·10⁻³⁶.
- Odd sector: the peak is at the **same zeros** (n = 71, 72: 4.8·10⁻³⁴ and 6.0·10⁻³⁴), above a 10⁻³⁴ plateau.
- The peak lies just on the bright side of t_c, as an Airy maximum should.

**Identity for t* (ARGUED, NUMÉRICO-consistent):** t* = min_{ω>1} ω√((c²ω²−χ_k)/(ω²−1)) ≈ 4πμ − (2k+1)/2.

This answers MORI15 OPEN item "what fixes t*": t* is not set by the floor level. It is set by the bandwidth c of the
dominant exterior prolate. The floor level (≈ 10⁻³⁶ = the edge boundary layer, MORI15 §5.5) only sets the plateau.

## 3. Task (iii): BRS interpolation and the Gram form — REF-D, stop

**3.1 What BRS gives (CITED, as recorded in L30/L102; exact multiplicity and convergence hypotheses not re-checked).**
The reconstruction uses values at the zeros **together with samples at the points log n** (equivalently, Dirichlet-series
data). The kernels are modular integrals and the series converge in grouped form. The node system is not a Riesz basis:
the zero nodes alone are not a sampling set (§4.2 below), and the log-n samples are exactly the comb data. So writing
Φ_ℓ = Σ_ρ Φ_ℓ(ρ)b_ρ + (log-n part) only rewrites the explicit formula. The log-n remainder carries the whole comb. No
Gram bound ‖Φ_ℓ‖² ≍ Σ|Φ_ℓ(ρ)|² follows from BRS.

**3.2 Even granting a Riesz equivalence, the comparison is REF-D (PROVED algebra).**
- For real g, Φ(s̄) = conj Φ(s).
- If Re ρ = ½, then 1 − ρ = ρ̄, so Φ(ρ)Φ(1−ρ) = |Φ(ρ)|².
- Hence, exactly, Σ_ρ Φ_ℓ(ρ)Φ_ℓ(1−ρ) − Σ_ρ |Φ_ℓ(ρ)|² = Σ_{ρ: Re ρ ≠ ½} [Φ_ℓ(ρ)Φ_ℓ(1−ρ) − |Φ_ℓ(ρ)|²].
- The difference is supported on off-line pairs, if any exist. The same holds for any diagonal Gram form Σ w_ρ|Φ_ℓ(ρ)|².

**Plainly:** through this route, "the pair form dominates the Gram form with polynomial loss" is equivalent to a lower
bound on the off-line-pair sum by −(1 − κμ^{−A})·(Gram). That statement is the target itself. It is REF-D, and the
route stops here. No location assumption was used to reach this point.

## 4. Task (iv): the PROVED content

**Theorem W.1 (Carleson-type sampling at the zeros; PROVED, unconditional).** Let F be holomorphic on −¼ < Re s < 5/4,
with ‖F‖²_σ := (1/2π)∫|F(σ+it)|²dt bounded on that strip. Let t* ≥ 2, and let M(t*) := max_{|t|≤t*} #{ρ : |γ − t| ≤ ¼}
(counted with multiplicity). Then
  Σ_{|γ|≤t*} m_ρ |F(ρ)|² ≤ 48·M(t*)·sup_{σ∈[−¼,5/4]} ‖F‖²_σ.

*Proof.*
1. Every ρ has 0 < Re ρ < 1 (CITED, classical). So the disc D_ρ of radius ¼ about ρ lies in the strip.
2. Subharmonicity of |F|² gives |F(ρ)|² ≤ (16/π)∫_{D_ρ}|F|²dA.
3. A point s lies in at most M(t*) discs D_ρ with |γ| ≤ t*, counting multiplicity.
4. ∫_{strip}|F|²dA ≤ (3/2)·2π·sup_σ‖F‖²_σ, by Fubini and Plancherel on each line.
5. Combining: (16/π)·M·3π = 48M. □

Separation of the ordinates is not used. **M(t*) = O(log t*)**: it is bounded by N(t+½) − N(t−½), and the
Riemann–von Mangoldt formula with an explicit S(T) bound (Trudgian 2014, CITED) gives the explicit constant.

**Corollary W.2 (applied to the tail; PROVED).**
- Take F = Φ_ℓ. Here Φ_ℓ(σ+it) is the Fourier transform of H(e^y)e^{σy} on y < −T. Since y < 0, the weight e^{2σy} is
  largest at σ = −¼, so sup_σ‖Φ_ℓ‖²_σ = ‖ℓ‖²_* := ∫_{−∞}^{−T}|H(e^y)|²e^{−y/2}dy. This is finite because Ψ_f = O(e^{3y/2})
  (A_001).
- Since Φ_ℓ(ρ) = −Φ_g(ρ) is gauge-invariant, the bound holds with ‖ℓ‖²_* replaced by its infimum over gauges:
  **inf_gauge ‖ℓ‖²_* ≥ (48 M(t*))⁻¹ Σ_{|γ|≤t*} m_ρ|Φ_g(ρ)|²**.
- This is the requested "leakage ≥ κ Σ_{γ≤t*}|Φ(ρ)|²". The constant κ⁻¹ = O(log t*) is unconditional and uses only the
  zero density.
- **Caveat (OPEN):** ‖·‖_* is a weighted norm of the tail H = Z r. Converting it to L′♯'s leakage ℓ(g) = dist²(r, gauge)
  needs ‖Z r‖_* ≲_μ ‖r‖. That bound is not proved here. (C_001 proves only the opposite comparison, leak ≤ 18‖ℓ‖²_X/μ.)

**Corollary W.3 (upper bound on the form; PROVED).**
- ρ ↦ 1 − ρ is a multiplicity-preserving involution of the zeros. Cauchy–Schwarz then gives
  |W_T(g)| ≤ Σ_ρ m_ρ|Φ_ℓ(ρ)|².
- Summing Theorem W.1 over unit height blocks gives |W_T(g)| ≤ C∫_{strip}log(|t|+2)|Φ_ℓ|²dA.
- This is an unconditional upper bound by a log-weighted tail energy. It points the same way as the CITED Guo upper side
  (A_001), and it carries no sign.

**Proposition W.4 (the converse sampling inequality is false; PROVED).** No inequality Σ_ρ|Φ_ℓ(ρ)|² ≥ κ‖ℓ‖²_* can hold.
Take f supported in (−1/λ, 1/λ) (the gauge falsifier, AUDIT_199). Then g = 0, Φ_g = 0, and so Φ_ℓ = ζf̃ vanishes at every
zero, while ℓ ≠ 0. The zeros are a Carleson set but not a sampling set. Their deficiency is exactly the gauge, which is
the radical (A_001). □

## 5. Labels
| item | label |
|---|---|
| new reason vs L30/L102 | stated (§0) |
| counting identities for t* (Landau 4μ, N(t) = Tt/π, density crossing) | NO-GO (NUMÉRICO + elementary) |
| zero-killing below t* = Φ_g(ρ) = −Φ_ℓ(ρ) + Φ_ℓ dark below the caustic | identity PROVED; mechanism ARGUED |
| t* ≈ 4πμ − (2k+1)/2 (caustic of the k = 4 prolate continuation) | ARGUED; NUMÉRICO-consistent (peak n = 71–72, both sectors) |
| BRS reconstruction ⇒ Gram bound | NO-GO (not Riesz; the log-n part is the comb) |
| pair form − Gram form = off-line-pair sum | PROVED algebra; route = REF-D, stopped |
| Thm W.1 Carleson sampling at the zeros, κ⁻¹ = 48M(t*) = O(log t*) | PROVED (density CITED) |
| Cor W.2 tail-norm ≥ κ Σ_{γ≤t*}|Φ_g(ρ)|² (gauge-infimum) | PROVED; link to ℓ(g) OPEN |
| Cor W.3 |W_T| ≤ log-weighted tail energy | PROVED (upper side, no sign) |
| Prop W.4 the converse is false (gauge) | PROVED |
| L′♯ / (★★) | OPEN |

**Do not retry:**
- "BRS interpolation basis as a Riesz/Gram comparison for W_T". It is REF-D: the difference is the off-line-pair sum.
- "t* as a degrees-of-freedom count".
- "a lower sampling inequality at the zeros for tail data". It is false by the gauge.

The open residue of this strategy is the lower side: a lower bound on W_T in terms of tail energy whose wavenumbers lie
above the caustic t_c. That lower side is L′♯ itself. Row D OPEN.
