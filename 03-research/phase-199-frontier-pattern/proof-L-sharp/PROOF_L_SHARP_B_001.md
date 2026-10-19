# PROOF_L_SHARP_B_001 — Strategy B: can Mori's certificate be made uniform in μ?

Phase 199, prover memo (pen and paper; the only arithmetic is on cited numbers). Target: Lemma L′♯ (AUDIT_199):
∃κ>0, A≥0: ∀μ≥5, ∀g = E f: W_T(g) ≥ κμ^{−A}ℓ(g). Strategy B: find the uniform content of the one non-uniform step
(S7) of the Liu–Mori chain and prove it for all μ, which would give K_κ and hence the κ-band (MECH_001 Prop 2.1).
No zero data is used beyond citation. Labels:
PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMÉRICO.

Notation (Mori VII §3, VIII §2). L = T, I = [−L,L], μ = e^{2L}, H = L²(I). Ff(t) = ∫f e^{itx}. c_f(a) := Re(f⋆f̃)(a) =
Re∫f(x)\overline{f(x−a)}dx (even in a, c_f(0) = ‖f‖², c_f = 0 for |a| ≥ 2L). a(t) = Re ψ(¼+it/2) − log π.
Q = W_T is the complete form (Paper 47 def. of W_T = 𝔞_T + 2Re(A B̄); Mori's (1.1)):
Q(f) = 2|⟨f,cosh(x/2)⟩|² − 2|⟨f,sinh(x/2)⟩|² + (1/2π)∫a(t)|Ff|²dt − ⟨f,C_p f⟩,
C_p = Σ_{n<μ}Λ(n)n^{−1/2}(S_{log n}+S_{−log n}), ⟨f,C_p f⟩ = Σ_{n<μ}2Λ(n)n^{−1/2}c_f(log n), A_T = Σ_{n<μ}2Λ(n)n^{−1/2}.
Mori's parameters: s ≥ ‖C_p‖ (Schur), m>0, γ = s+m, M = γI − C_p; Ω with C = log(Ω/2π) − 1/Ω − γ > 0; c = ΩL;
B = B_band (kernel sin(Ω(x−y))/(π(x−y)) on I); K = pole + (1/2π)∫_{−Ω}^{Ω}(a−γ)|e_t⟩⟨e_t|; T_tail(f) = (1/2π)∫_{|t|>Ω}(a−γ)|Ff|²;
U = u_0|h_0⟩⟨h_0| + u_1|h_1⟩⟨h_1| (rank 2, h_j = (I−B−δ)v_j, u_jE_j ≤ C); V = K+U. Values: μ=12: s=57/16, m=½, Ω=416,
C≈0.128, N=832; μ=15: s=66/16, m=½, γ=37/8, Ω=736, c≈996.6, C≈0.137, N=1664 (CITED).

## 0. Corpus check (rule )
- **Index read:** README families l.50 (coercivity/Schur: walls W-lin … W-mom), l.52 (Euler/Möbius algebra: N_018), l.104
  (certified Schur induction with underived tail constant: dead), MECH_001/AUDIT_12 entry (l.450), BARRIER_EST_001
  (phase 197, Thm 4), AUDIT_ZENODO_FRONTIER, PATTERN_001.
- **Paper 47 read:** def:W, prop:env (i)–(iii), prop:archneg, cor:margin1, rem:moriceiling.
- **Mori read:** VII §1.2, §3.1–3.3, (3.1)–(3.4), Prop 3.1, Lemma 3.2, §4–§5; VIII §1–§2 (parameters); VI (1.1), Lemma 3.3.
- **Why this is not a retry.** MECH_001 did the scaling of S0–S7 and *named* the uniform target; it did not open S7. This
  memo opens S7: it identifies the exact quadratic form that the finite matrix tests (§1), its block structure (§2), the
  one exact Λ-cancellation available inside it (§3), and proves what any uniformization must bound (§4). It is an
  analysis of a method class, with proofs; it launches no construction. The exact cancellation of §3 (pole against the
  Chebyshev main term) is classical and is used here only to *locate* where the sign lives; the index records no attempt
  to uniformize the Liu–Mori finite test itself.

## 1. (i) What S7 tests, exactly

**1.1 The matrix.** In the Legendre basis v_j = √((2j+1)/2L)·P_j(x/L), j<N, E: ℂ^N→H, P = EE*, Mori certifies in each
parity (VII (3.4))
  T_N := W(X)^{−1} + J − αI − β(B − A²) ≻ 0,  A = E*ME, B = E*M²E, J = E*VE, W(X) ⪰ G = E*M^{−1}E,
with α, β the Schur-complement error budgets of Lemma 3.2 (e, n, h ~ e^{c(ρ−ρ^{−1})/2}ρ^{−N}, uniform in L, CITED).
By (3.3), T_N ≻ 0 ⟹ G^{−1}+J ⪰ αI+βD_M ⟹ M+V ⪰ 0 on H. So S7 is a finite sufficient test for

  **(B_μ):  M + V ⪰ 0 on L²(I).**

**1.2 The form (B_μ) tests, without Legendre or N.**

**Lemma 1.1 (PROVED; bookkeeping of Mori VII (3.2)).** For every f in the C² core,
  ⟨f,(M+V)f⟩ = Q(f) − T_tail(f) + ⟨f,Uf⟩,
and M + V = [pole + (1/2π)∫_{−Ω}^{Ω}a(t)|e_t⟩⟨e_t|dt − C_p] + γ(I − B) + U.
*Proof.* Q = ⟨f,(M+K)f⟩ + T_tail by definition of K and T_tail; V = K+U. For the second form:
M+K = γI − C_p + pole + (1/2π)∫_{−Ω}^{Ω}(a−γ)|e_t⟩⟨e_t| and (1/2π)∫_{−Ω}^{Ω}|e_t⟩⟨e_t|dt = B. □

**Corollary 1.2 (PROVED).** (a) (B_μ) ⟺ Q(f) ≥ T_tail(f) − ⟨f,Uf⟩ for all f ∈ L²(I).
(b) λ_min(M+V) ≤ λ^W_T − Cδ. In particular (B_μ) is strictly stronger than window positivity, and K_κ ⟹
λ^W ≥ κ₋(1−λ₄) + Cδ.
(c) On vectors with T_tail(f) ≤ ε‖f‖²: ⟨f,(M+V)f⟩ ≥ (Q(f)/‖f‖² − ε)‖f‖².
*Proof.* (a) is Lemma 1.1. (b): T_tail ≥ Cδ‖f‖² + ⟨f,Uf⟩ (Prop 3.1), so ⟨f,(M+V)f⟩ ≤ Q(f) − Cδ‖f‖². (c) U ⪰ 0. □

So the uniform content of S7 is an **x-space leakage coercivity**:

  **Lemma L_x(Ω) (OPEN):** Q(f) ≥ (1/2π)∫_{|t|>Ω}(a(t)−γ)|Ff(t)|²dt − u_0|⟨h_0,f⟩|² − u_1|⟨h_1,f⟩|²  ∀f ∈ L²(I),

with Ω = Ω(μ) ≥ 2πe^{γ}, γ ≥ ‖C_p‖ (Prop 1.1 of MECH_001: Ω superpolynomial in μ). L_x(Ω) ⟺ (B_μ) (Cor 1.2(a)).
It is the same kind of statement as L′♯ (the form dominates an out-of-band energy), with two differences: the band is
Ω(μ) in x-space, not λ in u-space; the weight a−γ is ≥ C ≈ 0.13 only just beyond Ω and grows like log(t/Ω).

**1.3 Prolate coordinates.** Let ψ_k (k ≥ 0) be the prolate functions of I with c = ΩL, Bψ_k = λ_k(c)ψ_k. Then
  ⟨f,(M+V)f⟩ = ⟨f,(pole + A_b − C_p)f⟩ + γΣ_k(1−λ_k(c))|⟨ψ_k,f⟩|² + ⟨f,Uf⟩,   A_b := (1/2π)∫_{−Ω}^{Ω}a|e_t⟩⟨e_t|.
The γ-term is diagonal: ≈ 0 for k < 2c/π − O(log c), ≈ γ beyond (Landau–Widom, CITED). Hence (B_μ) is, up to the
compensators, the statement that pole + A_b − C_p is nonnegative on the ≈ 2c/π = 2ΩL/π near-band-limited prolate
modes, which is why N ≳ 2ΩL/π (MECH Prop 1.1(v)).

## 2. (ii) Block decomposition and sign structure

| block | rank / symbol | operator-norm size | sign | label |
|---|---|---|---|---|
| pole 2\|⟨f,cosh⟩\|² − 2\|⟨f,sinh⟩\|² | rank 2 | 2(L+sinh L) ≈ √μ on even, 2(sinh L − L) ≈ √μ on odd | **+ on even, − on odd** | PROVED |
| A_b (band archimedean) | symbol a(t), \|t\|≤Ω | a(0) = ψ(¼)−log π = −5.37 … a(Ω) ≈ γ+C | **indefinite**: a<0 for \|t\|<t₀≈2π, a≥0 beyond | PROVED (a increasing, Mori VI Lemma 3.3) |
| −C_p (prime) | symbol −Σ2Λ(n)n^{−1/2}cos(t log n) on L²(ℝ) | ‖C_p‖ ≤ A_T = (4+o(1))√μ; ⟨v₀,C_pv₀⟩ = (8+o(1))√μ/log μ | indefinite, sup of symbol = A_T (prop:env(ii)) | PROVED/CITED |
| γ(I−B) | diag γ(1−λ_k(c)) in prolates | ≤ γ ≈ A_T-scale | ⪰ 0, ≈ 0 in band | PROVED |
| U | rank 2 | ≤ u₀E₀+u₁E₁ ≤ 2C ≈ 0.27 | ⪰ 0 | PROVED |
| Cδ | scalar | e^{−2(c+1)}/(4(c+1)(c+4)) | > 0 | CITED (Thm N) |

**Three corrections to the brief's expected picture (PROVED).**
1. *The archimedean block is not positive definite, uniformly or otherwise.* The full archimedean complete form
   (pole + full a) is negative on L²(I) for every T ≥ 0.4608 (Paper 47 prop:archneg, CITED), and A_b alone has
   symbol −5.37 at t = 0. The only uniformly nonnegative pieces are the compensators γ(I−B), U, Cδ, which live outside
   the band, where Q is positive anyway (a(t) ≥ γ+C there).
2. *The prime block is of the same size as the pole block,* √μ, and on low frequencies the two are both of size
   8√μ/log μ with opposite signs on the even sector and the same sign on the odd sector (on odd f both the pole and
   the prime term at shifts near 2L are negative; there −C_p at shifts a ≈ 2L is positive because c_f(a) < 0 for odd f).
   The norm-level sum Σ_{n<μ}Λ(n)n^{−1/2} is (2+o(1))√μ by PNT, not 2√μ/log μ; the /log μ appears only in the
   Rayleigh quotient on the constant (weight 1 − log n/log μ).
3. *The operator-norm bound ‖C_p‖ ≤ s is used only to fix γ and hence Ω;* it plays no role in the sign of the band
   block. For every comb a ≥ 0 the same Schur test holds, so steps S1–S2 are comb-generic (MECH §4). The in-band
   balance pole + A_b − C_p has three terms of size √μ, √μ/log μ·O(1) and √μ, with no slack of norm type: positivity
   of (B_μ) is a cancellation statement, not a domination statement.

## 3. (iii) The cancellation that the certified block exploits

**3.1 The exact cancellation (pole against the Chebyshev main term).**

**Lemma 3.1 (PROVED, classical).** For every f ∈ L²(I),
  2Re(A B̄) − 2∫_1^μ t^{−1/2}c_f(log t)dt = ∫_{−2L}^{2L}e^{−|a|/2}c_f(a)da = (1/2π)∫|Ff(t)|²/(¼+t²)dt ≥ 0,
and therefore
  **Q(f) = (1/2π)∫ ã(t)|Ff(t)|²dt − R_Λ(f),  ã(t) := Re ψ(5/4+it/2) − log π,  R_Λ(f) := 2∫_1^μ t^{−1/2}c_f(log t)d(ψ(t)−t).**
*Proof.* 2Re(AB̄) = 2Re∫∫f(x)\overline{f(y)}e^{(x−y)/2} = 2∫c_f(a)e^{a/2}da = ∫(e^{|a|/2}+e^{−|a|/2})c_f(a)da (c_f even).
The substitution t = e^a gives 2∫_1^μ t^{−1/2}c_f(log t)dt = 2∫_0^{2L}e^{a/2}c_f(a)da = ∫e^{|a|/2}c_f(a)da. Subtract.
The Fourier transform of e^{−|a|/2} is 1/(¼+t²), and ∫e^{−|a|/2}c_f = (1/2π)∫|Ff|²/(¼+t²) by Plancherel. Finally
⟨f,C_pf⟩ = 2∫_1^μt^{−1/2}c_f(log t)dψ(t), and a(t) + 1/(¼+t²) = Re[ψ(z) + 1/z] − log π = Re ψ(z+1) − log π at z = ¼+it/2. □

Reading. The residue of −ζ′/ζ at s = 1 (the drift dt of dψ) is cancelled *exactly* by the pole term, for every f, and
the leftover is the s = 0 pole, which shifts the digamma argument by one: ã(0) = ψ(5/4) − log π = −1.37 (instead of
−5.37), ã(t) = 0 at t ≈ 5.8, ã(t) = log(t/2π) + O(t^{−2}) beyond. So after the exact cancellation the √μ-size blocks
are gone and the form is

  Q = (archimedean form with weight ã, negative only on |t| ≲ 5.8, of size O(1)) − (Chebyshev remainder form R_Λ).

The sign of Q on low-frequency vectors is decided by R_Λ: for f = v₀ at μ = 15, R_Λ(v₀) = 3.312 − (8√15/log 15 − 4 −
8/log 15) = 3.312 − 4.49 = −1.18 (audit table + MECH Prop 1.1(iii)), while the ã-form on v₀ is ≈ −1.1 (ã between
−1.37 and −0.4 on the Fejér mass |t| ≤ 4): Q(v₀) ≈ +0.1. The constant direction is nearly tight, and its positivity is
the statement ψ(t) < t "on average with weight t^{−1/2}(1 − log t/log μ)" on [1,μ]: a Chebyshev-bias statement.

**3.2 Is the remainder form small?** Not in operator norm.

**Lemma 3.2 (PROVED).** The symbol of R_Λ on L²(ℝ) is r(t) = 2Re∫_1^μ t′^{−1/2−it}d(ψ(t′)−t′) = s_Λ(t) − 2Re[(μ^{½−it}−1)/(½−it)],
s_Λ(t) = Σ_{n<μ}2Λ(n)n^{−1/2}cos(t log n). Hence sup_t|r(t)| ≥ A_T − O(√μ/t₁) at any t₁ with s_Λ(t₁) ≥ A_T − o(√μ)
(Kronecker; such t₁ exist by prop:env(ii)), so ‖R_Λ‖_{L²(ℝ)} = (4+o(1))√μ, and the compression to I has norm between
|R_Λ(v₀)| = O(1) and A_T. □

So R_Λ is O(1) at low frequency and of full size √μ at resonant frequencies; the ã-weight must beat it there, which it
does pointwise only for ã(t) = log(t/2π) ≥ A_T, i.e. t ≥ 2πe^{A_T} = τ_env (prop:env). This is exactly why Mori's
Ω ≥ 2πe^{γ}: beyond Ω the archimedean weight dominates the *worst-case* symbol of the prime block, and there the test
is comb-generic. In the band, positivity is restored only by the window averaging at resolution π/L (Theorem X of
phase 186, walls W-*), and that is the non-robust part.

**3.3 Candidate (b): bound R_Λ by a prime-number estimate.**

**Proposition 3.3 (PROVED).** Let E be any function with |ψ(t) − t| ≤ E(t) on [1,μ], proved for a class of
measures ν on [1,μ] containing a TV-ball of radius r_E around ν_Λ (this holds for every estimate whose proof is
uniform over such a ball, BARRIER_EST Def. 1; for the zero-free-region and Vinogradov–Korobov bounds it is the
reading ARGUED there). Then the best bound derivable from E alone is
  Q(f) ≥ (1/2π)∫ã|Ff|² − |R_Λ(f)| with |R_Λ(f)| ≤ 2‖f‖²·sup_{[1,μ]}E(t)t^{−1/2} + 2∫_1^μ E(t)|d(t^{−1/2}c_f(log t))|,
and its slack is ≥ 2r_E‖f‖². It is a TV-robust premise.
*Proof.* Integrate by parts in the Stieltjes integral R_Λ; the boundary term at t = 1 is 2(ψ(1)−1)c_f(0) = −2‖f‖²,
and any ν in the class with the same bound gives the same inequality. □

**Honest size comparison (arithmetic on cited numbers; the floor r_E ≥ 10^{−10}μ is ARGUED: no proved explicit
bound on |ψ(x) − x| is below 10^{−10}x in absolute size on any range, and the first-order slack of any such bound is at
least its own value at x = μ).**

| μ | required precision ≈ λ^W (certified/NUMÉRICO) | slack floor 2r_E ≥ 2·10^{−10}μ | ratio |
|---|---|---|---|
| 5 | ~10^{−17} (λ^W ≥ 10^{−18} certified, Paper 47) | ≥ 10^{−9} | ≥ 10^{8} |
| 10 | 8.4·10^{−44} (Mori VI, certified finite margin) | ≥ 2·10^{−9} | ≥ 10^{34} |
| 15 | 2.4·10^{−70} (Mori VIII) | ≥ 3·10^{−9} | ≥ 10^{61} |
| 100 | ~10^{−529} (PATTERN model) | ≥ 2·10^{−8} | ≥ 10^{520} |

The ratio grows like e^{4πμ}. The remainder bound is never below the margin scale, at any μ ≥ 5, by at least eight
orders of magnitude. Candidate (b) therefore gives "positivity up to O(remainder)" with a remainder ≫ margin:
**NO-GO as a uniformization of S7 (PROVED by Lemma 4.1 below, given the floor).**

**3.4 Candidate (a): the explicit-formula pairing on the finite block.**

**Proposition 3.4 (PROVED as an identity; CITED: Guinand–Weil, Mori VI §2).** Let dN be the zero-counting measure
(zeros ρ = ½+iγ counted with the pairing of Mori (1.1); no hypothesis on their position), dN_s := a(t)dt/2π its smooth
part (dN_s = dθ/π with θ the Riemann–Siegel phase, since θ′(t) = a(t)/2), and dS := dN − dN_s. Then for every f in the
core
  ⟨f,(M+V)f⟩ = Q_{≤Ω}(f) + ∫_{|t|>Ω}|Ff|²dS(t) + (γ/2π)∫_{|t|>Ω}|Ff|²dt + ⟨f,Uf⟩,
where Q_{≤Ω} is the explicit-formula zero sum truncated at height Ω.
*Proof.* Q = ∫|Ff|²dN (explicit formula). T_tail = ∫_{|t|>Ω}|Ff|²(dN_s − γdt/2π). Insert into Lemma 1.1. □

What it would take to make (B_μ) uniform by this route: (1) Q_{≤Ω(μ)} ⪰ 0, i.e. zero data up to height Ω(μ) → ∞;
(2) a bound on the high-pass prime form ∫_{>Ω}|Ff|²dS by (γ/2π)∫_{>Ω}|Ff|² — this is the comb beyond the window
(the high-pass of f is not compactly supported, so all primes enter), controlled by the *smooth* zero density: a
Backlund-type statement about S(t) in quadratic-form sense. Item (1) is finite in Ω: with the verified height
3·10^{12} (Platt–Trudgian, CITED) and Ω ≥ 2πe^{⟨v₀,C_pv₀⟩}, (1) is available only for μ ≲ 650 (T ≲ 3.2), and it is zero
information (index family "Información de ceros"); the all-μ version is not a method of our class and is not invoked.
Item (2) is uniform in nothing we can prove: the high-pass form carries the full Dirichlet series. **Rejected as a
uniform inequality on the finite block,** per the brief's criterion; recorded because it identifies the content of
(B_μ): "the zero sum up to height Ω(μ) is ≥ 0, and beyond Ω the smooth density beats the prime fluctuation."

**3.5 Candidates (a) and (b) coincide.** By von Mangoldt's formula, R_Λ(f) = (1/2π)∫ã|Ff|² − Q(f) = (ã-form) −
(zero sum): the Chebyshev remainder form *is* the zero sum (identity, CITED). "Bound the remainder" and "bound the
zero sum" are the same request; the only exact Λ-arithmetic beyond identities that enters either is the sign of the
zero sum, which is the target. Mori's numerics exploit no further cancellation: the certificate is the exact evaluation
of the N×N block at ≥ 4πμ/ln 2 bits, with every Λ-specific entry a finite sum Σ_{n<μ}Λ(n)n^{−1/2}⟨v_j,S_{±log n}v_k⟩.

## 4. (iv) The obstruction, stated exactly

**Lemma 4.1 (barrier for the complete form and for (B_μ); PROVED).** Let 𝒬 be any quadratic form on L²(I) of the
shape 𝒬_ν(f) = 𝒜(f) − ∫c_f(u)dν(u) with 𝒜 independent of the comb ν (this covers Q, M+V, and the finite block T_N
up to the fixed γ), and let λ_min(𝒬_{ν_Λ}) = m_0 > 0 with bottom vector g_0. For every m > m_0/2·(1+ε) there is a
measure ν′ with ‖ν′−ν_Λ‖_TV = m and 𝒬_{ν′}(g_0) < 0.
*Proof.* c_{g_0}(u) → ‖g_0‖² = 1 as u → 0; pick u_0 ∉ {log n} with c_{g_0}(u_0) ≥ (1+ε)^{−1} and ν′ = ν_Λ + mδ_{u_0}
(symmetrized). Then 𝒬_{ν′}(g_0) = m_0 − 2mc_{g_0}(u_0) < 0. □
This is BARRIER_EST Thm 4 for the complete form, which AUDIT_199 asked for as item (i); the proof is verbatim, and for
(B_μ) the fixed γ = s+m_Mori is admissible since m < m_Mori/2 keeps ‖C_{ν′}‖ ≤ s + m_Mori.

**Theorem 4.2 (no uniformization of S7 by comb-robust inputs; PROVED, with the CITED ceiling).**
Let 𝒫 be a proof of (B_μ) for all μ ≥ μ_0 whose only Λ-specific premises hold uniformly on TV-balls of radius r(μ)
around ν_Λ (Schur bounds, PNT-type bounds, zero-free regions used through |ψ−t|, any inequality of §3.3). Then
  r(μ) ≤ ½(1+ε)λ_min(M+V) ≤ ½(1+ε)(λ^W_T − Cδ) ≤ 1.8·10^{24}μ^{9/2}log μ·e^{−4πμ}  (50 ≤ μ ≤ 10^4, rem:moriceiling),
and at the certified windows r ≤ 4.2·10^{−44}, 6·10^{−55}, 1.2·10^{−70} (μ = 10, 12, 15). No input of §3.3 satisfies
this at any μ ≥ 5 (table), and none can for large μ because every unconditional remainder is ≥ √μ e^{−c(log μ)^{3/5}} ≫
e^{−4πμ}.
*Proof.* Lemma 4.1 with 𝒬 = M+V and Cor 1.2(b). □

**Check that the finite margins sit at the e^{−4πμ} scale (PROVED arithmetic on cited numbers).** log₁₀ of the
certified margins: μ=10: −43.1; μ=12: −53.9 (even), −49.8 (odd); μ=15: −69.6 (even), −65.4 (odd). Slopes per unit μ:
−5.3 (10→12), −5.23 (even, 12→15), −5.2 (odd, 12→15). Predicted by κμ^{9/2}e^{−4πμ}: −4π/ln 10 + 4.5·log₁₀(15/12)/3
= −5.46 + 0.15 = −5.31. Agreement within 2%. So the bottom of the finite block *is* the bottom of Q (the compensators
contribute nothing at the bottom), and S7 resolves λ^W itself.

**The exact quantity that must be bounded, and why current tools fail.** Write, on the N(μ)-dimensional Legendre
space (N ≈ 1.67·ΩL, Ω ≥ 2πexp((8+o(1))√μ/log μ)),
  T_N = Ã_N − R_N + Γ_N,   Ã_N = block of the ã-form (explicit, indefinite on |t| ≲ 5.8, symbol log(t/2π) beyond),
  R_N = block of R_Λ (entries 2∫_1^μ t^{−1/2}⟨v_j,S_{log t}^{sym}v_k⟩d(ψ(t)−t), all Λ-information),
  Γ_N = γ(I−B) + U + Cδ − Schur-complement budgets (explicit, ⪰ −αI − βD_M).
One must prove λ_min(T_N) ≥ 0 where λ_min(T_N) ≈ κμ^{9/2}e^{−4πμ}. Tools and their precision:
- Schur / operator norm on R_N: slack O(√μ). Comb-generic.
- PNT-type bounds on R_N (any E with |ψ−t| ≤ E): slack ≥ 2r_E ≥ 10^{−10}μ (ARGUED floor), and ≥ √μe^{−c(log μ)^{3/5}}
  asymptotically (PROVED for VK-type E). Comb-robust, hence excluded by Thm 4.2.
- Identities (Λ⋆1 = log, Möbius, Euler product, functional equation): exact, but they rewrite R_N as Ã_N − (zero-sum
  block) (Prop 3.4 / §3.5), i.e. as T_N itself. Under the N_018 meta-theorem (identities + Bochner/C–S), no sign.
- Zero data: finite height; bounds μ ≲ 650 for this route; outside the class.
- Exact finite evaluation at ≥ 4πμ/ln 2 bits on N ~ e^{8√μ/log μ} modes: Mori's S7. One μ at a time; cost
  superpolynomial (MECH Prop 1.1).

## 5. Consequences for L′♯ and K_κ
- **K_κ not obtained.** Strategy B reduces K_κ to L_x(Ω) (Cor 1.2), which is (B_μ) itself; no uniform inequality.
- **L′♯ remains OPEN.** Nothing here touches the u-space formulation except the following comparison (ARGUED): L_x(Ω)
  and L′♯ are both leakage-coercivity statements for the same form; L_x has a superpolynomial band Ω(μ) and a weight
  that is only ≥ C ≈ 0.13 at the band edge; L′♯ has the natural band λ = √μ and asks for a polynomial constant.
  Transport by E (Prop 3.1 of MECH, norms ≤ 2√μ) relates the leakages only up to the factor 4μ, which is polynomial,
  so a proof of either one at polynomial loss would give the other in the weak form λ^W > 0 ∀T; but neither is
  closer to a proof by this.
- **Strategy B as a method class — NO-GO (PROVED, Thm 4.2):** "make Mori's certificate uniform by comb-robust
  estimates" cannot work at any μ ≥ 5. What is not excluded: a non-robust, Λ-exact argument that is not an identity
  (the index's residue: coercivity of the exterior residual form, MECH §4; semiring principle). This memo does not
  supply one.
- **Falsifier consistency.** Lemma 3.1 holds for every comb with the pole term fixed: for ν = cΛ the cancellation leaves
  (1−c)∫e^{|a|/2}c_f, of size (1−c)√μ, and the sign of Q at low frequency flips for c > 1 (consistent with
  CERT_FALSIFIERS, λ^W(cΛ) < 0). The cancellation is exact in the residue only; it does not see the e^{−4πμ} scale,
  as Thm 4.2 requires.

## 6. Labels
- PROVED: Lemma 1.1, Cor 1.2, the §2 table and its three corrections, Lemma 3.1 (classical), Lemma 3.2, Prop 3.3,
  Prop 3.4 (as an identity), Lemma 4.1 (barrier for W and for (B_μ); discharges AUDIT_199 item (i)), Thm 4.2 (given
  the CITED ceiling for μ ≥ 50 and the certified margins for μ ≤ 15), the slope check.
- CITED: Mori VII (3.1)–(3.4), Prop 3.1, Lemma 3.2, Theorem N; Mori VIII parameters; Paper 47 prop:env, prop:archneg,
  rem:moriceiling (PLAUSIBLE-UNVERIFIED there, zero data); Guinand–Weil; Landau–Widom; Platt–Trudgian height.
- ARGUED: the floor r_E ≥ 10^{−10}μ for explicit PNT bounds (reading of the literature); L_x ↔ L′♯ comparison.
- NUMÉRICO: PATTERN model value at μ = 100; "~10^{−17}" at μ = 5.
- OPEN: L′♯, K_κ, L_x(Ω).
- NO-GO (PROVED): Strategy B = uniformization of S7 by TV-robust premises; candidates (a) and (b) of the brief as
  uniform inequalities.
- No sign is claimed. Row D OPEN.
