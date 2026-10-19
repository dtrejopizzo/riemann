# EI_002 — The phase-190 family s_w = m^{−½}w(m/M): exact spectral form with the Euler tail, exact Mellin/ℤ-Poisson expansion of the test, self-duality of near-coincidences, and why no square emerges

Construction round (phase 192), starting point (ii) of the mandate. Pen and paper; no numerics. no equivalence with
any other statement is used. P47 = Paper 47; SPEC_B = phase-191/SPEC_B.
**No sign certified; no negative value of 𝔞_T for ζ.**

## 0. Corpus check — why not a retry
Inputs taken as PROVED from the record: prop:AM (A_M = Arch − Div − Near; spectral form (ii)), thm:oneprofile, lem:transl(iii) (both Tate
moments of c₀ vanish: ∫c₀e^{±v/2} = 0, and ĉ₀ = F̂₀² has a double zero at ±i/2, so also ∫v c₀ sinh(v/2) = 0, eq:Kprim), prop:sharp (polar-free
form), prop:wit-cheb (Chebyshev form), SPEC_B §1.3 (T*₃ lattice identity, collapse D_w(N) = 2c log N − small-divisor defects), EXP_003 C3.
Dead neighbours not reused: L2_030 (Near as shifted convolution: operator bookkeeping, Ramanujan expansion), N_022 (no exact matrix identity
from Λ∗1 = log beyond divisors), L2_012 §2 (AFE as class statement: NO-GO; AFE with coefficients exactly 1 = Poisson on ℤ), N_009 §1
(the integer comb is Poisson-self-dual at s = ½), N_020 (Poisson-dual exterior positions = thm:Z prime part). None of them writes the
test's spectral density |P_{s_w}|² through the exact Mellin identity (Theorem 2), the (0,0)-term statement with both Tate conditions
(Theorem 3), or the self-duality of near-coincidences in ℤ² (Theorem 4). The question the mandate asks — exact ℤ²-Poisson + FE, does a
square emerge — is answered (Theorem 5: no, by a PROVED obstruction).

## 1. Setting (P47 subsec:oneprofile, prop:AM; SPEC_B §1.3)
Profile F₀ ∈ P_{T₀}, |b| > ½, 2T₀ < ½log2; c₀ = c_{F₀}, ĉ₀ = F̂₀² > 0. M ≥ 2, X' := Me^{2T₀}. w ∈ 𝒲_η (C_c^∞[0,1), w ≡ c on [0,η]);
s_w := (m^{−½}w(m/M))_{m≤M}; G_M := Σ_{m≤M}s_mV_{log m}F₀ ∈ P_T for T ≥ T₀ + log M (lem:transl(i)); Q_M(w) := s_wᵀA_Ms_w = 𝔞_T(G_M).
Smoothed partial sum ζ_w(s;M) := Σ_{m≤M}m^{−s}w(m/M) (entire in s); P_{s_w}(τ) = ζ_w(½−iτ;M), |P_{s_w}|² = |ζ_w(½+iτ;M)|².
Euler tail R_X(s) := −ζ'/ζ(s) − P_X(s), P_X(s) = Σ_{n<X}Λ(n)n^{−s}.

## 2. Theorem 1 — spectral form with the Euler tail (PROVED)
  Q_M(w) = (1/π)∫_ℝ F̂₀(τ)² |ζ_w(½+iτ;M)|² Re R_{X'}(½+iτ) dτ
  (the integrand is defined off the ordinates of the critical-line zeros, where it extends continuously).
*Proof.* prop:AM(ii): Q = (1/2π)∫F̂₀²|P_s|²[m − Σ_{n<X'}v_n cos(τ log n)]; prop:boundary: m(τ) = −2Re ζ'/ζ(½+iτ); and Σ_{n<X'}v_n cos(τ log n)
= 2Re P_{X'}(½+iτ). ∎
Polar-free version (prop:sharp(ii), prop:wit-cheb, since G_M ∈ P_T ∩ H¹₀):
  Q_M(w) = (1/2π)∫F̂₀²|ζ_w(½+iτ;M)|² m^♯(τ)dτ − 2∫_{[1,X')}y^{−½}c_{G_M}(log y) d(ψ(y) − y),   c_{G_M}(u) = Σ_{m,k}s_ms_kc₀(u − log(m/k)),   (2.1)
m^♯ = m + (¼+τ²)^{−1}, regular at ±i/2. **PROVED.** (2.1) is the exact "archimedean minus Chebyshev fluctuation" split on the family, with the
polar main term removed by the Tate conditions of F₀ (not by an estimate).

## 3. Theorem 2 — the test is ζ plus a polar term plus an exact contour remainder (Mellin = ℤ-Poisson) (PROVED; Mellin inversion CITED)
Let W(z) := ∫₀^∞w(x)x^{z−1}dx (Re z > 0). Then W continues meromorphically to ℂ with a single simple pole at z = 0 of residue w(0) = c
(w is constant near 0 so all other poles are absent), W(z) = −(1/z)∫w'(x)x^zdx with the integral entire and rapidly decreasing on vertical
lines. For s = ½+iτ:
  ζ_w(½+iτ;M) = c·ζ(½+iτ) + M^{½−iτ}W(½−iτ) + ρ_M(½+iτ),   ρ_M(s) := (1/2πi)∫_{Re z = −A}ζ(s+z)M^zW(z)dz,  any A > 0, A ∉ {½, 3/2, …}.   (3.1)
*Proof.* Mellin inversion w(n/M) = (1/2πi)∫_{(c₀)}W(z)(n/M)^{−z}dz for any c₀ > 0; summing over n ≤ M (finite sum; extend to all n since w(n/M)=0
for n > M) with c₀ > ½ gives Σ_n n^{−s}(n/M)^{−z} = M^zζ(s+z) absolutely; shift the line to Re z = −A, crossing the poles z = 0 (residue cζ(s)) and
z = 1−s = ½−iτ (residue M^{1−s}W(1−s)); W decays rapidly on vertical lines and ζ(s+z) grows polynomially, so the horizontal segments vanish. ∎
**ℤ-Poisson reading (PROVED by the same computation).** M^{1−s}W(1−s) = ∫₀^∞x^{−s}w(x/M)dx is the ℓ = 0 Euler–Maclaurin/Poisson term of Σ_n n^{−s}w(n/M);
cζ(s) collects the singular boundary at n = 0 (the regularized value of Σ n^{−s}); ρ_M collects the nonzero dual frequencies. The three pieces are
the integer lattice ℤ entering the **test**, exactly.
**Size of the pieces (PROVED, CITED convexity/FE bound |ζ(½−A+it)| ≪_A (1+|t|)^A).** |ρ_M(½+iτ)| ≪_A M^{−A}(1+|τ|)^A. Hence for |τ| ≤ M^{1−ε},
|ρ_M| ≪ M^{−Aε}; and M^{½}|W(½−iτ)| ≪_k M^{½}(1+|τ|)^{−k}.
**Corollary (Fact N2 of phase 190 upgraded from NUMÉRICO to PROVED, descriptive).** At every critical-line zero ½+iγ with |γ| ≤ M^{1−ε},
|P_{s_w}(γ)| = |ζ_w(½+iγ;M)| ≤ M^{½}|W(½−iγ)| + O_A(M^{−Aε}) ≪ M^{½}(1+|γ|)^{−k} + M^{−Aε}: the family annihilates the low zeros to any polynomial
order. This is a zero-side *observation* (it uses ζ(ρ) = 0 only to evaluate the test), recorded as such; it is not used for the sign.

## 4. Theorem 3 — ℤ²-Poisson: the (0,0) term of the atom-n lattice sum, and self-duality of near-coincidences (PROVED)
For n ≥ 2 put g_n(x,y) := x^{−½}y^{−½}w(x/M)w(y/M)c₀(log x − log y − log n) on (0,∞)² (extended by 0), so that the atom-n part of the comb term of Q
is v_nΣ_{m,k≥1}g_n(m,k) (with the symmetrization of prop:AM(iii)). Poisson on ℤ² (g_n has compact support inside (0,∞)² for n ≥ 2, since x ≈ ny ≥ 2e^{−2T₀}y > y/M-scale and y ≤ M, so the support touches
neither axis; regularity: see review item 3) gives Σ_{m,k}g_n(m,k) = Σ_{(ℓ₁,ℓ₂)∈ℤ²}ĝ_n(ℓ₁,ℓ₂) and, with x = nye^v,
  ĝ_n(ℓ₁,ℓ₂) = n^{½}∫dv e^{v/2}c₀(v)·Ŵ_v(ℓ₁ne^v + ℓ₂),   Ŵ_v(ξ) := ∫dy w(nye^v/M)w(y/M)e^{−2πiyξ}.                                            (4.1)
(i) *(0,0) term.* ĝ_n(0,0) = n^{½}∫dy w(y/M)∫dv e^{v/2}c₀(v)w(nye^v/M). For y with nye^{2T₀} ≤ ηM (the bulk), w(nye^v/M) ≡ c and the v-integral is
    c·∫e^{v/2}c₀ = 0 (Tate). On the edge, expand w(nye^v/M) in v: the constant and linear terms vanish (∫e^{v/2}c₀ = 0 and ∫ve^{v/2}c₀ = 0, both Tate
    conditions), so ĝ_n(0,0) = n^{½}∫dy w(y/M)·[½(a²w''(a) + aw'(a))κ₂ + O(v³-moments)]_{a = ny/M}, κ₂ := ∫v²e^{v/2}c₀(v)dv ≠ 0 in general. So the
    continuous term vanishes **to second order** in the bulk and is an explicit edge quantity ≍ (M/n)·n^{½}·O(T₀²) at the edge. PROVED.
(ii) *Dual near-coincidences.* |Ŵ_v(ξ)| ≪_k M(1+M|ξ|)^{−k}: the dual term (ℓ₁,ℓ₂) ≠ 0 is negligible unless |ℓ₁ne^v + ℓ₂| ≲ 1/M with |v| < 2T₀, i.e.
    **−ℓ₂ ≈ ℓ₁n to relative precision e^{±2T₀}**: the dual lattice sum has exactly the near-coincidence structure of the primal one (m ≈ kn), with
    (m,k) ↔ (−ℓ₂, ℓ₁). PROVED. This is N_BUILD_009 §1's self-duality of the integer comb at s = ½ seen on the ℤ²-lattice form: Poisson summation on ℤ²
    maps problem (S) to itself; it does not diagonalize Near or separate it from Arch.
(iii) *Sum over atoms.* Σ_n v_nĝ_n(0,0) = 2Σ_nΛ(n)Ψ(n) with Ψ(u) := ∫dy w(y/M)∫dv e^{v/2}c₀(v)w(uye^v/M) smooth on (0,∞), and ∫₀^∞Ψ(u)du = 0 exactly
    (substitute z = uye^v/M; the v-integral becomes ∫e^{−v/2}c₀ = 0), **provided** the y-integration is cut at y ≥ 1 (otherwise ∫w(y/M)dy/y
    diverges and the (0,0) term is ill-defined). With the cut, 2Σ_nΛ(n)Ψ(n) = 2∫_{[2,X')}Ψ(u)d(ψ(u) − u) − 2∫₀²Ψ(u)du: the continuous main
    term over all atoms cancels by Tate (this is "Div ≈ −Near" of EXP_003 §3, PROVED here), leaving (a) the Chebyshev fluctuation at scale u ≍ M
    tested by Ψ (the **edge term** of EXP_005 §6, of size O(1)·(ψ − u)/u^{½}-type, not estimated here), (b) the explicit boundary term −2∫₀²Ψ from
    the atoms n ∈ {2,3,…} near the cut (the **small-divisor defects** at N = 2,3,4 of EXP_003 §4 in continuous form), and (c) the nonzero dual terms
    (near-coincidences, (ii)). PROVED as an identity (the cut at y ≥ 1 produces Euler–Maclaurin boundary terms at y = 1 which belong to (b)).

## 5. Theorem 5 — no exact positive representation emerges (PROVED by the record)
Insert (3.1) into Theorem 1: Q_M(w) = c²I_{ζζ} + I_{pp} + 2cI_{ζp} + I_ρ, with
  I_{ζζ} = (1/π)∫F̂₀²|ζ(½+iτ)|²Re R_{X'}(½+iτ)dτ = (1/π)∫F̂₀² Re[ζ(½−iτ)D_{X'}(½+iτ)]dτ,   D_X(s) := −ζ'(s) − ζ(s)P_X(s) = Σ_{n≥X}ℓ_X(n)n^{−s} (Re s > 1),
  ℓ_X(n) := Σ_{d|n, d≥X}Λ(d) ≥ 0  (uses Λ∗1 = log, i.e. the Euler product over ℕ: −ζ' = ζ·(−ζ'/ζ)),
  I_{pp} = (M/π)∫F̂₀²|W(½−iτ)|²Re R_{X'}dτ,  I_{ζp} = (1/π)∫F̂₀²Re[ζ(½−iτ)M^{½−iτ}W(½−iτ)]Re R_{X'}dτ,  I_ρ = the terms containing ρ_M.
(a) Each piece is the pairing of a nonnegative density (F̂₀²|ζ|², MF̂₀²|W|², …) or of a signed cross density with Re R_{X'}(½+iτ) = ½σ_{T'}(τ), and σ_{T'}
    is negative on the nonempty set U_{T'} (P47 subsec:band; thm:kappa(iv): κ = 1 < κ⋆). So no piece is termwise nonnegative, and no
    choice of w changes the symbol. PROVED.
(b) A representation Q_M(w) = Σ_i(squares) + (free p.d. part) valid for all w, M is a certificate of class (D) (def:PD, thm:sos, thm:D1):
    its content is λ_P itself — REF-D, excluded by the mandate. A representation through |ζ(½+iγ)|² = 0 at the zeros is lem:roughEF/thm:Z —
    zero-side, excluded. PROVED (lem:shape-restate, lem:shape-lin).
(c) The theta/Riemann identity π^{−s/2}Γ(s/2)ζ(s) = 1/(s(s−1)) + ∫₁^∞ω(x)(x^{s/2−1} + x^{−(s+1)/2})dx (CITED) rewrites ζ in I_{ζζ}, I_{ζp}; applied
    alone it transfers to Epstein E_Q (L2_012 §2(a), O10); here it is used jointly with the Euler tail R_X (absent for E_Q) and with ℤ (absent
    for Beurling), so the object passes O10/O11 — **by identification only** (W-identification, I5): the joint use names ζ, it does not
    produce a sign.
(d) **The Mellin split is exact but not estimable inside the margin.** The M^{−3} law of phase 190 (NUMÉRICO) lives on the A_M-minimizer; on
    the family, any bound on I_ρ of the form M^{−A}(1+|τ|)^A integrated against F̂₀²|ζ|m^♯ converges only for A < 3 − 1/6 (convexity), so
    the remainder cannot be bounded below the scale M^{−3}: to respect MUST-NOT 1 (no estimate with remainder) ρ_M must be carried as the
    contour integral (3.1). PROVED (CITED growth bounds).
(e) Where the sign would have to come from, exactly: Q_M(w) − [c²I_{ζζ} + I_{pp} + 2cI_{ζp}]_{|τ| ≤ M^{1−ε}} = (tail |τ| > M^{1−ε}) + (I_ρ): the low-
    frequency part is the twisted second moment of ζ at bounded height against F̂₀² and the Euler tail (an explicit number for each M, with
    no asymptotic parameter other than X' inside R_{X'}), and the tail beyond the Nyquist frequency of the lattice is where the family stops
    approximating ζ. On the record (Fact N2, NUMÉRICO) the margin on the minimizer is of the size of that tail; here that is ARGUED only.

## 6. Review (self)
1. Theorem 1 is a one-line rewriting of prop:AM(ii) + prop:boundary; the set of ordinates is null. ✓
2. Theorem 2: Mellin inversion for w ∈ C_c^∞ with w constant near 0 — W(z) = −(1/z)∫w'x^z: w' ∈ C_c^∞(η,1), so the integral is entire and
   O(|Im z|^{−k}); the only pole of W is z = 0. The contour shift needs ζ(s+z) of polynomial growth on Re z = −A: convexity/FE, CITED. ✓ The
   corollary on zeros is descriptive; no zero information is used in any sign statement. ✓
3. Theorem 3: Poisson on ℤ² needs g_n integrable with integrable transform. c₀ = F₀∗F̃₀ with F₀ continuous and piecewise smooth (jumps in
   F₀'), so c₀ is C¹ with bounded second derivative a.e.; hence ĝ_n(ℓ) = O(|ℓ|^{−2}) and Poisson holds with absolute convergence (the
   statement "g_n is C²" in §4 is to be read in this a.e. sense). ✓ The (0,0) second-order vanishing uses both Tate conditions of c₀ (eq:Kprim): PROVED. The "edge size" line is
   bookkeeping, not an estimate used for a sign. The cut y ≥ 1 is essential (noted; without it the ℓ = 0 term is ∞·0) — SPEC_B §4 Line 2
   ("vanishes to second order, ARGUED") is now PROVED in the bulk and corrected at the edge (it does not vanish atom by atom there; it
   vanishes after the sum over atoms with the PNT density, leaving the fluctuation (a)). ✓
4. Theorem 3(ii): the width bound on Ŵ_v is integration by parts k times in y (w smooth): ✓. Self-duality is an exact structural statement.
5. Theorem 5(a): U_{T'} ≠ ∅ is PROVED in P47 (subsec:band; thm:kappa(iv): the polar-free main-term symbol has g₁(0) = C₀ + 4 < 0). ✓ (b) is the record. (d): the exponent 1/6 is the convexity bound; with any
   subconvexity bound θ the condition becomes A < 3 − 2θ, still < 3. ✓
6. Non-linearity in Λ: present in the *test* (|ζ|² = |exp(Σ_nΛ(n)n^{−s}/log n)|² formally; concretely through the coefficients 1 of ζ_w,
   which encode Λ∗1 = log) and absent in the symbol (Re R_X is linear in Λ). Recorded in §7.
7. No numerics; no estimate used for a sign; no sign claimed. ✓

## 7. Compliance table
| clause | status | note |
|---|---|---|
| MUST-NOT: estimate with remainder | ✓ avoided | Theorems 1–3 exact; §5(d) shows the remainder must stay exact |
| MUST-NOT: O1–O15 invariant | ✓ | the identity (3.1) uses coefficients exactly 1 (fails for a_P, Beurling, Poisson positions, f_t, E_Q); Theorem 1 uses R_X (fails for E_Q); the collapse uses Λ∗1 = log (fails for O1–O5) — all by identification |
| MUST-NOT: class / symbol-statistic functional / opcalc / certificate / zeros / σ-transport / induction / REF-D | ✓ for the identities | the sign content remains T*₃(η) = (S) = REF-D for η ≤ η₀ (SPEC_B §1.4) |
| MUST: exact identity on the A_M family | ✓ | Theorems 1–4 |
| MUST: Λ non-linear | ✓/✗ | non-linear only on the test side (ζ_w, coefficients 1); the symbol side Re R_X is linear in Λ |
| MUST: Euler × FE × ℤ jointly as mechanism | partial | Euler: Λ∗1 = log in D_X and in "coefficients 1"; FE: m = −2Re ζ'/ζ in R_X, and θ/ω if ζ is rewritten; ℤ: Mellin polar term = Poisson ℓ = 0, ρ_M = dual modes, ℤ²-Poisson of the atom sums. They enter in the *same integrand* multiplicatively (|ζ_w|²·Re R_X) — jointly as factors, not as one mechanism with a sign |
| MUST: doubly-exponential margin from the identity | ✗ | margin on the family is polynomial (M^{−3}, NUMÉRICO) and sits in the τ > M^{1−ε} tail + I_ρ (ARGUED) |
| MUST: fluctuation not density | ✓ | main term (0,0) cancels to second order (Theorem 3(i),(iii)); D_X has nonnegative coefficients but Re R_X is indefinite |
| MUST: 10⁻⁵-sensitive | ✓ | Λ∗1 = log breaks for every weight change (SPEC_B A4ε/A5) |
| MUST: names ζ vs ζ_K | ✓ (named) | coefficients 1 on ℕ, Poisson on ℤ (for K ≠ ℚ: ideal lattice, Poisson on 𝒪_K, a different polar term M^{1−s}W·res) — named, not exploited |
| (R)(1)–(3) | ✓/✓/✗ on the symbol side | |
| (R)(4) zeros | ✓ | the Corollary of §3 is descriptive only |
| (R)(5)–(9) | ✓ formally | |
| (R)(10) | ✓ named | |

## 8. Column bookkeeping
Moved from YES to NO for this object: "doubly-exponential margin out of the identity" (NO: the identity places the margin in the
beyond-Nyquist tail and in the exact Mellin remainder, neither of which can be bounded without an estimate below the M^{−3} precision);
"non-linear in Λ" (NO on the symbol side; YES only through the test's coefficients 1); "Euler × FE × ℤ as one mechanism" (NO: they appear
as three separate exact factors/identities inside one integrand). Moved from NO to YES relative to EI_001: ℤ-integrality enters as a
mechanism (Mellin pole at z = 0 ↔ w(0), polar term ↔ ℓ = 0, dual modes ↔ ρ_M; ℤ²-Poisson of the atom sums with second-order Tate vanishing)
and the FE enters beyond m (through ζ itself in the test). PROVED new facts: Theorem 2 (+ Fact N2 upgraded), Theorem 3(i),(iii) (SPEC_B Line 2
made exact and corrected at the edge), Theorem 4 (self-duality of near-coincidences on ℤ²), Theorem 5(a),(d) (no termwise sign; Mellin split
not estimable within the margin). Residual: T*₃(η)/C*₃ unchanged (OPEN; REF-D for η ≤ η₀).
