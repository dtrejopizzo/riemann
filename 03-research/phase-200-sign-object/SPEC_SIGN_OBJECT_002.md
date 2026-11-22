# SPEC_SIGN_OBJECT_002: v2 specification of the sign object (quotient structure) and three candidates (phase 200, stage 2, round 2)

Synthesizer. Pen and paper. There is only exact integer or rational arithmetic (tables of c_N, y_k, S_n(1) at μ = 15)
and one digamma root (NUMERICAL, mpmath). Row D, L′♯ and (★★) are treated as independent goals. No
equivalence with any other statement is invoked.
NO-GO / NUMERICAL. **No sign is proved.**

**Read.**
- Phase 200: SPEC_001, AUDIT_200_SPEC_001, K1_OSG_001, K3_GAMMA_001, LEDGER_L1…L5 (seeds and negative space).
- Phase 199: AUDIT_CONSTRAINTS_001, PROOF_L_SHARP_FF_001, PROOF_L_SHARP_GG_001, MORI15_EXTREMAL_001.
- Paper 46: def:ext, thm:ext-half, rem:ext-killing, prop:ext-gauge, thm:ext-lattice, prop:ext-grouped.
- ROUTES-TRIED index (full README, "Phase 200" section).

**Index entries touching this round.**
- **E_001**: Thm E.1, which groups by ratio m/n; Thm E.5, "indefinite classes one by one".
- **F_001**: interference between ratio classes.
- **J_001**: Thm J.2, no Hilbert kernel; AUDIT_14 note: "Toeplitz-in-log symbol (mn)^{−½}c_r̃(log n/m) PD, excluded by
  N_018".
- **INV_H_001**: "finite Ramanujan = regrouped Möbius (Beurling-generic)"; do not retry Ramanujan, Vaughan nor Poisson-on-ℤ
  **as a linear identity**.
- **INV_C**: pair counts, Farey, Möbius.
- **INV_J**: large sieve and Selberg as upper bounds.
- **GG_001**: renormalization.
- Lemma M and H_001: flows in T, restriction 11.

Each candidate states its new reason versus the closest matching entry.

**Notation** (FF_001, GG_001).
- μ ≥ 5, a = T = ½log μ, g even in the core on (−a, a), A = A(g) = ∫g e^{x/2} (= B, g even).
- λ_d := μ(d)1_{d<μ} (strict convention m < μ, AUDIT_200 §1).
- c_N := Σ_{d|N} λ_d. Then c_1 = 1, c_N = 0 on [2, μ) and c_N = −μ(N) on [μ, 2μ).
- D_μ(s) := Σ_{N≥μ} c_N N^{−s} = ζ(s)M_μ(s) − 1.
- Ψ̌_c := Σ_{N≥μ} c_N N^{−½} τ_{log N} g.
- c_g(u) := ∫g(x)g(x+u)dx, supported on [−log μ, log μ].
- v_n = 2Λ(n)n^{−½}.
- m(t) = Re ψ(¼ + it/2) − log π.

---

## A. Specification v2

### A.0 The Toeplitz form in quotient coordinates (what can be proved)

**Lemma T.1 (Fourier version, PROVED given Guo L4.3–4.4, CITED).** Let g be in the core with A(g) = 0. Then:
- (a) 𝓕Ψ̌_c(t) = ĝ(t)·D_μ(½ + it), with 𝓕Ψ(t) = ∫Ψe^{−itx}.
- (b) A(Ψ̌_c) = 0.
- (c) The equality
  W_T(g) = (1/2π)∫_ℝ |ĝ(t)|²|D_μ(½+it)|² m(t) dt − Σ_{n≥2} v_n·(1/2π)∫_ℝ |ĝ(t)|²|D_μ(½+it)|² cos(t log n) dt,
  holds with each integral absolutely convergent and the sum over n absolutely convergent.

*Proof.*
1. Ψ̌ = Ψ̌_c + Φ̌_{φ₀}. By GG.0 with A = 0, φ₀ ∈ 𝒢₀ is radical (prop:ext-gauge), so W_T(g) = 𝒲[Ψ̌] = 𝒲[Ψ̌_c]
   (thm:ext-half). Ψ̌_c = Ψ̌ − Φ̌_{φ₀} inherits Guo's e^{−3x/2} bound and has support at x > T. Hence 𝓛Ψ̌_c(s) = ∫Ψ̌_c e^{−sx}
   is holomorphic on Re s > −3/2.
2. For Re s > ½, summing term by term, 𝓛Ψ̌_c(s) = D_μ(½+s)𝓛g(s). The only possible pole of the right-hand side on
   Re s > −3/2 is at s = ½, with residue ∝ M_μ(1)𝓛g(½) = M_μ(1)·B(g) = 0. By uniqueness of the continuation, the identity holds
   on the whole strip. At s = it one obtains (a).
3. At s = −½ one obtains A(Ψ̌_c) = D_μ(0)·A(g) = 0. Thus 2A(Ψ̌_c)B(Ψ̌_c) = 0: the polar term disappears, giving (b).
4. (c) is def:ext with c_Ψ(u) = (1/2π)∫|𝓕Ψ|²e^{iut}. The sum over n converges because |c_Ψ̌(log n)| ≤ Cn^{−3/2}. □

For A ≠ 0 one adds the rank-one row κψ̌, κ = −2AM_μ(1) (GG.0). Everything that follows is stated for A = 0, and the rank-
one row is treated separately (P1).

**Corollary T.2 (reading in quotients; FORMAL except on finite sums).** Expanding |D_μ|² = Σ_{N,N′} c_N c_{N′}(NN′)^{−½}
(N′/N)^{it} one obtains
 W_T(g) "=" Σ_{N,N′≥μ} c_N c_{N′}(NN′)^{−½} 𝒯_g(log N′/N),
 𝒯_g := c_g ∗ ν, with ν = ν_∞ − Σ_n (v_n/2)(δ_{log n} + δ_{−log n}).
Here ν_∞ is the archimedean part (b_∞δ₀ + Lévy in principal value), with Fourier transform m(t).
- The identity is exact for each finite truncation, by bilinearity and translation invariance of 𝒲 (PROVED).
- It is **not** exact as a double series: Σ c_N²/N ≥ Σ_{p≥μ} 1/p = ∞ (GG §2(b), PROVED). The truncation boundary (GG.1's
  R_X cluster) does not go to 0 in L²: |c_N| ≤ d(N) and the translates cancel only on the set.
- **The rigorous meaning of "Toeplitz form in quotients" is T.1**, with effective symbol |D_μ(½+it)|²·[m(t) − Σ_n v_n cos(t log n)].

**Which part of 𝒯 is archimedean and which is the comb.**
- 𝒯_∞ = c_g ∗ ν_∞ has transform |ĝ|²m. **It is not positive.** m is strictly increasing in t > 0, because
  ∂_t Re ψ(¼ + it/2) = Σ_k (t/2)·2(k+¼)/((k+¼)² + t²/4)² > 0 (PROVED). Also m(0) = ψ(¼) − log π = −5.372 and m has a unique
  positive root t₀ = 6.28984 (NUMERICAL). The archimedean part is negative for |t| < t₀, and in the extremal it is the large
  negative piece: Γ_ℝ −5.372, MORI15. **Correction to the target:** "archimedean (positive)" is false. The only positive
  archimedean part is the one above t₀.
- 𝒯_Λ(s) = −Σ_n (v_n/2)[c_g(s − log n) + c_g(s + log n)]. The atom n couples a pair (N, N′) iff N′/N ∈ n·(μ^{−1}, μ), and
  weighs it by c_g(log(N′/(nN))). Its maximum c_g(0) = ‖g‖² is reached on the **exact sub-lattice** Λ_n := {(N, nN) : N ≥ μ}. Since nN ≥ N ≥ μ,
  the gap never trims Λ_n: the cutoff at μ acts only on N.

**Lemma T.3 (exact alignment = count on a lattice; PROVED).** Let n ≥ 1. For Re s > 1,
 Σ_{N≥μ} c_N c_{nN} N^{−s} = ζ(s)·S_n(s) − c_n,
 S_n(s) := Σ_{d,e<μ} μ(d)μ(e)·[d, e/(e,n)]^{−s} (finite sum).

*Proof.* c_N c_{nN} = Σ_{d|N, e|nN} λ_dλ_e. Also e | nN ⟺ e/(e,n) | N. The sum over N ≥ 1 of N^{−s} over multiples of
L = [d, e/(e,n)] is L^{−s}ζ(s). The term N = 1 is c_1c_n = c_n, which is 0 if 2 ≤ n < μ. Terms with 2 ≤ N < μ are
zero by the gap. □

**Here is where the arithmetic enters.** The factor ζ(s) is *the count of the points of the lattice L·ℤ in ℕ*: a_n ≡ 1 in its
crudest form. The Möbius part is a finite Dirichlet polynomial S_n.
- **Selberg (CITED, classical):** 1/[d,e] = (de)^{−1}Σ_{k|(d,e)}φ(k). Hence
  S_1(1) = Σ_{k<μ} φ(k)y_k² ≥ 0, with y_k := Σ_{k|d} λ_d/d = (μ(k)/k)·M̃_k(μ/k).
  **The y_k are exactly the coefficients 𝖼_{b/a} of prop:ext-grouped** (with a = k). The "mean" of c_N is y_1 = M_μ(1), and its
  "mean square" is S_1(1).
- For general n, S_n(1) = Σ_k φ(k)·y_k·z_k^{(n)}, with z_k^{(n)} := Σ_{e : k | e/(e,n)} λ_e·(e,n)/e. **All classes n share
  the same diagonal base k.** This is the coupling between classes that idea (i) was looking for. It is exact (PROVED) and is a
  bilinear form, not a sum of squares per class. This is consistent with E.5.
- For prime p with p ∤ N, N ≥ 2: **c_{pN} = c_N − c_N^{(μ/p)}**, where c^{(Y)}_N := Σ_{d|N, d<Y} μ(d) (PROVED: the divisors of pN
  are d and pd with d | N). The class p links level μ with level μ/p.

**Exact data at μ = 15.**
- y_1 = −89/15015, y_2 = −17/105, y_3 = −1/6, y_5 = −1/10, y_6 = 1/6, y_7 = −1/14, y_10 = 1/10, y_11 = −1/11, y_13 = −1/13,
  y_14 = 1/14. The remaining y_k (k < 15) are 0.
- S_1(1) = Σφ(k)y_k² = 0.432234, of which 0.4322 come from k ≥ 2. That is: mean ≈ 0 and variance ≈ 0.43.
- S_2(1) = S_4(1) = 0.154645, S_3(1) = 0.269131, S_5(1) = 0.289843.
- The expansion c_N = Σ_k y_k c_k(N) was verified for N < 400.
- The rule c_{pN} was checked at (33, 66) and (39, 78): c^{(7.5)} = 0, so c_{2N} = c_N = −1 (these are the K1 §3 pairs). Also at
  (15, 30): c^{(7.5)}_{15} = −1, so c_30 = 0 (directly: μ(15) + μ(30) = 0).
- **Observation:** S_4 = S_2 because λ is square-free. The sub-lattice of class 4 weighs the same as that of class 2 even though
  μ(4) = 0. The class weight is set by Λ(4) = log 2, not μ(4). This is another argument against K2's "cocycle μ(n)".

### A.1 Idea (ii), made exact: NO-GO (PROVED)

By F4 (CA_M, PROVED), m(t) + 2Re(ζ′/ζ)(½ + it) = 0 for every real t outside the ordinates. In T.1 the series Σ_n v_n cos(t log n)
does not converge on the line. The total symbol m − Σv_n cos(t log n) is, as a distributional boundary value from Re s > ½, 2Re ξ′/ξ
plus the polar terms. On the line it is **zero as a function**: all its mass is singular and sits on the ordinates of zeros.
This is exactly rem:ext-killing(iii): W_T(g) = Σ_ρ Φ_Ψ̌(ρ)Φ_Ψ̌(1−ρ).

Moreover, **D_μ(ρ) = ζ(ρ)M_μ(ρ) − 1 = −1 at every zero**. There |D_μ|² = 1: the mollifier disappears exactly where the symbol
lives, and the exterior form becomes the zero-side window form (PROVED, one line).

No "discrete archimedean part" remains. The poles of Γ_ℝ cancel against the trivial zeros inside ξ. **(ii) is a
reformulation of the zero side**, excluded by P4 (Bochner blind) and by cor:void C_zeros. The useful output is negative: *the
square |ζM_μ − 1|² cannot be the 𝒫 of P3, because its symbol is null except at the zeros.*

### A.2 Properties P1–P9 (v2)

**P1. Exterior and gauge-invariant.** Q_μ depends on r only modulo 𝒢̄, and the rank-one row κψ̌ (A ≠ 0) is treated as
gauge: GG.0, polar ≡ 0 at A = 0.
- Origin: restriction 17; K1 §3 step 4 (Müntz: the Hankel halves are not gauge-invariant).
- Test: at f*, with minimal gauge (M = 28) and with φ = 0 (jump leak 0.0645), Q_μ must give the same.

**P2 (resolved versus P5). Post-cancellation scale measured against the escape.** Each piece of 𝒫 and of ℛ is gauge-invariant and
satisfies |piece(g)| ≤ C μ^{A}·ℓ(g), with ℓ = 2dist²(r, 𝒢̄).
- Test at μ = 15: ℓ(g*) = (4.4–8.5)·10⁻⁷⁰ and W_T(g*) = 4.763·10⁻⁷⁰. Every piece must be ≤ 10³·ℓ* at g*.
- **New consequence.** The FF.1 translates on their own are **not** post-cancellation coordinates: at g* the translates and the
  gauge mirror cancel to 35 digits in amplitude (K1 §4). Any decomposition of 𝒲[Ψ̌_c] into pieces of pairs (N, N′), into
  classes n, or into modes k has pieces of O(1)·‖g‖² and violates P2.
- Therefore, **𝒫 must be a square of a functional that vanishes on the extended radical** (gauge + summation-image
  translates), not a square of the c_N nor of the translates.

**P3 (new). Free positivity NONlinear in the comb, false in the identity for the falsifiers.** Q_μ = 𝒫 − ℛ, where:
- (a) 𝒫 = ‖𝔏·‖² or a count, built with data **quadratic or of higher degree** in the arithmetic: products λ_dλ_e, counts of
  the lattice L·ℤ, additive characters mod k. It cannot be a kernel fixed only by Γ_ℝ or by the symbol (this excludes
  Bochner-Lévy, restriction 4, and K1's CM square).
- (b) The identity Q_μ(ι r) = W_T(Ef) must be **false as an identity**, not merely as a bound, for:
  - DH: DH's summation image has conductor 5 and a two-L mirror, and the radical identity of ζ·M_μ does not exist.
  - cΛ with c < 1: ζ^c has no Poisson mirror and FF.1/GG.1 fail at the radical step (GG §4, ARGUED). It must be proved
    PROVED for the concrete object.
  - Beurling: there is no lattice L·ℤ nor additive characters, so T.3 loses its counting factor.
- (c) a_P shares FF.1 (GG §4, PROVED). Hence a_P's separation must appear **in 𝒫 or in ℛ**, not in the identity.

**P4. Orientation.** Half-space positivity with carrier inversion between sectors.
- Test: in the odd sector the positive carrier is prime 2 (+0.340) versus Γ_ℝ-Lévy (−0.304).

**P5 (redefined). Auxiliary anatomy and separation of a_P.**
- The object's identity must *refine* the four-piece anatomy −5.3722 + 3.9164 + 1.5190 − 0.0632 of MORI15, but that
  anatomy is an *auxiliary* identity (O(1) pieces) and not that of Q_μ. This removes the contradiction with P2.
- Added as a test: the object gives a different value at a_P than at Λ already in the block N ∈ [μ, 2μ), where c_N = −μ(N) and c^P_N
  differ at N = p·(…).

**P6 (corrected). Falsifiers evaluated at their own extremal r_F.**
- cΛ with c > 1: Q^{F}(r_F) < 0 (Theorem B, cor:ext-cfals; test at μ = 15 along the line c).
- cΛ with c < 1, Beurling, DH: the identity of P3(b) fails. The object cannot be "more positive" there: either it is undefined, or its
  identity is false. There is no prediction at r*.
- a_P: Q^{a_P}(r_{a_P}) < 0 by the CERT_FALSIFIERS battery (certified deletions).

**P7: REMOVED.** It was the output (REF-D, AUDIT_200 §2). The form of the output moves to each candidate's "target theorem".

**P8. Index 4 (test, not a property).** The object must explain, without assuming it, that the extremal's repair follows ψ₄
(a₄/a₀ = −1.6466, |a_{4j+2}| ≤ 6·10⁻³⁸, W/(1 − λ₄) = 4.08).

**P9 (new, from R-K1). Quotient structure.**
- The object acts on pairs (N, N′) with N′/N ≈ n, with coefficients c_N c_{N′} and weights 𝒯_g(log N′/N). It never acts on
  products NN′. The gap protects products, not quotients (K1 §3 step 2).
- The arithmetic enters through the **exact sub-lattice Λ_n = {(N, nN)}** and its series ζ(s)S_n(s) (T.3), and through the
  coupling between classes in the common diagonal base k (Selberg).
- **Against the index:** E.1, F and J read the ratio classes on dilates of r (before cancellation: Möbius lines of
  size 10³³, restriction 25). P9 reads them on the post-cancellation integer sequence (c_N), whose diagonal base (y_k) is finite and
  known in closed form.

**Compatibility with the hard restrictions.**
- 1: the carrier is exterior.
- 2: P3(b), a step false for the falsifiers.
- 8: J.2. No Hilbert kernel; T.1 is symmetric Toeplitz.
- 12: it is not Eψ₀ + repair.
- 17: P1.
- 24(a,b): the Möbius lattice is absorbed into c_N.
- 4 (hard): P3(a).
- 19(a): T.1 is an exact identity, not a stationary phase.
- R-K1: P9.

---

## B. Three candidates on the quotient structure

### Q1: Selberg form of the quotient lattice (SQ), with variance as 𝒫

**1. Definition.** Work in T.3's common diagonal base.
- For g with A(g) = 0 and k < μ square-free, the Ramanujan mode of the exterior datum is
  Ψ̌^{(k)} := Σ_{N≥μ} c_k(N)N^{−½}τ_{log N}g, with c_k the Ramanujan sum.
- By the finite expansion c_N = Σ_{k<μ} y_k c_k(N) (PROVED: 1_{d|N} = d^{−1}Σ_{k|d}c_k(N)), Ψ̌_c = Σ_k y_k Ψ̌^{(k)}.

**Lemma SQ.0 (PROVED given Guo L4.4).** The complete comb R_k := Σ_{N≥1}c_k(N)N^{−½}τ_{log N}g equals
Σ_{d|k}μ(k/d)d^{½}τ_{log d}Z_g, with Z_g := Σ_j j^{−½}τ_{log j}g.
- Z_g is the (mirrored) summation image of H(u) = u^{−½}g(log u). H is admissible if A(g) = 0, because Ĥ(0) = 2A. That is why Z_g is
  radical.
- 𝒲 is translation-invariant, so every translate of a radical vector is radical, and R_k is radical.
- Therefore **Ψ̌^{(k)} ≡ −F_k modulo the radical**, with F_k := Σ_{1≤N<μ}c_k(N)N^{−½}τ_{log N}g (a **finite** sum, quotients N′/N < μ).
- Also Σ_k y_k F_k = g, by the gap: it is the "Ramanujan resolution" of the window function.

The object is the finite Gram matrix 𝔅_{kk′}(g) := 𝒲(F_k, F_{k′}) (of size at most μ × μ), with W_T(g) = y^T𝔅(g)y. 𝔅 is a
Toeplitz quotient form **inside** the index N < μ: the window atoms n < μ pair (N, nN) with N, nN < μ, exactly what the
gap was making invisible exteriorly.

Set 𝒫 := Σ_{k≥2} φ(k)y_k²·β_k(g) and ℛ := 𝒫 − y^T𝔅y, with β_k(g) := 𝔅_{kk}/φ(k).

**2. Target theorem (OPEN).** There exists a decomposition 𝔅 = Φ^{½}(B_diag + E)Φ^{½}, with Φ = diag φ(k), such that:
- (a) B_diag ≥ θ·(escape norm by modes), and E vanishes on the aligned sub-lattice: for (n, k) = 1, c_k(nN) = c_k(N) (PROVED,
  classical). The class n coprime to k does not couple distinct modes on average.
- (b) |E| ≤ (1 − θ)B_diag by **identity**: the Ramanujan sums are orthogonal on average, with the average of c_kc_{k′} equal to
  φ(k)δ_{kk′}, and the error of the average is a lattice count with an explicit boundary term.

Corollary: W_T(g) ≥ θΣφ(k)y_k²β_k. The output is the **weighted Selberg variance** (a quadratic square in the Möbius
arithmetic).

**3. Exact Λ and falsifiers.**
- a_n ≡ 1: T.3's ζ factor and the radicality of Z_g (Poisson over ℕ).
- Residue 1: mode k = 1 carries the mean y_1 = M_μ(1), and A = 0 removes the polar row.
- Γ_ℝ: it sits in 𝒯_∞ inside 𝔅.
- Aliasing: N < μ ⟷ u ≈ λ/N.
- **cΛ with c < 1:** Z_g is not radical for the form of cΛ (no mirror), so SQ.0 is false in the identity.
- **Beurling:** there is no radicality of Z_g. Note: the Ramanujan expansion *is* Beurling-valid as a Möbius regrouping
  (INV_H). The failure for Beurling comes **only** from SQ.0.
- **DH:** the radical is DH's image, not Z_g, so SQ.0 is false.
- **a_P:** the radical is Z^{P}_g (ζ_P). R_k is no longer radical and a defect appears in mode k = p: R_p − R_p^{P} ∝ τ_{log p}Z_g.
  This is the separation required by P5.

**4. Index and new reason.**
- Closest entries: INV_H_001 ("finite Ramanujan = regrouped Möbius"; NO-GO 𝓒_H, which are additive identities used
  **linearly** on the window vector (v_n)_{n<N}); INV_J (Selberg as upper bound); E.5 (indefinite classes).
- **New reason stated:**
  - (1) Ramanujan is not used as a linear identity for Λ, but to resolve the window function g into modes whose exterior
    complement is radical (SQ.0). That resolution did not exist.
  - (2) The candidate positivity is the Selberg diagonalization of the **quadratic** form in λ_d, i.e. an equality and not an
    upper sieve bound. It evades J2 of INV_J, which concluded "Selberg only gives upper bounds" for sieves over Λ(n)Λ(n+h).
  - (3) The ratio classes of E.5 are the rows of 𝔅 in the quotient basis. SQ switches to basis k, where classes coprime
    to k are invariant. That is the cancellation between classes demanded by restriction 7, which E.5 did not have.

**5. Test at μ = 15 (against MORI15).**
- Compute 𝔅(g*), a 10 × 10 matrix over k ∈ {1, 2, 3, 5, 6, 7, 10, 11, 13, 14}, with g* (σ ≈ 0.21) and Mori's form (A + J).
- Control datum: y^T𝔅y = 4.763·10⁻⁷⁰.
- **Death prediction (P2):** the entries 𝔅_{kk}(g*) are O(1). F_k is a fixed combination of translates of g* with coefficients
  |c_k(N)| ≤ φ(k), with no cancellation. So 𝒫(g*) = Σφ(k)y_k²β_k ≈ 0.43·O(1) ≫ ℓ*, and ℛ must cancel 𝒫 to 70 digits. **If
  no block of 𝔅 is ≲ ℓ*, SQ violates P2 and dies as a sign object.**
- It survives only if 𝔅 has an almost-null, structured vector (the radical of the form restricted to span{F_k}) whose complement
  gives pieces ≍ ℓ.

**6. First lemma and risk.** *Lemma SQ.1:* compute exactly the kernel of 𝔅 in the limit A = 0 and check whether y is at
distance O(ℓ^{½}) from it by identity (not numerically).
- **Risk: high.** The resolution is pre-cancellation (P2). Most likely SQ.1 reduces it to "ker 𝔅 ∋ y modulo escape", which is
  REF-D.
- Permanent value: SQ.0 and T.3 are PROVED tools of P9.

### Q2: ladder of levels by prime class (discrete renormalization μ → μ/p on the sub-lattice Λ_p)

**1. Definition.** By T.3 and the rule c_{pN} = c_N − c_N^{(μ/p)} (p ∤ N), the aligned sub-lattice of class p links the level-μ datum
with the level-μ/p datum.
- For Y ≤ μ define Ψ̌^{[Y]} := Σ_{N≥Y} c^{(Y)}_N N^{−½}τ_{log N}g, the exterior with a level-Y mollifier (gap [2, Y)).
- Define the **class operator** 𝒟_p: (𝒟_pΨ)(x) := p^{½}Ψ(x + log p) restricted to the p ∤ N part.
- The identity (PROVED, by T.3) is: the projection of 𝒟_pΨ̌^{[μ]} onto the translates with p ∤ N equals that same part of
  Ψ̌^{[μ]} − Ψ̌^{[μ/p]}.

The object is the Gram matrix of the nested family 𝔊_{YY′} := 𝒲(Ψ̌^{[Y]}, Ψ̌^{[Y′]}), with Y ∈ {μ/d : d | P_μ, d < μ}.

**2. Target theorem (OPEN).** A **ladder identity**:
 W_T(g) = 𝔊_{μμ} = Σ_p (v_p p^{−½})·(𝔊_{μμ} − 𝔊_{μ,μ/p})·‖g‖²-weights + (non-prime classes) + 𝒜-part.
Together with it, a **ladder positivity**: 𝔊_{μμ} − 2𝔊_{μ,μ/p} + 𝔊_{μ/p,μ/p} = 𝒲[Ψ̌^{[μ]} − Ψ̌^{[μ/p]}] is a Weil
square on a **post-cancellation** datum. The difference of two mollifiers has coefficients Σ_{d|N, μ/p≤d<μ}μ(d), supported
on N with a divisor in [μ/p, μ), which is the Erdős band of divisors in an interval.

Output: W_T ≥ (count of N with a divisor in [μ/p, μ)) × (escape weight), by induction on μ. Lemma M (λ_A nonincreasing in T, PROVED)
is the direction of the monotonicity.

**3. Exact Λ and falsifiers.**
- The classes p appear with weights v_p and the classes p^k with the same S (S_4 = S_2): Λ(p^k) = log p, which is a_n ≡ 1 via Λ ∗ 1 = log.
- The ladder uses that the levels μ/p **are again mollifiers of ζ**, i.e. that c^{(Y)} be the truncated inverse of the
  same ζ. For a_P the levels are those of ζ_P and at step p the operator 𝒟_p does not exist (a_P(p·) = 0). Separation PROVED as
  an identity.
- cΛ with c < 1 and Beurling: there is no FF.1 at any level.
- DH: the levels would be those of L_DH, whose inverse does not satisfy the rule c_{pN} (not multiplicative).

**4. Index and new reason.**
- Closest entries: GG_001 (single-level renormalization; NO-GO as a sign mechanism because the sign factor is ν̂);
  H_001 and restriction 11 (flows in T); Lemma M; KK (Grönwall).
- **New reason:**
  - (1) It is neither a flow in T nor a derivative: it is a **discrete** identity linking two levels through the **exact
    quotient sub-lattice** Λ_p. This is not in GG (a single M_μ) nor in H (a derivative in c with no lattice structure).
  - (2) The proposed positivity is that of 𝒲 on the **difference of mollifiers**, which has arithmetic support (divisors in
    [μ/p, μ)). It is not a virial of the minimizer. If it were, it would clash with restriction 11 and die.

**5. Test at μ = 15.** The levels μ/p are 7.5, 5 and 3 (p = 2, 3, 5).
- For p = 2: c^{(7.5)} has a gap [2, 7.5).
- K1's pairs (22, 44), (26, 52), (33, 66), (39, 78) fall in class p = 2. With T.3 one predicts exactly what part of their
  weight passes to level 7.5: c^{(7.5)}_{33} = c^{(7.5)}_{39} = 0, so those pairs stay whole at level 15. In contrast
  c^{(7.5)}_{15} = −1, so the pair (15, 30) is transferred whole.
- Datum to compare: the resonance (1, 2) of AUDIT_16 §6 (−0.481 W*) should equal the contribution of step 2. **If step
  2 does not reproduce −0.481 within a factor of 2, Q2 dies.**

**6. First lemma and risk.** *Lemma Q2.1:* state and prove the exact ladder identity for p = 2 (including the classes p | N
and the boundary N ∈ [μ/2, μ)), and decide whether Ψ̌^{[μ]} − Ψ̌^{[μ/2]} is a post-cancellation datum in P2's sense, with amplitude ≍ ℓ^{½}
at g*.
- **Risk:** Ψ̌^{[μ/2]} is built with the same g, whose support (−a, a) exceeds the level-μ/2 window. It is not the exterior of a
  function admissible at that level, and the translates with μ/2 ≤ N < μ enter (a − log 2, …), overlapping the window. If the
  radicality of level μ/2 fails (most likely), the ladder has an O(1) boundary term and Q2 reduces to C6 (Möbius correlation in
  [μ/2, μ)).

### Q3: (S⁺) on shifts: exact singular series of the near-coincidences N′ = nN + h

**1. Definition.** The near-coincidences that atom n sees outside the sub-lattice are N′ = nN + h with h ∈ ℤ, |h| < nN(μ − 1). By the
Ramanujan expansion in **additive** characters, c_k(N) = Σ_{(j,k)=1}e(jN/k) (PROVED, classical), so c_N c_{nN+h} is written
with phases e(jh/k′). The average over N with a smooth weight is
 𝔖_n(h) := Σ_{k,k′<μ} y_ky_{k′} Σ_{(j,k)=1,(j′,k′)=1, j/k + nj′/k′ ∈ ℤ} e(j′h/k′),
a finite **singular series**, exact for periodic weights (PROVED: the average of e(αN) over N is [α ∈ ℤ]).

The object is the shift function h ↦ 𝔖_n(h) and its Bochner form on ℤ. For n = 1:
 𝔖_1(h) = Σ_k |y_k|²c_k(h),
which is **positive definite on ℤ** since it is a combination of additive characters with weights y_k² ≥ 0 (c_k(h) is a sum of characters). That is a free square, and
**quadratic** in the Möbius arithmetic (satisfies P3(a)).

**2. Target theorem (OPEN).** One must prove a Poisson identity in N for the Toeplitz form in quotients, with weight
w_{n,h}(N) = N^{−½}(nN + h)^{−½}c_g(log((nN+h)/(nN))):
 W_T(g) = Σ_n Σ_h 𝔖_n(h)·∫w_{n,h} + 𝔈_Poisson.
The nonzero frequencies of the error term must be controlled **by identity**. One candidate is FF.1's Poisson mirror applied to
the variable N, which leaves 𝔈 = a form of the same type at the level of the mirror.

Positivity: Σ_h 𝔖_1(h)ĉ(h) ≥ 0 for every ĉ of positive type (Bochner on ℤ). The classes n ≥ 2 couple to n = 1 via (S⁺):
- Erdős (1946): an additive function with f(N + 1) − f(N) → 0 is c·log.
- Here the continuity under successors is read at h = 1: 𝔖_n(1) against 𝔖_n(0).

Output: a Bochner form on ℤ (square) plus a count of pairs (N, nN + h) on the lattice.

**3. Exact Λ and falsifiers.**
- The **additive** structure of ℕ (h ∈ ℤ and characters e(jN/k)) is precisely what Beurling lacks. Q3's identity does not exist for
  Beurling: it is false in the identity, not in the bound (satisfies P3(b)).
- cΛ with c < 1: c_N does not change, but the identity W_T = Σ𝔖·∫w uses FF.1 (radicality), which fails.
- DH: fails for the same reason (it is not ζ·M).
- a_P: the weights y^{P}_k change at k = p (inverse of ζ_P). One must show 𝔖^P_1(h) ≠ 𝔖_1(h) at h ≡ 0 (mod p).
- (S⁺) separates ζ from O1–O6, O8, O10–O12 and O15, but not from O7 (index, phase 193). The O7 test remains open.

**4. Index and new reason.**
- Closest entries: INV_H ("do not retry Poisson-on-ℤ as an identity"; class 𝓒_H, **linear** use on the window vector);
  INV_J (additive correlations Λ(n)Λ(n+h), lower bound forbidden); phase-193 README H ((S⁺) as a separating invariant, not an
  inequality); seed L3 S8 ((S⁺) plus Markov as an inequality, never pursued).
- **New reason:**
  - (1) The correlations are not of Λ (C6, inaccessible) but of the **truncated coefficients c_N** (divisors of level < μ), whose
    correlations are **finite and exact** singular series. It is the difference between Hardy–Littlewood (open) and the correlation of
    a truncated Λ_R (computable).
  - (2) The use is quadratic (Bochner in h with weights |y_k|²), not linear. It evades 𝓒_H.
  - (3) (S⁺) enters as a **coupling between classes n** via h = 1, not as a separator.

**5. Test at μ = 15.**
- 𝔖_1(h) = Σ_k y_k²c_k(h), with the exact y_k of A.0. For example 𝔖_1(0) = Σφ(k)y_k² = 0.432 and 𝔖_1(1) = Σ_k y_k²μ(k) (a
  one-line computation).
- Compare with the unexplained "directional cross" (−0.481, reverse 0) of L4's seed 4. Q3 predicts that the directional
  asymmetry comes from h ↦ nN + h with n = 2, i.e. from the orientation of the quotient: 𝔖_2(h) ≠ 𝔖_2(−h) only through the e(j′h/k′) with
  n·j′/k′.
- **If 𝔖_2 is even in h, Q3 does not explain the asymmetry and fails its P4 test.**

**6. First lemma and risk.** *Lemma Q3.1:* closed formula for 𝔖_n(h) and for the Poisson error in N for w_{n,h} with g of class C².
- **Risk:**
  - The weight w varies at scale N·(width), which at the boundary N ≈ μ is ≈ 0.2μ, smaller than the modulus [d, e] ≤ μ². There the
    nonzero Poisson frequencies are **not** small, and that is exactly where the escape lives. If the boundary error admits no
    identity (mirror), Q3 is C6 on [μ, μ²].
  - Index risk: an auditor may read Q3 as "Poisson-on-ℤ as an identity" (INV_H). The defense is the new reason (1)–(2),
    which stays ARGUED.

---

## C. Ranking and first lemma to launch

| | Source of 𝒫 (P3a) | P3(b) in the identity | P9 | P2 risk | Index risk | Lemma 1 decidable |
|---|---|---|---|---|---|---|
| **Q2 ladder** | 𝒲 of the difference of mollifiers (support on divisors in [μ/p, μ)) | yes (FF.1 per level; a_P via 𝒟_p) | exact sub-lattice Λ_p | medium (the difference may be post-cancellation) | medium (GG, restriction 11) | yes: identity for p = 2 plus amplitude at g* |
| **Q1 SQ** | weighted Selberg variance Σφ(k)y_k²β_k | yes (SQ.0) | base k common to all classes | **high** (pre-cancellation modes) | medium (INV_H, defensible) | yes: kernel of 𝔅 |
| **Q3 (S⁺)-h** | Bochner on ℤ with weights |y_k|² | yes (Beurling without ℤ) | near-coincidences N′ = nN + h | medium | **high** (INV_H, Poisson-on-ℤ) | partial: the boundary N ≈ μ |

**Ranking: Q2 > Q1 > Q3.**
- Q2 is the only one whose candidate 𝒫 is **a priori post-cancellation**. The difference of two mollifiers only has coefficients at N
  with a divisor in [μ/p, μ), and the Möbius cancellation between levels is built into the definition, not between pieces, as P2
  requires.
- Q2 uses the exact sub-lattice Λ_p (T.3) as its sole arithmetic gate, and its test at μ = 15 (step 2 against the resonance −0.481) is
  falsifiable with existing data.
- Q1 provides the PROVED tools (T.3, SQ.0, Selberg base = 𝖼_{b/a}), but its natural 𝒫 almost certainly violates P2.
- Q3 is the riskiest against the index and at the Poisson boundary.

**First lemma to launch (construction and audit): Lemma Q2.1.**
- (i) Exact ladder identity for p = 2: W_T(g) as a function of 𝔊_{μμ}, 𝔊_{μ,μ/2}, 𝔊_{μ/2,μ/2} and the boundary terms
  N ∈ [μ/2, μ), with c_{2N} = c_N − c^{(μ/2)}_N (N odd) and its analogue for N even.
- (ii) Decide whether the radicality of level μ/2 holds for the g of the level-μ core. If it does not hold, write the exact defect.
- (iii) At g*, evaluate the amplitude of Ψ̌^{[μ]} − Ψ̌^{[μ/2]} against ℓ*^{½} and step 2 against −0.481 W*. This is NUMERICAL on the
  MORI15 data.
- **Death criterion:** if (ii) leaves an O(1)·‖g‖² defect controllable only by a Möbius bound on [μ/2, μ), Q2 is C6 and is
  recorded as NO-GO.

**In parallel (no dedicated construction):**
- Lemma SQ.1 as a P2 check for Q1, a single evaluation of 𝔅(g*).
- Index record of what is PROVED this round:
  - T.1 (exact Fourier Toeplitz with symbol |D_μ|²; polar ≡ 0 if A = 0).
  - T.3 (exact sub-lattice = ζ·S_n, Selberg) and the rule c_{pN}.
  - SQ.0 (radicality of the Ramanujan combs).
  - A.1: (ii) is the zero side, with D_μ(ρ) = −1.
  - The correction "𝒯_∞ is not positive" (t₀ = 6.2898).

Row D: **OPEN**. L′♯: **OPEN**. No sign is asserted.
