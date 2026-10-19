# CA_J_002 — Griffiths/GKS: the window matrix is frustrated by a +/· cycle; FKG on the divisor lattice: Euler tests are the FKG-equality class (seeds J1, J2, J3, J9, J11, J12)

Phase 193. Pen and paper; no numerics. Setting, Lemmas J0, J0′: CA_J_000 §1.
**No sign contact. No negative value for ζ.** (Negative values below are values of the kernel 𝖡 at nonzero shifts, i.e. off-diagonal
entries of 𝔸_M, never values of the quadratic form.)

## 1. Seed J1 — Griffiths (GKS) inequalities on the integer lattice
Model: sites m ∈ {1, …, M}; the window matrix 𝔸_M enters either
 (H) as the *Hamiltonian/precision*: H(x) = ½x^T𝔸_Mx, couplings J_{mk} = −𝔸_{mk} (m ≠ k), free single-site part 𝔸_{mm} = 𝖡(0); or
 (C) as the *covariance* of a spin field.
GKS I/II (Griffiths 1967; Kelly–Sherman 1968; CITED) need ferromagnetic couplings J_{mk} ≥ 0 after a ±1 gauge ε (spin flip
x_m ↦ ε_mx_m). Ginibre, GHS, Lebowitz, FK random-cluster (J3, J9) need the same.

**Lemma 1.1 (additive block; PROVED).** 𝖡(0) > 0 (CA_E_001 Fact 0, CITED via P47/Zhu) and 𝖡 is continuous, so there is δ > 0 with
𝖡(d) > 0 for |d| < δ. Hence for m ≥ m₀ := ⌈2/δ⌉ every entry 𝔸_{m,m+h} with 0 ≤ h ≤ 2 is positive, and more generally 𝔸_{m,k} > 0
whenever |log(m/k)| < δ.

**Lemma 1.2 (multiplicative negative edge; PROVED for T₀ ≤ 0.05; PROVED under the premise + CITED for every T₀).**
(a) If 2T₀ ≤ 0.1 then 𝔸_{m,2m} = 𝖡(log 2) < −0.27 for every m (Lemma J0′).
(b) Under the premise (φ PD), 𝖡 takes negative values on a nonempty open set, hence 𝔸_{m,k} < 0 for some pair with m, k ≥ m₀ (any m₀).
*Proof of (b).* The mean lim_{D→∞}(1/2D)∫_{−D}^{D}𝖡 = ν({0}) (Wiener, CITED). By the explicit
formula (P47 thm:Z, CITED) ν is carried by zero ordinates with weights m_γĉ₀(γ), and 0 is not an ordinate (ζ(½) ≠ 0, CITED), so the mean is 0.
𝖡 ≢ 0 (𝖡(0) > 0) and continuous, so 𝖡 < 0 on an open set U. log G is dense in ℝ and log(Lm/Lk) = log(m/k), so U ∩ log G contains a
ratio m/k with m, k ≥ m₀. ∎

**Theorem 1.3 (frustration; PROVED).** (H) For M ≥ m₀ + 2 there is no gauge ε ∈ {±1}^M making 𝔸_M ferromagnetic in the Hamiltonian
sense (ε_mε_k𝔸_{mk} ≤ 0 for all m ≠ k). (C) For M large there is no gauge making 𝔸_M a ferromagnetic covariance (ε_mε_k𝔸_{mk} ≥ 0
for all m, k) — unconditionally when 2T₀ ≤ 0.1, under the premise for every T₀.
*Proof.* (H) The triangle {m₀, m₀+1, m₀+2} has three positive entries (Lemma 1.1); ε_aε_b = −1 on all three edges is impossible since
the product of the three products is (ε_{m₀}ε_{m₀+1}ε_{m₀+2})² = +1. (C) Positive entries between k and k+1 for all k ≥ m₀ force ε
constant on [m₀, M]; Lemma 1.2 gives a pair m, k ≥ m₀ in that interval (M large) with 𝔸_{mk} < 0. ∎
**Reading (+/·).** In the covariance reading the signed graph of 𝔸_M contains the cycle m → m+1 → … → 2m → m: all edges along the
additive path are positive (the + side: near-coincidence |log((k+1)/k)| small), the closing multiplicative edge (m, 2m) carries the
Euler atom and is negative (the · side). One negative edge on a cycle = frustration. So **the +/· interaction is exactly a frustrated
cycle**: the additive successor and the multiplicative doubling cannot be made simultaneously ferromagnetic. In the Hamiltonian reading
already the additive triangles frustrate (antiferromagnetic on the additive scale).
**Corollary 1.4.** GKS I/II, Ginibre, GHS, Lebowitz, Newman, FK random-cluster and switching-lemma arguments have no input for 𝔸_M in
either reading (they require an unfrustrated sign pattern). Even granted, GKS outputs entrywise sign of correlations, not 𝔸_M ⪰ 0;
and the Gaussian model of reading (H) exists only if 𝔸_M ⪰ 0 already (G0 / REF-D).
**Relation to the corpus.** G2_B8_R2 §1 reads 𝔞_T on the t-line as a ferromagnetic jump process (couplings ½K, ½v_n ≥ 0) minus a
chemical potential A_T − C₀; that is ferromagnetic *in the continuum*, and Theorem R shows non-monotonicity in the coupling. Theorem 1.3
says that in the *integer-site* picture the same object is frustrated, so the lattice tools are not available either. E78_1's numerical
frustration (different matrix) is now a theorem for 𝔸_M.

## 2. Seed J2 — FKG on the divisor lattice (ℕ, |, gcd, lcm)
For a finite set S of primes and N = (N_p), let L = L_{S,N} = {x ∈ ℤ^S : 0 ≤ x_p ≤ N_p} ≅ divisors of ∏p^{N_p}, with x ∨ y = lcm,
x ∧ y = gcd. L is a finite distributive lattice (product of chains). f: L → (0,∞) is log-supermodular if f(x∨y)f(x∧y) ≥ f(x)f(y),
log-modular if equality holds.

**Proposition 2.1 (Euler tests are the FKG-equality class; PROVED).** A positive f on L is log-modular iff f(x) = ∏_{p∈S}c_p(x_p) for
positive c_p, i.e. iff f is (the restriction of) an Euler-product test vector of CA_E_001 Thm 1. Signed product vectors are exactly the
s with |s| log-modular and sgn s a product of coordinate signs.
*Proof.* (⇐) max/min act coordinatewise, so ∏c_p(max) ∏c_p(min) = ∏c_p(x_p)c_p(y_p). (⇒) g = log f is modular. For x ∈ L write
x = ⋁_p x_pe_p, with the x_pe_p pairwise having meet 0. Modularity on elements with disjoint supports gives
g(u ∨ w) = g(u) + g(w) − g(0) when u ∧ w = 0; induction on |supp x| gives g(x) = Σ_p[g(x_pe_p) − g(0)] + g(0). Put
c_p(k) = e^{g(ke_p) − g(0)}·e^{g(0)/|S|}. ∎
**Corollary 2.2 (PROVED, from CA_E_001 Thm 1).** (eq:target) ⟺ s^T𝔸s ≥ 0 for all s on finite divisor boxes whose modulus is in the
FKG-*equality* class. So the decisive test vectors are those for which every FKG/Harris/Holley/Ahlswede–Daykin inequality *built from
the test vector alone* is an equality: lattice correlation inequalities carry no information on exactly the class that decides.

**Proposition 2.3 (no FKG measure from the kernel; PROVED).** An FKG proof of s^T𝔸s ≥ 0 needs a positive measure on L (or on L × L)
whose correlations are the form. Candidates:
(i) w(x, y) = s_xs_yφ(x − y) on L × L: signed, because φ takes negative values (Lemma 1.2) — not a measure.
(ii) |φ| or φ₊: discards the sign of the Euler atoms; the resulting statements hold for every comb with the same moduli ((B″)).
(iii) the Bochner representation s^T𝔸s = E_ν|Σ_ms_mX_m|² with X_m = m^{iτ}, τ ∼ ν/ν(ℝ): here the "spins" X_m are completely
multiplicative (X_{mk} = X_mX_k, the · structure) functions of a single real variable τ (the + structure). This *is* a covariance
representation, but it is the Gram factorization G0 (CA_G_SYNTHESIS) and presupposes ν ≥ 0, i.e. the target (REF-D). Moreover the
real spins Re X_m = cos(τ log m) are not monotone in the divisor order, so FKG does not apply to them either.
**Proposition 2.4 (Holley comparison is linear and local; ARGUED).** Holley's criterion compares two positive measures through
μ₁(x∧y)μ₂(x∨y) ≥ μ₁(x)μ₂(y). Applied to kernels from two combs a, b, the difference φ_a − φ_b = −½Σ(a − b)(n)n^{−½}[…] is linear in the
comb (CA_H_002 Thm 3.2), and on the decisive class (Prop 2.1) the criterion separates over coordinates, i.e. compares local Euler
factors one prime at a time: (B′)/(R)(5) local, CA_F_001 Prop 3 (bare local positivity false at every p).
**+/· test (PRINCIPIO RECTOR).** The lattice (ℕ, |) is monoid-only: it is isomorphic to the divisor lattice of every free commutative
monoid, so purely lattice statements survive O11/O12 (G1). The + enters only through φ = 𝖡∘log, i.e. through the anatomy of
CA_H_002 Thm 3.2 (additive weight × monoid coefficient, linear in Λ). FKG adds a lattice inequality on top of that anatomy and, on the
decisive class, the lattice inequality is an equality (Cor 2.2). **Verdict J2: NO-GO as a sign step (PROVED: Prop 2.1, Cor 2.2,
Prop 2.3; ARGUED: Prop 2.4).** J11, J12 folded here.

## 3. Screens
| item | REF-D | (B″) | O7 | O11/O12 | [crit] | sign content |
|---|---|---|---|---|---|---|
| Thm 1.3 frustration | no | (a) uses the atom at 2; (b) generic under premise | survives | survives | no | NO-GO for GKS-family inputs |
| Prop 2.1 / Cor 2.2 | Cor 2.2 is an exact restatement | yes | survives | survives | no | coordinate fact: decisive class = FKG equality |
| Prop 2.3 | (iii) REF-D | (ii) B″ | — | — | — | NO-GO for FKG measures |
| Prop 2.4 | — | linear in Λ | — | — | — | local, (R)(5) |

## 4. Self-review
1. *Lemma 1.2(b) uses zeros.* Only ζ(½) ≠ 0 and the explicit-formula form of ν, to show that 𝖡 has a negative value somewhere; used to
   refute a gauge, not to deduce the sign. For 2T₀ ≤ 0.1 the proof is unconditional and explicit.
2. *Is frustration avoidable by choosing a sub-family of sites?* GKS on a sublattice of sites where 𝔸 is unfrustrated (e.g. only
   multiplicatively independent sites) tests 𝔸 on a subspace; positivity there is a restriction, not the target, and every site set
   containing m, …, 2m for some m ≥ m₀ is frustrated (C). The sites that see near-coincidences (residue R9, problem (S)) are exactly
   the frustrated ones.
3. *Prop 2.1 is elementary.* Yes. Its use is Cor 2.2: it names CA_E_001's decisive class in lattice language and shows FKG is blind on it.
4. *Could a non-FKG lattice inequality (e.g. Ahlswede–Daykin with four different functions built from s and φ) work?* AD needs four
   nonnegative functions; any function built from φ inherits negative values or loses the sign (Prop 2.3 (i)/(ii)). With φ only in
   the weights and s in the functions, the AD conclusion is an inequality between lattice sums of s (no Λ): (B″).
5. *Numerics.* None run.
**Verdict.** J1/J3/J9: NO-GO (frustration, PROVED). J2/J11/J12: NO-GO as sign step; PROVED coordinate fact (Euler tests = FKG equality class).
