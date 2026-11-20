# Round 16, memo C: reflection positivity, correlation inequalities and Gaussian domination as source of the sign

Summary. Three sources of sign from statistical mechanics that are not «sum of
squares with positive weights» were put through the gate: (a) Osterwalder–Schrader (OS) reflection positivity with
transfer-matrix reconstruction; (b) GKS, Griffiths, Ginibre, FKG, four functions and Lee–Yang
on the divisor lattice; (c) Gaussian domination and infrared bounds. All three are **repetition**,
read in primary sources. The even/odd decomposition `a_T = D ± R` proposed by the assignment is, literally,
Lemma 1 of `phase-193-creation-campaign/CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` §3. The non-negativity
of `R` (the Hankel half) is false for every comb with an atom (Theorem 2, same file, PROVED). By the
filter rule, the memo does not build. Nor did I find a neighbouring idea I can defend (§4).

Primary reading: `CA_A_007_SEED_TRIAGE_HOMOTOPY_TRIPLES_RP.md` §§3–5 and `CA_A_007_REVIEW.md`
(header and row of Lemma 1); `phase-200-sign-object/K1_OSG_001.md` §1b and the proposed index entry;
`phase-6-osterwalder-schrader-reflection/README.md` and `M-OS-2-S2-local-REFUTATION.md` §2;
`CA_J_000_SEEDS.md`, rows J6 and J7; index `README.md`, front J of phase 193;
`RULES_AVOID.md` M3, M5, W4 and Y; `ROUND_009_G3.md`, row 17; grid, entry 52;
`ANNEX_PHASE_193_LABELS.md`, J6 and J7. Grep in `03-research` and `05-meta-and-planning` for «reflection positiv»,
«Osterwalder», «chessboard», «GKS», «FKG», «Lee–Yang», «four functions», «infrared», «Gaussian domination»,
«dominación gaussiana» and «Fröhlich». The relevant hits are the above; the others use those words
in passing. I did not reread `CA_J_001` or `CA_J_002` in full: their content is taken from the index and the grid
(indirect reading).

## 0. Four-point filter

1. **Closest antecedent.**
   - (a) `CA_A_007` §3. Lemma 1: for `F = f + Θf` with `f` on `(0,T)`, `𝔞(F) = 2𝔞(f) + 2H_K(f)`, with
     `H_K(f) = ∬ f(t)f(s)K(t+s)` and `K` the window kernel (archimedean part minus the comb
     `Σ (v_n/2)δ_{±log n}`): «RP is the Hankel half of the Toeplitz form». Theorem 2: `H_K` is not `≥ 0` on
     `(0,T)` if `T > ½ log n_0` for some atom `n_0`. Reflection at the edge `x = T` is `K1_OSG_001`
     (NO-GO; it is Theorem 2 conjugated by a translation). The multiplicative reflection `n ↦ 1/n` is the
     symmetrization by the functional equation (`CA_A_007` §3, last paragraph; L2_026, NG-D4). Positivity
     per place is phase 6, S2.1 (`G_p` indefinite).
   - (b) Front J of phase 193 (`CA_J_002`, Theorem 1.3). The additive cycle `m → m+1 → … → 2m`, closed
     by the multiplicative edge `(m, 2m)`, is frustrated, so no `±1` gauge makes `𝔸_M`
     ferromagnetic. That leaves GKS, Ginibre, GHS, Lebowitz and FK without entry. In FKG, the equality class on the
     divisor lattice are the Euler-product vectors (`CA_E_001`), so FKG is blind. Lee–Yang
     and strong Rayleigh are in M3/M5 and in `INV_M_001`.
   - (c) `CA_J_000`, row J7: «DISCARD: requires RP ⇒ dies with J6».
2. **New object proposed by the assignment.** There are three claims. First, the
   «transfer» spectrum of the archimedean part. Second, that the comb enters as an interaction of the form
   `−Σ(θA_i)A_i` preserving RP. Third, an infrared bound «interaction ≤ free part», uniform in `T`.
3. **Does it avoid the difficulty of the antecedent?** No, in none of the three cases.
   - The first claim is correct but not new (§1). Moreover it is blind: it uses only the archimedean part,
     which is the same in the three controls.
   - The second collides with Theorem 2 (§2).
   - The third presupposes RP, or else is the statement itself (§3).
4. **Global link.** The only link that can be written is `𝔞_T(f) ≥ |H_K(f)|` on the two parity
   sectors. It is the positivity of `a_T` restricted to evens and odds, i.e. the form itself (J3). There is
   no new inequality.

By the filter rule, the construction stops here.

## 1. The archimedean kernel is completely monotone (correct, known, blind)

**Observation 1 (PROVED; elementary).** For `u > 0`, `1/(2 sinh(u/2)) = Σ_{k≥0} e^{−(k+½)u}` and
`1/(2 cosh(u/2)) = Σ_{k≥0} (−1)^k e^{−(k+½)u}`. Adding,
`K(u) = 2 Σ_{j≥0} e^{−(2j+½)u}`: it is the Laplace transform of the positive measure `2Σ_j δ_{2j+½}`. Hence
`H_{K_arch}(f) = 2 Σ_j |∫ f(t) e^{−(2j+½)t} dt|² ≥ 0`. This is RP of the archimedean part,
with «energies» `2j+½`.

It is not new. `K1_OSG_001` builds exactly the «CM Hankel square of the poles of Γ_ℝ». Moreover, by
Lemma K (`RULES_AVOID` W4), positivity coming from a positive measure holds for every weight: it is blind at
`c = 2`, on deleting a prime power and for Beurling. A proof of RP using only this does not see the comb.

## 2. The comb as an RP-preserving interaction: falsified by Theorem 2

In the even sector the form is `2𝔞_T(f) + 2H_K(f)` and in the odd one `2𝔞_T(f) − 2H_K(f)` (Lemma 1 of `CA_A_007`
applied to `f ± Θf`; PROVED there). With `D = 2𝔞_T(f)` and `R = 2H_K(f)`, the OS scheme required `R ≥ 0`. The
contribution of the comb to `R` is `−Σ_n (v_n/2) ∫ f(t) f(log n − t) dt`: a Hankel form with kernel
`−Σ (v_n/2) δ(t + s − log n)`. By the Widom–Bernstein criterion, a Hankel kernel `h(t+s)` is `≥ 0` on
a half-line if and only if `h` is the Laplace transform of a positive measure (CITED). A comb of
deltas with negative sign is not. Theorem 2 of `CA_A_007` gives the direct proof, also in a finite
window: `f_ε` concentrated at `½ log n_0` gives `H_K(f_ε) → −v_{n_0}/2`, because the continuous part contributes
`O(ε)`.

On the form `−Σ(θA_i)A_i`: in OS, an interaction preserves RP when it enters the Boltzmann weight as
`exp(+Σ(θA_i)A_i)`. At the quadratic level that means adding to `R` a term of the form `+Σ|⟨A_i, f⟩|²`. In `a_T`,
the comb enters with the opposite sign (`−v_n c_F`), precisely the one that destroys RP. No choice of
reflection fixes it:
- translation of the centre is the case of `K1_OSG_001`;
- the inversion `n ↦ 1/n` is the functional equation (NG-D4);
- the per-prime reflections `θ_p` are the chessboard of `CA_J_001`, which forces constant `𝖡` with two primes.

**Controls.** Theorem 2 holds for every comb with an atom, including `2Λ`, the comb with a deletion and
Beurling. RP is false in all four cases. It does not fail at «the step that breaks at `c = 2`»; it fails
everywhere. Hence it is not a sign mechanism (Lemma T).

**Dominance in the two sectors.** The requirement `𝔞_T(f) ≥ |H_K(f)|` (Toeplitz dominates Hankel) is an
OS Cauchy–Schwarz-type bound. Without RP there is no Cauchy–Schwarz for `⟨θ·,·⟩`. As a statement, it is
`a_T ≥ 0` in each parity sector, where `P_T` imposes a single condition per sector (`∫F cosh(t/2) = 0` in the
even one, `∫F sinh(t/2) = 0` in the odd one). It is the already known parity reduction (thm:parityschur, `CA_A_007`
§2), hence J3. The Toeplitz−Hankel matrix of phase 205 is that same form in coordinates, not a source of
sign. That file was not reread: indirect reading, from the project memory.

## 3. Gaussian domination and infrared bounds

Fröhlich–Simon–Spencer Gaussian domination (CITED) deduces `Z(h) ≤ Z(0)` from RP via the chessboard,
and from there an infrared bound. Without RP of the full object there is no entry: this is how J7 was discarded. The
target format, «prime part ≤ Arch» uniform in `T`, is `a_T ≥ 0` for all `T`. Written without RP, it is the
statement itself (J3), not a tool.

## 4. Neighbouring idea

I looked for a variant that changes the class of methods and not just the reflection. I did not find one. The
possibilities reviewed were:
- RP with a Hankel kernel `h` depending on `Λ` nonlinearly. To have RP, `h` would have to be positive
  Laplace, and then it would be blind by Lemma K.
- «Conditional» positivity: RP only on the subspace orthogonal to the modes `δ_{log n}`. It is the boundary or
  the carrier with additional conditions, the case of `K1_OSG_001` (i), where the gap only protects
  products.
- A reflection nonlinear in `F`. I know of no OS reconstruction theory for it, and I do not invent one without
  mechanism.

Instead of proposing something without mechanism, I record it as an absence. Still unexcluded, according to `RULES_AVOID`
X and Y: Hadamard positivity coupling primes through `m ≈ kn` and the potential `V(x,F)` convex only
for the true weight. This memo does not attack them.

## 5. Status

- (a) OS/RP with transfer reconstruction: **repetition** (`CA_A_007` §3, `K1_OSG_001`, phase 6, `CA_J_001`).
  Non-negativity of the Hankel half with the comb is **NO-GO** (PROVED there, for every comb with an atom).
- (b) GKS, Griffiths, Ginibre, FKG, four functions and Lee–Yang: **repetition** (front J of phase 193,
  `CA_J_002`, `CA_E_001`, M3).
- (c) Gaussian domination and infrared bounds: **repetition** (J7). Without RP, the target format is J3.
- Observation 1 (completely monotone kernel `K`, exponents `2j+½`): PROVED, but already in `K1_OSG_001`
  and blind.
- Nothing new to record in the index as a closed route.
