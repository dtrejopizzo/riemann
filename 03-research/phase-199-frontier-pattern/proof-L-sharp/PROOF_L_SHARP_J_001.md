# PROOF_L_SHARP_J_001 — Strategy J: (★★) as a weighted Hilbert-type inequality on the exterior carrier

Phase 199, prover memo (pen and paper; no numerics). Target: **Lemma L′♯ in the consolidated form (★★)** of
AUDIT_L_SHARP_1 §6.3: for λ = √μ, a = ½log μ, real r = f̂|_{(λ,∞)} with f even, C², supp f ⊂ [−λ,λ],
f(0) = f̂(0) = f(λ) = 0, modulo the radical 𝒢̄,
 (★★)  𝒜[Zr] + 2AB − 2⟨Zr, Z_log r⟩ ≥ κμ^{−A}·dist²_{L²(λ,∞)}(r, 𝒢̄),
(Zr)(u) = u^{1/2}Σ_{n≥1}r(nu), (Z_log r)(u) = u^{1/2}Σ_{n≥2}(log n)r(nu) on u > λ, Ψ̌(x) = (Zr)(e^x) for x > a and
0 for x ≤ a, 𝒜 = archimedean form with killing term, 2AB = pole term.
OPEN / NO-GO / NUMÉRICO. Notation of memos A/E and of the audit: ν(t) = e^{−|t|/2}/(1−e^{−2|t|}), b_∞ = ψ(¼) − log π,
c_q = Λ(q)q^{−1/2}, Θ_∞(τ) = b_∞ + 2∫_0^∞(1−cos τu)ν(u)du, ã(τ) = Θ_∞(τ) + 4/(1+4τ²) = Re ψ(5/4+iτ/2) − log π.

**Outcome in one line.** (★★) is NOT proved. What is proved: (J.1) the three terms of (★★) as explicit forms on
(λ,∞) in the variable u, with the Gram matrix of dilates J(m,n) = ⟨r(m·), r(n·)⟩ and the Stieltjes form
Z = ∫D_t d⌊t⌋, 𝒞 = ∫D_t d(ψ(t)−t); (J.2) **the brief's step (ii) has no object**: on the exterior carrier the
archimedean pairing between two dilates is the polarised Lévy form, a bounded function of log(n/m) for Lipschitz
data (no 1/|log m − log n| matrix), and the prime pairing is the multiplicative diagonal weight log(mn) on the Gram
matrix (no antisymmetric 1/(log m − log n) kernel); the only Hilbert kernel in the problem is the Riesz projection
in the Mellin frequency of r, which carries no arithmetic — NO-GO (PROVED) for "Montgomery–Vaughan against the Lévy
singularity"; also a correction to Thm E.1′ (the literal class-by-class reading of −ν diverges). (J.3) The **deep
quasi-mode theorem**: for smooth data at depth D the exterior form equals (2 + γ − log 4π)·B_φ²e^D + o(e^D), and
the constant is produced, without any zero, as b_∞ + (log 2 + π/2) + 2 + 2γ = 2(ξ′/ξ)(1) — Γ_ℝ, the Lévy energy of
the mode e^{−x/2}, the pole against the Chebyshev main term (residue 1), and Mertens' constant (a_n ≡ 1): the exact
"constant comparison" asked in (iii). It pins c = 1 (for cΛ the limit is −2(c−1)D·e^D) and shows that at the deep
mode the archimedean part is *negative* (−3.108) and the sign (+0.046) is carried by the Chebyshev remainder. (J.4)
The deep mode is outside the aliasing regime of Paley–Wiener tails, so (★★) remains OPEN; two constraints are added
to the audit's list.

## 0. Corpus check (rule ) and why this is not a retry
- **Index read:** README l.52 (N_018), l.396 (INV_H_001: additive identities of Λ used linearly, NO-GO class 𝓒_H),
  l.397 (INV_J_001: Montgomery–Vaughan / large sieve give only the trivial bound; H_sparse), l.449–455 (phase 199:
  PATTERN_001, MECH_001, memos A–E with AUDIT_13 annotations), 03_ NG-A3/NG-B1/NG-B8 (Montgomery–Vaughan and pair
  correlation as sign sources: NO-GO), 04_ W-sieve, G3A-R167_102 ("MV gives η = ½ for every weight"), 05b L87
  (Perfekt: multiplicative Hilbert matrix 1/(√(mn) log(mn)), falsifier-first only), 06_ R9 (near-coincidences
  m ≈ kn: dead sub-routes "Near as a separate signed operator", "Gram of translates in {log n} alone").
- **Sources read:** AUDIT_L_SHARP_1 §1–§6 (constraints 1–7), PROOF_L_SHARP_E_001 (Thms E.1, E.1′, E.2, E.5, Lemma
  E.4, §7), PROOF_L_SHARP_C_001 §2–§4 (off-line multiplier form, no diagonal weight, leak ≤ 18‖ℓ‖²_X/μ, no converse),
  PROOF_L_SHARP_A_001 §1, §3.2, §4 (Lemma 4.1), phase-55 173 §2.1 (Hadamard sum rule Σ_ρ 1/(ρ(1−ρ)) = 2+γ−log 4π,
  used there on the zero side; not the object below).
- **Why not a retry.** (a) MV/Hilbert's inequality was tried on the *window* carrier as an estimate (INV_J, R167);
  here it is not applied but *tested for an object* on the exterior carrier, and the answer is that there is none
  (Thm J.2) — a structural NO-GO, not an estimate. (b) The deep quasi-mode (Thm J.3) is a new object: the integral
  part X^{1−s}/(1−s) of the harmonic cut Σ_{n≤X}n^{−s} of memo E, isolated as a function on the half line; its form
  value is computed arithmetically (Mertens with constant −γ, Lévy energy of e^{−x/2}) and only *checked* against
  Hadamard's sum rule. No zero datum enters the proof. (c) Nothing below claims a sign for (★★); every identity is
  non-decisive by N_018 and §4 says so.

## 1. The three terms as forms on (λ,∞) (PROVED)

Write H := Zr·u^{−1/2}, i.e. H(u) = Σ_{n≥1}r(nu) (u > λ), H_log(u) = Σ_{n≥2}(log n)r(nu), so Ψ̌(x) = e^{x/2}H(e^x).
All sums converge absolutely by r = O(ξ^{−2}) (Guo Lemma 4.3, CITED). Dilation: (D_t r)(u) := r(tu).

**Proposition J.1 (exact kernels; PROVED).**
(a) Gram matrix of dilates. ‖Ψ̌‖²_{L²(a,∞)} = ‖H‖²_{L²(λ,∞)} = Σ_{m,n≥1}J(m,n), with
 J(m,n) := ∫_λ^∞ r(mu)r(nu)du = m^{−1}∫_{mλ}^∞ r(v)·r((n/m)v)dv = m^{−1}C_{n/m}(mλ),  C_ρ(X) := ∫_X^∞ r(v)r(ρv)dv.
 The overlap of the dilates is exact: in the variable v = mu both factors are evaluated beyond their cut
 (v > mλ ⇒ (n/m)v > nλ), so J(m,n) is the correlation of r at the *ratio* n/m (multiplicative), cut at the depth mλ
 of the smaller index.
(b) Prime part. 2⟨Ψ̌, Ψ̌_log⟩_{L²(a,∞)} = 2⟨H, H_log⟩_{L²(λ,∞)} = Σ_{m,n≥1} log(mn)·J(m,n).
 *The prime part is the Gram matrix of dilates with the multiplicative diagonal weight log m + log n. No kernel in
 log m − log n occurs.*
(c) Ratio classes (single integral). For (α,β) = 1 and any weight w(j),
 Σ_{j≥1} w(j) J(jα, jβ) = α^{−1}∫_λ^∞ r(v) r(βv/α) [Σ_{j ≤ v/(αλ)} w(j)/j] dv.
 With w ≡ 1 this is the harmonic cut H(v/(αλ)) of Thm E.1′ (one variable, because the Gram matrix is a single
 integral); with w(j) = log(j²αβ) it is G_{αβ} of Thm E.2.
(d) Pole term. A = ∫_a^∞Ψ̌e^{−x/2}dx = ∫_λ^∞ H(u)du/u = Σ_n∫_{nλ}^∞ r(v)dv/v, B = ∫_a^∞Ψ̌e^{x/2}dx = ∫_λ^∞H(u)du
 = Σ_n n^{−1}∫_{nλ}^∞ r(v)dv, and 2AB is the rank-two form 2(∫H du/u)(∫H du).
(e) Archimedean part. 𝒜[Ψ̌] = (1/2π)∫Θ_∞(τ)|FΨ̌(τ)|²dτ with
 FΨ̌(τ) = ∫_λ^∞H(u)u^{−½−iτ}du = Σ_n n^{−½+iτ}ρ_n(τ) = ∫_λ^∞ r(v)v^{−½−iτ}·ζ_{≤v/λ}(½−iτ)dv,
 ρ_n(τ) := ∫_{nλ}^∞ r(v)v^{−½−iτ}dv, ζ_{≤X}(s) := Σ_{n≤X}n^{−s}. In the pair expansion, 𝒜[Ψ̌] = Σ_{m,n}𝒜(s_m,s_n) with
 s_m := m^{−1/2}r̃(·+log m)·1_{(a,∞)} and 𝒜(Φ₁,Φ₂) = b_∞⟨Φ₁,Φ₂⟩ + 𝓛(Φ₁,Φ₂), 𝓛 the polarised Lévy form
 ½∫∫(Φ₁(x)−Φ₁(x′))(Φ₂(x)−Φ₂(x′))ν(x−x′)dxdx′ (finite for Lipschitz functions with finitely many jumps).
(f) Stieltjes form. Z = ∫_1^∞ D_t d⌊t⌋ (counting of integers), 𝔐 := ∫_1^∞ D_t dt (so (𝔐H)(u) = u^{−1}∫_u^∞H),
 𝒞 := ∫_1^∞ D_t d(ψ(t) − t) = Σ_q Λ(q)D_q − 𝔐 (Chebyshev remainder), and Lemma E.4 reads
 𝒲_ext[Zr] = (1/2π)∫ã(τ)|FΨ̌(τ)|²dτ − 2⟨H, 𝒞H⟩_{L²(λ,∞)},  with 𝒞H = H_log − 𝔐H (Λ∗1 = log).
*Proof.* (a) Substitute u = e^x in ⟨s_m,s_n⟩ = (mn)^{−1/2}∫_a^∞ r̃(x+log m)r̃(x+log n)dx, r̃(x+log m) = (me^x)^{1/2}r(me^x);
then v = mu. (b) By (a) and Thm E.2 (prime collapse) with log(mn) after symmetrisation. (c) m = jα, n = jβ in (a):
J(jα,jβ) = (jα)^{−1}∫_{jαλ}^∞ r(v)r(βv/α)dv; sum over j and exchange (absolute convergence: Σ_j j^{−1}·O((jαλ)^{−3})).
(d) Direct. (e) u = v/n in each term; exchange of Σ_n and ∫ by absolute convergence; Σ_{n ≤ v/λ} because the n-th term
is supported in v > nλ. (f) ∫_1^∞ r(tu)d⌊t⌋ = Σ_n r(nu); ∫_1^∞ H(tu)d(ψ(t)−t) = Σ_qΛ(q)H(qu) − u^{−1}∫_u^∞H, and
Σ_qΛ(q)H(qu) = Σ_n(Σ_{q|n}Λ(q))r(nu) = H_log(u); the second line is Lemma E.4 with C(log t) = t^{1/2}∫_λ^∞H(u)H(tu)du
(u = e^x, Ψ̌(x+log t) = (tu)^{1/2}H(tu)). □

**Reading.** (★★) is an inequality between two Stieltjes measures on [1,∞) applied to r through dilations: d⌊t⌋ (the
additive counting, inside Z and Z_log) and d(ψ(t)−t) (the multiplicative counting minus its archimedean mean,
inside 𝒞), tested against the archimedean symbol ã on the half line. Replacing ⌊t⌋ by t turns Z into 𝔐 (symbol
1/(s−1), the pole only) and replacing ψ(t) by t kills 𝒞; §3 computes what each replacement does to the sign.

## 2. There is no Hilbert kernel on the exterior carrier (PROVED; NO-GO for step (ii) of the brief)

**Theorem J.2.** Let r̃ be Lipschitz on [a,∞) with r̃ = O(e^{−3x/2}) (true for every Paley–Wiener tail, since
r = f̂|_{(λ,∞)} is the restriction of an entire function).
(a) *Prime pairing.* The coefficient of the pair (m,n) in the prime part is log(mn)·J(m,n) (Prop J.1(b)): a
 multiplicative weight on the Gram matrix of dilates, symmetric, with no singularity and no antisymmetric part.
 Hilbert's inequality in the Montgomery–Vaughan form, |Σ_{m≠n}a_mā_n/(log m − log n)| ≤ πΣ|a_n|²·n (or any of its
 weighted variants), has no term of this shape to act on.
(b) *Archimedean pairing.* The coefficient of (m,n) in 𝒜 is 𝒜(s_m,s_n) = b_∞⟨s_m,s_n⟩ + 𝓛(s_m,s_n). If
 supp r̃ ⊂ (a + log max(m,n), ∞) (both truncations inactive), then
 𝓛(s_m,s_n) = (mn)^{−1/2}·c_{r̃}(log(n/m)),  c_{r̃}(t) := 𝓛(r̃, S_t r̃) = (1/2π)∫(Θ_∞(τ) − b_∞)|Fr̃(τ)|²cos(τt)dτ,
 and c_{r̃} is a bounded, uniformly continuous, even function of t with c_{r̃}(0) = 𝓛[r̃] < ∞. In particular the
 archimedean coefficient has **no singularity at log(n/m) → 0**: the Lévy kernel 1/(2|t|) is integrated against
 |r̃(x) − r̃(x′)|² and produces the Lévy *energy* (the log|τ| growth of Θ_∞), not a Hilbert matrix 1/|log m − log n|.
 With active truncations the coefficient is the polarised pairing of two truncated functions, finite for the same
 reason (one jump each, ∫_0^1∫_0^1 ds dt/(s+t) < ∞), and again bounded uniformly in (m,n).
(c) *Where a Hilbert kernel does occur.* J(m,n) = (1/2π)∫(mn)^{−1/2}(m/n)^{iτ}ρ_m(τ)\overline{ρ_n(τ)}dτ with
 ρ_m = F[r̃·1_{(b,∞)}], b = a + log m, and F[g·1_{(b,∞)}](τ) = ½ĝ(τ) ± (i/2)e^{−ibτ}ℋ[e^{ib(·)}ĝ](τ), ℋ the
 Hilbert transform with kernel p.v. 1/(π(τ−τ′)) (sign by convention) — the Riesz projection in the Mellin frequency
 of r. It is a bounded operator with no arithmetic input; the integers enter only as the phases (m/n)^{iτ}.
Consequently, **the comparison "Lévy singular constant ½ versus Hilbert constant π" proposed in step (ii) has no
object on the exterior carrier**: neither term of (★★) contains an off-diagonal kernel in log m − log n. NO-GO
(PROVED by (a)–(c)) for any proof of (★★) that bounds the prime part by Hilbert/MV inequalities in the integer index
and compares with the Lévy singularity.
*Proof.* (a) is Prop J.1(b). (b): 𝓛 is translation invariant and bilinear; S_{−log m}r̃ and S_{−log n}r̃ differ by
the translation log(n/m); Plancherel for the Lévy form (Θ_∞ − b_∞ = 2∫(1−cos τu)ν ≥ 0, A §1) gives the cosine
formula; boundedness and continuity in t follow from ∫(Θ_∞−b_∞)|Fr̃|² < ∞ (r̃ Lipschitz ⇒ |Fr̃|² = O(τ^{−2}), and
Θ_∞ = O(log τ)). (c): 1_{(b,∞)} = ½(1 + sgn(x−b)) and F[sgn(·−b)g] = i e^{−ibτ}ℋ[e^{ib·}ĝ]-type (classical). □

**Remark 2.1 (a correction to Thm E.1′, harmless for E.5).** E.1′ states that in the ratio classes the kernel
K_W(y−y′+log(β/α))·H(min(…)) "is to be read literally for the regular part −ν(t), t ≠ 0" and that the singular part
occurs only in the class (1,1). This is not right: in the class (α,β) the function ν(y − y′ + log(β/α)) is singular on
the line y′ = y + log(β/α), which meets (a,∞)² whenever |log(β/α)| < diam supp r̃, and ∫∫r̃(y)r̃(y′)ν(y−y′+log(β/α))dydy′
diverges logarithmically there. The class terms are finite only in the polarised reading
Σ_j j^{−1}(αβ)^{−1/2}𝓛(S_{−log jα}r_{jα}, S_{−log jβ}r_{jβ}) (which is what Thm E.1 uses). Thm E.5 is unaffected: its
diagonal class is written polarised, and for (α,β) ≠ (1,1) the archimedean class term on deep data is
Σ_j j^{−1}(αβ)^{−1/2}c_{r̃}(log(β/α)) + O(1) = (αβ)^{−1/2}c_{r̃}(log(β/α))·D + O(1), linear in D as E claims.

## 3. The deep quasi-mode: the exact constant comparison (PROVED given the PNT)

The harmonic cut of memo E, Σ_{n≤X}n^{−s} = ζ(s) + X^{1−s}/(1−s) + E_X(s) (Euler–Maclaurin), inserted in Prop J.1(e)
gives FΨ̌ = [ζ·ρ_λ-part] + B·λ^{−½−iτ}/(½+iτ) + [E-part]: the middle term is exactly the Fourier transform of
Ψ_0^{(∞)} := B e^{−x/2}1_{(a,∞)} — the **quasi-mode**, the image of the pole under the summation map (Z ≈ 𝔐 = ∫D_t dt,
𝔐r = u^{−1}∫_u^∞r ≈ B/u). On its own Ψ_0 is outside the domain of the prime comb (Σ_qΛ(q)/q = ∞); it is cut off at
the depth of the data. The following theorem isolates it with smooth data, where the cut is clean.

**Theorem J.3 (deep quasi-mode; PROVED given the PNT, CITED).** Let φ ∈ C_c^∞(0,1) be real, B_φ := ∫φ(s)e^{s/2}ds,
and r̃ := φ(· − a − D), i.e. r(ξ) = ξ^{−1/2}φ(log(ξ/λ) − D) (data at depth D, relative width 1). Then, as D → ∞,
 **𝒲_ext[Zr] = 𝒜[Zr] + 2AB − 2⟨Zr, Z_log r⟩ = (2 + γ − log 4π)·B_φ²e^D + o(e^D),**
and the constant decomposes term by term as
 (J.3a)  𝒜[Zr] = (b_∞ + log 2 + π/2)·B_φ²e^D + o(e^D) = −3.108…·B_φ²e^D + o(e^D),
 (J.3b)  2AB − 2⟨Zr,Z_log r⟩ = (2 + 2γ)·B_φ²e^D + o(e^D),
and on the quasi-mode Ψ_0 of the proof separately 2A(Ψ_0)B(Ψ_0) = 2D(1−e^{−D})·B_φ²e^D and
2⟨Ψ_0,Ψ_{0,log}⟩ = 2(D − 1 − γ)·B_φ²e^D + o(e^D) (pole and prime part individually of size D·e^D, their difference
2 + 2γ), so that 2 + γ − log 4π = [ψ(¼) − log π] + [log 2 + π/2] + [2] + [2γ] = −5.372 + 2.264 + 2 + 1.154 = 0.0462.
*Proof.* Put c := a + D, L := e^{c−x}. For x > a, Ψ̌(x) = Σ_{m≥1}F_x(m), F_x(m) := m^{−1/2}φ(x + log m − c)
= e^{−(c−x)/2}g(m/L), g(ρ) := ρ^{−1/2}φ(log ρ) ∈ C_c^∞(1,e). Poisson summation in m (F_x ∈ C_c^∞(0,∞)):
Σ_{m≥1}F_x(m) = ∫_0^∞F_x + Σ_{k≠0}F̂_x(k) = B_φL^{1/2} + Σ_{k≠0}L^{1/2}ĝ(kL), and |ĝ(ξ)| ≤ C_N(1+|ξ|)^{−N}. Hence
 Ψ̌ = Ψ_0 + Ψ_1,  Ψ_0(x) := B_φ e^{(c−x)/2}1_{(a,c)}(x) = B e^{−x/2}1_{(a,c)}(x) with B := B_φe^{c/2},
 |Ψ_1(x)| ≤ C_N e^{−(N−½)(c−x)} (a < x < c),  |Ψ_1(x)| ≤ 3‖φ‖_∞ (c ≤ x < c+1),  Ψ_1 = 0 (x ≥ c+1),
with the same bounds for Ψ_1′ on (a,c) ∪ (c,c+1) (differentiate under Σ_k); Ψ_1 has one jump (at c, of size B_φ)
and ‖Ψ_1‖_{L¹}, ‖Ψ_1‖_{L²}, 𝓛[Ψ_1] are O(1) uniformly in D. Note B²e^{−a} = B_φ²e^D.
(i) *ã-form of Ψ_0.* FΨ_0(τ) = B(e^{−a(½+iτ)} − e^{−c(½+iτ)})/(½+iτ), |FΨ_0|² = B²e^{−a}|1 − e^{−D(½+iτ)}|²/(¼+τ²), so
(1/2π)∫ã|FΨ_0|² = B²e^{−a}[c₀ + O(e^{−D/2})], c₀ := (1/2π)∫ã(τ)dτ/(¼+τ²) (|ã| = O(log τ), the integral converges).
Compute c₀ with Tonelli on the Lévy representation ((1/2π)∫(1−cos τu)/(¼+τ²)dτ = 1 − e^{−u/2}, (1/2π)∫dτ/(¼+τ²) = 1,
(1/2π)∫[4/(1+4τ²)]/(¼+τ²)dτ = (1/2π)∫dτ/(¼+τ²)² = 2):
 c₀ = b_∞ + 2∫_0^∞ν(u)(1−e^{−u/2})du + 2,  2∫_0^∞ e^{−u/2}(1−e^{−u/2})/(1−e^{−2u})du = 4∫_0^1 dw/((1+w)(1+w²)) = log 2 + π/2
(w = e^{−u/2}; 1/((1+w)(1+w²)) = ½[1/(1+w) + (1−w)/(1+w²)]). Thus c₀ = ψ(¼) − log π + log 2 + π/2 + 2 = ψ(3/2) − log π
= 2 − γ − 2log 2 − log π (ψ(¼) = −γ − π/2 − 3log 2, ψ(3/2) = 2 − γ − 2 log 2). This gives (J.3a) after removing the
P₀-part "+2" (𝒜 = ã-form − (1/2π)∫[4/(1+4τ²)]|F|²).
(ii) *Chebyshev remainder of Ψ_0.* For a < x < c, with Y := e^{c−x}:
 (𝒞Ψ_0)(x) = Σ_qΛ(q)q^{−1/2}Ψ_0(x+log q) − ∫_0^∞e^{t/2}Ψ_0(x+t)dt = Be^{−x/2}[Σ_{q<Y}Λ(q)/q − log Y] = Be^{−x/2}(−γ + ε(Y)),
where ε(Y) → 0 is the Mertens remainder: Σ_{n≤Y}Λ(n)/n = log Y − γ + o(1), the constant −γ being the constant term of
−ζ′/ζ at s = 1 and the o(1) the PNT (CITED; e.g. Montgomery–Vaughan, *Multiplicative Number Theory I*, Ch. 8). Hence
2⟨Ψ_0,𝒞Ψ_0⟩ = 2B²∫_a^c e^{−x}(−γ + ε(e^{c−x}))dx = 2B²e^{−a}[−γ(1−e^{−D}) + ∫_0^De^{−t}ε(e^{D−t})dt] = −2γB_φ²e^D + o(e^D)
(dominated convergence, ε bounded). Separately, Σ_qΛ(q)q^{−1/2}·2⟨Ψ_0,S_{log q}Ψ_0⟩ = 2B²∫_a^ce^{−x}(c − x − γ + ε)dx
= 2B_φ²e^D(D − 1 − γ + o(1)), and 2A(Ψ_0)B(Ψ_0) = 2·Be^{−a}(1−e^{−D})·BD = 2D·B_φ²e^D(1 − e^{−D}): the quasi-mode
part of (J.3b); the difference 2AB − (prime main term) = 2B_φ²e^D is the "+2" of (i), as Lemma E.4 requires. (For the
full Ψ̌ the pole term and the prime part are each 2D·B_φ²e^D + O(e^D), the cross terms with Ψ_1 being O(e^D); only
their combination 2AB − 2⟨Ψ̌,Ψ̌_log⟩ = ã-remainder is controlled to o(e^D), through (iii).)
(iii) *Cross and remainder terms.* 𝒲_ext = ã-form − 2⟨·,𝒞·⟩ is a quadratic form; polarise. ã-cross:
|(1/2π)∫ã FΨ_0\overline{FΨ_1}| ≤ (∫|ã||FΨ_0|²)^{1/2}(∫|ã||FΨ_1|²)^{1/2} = O(e^{D/2})·O(1). ã-form of Ψ_1: O(1). Prime
cross: ⟨Ψ_1,𝒞Ψ_0⟩ = ∫Ψ_1(x)Be^{−x/2}(−γ+ε)1_{(a,c)}dx = O(∫_a^c e^{−(N−½)(c−x)}e^{(c−x)/2}dx) = O(1); and, by the
computation of (ii) with Ψ_1 in the second slot,
 ⟨Ψ_0,𝒞Ψ_1⟩ = B_φ∫Ψ_1(y)e^{(c−y)/2}[(ψ(e^{y−a}) − e^{y−a}) − (ψ(e^{y−c}) − max(1,e^{y−c}))]dy = o(e^D)
since ψ(Y) − Y = o(Y) (PNT) at Y = e^{y−a} ≈ e^D on the support of Ψ_1, and ‖Ψ_1e^{(c−·)/2}‖_{L¹} = O(1). Prime part
of Ψ_1: Σ_qΛ(q)q^{−1/2}|⟨Ψ_1,S_{log q}Ψ_1⟩| ≤ Σ_qΛ(q)q^{−1/2}·O(q^{−N+½}) < ∞, integral part O(1). Summing (i)–(iii):
𝒲_ext[Zr] = B_φ²e^D(c₀ + 2γ) + o(e^D) = (2 + γ − log 4π)B_φ²e^D + o(e^D). □

**Corollary J.4 (anatomy and consistency; PROVED / CITED).**
(a) *Explicit-formula check.* 2 + γ − log 4π = 2(ξ′/ξ)(1) = Σ_ρ 1/(ρ(1−ρ)) (Hadamard product, CITED: Davenport
 Ch. 12; phase-55 173 §2.1). Directly: Φ_{Ψ_0}(s) = B(e^{(s−1)c} − e^{(s−1)a})/(s−1), so Σ_ρ Φ_{Ψ_0}(ρ)Φ_{Ψ_0}(1−ρ) →
 B²e^{−a}Σ_ρ 1/(ρ(1−ρ)) as D → ∞ (dominated convergence, |e^{(ρ−1)D} + e^{−ρD}| ≤ 2, Σ|ρ|^{−2} < ∞, no zero-free
 region used). The zero-free computation of Thm J.3 and the zero-side representation of the exterior form (C Prop
 1.2 / Rem 2.1(i)) agree: the deep quasi-mode evaluates the Weil distribution at the pole s = 1, where
 ξ′/ξ(1) = 1 − ½log π + ½ψ(½) + [ζ′/ζ(s) + 1/(s−1)]_{s=1} = 1 − ½log π + ½ψ(½) + γ.
(b) *Continuous model (ψ(t) → t, 𝒞 = 0: the comb replaced by its mean).* The limit becomes c₀ = ψ(3/2) − log π =
 −1.108 < 0. So **on the deep quasi-mode the archimedean form, pole included, is negative, and the sign +0.046 is
 produced by the Chebyshev remainder through Mertens' constant −γ** (Λ∗1 = log composed with Σ_{n≤Y}1/n − log Y → γ:
 the semiring constant). Any mechanism that proves (★★) by dominating the prime part with the archimedean part
 fails already on smooth deep data (quantitative form of A §5's NO-GO, independent of the TV barrier).
(c) *Pinning c = 1 (step (iii) of the brief).* For the exterior form with comb cΛ and the same Z, pole and Γ_ℝ,
 form_c := 𝒜 + 2AB − 2c⟨Zr,Z_log r⟩, Thm J.3 gives e^{−D}B_φ^{−2}form_c = 0.046 − 2(c−1)(D − 1 − γ) + o(1): negative for
 every c > 1 once D > 1 + γ + 0.023/(c−1), and → +∞ for c < 1. Without the pole (F-DH-type, with ζ's comb) the limit
 is 0.046 − 2D → −∞. For deleted primes a_P with the same Z the limit is 0.046 + 2Σ_{p∈P}(log p)/(p−1) > 0 (Mertens
 for the P-free comb), so a_P is not detected at the deep mode — its failure lives elsewhere. The residue 1 is what
 cancels the growth 2D (pole) against 2(D−1) (Chebyshev main term); the O(1) constants then decide, and they are
 the four inputs (Λ-E) of memo E: Γ_ℝ (ψ(¼)), conductor 1 (−log π), residue 1 (+2), a_n ≡ 1 (+2γ).
(d) *Cross-class cancellation of Thm E.5, quantified.* In E's normalisation the class (1,1) contributes
 D c_φ − D² + O(D) on these data, while the total is +0.046·B_φ²e^D: the near-coincident classes (α ≈ β, α,β ≤ e^D,
 total weight Σ(αβ)^{−1/2} ≍ e^D) carry the sign, as E.5 predicted; here with its value.

## 4. What this gives for (★★), and the residual (OPEN)

**4.1 The deep mode is not the regime of (★★) (PROVED, elementary).** A Paley–Wiener tail r = f̂|_{(λ,∞)} oscillates on
the scale 1/λ in ξ, i.e. on the scale 1/μ in y = log ξ near y ≈ a; the data of Thm J.3 are smooth on scale 1 in y
at depth D. A function f̂ entire of type λ whose restriction to (λ,∞) were a bump at ξ ≈ λe^D of relative width 1
would have f supported in an interval of length ≍ (λe^D)^{−1} < 1/λ, i.e. f in the gauge, with Zr a radical vector
(𝒲_ext = 0) — so the data of J.3 are not Z-images of admissible f, and Thm J.3 is a theorem about the complete Weil
form on half-line tests (the object of E §5), not about (★★). (Deep bumps are L²(λ,∞)-limits of PW_λ tails by the
Hardy-space density argument, but Z is not L²-bounded (C Prop 4.2), so no limit statement transfers: ARGUED, not
used.) On the aliasing regime, the quasi-mode Ψ_0 = Be^{−x/2} is still present in FΨ̌ (the X^{1−s}/(1−s) term of
the harmonic cut), with B = ∫_λ^∞ r = −∫_0^λ f̂ not gauge-invariant; its interaction with the E-part is the
truncation defect, and nothing in §3 bounds it.

**4.2 The residual inequality.** (★★) in the Stieltjes form of Prop J.1(f):
 (1/2π)∫ã(τ)|∫_λ^∞ r(v)v^{−½−iτ}ζ_{≤v/λ}(½−iτ)dv|²dτ − 2⟨Zr, 𝒞Zr⟩ ≥ κμ^{−A}dist²(r,𝒢̄),  𝒞 = ∫_1^∞D_t d(ψ(t)−t),
for r a Paley–Wiener tail of type λ. OPEN. Strategy J adds no estimate towards it; the only Hilbert-type inequality
available on this carrier is the Riesz projection in the Mellin frequency (Thm J.2(c)), which is comb-blind.

**4.3 Two constraints to add to AUDIT_L_SHARP_1 §6.3.**
8. *No Hilbert matrix in the integer index* (Thm J.2): the prime part is log(mn) on the Gram matrix of dilates and
 the archimedean pairing between dilates is a bounded function of log(n/m) on Lipschitz data; Montgomery–Vaughan,
 large-sieve or Hilbert-matrix bounds in (m,n) have no object on the exterior carrier.
9. *The deep-mode value* (Thm J.3): on smooth deep data the exterior form tends to 2(ξ′/ξ)(1)·B_φ²e^D with
 2(ξ′/ξ)(1) = 2+γ−log 4π = 0.046, archimedean part −3.108, pole against Chebyshev +2, Mertens +2γ. A candidate
 mechanism for (★★) that extends to C_c^∞ data must reproduce this number; "archimedean dominates primes" cannot.

## 5. Labels and verdict
- **PROVED:** Prop J.1 (a)–(f); Thm J.2 (a)–(c); Rem 2.1 (correction to E.1′; E.5 unaffected); Thm J.3 (given the
  PNT in Mertens' form, CITED), including the elementary constants c₀ = ψ(3/2) − log π and 2∫ν(1−e^{−u/2}) = log 2 + π/2;
  Cor J.4 (b), (c), (d); §4.1.
- **CITED:** Guo Lemma 4.3; Thm E.2, Lemma E.4, Thm E.5; C Prop 1.2, Prop 4.2; Mertens' formula with constant −γ /
  PNT (Montgomery–Vaughan Ch. 8); Hadamard's Σ_ρ 1/ρ = 1 + γ/2 − ½log 4π (Davenport Ch. 12) for Cor J.4(a).
- **ARGUED:** the Hardy-space density of deep bumps in L²(λ,∞) (§4.1; not used).
- **NO-GO (class, PROVED):** "Hilbert/Montgomery–Vaughan inequality in the integer index against the Lévy singularity"
  on the exterior carrier (no object, Thm J.2); "archimedean part dominates the prime part" (false at the deep mode,
  Cor J.4(b)).
- **OPEN:** (★★) = L′♯. No sign is claimed. Row D OPEN.

**Verdict.** Strategy J, taken literally, has no object: the exterior form has no Hilbert kernel in log m − log n,
and the Lévy singularity is the Lévy energy, not a matrix. What survives is the exact constant comparison at the
deep quasi-mode, computed without zeros: Γ_ℝ (ψ(¼) − log π = −5.372) + Lévy energy of e^{−x/2} (log 2 + π/2 = 2.264)
+ pole against Chebyshev main term (+2, residue 1) + Mertens (+2γ = 1.154) = 2(ξ′/ξ)(1) = 0.046 > 0, negative for
cΛ (c > 1) and without the pole. It is the semiring principle evaluated at one point (the pole s = 1), it certifies
that the prime remainder — not the archimedean form — carries the sign there, and it is not the aliasing regime of
Paley–Wiener tails where (★★) lives. Do not retry Hilbert-type bounds in the integer index on the exterior carrier.
