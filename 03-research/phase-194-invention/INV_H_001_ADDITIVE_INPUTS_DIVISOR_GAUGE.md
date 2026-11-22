# INV_H_001 — Additive structure of ℕ in the window form: catalogue, divisor gauge, integer comb (track H)

Track H.
 Notation of Paper 46
(04-papers/46-row-d-dual-certificates/main.tex): m(τ)=Re ψ(¼+iτ/2)−log π (eq:m), v_n=2Λ(n)n^{−1/2}, 𝔞_T=m_T+Π_T on 𝒫_T,
N:=e^{2T}, combs and 𝔠⁺ (def:comb), ρ_κ, g_κ (thm:kappa), polar elimination (lem:polarelim), thm:shape, cor:shape.

## 0. Corpus / index check (done before building)
- ROUTES-TRIED-INDEX: Ramanujan/additive characters appear only as L2_030 §3 (components c_{p^b}(j) of Near; listed as an
  *admissible* direction in 06_OPEN_RESIDUES R9) and L2_031 (residue-balanced subspaces ⟺ D, Thm E). Vaughan/Selberg/large sieve:
  R167_103 Thm S (valid in every discrete Beurling system) and W-sieve NO-GO. Progressions: P46 prop:prog (BV/BDH/SW NO-GO).
  Poisson on ℤ / Euler–Maclaurin: EI_002 (s_w family), CA_C_007, PRINCIPIO RECTOR ("only additive ⇒ FE-generic", ARGUED).
  Hardy–Littlewood/Kloosterman: P149 additive pencil (Vaughan singular series, DEAD, T5). Mollifiers: G3D-159 (DEAD, DH/Epstein).
  Integer density: thm:ceiling (r ≤ 1 necessary), thm:kappa (ρ_1 ∉ 𝔠⁺). G1 (INV_G_001): Dirichlet algebra is Beurling-generic.
- Grid/crossword/phase 193: CA_H_002 anatomy (each term = additive weight at log q × monoid coefficient, linear in Λ) is the
  closest relative.
- **New reason.** None of the indexed items computes the window form of the *integer comb* (weight 1 on every n, the q = 1
  Ramanujan component) nor the exact symbol of 𝔞_T under the *divisor gauge* (free choice of the Möbius weights beyond N). Both
  are below. Where an item of the catalogue coincides with an indexed one, it is only classified, not retried.

## 1. Window-collapse lemma (PROVED, elementary)
𝔞_T(F) depends on Λ only through the vector (v_n)_{n<N}, and Re c_F is supported in (−2T,2T). Hence any identity
Λ(n) = Φ(n) valid for n < N (however it is derived: additive characters, Poisson on ℤ, combinatorial identities) produces the
*same* number 𝔞_T(F). An additive identity can change the value only through what it puts *outside* the window (a gauge) or
through an inequality applied to its pieces. So the question "how does + enter 𝔞_T exactly" is: (a) which exterior gauges it
allows, (b) which pieces become sign-definite.

## 2. Catalogue (task 1–2)
| # | Additive fact (fails in Beurling) | How it enters 𝔞_T exactly | Signed ζ-specific term? |
|---|---|---|---|
| A1 | Divisibility by characters 1[d∣n] = d^{−1}Σ_{a mod d} e(an/d) | Λ(n) = −Σ_{d<N} μ(d)log d·1[d∣n] for n<N (finite, exact) ⇒ Λ = Σ_{q<N} α_q(N) c_q(n), α_q(N) = −Σ_{d<N, q∣d} μ(d)log d/d (finite Ramanujan expansion; α_q → μ(q)/φ(q), Hardy). By §1 it collapses to the Möbius identity Λ = −(μ log)*1, which holds verbatim for Beurling (μ_B, 1_B). | No: regrouping of a Dirichlet-algebra identity ⇒ comb-generic (B″, G1). The infinite Hardy series does not even enter: interchanging q with the window sum diverges (Σ_{(k,d)=1} μ²(k)/φ(k) = ∞). |
| A2 | Ramanujan components c_q, q ≥ 2 | Dirichlet series Σ c_q(n)n^{−s} = ζ(s)E_q(s), E_q(s) = Σ_{d∣q} μ(q/d)d^{1−s}; E_q(1)=0 ⇒ **pole-free** pieces, symbol −2α_q Re[ζ(½+iτ)E_q(½+iτ)] (PROVED, §3). | Sign-indefinite (E_q oscillates); individually not in any cone. |
| A3 | q = 1 component = integer comb a ≡ 1 | Symbol m(τ)+2−2Re ζ(½+iτ) (Theorem H3). | Signed: **negative** at |τ| ≲ 2.1 ⇒ NO-GO piece (H3). |
| A4 | N(x) = ⌊x⌋ (Euler–Maclaurin; ζ − 1/(s−1) entire) | Only via the boundary value ζ(½+iτ) in the symbols of A2–A3, i.e. via Poisson on ℤ. | Beurling systems with N_B = ρx+O(x^θ), θ < ½ (e.g. F-P171, θ=83/208) continue to the line and the identities of §3 hold verbatim with ζ_B ⇒ comb-generic; full continuation + FE is shared by Epstein (FE-class, ARGUED in the index). |
| A5 | Vaughan / Heath-Brown identities | Pure Dirichlet algebra (−ζ′/ζ = F − G′... truncations) ⇒ by §1 the same vector; bilinear (type II) pieces are *nonlinear* in the comb but valid in Beurling (R167_103 Thm S). | No (B″); ℤ enters only when type II sums are *estimated* (large sieve, Poisson) ⇒ remainder ⇒ B′ (margin 4·10⁹Te^{−15.449T}). |
| A6 | Progressions / BV / Siegel–Walfisz | Constraints on ψ(x;q,c) | NO-GO, prop:prog (indexed). |
| A7 | Hardy–Littlewood correlations Σ Λ(n)Λ(n+h), Kloosterman/Weil bound | 𝔞_T is linear in Λ; a quadratic correlation enters only through a square/CS (G0 ⇒ REF-D or certificate) or an asymptotic (estimate ⇒ B′). Kloosterman sums do not occur in 𝔞_T on 𝒫_T (no spectral side of level q). | No exact signed term; P149 pencil DEAD (T5). |
| A8 | Integrality of positions {log n} (n+1 ∈ ℕ) | Positions of the comb; thm:ceiling, AL′ | Necessary-only (ceiling), no sign. |

Verdict of the catalogue (PROVED for A1–A3, A5 by §1 + §3; ARGUED for A4, A7 classification): the additive structure of ℕ
enters the window form *exactly* in one place only — the boundary value ζ(½+iτ) of the integer comb (Poisson on ℤ), carried by
the q-graded symbols of §3. Everything else is Dirichlet algebra (Beurling-generic) or an estimate.

## 3. The divisor gauge (Theorem H1, PROVED modulo the stated regularity)
For φ: ℕ → ℝ finitely supported with φ(d) = 1 for d < N put Q_φ(s) := −Σ_d φ(d)μ(d)(log d)d^{−s} (Dirichlet polynomial) and
a_φ(n) := −Σ_{d∣n} φ(d)μ(d)log d, so Σ a_φ(n)n^{−s} = ζ(s)Q_φ(s) and a_φ(n) = Λ(n) for n < N.

**Theorem H1.** For F ∈ 𝒫_T∩𝒟_T with ∫|F̂|²(1+|τ|)^{1/6+ε} < ∞,
  𝔞_T(F) = (1/2π) ∫_ℝ |F̂(τ)|² s_φ(τ) dτ,   s_φ(τ) := m(τ) − 2 Re[ ζ(½+iτ) Q_φ(½+iτ) ].
*Proof.* By §1 replace v_n by 2a_φ(n)n^{−1/2} (equal for n<N; Re c_F vanishes at log n ≥ 2T). Write the even measure
μ = Σ_n a_φ(n)n^{−1/2}δ_{log n} − Q_φ(1)e^{u/2}du on (0,∞); its cosine transform is Re[(ζQ_φ)(½+iτ)] + Q_φ(1)·½(¼+τ²)^{−1}
(Mellin: ζQ_φ − Q_φ(1)/(s−1) is entire; boundary value at s = ½−iτ; justified by Abel summation and the τ^{1/6} bound, CITED
convexity/Weyl). The polar part 2Q_φ(1)e^{u/2}du = ρ_{Q_φ(1)} contributes +Q_φ(1)(¼+τ²)^{−1} on 𝒫_T (lem:polarelim, thm:kappa(i));
the two (¼+τ²)^{−1} terms cancel. ∎
Remarks. (i) Q_N := Q_{1[d<N]} has Q_N(1) = α_1(N) and Q_N = Σ_q α_q(N)E_q, so H1 is the q-graded symbol of A1–A3 summed.
(ii) Consequence (PROVED): λ_A(T) ≥ sup_φ inf_τ s_φ(τ) — a new sub-family of dual certificates whose exterior measure is a
*divisor comb* Σ_{n≥N} 2a_φ(n)n^{−1/2}δ_{log n} (signed, ℤ-shaped), not in 𝒲_T (no e^{−(½+δ)u} decay).
(iii) (ARGUED) For every finite φ, inf_τ s_φ = −∞: Q_φ(½+iτ) is almost periodic and returns near any value, while ζ(½+iτ) takes
large values with prescribed phase on resonator sets (Bondarenko–Seip type; not proved here jointly with Q_φ). If so, the
divisor-gauge family is empty as a certificate family at every T, and the gauge must be infinite with ζQ_φ bounded on the line,
i.e. a mollifier of ζ — indexed DEAD (G3D-159, DH/Epstein). (iv) Beurling: the identical statement holds with μ_B, 1_B, ζ_B for
every discrete Beurling system whose ζ_B reaches the line (θ < ½) ⇒ H1 is comb-generic (B″); it is a tool, not a sign.

## 4. Theorem H3 — the q = 1 component (integer comb) is not positive (PROVED; one CITED value)
Let ν_ℤ := Σ_{n≥2} 2n^{−1/2}δ_{log n} (the comb of a ≡ 1, the q = 1 Ramanujan piece of Λn/φ(n)). By H1 with Q ≡ 1 and the n = 1
atom removed, its window form on 𝒫_T∩𝒟_T has the fixed symbol
  g_ℤ(τ) = m(τ) + 2 − 2 Re ζ(½+iτ).
g_ℤ(0) = C_0 + 2 − 2ζ(½) = −0.45147… (ζ(½) = −1.4603545…, CITED; m(0) = C_0 = −5.3721834). NUMÉRICO (mpmath, 15 digits):
g_ℤ(1) = −0.3130, g_ℤ(2) = −0.0426, g_ℤ(3) = +0.190. Hence, by the argument of thm:kappa(ii) (spectral-derivative packets
concentrating at γ with g_ℤ(γ) < 0, lem:wit-conc; the growth |ζ(½+iτ)| ≪ τ^{1/6} is harmless for packets of bounded tails —
this applicability check is the only non-verbatim step, ARGUED→PROVED after a line-by-line check of lem:wit-conc's hypotheses),
**ν_ℤ ∉ 𝔠⁺**: there is T_0 with b_T(ν_ℤ) < 0 for T > T_0.
Reading. The integer comb sits exactly at the ceiling (r = 1, thm:ceiling passes: G_M(1) = log M + O(1)) and is still negative,
but less so than its own main term ρ_1 (g_1(0) = C_0+4 = −1.37 vs g_ℤ(0) = −0.45): the ℤ-fluctuation 2−2Re ζ(½) = +4.92 versus
the continuous +4 is the *only* exactly computable additive gain, and it is not enough. Any proof of positivity of 𝔞_T must
therefore draw strictly positive contribution from the pole-free pieces q ≥ 2 (−2Σ_{q≥2}α_q Re[ζE_q]) at small τ, i.e. from the
*joint* ζ×(Möbius polynomial) phase — exactly the "+/· interplay at m ≈ kn" demanded by the semiring principle, now located as
an explicit symbol.

## 5. Candidate theorem and gap (task 3)
**Candidate H (OPEN).** For T ≥ T_1 there is a Dirichlet polynomial Q with Q ≡ Q_N on the window (coefficients −μ(d)log d for d<N)
and a test-side certificate such that m(τ) − 2Re[ζ(½+iτ)Q(½+iτ)] ≥ −η on the Paley–Wiener spectrum of type 2T, in the Toeplitz
sense ∫|F̂|² s ≥ 0 on 𝒫_T.
- Proved part: the exact symbol (H1), the lower bound λ_A ≥ sup_φ inf s_φ (H1(ii)), and the negativity of the q = 1 piece (H3).
- Gap: pointwise s_φ ≥ 0 is (ARGUED) impossible (H1(iii)); the Toeplitz statement on 𝒫_T is 𝔞_T ≥ 0 itself (REF-D). Proved
  positivity of any definite piece of 𝔞_T: **none** — the only signed piece found (q = 1) has the wrong sign.

## 6. Self-check (task 4)
- thm:shape(B″): H1 and the Ramanujan grading are identities valid for every Beurling system reaching the line ⇒ carry no sign
  (confirmed, §3(iv)). The ζ-specific input is ζ(½+iτ) itself (FE + Euler jointly enter only through the product ζ·Q_N), as
  prop:shape-inputs requires; but the sign statement in that product is REF-D.
- cor:shape(a): every use above is linear in Λ ⇒ measure identity on the window (lem:shape-lin(i)) ⇒ value λ_P. Confirmed.
- (B′): A5/A7 estimates excluded.
- Problem (R): H1 is a restatement inside clause "certificate = explicit formula" (thm:Z) with a ℤ-shaped exterior; no clause is
  discharged.
- REF-D: Candidate H is REF-D as stated. H3 is a genuine (negative) result.

## 7. Verdict
PROVED: §1 window collapse; A1 finite Ramanujan/divisibility identity; A2 pole-freeness of q ≥ 2 pieces; H1 divisor-gauge symbol
and certificate bound; H3 integer comb ∉ 𝔠⁺ (modulo the lem:wit-conc hypothesis check; g_ℤ(0) uses the CITED ζ(½)).
NO-GO (class 𝓒_H: additive identities of Λ — Ramanujan/additive characters, Vaughan/Heath-Brown, Poisson on ℤ/Euler–Maclaurin —
used linearly or as exact identities): comb-generic or FE-generic ⇒ B″ / cor:shape(a). ARGUED: H1(iii) (finite divisor gauges never
certify), A4/A7 classification. OPEN: Candidate H = REF-D. Residue (new, unindexed): the **small-τ sign of the pole-free q ≥ 2
symbol −2Σ_{q≥2}α_q Re[ζ(½+iτ)E_q(½+iτ)]** must exceed |g_ℤ| ≈ 0.45 on |τ| ≲ 2.1 in the Toeplitz sense — a concrete, finite-T
check of where the semiring interplay has to supply the sign.
