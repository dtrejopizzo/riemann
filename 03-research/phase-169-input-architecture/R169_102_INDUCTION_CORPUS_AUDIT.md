# R169_102 — Corpus audit: induction in T and Eratosthenes/Legendre; check of the "single-step Eratosthenes propagation law"

*Phase 169. Pure mathematics, no numerics. No label moves.*
*Method: grep over 03-research (all phases), 04-papers, 05-meta-and-planning, NO-GO-LIST.md, master grid JSON
(`eratosthen|legendre|upward induction|ideal sieve|bootstrap|sieve flow|propagat|monotone flow|[X,X²]`), followed by reading the hits.*

## 0. Verdict

1. **The lead's law is already in the record in its exact form.** The Eratosthenes/Λ∗1 = log determination of the
   new annulus from the window is **Theorem Ψ1** (G2_B2_R2, phase 159): the "sieve flow" Ψ_{T→T′}. Ψ2 states that its
   only orbit is Λ. A scheme "J(T) ≥ 0 ⟹ J(T′) ≥ 0" that uses Ψ is closed by **Theorem NB** (G2_B2_R3, the no-bootstrap
   trichotomy; grid: `R160_S5 §2.4#32 G2_B2_R3`, DEAD, killer "Thm NB trichotomy"; `159 G2_B2`, DEAD, E1 "flow on
   orbit is identity").
   - If the domain is {Λ} (identification), the step for all T is the ∀T arrow (W15/cor:mono).
   - If the domain is a class, the scheme must be false on deletions and amplifications, and near Λ it is a singleton.
   "Used once, with a sign" is NB(b1). The step at T, ranged over T, is a proof of ∀T λ_T ≥ 0. The escapes from the
   falsifiers are correct, but they **do not create a new mechanism**: they only show that no record falsifier blocks
   the arrow, which NB already allows.
2. **The escapes are correct** (§3): M_m, f_t and DMV are all non-Eratosthenes-determined.
3. **Falsifier search: there is no Eratosthenes-determined falsifier in the record, and none is known in mathematics.**
   The determination hypothesis is weaker than the lead suggests, however. By strong multiplicity one or Sturm bounds,
   **every** automorphic L-function of fixed conductor is determined by a finite window. So the class a successful
   law would cover is far larger than {ζ, L(s,χ)}, and the law would amount to GRH-type positivity uniformly on it. The
   law must name which property of ℤ it uses beyond window-determinacy (W9/T1). Confirmed with this correction.

## 1. Hits table

| # | File | What was attempted | How it died | Eratosthenes determination in the hypothesis? |
|---|---|---|---|---|
| 1 | phase-163/R163_702_SUPRALANDAU_VERIFIED.md §3.3 | upward step D_T ⟹ D_{T+ε} (or ⟹ P_loc(·,T+2ε)) from D_{½log5} | M_m (see §2); no uniform slack (Thm M(b), R163_601 Prop 4) | **No.** The step is allowed only multiplier structure, (1.1), V(H) data and zero counting. The conclusion is "it must use the atomic prime side (S4/T2)", which **leaves Eratosthenes open** |
| 2 | phase-159/G2_B2_R1.md | naive bootstrap / renormalisation in T, rate identity dλ/dT | Prop G: uniform c ∈ L¹_loc ⟺ RH, EQUIVALENT; cites D.133 "no uniform signed Hadamard induction" | No |
| 3 | phase-159/G2_B2_R2.md | **sieve flow Ψ**: Λ(n) = log n − Σ_{d∣n,1<d<n}Λ(d) on the annulus 2T ≤ log n < 2T′ (T′−T ≤ ½log2) determines new data from the window (Ψ1); unique orbit (Ψ2); Ψ3 the flow exists for DMV and Epstein; Ψ3′ an invariant must use r ≡ 1 both as Euler product and as lattice | no candidate J; (M-Ψ)(ii) is an induction in T | **Yes. This is the Eratosthenes/Möbius determination itself** (at step ½log2 in n; the primality-only version reaches Y < X²) |
| 4 | phase-159/G2_B2_R3.md Thm NB | every scheme "state at T ⟹ state at T+δ", including Ψ-propagated data | trichotomy: (a) class: false or vacuous (FinMod, Rig, Cor R1); (b) {Λ}: ∀T arrow, data flow is identity (b2); (c) T-free statements: EQUIVALENT | **Yes. It covers Ψ explicitly (b2)** |
| 5 | phase-159/G2_B2_R4.md | Thm U (growth law, conditional on BD) | upper half only; no sign | No |
| 6 | phase-155 thm:margin, grid "Uniform margin / upward induction in T" (R160_S4 §2.D#49) | uniform margin to propagate positivity | DEAD, killer M; λ^A ≤ 4e9·T·e^{−15.4T}: the margin decays | No |
| 7 | grid R160_S3 §5#15 (finite certs ½log5, ½log6) | extend [prim] one window at a time | PARTIAL, "no upward induction in T (cor:mono)" | No |
| 8 | P46 §21.7 cor:mono / W15; P47 lem:monoT | monotonicity of λ_T is downward | structural: positivity propagates downward only | No |
| 9 | phase-166/R166_601 items 1–4, 4F | Legendre Φ(x,X) = Σ_{d∣P}μ(d)⌊x/d⌋; rough-integer positivity; identity ℰ_X(ρ*) = −ρ_X/(ρ*−1) | **tautological (E1)**: the X-family is A_X(s)ζ(s) = 0, which holds whatever the zero set is. Internal falsifier: any 0/1 Dirichlet series with a finite-Euler-factor sieve. Legendre is useful only for x ≫ 2^{π(X)}, where it does not compete with the sieve range | Yes (Legendre = Eratosthenes counting). It died because it is **iterated as an identity**, consistent with the lead's first clause |
| 10 | phase-164/R164_102 Cor L.1 | positive tail above X | pure additions ν ≥ 0 create no zero; off-line zeros require a new pole or a deletion ν₋ above X. The witness class reduces to a deletion question, OPEN | Implicit: for ℤ the tail is not free (Eratosthenes), but R164_102 does not use this |
| 11 | phase-169/R169_091 §§A3, 3, 5, Prop 5.2 | Λ on [X,Y] = Eratosthenes(window) for Y < X², so A3 really means "use integrality" | survives as the only interior: "the Eratosthenes image of the window does not resonate on Γ_S(F)"; no statement exists | **Yes** (the source of the present lead) |
| 12 | phase-104/104_99 (Eratóstenes exacto, paridad, gate energético) | π(x) = π(√x) − 1 + Φ(x,√x); parity/energy gate (row A era) | gate check script; not a row-D sign argument | Yes (counting only; no sign propagation) |
| 13 | phase-106/106_21 NESTED_CUTOFF_FLOW_STOP_GATE (l.187) | nested cutoff flow | "positivity at one finite cutoff does not propagate" (Arakelov setting) | No |
| 14 | phase-157/R157_002 rows 16, 17, 20, 30; R155_053; P47 cor:void | bootstrap (EXCL, F2), first crossing (EQUIV), classical sieve bounds as class C_BT | C_BT closed under deletion, so it decides no window > ½log2 (> 0.749 upper-bound sieve) | Sieve as **upper-bound class**, not as determination |
| 15 | R160_S4 l.162, l.301; R166_404 row 36 (bootstrap, sieve flow Ψ, Thm U → E1), row 51 (prime estimates incl. sieve → f_t theorem) | survey entries | as rows 3–4 and 14 | as above |
| 16 | NO-GO-LIST MW-2 (arithmetic propagation wall) | Re s > 1 data to the strip | wall; it concerns propagation in σ, not in T | No |
| 17 | phase-162/R162_2501 (M_m construction, Thm 3) | class obstruction | see §2 | M_m is not even a Dirichlet series (R162_2601 l.73) |

No hit uses "ideal sieve" (Dedekind) or ζ_K as a test of a T-induction. GAP-157 / phase 49 have no Eratosthenes or
induction content relevant here (no grep hit).

## 2. R163_702 §3.3: exact analysis

**Claim there.** Any step D_T ⟹ D_{T+ε} that is valid for all T and uses only (multiplier structure, (1.1), V(H)-type
verified data, zero counting) also applies to M_m, which has D_T for T < T_c(M_m) and fails after it. So the step is
false at T_c(M_m), and it "must use the atomic prime side of ζ".

**The counterexample.** ξ_m = ξ · Π_j(s−ρ_j)(s−ρ̄_j)(s−1+ρ_j)(s−1+ρ̄_j) / Π_k(s−½∓iγ_k^0) (R162_2501 §1). It has m
off-line quartets above H, and 2m on-line ζ-zeros above H removed.
- Its explicit-formula arithmetic side is: the arch term, ζ's atoms 2Λ(n)n^{−1/2}δ_{log n}, and an **absolutely
  continuous exponential density** E_m (Σ of e^{(β_j±iγ_j)u}-type terms from the rational factor), as in R162_2501 l.87.
- It is not a Dirichlet series (R162_2601 l.73) and has no Euler product. Its "new prime data" on [X,X²] are ζ's
  atoms **plus** E_m restricted there. E_m is not a function of the window atoms through any sieve. (The rational
  factor's parameters are visible in the window as a continuous density, but they are not produced by Eratosthenes
  from atoms.)

**Answer.** The argument uses a configuration that is **not** Eratosthenes-determined. The atomic part follows the
sieve; the continuous part is extraneous. So §3.3 kills only steps blind to atomicity. An Eratosthenes-using step escapes
M_m, and §3.3 says this itself ("must use the atomic prime side"). The escape is correct. §3.3 is a necessary condition,
not a NO-GO for Eratosthenes steps.

## 3. Escape claims

| Falsifier | Claim | Verdict |
|---|---|---|
| M_m | escapes: β_m continuous | **CORRECT** (§2). One caveat: the inputs used by the step must be stated on the atom/a.c. decomposition. A step written in terms of the window functional W_T alone does not see the decomposition, because M_m and ζ differ on W_T only above the contact. |
| f_t = ζ + t·g (R163_901 Thm F) | escapes: no Euler product | **CORRECT.** f_t has an atomic prime side on the semigroup generated by ℕ and {m/√M}, with frequencies log(m/√M) ∉ log ℕ. There is no unique factorisation, so Ψ1 (which needs Σ_{d∣n}Λ(d) = log n) fails off log ℕ. f_t agrees with ζ's window for T ≤ ½log λ₁, but its tail is not the Ψ-image of the window. |
| DMV (Beurling) | escapes: g-primes in [X,X²] are free | **CORRECT.** For a Beurling system the g-integers determine the g-primes, but the g-integers are not forced by smaller ones. Ψ3 builds a flow Ψ_DMV from the g-integer counting, but it does not determine new g-primes from old ones. DMV also has no FE. |
| deletion / amplification (FinMod) | not listed by the lead | They escape too: Λ1_{n≥N} violates Ψ1 at n = N·(prime). This is consistent with NB(a1). |
| Epstein ζ_Q (h > 1; off-line zeros, FE) | not listed | Escapes. There is no Euler product, so r_Q(n) is not sieve-determined. Ψ_Q exists only as the generic recursion Ψ3 (G2_B2_R2), which "determines" any Dirichlet series trivially. **Warning:** "determined by the window" in the Ψ3 sense is satisfied by every normalised Dirichlet series. The hypothesis must be specifically multiplicative (Euler + unique factorisation), or it does not separate. |

**The escapes are not the issue. Theorem NB(b) is.** Restricting to D = {Λ}, the escape makes the scheme an induction
on one sequence, whose step for all T is the ∀T arrow. Ψ-propagation is the identity on that orbit (NB(b2)). If the
scheme is instead stated on the class 𝔈 of Eratosthenes-determined Euler products, NB(a) applies. 𝔈 is not closed under
deletion or amplification, so (a1) does not kill it. NB(a2) (near Λ in weighted ℓ¹, only Λ) is compatible, since
χΛ − Λ ∉ ℓ¹_w. So a class-level Eratosthenes law over 𝔈 is **not excluded by the record**. It is also not constructed:
there is no candidate J (G2_B2_R2 "Weakest step").

## 4. Falsifier search: an Eratosthenes-determined system with an off-line zero?

Required: an Euler product over the rational primes, with the support of Λ_L ⊂ prime powers (Eratosthenes-determined),
real coefficients, ζ's Γ-factor, FE, and an off-line zero.

- **Conductor 1, degree 1, frequencies log ℕ:** Hamburger / Thm O (R162_1203, R162_407) gives only ζ. This is
  identification, not a falsifier.
- **L(s,χ), q > 1.** Support is sieve-determined. The values χ(p) = χ(p mod q) are window-determined once the window
  contains primes in each class mod q (true for X ≫ q^{O(1)}, by Linnik). So L(s,χ) is in 𝔈.
  - Real coefficients plus ζ's Γ_ℝ(s) force χ to be real and even. Odd χ has Γ_ℝ(s+1).
  - GRH is open. A Siegel zero would be an off-line zero of exactly this type, and none is known.
  - **Not a falsifier, but a constraint:** the law must hold for these too, or name the separating property (W9/T1).
- **ζ_K (ideal sieve), ζ·L(s,χ) = ζ_{ℚ(√q)}:** these have degree 2 and Γ_ℝ(s)², so they are outside "ζ's Γ-factor".
  Ideal support and values are sieve-determined over 𝒪_K. GRH is open and there is no known counterexample, so the
  same constraint applies.
- **Extension:** strong multiplicity one / Sturm bounds make **every** cuspidal automorphic L-function of fixed
  conductor window-determined, through finitely many a_p, although a_p for new p is not sieve-produced. So
  "window-determined + Euler + FE" ⊋ 𝔈. A law that uses only determinacy would prove GRH for the whole Selberg class
  of known type. A law that uses the specific sieve map (support from unique factorisation, values from residues) is
  restricted to 𝔈 = {ζ_K, Hecke/Dirichlet L of finite order}.
- **All record falsifiers with off-line zeros (DH, Epstein, f_t, M_m, DMV, deletion/finmod)** lack either the Euler
  product over ℤ or the sieve-determined tail. **No falsifier in the record is Eratosthenes-determined, and none is
  known in mathematics.** An Euler product with FE and an off-line zero would be a counterexample to GRH.

**Conclusion (confirmed, with corrections).**
- At conductor 1 with ζ's Γ-factor, the Eratosthenes-induction class is {ζ}: identification, so NB(b) applies and the
  step is the ∀T arrow.
- Over all conductors it is 𝔈, which contains even real Dirichlet L and, at higher degree, Dedekind/Hecke L. A
  successful law would prove GRH uniformly on 𝔈, which is consistent with W9.
- There is no falsifier.
- Corrections:
  - (i) "Escapes" is not a mechanism. NB(b1) still requires a step proof for each T, so the open content is exactly a
    candidate J with a sign-carrying step on 𝔈.
  - (ii) The hypothesis must be the multiplicative sieve map. Mere window-determinacy is satisfied by every Dirichlet
    series (Ψ3) or every automorphic L-function (multiplicity one), and it separates nothing.
  - (iii) M_m is evaded only if the step reads the atom/a.c. decomposition, not W_T alone.

## Ledger
| Item | Label |
|---|---|
| Hits table §1 | CORPUS (grep-verified) |
| R163_702 §3.3 uses non-Eratosthenes M_m (a.c. E_m) | PROVED (from R162_2501 construction) |
| Escapes M_m / f_t / DMV / Epstein / FinMod | CORRECT |
| Lead's law ≡ Ψ1 + NB(b) on {ζ}; on 𝔈 not excluded by NB(a) | PROVED (record) / OPEN |
| No Eratosthenes-determined falsifier in record | CORPUS + standard (would refute GRH) |
| Determinacy alone does not separate (Ψ3, multiplicity one) | PROVED / CITED |
