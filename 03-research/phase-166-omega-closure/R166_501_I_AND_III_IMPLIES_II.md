# R166_501 — (i) + (iii) ⟹ (ii), and the collapse of the Thm R transport to η = Z − Q_X

*Phase 166, round 9. No numerics, no commits. Only this file was written. No label of record changes.*
*Read first: R166_405, R166_400 (requirements (i)–(iii), families P and Q), R166_190 §0, R164_401 (Thm R, Lemma 2), R164_501 (Thm SA, Prop 3, Prop 4), R164_601 (Props 1.1–1.3, Thm 3.1), R163_502 (Q0), R163_401 §2.4, R163_801 Thm 5, R163_901 Thm F, R165_201 Thm 2.*
*Corpus check.* I grepped phases 163–166 for "falsifier class", "hypothesis class", "projective", "(i)+(iii)", and "Z − Q". The empirical statement "{i,iii} is empty in the corpus" is in R166_400. No proof of it exists in the corpus. The transport to η = Z − Q_X exists only as the conditional Rem SA.3 of R164_501 (ARGUED, conditional on (Q)). Part B below removes the condition (via Q0) and adds the room-Δ analysis.

## 0. Status table

| # | statement | label |
|---|---|---|
| Def 1 | system Σ = (Z_Σ, P_Σ), contact datum 𝔠_Σ = (T_c, F, X), mechanism 𝔐 = (H, S) with H(Σ) ⟹ S(Σ, 𝔠_Σ) a theorem | definition |
| Lem A.0 | the data map: Z_Σ determines P_Σ and conversely (Γ_ℝ fixed). "Prime data" and "zero data" are two descriptions of one object. A data *type* is a partial description: window P\|_{(−2T_c,2T_c)}, on-line part Z^on, atomic part of P, and so on | PROVED (Fourier duality, (1.1)) |
| Lem A.1 | (f_t-coincidence) assume ¬RH and fix ζ's contact T_c. For N₀ with log λ₁ > 2T_c, f_t has the same contact, the same kernel, the same witness F and nodes X, and the same window prime side as ζ, and f_t has off-line zeros | PROVED (from R163_901 Thm F) |
| **Thm A** | if 𝔐 satisfies (iii) (that is, f_t ∉ H and M_m ∉ H), then: (a) H is not a function of the window data P\|_{(−2T_c,2T_c)} (with 𝔠). (b) H is not a function of (Z^on, atomic part of P, arch, polar). (c) If H is a function of the zero side through its off-line part, then on the M_m-fibre H singles out ζ's off-line set exactly ("confinement = location": a proof of ζ ∈ H decides RH). Hence H depends on P beyond the window **and** on the non-atomic part / the quartet additions. This is (ii) in the precise form (ii′). Requirement (i) is not used | (a), (b), (c) PROVED. The reading "a proof of ζ ∈ H of type (c) is RH-strength" is PROVED when Z_ζ^off = ∅ and ARGUED in general (it is a proof-theoretic statement) |
| Cor A.1 | the corpus observation "{i,iii} is empty" (R166_400) is a theorem: {i,iii} ⊂ {i,ii,iii} | PROVED (given Thm A) |
| Lem A.2 | (projective invariance) S is invariant under F ↦ cF, c ∈ ℝ^×. A sign statement on a homogeneous polynomial functional of F therefore has even degree, and degree 0 means S does not depend on F | PROVED |
| Cor A.2 | the three requirements reduce to two. **(G)** S is a non-constant projective invariant of the witness and global in X; polynomial representatives have even degree ≥ 2, and degree-0 invariants such as phase or harmonic measure are allowed. **(N)** H depends on Λ beyond the window and sees the non-atomic/quartet part; it is not a single test of (1.1), not an identity, and not merely the positive cone of Λ (the last is W-identification by Thm R) | PROVED for the reduction. "Non-linear in Λ" is ARGUED as the remaining way out, **not** proved necessary (Rem A.3) |
| B(1) | gap: ⟨η, ĜĤ^#⟩ = 0 for G, H ∈ N̄^𝒟. Sign of η: +mult on the on-line atoms, −w_x ≤ 0 on X, complex atoms at the t_q | PROVED (Q0) |
| B(2) | no room: a test Ψ ≥ 0 on ℝ of type ≤ 2T_c, in the gap, vanishing on X, is ĤĤ^# with H ∈ E_c. Output = Rem 4.8a | PROVED (Akhiezer–Krein CITED + W ≥ 0; no S ∈ N̄ needed) |
| B(3) | room Δ > 0: Ψ ≥ 0 on ℝ of type ≤ 2T_c+2Δ, vanishing on X ⟺ Ψ = G²·KK^# with K Cartwright of type ≤ Δ and GK ∈ PW_{T_c+Δ}. ⟨η,Ψ⟩ = ⟨Z,Ψ⟩ = 𝔄(Ψ) − Π_{<2T_c+2Δ}(Ψ): the explicit formula with Λ(n), log n < 2T_c+2Δ. This is (ii) and family P | PROVED (Akhiezer–Krein, Krein's quotient theorem CITED) |
| B(4) | if moreover KK^# vanishes on every off-line quartet, then 𝔄(Ψ) − Π(Ψ) = Σ_on G(γ)²\|K(γ)\|² > 0 for K ≠ 0: Weil positivity on a subspace, true for every system. No contradiction can arise. This is R164_601 Thm 3.1 with S = 0 | PROVED (strict sign: Prop 3 of R164_501, PROVED-CITED) |
| B(5) | exact obstruction: annihilating the uncontrolled set {t_q} requires excess type, and excess type destroys the gap. With both, the identity is a consistency statement. The cause: the uncontrolled set of η is **non-real**, and positivity on ℝ says nothing at t_q | PROVED (as a conjunction of B(2)–B(4)) |
| (★_cell), RH, row D | | **OPEN** |

**Verdict.** (A) Requirement (ii) is a consequence of (iii), stated as (ii′). The proof needs no use of (i). So the R166 search space is (i)+(iii), and the corpus finding "{i,iii} = ∅" was forced, not accidental. The only non-formalizable step is the proof-theoretic one in Thm A(c): "a proof that ζ's off-line set is confined to A, with A exact on the M_m-fibre, is RH-strength". It is a theorem when Z_ζ^off = ∅. Otherwise it is ARGUED. (B) The Thm R mechanism transported to η = Z − Q_X gives one of two things. With no room it gives Rem 4.8a (E1). With room it gives family P, and it dies by the drop-term principle. The obstruction is exact: the uncontrolled part of η is supported off ℝ.

---

## 1. Formal setting

**Def 1.**
- *System.* A system is Σ = (Z_Σ, P_Σ). Here Z_Σ = Σ_ρ m_ρ δ_{t_ρ} is a locally finite point measure on ℂ with m_ρ ∈ ℤ_{>0}, invariant under t ↦ −t and t ↦ t̄. P_Σ is a tempered distribution on ℝ whose polar part and archimedean part are those of Γ_ℝ, and (1.1) holds: ⟨Z_Σ, ĝ⟩ = ⟨P_Σ, g⟩ for admissible g. Write Z^on = Z|_ℝ and Z^off = Z|_{ℂ∖ℝ}.
- *Window form.* W^Σ_T is the window form. Its *contact* is T_c(Σ) = sup{T : W^Σ_T ≥ 0}. A *witness* is F ∈ ker W^Σ_{T_c}, taken real, parity-definite and real-rooted as in R163_401 §2.4. Its nodes X are the zeros of F̂, and G = F̂ (or −iF̂).
- *Contact datum.* 𝔠_Σ = (T_c, [F], X). The witness is defined only up to a real scalar, so [F] is its projective class.
- *Mechanism.* A mechanism is a pair 𝔐 = (H, S). H is a property of systems, S is a predicate on pairs (Σ, 𝔠), and ∀Σ: H(Σ) ⟹ S(Σ, 𝔠_Σ) is a theorem. Also ζ ∈ H is a theorem that does not assume RH. "S is true for ζ" always means "true because of a proof", and the proof is H. A statement that is true for ζ but unproved is no mechanism.
- *Requirements.*
  - (i) S depends on [F] globally in X: it is not a function of finitely many node jets.
  - (iii) S(f_t, 𝔠_{f_t}) and S(M_m, 𝔠_{M_m}) are false for the falsifier families. Equivalently f_t ∉ H and M_m ∉ H, by contraposition.
  - (iii-E) S is not an instance of (1.1) on a single test.
  - (ii′) H depends on P_Σ restricted to |u| ≥ 2T_c, and it is not a function of the data listed in Thm A(b).

**Lem A.0. PROVED.** P_Σ = (Z_Σ)^ as distributions modulo the fixed Γ_ℝ part, by (1.1) over a dense family of tests. So every H is a property of Z_Σ, and also a property of P_Σ. A "data type" is a coarser invariant π(Σ). The ones that matter here are:
- π_win(Σ) = P_Σ|_{(−2T_c,2T_c)}. By (1.1) this is the same as Z_Σ modulo the annihilator of PW_{T_c}·PW_{T_c}. Equivalently it is W^Σ_{T_c}, and it determines 𝔠_Σ.
- π_on(Σ) = Z^on_Σ.
- π_at(Σ) = the atomic part of P_Σ − (polar + arch).
- π_off(Σ) = Z^off_Σ.

H "uses only π" means H(Σ) = H(Σ′) whenever π(Σ) = π(Σ′). ∎

**Lem A.1 (f_t-coincidence). PROVED.** Assume ¬RH. Then T_c := T_c(ζ) < ∞ (record, Weil's criterion), and T_c > 0.8047. In R163_901 Thm F, choose N₀ with ½log λ₁ > T_c.
- By Thm F.3, W^{f_t}_T = W^ζ_T for all T ≤ ½log λ₁. So f_t and ζ have the same contact T_c, the same kernel E_c, the same witnesses, the same nodes X, and π_win(f_t) = π_win(ζ). This holds for every t.
- W^{f_t}_T is not ≥ 0 for T slightly above T_c. By (1.1) for f_t (Thm F.3, Weil–Barner), f_t then has a non-real t_ρ.
- So f_t is a genuine system with off-line zeros, and it has *literally the same contact datum as ζ*. ∎

## 2. Theorem A

**Theorem A.** Let 𝔐 = (H, S) satisfy (iii). Assume ¬RH; under RH there is no contact and the statement is vacuous.

(a) H does not use only (π_win, 𝔠). **PROVED.** By Lem A.1, π_win(f_t) = π_win(ζ) and 𝔠_{f_t} = 𝔠_ζ. If H used only these, then ζ ∈ H would give f_t ∈ H, against (iii). ∎

(b) H does not use only (π_on, π_at, polar, arch). **PROVED.**
- M_m = ξ·∏R_j. Its zero set is Z_ζ + Σ_j q_j, where the q_j are quartets disjoint from Z_ζ. So π_on(M_m) = π_on(ζ). The quartets are non-real, and that is all the definition requires.
- P_{M_m} = P_ζ + β̂_q, where β_q(u) = Σ_j 4cos(γ_j u)cosh(δ_j u) on all of ℝ (R163_801 Thm 5(a); the global form is the Fourier transform of the added atoms). β_q is real-analytic, hence non-atomic, so π_at(M_m) = π_at(ζ). Polar and archimedean parts are unchanged.
- If H used only these data, M_m ∈ H, against (iii). ∎

  *Remark (the (X, Γ) case of the brief).* Let S be any functional of (X, Γ) with Γ = Z^on, global in X; for example the phase identity of R165_201 Thm 2, Θ_X = Θ_Γ + π ω(E⁺) − π ω(E⁻) + Ψ_out. Suppose its proof H uses only "X is the node set of a contact witness of a system whose on-line set is Γ". M_m satisfies that hypothesis with its own X_{M}. So S(X_M, Γ) holds and (iii) fails. This is case (b). The contact datum is a function of Σ, so allowing S to depend on X adds nothing to H: requirement (i) constrains S, never H.

(c) The zero-side escape. Suppose H uses only π_off on the fibre 𝔉_M := {Z_ζ + Σq_j}, the zero sets of all M_m with all admissible quartet families q (finite, disjoint from Z_ζ, anywhere in the strip off ℝ). Then (iii) for all M_m says exactly this: H(Z_ζ^off ⊔ q) is false for every q ≠ ∅, and H(Z_ζ^off) is true. **PROVED** (restatement). In particular:
- if H has the confinement form H = {Σ : Z^off_Σ ⊆ A} with A explicit, then A ∩ U = Z_ζ^off ∩ U, where U is the region where quartets may be added (the open strip minus ℝ). Otherwise a quartet q ⊂ A ∖ Z_ζ^off would give M_m ∈ H. **PROVED.**
- So "ζ ∈ H" is the theorem "the off-line zero set of ζ in U is exactly the explicit set A ∩ U". Such a proof decides RH: RH ⟺ A ∩ U = ∅. **PROVED** in this sense.
- If Z_ζ^off = ∅, the statement is RH verbatim.
- *What is not formal:* the claim that any non-confinement zero-side H separating all M_m is also "RH-strength". H can be an arbitrary set of point configurations, and "RH-strength" is a statement about proofs, not about sets. **ARGUED.** No formalisation of "a proof of ζ ∈ H uses no knowledge of Z_ζ^off" is attempted.

**Conclusion (ii′). PROVED, modulo the ARGUED clause of (c).** By (a), H must see P beyond the window or, equivalently by Lem A.0, Z beyond window tests. By (b), H must see β_q or the added quartets.
- The data that see β_q are the non-atomic part of P. That part is window-visible: β_q is nonzero on every subinterval of (−2T_c, 2T_c). But it is invisible to f_t, since π_at and π_win of f_t and ζ coincide on the window.
- The data that see the added quartets are π_off. By (c), using them means knowing Z_ζ^off.
- So a mechanism that does not know Z_ζ^off must use **both**:
  - window atomicity of P (to fail M_m). This is shared with f_t.
  - prime data beyond the window (to fail f_t). On the atomic side this means support on log ℕ, sign, or multiplicativity, because f_t's atoms beyond λ₁ are signed and lie off log ℕ (R164_401 Cor R.3).
- That is (ii′): coupling to the atomic prime side beyond the window. ∎

**Cor A.1. PROVED.** No mechanism has (i) and (iii) without (ii′). This explains R166_400's finding that "{i,iii} is empty in the corpus". It is a consequence of (iii) alone. The Levinson–Conrey exception noted there is killed by Davenport–Heilbronn and Epstein. That is the same pattern: a non-Euler system that shares the window-type inputs, i.e. case (a) with another falsifier.

**Lem A.2 (projective invariance). PROVED.** F is determined only up to c ∈ ℝ^×, so S(Σ, cF) = S(Σ, F). Let S = "Φ(F) ≥ 0" (or "> 0") with Φ homogeneous polynomial of degree d. Taking c = −1 gives (−1)^dΦ(F) ≥ 0, so either d is even or the statement forces Φ(F) = 0. If d = 0, Φ is constant in F. Non-polynomial invariants are also allowed. Functions of X alone (Θ_X, harmonic measure ω) have homogeneity 0 and still depend on F. ∎

**Cor A.2 (two requirements). PROVED (reduction).** (i) ∧ (ii) ∧ (iii) ⟺ (i) ∧ (iii) by Thm A, and (iii) splits into (iii-f) ∧ (iii-M) ∧ (iii-E). Regrouped:
- **(G)** S is a non-constant projective invariant of [F] and global in X. Its polynomial representatives have even degree ≥ 2 (Lem A.2). This **corrects** the phrase "at least quadratic": degree-0 functions of X, such as the phase, are admissible.
- **(N)** H depends on Λ beyond the window and on the window's non-atomic part (Thm A). It is not an identity. A single test of (1.1) holds for every system, so it is never a separator. It is also not merely the positive cone of Λ.

**Rem A.3 (what is not proved: "non-linear").**
- (iii) does not force non-linearity in Λ. Take the cone condition H₊ = "P − polar − arch = −(nonnegative atomic measure on ±log ℕ) beyond the window". It is linear in P, and it fails for f_t (signed atoms off log ℕ) and for M_m (β_q changes sign). So it passes (iii).
- It is killed by a different wall. With the FE, Γ_ℝ, the polar data and the window, H₊ ∩ {systems} = {ζ} (R164_401 Thm R). That is W-identification: "S ⟹ no off-line zeros" for the only member is RH itself.
- If H₊ is coupled to F through tests G²K, each instance is a drop-term inequality (R164_601 Thm 3.1). An arbitrary conjunction of drop-term inequalities is still satisfied by ζ's true zero set, whatever it is (Thm 3.1 applied test by test). **PROVED.**
- So the honest form of (N) is: **not linear-and-single, not cone-and-identifying.** "Non-linear in Λ" (R166_405's union column) is the natural candidate. It is **ARGUED**, not a theorem.

## 3. Part B: the Thm R mechanism on η := Z − Q_X

Notation is that of R163_401 §2.4:
- G is real, of type T_c, real-rooted, with simple nodes X. The convex support of F is [−T_c, T_c] (2.4(i), full support), so the indicator of G is T_c|sin θ|.
- w_x = W(H_x)/|F̂′(x)|² ≥ 0, and Q_X = Σ_x w_x δ_x.
- E_c = ker W_{T_c}.
- Write η := Z − Q_X, paired with entire test functions: ⟨η, Ψ⟩ = Σ_ρ m_ρΨ(t_ρ) − Σ_x w_xΨ(x).

**B(1) (gap and sign). PROVED.**
- For G₁, H₁ ∈ N̄^𝒟, Q0 (R163_502) gives Σ_ρ(Ĝ₁Ĥ₁^#)(t_ρ) = Σ_x w_x Ĝ₁(x)conj Ĥ₁(x), i.e. ⟨η, Ĝ₁Ĥ₁^#⟩ = 0. This is the analogue of ⟨η, φ⟩ = 0 for supp φ ⊂ (−X, X) in Lemma 2.
- Sign: η = +m_γ at on-line atoms (real) and −w_x ≤ 0 at the nodes. If a node coincides with an on-line zero, the net weight m − w_x has either sign; those points belong to the controlled set X.
- At each off-line quartet η has unit atoms at complex points. For a real Ψ (Ψ^# = Ψ) that is even, the quartet contributes 4Re Ψ(t_q), which has no sign for Ψ ≥ 0 on ℝ.
- The controlled-negative set is X ⊂ ℝ. The uncontrolled set is {t_q} ⊂ ℂ∖ℝ. ∎

**B(2) (no room at type 2T_c). PROVED.**
- Let Ψ lie in the gap (a finite sum of products from N̄^𝒟), with Ψ ≥ 0 on ℝ and Ψ = 0 on X.
- By Akhiezer–Krein (CITED as in Thm SA), Ψ = SS^# with S ∈ 𝒟_{T_c}. The log-weight integrability is inherited from the absolutely convergent sums, as in Thm SA step 1.
- Then W(S) = ⟨Z, SS^#⟩ by (1.1), = ⟨Q_X, Ψ⟩ by the gap, = Σ w_x Ψ(x) = 0. Since W_{T_c} ≥ 0, S ∈ E_c. So Ψ = ĤĤ^# with H ∈ E_c.
- No membership S ∈ N̄^𝒟 is needed; this improves on Rem SA.3 of R164_501, which needed (Q).
- The identity ⟨η, Ψ⟩ = 0 then reads W(H) = 0. For H = F it is Σ_ρ G(t_ρ)² = 0, which is Rem 4.8a. Code E1: only (1.1), W ≥ 0 and Q0 are used, so it holds for M_m, f_t and f_χ.
- Note: the quartets cannot be annihilated at this type, because G(t_q) ≠ 0 (G is real-rooted). ∎

**B(3) (room Δ > 0: Akhiezer factorisation). PROVED.** Let Δ > 0. Let Ψ be entire of exponential type ≤ 2T_c+2Δ, Ψ ≥ 0 on ℝ, Ψ ∈ L¹(ℝ), with ∫log(2+|τ|)Ψ < ∞, and Ψ = 0 on X.

*Claim.* Ψ = G²·KK^#, where K is entire of Cartwright class with exponential type ≤ Δ and GK ∈ PW_{T_c+Δ}. Conversely every such Ψ is ≥ 0 on ℝ and vanishes on X (to order 2).

*Proof.*
1. Akhiezer–Krein (Levin, Lecture 16, Thm 3, CITED) gives Ψ = SS^# with S entire, of type ≤ T_c+Δ, and all zeros in the closed upper half-plane. Since |S|² = Ψ ∈ L¹, S ∈ PW_{T_c+Δ}.
2. On ℝ, |S(x)|² = Ψ(x) = 0 for x ∈ X, so S vanishes on X. The nodes are simple zeros of G, so K := S/G is entire.
3. S and G are Cartwright. By Krein's theorem (Levin, Lecture 16; CITED), K is Cartwright with indicator h_K = h_S − h_G. So h_K(±π/2) ≤ (T_c+Δ) − T_c = Δ. This uses full support: h_G(±π/2) = T_c exactly.
4. G is real, so SS^# = G²KK^#.
5. The converse is immediate. ∎

When K is real entire, KK^# = K², and this is the G²K² of the brief.

*Pairing.* Ψ vanishes on X, so ⟨η, Ψ⟩ = ⟨Z, Ψ⟩. By (1.1),
  ⟨Z, Ψ⟩ = 𝔄(Ψ) − Σ_{log n < 2T_c+2Δ} Λ(n) n^{−1/2}(Ψ̌(log n) + Ψ̌(−log n)),
because supp Ψ̌ ⊂ [−2T_c−2Δ, 2T_c+2Δ]. The atoms with 2T_c ≤ log n < 2T_c+2Δ enter. This is (ii) at finite depth. In the notation of R164_601 Prop 1.1, Ψ̌ = g * (KK^#)ˇ: these are exactly the G²K tests of family P (P1–P4). They are not in the gap, and ⟨η, Ψ⟩ is a prime-side value, not 0. ∎

**B(4) (annihilating the uncontrolled set). PROVED.** Let K be as in B(3), K ≠ 0, with KK^# vanishing on every off-line quartet (for an even K, K(t_q) = 0 suffices, since K^#(t̄_q) is the conjugate of K(t_q)). Then:
- Σ_ρ Ψ(t_ρ) = Σ_on m_γ G(γ)²|K(γ)|² ≥ 0.
- The identity reads
  𝔄(Ψ) − Π_{<2T_c+2Δ}(Ψ) = Σ_on m_γ G(γ)²|K(γ)|²  (> 0).
- *Strictness:* GK ≠ 0 has finite type. By R164_501 Prop 3 (Selberg + Jensen; PROVED-CITED) it cannot vanish at all on-line ordinates.
- In words: the window-extended Weil form is positive at GK, for every GK that vanishes on the off-line zeros. This holds for every system Σ satisfying (1.1) (ζ under any hypothesis, M_m, f_t), each with its own t_q. It is an identity whose right side has a sign by construction, so **no contradiction can arise from it**. This is R164_601 Thm 3.1 with S = 0: nothing is left to bound, because the other quartets are annihilated.
- If one quartet q₀ is kept (K vanishing at all the others), the identity becomes Σ_on + 4Re[G²KK^#](t_{q₀}) = 𝔄 − Π. Excluding q₀ then needs an upper bound on 𝔄 − Π (window data at depth 2T_c+2Δ) beating −4Re[…](t_{q₀}). That inequality is implied by the identity for ζ's true zeros, so it is the drop-term principle again (R164_601 Thm 3.2 with S = 0).
- *Effectivity caveats.* (1) Such K must know {t_q}, which is unknown for ζ. (2) It exists only if the off-line set has zero-density compatible with type Δ (a Cartwright function of type Δ has ≤ (2Δ/π + o(1))R zeros of modulus ≤ R). So B(4) is a statement about every configuration, never a construction for ζ. ∎

**B(5) (the exact obstruction). PROVED.** Compare the two settings.

*Lemma 2 (R164_401).* Lemma 2 rests on three facts holding at once:
- (α) a hole: ⟨η, Ψ⟩ = 0 for a whole family of Ψ;
- (β) Ψ annihilates the uncontrolled negative part: Ψ = |sinc·χ̂|² kills η₋ on ℤ;
- (γ) Ψ ≥ 0 on the rest of supp η, so ∫Ψ dη₊ = 0 forces supp η₊ ⊂ Z(Ψ). The excess type π(X−1) moves Z(χ̂) freely, which forces supp η₊ = ∅.

All three hold because **the uncontrolled set ℤ is real**: positivity on ℝ is exactly positivity on supp η.

*On η = Z − Q_X.*
- (α) holds only at type ≤ 2T_c (B(1)).
- There is no excess type: the node density is critical, so B(2) leaves only E_c.
- The uncontrolled set {t_q} is **non-real**. (β) for it requires vanishing at t_q, which a type-2T_c member of the gap cannot do (G(t_q) ≠ 0). It therefore needs excess type Δ > 0 (K(t_q) = 0).
- Excess type destroys (α): ⟨η, Ψ⟩ = 𝔄 − Π ≠ 0, and by B(4) it is strictly positive whenever (β) holds.
- When (β) and a value coexist, (γ) yields only "a positive quantity equals a positive quantity". That is Weil positivity on a subspace, valid for every zero set.
- Without (β), (γ) fails at the t_q: Ψ ≥ 0 on ℝ gives no sign for Re Ψ(t_q).

> **Obstruction (R166_501).** In the transport of Thm R to η = Z − Q_X, the hole (α) and the annihilation (β) of the uncontrolled set are incompatible. The hole lives at type 2T_c with zero excess. Annihilating the non-real set {t_q} needs excess type, and excess type converts the hole into a prime-side value at depth 2T_c+2Δ. With both, the output is an identity whose two sides have the same sign for every system. The root cause is that η's uncontrolled support is off ℝ, where positivity of the test on ℝ carries no information. In Thm R it was on ℤ ⊂ ℝ.

The Thm R transport with room is therefore family P (B(3)), and it dies by the drop-term principle (B(4)). Without room it is Rem 4.8a (B(2)).

## 4. Falsifier checks

| statement | uses | f_t | M_m | f_χ / DH | consistent? |
|---|---|---|---|---|---|
| Lem A.1 | Thm F only | is the falsifier | — | — | yes. It needs ¬RH and N₀ > e^{2T_c}, and Thm F allows any N₀ |
| Thm A(a) | Lem A.1 | separates nothing window-local | — | — | yes |
| Thm A(b) | Thm 5 of R163_801 | — | shares π_on, π_at | — | yes. Note that β_q acts on all of ℝ; the "windowed M_m" of R164_501 is a different object with the same W_{T_c} |
| Thm A(c) | definitions | — | fibre 𝔉_M | — | yes; it is a restatement |
| Cor A.1 vs corpus | R166_400 | — | — | Levinson–Conrey killed by DH: case (a) | yes. P has (i,ii), Q has (ii,iii), and nothing has (i,iii) without (ii) |
| Thm R (Q2) vs Thm A | — | fails H₊ | fails H₊ | fails | yes. It has (ii)+(iii) and lacks (i) (Rem A.3) |
| B(1)–B(3) | (1.1), W ≥ 0, Q0, Akhiezer | hold | hold | hold | yes. E1 by design |
| B(4) | (1.1), Prop 3 | holds, with its own t_q | holds | holds | yes. "No contradiction" is the claim |

Each statement fails for exactly the systems it predicts it fails for, and holds for the others.

## 5. Ledger

| Id | content | label |
|---|---|---|
| R166_501.D1 | formal notion of a mechanism (H, S); (iii) ⟺ falsifiers ∉ H | definition |
| R166_501.A0 | Z ↔ P data map; data types are partial invariants | PROVED |
| R166_501.A1 | under ¬RH, f_t with N₀ > e^{2T_c} has ζ's contact datum exactly and off-line zeros | PROVED |
| R166_501.A | (iii) ⟹ (ii′); (i) is not used | PROVED, (c) "RH-strength" for non-confinement H is ARGUED |
| R166_501.A.c | zero-side confinement separating all M_m ⟺ exact location of Z_ζ^off; decides RH | PROVED |
| R166_501.CA1 | "{i,iii} = ∅" is a theorem | PROVED |
| R166_501.A2 | projective invariance: even degree; degree-0 functions of X are allowed | PROVED |
| R166_501.CA2 | reduction to (G)+(N); "≥ quadratic" corrected to "non-constant projective invariant" | PROVED |
| R166_501.RA3 | "non-linear in Λ" not forced by (iii). The linear cone H₊ passes (iii) and dies by W-identification (Thm R). Conjunctions of drop-term inequalities give nothing | PROVED (cone/identification, drop-term); "non-linear is the way out" ARGUED |
| R166_501.B1 | gap ⟨η, ĜĤ^#⟩ = 0 on N̄^𝒟; sign of η | PROVED |
| R166_501.B2 | no room at type 2T_c, without (Q) (improves R164_501 Rem SA.3) | PROVED |
| R166_501.B3 | Ψ ≥ 0 of type 2T_c+2Δ vanishing on X ⟺ G²KK^#, K Cartwright of type ≤ Δ; pairing = EF with Λ to e^{2T_c+2Δ} | PROVED (CITED: Akhiezer–Krein, Krein) |
| R166_501.B4 | annihilating the t_q gives Weil positivity on a subspace, true for every system | PROVED |
| R166_501.B5 | exact obstruction: hole and annihilation of a non-real set are incompatible | PROVED |
| O166.501.1 | does every separating H not of confinement type, whose proof does not use Z_ζ^off, have to be non-linear in Λ beyond the window? (formalise "proof uses no knowledge of Z^off") | OPEN (meta) |
| (★_cell), RH, row D | | **OPEN** |

## 6. Summary (15 lines)

1. A mechanism is formalised as (H, S): H is a property of systems, ζ ∈ H is proved without RH, and H ⟹ S. Requirement (iii) is "f_t, M_m ∉ H".
2. Lem A.1 (PROVED): under ¬RH, f_t with N₀ > e^{2T_c} has ζ's exact contact datum (T_c, F, X), the same window, and off-line zeros.
3. Thm A (PROVED): (iii) forces H to use prime data beyond the window (because of f_t) and the non-atomic or quartet part (because of M_m). This is (ii′).
4. Requirement (i) is never used: (iii) ⟹ (ii) by itself. The corpus fact "{i,iii} = ∅" is now a theorem.
5. Functionals of (X, Γ_on), including the phase / harmonic measure, are satisfied by M_m through its own witness.
6. Zero-side separation of all M_m is exact location of ζ's off-line set: a proof of it decides RH (PROVED for confinement H; ARGUED in general).
7. Corollary: the requirements reduce to (G) and (N).
   - (G) is a non-constant projective invariant of F, global in X; polynomial forms have even degree ≥ 2, and degree-0 functions of X are allowed. This corrects "≥ quadratic".
   - (N) is Λ beyond the window, not an identity, not a single test, not the identifying cone.
8. Honest gap: "non-linear in Λ" is NOT forced. The linear cone "Λ ≥ 0 beyond the window" passes (iii) and dies by W-identification (Thm R) instead.
9. B(1) (PROVED via Q0): η = Z − Q_X annihilates ĜĤ^# on N̄^𝒟. η is ≥ 0 on on-line atoms, ≤ 0 on X, and complex at the t_q.
10. B(2) (PROVED, without (Q)): the nonnegative gap tests vanishing on X are ĤĤ^#, H ∈ E_c; the output is Rem 4.8a (E1).
11. B(3) (PROVED): with room Δ, these tests are exactly G²KK^#, K Cartwright of type ≤ Δ. Pairing them with Z gives the explicit formula with Λ up to e^{2T_c+2Δ}: this is family P.
12. B(4) (PROVED): vanishing at the off-line zeros gives 𝔄 − Π = Σ_on G²|K|² > 0, Weil positivity on a subspace, true for every system. It is drop-term with S = 0.
13. B(5), the exact obstruction: the hole needs type 2T_c with zero excess, and killing the non-real set {t_q} needs excess type, which destroys the hole.
14. In Thm R the uncontrolled set ℤ was real, so positivity on ℝ was positivity on supp η. Here supp η₍uncontrolled₎ ⊂ ℂ∖ℝ.
15. No label of record changes. (★_cell), RH and row D remain OPEN. New open meta-question: O166.501.1.
