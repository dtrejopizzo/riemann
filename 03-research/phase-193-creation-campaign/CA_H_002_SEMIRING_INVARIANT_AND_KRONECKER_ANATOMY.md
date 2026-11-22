# CA_H_002 — The semiring invariant that separates ℕ from the falsifiers (Erdős rigidity), and the exact +/· anatomy of the window matrix (Kronecker line minus Haar) (seeds H5, H6; front E input)

Phase 193. Pen and paper; no numerics. no equivalence with any statement about
another object is used. P46 = Paper 46.
**No sign contact. No negative value for ζ.**

## 1. Setting (checked against P46 subsec:oneprofile, prop:AM, thm:band; CA_E_001 §0)
Profile F₀ ∈ 𝒫_{T₀}, 2T₀ < log 2, ‖F₀‖ = 1, c₀ = c_{F₀}, ĉ₀ = F̂₀² > 0, supp c₀ ⊂ (−2T₀, 2T₀), c₀(0) = 1, c₀ even.
For a real comb a on ℕ_{≥2} put v^a_n = 2a(n)n^{−½} (v = v^Λ). For finitely supported real s on ℕ: P_s(τ) = Σ s_m m^{iτ},
Arch(s) = (1/2π)∫m F̂₀²|P_s|², Div_a(s) = Σ_{kn=m, n≥2} s_ms_kv^a_n, Near_a(s) = Σ_{m≠kn} s_ms_kv^a_nc₀(log(kn/m)),
and s^T𝔸_M s = Arch(s) − Div_a(s) − Near_a(s) (prop:AM(ii)–(iii) after symmetrization; derivation in §3.1).
G = ℚ_{>0}^×, Ĝ its compact dual, ι(τ)(q) = q^{iτ}, m_Ĝ Haar probability. ν₀^ℝ := (1/2π)F̂₀²(τ)dτ (a probability measure on ℝ since
c₀(0) = ‖F₀‖² = 1), ν₀ := ι_*ν₀^ℝ on Ĝ.
(E) Euler product ⟺ Σ_{d|N}a(d) = log N; f_a := 1 ∗ a (divisor sum).

## 2. Seed H5 — the semiring invariant
**Theorem 2.1 (Erdős; CITED).** If f: ℕ → ℝ is additive (f(mn) = f(m) + f(n) for coprime m, n) and f(n+1) − f(n) → 0, then f = c·log.
(P. Erdős, *On the distribution function of additive functions*, Ann. of Math. 47 (1946), 1–20; extended by Kátai and Wirsing.)
The hypothesis couples + (the successor n ↦ n+1) and · (additivity over coprime factors); it is the cleanest +/·-genuine
characterization of the archimedean norm.

**Definition.** A comb a has the **successor property** (S⁺) if a is supported on prime powers of ℕ and f_a(n+1) − f_a(n) → 0.

**Theorem 2.2 (the separating invariant; PROVED from Thm 2.1).** (i) A comb has (S⁺) iff a = cΛ for some c ∈ ℝ.
(ii) Λ has (S⁺). The following falsifiers of P46 def:shape-ops fail (S⁺): O1, O2, O3, O5, O6 (all as combs on ℕ), O8 (frequencies not in
log ℕ), O10 (Epstein x²+5y², and every class-number > 1 Epstein), O11 (any Beurling system ≠ ℕ), O12 (every ζ_K, K ≠ ℚ), O15.
(iii) (S⁺) does not separate ζ from O4 (cΛ), O7 (quartets), O9 (ξR), O14 (symbol truncation).
*Proof.* (i) If a lives on prime powers, f_a is additive: a prime-power divisor of mn (coprime) divides exactly one of m, n. Theorem 2.1
gives f_a = c log; Möbius inversion gives a = μ ∗ (c log) = cΛ. Conversely f_{cΛ} = c log and c log(1 + 1/n) → 0.
(ii) O1, O2, O3, O5, O6 produce combs on ℕ that are either not supported on prime powers (then (S⁺) fails by definition) or are supported
on prime powers and are not a multiple of Λ (Λ1_{n≥N}, Λ + cδ_{n₀} with n₀ a prime power, Λ1_{n<n₀}, a one-weight change, a_P): (i) excludes
them. O8, O11, O15 have frequencies outside log ℕ: no successor. O12: Λ_K is supported on prime powers and, for K ≠ ℚ, is not a multiple of
Λ (at a prime q inert in a quadratic K, Λ_K(q) = 0 while Λ_K(q²) = 2log q); by (i) f_{Λ_K}(n+1) − f_{Λ_K}(n) does not tend to 0. O10: if the
log-derivative coefficients b of ζ_Q were supported on prime powers, ζ_Q = exp(Σ b(n)n^{−s}/log n) would be a formal Euler product, so the
normalized coefficients r_Q(n)/2 would be multiplicative; for Q = x²+5y², r_Q(2) = r_Q(3) = 0 and r_Q(6) = 4 (6 = 1 + 5), a contradiction.
(iii) O4 keeps the shape cΛ; O7, O9, O14 keep the comb (lem:shape-quartet; prop:shape-twist; the truncation acts on the symbol). ∎
**Remark.** The scale c in O4 is fixed by the pole at 1 (residue 1) or by the density ceiling thm:ceiling (c ≤ 1) together with Mertens;
both are archimedean/FE data. So (S⁺) + (F) separates ζ from every comb-changing falsifier, and from none of the comb-keeping ones.

**Corollary 2.3 (where H5 dies; PROVED).** Any deduction whose ζ-specific input is (S⁺) together with properties that O7 keeps (FE, Γ-factor
at conductor 1, pole, reality, the exact comb) is excluded by lem:shape-quartet: the quartet models have all of them and a witness at large
k. Hence (S⁺) can be load-bearing only through a property O7 destroys, which is the purity of the arithmetic side (no absolutely continuous
part −kβ_z), i.e. the explicit form 𝔞_T itself read with its own archimedean term (P3), (P6).

**Proposition 2.4 (how (S⁺) enters the form; PROVED).** Let w ≡ c on [0, e^{2T₀}/2], s = s_w = (m^{−½}w(m/M))_{m≤M}. For every comb a supported on
prime powers,
  Div_a(s) + Near_a(s) = 2c Σ_{2≤N<Me^{2T₀}} N^{−½} f_a(N) E^w_M(N),   E^w_M(N) := Σ_{m≤M} m^{−½}w(m/M) c₀(log(N/m)).
*Proof.* §3.1 gives Div_a + Near_a = Σ_N (s ∗ v^a)(N)E_s(N). (s ∗ v^a)(N) = 2N^{−½}Σ_{n|N, n≥2}a(n)w(N/(nM)), and N/(nM) < e^{2T₀}/2 for n ≥ 2 and
N < Me^{2T₀}; E_s(N) = 0 for N ≥ Me^{2T₀} because supp c₀ ⊂ (−2T₀, 2T₀). ∎
So on the collapse class (SPEC_B §1.3, there with a = Λ) the comb part is a Riemann sum over consecutive integers N of f_a(N) against a weight
that is smooth in N at scale ≍ T₀N. **(S⁺) is precisely the condition that makes this a Riemann sum of a smooth function**, which then
collapses by Euler–Maclaurin / ℤ-Poisson and the Tate conditions (SPEC_B Line 2; EI_002 Thm 3). For a = Λ the expression contains no prime.
This is the exact point where the semiring enters the window form, and it is non-critical: the critical cutoffs are not flat on
[0, e^{2T₀}/2] (EXP_005 §5, NUMÉRICO: r(0.5M) ≈ 0.9), so on them the comb returns through the small-divisor defects of SPEC_B Line 3 (seed
H9, retry). Q_M(1) = 2.58 > 0 with O(1) margin on the collapse class (NUMÉRICO, quoted from EXP_005).

## 3. Seed H6 — the exact +/· anatomy: Div is Haar, Near is the Kronecker defect
**Retry note (FIX 2).** The box version of Theorem 3.1 is CA_C_002 Prop 2(a)–(d) (PROVED, reviewed): on 𝕋^S, Near_M = (line − Haar)(Σ_pδ_p|P_s|²) when every near-coincidence atom is an S-unit. What this section adds: (i) the statement on the full solenoid Ĝ, with no S-unit hypothesis (non-S atoms are included automatically, since κ_a is a character polynomial on Ĝ); (ii) the anatomy Theorem 3.2 (additive-only weights × monoid-only coefficients, linear in Λ), which is the +/· classification CA_C_002 did not state; (iii) the Weyl-limit form Prop 3.3 and the tail Prop 3.4 with its [crit] reading; (iv) (K) on product vectors via CA_E_001 Thm 1. Theorem 3.1 itself is recorded as a re-derivation/extension of CA_C_002 Prop 2.
### 3.1 Comb part as a Dirichlet–archimedean pairing (PROVED)
For every s and every comb a: Div_a(s) + Near_a(s) = Σ_{m,k,n} s_ms_kv^a_n c₀(log(kn/m)) = Σ_N (s ∗ v^a)(N)·E_s(N), E_s(N) := Σ_m s_m c₀(log(N/m)).
*Proof.* prop:AM(ii): (1/2π)∫F̂₀²|P_s|² Σ_n v_n cos(τ log n) = Σ s_ms_kv_n ½[c₀(log(mn/k)) + c₀(log(m/(kn)))]; the first bracket term equals the second
after m ↔ k, and c₀ is even. Regroup by N = kn. ∎
Since c₀(0) = 1: Div_a(s) = Σ_N (s∗v^a)(N)s_N and Near_a(s) = Σ_N (s∗v^a)(N)Σ_{m≠N}s_m c₀(log(N/m)); the additive parametrization m = N + h
gives Near_a(s) = Σ_{h≠0}Σ_N (s∗v^a)(N)s_{N+h}c₀(log(1 + h/N)) — the shifted-convolution form (L2_030, retry; not reopened).

### 3.2 Theorem 3.1 (Div = Haar integral, Div + Near = line integral; PROVED)
Let κ_a(χ) := Σ_{n<Me^{2T₀}} v^a_n Re χ(n) and g_s := |P̃_s|²κ_a on Ĝ, P̃_s(χ) := Σ s_mχ(m). Then for every finitely supported real s,
  Div_a(s) = ∫_Ĝ g_s dm_Ĝ,   Div_a(s) + Near_a(s) = ∫_Ĝ g_s dν₀,   hence   **Near_a(s) = ∫_Ĝ g_s d(ν₀ − m_Ĝ).**
*Proof.* g_s = ½Σ s_ms_kv_n[χ(mn/k) + χ(m/(kn))]. m_Ĝ integrates χ(q) to 1[q = 1]: only m = kn survives (mn = k with n ≥ 2 is the same set after
m ↔ k), giving Div. ν₀ integrates χ(q) to (1/2π)∫F̂₀²q^{iτ}dτ = c₀(log q), giving §3.1. ∎
**Reading.** The Haar part sees only exact multiplicative relations (monoid-only, G1). The line part ν₀ is the archimedean profile pushed
onto the Kronecker line. Their difference has Fourier transform
  (ν₀ − m_Ĝ)^(q) = c₀(log q)·1[q ≠ 1],   supported on G*_{2T₀} := {q = a/b ≠ 1 : |log q| < 2T₀},
the rationals near 1, i.e. the **additive near-identities a = b + h**. So Near is exactly the defect of the weighted Kronecker line against
multiplicative Haar measure. (Front E's input, made an identity.)

### 3.3 Theorem 3.2 (complete +/· anatomy of the window matrix; PROVED)
For every s and every comb a,
  s^T𝔸_M s = Σ_{q∈G} [ α(log q)·N_s(q) − c₀(log q)·M^a_s(q) ],
with N_s(q) := Σ_{m/k=q} s_ms_k, M^a_s(q) := ½Σ_{m/(kn)=q or mn/k=q} s_ms_kv^a_n (finite sums), and α(d) := (1/2π)∫m F̂₀² cos(τd)dτ.
The weights α(log q), c₀(log q) depend only on F₀, on the Γ-factor and on the archimedean embedding log: G → ℝ (**additive-only**); the
coefficients N_s(q), M^a_s(q) are defined from exact relations in the monoid together with the norm weights n^{−½} (**monoid-only**).
*Proof.* Expand |P_s|² = Σ s_ms_k (m/k)^{iτ} in Arch, and use Theorem 3.1 for the comb. ∎
**Consequence (PROVED).** The +/· interplay of the window form is a pairing, Σ_q (additive-only weight at log q) × (monoid-only coefficient at q),
and the pairing is **linear in the comb**. No term of the form is +/·-genuine by itself; genuineness lives only in which points q ∈ G have small
|log q| and with which coefficients. Any inequality obtained from this anatomy by bounding termwise or by Cauchy–Schwarz is (R)(3) or lem:shape-misc;
any use of it with a non-linear input must take the non-linearity from the test s (the infimum over s), which is the minimizer channel: REF-D
(SPEC_A Lemma S; EI_003 Thm 2, symbol rigidity).

### 3.4 Kronecker–Weyl as an exact limit, and the location of the defect
**Proposition 3.3 (PROVED).** m_Ĝ = weak*-lim_{U→∞} ι_*(1_{[−U,U]}dτ/2U). Hence Near_a(s) = lim_{U→∞}∫_ℝ (g_s∘ι)(τ)[(1/2π)F̂₀²(τ) − 1_{[−U,U]}(τ)/2U]dτ.
*Proof.* For q ≠ 1, (1/2U)∫_{−U}^U q^{iτ}dτ = sin(U log q)/(U log q) → 0; characters span a dense subalgebra of C(Ĝ); g_s is a trigonometric
polynomial. ∎
This is equidistribution used as an identity, not an estimate. It shows that the defect is concentrated where (1/2π)F̂₀² exceeds the flat
density: the central cell |τ| ≲ 1/T₀ (consistent with CA_D_SYNTHESIS: row D lives on the central Nyquist cell).
**Proposition 3.4 (tail of the line measure; PROVED).** (1/π)∫_U^∞F̂₀(τ)²dτ ≍ U^{−3} as U → ∞, with constants depending on (a,b) of the profile.
*Proof.* F̂₀(τ) = (τ² + ¼)|ĝ(τ)|⁴ with ĝ(τ) = (e^{(b+iτ)a} − 1)/(b+iτ) and |e^{ba} − 1| ≤ |e^{(b+iτ)a} − 1| ≤ e^{ba} + 1, so F̂₀ ≍ τ^{−2}. ∎
**Reading (ARGUED).** A near-coincidence at integer resolution, q = (b+1)/b with b ≍ M, has |log q| ≍ 1/M, i.e. it is detected at frequency ≍ M.
The part of ν₀ beyond the integer Nyquist frequency M has mass ≍ M^{−3}. This matches the [crit] exponent λ_min(𝔸_M) = M^{−3+o(1)} (EXP_005
C1, NUMÉRICO): the criticality of problem (S) is of the size of the archimedean line mass that the integer lattice cannot resolve. This is a
size coincidence explained, not a proof of the exponent; EXP_005 gives a zero-side mechanism with an extra log M.

### 3.5 Corollary 3.5 (Kronecker-defect form of the target; REF-D, PROVED)
By CA_E_001 Theorem 1 it suffices to test product vectors s = ⊗_{p∈S}c_p. On them Div factorizes over p (rem:boxes: the Kronecker sum of local
Toeplitz matrices with symbols δ_p(θ) = 2 log p Re x/(1−x), x = p^{−½}e^{iθ}). So (eq:target) holds iff for all finite S and product s:
  (K)   ∫_Ĝ g_s d(ν₀ − m_Ĝ) ≤ Arch(s) − Σ_{p∈S}⟨c_p, D_p c_p⟩∏_{q≠p}‖c_q‖²   (with the comb's non-S atoms entering only the left side).
(K) is an exact restatement (lem:shape-restate class): the Kronecker defect of the archimedean line against multiplicative Haar, tested on
Euler-product polynomials times the comb character, is bounded by archimedean energy minus local Euler-factor energy. It is the +/· form of
problem (S). Label REF-D.

## 4. Where H5 and H6 die (summary table)
| object | +/· genuine? | (B″) | O7 | O11 | FE-gen | linear in Λ (P2) | sign content |
|---|---|---|---|---|---|---|---|
| (S⁺), Thm 2.2 | yes (Erdős: successor × additivity) | no (separates ζ) | **survives** | separated | separated | — (comb property) | none: comb-only, Cor 2.3 |
| Prop 2.4 collapse | yes | no (needs (S⁺)) | survives | separated | separated | yes (W7) | O(1) margin, non-critical class |
| Thm 3.1 / 3.2 anatomy | only as a pairing | **yes** (every comb) | survives | holds for ℚ-independent Beurling logs on their own G | holds | yes | none (coordinates) |
| Prop 3.3 / 3.4 | additive | yes | — | — | — | — | location only (central cell; M^{−3} tail) |
| (K), Cor 3.5 | yes | — | — | — | — | — | REF-D |

## 5. Self-review
1. *Theorem 2.2 is "only" Erdős + Möbius.* Yes. Its value is the table: it names the +/·-genuine property separating ζ from every
   comb-changing falsifier, including ζ_K (which (R)(10) demands), and it proves the property is blind to O4, O7, O9, O14. Erdős's theorem
   is cited, not reproved.
2. *Is (S⁺) used in the form at all?* Prop 2.4 shows exactly where: on the collapse class, f_a(N) is sampled at consecutive integers
   against a smooth weight. Outside that class the form reads a only through the small-divisor defects (SPEC_B Line 3), where (S⁺) gives
   nothing beyond a = Λ at small n.
3. *Theorem 3.1 might be a retry.* The Fourier statement (ν₀ − m)^ = c₀(log q)1[q≠1] is the same arithmetic as prop:AM(iii) and the Farey
   picture of SPEC_B; what is new is the measure-theoretic identification Div = Haar, Near = line − Haar on Ĝ, which turns front E's
   Kronecker-line input into an identity and makes the monoid/additive split of Theorem 3.2 exact. It is a coordinate system; (B″).
4. *Could the line structure (ι(ℝ) ⊂ Ĝ, Bohr–Jessen) give a sign as an exact identity?* Prop 3.3 is the only exact identity it supplies
   (Weyl limit); Bohr–Jessen value distribution concerns m_Ĝ-statistics of κ (monoid-only, G1), and CA_E_001 Thm 2 rules out product-kernel
   factorizations of the line measure. The line enters the form only through ν₀, i.e. through F₀ and Γ.
5. *Prop 3.4 reading.* Labelled ARGUED; it does not prove λ_min ≍ M^{−3}. Constants not computed.
6. *Numerics.* None run. The two NUMÉRICO values quoted (Q_M(1) = 2.58, the shape of w_opt) are from EXP_005.
7. *Equivalences.* Cor 3.5 is an internal restatement (lem:shape-restate type), not an equivalence with a statement on another object.
**Verdict.** H5: PROVED separating invariant; dies at O7 (Cor 2.3) and is non-critical where it enters (Prop 2.4). H6: PROVED exact
anatomy; (B″) and linear in Λ; its sign content is (K), REF-D. Neither is a sign step.
