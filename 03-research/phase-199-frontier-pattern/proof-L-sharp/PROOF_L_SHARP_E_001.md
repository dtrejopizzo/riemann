# PROOF_L_SHARP_E_001 — Strategy E: the truncation defect written on the pairs (m,n) of integers

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯** (AUDIT_199): ∃κ>0, A≥0:
∀μ ≥ 5, ∀g ∈ E(core): W_T(g) ≥ κμ^{−A}ℓ(g), ℓ(g) = inf{leak(f): Ef = g}.
Notation as in PROOF_L_SHARP_A_001 (memo A): λ = e^T, μ = λ², a = T, f admissible real with f(λ) = 0,
r = r_f = f̂·1_{|ξ|>λ}, r̃(x) = e^{x/2}r(e^x) (x > a), Ψ̌(x) = Ψ_f(−x) = (Zr)(e^x) = e^{x/2}Σ_{n≥1}r(ne^x) for x > a,
Ψ̌ = 0 for x ≤ a. Weil kernel pieces: b_∞ = ψ(¼) − log π, ν(t) = e^{−|t|/2}/(1−e^{−2|t|}), c_q = Λ(q)q^{−1/2}.

**Outcome in one line.** L′♯ is NOT proved. What is proved: (E.1) an exact *pair expansion* of the exterior
form on the aliasing tail, 𝒲_ext[Zr] = Σ_{m,n≥1}(mn)^{−1/2}⟨r̃(·+log m), K_W r̃(·+log n)⟩_{(a,∞)}, and its
regrouping by ratio m/n = α/β in lowest terms, in which the multiplier-sum over j (m = jα, n = jβ) is the
*harmonic partial sum* H(X) = Σ_{j≤X}1/j cut at X = min(ξ/αλ, η/βλ) — this is the "+ meets ·" object of the
semiring principle, written exactly; (E.2) the **prime collapse**: on Z-images the whole prime comb Σ_q c_q S_{log q}
reduces, by Λ∗1 = log, to the single log-weighted summation map, so the exterior form is **Λ-free**: it depends on
the comb only through a_n ≡ 1; (E.3) the exact cancellation pole − Chebyshev main term (memo B Lemma 3.1) holds
verbatim on the half line and gives 𝒲_ext = ã-form − R_Λ with R_Λ an explicit Λ-free functional of r; (E.4) the
ratio classes are **individually indefinite** (the diagonal class α = β = 1 is negative on deep data), so no
sum-of-squares over ratios exists: the sign, if any, is an interference between classes mediated by the harmonic
cut. The remaining inequality (★E) is stated exactly in §5; the falsifier table in §6 shows that every step here is
multiplicative-generic or additive-generic, and that the only Λ-ingredient left is the triple (a_n ≡ 1 on ℕ,
residue 1, Γ_ℝ with conductor 1) — not Λ ≥ 0, which the collapse has consumed. One correction to memo A (§1).

## 0. Corpus check (rule ) and why this is not a retry
- **Index read:** README l.52 (N_018: identities + Bochner/C–S are non-decisive), l.390 (INV_C_001: Farey/coprime/
  Möbius counts of h⁰ off the diagonal, "sin información para el signo", Möbius normalisation
  ζ(2σ)^{−1}∫|ζ|²F̂ — do not retry as Farey/coprimes/Möbius of h⁰), l.415 (INV_V_002: Λ∗1 = log as the operator
  identity V^*Ш = 2log|x|·Ш, linear, Hamburger class), l.396 (INV_H_001: additive identities of Λ used linearly:
  NO-GO class 𝓒_H), l.450–452 (MECH_001, memo B, memo A), phase 197 BARRIER_EST Thm 4, PRINCIPIO RECTOR (semiring).
- **Sources read:** memo A (Thm 1.1, Prop 2.1, §3.2–3.4, §5, §6), memo B (Lemma 1.1, Lemma 3.1, Lemma 3.2,
  Prop 3.3, Lemma 4.1, Thm 4.2), AUDIT_199 (L′♯ definition), Paper 47 thm:A and the killing-form remark after it
  (Dirichlet form with killing κ(x) = ∫_{|y|>T}K(|x−y|)dy), prop:archneg, Guo §4 as cited in memo A.
- **Why not a retry.** (a) INV_C_001 grouped *pairs of integers in the window* by ratio to build h⁰; here the
  pairs are the integers *beyond* the window that produce the aliasing tail, the weights are the Weil kernel
  itself, and the new object is the harmonic cut H(min(ξ/αλ, η/βλ)) that the truncation of memo A §3.2 induces on
  each ratio class — INV_C has no truncation (it works on 𝒫_T, where the ratio comb is exact). Its conclusion
  "ratio counting carries no sign" is *confirmed* here (Thm E.4), not retried as a sign source. (b) INV_V_002 used
  Λ∗1 = log as a linear transfer on the window; here the same identity is applied *inside* a quadratic form in
  which the comb is complete (all q, not q < μ), and it eliminates Λ from the form altogether (Thm E.2). That is a
  structural statement about the target, not a positivity attempt. (c) Nothing below claims a sign; by N_018 no
  identity here is decisive, and §7 says which identity is which.

## 1. The exterior form: one correction to memo A (killing term)

Memo A's display of 𝒲_ext writes the Lévy energy as ½∫∫_{y,y'<−a}|Ψ(y)−Ψ(y')|²ν(y−y')dydy' (both variables on
the half line). The object actually used in Theorem 1.1 is ∫Ψ̄WΨ with W the full-line distribution, whose
Lévy part is ½∫∫_{ℝ²}|Ψ(y)−Ψ(y')|²ν(y−y')dydy' for Ψ extended by zero (Plancherel on the symbol
Θ_∞(τ) = b_∞ + 2∫_0^∞(1−cos τu)ν(u)du; Paper 47 thm:A and the "Dirichlet form with killing" remark). The strips
{y < −a < y'} contribute the **killing term** ∫_{y<−a}|Ψ(y)|²κ_a(y)dy, κ_a(y) := ∫_{−a}^∞ν(y−y')dy' = ∫_{|y+a|}^∞ν(t)dt
(≈ ½log(1/|y+a|) near the boundary, integrable against |Ψ|² since Ψ is bounded there). **Correction (PROVED):**
 𝒲_ext[Ψ] = b_∞‖Ψ‖² + ½∫∫_{(−∞,−a)²}|Ψ(y)−Ψ(y')|²ν + ∫_{−∞}^{−a}|Ψ|²κ_a − 2Σ_q c_q∫Ψ(y)Ψ(y−log q)dy + 2A(Ψ)B(Ψ).
Theorem 1.1 of memo A (W_T(g) = ∫Ψ̄_f WΨ_f) is unaffected; only the displayed formula lacked the (nonnegative)
killing term. Prop 2.1 and Thm 3.1 of memo A are unaffected (they use 𝒲_ext as ∫Ψ̄WΨ). Below, 𝒲_ext always means
the full-line form of the zero-extended function, written in the reflected variable x = −y:
 𝒲_ext[Zr] = 𝒲[Ψ̌] = ∫∫_{ℝ²}Ψ̌(x)Ψ̌(x′)K_W(x−x′)dxdx′  (formal kernel notation),
with K_W = b_∞δ + Lévy(ν) − Σ_q c_q(δ_{log q}+δ_{−log q}) + 2cosh(t/2); the Lévy piece is read in the polarised
form 𝓛(Φ₁,Φ₂) = ½∫∫(Φ₁(x)−Φ₁(x′))(Φ₂(x)−Φ₂(x′))ν(x−x′)dxdx′. All pairings below converge absolutely because
r = O(ξ^{−2}) (Guo Lemma 4.3, CITED), hence r̃(x) = O(e^{−3x/2}) and Σ_n n^{−1/2}|r̃(x+log n)| = O(e^{−3x/2}).

## 2. The pair expansion and the ratio regrouping (PROVED)

**Theorem E.1 (pair expansion; PROVED).** With r_n := r̃·1_{(a+log n,∞)} (the part of r beyond ξ = nλ, in the
log variable) one has the identity of functions on ℝ
 Ψ̌ = Σ_{n≥1} n^{−1/2} S_{−log n} r_n,   (S_u φ)(x) = φ(x−u),
and therefore, by bilinearity and translation invariance of 𝒲,
 (E.1a) 𝒲_ext[Zr] = Σ_{m,n≥1}(mn)^{−1/2} ∫∫_{x,x′>a} r̃(x+log m) r̃(x′+log n) K_W(x−x′) dx dx′
        = Σ_{m,n≥1}(mn)^{−1/2} ∫∫ r_m(y) r_n(y′) K_W(y−y′+log(n/m)) dy dy′.
*Proof.* For x > a, Ψ̌(x) = e^{x/2}Σ_n r(ne^x) = Σ_n n^{−1/2}r̃(x+log n), and r̃(x+log n) = r_n(x+log n) because
x+log n > a+log n; for x ≤ a both sides vanish (r_n(x+log n) = 0 when x + log n ≤ a + log n). Insert into
𝒲[Ψ̌] = Σ_{m,n}(mn)^{−1/2}𝒲(S_{−log m}r_m, S_{−log n}r_n) and use 𝒲(S_uΦ₁,S_vΦ₂) = ∫∫Φ₁(y)Φ₂(y′)K_W(y−y′+v−u)
(K_W is a convolution kernel: Θ_∞(D), the shifts, and 2cosh((x−x′)/2) are all translation invariant). Absolute
convergence: Σ_{m,n}(mn)^{−1/2}∫∫|r_m||r_n|(|ν|+2cosh+Σ_q c_q(…)) < ∞ by the decay in §1 and Σ_q c_q q^{−3/2} < ∞;
the Lévy piece is handled in polarised form, where |r̃| Lipschitz on (a,∞) and the single jump of Ψ̌ at a give
∫∫_{x<a<x′}ν(x−x′)|Ψ̌(x′)|² < ∞ (∫_0^1∫_0^1 dsdt/(s+t) < ∞). □

**Theorem E.1′ (ratio classes and the harmonic cut; PROVED).** Write each pair as (m,n) = (jα, jβ) with
(α,β) = 1, j ≥ 1. Then
 (E.1b) 𝒲_ext[Zr] = Σ_{(α,β)=1}(αβ)^{−1/2} ∫∫_{y,y′>a} r̃(y) r̃(y′) K_W(y−y′+log(β/α)) · H(min(e^{y−a}/α, e^{y′−a}/β)) dy dy′,
 H(X) := Σ_{1≤j≤X} 1/j  (H = 0 for X < 1).
Here K_W(t)·H is to be read literally for the *regular* part of K_W (−ν(t) for t ≠ 0, the prime δ's, 2cosh(t/2));
the singular diagonal part (b_∞δ and the Lévy regularisation at t = 0) occurs only in the class (α,β) = (1,1),
where it is read as Σ_j j^{−1}·[b_∞‖r_j‖² + 𝓛(r_j,r_j)] with r_j = r̃·1_{(a+log j,∞)} (polarised Lévy form of the
truncated functions, not a pointwise weight).
*Proof.* In (E.1a), r_{jα}(y)r_{jβ}(y′) = r̃(y)r̃(y′)·1[y > a+log(jα)]·1[y′ > a+log(jβ)], (mn)^{−1/2} = j^{−1}(αβ)^{−1/2},
and the shift log(n/m) = log(β/α) does not depend on j. For the regular part of K_W, summing j^{−1} over the j
allowed by both indicators gives H(min(e^{y−a}/α, e^{y′−a}/β)); for the singular part (shift 0, so α = β = 1) the
j-th term is the archimedean self-pairing of r_j. Rearrangement is justified by the absolute convergence of E.1. □

**Reading.** In the ξ-variables (ξ = e^y, η = e^{y′}) the cut is j ≤ min(ξ/αλ, η/βλ): the pair (ξ,η) of
out-of-band frequencies is paired through the Weil kernel at the *rational* shift log(β/α) (the · part: the
kernel sees only the ratio), and the pair is counted once for each common multiplier j such that jαλ ≤ ξ and
jβλ ≤ η (the + part: counting multiples up to a bound), with the harmonic weight 1/j. Without the cut
(H ≡ const) the (α,β)-sum is the coprime comb Σ_{(α,β)=1}(αβ)^{−1/2}δ_{log(α/β)} of INV_C_001, whose Mellin symbol
is |ζ(½+iτ)|²/ζ(1) — formally zero, i.e. divergent-and-cancelling. The harmonic cut H(X) = log X + γ + h(X),
h(X) = O(1/X) a sawtooth, regularises ζ(1) to log X + γ: the Euler constant and the truncation depth
log(ξ/αλ) are the only things the form retains from the counting of multiples. This is the exact form of memo A's
"all of W_T(g) is a truncation defect at n ≈ λ/u".

## 3. The prime collapse (PROVED): the exterior form is Λ-free

**Theorem E.2 (prime collapse; PROVED).** On Z-images the complete one-sided prime comb reduces to the
log-weighted summation map:
 −2Σ_{q≥2} c_q ⟨Ψ̌, S_{log q}Ψ̌⟩_{L²(a,∞)} = −2⟨Ψ̌, Ψ̌_log⟩_{L²(a,∞)},   Ψ̌_log(x) := Σ_{n≥1} n^{−1/2}(log n)·r̃(x+log n) = e^{x/2}Σ_n (log n) r(ne^x).
Equivalently, in the pair expansion the prime part of K_W contributes exactly −Σ_{m,n}(mn)^{−1/2}log(mn)·I_a(m,n),
I_a(m,n) := ∫_a^∞ r̃(x+log m)r̃(x+log n)dx, and in the ratio classes exactly
 −Σ_{(α,β)=1}(αβ)^{−1/2}∫_{y>a} r̃(y) r̃(y+log(β/α)) G_{αβ}(e^{y−a}/α) dy,  G_{αβ}(X) := Σ_{j≤X}(2log j + log αβ)/j.
*Proof.* For x > a and q ≥ 2, Ψ̌(x+log q) = Σ_l l^{−1/2}r̃(x+log(lq)) (the restriction x+log q > a is automatic).
Hence Σ_q c_q⟨Ψ̌,S_{log q}Ψ̌⟩ = Σ_q Σ_{m,l} Λ(q)q^{−1/2}(ml)^{−1/2} I_a(m, lq) = Σ_{m,n}(mn)^{−1/2}(Σ_{q|n}Λ(q)) I_a(m,n), and
Σ_{q|n}Λ(q) = log n (Λ∗1 = log; the n = 1 term is 0 = log 1, consistent with q ≥ 2). All sums converge absolutely
(§1), so the rearrangement is legitimate. Symmetrise I_a(m,n) = I_a(n,m) to get log(mn). The ratio form follows
with m = jα, n = jβ, log(mn) = 2log j + log αβ and the cut j ≤ e^{y−a}/α (= e^{y′−a}/β on the shifted diagonal).
Consistency with (E.1b), where the prime δ's of K_W sit at shifts log(β/α) ∓ log q with weight c_q(αβ)^{−1/2}H(·):
collecting the classes (α,β) that land on a given shift log(β′/α′) and using Σ_{q: q/gcd(q,α′) | j}Λ(q) = log(jα′)
(a prime power p^e satisfies p^e/gcd(p^e,α′) | j iff p^e | jα′) reproduces Σ_{j≤X}(log(jα′)+log(jβ′))/j = G_{α′β′}(X):
the two bookkeepings agree. □

**Corollary E.3 (the exterior form without Λ; PROVED).** For every admissible real f with f(λ) = 0,
 W_T(Ef) = 𝒲_ext[Zr] = 𝒜_a[Ψ̌] − 2⟨Ψ̌, Ψ̌_log⟩ + 2A(Ψ̌)B(Ψ̌),
where 𝒜_a[Ψ̌] = b_∞‖Ψ̌‖² + ½∫∫_{ℝ²}|Ψ̌(x)−Ψ̌(x′)|²ν(x−x′) (= (1/2π)∫Θ_∞|FΨ̌|²) is the archimedean form of the
zero-extended Ψ̌, A = ∫_a^∞Ψ̌e^{−x/2}, B = ∫_a^∞Ψ̌e^{x/2}, and Ψ̌ = Zr, Ψ̌_log = Z_log r with
 (Zr)(w) = w^{1/2}Σ_{n≥1}r(nw),  (Z_log r)(w) = w^{1/2}Σ_{n≥2}(log n)r(nw)  (w > λ).
No prime, no Λ(q), no Euler product appears: **the comb enters the exterior form only through the identity
Λ∗1 = log, i.e. only through the fact that the summation map has coefficients a_n ≡ 1.**

**Remark 3.1 (operator form; PROVED, elementary).** Z_log = M_{log w}Z − Z M_{log ξ} (commutator of the summation
map with multiplication by the logarithm), and Z is invertible on functions on (λ,∞) by Möbius,
Z^{−1}Φ(w) = Σ_m μ(m)(mw)^{−1/2}Φ(mw). Hence Z_log Z^{−1} = Σ_{N≥2}c_N S_{log N} (because μ∗log = Λ): the one-sided
prime comb *is* the commutator defect [M_log, Z]Z^{−1}. This is the operator content of Theorem E.2 and of the
transfer identity of INV_V_002; nothing more is claimed from it.

**Remark 3.2 (universality; PROVED).** For any Dirichlet series D(s) = Σa_n n^{−s} with comb Λ_D (coefficients of
−D′/D) one has Σ_{ql=n}Λ_D(q)a_l = a_n log n, so the same collapse holds for the exterior form of any
(E_D, Λ_D)-system: 𝒲^D_ext[Z_D r] = 𝒜^D[Z_D r] − 2⟨Z_D r, (Z_D)_log r⟩ + pole_D, (Z_D)_log r = w^{1/2}Σa_n log n·r(nw).
The difference between ζ and its twins lies entirely in (a_n, Θ_D, pole_D) and in how r is produced.

## 4. The pole–Chebyshev cancellation on the half line (PROVED) and the Mellin reading

**Lemma E.4 (memo B Lemma 3.1 on the half line; PROVED, classical).** For Ψ̌ as above put C(u) := ∫Ψ̌(x)Ψ̌(x+u)dx
(even, C(u) = O(e^{−3|u|/2})). Then
 2A(Ψ̌)B(Ψ̌) − 2∫_1^∞ t^{−1/2}C(log t)dt = ∫_ℝ e^{−|u|/2}C(u)du = (1/2π)∫|FΨ̌(τ)|²(¼+τ²)^{−1}dτ ≥ 0,
and therefore
 (E.4) 𝒲_ext[Zr] = (1/2π)∫ã(τ)|FΨ̌(τ)|²dτ − R_Λ(Ψ̌),  ã(τ) = Re ψ(5/4+iτ/2) − log π,  R_Λ(Ψ̌) := 2∫_1^∞ t^{−1/2}C(log t)d(ψ(t)−t),
with, by Theorem E.2, the Λ-free expression
 R_Λ(Ψ̌) = Σ_{m,n}(mn)^{−1/2}log(mn)·I_a(m,n) − 2∫_0^∞e^{u/2}C(u)du = 2⟨Ψ̌,Ψ̌_log⟩ − 2∫_0^∞ e^{u/2}C(u)du.
*Proof.* Identical to memo B Lemma 3.1 (2AB = ∫(e^{|u|/2}+e^{−|u|/2})C(u)du; 2∫_1^∞t^{−1/2}C(log t)dt = ∫e^{|u|/2}C;
F(e^{−|u|/2}) = (¼+τ²)^{−1}); all integrals converge absolutely by the decay of C. The Stieltjes integral against
dψ reproduces −2Σ_q c_q C(log q) = −2Σ_q c_q⟨Ψ̌,S_{log q}Ψ̌⟩. □

**Reading (the "(iii)" of the brief, as identities).** (a) The residue 1 of −ζ′/ζ at s = 1 is cancelled by the
pole term for *every* half-line Ψ̌; after the cancellation the archimedean weight is ã (negative only on
|τ| ≲ 5.8, = log(τ/2π) + O(τ^{−2}) beyond) and the whole arithmetic is the Chebyshev-remainder form R_Λ.
(b) On the *full* line the symbol of R_Λ is the boundary value of −2Re[ζ′/ζ(s) + 1/(1−s)] on Re s = ½, and by the
functional equation it equals ã minus the zero point masses: the full-line form ã − R_Λ is the zero sum
(memo B §3.5; CITED Guinand–Weil). On the half line this symbol calculus is unavailable (memo A Rem 3.3), and
(E.4) is an identity between two explicit functionals of r with no zero data and no prime data.
(c) In Mellin terms (memo A §3.2) H_{Ψ}(s) = Σ_n n^{s−1}R_{nλ}(s) with R_c(s) = ∫_c^∞ rξ^{−s}dξ, and
H_{Ψ_log}(s) = Σ_n n^{s−1}(log n)R_{nλ}(s): the two are the truncated versions of ζ(1−s)R_λ(s) and −ζ′(1−s)R_λ(s).
The prime collapse is the statement that on the half line the pairing −2Σc_q C(log q) is the truncated version
of the multiplier −2Re(ζ′/ζ)(1−s̄)… applied to ζ(1−s)R_λ(s), i.e. of −2Re[ζ′(1−s)ζ(1−s̄)]|R_λ|²; the Γ_ℝ-term
Θ_∞ is the truncated version of the same multiplier with the opposite sign (FE). **The sign of 𝒲_ext is the sign of
the difference between the two truncations of one vanishing symbol.**

## 5. Ratio classes are not individually positive (PROVED) — the remaining inequality (★E)

**Theorem E.5 (no sum of squares over ratios; PROVED).** Write 𝒲_ext[Zr] = Σ_{(α,β)=1}(αβ)^{−1/2}Q_{α/β}(r̃) with
Q_{α/β} the (α,β)-term of (E.1b) (prime part in the form of Theorem E.2). Then the diagonal class Q_{1/1} is
indefinite: for every μ there are r̃ ∈ C_c^∞(a,∞) with Q_{1/1}(r̃) < 0. Consequently 𝒲_ext is not a sum of
nonnegative ratio-class forms, for any choice of the (αβ)^{−1/2}-normalisation.
*Proof.* By Thm E.1′ (singular part read as stated there) and Thm E.2,
 Q_{1/1}(r̃) = Σ_j j^{−1}[𝒜_a[r_j] + 2A(r_j)B(r_j)] − 2∫r̃(y)²H₁(e^{y−a})dy,  r_j = r̃·1_{(a+log j,∞)},
with H₁(X) = Σ_{j≤X}(log j)/j = ½log²X + γ₁ + O(log X/X). Take r̃ = φ(· − a − D) with φ a fixed smooth bump of unit
L²-norm supported in (0,1) and D large. For j ≤ e^D, r_j = r̃ and the bracket equals 𝒜_a[φ] + 2A(φ)B(φ) =: c_φ
(the archimedean form and the pole term are translation invariant); for e^D < j < e^{D+1}, r_j is a truncated bump
with one jump, whose Lévy energy is finite and bounded uniformly in the cut (jump² × ∫_0^1∫_0^1 dsdt/(s+t)), so the
bracket is O(1); for j ≥ e^{D+1}, r_j = 0. Hence the first sum is H(e^D)c_φ + O(1) = Dc_φ + O(1). The prime term is
−2∫φ²·H₁(e^{D+·}) ≤ −2(½D² + O(1)) = −D² + O(1). For D large the total is negative. □
(The same computation shows the class (α,β) is negative on data placed at depth D ≫ log(αβ): the coefficient
G_{αβ} ~ log²X is quadratic in the depth while H ~ log X is linear.)

**What this means.** The positivity of 𝒲_ext on aliasing tails, if true, is produced by the *off-diagonal* classes
(α,β) ≠ (1,1) through the Weil kernel at log(β/α) and by the rational shifts' interference — the pairs
(ξ, η) = (jαλ·, jβλ·) with ξ/η rational, i.e. exactly the near-coincidences m ≈ kn of the semiring principle; and
the depth weights H (linear) and G (quadratic) must cancel *across* classes. No single class, and no finite set
of classes, carries the sign (same proof: data deep enough).

**The remaining inequality (OPEN).** By memo A Thm 3.1 and Corollary E.3, L′♯ is equivalent to: ∃κ, A such that
for all μ ≥ 5 and all real admissible f with f(λ) = 0, with r = (1−P_λ)f̂ and Ψ̌ = Zr on (a,∞),
 (★E)  𝒜_a[Zr] + 2A(Zr)B(Zr) − 2⟨Zr, Z_log r⟩ ≥ κμ^{−A}·dist²(r, 𝒢̄),
equivalently (1/2π)∫ã|F(Zr)|² − R_Λ(Zr) ≥ κμ^{−A}dist²(r,𝒢̄), with R_Λ as in Lemma E.4 — an inequality between
explicit functionals of r **in which no prime appears**. The data class is the only place where ℕ's additive
structure enters: r is the restriction to |ξ| > λ of an entire function of exponential type λ (f̂, f supported in
[−λ,λ]) with f(0) = f̂(0) = f(λ) = 0, modulo the radical 𝒢̄ = closure{(1−P_λ)φ̂ : supp φ ⊂ [−1/λ,1/λ]}.
(★E) is false for arbitrary r ∈ L²(λ,∞): translation invariance of 𝒲 and the surjectivity of Z (Möbius) make
"𝒲_ext[Zr] ≥ 0 for all half-line r" the positivity of the complete Weil form on all compactly supported tests
(PROVED, elementary) — which is not a tool here and is not used. So the Paley–Wiener constraint on r (lattice
aliasing) is not decorative: it is the whole additive input.

## 6. Falsifier table (constraint (iv) of the brief)

| step | cΛ (with E_c, d_c) | a_P (deleted primes, E over P-free n) | Beurling B (E_B over 𝒩_B) | F-DH (conductor 5, no pole) | verdict |
|---|---|---|---|---|---|
| Thm E.1/E.1′ pair expansion + harmonic cut | YES (weights d_c(m)d_c(n), cut Σ_{j≤X}d_c-weighted) | YES (pairs in P-free integers) | YES (pairs in 𝒩_B; cut Σ_{j∈𝒩_B, j≤X}1/j = log X + γ_B + h_B) | YES (weights a_DH(m)a_DH(n)) | generic bookkeeping |
| Thm E.2 collapse Λ_D∗a = a·log | YES | YES | YES | YES | multiplicative-generic (Rem 3.2) |
| Cor E.3 Λ-free form | YES | YES | YES | YES (no pole term) | generic |
| Lemma E.4 pole cancels residue | residue c ≠ 1: leftover (1−c)∫e^{|u|/2}C, sign flips for c > 1 | residue Π_{p∈P}(1−1/p) ≠ 1: leftover | residue of ζ_B: leftover unless 1 | no pole: the main term ∫e^{u/2}C is *not* cancelled | **selects residue 1** |
| Thm E.5 classes indefinite | YES | YES | YES | YES | generic |
| (★E) | FALSE (certified λ^W(cΛ) < 0, via the cΛ-identity) | FALSE | FALSE (NUMÉRICO) | FALSE (Ziad, UNVERIFIED) | the Λ-step; OPEN |

**Conclusion (PROVED by the table).** Every identity of this memo survives all four falsifiers; none is decisive
(N_018). The only step that distinguishes ζ is Lemma E.4's cancellation, and it distinguishes by the *residue*, not
by Λ ≥ 0. After Theorem E.2 the statement (★E) contains no Λ at all; the Λ-ingredient of L′♯ is therefore exactly:
 **(Λ-E)** a_n ≡ 1 on all of ℕ (plain summation map Z, so that Λ∗1 = log with coefficient 1), residue 1 (pole
 term 2AB cancelling ∫e^{u/2}C exactly), Γ_ℝ(s) with conductor 1 (Θ_∞, and the band λ = e^T of the Poisson
 aliasing matched to the Γ-factor), and r = lattice aliasing of a compactly supported f (Paley–Wiener).
"Λ ≥ 0 on prime powers" is not available as an input in this formulation: it has been consumed by the collapse
(it is equivalent to a_n ≡ 1 giving log ζ nonnegative coefficients, which the form never sees separately).
A proof of (★E) must use the four items of (Λ-E) together — the brief's "pole/conductor-1 input" — and nothing
else is left to use.

## 7. What was attempted on (★E) and why it is not finished (ARGUED / NO-GO)
- **Sum of squares over ratios:** NO-GO (Thm E.5).
- **Schur product of the Lévy kernel with the coprime comb:** the coprime comb at weight ½ has Möbius signs
  (Σ_d μ(d)/d·full comb), so it is not a positive-definite measure; its product with a PD kernel need not be PD;
  with the harmonic cut it is not even a comb (it depends on (y,y′) separately). NO-GO as a Bochner argument
  (and TV-robust ⇒ excluded by memo B Lemma 4.1 anyway).
- **Depth asymptotics:** H(X) = log X + γ + h(X), G_{αβ}(X) = log²X + (log αβ)(log X + γ) + 2γ₁ + h_{αβ}(X), with
  the Stieltjes constants γ, γ₁ (Laurent coefficients of ζ at 1) and sawtooth remainders h = O(1/X). Replacing H, G
  by their smooth parts gives a form whose symbol is the full-line zero sum (vanishing symbol) — but the min() in
  H(min) is not smooth, and no exact identity for the "smooth part" on the half line was found. The sawtooth parts
  are O(λ^{−1}) relative and cannot alone carry a bound at scale μ^{−A} (ARGUED: they are of size ‖r‖²/λ at the
  edge, which is the right scale for A ≥ 1, but no sign).
- **Edge-localised data:** if supp r ⊂ (λ, 2λ] then Zr = r̃, Z_log r = 0 and 𝒲_ext[Zr] = 𝒜_a[r̃] + 2AB, the
  complete archimedean form on an interval of length log 2 (half-length 0.347 < 0.4608 of prop:archneg). Paper 47
  proves only the upper bound there (negative from 0.4608, on the odd vector); no positivity below is recorded, and
  true aliasing tails are never compactly supported (Paley–Wiener). Not usable; recorded to avoid a retry.

## 8. Labels and verdict
- **PROVED:** §1 correction (killing term), Thm E.1, Thm E.1′, Thm E.2 (incl. the consistency check of the two
  bookkeepings), Cor E.3, Rem 3.1, Rem 3.2, Lemma E.4 (classical), Thm E.5, the "arbitrary r" remark of §5, the
  table of §6 and its conclusion (Λ-E).
- **CITED:** Guo Lemma 4.3 (r = O(ξ^{−2})), Paper 47 thm:A and the killing-form remark, prop:archneg, memo A
  Thm 1.1/Prop 2.1/Thm 3.1, memo B Lemma 3.1, Guinand–Weil.
- **ARGUED:** size of the sawtooth parts (§7).
- **NO-GO:** sum of squares over ratio classes; Schur/Bochner on the coprime comb; edge-localised model.
- **OPEN:** (★E), equivalently L′♯. No sign is claimed. Row D OPEN.

**Verdict.** Strategy E delivers the exact arithmetic of the truncation defect: pairs (m,n) of integers beyond the
window, Weil kernel at log(n/m), harmonic counting of common multiples cut at the window edge; and it shows that
the complete prime comb collapses to the log-weighted summation map, leaving a Λ-free inequality (★E) whose only
arithmetic inputs are a_n ≡ 1, residue 1, conductor 1 and lattice aliasing. Ratio classes are individually
indefinite, so the sign is an interference across rational shifts mediated by the harmonic cut — the semiring
principle in its exact form — and this memo does not prove it. Do not retry "positivity of 𝒲_ext class by class"
or "Λ ≥ 0 inside the exterior form" (both closed here).
