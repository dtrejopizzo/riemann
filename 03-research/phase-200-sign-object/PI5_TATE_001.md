# PI5_TATE_001: Lemma Π.5 (scale of the Tate mode versus the leak; phase 200, round 26b)

**Leak lemma, not a sign lemma. L′♯ OPEN.
Row D OPEN.** Read: PI4_JUMPS_001 (§1.3, §2, R-Π4, Π.5 proposed), PI_MU_001 (Π.0, Π.0′, Π.1), AUDIT_200_PIMU_001,
B1_FLAT_001, K3_GAMMA_001, Paper 47 prop:ext-gauge, lem:ext-mob, lem:ext-ellbound.

**Index check.** Grep in ROUTES-TRIED-INDEX for "Tate", "f♯(0)", "Slepian", "prolate", "coerciv", "MORI15". Hits:
MORI15 (ℓ* ∈ [4.4,8.5]e−70), PI_MU (Π.0 with χ_0(2π)), PI4 (Tate mode, R-Π4). No entry bounds f♯(0) by ℓ nor
studies the N-dependence of that constant. New reason: here the Slepian coercivity is used on the **full** interval
[−λ,λ] (not only on I = [−1/λ,1/λ], as in Π.0), which is what fixes the scale e^{−4πN}.

## 1. Exact statement

Notation from def:ext: λ = e^T, N = λ², I = [−1/λ,1/λ], Q = 1 − B_λ, L²_0 = {φ even, supp φ ⊂ I, ∫φ = 0},
𝒢̄_T = Q𝓕(L²_0) (Π.0). For g in the core (compact support in (−T,T), g(±T) = 0 to order 2, A = B = 0), f = E⁻¹g.
By lem:ext-mob, f(u) = u^{−½}Σ_m μ(m)m^{−½}g(log(mu)), hence supp f ⊂ [−λ,λ] and f_out := f·1_{|u|>1/λ} ∈ L²(J),
J = {1/λ < |u| < λ}.

**Definition (f♯).** f♯ := f − φ_opt, with φ_opt ∈ L²_0 the (unique, Π.0) minimizer of ‖Q𝓕(f − φ)‖². Then
ℓ(g) = 2‖Q𝓕f♯‖² = 2 dist²(r_f, 𝒢̄_T), and Q𝓕f♯|_{(λ,∞)} = Π_μ r_f.

**Lemma 1.1 (f♯(0) well defined; PROVED).** The optimality condition is Q𝓕f♯ ⊥ Q𝓕(L²_0), i.e.
P(f♯ − Bf♯) = c·1_I (Lagrange multiplier for ∫φ = 0). Hence f♯ = c + Bf♯ on I: f♯|_I is the restriction of an
entire function plus a constant, and f♯(0) is defined pointwise. Since f(0) = 0 (admissibility),
 f♯(0) = −φ_opt(0).
Moreover f_out ↦ f♯(0) =: Λ_N(f_out) is linear and L²-bounded: ‖f♯‖ ≤ C_0‖f_out‖ with
C_0 = (1 − χ_0(2π))^{−1/2}·O(1) (uniform resolvent of Π.0), and |Bf♯(0)| ≤ (2λ)^{½}‖f♯‖, |c| ≤ O(λ^{½})‖f♯‖. Thus
|Λ_N|² ≤ C_1λ (C_1 absolute). □

Remark: f♯ depends only on f_out (φ_opt absorbs f_in). The algebraic constraint φ(0) = 0 does not enter: with it
the infimum is not attained (AUDIT_PIMU) and f♯ does not exist; with the closure, f♯ exists and φ_opt(0) is free.
Π.5 is therefore stated as follows:

**Π.5.** There exists C such that |f♯(0)|² ≤ C·ℓ(g) for every g of the core. Question: is C independent of N
(of μ)?

## 2. Answer: true for each N, with an exponential constant; false uniformly

### 2.1 Theorem Π.5(a) (coercivity; PROVED)

For every g of the core (and, by continuity, every f_out ∈ L²(J)):
 ℓ(g) ≥ 2(1 − χ_0(2πN))·‖f_out‖²,
where χ_0(c) is the first Slepian eigenvalue of the pair (time [−λ,λ], band (−λ,λ)), parameter c = 2π·λ·λ = 2πN.
Consequently
 |f♯(0)|² ≤ C(N)·ℓ(g),  C(N) := C_1λ / (2(1 − χ_0(2πN))).  (2.1)

*Proof.* f − φ has support in [−λ,λ] for every φ ∈ L²_0. By Slepian–Landau–Pollak (CITED),
‖Q𝓕h‖² ≥ (1 − χ_0(2πN))‖h‖² for h ∈ L²[−λ,λ]; the factor ½ for parity is absorbed in the 2 of ℓ. With h = f♯ and
‖f♯‖ ≥ ‖f_out‖ (f♯ = f_out outside I) the first inequality follows; (2.1) follows from Lemma 1.1. □

Asymptotics (CITED, Slepian 1965): 1 − χ_0(c) ~ 4√π c^{½}e^{−2c}. Hence C(N) ≍ λ N^{−½}e^{4πN}. For N = 15:
e^{4π·15} ≈ 10^{82}.

**Corollary.** ℓ(g) > 0 for every g ≠ 0 of the core (PROVED) — this is positivity of the leak, not a sign of W.

### 2.2 Theorem Π.5(b) (the constant is not uniform; PROVED except for absolute constants)

sup_{g ∈ core, g ≠ 0} |f♯(0)|²/ℓ(g) ≥ c_* N^{−a}e^{(4π−o(1))N} for some fixed a. In particular **no C independent
of μ exists**.

*Construction.* Let ψ_0, ψ_2 be the first two even prolates of (time [−λ,λ], band (−λ,λ)), extended to ℝ as
functions of band (−λ,λ). Let F := ψ_0 − aψ_2 with a := ∫ψ_0/∫ψ_2 (∫ψ_2 ≠ 0 generically; otherwise use ψ_4), so
that 𝓕F(0) = ∫F = 0, and F(0) ≠ 0 (ψ_0(0)ψ_2(0)-generic; normalizable to F(0) = 1 by scaling). Then:
- F is of band (−λ,λ) and ∫F = 0, so, as a function on ℝ, its tail Q𝓕F = 0: the "leak" of F is zero and its
  minimal-leak representative is F itself, with F(0) = 1 (this is the situation of AUDIT_PIMU: an element of the
  closure, φ(0) ≠ 0, ℓ = 0).
- F does not come from the core (it has no compact support). But τ² := ‖F·1_{|u|>λ}‖² ≤ (1−χ_0)+a²(1−χ_2) =
  e^{−4πN}·poly(N).
- The image of the core in L²(J) is dense (E is a bijection between g on (−T,T) and f on (0,λ) via finite Möbius;
  the core constraints have finite codimension and are closed under spikes, as in Π.0′(c)). Take g_n with
  f_out,n → F|_J.
- Continuity: ℓ^{½} is a √2-Lipschitz seminorm in f_out and ℓ(F) = 0, hence ℓ(g_n) → ℓ(F|_J) ≤ 2τ². And
  |f♯_n(0) − 1| ≤ |Λ_N|·τ ≤ (C_1λ)^{½}τ → 0 (Λ_N continuously extended to L²(|u|>1/λ), Lemma 1.1).
Thus |f♯(0)|²/ℓ ≥ (1 − (C_1λ)^{½}τ)²/(2τ²) ≍ e^{4πN}/poly(N). □

Reading: (a) and (b) agree on the exponent 4πN. **The natural scale of the Tate mode is e^{4πN} times the leak.**
This is exactly the closure phenomenon of AUDIT_PIMU, now quantified: in the core, ℓ = 0 is not attained, but
f♯(0) = O(1) is compatible with ℓ ~ e^{−4πN}.

### 2.3 On the reading "Π.5 false due to the closure"

The task's proposal (ℓ = 0 with f♯(0) ≠ 0) is correct in the **closure** of the classes (F of §2.2), not in the
core: in the core, Π.5(a) proves ℓ > 0 and the inequality with finite C(N). What fails is not Π.5 for fixed N, but
its "at-scale" use: any argument that needs C = O(1), or even C = poly(N), is NO-GO. The "algebraic gauge" version
(φ(0) = 0 imposed) gives f♯(0) = 0 tautologically but has no minimizer (AUDIT_PIMU), so it does not define f♯.

## 3. Consequences

**For R-Π4.** R-Π4 ("f♯(0)² cannot be taken as a leak-scale term") moves from restriction to **theorem** (Π.5(b)):
the term −2a₀𝒲⁰(g,𝔪) − a₀²λ⁻¹(2+γ−log4π) of PI4 (2.3), with a₀ = ½f♯(0), is only controlled by C(N)ℓ, with
C(N) ≍ e^{4πN}. The Tate mode is a second falsifier of P2 in the quotient (together with the jump σ, Π.0′(c)):
P2 cannot read 𝒲 on Ψ̌_{f♯} with leak-scale constants.

**For MORI15.** The ℓ* ∈ [4.4, 8.5]·10⁻⁷⁰ was computed with the polynomial family that imposes f*(0) = 0
(a₄² = 3.32 "fixed by f(0) = 0"). Since the infimum of def:ext is over 𝒢̄_T (without that constraint), ℓ* is an
**upper bound** of the true ℓ of g* (PROVED: infimum over a larger set). Π.5(a) gives the lower bound
ℓ(g*) ≥ 2(1−χ_0(30π))‖f*_out‖² ≈ 10^{−82}·‖f*_out‖² (with the caveat that g* is not in the core, g*(T) ≠ 0; (a)
only uses support in [−λ,λ], so it still holds). Hence
 ℓ_true(g*) ∈ [~10^{−82}‖f*_out‖², 8.5·10^{−70}]  (PROVED in form; NUMERICAL constants to be checked),
and f♯*(0) = O(1) is not excluded: (2.1) allows |f♯*(0)|² up to ~10^{12}·ℓ*·λ. The value of ℓ* as a "value" is
WITHDRAWN; as an upper bound it stands. The test of PI4 §5 (computing f♯*(0) and the true ℓ without the
constraint) remains the only way to fix it and is NUMERICAL.

## 4. Labels

| item | label |
|---|---|
| f♯(0) well defined, f♯ = c + Bf♯ on I, f♯(0) = −φ_opt(0) | PROVED |
| Λ_N bounded, |Λ_N|² ≤ C_1λ | PROVED (absolute constant not made explicit) |
| Π.5(a): ℓ ≥ 2(1−χ_0(2πN))‖f_out‖², |f♯(0)|² ≤ C(N)ℓ | PROVED (Slepian CITED) |
| Π.5(b): C(N) ≥ e^{(4π−o(1))N}/poly(N); no C uniform in μ | PROVED (genericity ∫ψ_2 ≠ 0, F(0) ≠ 0: ARGUED, avoidable with ψ_{2k}) |
| R-Π4 as a theorem | PROVED |
| MORI15's ℓ* = upper bound; range [10^{−82}‖f*_out‖², 8.5e−70] | PROVED in form / NUMERICAL in constants |
| sign of W, L′♯, row D | OPEN (this lemma gives no sign) |

## 5. Entry for the index

- **PI5_TATE_001 (round 26b).** Π.5 |f♯(0)|² ≤ Cℓ: PROVED for each N with C(N) ≍ λN^{−½}e^{4πN} (Slepian
  coercivity on [−λ,λ], c = 2πN); NO-GO uniform in μ (prolates with ∫ = 0 give ℓ ~ e^{−4πN}, f♯(0) = 1). R-Π4
  becomes a theorem; MORI15's ℓ* is an upper bound. Do not retry: controlling the Tate mode or the jump by ℓ with
  poly(N) constants.

## Summary (≤150 words)

f♯ = f − φ_opt (gauge in the closure) is constant + band-limited on I, so f♯(0) = −φ_opt(0) is defined and is an
L²-bounded functional of f_out. Π.5 is TRUE for each N: since f♯ has support in [−λ,λ], Slepian gives
ℓ ≥ 2(1−χ_0(2πN))‖f_out‖² and |f♯(0)|² ≤ C(N)ℓ with C(N) ≍ e^{4πN}. It is FALSE uniformly in μ: a combination of
prolates with ∫ = 0 and value 1 at 0, approximated from the core, has ℓ ~ e^{−4πN}. The reading "false due to the
closure" holds only in the closure (ℓ = 0 is not attained in the core). R-Π4 stands as a theorem: the Tate mode is
not at leak scale. MORI15's ℓ* is an upper bound (constraint f(0) = 0 imposed); the true ℓ is in
[~1e−82‖f*_out‖², 8.5e−70]. No sign; L′♯ and row D OPEN.
