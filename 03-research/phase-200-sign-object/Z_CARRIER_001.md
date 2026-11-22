# Z_CARRIER_001: Z as an operator on 𝒦₁ (phase 200, round 6)

ARGUED / OPEN / NO-GO / REF-D / NUMERICAL. Definitions verified against Paper 46 §22: def:ext (l.9601–9630: Z, Z_log,
gauge 𝒢_T, ℓ), thm:ext-half (l.9647), prop:ext-consol / eq:ext-starstar (l.9715–9730). Starting point: AUDIT_200_PIMU_001
§8 (the exact Λ lives in (a) Z = Poisson over ℤ with a_n ≡ 1, or (b) Guo L4.4 quantitative; every proposal names (a) or (b)
and the falsifier that separates them).

## 0. Corpus and index check (mandatory, before proposing)

Grep in `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for «approximate functional», «funcional aproximada»,
«Hardy–Littlewood», «AFE», «Riemann–Siegel», «Mellin», «Hankel», «Nehari», «Ingham», «second moment», «Estermann»,
«Kloosterman», «mirror», «reflect». Findings that condition this memo:

| index entry | what it covers | consequence here |
|---|---|---|
| PROOF_L_SHARP_C_001 (l.454) | E = multiplication by ζ in Mellin; Thm 2.1: off-line residue with Φ_ℓ = Σ n^{s−1}R_{nλ}(s); Thm 3.1: no diagonal weight in Mellin | §1 is a normalized recap in 𝒦₁, not a new result |
| PROOF_L_SHARP_A_001 (l.452) | null formal symbol (Θ_∞ + 2Re ζ′/ζ = 0 at σ=½); the whole value is a truncation defect at n ≈ λ/u | idem (F4) |
| PROOF_L_SHARP_Q_001 (l.462) | 𝔔_c = T_{a_c} + 𝐇_c, a_1 ≡ 0, Hankel part of symbol ζ; **NO-GO 𝒦_{T+H}** (Nehari/AAK/Widom) | discards "Hankel of ζ + Nehari" as a candidate |
| EI_003 (l.164) | symbol rigidity: identities on σ_T with FE/Euler/Mellin/Poisson/Riemann–Siegel are linear in Λ | every AFE used as an *identity* is linear in Λ |
| INV_K_001 (l.398) | ζ(½+iτ) universal carrier; "AFE/Euler–Maclaurin: reformulation" | AFE as a rewriting of the symbol: already registered |
| PROOF_L_SHARP_R_001 R.4 (l.463), S_001 S.3 (l.464) | log(k/t) weight of the harmonic; sign change at the AFE point √(τ/2π) | the AFE point already appeared as the harmonic sign boundary |
| PROOF_L_SHARP_LL_001 (l.504) | **NO-GO 𝒦^{group}** with fixed harmonic cutoff k₀; "frequency-dependent cutoff = AFE" is named as an escape, not executed | **the only unexecuted AFE residue**: frequency-dependent cutoff |
| FF_001 (l.487), T_001 (l.465), S_001 (S-dual) | co-Poisson mirror; exterior datum = comb of translates with gap c_N = 0 (2 ≤ N < μ); exact mirror only with c = 1 | the "second reflected comb" of the AFE coincides with this mirror (see §2.1) |
| EI_002 (l.160) | Poisson on ℤ² over the form, term (0,0) with second-order cancellation; no square | Gram of dilations via Poisson-ℤ² = duplicate |
| INV_H_001 (l.396) | HL/Kloosterman/Ramanujan/Vaughan used linearly: NO-GO 𝒞_H | shifted sums are only admitted in quadratic use |
| K1_OSG_001 / R-K1 (l.511) | every Hankel form using the gap [2,μ) with product structure NN′ fails P1+P2; the sign lives in the quotient N′/N | hard filter for any dual pair of the AFE (product mn ≈ τ/2π) |
| PI4_JUMPS_001 (l.526) / R-Π4 | Z_log of the comb: logarithmic singularities only on ℤ (Kummer); Tate mode | regularity of Z_log already registered as a site of Λ |

**New declared reason (index rule).** The only thing this memo attempts that does not appear as executed is the residue
of LL_001: the AFE with a **Mellin-frequency-dependent cutoff**, used not as an identity on the symbol (EI_003,
INV_K) nor as a Hankel bound (Q_001), but as a **phase-space partition** of the operator Z on 𝒦₁, to see whether the
cross form between the two blocks has a sign that uses (a). The rest of the brief's questions (symbol of Z, Ingham,
Re ζ/ζ) are answered with what is already indexed, without retrying.

## 1. Structure of Z on 𝒦₁

### 1.1 Normalization

Rescaling prop:ext-univ: w ↦ w/λ carries (λ,∞) to (1,∞); μ (or λ) enters only through the cutoff and the band of the
data. Let 𝒦₁ = L²((1,∞), dw) with the restriction that r be the trace, outside the band, of an admissible f. I use the
Mellin transform r̃(s) = ∫ r(w) w^{s−1} dw; Plancherel: ‖r‖²_{L²(dw)} = (1/2π)∫|r̃(½+it)|² dt.

In the variable y = log w (exterior datum Ψ̌(y) = (Zr)(e^y)), the factor w^{½} of def:ext turns L²(dy) into L²(dw):
‖Ψ̌‖²_{L²(dy)} = ∫ |Σ_n r(nw)|² dw. That is, with Z₀r(w) := Σ_{n≥1} r(nw), Z is Z₀ conjugated by the isometry
L²(dw) → L²(dy), and its Fourier transform in y is the Mellin transform of Z₀r on the line Re s = ½.

### 1.2 Symbol (PROVED, classical)

**Prop Z.1 (Müntz; CITED Titchmarsh §2.11, PROVED here for r ∈ C²_c(1,∞)).** For 0 < Re s < 1,

 ∫_0^∞ [ Σ_n r(nw) − w^{−1}∫_0^∞ r ] w^{s−1} dw = ζ(s) r̃(s).

Likewise, Σ_{n≥2} (log n) r(nw) minus its polar part (w^{−1}(∫r)·(−log w − γ_0) + w^{−1}∫ r(v) log v dv, constants
ARGUED up to convention) has Mellin transform −ζ′(s) r̃(s).

Consequences:
- **Z is diagonal in Mellin, with symbol ζ(s) on the line Re s = ½, *after* subtracting the polar mode w^{−1}∫r.** The
  polar mode is exactly the Tate mode e^{−y/2} of PI4 in the variable y, and its pairing with the rest produces 2AB.
- **Z_log has symbol −ζ′(s)** with the same polar correction (double pole of −ζ′ at s = 1).

### 1.3 Origin of unboundedness (PROVED)

Z₀ on L²(0,∞) is the multiplier of symbol ζ(½+it) plus a rank-one unbounded perturbation (polar mode).
1. High frequency: |ζ(½+it)| is unbounded (Ω-results of Hardy–Littlewood; CITED Titchmarsh 8.12), so the
   multiplier is not bounded on L².
2. Low frequency: the polar mode w^{−1}∫r is neither in L²(dw) near 0 nor bounded in norm of r over (1,∞)
   restricted to flat data (r ≈ 1 on [1, R]: ∫r ≈ R, contribution ≈ R²·∫_1^∞ w^{−2} = R², versus ‖r‖² = R).
The harmonic stacking of B1_FLAT is point 2 (the pole at s = 1), not point 1. In PW data of the aliasing scenario, the
relevant Mellin frequencies are large (§2.1), so point 1 is what governs the oscillatory block. (PROVED as a
description; the quantitative split in 𝒦₁ remains ARGUED.)

### 1.4 (★★) in Mellin (PROVED as a rewriting; recapitulates A_001, C_001, Q_001)

Let 𝒫 be the projection of L²(dy) onto (T,∞) (in 𝒦₁, onto (0,∞) after rescaling), read in Fourier/Mellin as the Riesz
projection conjugated by the modulation e^{iτT}. Let u = ζ(½−i·)r̃(½−i·) be the regularized image. With Θ_∞ := 2θ′,
where ζ(½+iτ) = e^{−iθ(τ)}Z(τ) (Hardy), on the line one has

 ζ′/ζ(½+iτ) = −θ′(τ) − i Z′(τ)/Z(τ),

(PROVED; the imaginary part has poles at the zeros of the line, but (Z′/Z)·u = e^{−iθ}Z′·r̃ is entire). The left-hand
side of eq:ext-starstar is

 Q(r) = (1/2π)⟨𝒫u, m𝒫u⟩ + 2Re⟨𝒫u, 𝒫(ζ′/ζ)u⟩ + 2AB.

As m = Θ_∞ + (polar term 1/(¼+τ²), which is what absorbs AB via prop:ext-consol (a)) and Re(iR) = 0 for real R,
decomposing u = 𝒫u + 𝒬u:

 **Q(r) = −2Re⟨𝒫u, θ′·𝒬u⟩ − 2Re⟨𝒫u, i(Z′/Z)·𝒬u⟩ + (polar boundary terms).** (1.4)

The whole form is **cross**-shaped between the part of u supported on y > T (the exterior datum) and the part on y < T
(which, via Poisson, is the window: the truncation Σ_{n>λ/w} r(nw)). This is F4/Thm 3.1 of C_001 in other notation:
pointwise-null symbol, the whole value is a commutator [𝒫, multiplier]. (1.4) is Q_001 Q.2 with c = 1. **There is
nothing new in §1**: it is the correct reading of brief question 1, and the brief is right (Z_log ↔ −ζ′,
⟨Zr, Z_log r⟩ ↔ Re(ζ ζ̄′) truncated).

The only new (PROVED, minor) precision: the cutoff does not act as a convolution on |r̃|²; it acts on u = ζr̃, and that is
why **no form ∫|r̃|²·(weight) can represent Q** (this is Thm 3.1 of C_001 again). Brief question 2, "inequality
of forms between ∫|r̃|²|ζ|²w and ∫|r̃|²Re(ζζ̄′)w", is ill-posed if w is a weight: with a weight, the relevant combination
is ∫|r̃|²|ζ|²(m − Θ_∞)w = 0 (except for the pole). It must be posed for the *commutators* of (1.4).

## 2. Candidates for a quantitative property of Z

Filter applied to each candidate: (F-a) uses Z = Poisson-ℤ with a_n ≡ 1 (site (a)); (P10) the mechanism is not
comb-generic (it does not hold equally for Beurling, cΛ, DH with its Z_a r = Σ a_n r(n·)); (R-K1) does not use the gap
with product structure; (F4) is not pointwise in Mellin; a falsifier is named.

### 2.1 (i) Approximate functional equation: two combs?

**Scale of the AFE point in the aliasing regime (ARGUED, stationary-phase computation; new as an observation).** The
datum r(ξ) = 𝓕f(ξ) with f supported on [−λ,λ] has local phase 2πuξ with u ∈ (0,λ) (position in the window). In
y = log ξ, the Mellin frequency is τ ≈ 2πuξ. For the term n of Z₀r(w) = Σ r(nw), ξ = nw, so τ_n ≈ 2πunw. The
Hardy–Littlewood/Riemann–Siegel cutoff point is N(τ) = √(τ/2π). Therefore

 n ≤ N(τ_n) ⟺ n ≤ √(u n w) ⟺ **n ≤ u·w.** (2.1)

The direct/dual AFE boundary in 𝒦₁ is the hyperbola n = u·w in the variables (integer index, window position, exterior
point). At the edge w ≈ λ and u ≈ λ (original scale) this gives n ≈ λ² = μ (with convention λ = √μ): **the AFE point
coincides with the end of the gap [2, μ) of FF_001**. It is the same scale as the semiring (m ≈ kn with k ≈ μ).

**Two combs (ARGUED, reduction to what is already indexed).** With the smooth AFE (CITED Iwaniec–Kowalski Thm 5.3:
exact, with weight V and its dual), Z₀ = Z_dir + Z_dual, where Z_dir sums n ≲ uw and Z_dual is the dual comb,
n ↦ τ/(2πn), which after undoing the stationary phase is the dual Poisson sum, i.e. **the co-Poisson mirror**, which
returns the window datum (FF_001: translates of the window with coefficients c_N; T_001; exact mirror of S-dual). The
cross form of (★★) between the two combs is the window–exterior form of (1.4). **As an identity, (i) is a duplicate**
(FF_001, S-dual, EI_003).

**And as an inequality with a dependent cutoff (residue of LL_001)?** Three obstacles:
1. **DH (PROVED, trivial):** the smooth AFE of IK Thm 5.3 uses only the functional equation. It holds for the
   Davenport–Heilbronn function with its gamma factor, conductor 5 and root ε. Every inequality that uses Z only via
   "AFE + cutoff + null symbol" transfers to Z_a (a = DH coefficients), and the null symbol m_DH + 2Re L′/L = 0 also
   holds for DH. Hence **DH is the falsifier that separates (i)**: if the target inequality is false for DH (which is
   expected, ARGUED, in large windows), no proof using only what the AFE gives can work.
2. **R-K1:** the direct×dual cross terms of |ζ|², D_N·χ̄D̄_N, pair m with ñ with **m·ñ ≈ τ/2π**: product structure. If
   they fall in the gap [2,μ), which by (2.1) is exactly the transition zone, R-K1 excludes them as a source of sign
   (P1+P2). The direct×direct terms (quotient m/n) are Toeplitz-in-log, the object (mn)^{−½}c_r̃(log n/m) of
   J_001/AUDIT_14, excluded by A §5/N_018.
3. **EI_003:** the Riemann–Siegel remainder at the cutoff has an explicit asymptotic expansion (CITED Gabcke) that is
   linear in the datum. Used as an identity, it is linear in Λ.

**Verdict (i): NO-GO (ARGUED) for the class "AFE with frequency-dependent cutoff as a partition of Z on 𝒦₁".**
The direct block is comb-generic (P10 fails: Beurling has its own Z_dir with n_B). The cross block is of product type
(R-K1) and DH-transportable. The residue of LL_001 is closed with the named DH falsifier.

### 2.2 (ii) Moments of |ζ|² (Ingham) and shifted sums

∫|ζ(½+it)|²|A(t)|²dt with A quasi-Dirichlet: the diagonal Σ_n |a_n|²/n · (log + 2γ − log 2π) gives the main term. The
shifted sums (Estermann, d(n)d(n+h)) enter in the off-diagonal.
- The diagonal is comb-generic: with ζ_𝒫 of Beurling, N_𝒫(x) ~ x gives the same log and a different constant. The 2γ is
  the Mertens constant of a_n ≡ 1, already identified in J.3 (2+γ−log 4π) as the place where a_n ≡ 1 fixes the sign of
  the deep mode. S_001/AUDIT_16 forbids "constants of ℕ as an independent source of sign".
- Off-diagonal: in 𝒦₁ the form is Σ_{m,n} F(m,n) with F(x,y) = log y·∫_1^∞ r(xw)r(yw)dw, **smooth in (x,y) real**.
  No weights d(n) appear: the only arithmetic datum is the lattice ℤ² and the log. Poisson on ℤ² gives the
  decomposition of EI_002 (duplicate). Estermann has no object here; it would appear only with tests built with
  coefficients of ζ, which is the "second twisted moment" of EI_003, and that is the mollifier (DEAD, G3D-159).
**Verdict (ii): NO-GO by duplicate (EI_002 + J.3 + AUDIT_16).** No new reason.

### 2.3 (iii) Positivity of Re ζ′/ζ or of Re ζ/ζ-type

On the line, Re ζ′/ζ = −θ′ is purely archimedean (FE). It is DH-transportable and is the part of the symbol that
cancels against m. In Re s > 1 it is −Σ Λ(n)n^{−σ}cos(t log n): it is TV-robust (C_001 Thm 6.1, ARGUED after AUDIT_13).
**NO-GO (duplicate).**

### 2.4 Table

| candidate | site (a)/(b) | P10 | R-K1 | falsifier that kills it | status |
|---|---|---|---|---|---|
| symbol ζ / Hankel + Nehari | (a) weak | fails (Q_001) | — | cΛ c<1 (high frequency) | NO-GO (Q_001) |
| (i) AFE as identity | (a) | — | — | — | duplicate (FF_001, S-dual, EI_003) |
| (i′) AFE, dependent cutoff, inequality | (a) only via FE | fails (DH) | fails (cross product block) | **DH** | NO-GO ARGUED (new) |
| (ii) Ingham / Estermann | (a) | generic diagonal | — | Beurling (diagonal) | duplicate |
| (iii) Re ζ′/ζ | none | fails | — | DH | duplicate |
| (iv) see §3 | (a)+(b) | to be tested | quotient | Beurling, cΛ, DH | OPEN |

## 3. The strongest surviving candidate

### 3.1 What remains after §2

Putting together (1.4), §2.1 and R-K1:
- Everything Z contributes *through its symbol on the line* (multiplier ζ, FE, AFE, RS, moments) is DH-transportable
  or comb-generic. I state this as a restriction.

**Restriction R-Z1 (ARGUED, new).** An inequality on 𝒦₁ that uses Z only via its Mellin symbol on the line
Re s = ½ (as a multiplier, FE, smooth AFE or Riemann–Siegel, or weighted moments) holds equally for the DH family
(Z_a, a = DH coefficients, same Γ-factor except for the conductor). Hence it cannot separate DH. Separating DH requires
the Euler product, which in 𝒦₁ appears only in three places:
- (α) ζ′/ζ = −ΣΛn^{−s} for Re s > 1 (TV-robust, C_001);
- (β) the quantitative radicality of Guo L4.4 (site (b));
- (γ) the Möbius identity 1∗μ = δ that produces the gap c_N = 0 for 2 ≤ N < μ (FF_001, lem:ext-mob).

DH does not have (γ): its inverse coefficients (1/L_DH) are not multiplicative, and the "gap" of truncation of its
Dirichlet inverse does not vanish (ARGUED). Beurling has (γ) with μ_𝒫 but without the lattice ℤ (no Poisson). cΛ has
ℤ but its inverse is d_{−c}, with no exact gap (the weights are d_c).

**Conclusion of the selection:** the only site common to (a) and to the Euler product that is **non-linear and a
quotient** is the interaction between the **Möbius gap (γ)**, which lives in the index N < μ, and the **Poisson
lattice**, which lives in the AFE transition n ≈ uw ≈ μ of (2.1). In the language of R-K1: the gap protects the
products NN′, and the sign lives in the quotients N′/N. The candidate is the form of (★★) restricted to pairs
(N, N′) with N′/N = k fixed in the transition zone.

### 3.2 Candidate (iv): quotient form in the transition

Let Ψ̌ = Σ_{N≥μ} c_N N^{−½} g(· − log N) + mirror + polar (FF_001, PROVED). The Toeplitz term of 𝒲 pairs translates
with quotient N′/N = n (K1_OSG: (22,44), (26,52), … at μ = 15). Define, for each k ≥ 2, the **quotient block**

 𝔅_k[g] := Σ_{N≥μ} c_N c_{kN} (kN²)^{−½} · 𝒲(g, g(· − log k)) (3.1)

with the full bilinear form 𝒲 of def:ext. The sum over N is the multiplicative autocorrelation of the Möbius
truncation coefficients c_N at dilation k: it is a (+,·) object, because c_N is a truncated Möbius sum at N (additive
in the cutoff) evaluated along the multiplicative orbit N ↦ kN.

**Target theorem (OPEN).** There exist κ > 0 and A such that, for every μ ≥ 5 and every g in the core,

 Σ_{k≥1} 𝔅_k[g] + (mirror, polar) ≥ κμ^{−A} dist²(r_g, 𝒢̄_T), (3.2)

and the chain (3.2) ⇒ eq:ext-starstar ⇒ L′♯ is exactly prop:ext-consol (PROVED, Paper 46). (3.2) is not new as an
inequality: it is (★★) rewritten in the basis of translates (REF-D as a statement). What the candidate adds is
**where the bound is sought**: in the multiplicative autocorrelation of c_N, not in the symbol.

**Where the exact Λ enters.**
- c_N = 0 for 2 ≤ N < μ: requires 1∗μ = δ with a_n ≡ 1 (site (a) + (γ)). Fails for cΛ (weights d_c) and for DH.
- The Toeplitz term of 𝒲 carries v_n = 2Λ(n)/√n in log k: the block 𝔅_k pairs the quotient k with Λ(k), and by
  Λ∗1 = log it regroups as Z_log (site (a), Kummer).
- The lattice ℤ: the translates g(· − log N) with N ∈ ℕ, dualized by Poisson (FF_001).
- Falsifiers: Beurling breaks the lattice (the N_𝒫 are not closed under +1 and the mirror does not exist). cΛ breaks
  the gap. DH breaks the multiplicativity of c_N (R-Z1).

**First lemma (Lemma Z.2, OPEN, precise statement).** For N ≥ μ, c_N = −Σ_{m<μ, m|N} μ(m)·(truncation term) is the
truncated Möbius tail of lem:ext-mob. *Prove or disprove:* there exists an absolute C such that

 |Σ_{μ≤N≤X} c_N c_{kN}| ≤ C·(Σ_{μ≤N≤X} c_N²)·k^{−1/2}·μ^{−δ} for all k ≥ 2 and some δ > 0,

that is, that **the quotient blocks k ≥ 2 are small compared to the diagonal k = 1** at a polynomial scale in μ. If
Z.2 holds, (3.2) reduces to the diagonal Σ_N c_N²N^{−1}𝒲[g], whose sign is that of 𝒲[g] = W_T(g) on the window
datum, and that is a bound of a_T ≥ 0 type on the window. Note: this reduction could be circular (REF-D). That is why
Z.2 is formulated as a *structural* lemma about c_N, without a sign. If Z.2 is false (order-1 multiplicative
correlation of truncated Möbius, as C6 suggests in K1_OSG), the falsifier is explicit: the k* that maximizes the
correlation.

**Honest duplicate warning.** K1_OSG_001 already computed the reflected contribution as Σ(c∗c)(P)P^{−½}G(log(μn/P)),
"Möbius correlation (C6), comb-generic". The difference with (3.1) is that there the convolution is (c∗c)(P), of
product type (R-K1), and here it is Σ_N c_N c_{kN}, of quotient type. Whether it is comb-generic or not depends on
whether c_N, as a function of N, sees the lattice ℤ or only the multiplicative structure. If it sees only the
multiplicative structure (ARGUED probable: c_N depends on the divisors m < μ of N), Beurling reproduces it with μ_𝒫
and the candidate dies by P10. This is decided by Lemma Z.2′: **does c_N depend on N only through {m < μ : m | N}?**
If yes, (iv) is comb-generic (NO-GO) and Λ remains confined to (β), Guo L4.4.

## 4. Test μ = 15 (without computing)

Data from MORI15_EXTREMAL_001: d = 832 Legendre modes per parity; J = g*(T) = −1.42·10⁻³⁴; W* ≈ J²Σ_{γ>0}|ρ|^{−2} =
4.66·10⁻⁷⁰ (l.198, matches Q within 2%, NUMERICAL); pairs of translates (22,44), (26,52), (33,66), (39,78) (K1_OSG).

What is compared:
1. **AFE scale.** By (2.1), the transition n ≈ uw must fall at N ≈ 15. Comparison: the active quotients of K1_OSG are
   k = 2 with N ∈ [22,39]. If (2.1) is correct, the pairs that weigh in W* are just above the transition. Datum to
   extract: the distribution in N of the contribution to W* (not published in MORI15; requires the vector g* in the
   basis of translates).
2. **Lemma Z.2.** The ratio R₂ = |Σ_N c_N c_{2N}| / Σ_N c_N² with the truncation c_N at μ = 15. Prediction of Z.2:
   R₂ ≲ 15^{−δ}·2^{−½} ≈ 0.7·15^{−δ}. Compare it with off/diag = 0.72 of MM_001 (NUMERICAL μ = 15). If R₂ ≈ 0.7, Z.2
   fails at μ = 15 with no margin, and the k = 2 block is of the same order as the diagonal (consistent with MM_001,
   unfavorable).
3. **Tate mode.** W* ∝ Σ1/(ρ(1−ρ)) is the boundary eigenform (PI4 §5). Candidate (iv) does not explain it: the
   boundary mode is polar, not a quotient block. If W* is dominated by the Tate mode (J²·0.0231), the quotient part
   of the extremal is subdominant and test 2 is decisive.

None of this is executed here (rule: numerical only if strictly necessary). Test 2 is cheap (only c_N) and decides
Z.2 at μ = 15.

## 5. Final

### Labels

| item | label |
|---|---|
| Prop Z.1 (symbol ζ, −ζ′ after subtracting the polar mode) | PROVED / CITED (Müntz) |
| origin of unboundedness: pole s=1 (B1_FLAT) + |ζ(½+it)| (high frequency) | PROVED (descriptive) |
| (1.4) Q as cross form [𝒫, θ′] + [𝒫, iZ′/Z] | PROVED; recapitulates A_001, C_001, Q_001 |
| "inequality between ∫|r̃|²|ζ|²w and ∫|r̃|²Re ζζ̄′w" | ill-posed (weight ⇒ null symbol) |
| (2.1) AFE point n ≈ u·w ≈ μ in the aliasing regime | ARGUED (stationary phase) |
| (i) AFE as identity | duplicate (FF_001, S-dual, EI_003) |
| (i′) AFE with dependent cutoff as inequality | **NO-GO ARGUED** (DH + R-K1) |
| (ii) Ingham/Estermann | duplicate (EI_002, J.3, AUDIT_16) |
| (iii) Re ζ′/ζ | duplicate |
| R-Z1 | ARGUED (new) |
| (iv) quotient blocks 𝔅_k; (3.2) | OPEN; (3.2) REF-D as a statement |
| Lemma Z.2, Z.2′ | OPEN |
| L′♯ / row D | OPEN |

### New restriction

**R-Z1 (ARGUED):** every proposal that uses Z only via its symbol on Re s = ½ (multiplier, FE, AFE, RS, moments) is
DH-transportable. Separating DH requires the Euler product, which in 𝒦₁ appears only in (α) Re s > 1 (TV-robust),
(β) Guo L4.4 or (γ) the Möbius gap c_N = 0 (2 ≤ N < μ). Corollary: site (a) of AUDIT_PIMU, *without* (β) or (γ), does
not separate DH.

### Entry for the index

- **Z_CARRIER_001 (phase 200, round 6):** Z on 𝒦₁ = multiplier ζ(s) on Re s = ½ after subtracting the polar mode
  (Müntz, PROVED), Z_log ↔ −ζ′; (★★) = cross form of commutators [𝒫, θ′], [𝒫, iZ′/Z] (recapitulates A/C/Q_001). AFE
  point in the aliasing regime n ≈ u·w ≈ μ (ARGUED): coincides with the gap of FF_001. **NO-GO (ARGUED): AFE with
  frequency-dependent cutoff (residue of LL_001)**: the direct block is comb-generic, the cross block is of product
  type (R-K1) and everything is DH-transportable. Ingham/Estermann and Re ζ′/ζ are duplicates. **R-Z1:** the symbol
  of Z does not separate DH; the Euler product only enters via (α)/(β)/(γ). Residue OPEN: quotient blocks
  𝔅_k = Σ c_N c_{kN}, Lemmas Z.2/Z.2′. Not to retry: AFE (smooth, Riemann–Siegel or with dependent cutoff) as a
  source of sign on 𝒦₁. No sign. Row D OPEN.

### Next lemma

**Lemma Z.2′ (decisive, purely combinatorial, OPEN):** determine whether the truncation coefficients c_N of
lem:ext-mob (N ≥ μ) depend on N only through the set of divisors {m < μ : m | N}.
- If **yes**: candidate (iv) is Beurling-generic (NO-GO by P10), and the exact Λ remains confined to Guo L4.4
  (site (b)). Round 7 must attack (b).
- If **no** (c_N sees the additive lattice, for example via the smooth cutoff of f in the window): Lemma Z.2 and
  test 2 of §4.
