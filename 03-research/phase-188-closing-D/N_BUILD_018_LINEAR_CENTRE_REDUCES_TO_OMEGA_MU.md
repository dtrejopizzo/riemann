# N_BUILD_018 — The "linear-centre" bilinear split is N_BUILD_006 §2 rewritten; a meta-theorem: shift-multiplier calculus = 𝔄_T-linear algebra + Bochner

Pen and paper. Notation of N_BUILD_005/006/016/017. All shift operators below are finite sums of τ_a, i.e. Fourier multipliers.

## Corpus check
N_BUILD_006 §2 (comb = 2⟨L_M, f^μ⟩ + 2⟨L_B, f^μ⟩, Möbius-transported test f^μ; (Ω_μ)), N_BUILD_016/017 (Gram split), L2_BUILD_017
(operator form). Paper 47 thm:Z / R186_052 Thm 3.3 (dual cone via sinc-smoothed positive measures, Kreĭn; CONDITIONAL mod (−1)^k).
grep "bilinear split|operator calculus|Bochner.*multiplier|sum of squares.*Dirichlet|divisor lattice": none. New: Prop 1 (reduction),
Theorem 2 (meta-theorem), §3 (the residual structure), §4 (the next object).

## 1. Prop 1 (PROVED): the proposed split IS (Ω_μ)
Write U_log = 𝓛_M + 𝓛_B, where 𝓛_M is the multiplier of the main term L_M = u e^{u/2}du of the log-weighted integer comb and 𝓛_B its
Euler–Maclaurin remainder (N_BUILD_006 §2). For real F ∈ L²(I_T):
 2Re⟨U_μF, 𝓛_•F⟩ = 2⟨Z^{−1} * L_•, Re c_F⟩_{𝔄_T} = 2⟨L_•, f^μ⟩,  • ∈ {M, B},
because Re⟨AF, BF⟩ = ⟨A^*B, Re c_F⟩ for multipliers A, B given by finite measures on ℝ (Plancherel; the symbol of A^*B is
conj(â)b̂, and ⟨F, τ_aF⟩ = c_F(a)), and lags ≥ 2T vanish. So "pair U_μF with the fluctuation of U_logF, main term separately" is exactly the
split comb = 2⟨L_M, f^μ⟩ + 2⟨L_B, f^μ⟩ of N_BUILD_006 §2. Its main part 2⟨L_M, f^μ⟩ = 2⟨Z^{−1}*L_M, c_F⟩ is NOT the PNT density
2e^{u/2}du paired with c_F: Z^{−1}*L_M = M^{−1}*L_M − M^{−1}*B*Z^{−1}*L_M (N_BUILD_007 §0), and M^{−1}*L_M = (δ₀ − e^{−u/2})*ue^{u/2}
= (e^{u/2} − e^{−u/2})du·(…) carries the polar density, while the second term is a Möbius-weighted (Mertens-type) convolution.
So the "linear centre" is not Tate-annihilated exactly; Tate kills only the M^{−1}*L_M part (N_BUILD_001 (A)), and the rest is (Ω_μ). ∎

## 2. Theorem 2 (meta-theorem, PROVED)
Let 𝒜 be the commutative algebra of finite measures on ℝ (multipliers), with involution A ↦ A^* (reflection + conjugation). For F ∈ L²(I_T),
every expression built from the comb operators by sums, products, adjoints and real parts of inner products,
 Σ_i Re⟨A_iF, B_iF⟩,
equals ⟨ν, Re c_F⟩ with ν := Σ_i A_i^*B_i ∈ 𝒜 restricted to (−2T, 2T): a LINEAR functional of c_F. In particular (i) every operator
identity among U_s, U_μ, U_log, U_Λ (Euler, Möbius, log-derivative, s-derivatives) is an identity in the truncated algebra 𝔄_T (two-sided
version), and (ii) the only additional structure the operator language supplies is positive-definiteness: A^*A is a positive-definite
measure, so ⟨A^*A, c_F⟩ = ‖AF‖² ≥ 0 (Bochner) and Cauchy–Schwarz |⟨A^*B, c_F⟩|² ≤ ⟨A^*A, c_F⟩⟨B^*B, c_F⟩.
*Proof.* Plancherel per term; linearity. ∎
Consequence: N_BUILD_016/017 (Gram), L2_BUILD_017 (splitting certificates), and this memo use exactly two tools — linear identities in
𝔄_T and Bochner/Cauchy–Schwarz — and the latter loses (017: size 4T; L2_017: class empty for T ≥ 0.60). **NO-GO for any further
"operator-calculus" split of the comb that uses only these two tools in Cauchy–Schwarz form.**

## 3. What survives the meta-theorem: sums of squares
Bochner positivity is used without loss only in the form of a CERTIFICATE: the window measure
 μ^{form}_T := (archimedean measure) − (comb) (two-sided, on (−2T, 2T)), with 𝔞_T(F) = ⟨μ^{form}_T, c_F⟩,
is ≥ 0 on P_T iff it lies in the dual cone 𝒦_T^*, and a sufficient condition is
 μ^{form}_T = Σ_i A_i^*A_i + (positive-definite continuous part) + β₀cosh(u/2) + β₁u sinh(u/2)  on (−2T, 2T)   (SOS)
(Tate annihilators: P_T kills the last two; R186_052 / thm:Z context: the converse is the Kreĭn description, CONDITIONAL mod (−1)^k).
This is θ = 1, C = 0 by construction (escapes W-lin), uses positivity without Cauchy–Schwarz, and the arithmetic enters through the
choice of the A_i.

## 4. The next object (OPEN): divisor-lattice sums of squares
Take A_i ARITHMETIC: A = Σ_{n<N} x_n δ_{log n} (a Dirichlet polynomial). Then A^*A = Σ_{n,m} x_n x̄_m δ_{log(n/m)}: atoms at logarithms of
RATIONALS. The comb has atoms only at log of prime powers (with coefficient −v_k), the archimedean measure has none. Hence an arithmetic
SOS certificate requires: (a) at every lag log q, q = n/m ∉ {prime powers, 1}, the coefficients Σ_{n/m = q} x_n x̄_m summed over i cancel
(or are absorbed by Tate terms — impossible, those are continuous); (b) at q = p^k: Σ_i Σ_{n/m=p^k} x^{(i)}_n x̄^{(i)}_m = −v_{p^k} (negative!) ...
but (b) has the wrong sign for a Gram-type sum of a single square at small i; with several squares and cancellations it is a combinatorial
problem on the multiplicative lattice ℚ_{>0} ∩ [1/N, N]: realize the measure −Σ v_k(δ_{log k} + δ_{−log k}) + (archimedean part, which must
supply all atoms' compensation through its own positive-definite square root) as Σ A_i^*A_i.
Note μ*1 = δ gives the prototype: (Z^{−1})^*… with Z^{−1}*Z = δ₀ — the identity at the level of measures, not of squares.
First test (pen and paper, next memo): T = ½log 3 (comb atoms at log 2, log 3 only; Paper 47 Theorem C certifies positivity there): decide
whether a certificate with finitely many arithmetic squares A_i supported on {1, 2, 3} plus continuous positive-definite part exists.

## Self-review
1. Prop 1: Re⟨AF, BF⟩ = ⟨A^*B, Re c_F⟩ — for real F and real measures A, B, ⟨τ_aF, τ_bF⟩ = c_F(b − a) up to the convention; the real part
symmetrizes. Correct. The identification with N_006 §2 is exact. Correct.
2. Theorem 2 is elementary (Plancherel); its value is classificatory. It does not exclude non-Cauchy–Schwarz uses of positivity (SOS), which
are recorded in §3.
3. §3: SOS ⇒ positivity on P_T is immediate (each square pairs to ‖A_iF‖² ≥ 0; Tate terms vanish on P_T; continuous PD part ≥ 0). Correct.
The converse is the CONDITIONAL Kreĭn description; not used.
4. §4: the sign issue in (b) is real — a single square has nonnegative diagonal and its off-diagonal atoms can have either sign; the target
atoms −v_k are negative, so off-diagonal terms must produce them: allowed (x_nx̄_m can be negative). Restated as an open combinatorial
problem; no claim.
No sign contact; no negative value certified.
