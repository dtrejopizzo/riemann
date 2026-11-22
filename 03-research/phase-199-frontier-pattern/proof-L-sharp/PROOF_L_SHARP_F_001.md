# PROOF_L_SHARP_F_001 — Strategy F: interference between ratio classes, written on the critical line through the partial sums of ζ

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯** in the consolidated form (★★) of
AUDIT_L_SHARP_1 §6.3, with the seven constraints of §6.3 as the admissibility test of every step.
Notation of memos A/E and of the audit: λ = e^T, μ = λ², a = T; f admissible real with f(λ) = 0;
r = f̂·1_{|ξ|>λ}; r̃(x) = e^{x/2}r(e^x); Ψ̌(x) = (Zr)(e^x) = e^{x/2}Σ_{n≥1}r(ne^x) for x > a, 0 for x ≤ a;
Θ_∞(τ) = Re ψ(¼+iτ/2) − log π; ν(t) = e^{−|t|/2}/(1−e^{−2|t|}); ζ_X(w) := Σ_{n≤X}n^{−w}; H(X) = Σ_{j≤X}1/j.

**Outcome in one line.** L′♯ is NOT proved. What is proved: (F.0) (★★) is a statement about ONE fixed quadratic
form 𝔔 on L²(1,∞), independent of μ, tested on the increasing Paley–Wiener family PW_μ modulo the fixed radical
PW_1: all the μ-dependence of L′♯ sits in the data class; (F.1) on the critical line the exterior form is a
quadratic form in the *partial sums* ζ_X(1−s), X = ξ/λ, with the archimedean symbol Θ_∞ = −2Re(ζ′/ζ)(½+iτ)
(a Γ-identity, no zero data); (F.2) the Euler–Maclaurin/Poisson split of ζ_X(1−s) = ζ(1−s) + X^s/s + e_s(X)
resolves the obstacle recorded in memo E §7 ("no exact identity for the smooth part of the harmonic cut was found"):
the smooth part is a **null vector of the form, pointwise on the line**, and the exterior form is exactly
2Q(F₀,G) + Q(G), with G the Euler–Maclaurin defect (residue term + sawtooth); the sawtooth e_s(X) =
−Σ_{k≠0}∫_X^∞e^{2πikt}t^{s−1}dt is the ℤ-specific object (counting function ⌊X⌋ = X − {X}, i.e. a_n ≡ 1 with
O(1) error), absent for Beurling systems; (F.3) the archimedean coupling of two out-of-band frequencies ξ, η through
the dilates (m,n) is the **Hilbert-type kernel max(nξ,mη)/|n²ξ²−m²η²|**, singular on the rational lines
ξ/η = α/β, and the prime part is a *singular measure on the same rational lines*; the two-class system of the brief
is written exactly in these terms; (F.4) on deep data the ratio classes are of size D² each while the total is
O(1): the brief's hypothesis "(1,1) carries the pole that cancels its own growth" is FALSE class-wise and TRUE
only for the total (Lemma E.4), so the ratio-class decomposition is the wrong organisation of the sign and the
Euler–Maclaurin split is the right one; (F.5) on shallow data (depth ≤ e^{1.6}) the exterior form is the window
form at T ≤ 0.8 and is nonnegative (CITED Zhu). The remaining inequality is (★★_u) of §6, OPEN. Every proved step
is tested against cΛ, a_P, Beurling and F-DH in §7; none is decisive (N_018), and the table says which
ingredient of the split each falsifier removes.

## 0. Corpus check (rule ) and why this is not a retry
- **Index read:** README l.52 (N_018), l.390 (INV_C_001 Farey/Möbius of h⁰), l.396 (INV_H_001: additive identities
  of Λ used linearly, incl. Euler–Maclaurin, NO-GO class 𝓒_H), l.398 (INV_K_001: ζ(½+iτ) universal carrier of
  window symbols), l.415 (INV_V_002), l.446 (connection layer: the only built-in positivity at weight n^{−1/2} is the
  multiplicative Hilbert matrix, Helson/Perfekt, no FE), l.450–456 (MECH_001, memos A–E), 04_PHASES l.16 (W4:
  unconditional positivities incl. sawtooth are lower bounds, wrong direction), l.823/830 (R162_1902: B₂/sawtooth
  on the window, value linear in c, both signs, DEAD), l.973 (R170_885: Euler–Maclaurin port / Fredholm range on
  the window, exact identity without sign, DEAD), 05b l.39 (L87 Perfekt: multiplicative Hilbert matrix
  1/(√(mn)log(mn)) bounded, falsifier-first only).
- **Sources read:** AUDIT_L_SHARP_1 (all of §1–6), memo E (E.1–E.5, §7), memo A (Thm 1.1, Prop 2.1, §3.2, Rem 3.3),
  Paper 46 (sec:cert, the remark citing Zhu Thm 1.2 for T ≤ 0.8, prop:archneg).
- **Why not a retry.** (a) R170_885 and R162_1902 used Euler–Maclaurin / the sawtooth *on the window carrier*, as
  a linear functional in c or as a Fredholm-range condition; here the sawtooth is the Euler–Maclaurin remainder of
  the *partial sums ζ_X(1−s) inside the exterior quadratic form*, where (Thm F.2) its complement is a pointwise null
  vector — an object the index does not record. (b) INV_H_001's class 𝓒_H is "additive identities of Λ used
  linearly"; nothing here is linear in Λ: after E.2 the form has no Λ, and the split is of the summation map, not
  of the comb. (c) Perfekt's matrix (L87) is *not* used; §4 shows the kernel that actually occurs is the archimedean
  Hilbert-type kernel max(nξ,mη)/|n²ξ²−m²η²|, and §4.3 records why the Hilbert-inequality route of the brief does
  not give the sign (the sign is not a bound of one class by another). (d) No sign is claimed; by N_018 every
  identity below is non-decisive and §7 says so for each.

## 1. The universal form: (★★) is one fixed form on L²(1,∞) tested on PW_μ (PROVED)

**Proposition F.0.** Put ρ(X) := λ r(λX) for X > 1 and g(t) := f(t/λ), so that g is even, C², supported in
[−μ,μ], g(0) = ĝ(0) = g(μ) = 0, and ρ = ĝ|_{(1,∞)}. Then
  𝒲_ext[Zr] = λ^{−1}·𝔔[ρ],   dist²_{L²(λ,∞)}(r,𝒢̄) = λ^{−1}·dist²_{L²(1,∞)}(ρ, 𝒢̄₁),
where 𝔔 is the quadratic form on L²(1,∞) given by 𝔔[ρ] = 𝒲[Ψ̌_ρ], Ψ̌_ρ(y) := e^{y/2}Σ_{n≥1}ρ(ne^y) for y > 0,
0 for y ≤ 0 (the exterior form at a = 0), and 𝒢̄₁ := closure{φ̂|_{(1,∞)} : φ even C², supp φ ⊂ [−1,1],
φ(0) = φ̂(0) = 0}. Neither 𝔔 nor 𝒢̄₁ depends on μ. Consequently L′♯ ⟺
  **(★★_u)**  𝔔[ρ] ≥ κμ^{−A}·dist²(ρ,𝒢̄₁)  for all μ ≥ 5 and all ρ ∈ PW_μ := {ĝ|_{(1,∞)} : g as above},
and PW_1 ⊂ 𝒢̄₁ ⊂ ker 𝔔 (PW_1 with the three constraints is the radical, memo A Prop 2.1).
*Proof.* Ψ̌(a+y) = e^{(a+y)/2}Σ_n r(ne^{a+y}) = λ^{1/2}e^{y/2}Σ_n λ^{−1}ρ(ne^y) = λ^{−1/2}Ψ̌_ρ(y), and 𝒲 is translation
invariant (every piece of K_W is a convolution kernel, memo E §1), so 𝒲[Ψ̌] = λ^{−1}𝒲[Ψ̌_ρ]. ‖ρ‖² = λ‖r‖², and the
gauge rescales to 𝒢̄₁ (supp φ ⊂ [−1/λ,1/λ] ↦ [−1,1]); ĝ(X) = λf̂(λX) ✓. □

**Reading.** The whole μ-dependence of L′♯ is in the *data*: ρ is the out-of-band restriction (X > 1) of an
entire function of exponential type μ, modulo those of type 1. As μ → ∞ the family PW_μ|_{(1,∞)} is dense in
L²(1,∞), and memo E §5 shows 𝔔 ≥ 0 on all of L²(1,∞) is row D on every window; (★★_u) with κμ^{−A} → 0 is the
quantitative version of that limit, which is why only polynomial loss is required (audit §4.3(b)). Everything
below is written for 𝔔 (λ = 1, a = 0); the general case is Prop F.0.

## 2. The critical-line formulation through partial sums (PROVED)

**Theorem F.1.** For ρ ∈ L²(1,∞) with ρ = O(X^{−2}) and s = ½+iτ put
  F(s) := ∫_1^∞ ρ(X)X^{−s}ζ_X(1−s)dX,   F_log(s) := ∫_1^∞ ρ(X)X^{−s}(Σ_{n≤X}n^{s−1}log n)dX = −∫_1^∞ρ(X)X^{−s}ζ_X′(1−s)dX.
Then F = FΨ̌_ρ and F_log = F(Ψ̌_ρ)_log (Fourier transforms on the line), both in L²(dτ), and
  (F.1)  𝔔[ρ] = (1/2π)∫_ℝ[Θ_∞(τ)|F(s)|² − 2Re(\overline{F(s)}F_log(s))]dτ + 2AB,
  A = ∫_1^∞ρ(X)⌊X⌋X^{−1}dX,  B = ∫_1^∞ρ(X)H(X)dX,
and, on the line, Θ_∞(τ) = −2Re(ζ′/ζ)(½+iτ) wherever ζ(½+iτ) ≠ 0 (and Re(ζ′/ζ) extends continuously there).
*Proof.* ∫_0^∞Ψ̌_ρ(y)e^{−(s−½)y}dy = Σ_n∫_0^∞ρ(ne^y)e^{(1−s)y}dy = Σ_n n^{s−1}∫_n^∞ρ(X)X^{−s}dX =
∫_1^∞ρ(X)X^{−s}Σ_{n≤X}n^{s−1}dX (absolute convergence: Σ_n n^{−1/2}·n^{−3/2}); the same with log n gives F_log.
(F.1) is Cor E.3 in Plancherel form; A = F(1), B = F(0) (s = 1: Σ_n n^0∫_n^∞ρX^{−1} = ∫ρX^{−1}⌊X⌋; s = 0:
Σ_n n^{−1}∫_n^∞ρ = ∫ρH). The symbol identity: from ξ(s) = ξ(1−s), (ζ′/ζ)(s) + (Γ_ℝ′/Γ_ℝ)(s) + 1/s + 1/(s−1) =
−[same at 1−s]; on the line 1−s = s̄, so 2Re(ζ′/ζ)(s) = −2Re(Γ_ℝ′/Γ_ℝ)(s) − 2Re(1/s + 1/(s−1)), and
Re(1/s) + Re(1/(s−1)) = ½/(¼+τ²) − ½/(¼+τ²) = 0, while 2Re(Γ_ℝ′/Γ_ℝ)(½+iτ) = Re ψ(¼+iτ/2) − log π = Θ_∞(τ)
(memo A Rem 3.3 with the pole terms made explicit). □

**Remark 2.1 (what is and is not used).** Only Re(ζ′/ζ) on the line enters (F.1) through Θ_∞; it is a Γ-function.
Im(ζ′/ζ)(½+iτ), which carries the zeros, never appears. The on-line values ζ(½+iτ), ζ′(½+iτ) appear in §3 only
through the pointwise identity of Thm F.2(ii), never through bounds. No zero data, no prime data.

**Remark 2.2 (Mellin form of the ratio classes).** X^{−s}ζ_X(1−s) = Σ_{n≤X}n^{−1}(n/X)^s: the "+ meets ·" cut of
memo E (E.1b) is, on the line, the single-variable partial sum Σ_{n≤X}n^{−1}e^{iτlog(n/X)}; the two-variable cut
H(min(ξ/αλ, η/βλ)) of (E.1b) is the *product* of two one-variable cuts seen through |F|². This is why the
smooth/sawtooth split can be made exactly here and could not be made in memo E §7.

## 3. The Euler–Maclaurin–Poisson split and the pointwise null vector (PROVED)

**Lemma 3.1 (Euler–Maclaurin for partial sums; classical, CITED Titchmarsh §§3.5, 4.2).** For Re w > 0, w ≠ 1, X ≥ 1:
  ζ_X(w) = ζ(w) + X^{1−w}/(1−w) + e_w(X),  e_w(X) := −{X}X^{−w} + w∫_X^∞{t}t^{−w−1}dt = −Σ_{k≠0}∫_X^∞e^{2πikt}t^{−w}dt,
the last sum conditionally convergent, |e_w(X)| ≤ (1 + |w|/Re w)X^{−Re w}. With w = 1−s, s = ½+iτ:
ζ_X(1−s) = ζ(1−s) + X^s/s + e_s(X), e_s(X) := e_{1−s}(X) = O((1+|τ|)X^{−1/2}).

**Theorem F.2 (the split).** Write, on the line s = ½+iτ, F = F₀ + F₁ + F₂ and F_log = F₀^{log} + F₁^{log} + F₂^{log} with
  F₀(s) = ζ(1−s)R(s), R(s) := ∫_1^∞ρ(X)X^{−s}dX = (Fρ̃)(τ);   F₀^{log}(s) = −ζ′(1−s)R(s);
  F₁(s) = ρ₀/s,  ρ₀ := ∫_1^∞ρ;   F₁^{log}(s) = ρ₁/s − ρ₀/s²,  ρ₁ := ∫_1^∞ρ(X)log X dX;
  F₂(s) = ∫_1^∞ρ(X)X^{−s}e_s(X)dX;   F₂^{log}(s) = ∫_1^∞ρ(X)X^{−s}∂_s e_s(X)dX.
Let Q(F,F_log) := (1/2π)∫[Θ_∞|F|² − 2Re(F̄F_log)]dτ be the symbol part of (F.1), polarised as a symmetric bilinear
form in the pair (F,F_log) (each pair is a linear function of ρ). Then:
(i) all six functions are in L²(dτ) (F₁, F₁^{log} explicitly; F₀ because |ζ(½−iτ)|² = O(|τ|^{1/2+ε}) and
  |R(½+iτ)|² = O(τ^{−2}) by the jump of ρ at X = 1 and ρ ∈ C¹(1,∞); F₂ = F − F₀ − F₁; log versions likewise);
(ii) **Q(F₀,F₀) = 0, pointwise on the line:** Θ_∞|F₀|² − 2Re(\overline{F₀}F₀^{log}) = |R|²|ζ(1−s)|²[Θ_∞ + 2Re(ζ′/ζ)(1−s)] = 0
  for every τ with ζ(½+iτ) ≠ 0, since Re(ζ′/ζ)(1−s) = Re(ζ′/ζ)(s̄) = Re(ζ′/ζ)(s) = −½Θ_∞ (Thm F.1);
(iii) F₀ + F₁ is regular at s = 0 (ζ(1−s) + X^s/s = log X + γ + O(s)), and F₁ is the Mellin transform of ρ₀e^{−y/2}1_{y>0};
(iv) hence, with G := F₁ + F₂ (and G^{log} likewise),
  **(F.2)  𝔔[ρ] = 2Q(F₀,G) + Q(G,G) + 2AB,**
  2Q(F₀,G) = −(1/π)∫Re[ \overline{R(s)}·( χ(s)ζ′(1−s)G(s) + ζ(s)G^{log}(s) ) ]dτ,  χ(s) := ζ(s)/ζ(1−s) = π^{s−½}Γ((1−s)/2)/Γ(s/2),
  Q(G,G) = −(1/π)∫Re[ \overline{G}( Re(ζ′/ζ)(s)·G + G^{log} ) ]dτ.
*Proof.* (i)–(iii) as stated; (ii) is the computation displayed. For (iv): Θ_∞\overline{F₀} − \overline{F₀^{log}} =
\overline{R}[Θ_∞ζ(s) + ζ′(s)] (on the line \overline{ζ(1−s)} = ζ(s), \overline{ζ′(1−s)} = ζ′(s)) = \overline{R}ζ(s)[Θ_∞ + (ζ′/ζ)(s)]
= −\overline{R}ζ(s)\overline{(ζ′/ζ)(s)} = −\overline{R}χ(s)ζ′(1−s), using Θ_∞ = −(ζ′/ζ)(s) − \overline{(ζ′/ζ)(s)} and
ζ(s)/\overline{ζ(s)} = ζ(s)/ζ(1−s) = χ(s); χ is entire on the line and unimodular, so the expression is regular at
the zeros of ζ on the line. □

**Corollary 3.2 (the obstruction is in the cross term; PROVED, elementary).** A real quadratic form on a pair of
vectors (u,v) of the shape 2C(u,v) + D(v,v) with no (u,u)-term is nonnegative on a product set U × V only if the
cross form C vanishes on it. Hence no proof of (★★_u) can treat the full-line vector F₀(ρ) and the defect G(ρ) as
independent variables: the entire sign is carried by the *coupling* ρ ↦ (R(s), ρ₀, ρ₁, F₂(ρ)) imposed by the
Paley–Wiener class. This sharpens audit constraint 5 ("lattice aliasing is the whole additive input"): the
additive input is used *exactly* at the point where F₀ and G are linked through the same ρ.

**Remark 3.3 (the ℤ-specific piece, by inspection of Lemma 3.1).** The three pieces of the split are, for a
general Dirichlet series D(s) = Σa_n n^{−s} with summatory function N_D(X) = Σ_{n≤X}a_n:
F₀^D = D(1−s)R, F₁^D = (res_{s=1}D)·ρ₀/s, and F₂^D = ∫ρ(X)X^{−s}e^D_s(X)dX with e^D_s(X) := −∫_X^∞t^{s−1}d(N_D(t) − (res)·t)
(Stieltjes, after the same integration by parts as in Lemma 3.1): the remainder is driven by N_D(t) − (res)·t. For ℕ: N(t) − t = −{t} = O(1), and F₂ is the Poisson dual
(Lemma 3.1, last equality) — the lattice aliasing seen on the Mellin side. For a Beurling system with
N_B(t) = ct + O(t^θ), θ > 0, the remainder is of size X^{θ−1/2} instead of X^{−1/2}: not a sawtooth and not a Poisson
dual. For cΛ (a_n = d_c(n)) N_D(t) = t·P_c(log t) + O(t^{θ_c}) (P_c a polynomial of degree c−1 for integer c): the
main term is not X^s/s and F₁ is not rank one. For a_P (P-free integers): N_P(t) = ct + O(1), periodic remainder,
residue c < 1. For F-DH (conductor 5, residue 0): N_χ(t) = O(1), no F₁, no 2AB. See §7.

## 4. The Hilbert-type kernel and the two-class system (PROVED)

**Theorem F.3 (archimedean coupling of out-of-band frequencies through the dilates).** Let Φ_m(y) := e^{y/2}ρ(me^y)
for y > 0 (so Ψ̌_ρ = Σ_m Φ_m and Φ_m is supported where X = me^y > m). For m ≠ n and ξ = me^y, η = ne^{y′} with
nξ ≠ mη,
  Φ_m(y)Φ_n(y′)ν(y−y′)dy dy′ = ρ(ξ)ρ(η)·k_{mn}(ξ,η)dξdη,  **k_{mn}(ξ,η) := max(nξ,mη)/|n²ξ²−m²η²|** = (1/|nξ−mη|)·max(nξ,mη)/(nξ+mη).
Hence the regular (off-diagonal) part of the Lévy energy of Ψ̌_ρ is −∫∫ρ(ξ)ρ(η)𝒦(ξ,η)dξdη with
  𝒦(ξ,η) = Σ_{m,n≥1} 1[ξ>m, η>n]·k_{mn}(ξ,η) = Σ_{(α,β)=1} H(min(ξ/α, η/β))·max(βξ,αη)/|β²ξ²−α²η²|,
and the prime part is the singular measure on the rational lines η = βξ/α:
  −2⟨Ψ̌_ρ,(Ψ̌_ρ)_log⟩ = −Σ_{m,n}log(mn)∫_1^∞ρ(mU)ρ(nU)dU = −Σ_{(α,β)=1}α^{−1}∫_{X>α}ρ(X)ρ(βX/α)G_{αβ}(X/α)dX,
G_{αβ}(X) = Σ_{j≤X}(2log j + log αβ)/j (memo E, E.2).
*Proof.* y−y′ = log(nξ/(mη)); for nξ > mη, ν(y−y′) = (mη/nξ)^{1/2}(nξ)²/((nξ)²−(mη)²); Φ_m(y)dy = m^{−1/2}ξ^{−1/2}ρ(ξ)dξ,
Φ_n(y′)dy′ = n^{−1/2}η^{−1/2}ρ(η)dη; the product of the three factors is nξ/((nξ)²−(mη)²)ρρdξdη. The pair (m,n) =
(jα,jβ) gives k_{mn} = j^{−1}max(βξ,αη)/|β²ξ²−α²η²| and the indicator j ≤ min(ξ/α,η/β), whence H(min). The prime
part: ∫_0^∞Φ_mΦ_n dy = ∫_1^∞ρ(mU)ρ(nU)dU with U = e^y. □

**Reading (the semiring object, exactly).** The archimedean energy couples ξ and η through *every* pair of
dilates (m,n), with the Hilbert kernel 1/|nξ−mη| (up to the bounded factor max/(sum) ∈ [½,1]): it is singular
precisely at the near-coincidences nξ ≈ mη, i.e. ξ/η ≈ α/β rational — the "m ≈ kn" of the semiring principle — with
the harmonic weight H(min(ξ/α,η/β)) counting the common multipliers up to the window edge. The prime part lives
*on* those rational lines, as a negative measure with density G_{αβ}(X/α)/α ~ log²(X/α). The Lévy regularisation
(the diagonal b_∞ and the subtraction in ½∫∫|Φ−Φ|²ν) is what makes the logarithmically divergent mass of 1/|nξ−mη|
along each rational line finite: in Mellin terms it is the finiteness of Θ_∞. So (★★_u) reads: *the renormalised
Hilbert mass of the archimedean kernel on the rational lines, cut harmonically, dominates the log²-weighted prime
measure on the same lines, after the pole has removed the residue term, uniformly over PW_μ up to μ^{−A}.*

**4.2 The two-class system (PROVED bookkeeping).** With 𝔔 = Σ_{(α,β)=1}(αβ)^{−1/2}Q_{α/β} as in memo E Thm E.5:
- Class (1,1): Q_{1/1}(ρ) = Σ_j j^{−1}[𝒜(Φ^{(j)}) + 2A(Φ^{(j)})B(Φ^{(j)})] − 2∫_1^∞ρ(X)²H₁(X)dX, Φ^{(j)} := ρ̃·1_{(log j,∞)},
  H₁(X) = Σ_{j≤X}(log j)/j = ½log²X + γ₁ + O(X^{−1}log X). Its archimedean kernel is the diagonal m = n of Thm F.3:
  H(min(ξ,η))·max(ξ,η)/|ξ²−η²| — the Hilbert kernel 1/|ξ−η| on the diagonal line, harmonically cut.
- Generic class (α,β), α ≠ β: archimedean kernel H(min(ξ/α,η/β))·max(βξ,αη)/|β²ξ²−α²η²|, singular on η = βξ/α;
  prime measure −α^{−1}G_{αβ}(X/α)δ(η−βX/α); pole part 2Σ_j j^{−1}(αβ)^{−1/2}A(Φ_{jα})B(Φ_{jβ})-type cross terms.
- Cross terms between classes: none at the level of the kernel — the classes are *disjoint pieces of one kernel*
  𝒦 (resp. one singular measure), indexed by the rational slope. "Interference" between classes therefore means:
  the data ρ(ξ)ρ(η) is evaluated simultaneously on all rational lines through (ξ,η), and the sign of
  ∫∫ρρ d(𝒦 − prime measure) is a property of ρ against the *union* of the lines, not of any one line.

**4.3 Why the Hilbert-inequality route of the brief does not give the sign (ARGUED, recorded to avoid a retry).**
Hilbert-type inequalities (Hilbert, Hardy–Littlewood–Pólya, Montgomery–Vaughan) bound |Σ a_m\bar a_n/(m−n)| or
∫∫|ρ(ξ)ρ(η)|/|ξ−η| from *above* by a multiple of ‖ρ‖² (the Hilbert kernel is bounded, not coercive); Perfekt's
bounded multiplicative Hilbert matrix is likewise an upper bound. (★★_u) asks for a *lower* bound of the
archimedean mass against the prime measure. The only coercive archimedean object is the Lévy energy itself
(Θ_∞ ~ log|τ| at high frequency), and a lower bound of it by ‖·‖² plus an upper bound of the prime part is the
Bochner + C–S class, excluded by audit §6.3 item 4 (A §5) and by N_018. So Hilbert inequalities can at most
control cross-class *remainders* (the bounded factor max/(sum), the sawtooth of H), never the sign.

## 5. Deep and shallow data: where the sign is decided (PROVED / CITED)

**Proposition F.4 (deep data: the classes are the wrong organisation).** Let ρ̃ = φ(·−D) with φ ≥ 0 a fixed unit
bump supported in (0,1) (C_c^∞ data, not Paley–Wiener), D large, and put ρ₀ = ∫ρ = e^{D/2}B(φ) with B(φ) = ∫e^{v/2}φ.
Then, as D → ∞:
(i) Ψ̌_ρ(y) = ρ₀e^{−y/2}(1 + O(e^{−(D−y)})) uniformly on 0 < y < D − C, and Ψ̌_ρ = 0 for y > D + 1
    (Euler–Maclaurin main term: Σ_m m^{−1/2}φ(y+log m−D) ≈ ∫m^{−1/2}φ(y+log m−D)dm = e^{(D−y)/2}B(φ));
(ii) 2AB = 2ρ₀²D + O(ρ₀²), −2⟨Ψ̌_ρ,(Ψ̌_ρ)_log⟩ = −2ρ₀²D + O(ρ₀²), 𝒜[Ψ̌_ρ] = O(ρ₀²), so **𝔔[ρ] = O(ρ₀²) = O(e^D)**,
    with the O(1) constant determined by the transition region y ∈ (D − C, D + 1) (where Σ_m has O(e^C) terms);
(iii) the class (1,1) alone is −D²·e^{D}·c + O(D e^D) (memo E Thm E.5), and every class (α,β) with log(αβ) ≪ D is
    of the same order −log²(·)·e^D; the cross-class sum of the log² terms cancels to O(e^D).
*Proof.* (i) as displayed, with the Riemann-sum error of a C^∞ bump at step 1/m. (ii) A = ∫_0^∞Ψ̌e^{−y/2} = ρ₀(1+O(e^{−D})),
B = ∫Ψ̌e^{y/2} = ρ₀D + O(ρ₀); (Ψ̌_ρ)_log(y) = Σ_m m^{−1/2}log m·φ(y+log m−D) = e^{(D−y)/2}[(D−y)B(φ) + B₁(φ)] + O(·),
B₁ = ∫ve^{v/2}φ, so ⟨Ψ̌,Ψ̌_log⟩ = ρ₀²∫_0^{D}(D−y)e^{−y}dy + O(ρ₀²) = ρ₀²D + O(ρ₀²); the archimedean form of
ρ₀e^{−y/2}1_{(0,D)} plus a bounded transition is O(ρ₀²) (one jump of size ρ₀ at 0, Lévy energy of a jump finite
with ν, audit §1.2). (iii) is Thm E.5 with ‖φ‖² replaced by the e^D-normalisation. □

**Consequences.** (a) The brief's mechanism (ii) — "the (1,1) class carries exactly the pole 2AB that cancels its
log X growth, leaving a bounded remainder" — is FALSE class-wise: on the (1,1) class the pole contributes O(D·e^D)
and the prime part −D²e^D; the pole cancels the prime main term only for the *total* (Lemma E.4), and the D²
terms cancel only *across* classes. (b) The Euler–Maclaurin split is the organisation in which the cancellation
is manifest: on deep data F₁ (residue term) and 2AB are the two O(D)-objects, they cancel by E.4, and the
O(1) remainder is the transition region = the sawtooth F₂ evaluated where few dilates contribute (X/m = O(1)):
the small integers m,n at the edge of the data, i.e. the near-coincidences nξ ≈ mη with m,n = O(e^C). This is
the exact location of the "m ≈ kn" interaction: not "near the window edge X ≈ 1" but *near the edge of the
support of the data in units of the mesh*. (c) For Paley–Wiener data ρ = ĝ|_{(1,∞)}, ρ decays like X^{−2} and
oscillates at scale 1/μ, so there is no single depth: every depth D ≤ log μ carries mass ≍ e^{−D}·(…), and the
transition regions of all depths are superposed. The ratio-class decomposition of memo E is therefore the
Fourier-dual bookkeeping of the same sawtooth; its "cross-class interference" is Thm F.2's cross term 2Q(F₀,G).

**Proposition F.5 (shallow data = window form; PROVED reduction, positivity CITED).** If ρ is supported in
(1,X₀], then Ψ̌_ρ is supported in (0, log X₀] and 𝔔[ρ] = W_{T₀}(Ψ̌_ρ(·+½log X₀)) with T₀ = ½log X₀ (the complete
window form of Paper 46 with comb q < μ₀ = X₀; the pairs with log q ≥ log X₀ do not pair within the support).
Hence, for X₀ ≤ e^{1.6}: 𝔔[ρ] ≥ λ^W_{T₀}‖Ψ̌_ρ‖² ≥ 0 (Zhu, Thm 1.2, CITED: the complete form is positive for
T ≤ 0.8; Paper 46 thm:log5A/W give T ≤ ½log 5 unconditionally). Such ρ are not in PW_μ; the statement is a
positivity of the exterior form on compactly supported data of depth ≤ 4.95, nothing more. It fixes the scale:
*the depth of the data on the exterior carrier is the window half-length*, so the exterior carrier does not escape
the window problem — what it adds is the Paley–Wiener constraint (Cor 3.2) and the quotient by the radical.

## 6. The remaining inequality (OPEN), in the form produced here

By Prop F.0, Thm F.1 and Thm F.2, L′♯ is equivalent to each of the following, with the same (κ,A):
  (★★_u)   𝔔[ρ] ≥ κμ^{−A}dist²(ρ,𝒢̄₁)   ∀μ ≥ 5, ∀ρ ∈ PW_μ;
  (★★_EM)  2Q(F₀(ρ),G(ρ)) + Q(G(ρ),G(ρ)) + 2A(ρ)B(ρ) ≥ κμ^{−A}dist²(ρ,𝒢̄₁),
with F₀ = ζ(1−s)·(Fρ̃), G = ρ₀/s + ∫ρ(X)X^{−s}e_s(X)dX, e_s the sawtooth of Lemma 3.1, A = ∫ρ⌊X⌋/X, B = ∫ρH, and the
two bilinear forms displayed in Thm F.2(iv). The inequality contains no prime, no Λ, no zero: its ingredients are
ζ, ζ′, χ on the critical line (through the pointwise identities of §3 only), the Γ-symbol Θ_∞, the sawtooth {X},
the harmonic numbers H(X) and ⌊X⌋, and the Paley–Wiener class. It is OPEN.

**On the request "a single inequality on finitely many parameters".** Not achieved honestly. (★★_EM) is a
statement on the infinite-dimensional PW_μ/𝒢̄₁; the only finite truncations available are the prolate blocks of
memo A §3.4, whose dimension is superpolynomial (A §4.4). What *is* finite-parameter is a necessary condition:
by Prop F.4 the deep-bump family (shape φ, depth D → ∞) gives 𝔔 = e^D·(c(φ) + o(1)) with c(φ) an explicit
functional of the transition region; c(φ) ≥ 0 for every bump is necessary for 𝔔 ≥ 0 on C_c^∞ data, which is row D
on all windows (E §5), not (★★_u). I did not compute c(φ) in closed form; it is the Weil form of the Euler–Maclaurin
transition of a single bump and is recorded as a test object, not as a route.

## 7. Falsifier table (constraint (iii) of the brief; audit items 2 and 5)

| step | cΛ (E_c, a_n = d_c(n)) | a_P (P-free integers) | Beurling B | F-DH (cond. 5, no pole) | verdict |
|---|---|---|---|---|---|
| Prop F.0 universal scaling | YES | YES | YES | YES | generic (dilation invariance) |
| Thm F.1 partial-sum form, Θ_∞ = −2Re(ζ′/ζ) | YES with D_X, Θ_D = −2Re(D′/D) | YES | YES (if FE) | YES with Θ_{χ}, conductor 5 | generic (FE + residue cancellation 1/s + 1/(s−1)) |
| Thm F.2(ii) null vector Q(F₀,F₀) = 0 | YES | YES | YES (if FE) | YES | generic: it is the vanishing of the full-line symbol |
| Lemma 3.1 sawtooth O(X^{−1/2}), Poisson dual | NO: N_D(t) = tP_c(log t) + O(t^θ) | YES, residue c < 1, periodic | NO: remainder X^{θ−1/2} | YES (Pólya–Vinogradov), residue 0 | **selects N(t) − t = O(1), i.e. a_n ≡ 1** |
| Thm F.2(iii) F₀+F₁ regular at 0, F₁ rank one | NO (F₁ not rank one) | YES with c | NO | F₁ = 0 | selects residue 1 together with E.4 |
| Thm F.3 Hilbert kernel | YES with weights a_ma_n | YES | YES (kernel on 𝒩_B×𝒩_B) | YES | generic |
| Prop F.4 deep data O(ρ₀²) | residue ≠ 1: O(D) survives (E §6) | O(D) survives | O(D) survives | no F₁, no 2AB: total is 2Q(F₀,F₂)+Q(F₂) | **selects residue 1** |
| Prop F.5 shallow positivity | YES for small T | YES | YES (small T) | YES (small T) | generic, cites window positivity |
| (★★_EM) | FALSE (certified) | FALSE | FALSE (NUMÉRICO) | FALSE (Ziad, UNVERIFIED) | the Λ-step; OPEN |

**Conclusion (PROVED by the table).** Every identity here survives at least one falsifier; none is decisive
(N_018). The split isolates *where* the four falsifiers differ from ζ inside one formula: cΛ and Beurling
destroy the sawtooth (no O(1) counting error: a_n ≢ 1), a_P keeps the sawtooth but changes the residue, F-DH keeps
the sawtooth and removes F₁ and 2AB. Since (★★_EM) is false for F-DH, **no proof can proceed from
2Q(F₀,F₂) + Q(F₂) alone**: the residue term F₁ = ρ₀/s and the pole 2AB — two scalars ρ₀, ρ₁ and their couplings to
F₀ and F₂ — are indispensable, and since it is false for cΛ, the sawtooth F₂ is indispensable too. The sign of ζ's
exterior form is therefore a property of the *triple* (F₀, F₁, F₂) coupled through one Paley–Wiener datum ρ.

## 8. Labels, what not to retry, verdict
- **PROVED:** Prop F.0, Thm F.1, Thm F.2 (i)–(iv), Cor 3.2, Thm F.3, §4.2 bookkeeping, Prop F.4, the reduction in
  Prop F.5, the table of §7.
- **CITED:** Euler–Maclaurin for ζ_X (Titchmarsh), Guo Lemma 4.3 (r = O(ξ^{−2})), memo A Thm 1.1/Prop 2.1, memo E
  Cor E.3/E.2/E.5, Lemma E.4, Zhu Thm 1.2 (T ≤ 0.8), Paper 46 thm:log5A/W.
- **ARGUED:** §4.3 (Hilbert inequalities cannot give the sign), §5 consequence (c), Rem 3.3 for Beurling/cΛ
  summatory remainders (standard, not re-proved).
- **NO-GO (recorded):** Hilbert/Montgomery–Vaughan/Perfekt upper bounds as the decisive step; "(1,1) class bounded
  below after the pole" (false, Prop F.4); any argument on 2Q(F₀,F₂) + Q(F₂) alone (F-DH).
- **OPEN:** (★★_u) = (★★_EM) = L′♯. No sign is claimed. Row D OPEN.

**Verdict.** Strategy F does not prove L′♯. It replaces the two-variable harmonic cut of memo E by the one-variable
partial sums ζ_X(1−s) on the critical line, where the Euler–Maclaurin split is exact and its smooth part is a
pointwise null vector of the form; the exterior form becomes 2Q(F₀,G) + Q(G) + 2AB with G = residue term + sawtooth,
and the sign is the coupling between F₀ and G through one Paley–Wiener datum (Cor 3.2). The archimedean kernel is
the Hilbert-type kernel max(nξ,mη)/|n²ξ²−m²η²| on the rational lines, the prime part a measure on the same lines.
On deep data the ratio classes are each of size D² while the total is O(1); the sign is decided in the
Euler–Maclaurin transition region (few dilates), not class by class. Objects for REF-D: (★★_u), (★★_EM), the
kernel 𝒦, the null-vector identity Thm F.2(ii), the table of §7.
