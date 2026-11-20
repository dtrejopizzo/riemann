# LEMMA_E_EPSTEIN_001 — Lemma E: the Epstein window form x²+5y² is negative on P_T for T ≥ 1.59 (certificate)

Phase 200, round 7. Data and scripts: `LEMMA_E_EPSTEIN_001_data/`.

## Summary (≤250 words)

We define the Epstein window form 𝔞_T^Q (Q = x²+5y², disc. −20, h = 2) with the same template as P47 eq:Aform:
Λ_Q(s) = ½·20^{s/2}Γ_ℝ(s)Γ_ℝ(s+1)Z_Q(s), so the constant is C₀^Q = log20 − 2γ − 6log2 − 2logπ = −4.6070, the Lévy
kernel is 1/sinh(u/2), the polar term and P_T are the same as for ζ, and the comb is v_n^Q = 2Λ_Q(n)/√n (PROVED, standard
derivation from the verified FE). **Lemma E (PROVED, interval arithmetic):** there exists an explicit polynomial G of degree
56 with F = G(t/T) ∈ P_T, T = 159/100, and 𝔞_T^Q(F)/‖F‖² ∈ [−0.0599398587, −0.0599398456]; by P47 lem:monoT, the bottom
is negative for all T ≥ 1.59. Estimated true threshold (Galerkin, NUMERICAL) ≈ 1.575–1.58. In the certified window all
contact Λ_Q(n) are ≥ 0: **the first negative Λ_Q (n = 36) does not intervene**. Exact decomposition (PROVED):
Z_Q/2 = ½(ζ_K + L_ψ) = √(ζ_K L_ψ)·cosh y, y = ½log(L_ψ/ζ_K), hence Λ_Q = ½(Λ_K + Λ_ψ) + Λ_cosh, with Λ_cosh even in y
(starts at y²). On the witness: 𝔞^K = +5.049, 𝔞^ψ = +1.785, average +3.417, cosh deficit −3.479 (PROVED). At Mori's
extremal (μ = 15) the Epstein value is +1.975: the cancellation of ζ is broken by the Γ factor (degree 2), not by the
comb; against ζ_K (same Γ) the difference is 10⁻⁶. New constraint C-E: any proof of L′♯ must control the quadratic term
Λ_cosh. Lowest off-line zeros of Z_Q (NUMERICAL): 0.93297 + 15.66825i, 0.93767 + 29.98340i.

## 0. Check against the index and the corpus

Grep on `05-meta-and-planning/ROUTES-TRIED-INDEX/` ("Epstein", "Davenport", "Heilbronn", "DH", "class 2", "h=2"):

- **F-DH / F-01** (`01_PROGRAMS_RH1-RH2021.md:59`, `04_*:78`): the corpus's DH falsifier is the Davenport–Heilbronn
  function **mod 5**, linear combination f = ½(1−iκ)L(s,χ) + ½(1+iκ)L(s,χ̄) with χ a complex character mod 5,
  κ ≈ 0.28408, zero ρ ≈ 0.80852 + 85.6993i. **It is not Epstein**: it is a linear form of L(s,χ) mod 5, conductor 5, Γ
  factor Γ_ℝ(s+1) (degree 1). Epstein x²+5y² has degree 2 (Γ(s)), conductor 20, and a pole. These are two distinct
  falsifiers.
- **O10 / P47 lem:shape-epstein** (P47 l. 8525): "cited for the complete form, argued for the primitive bottom … A witness on the
  primitive subspace P_T … has not been written". This memo writes that witness. The lemma also says that Ξ_Q "shares with ξ
  the functional equation with Γ(s/2)": **this is inaccurate** (binary Epstein carries Γ(s) = Γ_ℝ(s)Γ_ℝ(s+1)·2^{s−1}π^{s} and
  conductor 20). Note for the P47 editor; it does not change O10's conclusion.
- **CA_C_007 §5** (phase 193): *complete* Epstein form negative on the Dirichlet basis (−4.5/−8.8/−12.4 at M = 200/400/800),
  NUMERICAL, without a P_T window or a certificate. **CA_L_001 Thm 4.2**: NO-GO from modular data at level 20 relying on O10 "as
  recorded" (without re-deriving the negative value) — Lemma E supplies the certified value that was missing.
- **L107 (Ziad, DH first kernel)**: DH witness, not Epstein, PLAUSIBLE-UNVERIFIED.
- AUDIT_2026-10-15_PHASE193: "O10 Epstein: CITED for the complete form, ARGUED for the primitive bottom". This memo upgrades
  the primitive bottom to PROVED.
- GUO_QUANT_001 §4.2–4.4 (C-Guo, Lemma E OPEN). META_200_BARRIER_001 (𝒦_200, piece (i) ARGUED).

Nothing done here is a retry: it is the (new) certification of a cited falsifier and the exact decomposition of its comb.
No sign route is being constructed.

## 1. The object and its window form

### 1.1 Z_Q (PROVED except for what is CITED)
Z_Q(s) = Σ_{(x,y)≠0}(x²+5y²)^{−s} = Σ_n r_Q(n)n^{−s}. With K = ℚ(√−5), Cl(K) = {C₀, C₁} (C₁ ∋ 𝔭₂, 𝔭₃, 𝔭₇, form
2x²+2xy+3y²), w = 2, and ψ the genus character (ψ(C₁) = −1):

  **Z_Q(s) = ζ_K(s) + L_ψ(s),  ζ_K = ζ·L(·,χ₋₂₀),  L_ψ = L(·,χ₋₄)L(·,χ₅)**,

i.e. Z_Q = 2Σ_{𝔞∈C₀}N𝔞^{−s} (CITED: Dirichlet/Hecke, genus theory; **verified** coefficient by coefficient
r_Q = 1∗χ₋₂₀ + χ₋₄∗χ₅ for n ≤ 500, `epstein_coeffs.py`). Both summands have the same gamma factor Γ_ℝ(s)Γ_ℝ(s+1)
and conductor 20. FE (CITED, Epstein 1903): Λ_Q(s) = (√20/2π)^sΓ(s)Z_Q(s) = Λ_Q(1−s); by duplication
(√20/2π)^sΓ(s) = ½·20^{s/2}Γ_ℝ(s)Γ_ℝ(s+1). Numerical check: |Λ_Q(s) − Λ_Q(1−s)| = 1.3·10⁻³⁵ at s = 0.3+7.1i; residue
at 1: 1.40496294621 = π/√5; Z_Q(0) = −1; Z_Q(2.5) from the identity matches the truncated lattice sum (`zeros_out.txt`).
Λ_Q has simple poles at s = 1 and s = 0 and none other.

### 1.2 The comb Λ_Q (exact)
With a(n) = r_Q(n)/2 (Z_Q/2 = 1 + …), −(Z_Q/2)′/(Z_Q/2) = Σ Λ_Q(n)n^{−s}, recursion a(n)log n = Σ_{d|n}a(d)Λ_Q(n/d).
Each Λ_Q(n) is Σ_p q_p log p with q_p ∈ ℚ, stored exactly (`lambdaQ_exact.json`, n ≤ 500). First nonzero values:
Λ_Q(4) = 2log2, Λ_Q(5) = log5, **Λ_Q(6) = 2log6**, Λ_Q(9) = 6log3, **Λ_Q(14) = 2log14**, Λ_Q(16) = 2log2, **Λ_Q(21) = 4log21**,
Λ_Q(25) = log5, Λ_Q(29) = 2log29, … and **Λ_Q(2) = Λ_Q(3) = Λ_Q(7) = Λ_Q(23) = 0**.
**Negative values (n ≤ 500):** 36, 54, 84, 126, 189, 196, 276, 294, 414, 441; e.g. Λ_Q(36) = −4log6 = −7.167,
Λ_Q(126) = −8log2 − 16log3 − 8log7 = −38.69 (`coeffs_out*.txt`). Moreover Λ_Q is supported outside prime powers
(6, 14, 21, 46, 69, …): there is no Euler product.

### 1.3 The form 𝔞_T^Q (PROVED from the FE; same template as P47 eq:Aform)
Weil's explicit formula for Λ_Q (CITED: Weil 1952, the version for any L with FE, finitely many poles and a
log-derivable Dirichlet series; the Euler product does not enter the derivation, only the sign of the coefficients) is
obtained exactly as for ζ, replacing d/ds logΓ_ℝ(s) by d/ds log[20^{s/2}Γ_ℝ(s)Γ_ℝ(s+1)]. On the line, doubled and
symmetrized:

  m_Q(τ) = log20 + [Re ψ(¼+iτ/2) − logπ] + [Re ψ(¾+iτ/2) − logπ] = 2Re ψ(½+iτ) + 2log(√20/2π).

The Lévy representation Re ψ(a+iτ/2) = ψ(a) + ∫₀^∞(1−cos τu)·2e^{−2au}/(1−e^{−2u})du with a = ¼, ¾ sums the kernels
K_{1/4} + K_{3/4} = 2(e^{−u/2}+e^{−3u/2})/(1−e^{−2u}) = **1/sinh(u/2)** (= K + (½/sinh − ½/cosh) in P47 notation). Thus,
for F ∈ L²(I_T), c = c_F:

  **𝔞_T^Q(F) = C₀^Q‖F‖² + ∫₀^{2T}(c(0)−c(u))du/sinh(u/2) + c(0)·2log coth(T/2) − Σ_{log n<2T} (2Λ_Q(n)/√n) c(log n),**

  **C₀^Q = log20 + ψ(¼) + ψ(¾) − 2logπ = log20 − 2γ − 6log2 − 2logπ = −4.607041911…**

(∫_{2T}^∞du/sinh(u/2) = 2log coth(T/2)). The polar term: Λ_Q has poles at 0 and 1 like ξ; its contribution is the same
form Φ(0)+Φ(1) = 2A(F)B(F) and **does not depend on the residue** π/√5 (the log-derivative only sees the divisor). Hence
the primitive subspace is the same P_T = {F ∈ L²(I_T): ∫F e^{±t/2} = 0} and on P_T the form is exactly the one above. The
conductor enters as +log20·‖F‖² (diagonal, favorable sign — consistent with GUO_QUANT §2.2). Compared with ζ: C₀ = −5.3722 → C₀^Q = −4.6070,
K → 1/sinh(u/2) (more Lévy mass: degree 2).

P47 lem:monoT (monotonicity in T) is proved by extending F by zero; it does not use the comb, it holds for 𝔞^Q (PROVED, same proof).

## 2. Lemma E

**Lemma E (PROVED by interval arithmetic).** Let T = 159/100. There is an explicit even polynomial G of degree 56
(rational coefficients with denominator 2^{280}, except for the x⁰, x¹ coefficients, which are the exact interval solution of
the two Tate conditions) such that F(t) = G(t/T) ∈ P_T and

  **𝔞_T^Q(F)/‖F‖² ∈ [−0.0599398587085, −0.0599398456115].**

Consequently λ_A^Q(T) := inf_{P_T} 𝔞_T^Q/‖·‖² < 0 for all T ≥ 1.59 (lem:monoT). Second certificate:
T = 8/5, degree 48: [−0.0619395254, −0.0619395173]. Third (odd sector, degree 31): T = 1.9: [−0.92552390, −0.92552389].
Full vectors: `cert_T1.59_full57.txt`, `cert_T1.6_full49.txt`, `cert_T1.9_odd32.txt`.

*Method.* Identical to phase-198 `cert_falsifiers.py` (mpmath.iv, outward rounding; reuses Cpoly, tate_mom), with three
changes: (a) moments ∫₀^{2T}u^r/sinh(u/2) = 2Σ_k γ(r+1,(k+½)2T)/(k+½)^{r+1}, k < 6000 exact, tail by integral comparison
with step 1; (b) tail ∫_{2T}^∞ = 2log coth(T/2) in intervals; (c) comb with exact Λ_Q(n) (rationals × log p in intervals),
contact set decided by interval comparison. Choice of G: Galerkin minimizer (non-rigorous, only used to choose G). Technical
lesson: with denominator 2⁴⁰ the degree-48 certificate **fails** (gives +4.61: the ill-conditioning of the monomial basis
amplifies rounding); with 2^{240}/2^{280} the interval matches Galerkin to 10⁻⁸. The phase-198 battery used
degree ≤ 24, where 2⁴⁰ suffices.

*Pieces on the witness T = 1.59 (normalized to ‖F‖ = 1):* C₀^Q = −4.6070, Lévy +8.7839, comb −4.2368 (contacts
4: +0.2825, 5: +0.0462, **6: +1.1192**, 9: +1.4107, **14: +0.5139**, 16: −0.0919, **21: +0.9563**); total −0.0599.

*Threshold.* Galerkin (NUMERICAL) on the full space: degree 40: 0.2418 (1.55), 0.0506 (1.59); degree 48: 0.0920 (1.58),
−0.0499 (1.60); degree 56: 0.2257 (1.56), 0.0905 (1.57), −0.00014 (1.58), −0.0599 (1.59). The bottom decreases with degree; the
true threshold T_E* lies in ≈ [1.55, 1.58]. Certificate: **T_E = 1.59**. (Comparison: ½log25 = 1.609, ½log15 = 1.354.)

*Zeros (NUMERICAL, data, not used in the proof).* Argument principle (`argcount.py`): no zero of Z_Q in
[0.52,1.6]×[0.1,15]; one in [0.52,1.6]×[15,16.5]; one in [0.52,1.6]×[16.5,30]. Newton:
**ρ₁ = 0.932969697485 + 15.668249531i**, **ρ₂ = 0.937666906700 + 29.983395235i** (with their reflections 1−ρ̄, ρ̄). The value
"0.68 + 3.3i" suggested as the target is **not** a zero (there are no off-line zeros with t < 15). The fact that there exist
zeros with Re s ≠ ½ (even Re s > 1) is CITED (Davenport–Heilbronn 1936). The scale is consistent: a test of type T ≈ 1.6
has resolution π/T ≈ 2, and the density of zeros of Z_Q at height 15 is (1/π)log(15√20/2π) ≈ 0.75 per unit.

**Key structural fact (PROVED, read off the certificate):** in the window T = 1.59 the contacts are {4,5,6,9,14,16,21} and
**all have Λ_Q(n) ≥ 0**. The first negative coefficient, n = 36, enters only at T = ½log36 = 1.79. Hence the negativity of
Lemma E does **not** come from negative comb coefficients: a non-negative comb, partially supported outside prime powers,
suffices to break positivity on P_T. "Λ ≥ 0" is not the property that separates.

## 3. Comparison at Mori's extremal μ = 15 (NUMERICAL, double precision, `mori15_compare.py`)

Complete form (with pole, convention of MORI15_EXTREMAL_001_pieces.py) on g* (even, ‖g*‖ = 1). Reproducing ζ gives
−5.372183 + 3.916389 + 1.518999 − 0.063204 = −1.6·10⁻⁹ (the arb value is 4.8·10⁻⁷⁰; double precision only sees 10⁻⁹: check OK).

| piece | ζ | Z_Q | ζ_K (Γ of Z_Q, Euler) | L_ψ |
|---|---|---|---|---|
| archimedean constant | −5.37218 | −4.60704 | −4.60704 | −4.60704 |
| Lévy | +3.91639 | +5.06284 | +5.06284 | +5.06284 |
| pole 2AB | +1.51900 | +1.51900 | +1.51900 | +1.51900 |
| comb | 0.063204 (n=2: 99 %) | 2.17·10⁻⁶ (n=4) | 0.063826 | −0.063823 |
| **total** | **≈ 0 (4.8·10⁻⁷⁰)** | **+1.97480** | +1.91098 | +2.03862 |

Reading. (a) On g*, Epstein is **positive** (+1.975). (b) The 70-digit cancellation of ζ is broken by the **archimedean**
part: ΔC₀ = +0.765, ΔLévy = +1.146; the comb contributes only +0.063 (Λ_Q(2) = Λ_Q(3) = 0 removes the n = 2 term that
carried 99 % of ζ's comb). Hybrids: arch ζ + comb Q = +0.0632; arch Q + comb ζ = +1.912. (c) With the correct archimedean
part (ζ_K or L_ψ, same Γ factor), Epstein = average of ζ_K and L_ψ + cosh deficit, and the deficit at g* is −1.08·10⁻⁶: g*
is a bump of width 0.21 that does not see contacts 6, 14, 21. **The Euler product does not act on ζ's extremal by itself**:
ζ's extremal is a vector for ζ, and Epstein's is another one (§2: an oscillating vector of degree ~50, which resolves the
composite contacts). What the extremal does show: ζ's cancellation at g* is archimedean-vs-pole with the comb as a 1 %
correction, and changing Γ_ℝ to Γ (degree) moves the value by O(1); that is why the honest comparison of "Euler vs no
Euler" is Z_Q vs ζ_K, not Z_Q vs ζ.

## 4. What Epstein teaches

### 4.1 Exact decomposition (PROVED)
Since Z_Q/2 = ½(ζ_K + L_ψ) with ζ_K, L_ψ Euler products of the same degree and conductor,

  **Z_Q/2 = √(ζ_K L_ψ)·cosh y,  y := ½log(L_ψ/ζ_K) = −Σ_{p∈𝒩} e_p Σ_{k odd} p^{−ks}/k,**

where 𝒩 = {primes whose prime ideals lie in the non-principal class} = {2, 3, 7, 23, 43, 47, 67, 83, 103, 107, 127, 163,
167, …}, e₂ = 1 (ramified), e_p = 2 (split). (Local computation: at p ∈ 𝒩 split, L_ψ/ζ_K has factor
((1−p^{−s})/(1+p^{−s}))², at 2 the factor (1−2^{−s})/(1+2^{−s}); at the other primes the quotient is 1.) Taking −d/ds log:

  **Λ_Q = ½(Λ_K + Λ_ψ) + Λ_cosh,  Σ Λ_cosh(n)n^{−s} = −(d/ds) log cosh y = −(d/ds)[y²/2 − y⁴/12 + y⁶/45 − …],**

with Λ_K(p^k) = log p·(1+χ₋₂₀(p)^k) ≥ 0 and Λ_ψ(p^k) = log p·(χ₋₄(p)^k + χ₅(p)^k). Verified exactly for n ≤ 200
(`cosh_decomposition.py`, 0 discrepancies). Consequences, all PROVED:
1. Since the form is linear in the comb and ζ_K, L_ψ, Z_Q share C₀^Q, the kernel 1/sinh(u/2) and P_T:
   **𝔞_T^Q = ½𝔞_T^K + ½𝔞_T^ψ − Σ_n (2Λ_cosh(n)/√n) c(log n).**
   The first two are forms of Euler products (each a sum of two degree-1 forms: ζ and L(χ₋₂₀); L(χ₋₄) and L(χ₅)).
2. Λ_cosh is **even in y**: it has no linear term. Its support is the n with Ω_𝒩(n) ≥ 2 even; the sign of its
   order-2j part is (−1)^{j+1} (log cosh series). Order 2: −(y²/2)′ = −y·y′ has coefficients ≥ 0 (y has coefficients ≤ 0),
   supported on products of two odd prime powers from 𝒩: 4, 6, 9, 14, 21, 46, 49, 69, … (Λ_cosh(6) = 2log6,
   Λ_cosh(21) = 4log21). Order 4: negative, n with four factors from 𝒩: 36, 54, 84, 126, 189, 196 — **exactly** the list
   of Λ_Q < 0.
3. On Lemma E's witness (T = 8/5, intervals, `eval_combs_on_E.py`): 𝔞^K = +5.04913, 𝔞^ψ = +1.78519, average
   **+3.41716**, cosh deficit **−3.47910**, total −0.06194. Control: Q-comb restricted to prime powers (Λ_Q·1_{prime powers})
   gives +2.4346; comb Λ_K plus the composite part of Λ_Q gives +2.5526 (neither alteration alone suffices at that vector;
   Galerkin NUMERICAL: with Λ_K the bottom is +1.097 (T=1.6), +0.0024 (1.9), +7.5·10⁻⁷ (2.2), positive and tending to 0 as
   for ζ; with Λ_K+composites it is already −1.40 at 1.9; with Λ_Q on prime powers −0.61 at 2.2).

### 4.2 The exact condition that C-Guo asks for
GUO_QUANT §4.2 asks for "a property of ζ absent in Epstein that enters quadratically in the complement of the radical". The
decomposition identifies it unambiguously:

**(Euler-quadratic)** *The comb is the log-derivative of* **one** *Euler product, i.e. Λ_cosh ≡ 0.* For Z_Q the failure of
this property is the term −Σ 2Λ_cosh(n)n^{−½}c(log n) with Λ_cosh = −(log cosh y)′, **quadratic (and higher even order) in
the class-signed sum over primes y**. Everything linear in the comb (radical, gauge, Tate, conductor, κ-count, "Λ ≥ 0",
support on the zero side) does not distinguish 𝔞^Q from the average ½(𝔞^K + 𝔞^ψ) plus a non-negative order-2 comb: that is
why they fail.

Formulated as a constraint (**C-E**, for AUDIT_CONSTRAINTS): *A proof of L′♯ (or of 𝔞_T ≥ 0 on P_T) must use an
inequality that is false when the comb Λ is replaced by ½(Λ_K + Λ_ψ) + Λ_cosh with Λ_cosh = −(log cosh y)′ and the
archimedean part by that of Γ(s)·20^{s/2}, already at T = 1.59 and on the contacts {4,5,6,9,14,16,21}.* Equivalently, it must
feel the quadratic term: if an inequality on the form is stable under "averaging two Euler products with the same Γ
factor" (convexity in the comb), Epstein falsifies it, because the averaging is done in Z (not in log Z) and the
deficit log cosh y ≥ 0 enters the comb with a fixed sign (at order 2: it contributes +y·y′ ≥ 0 to the comb, which enters
with a minus sign). ARGUED as a principle; PROVED as an identity and as a falsifier.

**Reading for the sign object (ARGUED).** The quantity a sign object must control is not Σ[2Λ − 2Λ_Q]/√n·c(log n)
against ζ (that mixes degree and conductor, §3), but the comb Λ_cosh against the Euler average, and this lives in the
**composites** n = mn′ with m, n′ of non-principal class: the cancellation m ≈ kn of the semiring principle operates here
in its purest form (the class group composes C₁·C₁ = C₀, and this generates positive comb mass at 6 = 2·3, 14 = 2·7,
21 = 3·7). For ζ (h = 1), y ≡ 0 and there is no such composition. A proof that uses Λ only through 𝒦_200 (META_200) does
not see y; this matches piece (i) ARGUED of M200 and supplies it with a certified falsifier.

## 5. Labels

- **PROVED:** form 𝔞_T^Q (from the CITED FE; P47 template); Lemma E (T = 1.59, 1.6, 1.9 certified); monotonicity for
  T ≥ 1.59; decomposition Λ_Q = ½(Λ_K+Λ_ψ) + Λ_cosh and exact verification n ≤ 200; values 𝔞^K, 𝔞^ψ, deficit on the witness;
  "all contacts of the certified window have Λ_Q ≥ 0".
- **CITED:** Epstein's FE and pole (Epstein 1903), Z_Q = ζ_K + L_ψ (Dirichlet/Hecke, genus theory), Weil's explicit
  formula 1952, existence of zeros with Re s ≠ ½ (Davenport–Heilbronn 1936).
- **NUMERICAL:** zeros ρ₁, ρ₂ and argument count; threshold T_E* ≈ 1.55–1.58; Galerkin bottoms; comparison at Mori's g*.
- **ARGUED:** C-E as a design principle; the "semiring/class composition" reading.
- **OPEN:** L′♯; row D. Lemma E gives no sign for ζ.

## 6. Entry for the index (paste into ROUTES-TRIED-INDEX)

- **LEMMA_E_EPSTEIN_001 (phase 200, round 7):** window form of Z_Q, Q = x²+5y² (Γ_ℝ(s)Γ_ℝ(s+1), cond. 20, C₀^Q = −4.6070,
  kernel 1/sinh(u/2), same P_T). **Lemma E PROVED (intervals):** 𝔞_T^Q/‖F‖² ∈ [−0.05993986, −0.05993985] at T = 1.59 (degree 56)
  ⇒ negative bottom ∀T ≥ 1.59; all contacts have Λ_Q ≥ 0 (the first Λ_Q < 0 is n = 36). Exact: Z_Q/2 = √(ζ_K L_ψ)cosh y,
  Λ_Q = ½(Λ_K+Λ_ψ) + Λ_cosh, Λ_cosh even in y (quadratic); on the witness Euler average +3.417, deficit −3.479. Mori's
  extremal: Epstein +1.975 (broken by Γ, not by the comb). Lowest off-line zeros 0.93297+15.66825i, 0.93767+29.98340i (NUM).
  The corpus's F-DH is DH mod 5 (linear form of L(χ)), not Epstein. Do not retry: "Λ ≥ 0", linearity in the comb, or
  convexity in the comb as a source of sign (C-E).

## 7. Falsifier battery

Add to CERT_FALSIFIERS_001 (row 11):

| witness | T | comb | sector, basis | enclosure |
|---|---|---|---|---|
| Epstein x²+5y² (Γ(s), cond. 20, comb Λ_Q) | 1.59 | Λ_Q | full, deg ≤ 56 | [−0.0599398587, −0.0599398456] |

with the caveat that this falsifier also changes the archimedean part (C₀^Q, 1/sinh): it falsifies every inequality that is
valid for "any L with FE, pole and Dirichlet coefficients ≥ 0" (P47 axioms A1–A6 except Euler) and, via §4.1, every
inequality stable under averaging of Euler products with equal Γ factor.

**Note for P47 (editor):** lem:shape-epstein can be upgraded to "proved for the primitive bottom" citing this certificate,
and should correct "functional equation with Γ(s/2)" → "with Γ(s) and conductor |D|".

Scripts: `epstein_coeffs.py`, `cert_epstein.py` (scan/cert; variables COMB, DPS, IVDPS, DENBITS), `eval_combs_on_E.py`,
`cosh_decomposition.py`, `diff_comb.py`, `mori15_compare.py`, `zeros_epstein.py`, `zeros2.py`, `argcount.py`.
Reproduce Lemma E: `DENBITS=280 IVDPS=140 DPS=200 python3 cert_epstein.py cert 159 100 full 57` (~25 min).
