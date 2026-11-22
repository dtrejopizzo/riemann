# AUDIT_200_CERTDH_001: Audit of CERT_DH_001 (phase 200, round 17C)

**Audit.** Object audited: CERT_DH_001.md, CERT_DH_001_data/ and the text of P46 rem:FDH (l. 8334). Row D /
L′♯ is treated as an independent goal; F_DH is used only as a falsifier of positivity of the window form.

## Summary (≤200 words)

I redid the certificate at T = 9/5, odd sector, and obtained the same result bit for bit: [−7.05197470947908·10⁻⁹ ± 4.19·10⁻²⁵],
with ‖F‖² = 0.460238064960785 and 35 contacts (n ≤ 36). The computation took 14 min 31 s and the dyadic witness stayed identical
(md5 c89bd639…). I rederived every ingredient from scratch:

- κ and a_n = Re((1−iκ)χ(n));
- the functional equation with ε = +1 (relative error 10⁻³⁵ at 35 digits);
- the zero ρ (|F(ρ)| = 4·10⁻³⁶);
- C₀ = log(5/π) + ψ(¾) = −0.62115285320177…;
- the Lévy kernel K_{3/4} (checked against a quadrature at t = 7);
- b₂ = κ log 2.

All the ingredients are correct and match P46 lem:K / eq:m / eq:Aform after substituting (q, δ) = (5, 1). The script's
bounds hold: F lies exactly in P_T, because λ₁ is solved for in balls and the evaluation is monotone by inclusion. The
upper Γ bound is valid in the range where it is used, and the comb is a finite sum. The control with ζ in the same mold
(T = ½log5, 1, 1.8) gives no negative eigenvalue, and the χ₋₄ one stays in the noise.

**Verdict: PROVED with minor corrections**, all of them textual, in rem:FDH:
- the citation of the zero ρ is misattributed;
- a line is missing to justify applying lem:monoT to the DH form;
- "ξ ≈ 84.5" corresponds to the T = 2 witness;
- "beyond 9/5" needs to be made precise.

## 1. F_DH (verified)

My checks are in `CERT_DH_001_data/audit_independent.py` and `audit_independent_out.txt` (mpmath, 35 digits).

- **κ.** κ = (√(10−2√5) − 2)/(√5 − 1) = 0.284079043840412296028291832393126…, same as in the memo. ✓
- **Coefficients.** a_n = Re((1−iκ)χ(n)) with χ(1, 2, 3, 4) = (1, i, −i, −1) gives (1, κ, −κ, −1, 0). ✓ χ(−1) = χ(4) = −1, so χ
  is odd and corresponds to Γ_ℝ(s+1). ✓
- **Functional equation.**
  - The root numbers are ε(χ) = τ(χ)/(i√5) = 0.85065 + 0.52573i and ε(χ̄) = ε(χ)‾, of modulus 1 and different
    from ±1. The combination ½(1−iκ)L(χ) + ½(1+iκ)L(χ̄) is the one that exchanges the two root numbers and leaves ε = +1; the
    value of κ is fixed by that condition.
  - Λ_DH(s) = (5/π)^{s/2} Γ((s+1)/2) F_DH(s) satisfies |Λ(s) − Λ(1−s)|/|Λ(s)| ≤ 1.7·10⁻³⁵ at four points, including
    0.1 + 40i, which the memo did not include. ✓ (NUMERICAL)
  - The memo's value "2.5·10⁻³⁰" corresponds to 30 working digits and is consistent.
- **Off-line zero.** findroot starting from 0.8085 + 85.6993i converges to ρ = 0.808517182456637385553… +
  85.699348485377592171929…i, with |F(ρ)| = 4·10⁻³⁶. ✓ (NUMERICAL)
  - **Citation.** Davenport–Heilbronn 1936 proves there are infinitely many zeros in Re s > 1, but **does not** contain this ρ. This
    critical-strip zero is the one published by Spira (1994) and recomputed by Balanzario–Sánchez-Ortiz (2007).
  - The memo says "CITED, Spira 1994", which is correct. P46 rem:FDH attributes the zero to \cite{DavenportHeilbronn1936}, which
    **is incorrect** (correction C1). Spira is not in P46's bibliography.
  - For the certificate it suffices to say "located numerically; existence of off-line zeros CITED [DH1936]".
- **b_n.** The script's recursion is b_n = a_n log n − Σ_{d|n, 1<d<n} a_d b_{n/d}. It comes from F·(−F′/F) = −F′, i.e.
  Σ_{d|n} a_d b_{n/d} = a_n log n, with a₁ = 1 and b₁ = 0. ✓
  - b₂ = a₂ log 2 = κ log 2 = 0.196908588294…, with positive sign, matching check_fdh_out. ✓
  - b_n = 0 if 5 | n, because a_{5k} = 0 and every divisor d > 1 of n with d ∤ 5 leaves n/d a multiple of 5. Checked
    by induction.

## 2. Window form (verified against P46)

**ζ convention in P46.**
- eq:symbol/eq:m: m(τ) = Re ψ(¼ + iτ/2) − log π. It is 2·Re of the logarithmic derivative of π^{−s/2}Γ(s/2) at ½ + iτ, because
  2·(−½ log π + ½ψ(s/2)).
- lem:K: C₀ = ψ(¼) − log π and K(u) = 2Σ_k e^{−(2k+½)u}.
- The comb is v_n = 2Λ(n)/√n: the factor 2 merges n and n⁻¹ from the explicit formula with c even.

**Substitution for DH.** 2·Re d/ds[(s/2) log(5/π) + log Γ((s+1)/2)] = log(5/π) + Re ψ(¾ + iτ/2).
- **The conductor enters C₀** (it does not appear as a separate term "+log 5·‖F‖²"): C₀^{DH} = log(5/π) + ψ(¾).
- The Lévy representation, following the proof of lem:K with z = ¾ + iτ/2 and t = 2u, is
  Re ψ(¾ + iτ/2) − ψ(¾) = ∫₀^∞ (1−cos τu)·2e^{−3u/2}/(1−e^{−2u}) du, with K_{3/4}(u) = 2Σ_k e^{−(2k+3/2)u}. ✓
- I checked it numerically at τ = 7: the two sides agree to 10⁻³⁴.
- **The "??" in the question resolves as follows.** C₀ is the value of the symbol at τ = 0, so "ψ(¾)" and "Re ψ(¾)" are the same
  and there is no contradiction with m_DH(t) from DH_TRANSFER §1.3.
- C₀ = log 5 − log π − γ + π/2 − 3 log 2 = −0.62115285320177196917. ✓ This is exactly the number −0.621152853 from the memo, and
  in the script it enters divided by ‖F‖² on the correct line (C0·c0/c0).
- **Comb.** v_n = 2b_n/√n with b_n real. The explicit formula for a real self-dual series (ε = +1, real coefficients)
  has the same form as that of ζ, with Λ(n) replaced by b_n. ✓ With no pole there is no polar term, and the script places
  none. ✓
- **Lev(c).** It decomposes as ∫₀^{2T}(c(0)−c(u))K + c(0)∫_{2T}^∞K, because c = 0 for u > 2T. ✓ This is eq:Aform with
  (C₀, K, v) substituted.

**P_T.**
- P46 l. 121: P_T = {A(F) = B(F) = 0}, with A(F) = ∫F e^{t/2} and B(F) = ∫F e^{−t/2}. With no pole, these conditions are
  not necessary, but they are kept by convention (DH_TRANSFER §1.3/𝔗₁). Since restricting can only raise the infimum, the
  certificate on P_T is stronger than one without conditions. ✓
- **Odd sector.** A = ∫F cosh + ∫F sinh and B = ∫F cosh − ∫F sinh. If F is odd, ∫F cosh(t/2) = 0, so A = −B and
  P_T ∩ {odd} = {∫F sinh(t/2) = 0}. ✓
- **Full sector.** The cosh moment sees only the even part and the sinh moment only the odd part. That is why λ₀ and λ₁ are solved
  separately, as the script does. ✓

## 3. Certificate

**Re-run.** I ran `python3 cert_arb.py vec_T1.8_odd_N260.json 9 5 60 7000` and saved the output in
`CERT_DH_001_data/audit_rerun_T9_5_odd.txt`:

  CERT 𝔞/‖F‖² = [−7.05197470947908e−9 ± 4.19e−25] → NEGATIVE: PROVED

- λ₁ = −0.006725291275…, ‖F‖² = [0.460238064960785 ± 1.7e−16].
- Breakdown: C₀ = −0.621152853202, Lévy + tail = 3.00903502865, comb = 2.38788218250.
- It took 14 min 31 s. It is identical to the memo's file, and the witness JSON the script rewrites did not change (md5).

**Audit of the script `cert_arb.py`.**

(a) **F ∈ P_T exactly.**
- G₀ ∈ ℚ[x] is exact: its coefficients are integers/2⁶⁰ and flint's P_j are exact.
- λ₁ = −sh(G₀)/sh(x) is obtained as a ball containing the unique real λ₁* for which G₀ + λ₁*x satisfies the moment
  condition exactly. exp_moment is an exact finite sum evaluated in arb.
- The cross terms (G₀G₀, G₀x, xx) are exact polynomials in ℚ[s]. Q is a polynomial/rational function of λ₁ evaluated
  in ball arithmetic, which is monotone by inclusion. Hence Q(λ₁*) ∈ Q(ball).
- **No separate "projection error" is needed**: the certified F is F* = G₀ + λ₁*x, which lies exactly in P_T. The
  radius of λ₁ is already propagated into the result. ✓

(b) **‖F‖² = T·P(0), in balls.** ✓ c(u) = T·P(u/T) is obtained with the change t = Tx. ✓ The cross formula,
P(s) = ∫_{s−1}^1 A(x)B(x−s)dx with exact Taylor expansion of B, is valid for s ∈ [0, 2], the only range used. ✓

(c) **C₀**, in balls, with the closed form. ✓

(d) **Lévy.**
- M_r = r!2^{−r}ζ(r+1, ¾) − 2Σ_k Γ(r+1, 2Ta_k)/a_k^{r+1}. This is correct, because ∫₀^∞ u^r·2e^{−au} = 2r!/a^{r+1} and
  Σ_k (2k+3/2)^{−r−1} = 2^{−r−1}ζ(r+1, ¾). Also c(0) − c(u) = −T Σ_{r≥1} p_r(u/T)^r, from which
  levy = −Σ T p_r M_r/T^r. ✓
- **Bound Γ(r+1, x) ≤ 2x^r e^{−x}.** For integer r, Γ(r+1, x) = x^r e^{−x} Σ_{j≤r} (r!/(r−j)!) x^{−j} ≤
  x^r e^{−x}/(1 − r/x) ≤ 2x^r e^{−x} if x ≥ 2r. The script uses it only if x > 2(r+1), and since the x_j increase it applies to
  all the remaining terms. ✓
- **Remainder.** It uses x_j^r/a_j^{r+1} = (2T)^r/a_j and the geometric bound Σ_{j≥k} e^{−x_j} ≤ e^{−x_k}/(1 − e^{−4T}), since
  x_{j+1} − x_j = 4T. ✓ That remainder is added as a ball [0, b]. There is one detail against it: the term is "−2·up", so the
  remainder should enter with a sign; but arb(0, b) is symmetric and covers ±b. ✓
- **Tail of K.** ∫_{2T}^∞K = 2Σe^{−2Ta_k}/a_k. The cutoff at 200 terms has a geometric remainder ≤ 2e^{−2Ta_{200}}/(a_{200}(1−e^{−4T})). ✓
- The terms k = 0, 1, … with x ≤ 2(r+1) are computed with arb's gamma_upper, which is rigorous. ✓

(e) **Comb.**
- The b_n are computed in balls with κ in arb. ✓
- c(log n) = 0 if log n ≥ 2T, so the sum is finite.
- **Contacts.** log 36 = 3.5835 < 3.6 < log 37 = 3.6109. The comparison is decided in balls, and the assert catches
  the undecidable cases. ✓

**What the certificate proves (PROVED).** There exists F* ∈ P_{9/5}, odd, explicit polynomial, with 𝔞^{DH}_{9/5}(F*) < 0.

**Propagation to T ≥ 9/5.** It needs lem:monoT for the DH form. The proof is the same as for ζ:
- if supp F ⊂ [−T₀, T₀] ⊂ [−T, T], the comb terms with log n ≥ 2T₀ give c(log n) = 0, so 𝔞_T(F) = 𝔞_{T₀}(F);
- moreover P_{T₀} ⊂ P_T.

This argument was not written down for DH (correction C2). With it, the propagation is PROVED.

**Minor observation (does not invalidate anything).** The certificate is reproduced from the float vector and rounded to 2⁻⁶⁰ inside
the script. The witness JSON is an output, not an input. I recommend that cert_arb.py be able to read the witness directly,
so a third party can verify without the float vector.

## 4. Controls (NUMERICAL)

**χ₋₄** (control_chi4_out.txt). Uses C₀ = log(4/π) + ψ(¾) and K_{3/4} correctly.
- All eigenvalues lie in [−7·10⁻¹⁴, 0). This is floating-point noise, of the same order as DH's Galerkin noise
  (≈10⁻¹³).
- It is consistent, but the control is **weak**: it shows absence of negativity above 10⁻¹³, not positivity.
- The contrast with DH at T = 2 (−0.75) is indeed conclusive as a control of the mold.

**ζ** (new: `audit_control_zeta.py` / `_out.txt`). It is the same explore_leg mold with K_{1/4}, C₀ = ψ(¼) − log π and
comb Λ(n), with N = 60:

| T | odd | full (P_T) |
|---|---|---|
| ½log5 | +6.44·10⁻¹⁰ | +3.33·10⁻¹² |
| 1 | +7.3·10⁻¹⁴ | +6.3·10⁻¹⁴ |
| 1.8 | +7.8·10⁻¹⁴ | +7.0·10⁻¹⁴ |

- There is no negative eigenvalue. At ½log5 the result is positive above the noise, consistent with the ½log5
  certificates of P46 and with Mori's range (½log15).
- For T ≥ 1 the degree-60 Galerkin stays in the noise, as expected.
- The mold does not manufacture negativity for ζ. ✓

## 5. P46 rem:FDH text (l. 8334): corrections

Every numerical claim is backed by the files: 7000 bits, −2.3799·10⁻⁷, −0.75194, 10⁻¹³, the numerical threshold
in [1.6, 1.8] and the Ziad citation. "Proved" is honest for the negativity at T ≥ 9/5, once these corrections are applied:

- **C1 (mandatory).** "with a zero at ρ = … \cite{DavenportHeilbronn1936}" attributes to DH 1936 a zero that is not in
  DH 1936. It should be rewritten: "with a zero at ρ = 0.808517…+85.699348…i (located numerically, first computed by Spira;
  Davenport–Heilbronn proved the existence of zeros off the line \cite{DavenportHeilbronn1936})". Spira
  1994 / Balanzario–Sánchez-Ortiz 2007 can be added to the bibliography, or it can be left as "numerically located".
- **C2 (mandatory).** "negativity propagates by Lemma monoT": monoT is stated for ζ. It should add "whose proof
  (supports nest, $\PT$ increases, contacts with $\log n\ge2T_0$ vanish) applies verbatim to this form".
- **C3.** "the witness concentrates $|\hat F|$ near ξ ≈ 84.5" is a datum of the T = 2 witness (memo §1) and is NUMERICAL.
  It should read "the $T=2$ witness concentrates … (numerical)".
- **C4.** "cannot prove window positivity beyond T = 9/5" should say "on any window $T\ge\frac95$". Positivity for
  T < 9/5 remains open: it is neither excluded nor asserted.
- **C5 (optional).** The title "a Davenport–Heilbronn falsifier, proved" is correct. It would help to specify that the
  identification of the form (constant, kernel, comb) is verified by substituting (q, δ) = (5, 1) into lem:K/eq:Aform, which
  is exactly what this audit has just checked.

## 6. Verdict

**PROVED with corrections (C1–C4, text only).**
- The rigorous-numerical certificate was reproduced exactly.
- No mathematical ingredient is wrong: form, constant, kernel, comb, P_T, balls and tail bounds.
- The negativity of 𝔞^{DH}_T on P_T for all T ≥ 9/5 is PROVED.
- The lower bound of T_DH remains OPEN.

**Entry for the ROUTES-TRIED index:**
> AUDIT_200_CERTDH_001 (phase 200): CERT_DH_001 audited and re-run (identical, [−7.05197470947908e−9 ± 4e−25]).
> DH falsifier PROVED: 𝔞^{DH}_T is not ≥ 0 on P_T for T ≥ 9/5. Any method using only FE + Γ + bounded real
> Dirichlet series (𝔗₁) is excluded on those windows. Text corrections in P46 rem:FDH: the zero citation
> (Spira, not DH1936), lem:monoT for DH, ξ≈84.5 is from T=2, "beyond" → "T ≥ 9/5". Lower T_DH: OPEN.

Audit files: `CERT_DH_001_data/audit_rerun_T9_5_odd.txt`, `audit_independent.py`/`_out.txt`,
`audit_control_zeta.py`/`_out.txt`.
