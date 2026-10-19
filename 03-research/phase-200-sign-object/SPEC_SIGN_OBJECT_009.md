# SPEC_SIGN_OBJECT_009 — Round 19 (V′): inventory of exogenous auxiliary objects

Phase 200 ("sign object"), synthesizer.
Objective: L′♯ / row D.

## 0. Corpus check (mandatory)

grep over `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md`, with line number:

| term | hits | relevant entry |
|---|---|---|
| Kurokawa, E101_083, tensor, C10, θ-sheaf, exogenous | 1 each | l.553 (SPEC_008: "before V′: grep E101_083, C10, θ-sheaf") |
| theta sheaf, auxiliary, auxiliary function, auxiliary measure, pair of L's, product of forms, sym², Mayer, parabolic, Laplacian, Katz, 1-level | 0 | — |
| Rankin / Rankin convolution | 4 | l.203 (front A: Petersson/Maass–Selberg/Rankin–Selberg blind to the comb and to h*), l.337 (residue "Rankin–Selberg in w", Salié/Kuznetsov), l.446 (connecting layer: Kronecker parity; **weight gap**: RS only in σ>1) |
| Petersson | 2 | l.203 |
| Eisenstein | 1 | l.204 (metaplectic, rank one) |
| Maass / Maass–Selberg | 3 | l.203–206: abscissa transport 1→½ NO-GO PROVED; Maass–Selberg = window form of ζ(2s) on the squares |
| Selberg / trace | 18 / 11 | l.252: "exact Selberg/Arthur traces (NO-GO PROVED class TF⁺)" = CA_F_002 |
| Lewis–Zagier | 3 | l.203, l.333 (NO-GO ARGUED: Λ absent) |
| transfer | 12 | l.229 (Hardy), l.360 (Thm N2) — none is the Mayer operator |
| W-det / W-mom / order ≥ 2 | 3/2/2 | l.39, l.50–51, l.550–552 (AUDIT_200_SPEC007: g at order ≥ 2 already indexed) |
| W-lin / N_018 | — | l.50, l.52, l.115 (averages/linear identities) |
| de Branges | 2 | l.232 (de Branges/Kreĭn dead) |
| Mori | 32 | l.440–449 (½log15, CITED; extremals = data) |
| Kuznetsov | 1 | l.337 (only as a front-A residue, without a family-by-weight development) |

Files read: SPEC_008 (V′, Prop 18.4), CA_F_002 (Lemma 1, Cor 2–3, class TF⁺), E101_083 (positive tensor transport),
LEDGER_L5 (C10 = global object never built). No index entry treats the **Hecke family averaged by Petersson with
weight k as a variable** nor the **shift r ↦ r + i/4 of the parabolic term**: these are the only two points in this
round with a new reason written out (§2, §3).

## 1. The restrictions of V′ (operational reminder)

A property Π of an auxiliary object 𝒳 is useful if 𝔞^ζ_T ≻ 0 in P_T follows from Π(𝒳), and Π is: (a) ≠ the form or
its minimum (REF-D); (b) nonlinear in the comb (Φ.1, Lemma 18.V3); (c) not a datum (C-data); (d) lives in P_T
(C-pol); (e) discontinuous in the comb (C-τ) and feels Λ_cosh (C-E′); (f) not an invariant of (ℚ,ℚ^×) (C-MvN).
Moreover, from SPEC_008 §V′: the variable ν that 𝒳 introduces is not in {T, σ, q, N, test k, scale, M} and falsifier
a_P does not admit the same extension in ν.

## 2. Table A: X1–X5

| | object | what it introduces | restriction that kills it | label |
|---|---|---|---|---|
| X1a | L′ and ζ·L′ | nothing (Φ.12 additive) | (b) linear: 𝔞^{ζL′} = 𝔞^ζ + 𝔞^{L′} | NO-GO PROVED (Φ.12) |
| X1b | f×f̄ (Rankin–Selberg), f fixed | bilinear comb in (λ_f, λ_f) | 𝔞^{f×f̄} = 𝔞^ζ + 𝔞^{sym²f} (Φ.12); subtracting requires 𝔞^{sym²f} ≤ 𝔞^{f×f̄}, which is 𝔞^ζ ≥ 0 rewritten (REF-D); Petersson positivity is a residue at s=1 (weight gap, l.446), not a window statement | NO-GO PROVED (Lemma 19.1 + Prop 19.2) |
| X1c | family {f} of weight k, averaged with harmonic weights | variable ν = k | ν enters only through the Γ factor (archimedean conductor): it is "scale", excluded by Prop 18.4; the averaged comb is Λ·(Sato–Tate constants), comb-generic; a_P admits the same extension | NO-GO PROVED mod. CITED (Theorem 19.3) — **most developed** |
| X2 | measure μ over tests | ∫𝔞_T(g)dμ(g) | linear in μ ⇒ a form of the average (N_018, W-lin); Cauchy–Schwarz over μ only gives upper bounds of the prime term (like the grand sieve of V3) | NO-GO PROVED (Obs 19.4) |
| X3a | operator A by formula with 𝔞 = ⟨g,Ag⟩ | positivity of A | if A is defined by the explicit formula, A ≥ 0 is the form (REF-D); R-Π, A_μ closed | NO-GO (REF-D) |
| X3b | Selberg trace formula of PSL₂(ℤ) | spectrum of Δ (≥ 0) | class TF⁺, CA_F_002 Lemma 1/Cor 3; the shift r ↦ r+i/4 carries ξ(2s) to the critical line only via Re ξ′/ξ = 0 or a sum of zeros, and destroys ĥ ≥ 0 | NO-GO PROVED (Prop 19.5, extension of CA_F_002) |
| X3c | Mayer transfer operator 𝓛_s | det(1−𝓛_s) = Z_Selberg | Z_Selberg is the spectral side of X3b: inherits Prop 19.5; Lewis–Zagier already NO-GO ARGUED (l.203) | NO-GO (by reduction to X3b) |
| X4 | Kurokawa tensor / E101_083 transport / θ-sheaf / C10 | positive tensor powers | E101_083: positive transport of tensor powers ⇒ disjoint supports (no mixing); Kurokawa ζ⊗ζ in the comb = Λ·Λ-convolution of logs, which has no FE with a finite-type Γ-factor nor a simple pole in the P_T sense (Kurokawa, CITED: multiple products are not automorphic L-functions), so it fails C-pol; θ-sheaf: C-MvN (sees only the (ℚ,ℚ^×) isomorphism); C10 without an object | NO-GO (E101_083 PROVED; θ-sheaf ARGUED); C10 OPEN without content |
| X5 | fixed exogenous F (Mori extremal, de Branges function) | 𝔞_T(g) vs 𝔞_T(F) | fixed F = datum (C-data); coupling it to g gives 𝔞(g+εF): order 2 in g ⇒ W-det/W-mom (l.550–552); Theorem X: the new prime contribution must cancel σ in U at resolution π/T, which fixed F does not see; de Branges dead (l.232) | NO-GO PROVED (by W-mom + C-data) |

## 3. Development of the points with a new reason

### 3.1 X1b: Rankin–Selberg with fixed f

Let f be a primitive Hecke form of level 1, weight k, with Satake parameters {α_p, β_p}, α_pβ_p = 1, |α_p| = 1
(Deligne, CITED). L(f×f̄,s) = ∏_p ∏_{i,j}(1 − γ_iγ̄_j p^{−s})^{−1}, γ ∈ {α_p, β_p}.

**Lemma 19.1 (PROVED).** The comb of f×f̄ is Λ_{f×f̄}(p^j) = log p · |α_p^j + β_p^j|² = log p · |λ_f(p^j) −
λ_f(p^{j−2})|² ≥ 0 (with λ_f(p^{−1}) = 0). Moreover L(f×f̄,s) = ζ(s)·L(sym²f,s) (Shimura, CITED) and
Λ_{sym²f}(p^j) = log p·(|α^j+β^j|² − 1).
*Proof.* −L′/L = Σ_p Σ_j log p · (Σ_{i,j′} (γ_iγ̄_{j′})^j) p^{−js}, and Σ_{i,j′}(γ_iγ̄_{j′})^j = |α^j+β^j|². For the
second equality: α^j+β^j = λ(p^j) − λ(p^{j−2}) by Hecke. The sym² decomposition is that of |tr|² = 1 + tr(sym²) for
SU(2). ∎

**Proposition 19.2 (PROVED).** With P_T and 𝔞 as in Paper 47 (sec:spec, thm:shape, rem:shape-additive):
(i) 𝔞^{f×f̄}_T = 𝔞^ζ_T + 𝔞^{sym²f}_T in P_T (Φ.12; additive conductors and Γ);
(ii) any derivation of 𝔞^ζ_T ⪰ 0 from this identity needs 𝔞^{sym²f}_T ⪯ 𝔞^{f×f̄}_T, which is literally 𝔞^ζ_T ⪰ 0
(REF-D);
(iii) there is no operator 𝒦_{T,g} on L²(Γ\ℍ) with 𝔞^{f×f̄}_T(g) = ⟨f, 𝒦_{T,g} f⟩_{Pet} for every primitive f, with 𝒦
independent of f.
*Proof.* (i)–(ii) are Φ.12. (iii): the left side depends on f via log-derivatives: at p^j, j ≥ 2, |λ(p^j) −
λ(p^{j−2})|² appears, which is quadratic in the Hecke sequence but **not** in the form f as an L² vector (λ_f(n) =
a_f(n)/a_f(1) is a nonlinear normalization; with ‖f‖ free, ⟨f,𝒦f⟩ scales as ‖f‖² and 𝔞^{f×f̄} is scale-invariant). If
‖f‖=1 is normalized, the form ⟨f,𝒦f⟩ restricted to primitives is still the restriction of a quadratic form, while
the archimedean term of 𝔞^{f×f̄} contains ψ(s+k−1) with k the weight, which is not a quadratic value of f in any
fixed-weight space except as a constant; the constant and the prime term coexist only as a Rankin–Selberg form
∫|f|²y^k E(z,s) dμ, which lives in Re s > 1 and at s=1 gives the residue ∝ ‖f‖² (Rankin, CITED). Carrying it to the
window at ½ is the abscissa transport 1 → ½, NO-GO PROVED (index l.205–206). ∎

Reading: Rankin's positivity is **residue** positivity (or σ > 1), exactly the "weight gap" of l.446.
Maass–Selberg (l.206) covers it for the Eisenstein part; Rankin's residue covers it for the cusp form. X1b adds no
new reason.

### 3.2 X1c (most developed): the Hecke family with weight as an exogenous variable

**New reason written out (index requirement).** Front A (l.203) closed Petersson positivity for individual forms
and abscissa transport. The **harmonic average of 𝔞^{f×f̄}_T over the Hecke basis of weight k**, with ν = k as a
free variable, was never written. The exogenous object is S_k(SL₂(ℤ)) with its Petersson product. It is exogenous
because k is not a parameter of ζ's explicit formula. It is nonlinear in the comb because the comb of f×f̄ is
bilinear in λ_f. And the intrinsic positivity is that of the harmonic weights ω_f = Γ(k−1)/((4π)^{k−1}‖f‖²) > 0. It
remains to see whether it survives Prop 18.4.

**Definition.** For k ≥ 12 even, let H_k be the Hecke basis and ω_f the harmonic weights. Define
  𝔄_{T,k}(g) := Σ_{f∈H_k} ω_f · 𝔞^{f×f̄}_T(g),  g ∈ P_T.

**Lemma 19.3a (CITED + PROVED).** Petersson formula (CITED, Iwaniec–Kowalski Prop 14.5):
  Σ_f ω_f λ_f(m)λ_f(n) = δ_{m,n} + 2π i^{−k} Σ_{c≥1} S(m,n;c)c^{−1} J_{k−1}(4π√(mn)/c).
For m,n ≤ e^{2T} and k−1 ≥ 8π e^{2T}, the Kloosterman term is bounded by C·e^{2T}·(2πe^{2T})^{k−1}/(k−1)! (bound
|J_ν(x)| ≤ (x/2)^ν/ν!, CITED; |S| ≤ c). That term is superexponentially small in k (PROVED). Also Σ_f ω_f = 1 +
(the same error).

**Corollary 19.3b (PROVED mod. 19.3a).** For n = p^j ≤ e^{2T}:
  Σ_f ω_f Λ_{f×f̄}(p^j) = log p · (min(j,2) + E_k), with |E_k| ≤ the error of 19.3a.
*Proof.* |λ(p^j) − λ(p^{j−2})|² = λ(p^j)² + λ(p^{j−2})² − 2λ(p^j)λ(p^{j−2}). By 19.3a: 1 + 1{j≥2} − 0. This matches
the Sato–Tate moments E|tr U^j|² = min(j,2) in SU(2). ∎

**Theorem 19.3 (NO-GO; PROVED mod. 19.3a CITED).** For k ≫ e^{2T}:
  𝔄_{T,k} = (Σω_f)·[A^{(k)}_T − P^{ST}_T] + O(E_k),
where P^{ST}_T is the prime term with comb Λ(n)·min(j(n),2) and A^{(k)}_T the archimedean part of
Γ_ℂ(s)Γ_ℂ(s+k−1) plus ζ's polar part (the only pole of L(f×f̄) at s=1). Then:
(i) ν = k enters **only** through A^{(k)}_T, and in P_T that is a shift of the C₀-type constant by
ψ(k−½+…) ~ log k (Φ.12: m = 2Re Γ′/Γ is linear). That is, k is a **scale/conductor** parameter, which Prop 18.4
excludes: ν is not exogenous in the sense of V′.
(ii) for large k, 𝔄_{T,k} ≻ 0 trivially, by conductor dominance (≈ log k against a prime term bounded in P_T), with
no information about 𝔞^ζ. The step from 𝔄 to 𝔞^ζ = 𝔄 − ⟨𝔞^{sym²}⟩ requires 𝔞^ζ ⪰ 0 (REF-D, as in 19.2(ii)).
(iii) the averaged comb Λ·min(j,2) is Λ times universal Sato–Tate constants. It is comb-generic and linear in Λ
(fails (b), Lemma 18.V3). Falsifier a_P = Λ·1{p ≥ P} admits the same extension (the family of Euler-deleted
L_P(f×f̄) averages to a_P·min(j,2)), so V′(iii) fails. The extension does **not** fail observably in ν, because ν
only moves the archimedean constant, which is identical for ζ and a_P.
(iv) C-MvN: the average only uses the multiplicative structure of ℕ (Hecke) and the SU(2) constants. It is an
invariant of (ℚ,ℚ^×) plus the Sato–Tate measure.
*Proof.* (i) Corollary 19.3b plus linearity of 𝔞 in (comb, Γ, conductor) (Φ.12). (ii) A^{(k)}_T grows like log k
uniformly in P_T (Stirling, CITED); the prime term is bounded by Σ_{n≤e^{2T}} 2Λ(n)n^{−½}‖g‖. (iii)–(iv) are a
direct reading of (i) and of 19.3b. ∎

**Level variant (ARGUED).** With level N instead of weight, the Petersson formula changes the error to Kloosterman
with c ≡ 0 mod N. For N ≫ e^{4T} the same conclusion holds, with ν = N = conductor: excluded for the same reason.
With the Maass and Kuznetsov family, the diagonal term is the same; the continuous Eisenstein term reintroduces
|ζ(1+2it)|^{−2} (abscissa 1, MW-2, CA_F_002 Cor 3).

**Falsifiers.** Beurling: there is no modular surface, but the averaged family only uses the Sato–Tate diagonal,
which is defined for any comb. So the object does not distinguish Beurling from ζ (C-MvN, expected and fatal).
Epstein h>1: the Hecke average does not see the class number. a_P: (iii).

**Test on Mori / Lemma E.** Unnecessary. The theorem is structural: for every T, including T = ½log15, 𝔄_{T,k} ≻ 0
for k ≥ k₀(T), and that positivity is the same for the comb Λ·1{p≥P}, whose form is negative on [0.60, ½log P]
(cor:Tarch). Explicit counterexample to "Π(𝔄) ⇒ 𝔞^ζ ≻ 0" with Π independent of the comb: PROVED.

**First exact lemma that would have been needed (for the record).** A property Π of {𝔄_{T,k}}_k that was
discontinuous in k (for example, a sign change for finite k depending on Λ beyond the diagonal). The diagonal is
forced by 19.3a, and the Kloosterman term is O(E_k) in the regime where 19.3a is useful. The only place where the
comb enters nonlinearly is the transition regime k ≍ 4πe^{2T}, where J_{k−1} stops being negligible. There the
dependence on the comb is through S(m,n;c), which is a sum of additive characters: Kloosterman sums = data over
𝔽_p (C-data), and their positivity is that of local Weil–Deligne (|S| ≤ 2√c τ(c)), a **bound**, not a sign. This is
the "Salié/Kuznetsov" residue of l.337. OPEN as a question, but with no survivor: any sign in the transition is a
functional of Kloosterman sums, which do not feel Λ_cosh (C-E′). ARGUED.

### 3.3 X3b: Selberg with a shift to ½ (the "weights n^{−1}" objection)

For PSL₂(ℤ): the continuous term is −(1/4π)∫ h(r) (φ′/φ)(½+ir) dr, with φ(s) = ξ(2s−1)/ξ(2s) (CITED,
Hejhal/Iwaniec). On the line, ξ(2s) appears at 1+2ir and ξ(2s−1) at 2ir: abscissas 1 and 0. Hence the weights
n^{−1}.

**Proposition 19.5 (PROVED; extension of CA_F_002 Lemma 1).** Let h be even entire with ĥ ≥ 0 on the unitary dual.
Shift the integral to Im r = −1/4 (s = ¼ + it, 2s = ½ + 2it):
(i) the factors become ξ(½+2it) and ξ(−½+2it) = ξ(3/2−2it). The first enters only as
Re ξ′/ξ(½+2it) + i·(phase). By CA_F_002 Lemma 1(i) the real part is 0, and the phase gives π Σ_γ ĥ(γ/2 − …) (the
zero side). The second is at abscissa 3/2 (absolute convergence, MW-2).
(ii) The shifted integral has integrand h(t − i/4), which is neither ≥ 0 nor real. Spectral positivity (ĥ ≥ 0 on
the unitary dual, Δ ≥ 0) applies to the discrete side, which **does not move**. The shifted identity is a Cauchy
equality (plus the residues of the poles of φ′/φ in the strip 0 < Im(−r) < ¼: zeros of ξ(2s), zero side) with no
new positivity.
(iii) Hence, ζ's window form at ½ with weights n^{−½} does not appear in any term of (TF⁺), either before or after
the shift. Only zeros or data at abscissa ≥ 1 appear.
*Proof.* (i) Direct substitution plus Lemma 1. (ii) Cauchy's theorem on the strip: h entire and φ′/φ meromorphic.
The poles of φ′/φ in ½ − ¼ < Re s < ½ are the zeros of ξ(2s) with ¼ < Re s < ½, i.e., zeros of ξ (all zeros of
ξ(2s) lie in ¼ ≤ Re s ≤ ½ if counted by 0 ≤ Re ρ ≤ 1), and their residues are ĥ at the ordinates of the zeros. The
poles of ξ(2s−1) fall at abscissa ≥ ½ (zeros of ξ) or at the pole s=1, outside the strip. (iii) follows from
(i)+(ii). ∎

Hyperbolic side: Σ_{D} h(D)·log ε_D·(…) with g(2 log ε_D). h(D) enters as **geometric multiplicity** (data of
classes of quadratic forms, C-data) and with weights ε_D^{−1} (abscissa 1 in the length parameter). What is
"interesting" about Epstein (h>1 in the hyperbolic part) is real, but only as data. Positivity remains on the
discrete side, which does not contain ζ at ½. **Verdict X3: NO-GO PROVED, covered by CA_F_002 (TF⁺). The i/4 shift
is not a new reason: Prop 19.5 reduces it to CA_F_002 Lemma 1.** The Mayer operator (X3c) is the same spectral
object (Fredholm determinant = Z_Selberg) and inherits the verdict.

### 3.4 X2, X4, X5 (brief)

**Obs 19.4 (X2; PROVED).** ∫𝔞_T(g)dμ(g) = tr(𝔞_T·Σ_μ) with Σ_μ = ∫ g⊗ḡ dμ ⪰ 0. Positivity for every μ ⇔
𝔞_T ⪰ 0 (REF-D). For fixed μ it is a number linear in the comb (Φ.1). Cauchy–Schwarz over μ,
|∫𝔞(g,h)dμ|² ≤ ∫𝔞(g,g)∫𝔞(h,h), presupposes 𝔞 ⪰ 0. Without 𝔞 ⪰ 0, it only bounds the prime term from above (like
the grand sieve, Prop 18.2): N_018/W-lin.

**X4.** E101_083 (PROVED): a linear transport sending a positive diagonal tensor power of prime events to a
positive spectral diagonal has rows with disjoint support, so it does not mix. The "Kurokawa tensor product" ζ⊗ζ has
a Λ⋆Λ-type comb (convolution of zero log-derivatives, ρ_i+ρ_j). It has no functional equation with a finite-type
Γ-factor nor a simple pole in the P_T sense (Kurokawa, CITED: multiple products are not automorphic L-functions),
so it fails C-pol. θ-sheaf: it only sees (ℚ,ℚ^×) (C-MvN, ARGUED, already recorded in SPEC_008). C10: OPEN without
an object. None of X1–X5 is C10, because all are objects already written over ℚ that contribute no ample class nor
h⁰.

**X5.** Fixed F enters as 𝔞(F) (a number: C-data) or as 𝔞(g,F) (linear in g and in the comb: Φ.1). The only way
for F to contribute nonlinear information is through 𝔞(g+εF) at order ε², which is order ≥ 2 in g: W-det/W-mom,
indexed (l.550–552, AUDIT_200_SPEC007 §5). The Mori extremal at μ=15 is a certificate (datum of ½log15, CITED) and
does not extend beyond its window (Lemma 18.1). Theorem X: the contribution of new primes when crossing e^{2T} must
cancel σ in U at resolution π/T, and a fixed F does not depend on T.

## 4. Table C: ranking

| rank | candidate | status | reason |
|---|---|---|---|
| 1 | X1c Hecke family, ν = weight/level | NO-GO PROVED mod. Petersson CITED | closest to V′: exogenous, bilinear, intrinsic positivity ω_f > 0; dies because ν = conductor (Prop 18.4) and the diagonal is comb-generic Sato–Tate. Residue: transition regime k ≍ 4πe^{2T} (Kloosterman, ARGUED dead by C-data/C-E′) |
| 2 | X3b Selberg with i/4 shift | NO-GO PROVED | Prop 19.5 = CA_F_002 Lemma 1; h(D) only as data |
| 3 | X1b Rankin with fixed f | NO-GO PROVED | Φ.12 + REF-D; residue positivity |
| 4 | X5 exogenous F | NO-GO | C-data / W-mom / Theorem X |
| 5 | X4 Kurokawa / θ / E101_083 | NO-GO (E101_083 PROVED; θ ARGUED) | no mixing; C-pol; C-MvN |
| 6 | X2 measure over tests | NO-GO PROVED | linear |
| — | C10 | OPEN | object not written |

**Structural conclusion (ARGUED, reinforces Prop 18.4).** Every auxiliary object built from automorphic
L-functions over ℚ introduces variables that, in P_T, enter through (comb, Γ, conductor), additively by Φ.12. The
weight, the level and the spectral parameter are Γ/conductor. Family averages reduce the comb to Sato–Tate
constants. A genuinely exogenous variable in the sense of V′ must live **outside** the category of L-functions with
FE over ℚ. The only gap not killed by a theorem remains C10. Round 19 closed with no sign. L′♯ OPEN. Row D OPEN.

## 5. For the index (add in this session)

"SPEC_SIGN_OBJECT_009 (round 19, V′ exogenous auxiliary objects): X1–X5 NO-GO.
X1a/b: L′ and Rankin f×f̄. Lemma 19.1 PROVED: Λ_{f×f̄}(p^j) = log p|α^j+β^j|². Prop 19.2: 𝔞^{f×f̄} = 𝔞^ζ + 𝔞^{sym²f}
(Φ.12), subtracting = REF-D; Rankin is residue positivity (weight gap).
X1c: Hecke family averaged by Petersson with ν = weight/level. Theorem 19.3 PROVED mod. CITED: averaged comb =
Λ·min(j,2) (Sato–Tate) + O(J_{k−1}); ν enters only through Γ/conductor (excluded by Prop 18.4); a_P admits the same
extension.
X2: linear (Obs 19.4). X3b: Selberg with shift r↦r−i/4, Prop 19.5 PROVED = CA_F_002 Lemma 1; h(D) only as data.
X3c: Mayer = Z_Selberg, inherits. X4: E101_083/C-pol/C-MvN. X5: C-data/W-mom/Theorem X.
ARGUED residue: transition regime k ≍ 4πe^{2T} (Kloosterman = data over 𝔽_p, a bound and not a sign).
Do not retry averaged automorphic families (weight, level, spectral), Rankin–Selberg, or shifted Selberg without a
variable other than Γ/conductor."
