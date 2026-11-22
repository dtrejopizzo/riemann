# R162_1003 — Round 10: the sum/difference object at coupling 1 (functional equation, Selberg Λ² test)

Pure mathematics, no numerics. Notation of R162_901 (f(T;ε), B, K, w_n = Λ(n)n^{-1/2},
α_T, β_T, γ, sum/difference channels), R162_903 (Z = M_T(1), log Z = M_T(Λ/log), Thm 4.1 Sylvester),
R162_402 (reflection dictionary), R162_802 (f = ⟨A_T^{-1}φ,φ⟩, projective flow).

**Verdict.**
- §2 Theorem S (exact cancellation of the uncontrolled part of the difference channel against the sum
  channel, all orders, at T = ∞, via the functional equation): **PROVED**.
- §3 Theorem R (the resummed object at ε = 1 is the Poisson-smoothed zero measure; its positivity ⟺ RH):
  **PROVED**, and it is **E1**.
- §4 Selberg Λ²-sieve test: the first-contact problem *is* a Selberg-type extremal problem (Prop 4.1,
  PROVED), but the Weil kernel is not a Selberg/GCD kernel (Prop 4.2, PROVED), and every Selberg
  representation H = Z*DZ is a congruence (Sylvester, Cor 4.3): **NO-GO**.
- §5 finite T: the cancellation of §2 does not survive compression (Brown–Halmos). **NO-GO**.

Overall: **PARTIAL (object constructed) / NO-GO (as a closing mechanism)**. No sign is claimed. Gate 1 OPEN.

## 0. Failing lines (stated first)

| line | where | what fails | killer |
|---|---|---|---|
| L1003.a | §3 | the object in which sum and difference cancel exactly is Σ_ρ (Poisson kernel at ρ); its positivity is the Weil sign | E1 |
| L1003.b | §2–3 | the cancellation uses only the functional equation + Hadamard product; it holds verbatim for DH, which has off-line zeros | F3 (DH), Φ |
| L1003.c | §2 | the surviving "Re D" part concentrates at the zeros as (1/η)·δ: the ε-series is termwise divergent on the line; this is the T = ∞ face of the pole ε_c < 1 | L901.c |
| L1003.d | §4 | Weil kernel is multiplicative-Toeplitz κ(log m/n), not a GCD kernel g((m,n)); Selberg diagonalisation needs the latter | Prop 4.2 |
| L1003.e | §4 | H = Z*DZ with Z unipotent integral: D ≥ 0 ⟺ H ≥ 0 (Sylvester); the Smith SOS with Λ(d) is Beurling-generic | R162_903 Thm 4.1, G2_B4_R3 §5 |
| L1003.f | §5 | at finite T, S_xB^{-1}S_y ≠ B^{-1}S_xS_y; the pointwise symbol algebra of §2 is lost | R162_301, L901.b |

## 1. Corpus check

- Sum/difference split and the residual: R162_901 §3, §6. Selberg Λ·L + Λ*Λ = μ*L²: R162_501, R162_901.
- Weil symbol = zero measure, Kreĭn indeterminacy: Paper 46 thm:KEP3, phase 155 r5 (E1).
- GCD/Smith SOS Σ a_m ā_n log gcd(m,n) = Σ Λ(d)|Σ_{d|m} a_m|²: G2_B4_R3 §5 (excluded, Beurling-generic).
- Nyman–Beurling / Vasyunin GCD Gram, Báez-Duarte Selberg-type coefficients μ(k)(1 − log k/log N):
  phase 33 Doc 82, R157_002 row 43 (EQUIV).
- Selberg sieve majorant Λ_Q^Sel: R149_001 (refuted as centring model, D.59.0a(1)).
- Sieve→index bridge: phase 36 Doc 108 (dead: "on average over windows" → "uniform" is RH).
- Multiplicative Toeplitz (Hilberdink): G2_P4_R5.
New here: Theorem S (the exact Im-part cancellation between the two channels at every order), Theorem R as
the resummation of the ε-series, the identification of the ε-series divergence with zero concentration, and
Prop 4.1/4.2 (first contact as Selberg extremal problem; non-GCD obstruction).

## 2. Exact cancellation between the channels — PROVED

Full line (T = ∞), where the compressed operators become Fourier multipliers (R162_901 Prop 3.2). Write
s = ½ + η + it, η > 0 (regularisation; D converges only for η > ½, and for ½ ≥ η > 0 we use the
meromorphic continuation — this is the only regularisation used), and

  D_η(t) := −(ζ'/ζ)(½ + η + it),   k_η = 2 Re D_η,   b = arch + polar symbol (the symbol of B).

On the line the ε-expansion of f is ∫ |φ̂|² Σ_j ε^j k^j / b^{j+1} dt, and at order 2

  k² = 2 Re(D²) + 2|D|²       (sum channel + difference channel),

with Re(D²) the Dirichlet series of Λ*Λ (sum channel, R162_901) and |D|² the mean-square kernel
(difference channel).

**Theorem S.** For every j ≥ 1 and η > 0,

  (i)  sum channel + difference channel = 4(Re D_η)²; the part (Im D_η)² of the difference channel
       cancels **exactly** against the −(Im D_η)² in Re(D_η²);
  (ii) more generally k_η^j = 2^j (Re D_η)^j: the j-point channels (the Λ^{*k} convolutions and all mixed
       |·|² terms) combine so that Im D_η never appears;
  (iii) by the functional equation and the Hadamard product,

        Re D_η(t) = ½ b_η(t) − Π_η(t),    Π_η(t) := Σ_ρ Re 1/(s − ρ) = Σ_ρ (½+η−β)/((½+η−β)² + (t−γ)²),

       where b_η is the arch + polar symbol evaluated at s (smooth in η, b_0 = b), the sum over ρ taken
       symmetrically in γ. Hence

        b_η − ε k_η = (1 − ε) b_η + 2ε Π_η   (exact, all ε).

*Proof.* (i) Re(D²) = (Re D)² − (Im D)², |D|² = (Re D)² + (Im D)²; add. (ii) k = 2 Re D by definition;
the claim is that the channel decomposition of k^j (expanding (D + D̄)^j into D^a D̄^{j−a}) recombines to
(2 Re D)^j, which is binomial. (iii) −ζ'/ζ(s) = −ξ'/ξ(s) + ½ψ(s/2) − ½log π + 1/(s−1) + 1/s, and
Re ξ'/ξ(s) = Σ_ρ Re 1/(s−ρ) (Hadamard, symmetric summation, B-term cancels by ξ(s) = ξ(1−s)); the
remaining terms are the arch + polar symbol, whose real part is ½b_η by definition of b. ∎

**Reading.** The "uncontrolled" part of the difference channel identified in R162_901 L901.b is exactly
(Im D)² = (∂_t log|ζ(½+η+it)|)², and it is *not* uncontrolled: it cancels identically against the sum
channel, at every order, once D is written through the functional equation. What remains is Re D, which by
(iii) is archimedean minus the Poisson-smoothed zero measure. So the requested non-perturbative object
exists and is explicit. The price is visible in (iii): all arithmetic is now in Π_η.

**Corollary S′ (divergence of the ε-series on the line; L1003.c).** For on-line zeros, Π_η → π Σ_γ δ(t−γ)
as η → 0, and (Π_η)² ~ (π/2η) Σ_γ δ(t−γ). The order-2 coefficient ∫|φ̂|² k_η²/b³ therefore diverges like
η^{-1} Σ_γ |φ̂(γ)|²/b(γ)³, and the order-j coefficient like η^{1−j}. The Taylor coefficients of f(∞;ε) have no
η → 0 limit: the ε-series on the line is termwise singular at the zeros. This is the T = ∞ counterpart of the
pole ε_c(T) < 1 of L901.c (there the compression regularises, here η does). ∎

## 3. The resummed object at coupling 1 — PROVED, E1

**Theorem R.** At T = ∞ and η > 0, for any test φ with φ̂ decaying,

  f_η(∞;ε) = ∫ |φ̂(t)|² / ((1 − ε) b_η(t) + 2ε Π_η(t)) dt   (whenever the denominator is positive),

and at ε = 1 the quadratic form B − K has symbol 2Π_η. Consequently, for every η > 0,

  B − K ≥ 0 on L²(ℝ) (η-regularised)  ⟺  Π_η ≥ 0 a.e.  ⟸  every zero has β ≤ ½ + η,

and Π_η ≥ 0 for all η ∈ (0, η_0) ⟺ RH (an off-line zero ρ_0 with β_0 > ½ gives Π_η(γ_0) → −∞ as
η ↑ β_0 − ½ from below, since its Poisson term (½+η−β_0)^{-1} dominates; conversely under RH every term is
positive).

*Proof.* Theorem S(iii) and diagonality of Fourier multipliers. The equivalence: each term of Π_η is a
Poisson kernel of sign sgn(½+η−β). ∎

**Why this is E1 (L1003.a).** Theorem R is the explicit formula in symbol form: B − K has symbol "zero
measure" (Paper 46 thm:KEP3, the Weil form W(g) = Σ_ρ ĝ(γ)·conj ĝ(γ̄)). The object in which "the
difference channel cancels exactly against the sum channel" is precisely Σ_ρ, and "manifest positivity" of
it is RH. The residual of R162_901 §6 anticipated this ("a positivity statement for ζ'/ζ on a line, i.e.
Weil again, unless it is exact and not positive"): Theorem S is the exact, not-positive version; Theorem R
shows the positive version is E1.

**Falsifier behaviour (L1003.b).**
- DH: satisfies a functional equation with the same Γ-type, and has a Hadamard product; Theorems S and R hold
  verbatim with Π_η^{DH}, which is negative near its off-line zeros. So S/R cannot yield positivity: F3 passes
  them. *The cancellation is FE-level, the sign is Euler-level.*
- Deletion Λ1_{n≥5}, κ-models: no functional equation. The analogue of (iii) acquires the residual
  2Re Σ_{n<5} w_n n^{-1/2-η-it} (deletion) or (1−κ)·(prime part) (κ-model), which is not concentrated at
  zeros; the exact cancellation of Im D still holds (it is algebra, S(i)), but the resummation to "zeros
  only" fails. So S(iii) *separates* deletion/κ-models — correctly, but these are separated already at the
  linear level (R162_903 §3 reading).
- Λχ₂ with ζ's archimedean data: the FE of L(s,χ₂) has conductor 4 and a different Γ-factor, so b_η does not
  match and S(iii) acquires a smooth archimedean mismatch; with its own data S/R hold and Λχ₂ satisfies GRH
  numerically — no separation from ζ either way.
- Beurling (DMV): no FE; S(iii) fails; nothing to separate, and nothing gained.
- F1: S and R are identities in the symbol, not in F; λ = 0 is not used. F2: S is even in D (sign-blind
  under D → −D only up to b ↦ −b, i.e. not orientation-producing). F4: exact, no limit in T (the η → 0
  limit is the only one, and it diverges, Cor S′).

## 4. Selberg Λ² sieve test

**Prop 4.1 (first contact is a Selberg-type extremal problem) — PROVED.** Where A_T > 0 in the parity
sector,

  1/f(T) = min { a_T(F,F) : ⟨F, φ⟩ = 1 },

attained at F = u_T/f(T). Selberg's Λ²: min { Σ_n (Σ_{d|n} λ_d)² w(n) : λ_1 = 1 } = 1/G(R), attained at
λ = (normalised) dual vector. The first contact λ_par = 0 is exactly 1/f crossing 0, i.e. the Selberg
minimum ceasing to be positive (Paper 46 g_par = 1/f + 2ε_par for the complete form).

*Proof.* Lagrange multiplier for a positive form with one linear constraint; minimum = 1/⟨A^{-1}φ,φ⟩. ∎

So the structural analogy asked for is exact: the Weil form near its kernel, under the one linear
constraint ⟨F,φ⟩=1, is an optimal-quadratic-form problem of Selberg type. The question is whether it has
Selberg's *explicit diagonalisation*.

**Prop 4.2 (the Weil kernel is not a Selberg/GCD kernel) — PROVED.** Selberg's form is diagonalised by
Möbius because its kernel is a GCD kernel: Σ_n w(n)1_{d|n}1_{e|n} = g([d,e]) = Σ_{k|(d,e)} (g*μ-type)(k)·…,
i.e. a function of (d,e) after the multiplicative normalisation (Smith). The Weil prime kernel on the lattice
basis e_n (R162_903 §3) is multiplicative-Toeplitz: K_{m,n} = κ(log m − log n). Suppose on {1,…,N}
κ(log m − log n) = g((m,n)) + c·δ_{mn} for some g, c. Taking m = 1 and n = 2,…,N gives κ(−log n) = g(1) for
every n ≤ N, and symmetrically κ(log n) = g(1); so κ is constant on {±log n : 2 ≤ n ≤ N}. The prime part of the Weil kernel,
κ_pr(x) = −Λ(e^{|x|})e^{-|x|/2}, is 0 at log 6 and −log 2/√2 at log 2, so constancy of κ = κ_arch+pol + κ_pr
would force κ_arch+pol(log 2) − κ_arch+pol(log 6) = log 2/√2, and similarly at every pair (prime power,
non-prime-power) ≤ N; a smooth fixed archimedean kernel cannot satisfy all of these as N grows
(the prime-power set is not a level set of any smooth function beyond finitely many points). ∎

**Cor 4.3 (Selberg representations are congruences) — PROVED.** Any representation H = Z*DZ with Z unipotent
integral (Möbius-invertible, R162_903 Lemma 3.1) has D = Z^{-*}HZ^{-1}; by Sylvester, D ≥ 0 ⟺ H ≥ 0 and
inertia(D) = inertia(H). A Selberg-sieve SOS for the Weil form is therefore equivalent to Weil positivity, and
the only all-N SOS with coefficients Λ(d) (Smith, G2_B4_R3 §5) is Beurling-generic and is not the Weil prime
side (whose entries are negative with zero diagonal). ∎

**Consequence.** Selberg's sieve gives *minimal positive* forms because its kernel is GCD (positive-definite
by Smith once g*μ ≥ 0, a coefficientwise check). Weil's kernel is Toeplitz in log, whose positive-definiteness
is Bochner = positivity of the symbol = Theorem R = RH. The two extremal problems share the Lagrange shape
(Prop 4.1) but not the diagonalising structure (Prop 4.2). The Nyman–Beurling route, which *does* put a GCD
Gram (Vasyunin) in play with Selberg/Báez-Duarte coefficients μ(k)(1 − log k/log N), is EQUIV (phase 33,
R157_002 row 43).

## 5. Finite T — NO-GO (L1003.f)

Theorem S is an identity of multipliers. At finite T the channels are carried by β_T(x,y), which depends on
x and y separately (L901.b); P_T S_x P_T S_y P_T ≠ P_T S_x S_y P_T with a finite-rank symbol-independent
defect (Brown–Halmos, R162_301). The algebraic identity Re(D²)+|D|² = 2(Re D)² has no compressed analogue:
in T(D)T(D̄) = T(|D|²) − H(D)H(D)* the compressed channels differ by Hankel products that do not cancel between
the sum and difference channels.
Its size is symbol-independent (F3 generic). The only exact finite-T trace of the functional equation is the
reflection dictionary G_+^0(−a_m) = −εζ'(−2m)K_F(a_m) (R162_402), which is linear in F (F2, F4) and was
shown DH-valid.

Could the reflection dictionary replace the η-regularisation at finite T? Inserting (1.1) of R162_402 into the
collar flux (R162_901 Cor 2.2) rewrites the edge residual R(T) as a Gamma-lattice sum
Σ_m a_m e^{−2a_m T}|G_+^0(−a_m)/ζ'(−2m)|²-type terms (R162_402 (f)) — a positive sum of squares, but of the
*port*, i.e. ‖R_LF‖² again: this is Gate 1 restated (E1), and it is DH-valid.

## 6. Record

- New PROVED: Theorem S (Im-part cancellation between sum and difference channels, all orders, T = ∞);
  Cor S′ (ε-series termwise divergent at the zeros, T = ∞ face of L901.c); Theorem R (resummed symbol at ε = 1
  is 2Π_η; positivity ⟺ RH); Prop 4.1 (first contact = Selberg-type extremal problem); Prop 4.2 (Weil kernel
  not GCD); Cor 4.3 (Selberg SOS = congruence).
- Route: NO-GO as a closing mechanism. The residual of R162_901 is answered: the non-perturbative object
  exists (Theorem R) and is the explicit formula (E1); the cancellation is FE-level and so DH-valid (F3); the
  sign sits in Π_η, i.e. in the zeros.
- Add to R162_590 §1c: "sum/difference resummation via FE; Selberg Λ² test — R162_1003 — Im D cancels
  exactly (Thm S), resummed symbol = Poisson zero measure (Thm R, E1); DH passes; Weil kernel Toeplitz not
  GCD (Prop 4.2), Selberg SOS = congruence (Cor 4.3); no finite-T analogue — E1, F3, Sylvester".
- Lesson: any exact use of the functional equation that resums the channels lands on Σ_ρ. A Gate 1 step must
  use the Euler product *after* the FE has moved everything to Π_η, and must fail for DH there — i.e. it must
  be a statement about zeros that DH violates, which is RH-type content by construction.
