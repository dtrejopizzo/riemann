# PROOF_L_SHARP_FF_001 — Strategy FF: recombination of the Möbius lattice under Z (pen and paper; one exact integer table)

Phase 199, , no zero
datum is used, and
Notation as in AA_001 §1: μ ≥ 5, λ = √μ, a = ½log μ (= T), g even admissible on [−a,a], h(v) = v^{-1/2}g(log v),
H = h·1_{[1/λ,λ)}(|·|), f = Σ_{m<μ}μ(m)H(m·) + φ₀ (Thm D(i)), r = f̂|_{(λ,∞)}, Ψ̌(x) = Zr(e^x) = e^{x/2}Σ_{n≥1}r(ne^x), x > a.

## 0. Corpus / index check, and why this is not a retry
Read: AA_001 + AUDIT_13, A_001 (Thm 1.1, Prop 2.1, Prop 3.1), T_001 Lemma 1.1 (co-Poisson intertwining, PROVED classical,
AUDIT_5), AUDIT_3 K.3 (Poisson-in-n on PW tails returns window samples: "A Thm 1.1 read backwards"; do-not-retry: J.3-type
Poisson evaluation *as an estimate* on PW tails), EXTERIOR_DATUM_001, TEST_2X2_001, TEST_BRIDGE_001 + AUDIT_10, GRAM_INERTIA_001
(Constraint 25: lines m ≥ 2 are 10³²–10³⁴ × ρ_p, 33-digit cancellation), INV_U_001/U_001 (phase 195). Index block phase 199
grepped for "Poisson", "co-Poisson", "recombin", "c_N", "reflected translates": T_001 has the mirror identity, AUDIT_3 K.3
the circularity remark, AA_001 the lattice. **New reason:** nobody composed T Lemma 1.1 with the exact lattice (D.1). The
composition turns the 33-digit cancellation of GRAM_INERTIA into an *exact closed form* with integer coefficients (§1). This
is an identity, not an estimate, so it is not the J.3 technique AUDIT_3 forbids.

## 1. Theorem FF.1: exact recombination (PROVED)
**Definition.** For N ≥ 1 put c_N := Σ_{m|N, m<μ} μ(m). Since Σ_{m|N}μ(m) = [N = 1],
 c_1 = 1, c_N = 0 for 2 ≤ N < μ, c_N = −Σ_{m|N, m≥μ} μ(m) for N ≥ μ.        (FF.0)
So c is the **Möbius truncation tail** (Dirichlet convolution 1 ∗ μ·1_{[1,μ)} minus δ). It is supported on N ≥ μ.
**Theorem FF.1.** For every admissible even g, any filler, and every x > a (Abel/L² reading of Σ_n as in AUDIT_13):
 Ψ̌(x) = Σ_{N≥μ} c_N N^{-1/2} g(x − log N) + Φ_{φ₀}(−x) + ½φ₀(0)e^{-x/2} − ½f̂(0)e^{x/2},           (FF.1)
with g extended by 0 outside [−a,a], Φ_{φ₀}(y) = e^{y/2}Σ_{n≥1}φ₀(ne^y), and f̂(0) = ∫f = Σ_{m<μ}μ(m)m^{-1}Ĥ(0) + φ̂₀(0).
*Proof.* (1) For x > a and n ≥ 1, ne^x > λ, so r(ne^x) = f̂(ne^x) and Ψ̌(x) = Φ_{f̂}(x). (2) T_001 Lemma 1.1 (Poisson for
even f): Φ_{f̂}(x) = Φ_f(−x) + ½f(0)e^{-x/2} − ½f̂(0)e^{x/2}, and f(0) = φ₀(0) because H vanishes on |u| < 1/λ. (3) Insert
(D.1): Φ_f(−x) = e^{-x/2}Σ_n Σ_{m<μ}μ(m)H(nme^{-x}) + Φ_{φ₀}(−x) = e^{-x/2}Σ_N c_N H(Ne^{-x}) + Φ_{φ₀}(−x), with N = nm.
(4) e^{-x/2}h(Ne^{-x}) = e^{-x/2}(Ne^{-x})^{-1/2}g(log N − x) = N^{-1/2}g(x − log N) (g even). The cut 1_{[1/λ,λ)} is
|x − log N| ≤ a, i.e. g extended by 0. (5) Term N is nonzero only for x ∈ [log N − a, log N + a). For x > a this rules out
N = 1, and by (FF.0) c_N = 0 for 2 ≤ N < μ. □
**Reading.** The exterior datum is a **comb of translated copies of the window function itself**, placed at log N with
weight c_N N^{-1/2} (the truncated Möbius tail), plus the gauge mirror Φ_{φ₀}(−x) and the rank-two polar term. There is no
Fourier transform in (FF.1). The 33-digit cancellation of the lattice lines (Constraint 25) is exactly the step
Σ_{m|N}μ(m) = 0 for 2 ≤ N < μ. Consistency check: the same computation on |x| < a gives Φ_f(−x) = c_1 g(x) = g(x) (A Thm 1.1).
**Integer table (exact), μ = 15:** c_15 = −1, c_16 = 0, c_17 = 1, c_18 = 0, c_19 = 1, c_20 = 0, c_21 = −1, c_22 = −1, c_23 = 1,
c_24 = c_25 = 0, c_26 = −1, c_29 = c_31 = c_37 = 1, c_33 = c_35 = c_39 = −1. For a prime N ≥ μ, c_N = 1. If μ is a squarefree
integer, c_μ = −μ(μ).

## 2. Answer to the brief's premise (i): "Zr = one Fourier truncation tail of Ĥ" is FALSE as stated (PROVED)
Z and the lattice do not compose by products on the Fourier side. Ĥ(·/m)/m dilates by 1/m and Σ_n r(n·) dilates by n, so
the composite is ratio-indexed (AA_001 D(ii), C_{b/a} = μ(a)M̃_a/a). It never collapses to one σ = Ĥ. The recombination does
happen, but **only after the co-Poisson mirror**, in the window variable. There it gives (FF.1): window samples, not the
out-of-band part of Ĥ. So the requested split 𝒲_ext[tail_smooth + tail_edge] (Langer/prolate tail + kink line) is not the
exact structure. Those Fourier tails are asymptotic descriptions of the individual lines, and the lines cancel to 33 digits.
What the brief called "tail" is precisely: **the arithmetic tail c_N (N ≥ μ) of the truncated Möbius convolution, acting on
translates of g.** The cut at v = λ (x = T) and the cut at v = 1/λ (x = −T) become the two ends of each translate's support
[log N − a, log N + a].

## 3. Theorem FF.2: the edge channel exactly (PROVED)
Let μ ∈ ℕ (as in the μ = 15 data). On the first exterior cell a < x < min(a + log((μ+1)/μ), 3a), only N = μ contributes:
 Ψ̌(x) = c_μ μ^{-1/2} g(2a − x) + [Φ_{φ₀}(−x) + ½φ₀(0)e^{-x/2} − ½f̂(0)e^{x/2}].        (FF.2)
(log μ − x = 2a − x ∈ (a − log(1+1/μ), a), and g is even.) Hence the exterior edge jet is the **reflected window edge jet**:
Ψ̌^{(k)}(a+) = (−1)^k c_μ μ^{-1/2} g^{(k)}(a) + (gauge/polar jet), with c_μ = −μ(μ) for squarefree μ (μ = 15: c_15 = −1).
This proves the edge-channel structure measured in TEST_BRIDGE_001 and AUDIT_10. It also explains why the minimizer's edge
value g*(T) ≈ −1.4·10^{-34} sits at the leakage scale: the edge value is literally the first exterior sample, up to the
factor −μ^{-1/2}. On a general cell, the active translates are N ∈ [e^{x−a}, e^{x+a}) ∩ [μ,∞). Neighbouring translates
log N, log N′ overlap whenever log(N′/N) < 2a. The dyadic pair (N, 2N) overlaps for every μ ≥ 5 (log 2 < 2a). It carries
c_N c_{2N}(N·2N)^{-1/2}. For odd N ≥ μ, c_{2N} = c_N − Σ_{m|2N, m≥μ, m∤N}μ(m), and the subtracted sum includes the term
m = 2N. This is the (1,2) resonance of EXTERIOR_DATUM, now as an **overlap of two translates of g** and not as a
chirp/kink cross term. (Structural identification PROVED; its size and sign in 𝒲_ext: OPEN.)

## 4. Items (ii)–(iii) of the brief: status
- Smooth/edge/cross decomposition on the Fourier side: superseded by §2. The exact pieces of 𝒲_ext[Ψ̌] are 𝒲-bilinear
  forms between translates, B_{NN′} := 𝒲_ext-pairing of N^{-1/2}τ_{log N}g and N′^{-1/2}τ_{log N′}g, with gauge and polar
  rows added. Then 𝒲_ext[Ψ̌] = Σ c_N c_{N′} B_{NN′} + (gauge, polar). The B_{NN′} carry no Möbius data. B_{NN′} = 0 when the
  supports are disjoint *only for the local part* 𝒜. The Lévy kernel and the cross pairing with Ψ̌_log are nonlocal. PROVED
  (bilinearity).
- Edge–edge block = B_{μμ} restricted to the first cell. Its sign: OPEN (no proof attempted beyond (FF.2)). The "kink line
  g′(T)cos(2πλx)/x² + g(T)sin(2πλx)/x" is the Fourier-side asymptotic of one lattice line. Constraint 25 forbids using it as
  the size of the datum. NO-GO (as a technique, PROVED by §2): bounding the cross term via stationary phase between the
  Langer chirp and the kink line. Those objects are not the summands of the exact datum.
- Ψ̌_log: log n is not a lattice character, so Σ_n log n f̂(nu) has no co-Poisson mirror. (FF.1) does **not** extend to Ψ̌_log.
  The formal analogue would replace c_N with ℓ_N = Σ_{m|N,m<μ}μ(m)log(N/m) = Λ(N) for N < μ. That replacement is
  CONDITIONAL on a log-weighted mirror, which is not available. OPEN.

## 5. (iv) The remaining inequality and the Λ-input
**Exact reformulation (PROVED from FF.1 + A Thm 1.1).** On admissible data, L′♯ is the statement that
 𝒲_ext[ Σ_{N≥μ} c_N N^{-1/2} τ_{log N} g + (gauge) + (polar) ] ≥ κ·S(Ψ̌),
which is a quadratic form in g alone (all edge jets and all smooth parts are included automatically: the edge jet enters
through (FF.2) and the smooth part through the deep cells). The μ-dependence is explicit through the integers c_N (FF.0) and
the start of the comb at log μ = 2a. OPEN: the inequality itself.
**Λ-input and falsifiers (PROVED).** Step (2) is Poisson summation over ℤ, and it requires the unweighted sum Σ_n. For a
system (E_D, Λ_D) with summation weights a_D(n) ≢ 1 (cΛ with c ≠ 1: a_c = coefficients of ζ^c; a_P: Euler factor removed),
Σ_n a_D(n)f̂(nu) has no Poisson mirror. So FF.1 fails at step (2): the exterior datum is not a comb of window translates. If one
nevertheless uses the integer Z with the μ_c-lattice, then c_N^{(c)} = Σ_{m|N,m<μ}μ_c(m) = coefficient of ζ^{1−c}, which is
≠ 0 for 2 ≤ N < μ (e.g. c_2^{(c)} = 1 − c). The gap 2 ≤ N < μ closes and the comb starts at N = 2 inside the overlap zone.
Hence **the gap of the comb (no translates with 2 ≤ N < μ) is the Λ-specific (ℤ-Poisson + exact Möbius) feature**. It is
also the semiring feature: the gap is the identity 1 ∗ μ = δ, i.e. the interplay of (ℕ,+) (Poisson) and (ℕ,·) (Dirichlet
convolution). This is a structural feature, not a sign.

## 6. Labels
PROVED: FF.0, Theorem FF.1, Theorem FF.2 (edge jet = reflected window jet with weight c_μ μ^{-1/2}), §2 (the premise
"single Fourier tail of Ĥ" is false; recombination exists only after the mirror), the bilinear decomposition B_{NN′}, the
cΛ/a_P failure of step (2). NUMÉRICO: none (the c_N table is exact integer arithmetic). OPEN: sign of B_{μμ} (edge–edge), sizes
of the overlaps (N,2N), the log-weighted analogue for Ψ̌_log, L′♯. NO-GO (technique): stationary phase chirp-vs-kink as a
bound on the exact cross term. No sign of row D claimed. L′♯ OPEN. Row D OPEN.
