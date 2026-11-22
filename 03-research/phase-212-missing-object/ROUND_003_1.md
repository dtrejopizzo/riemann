# Round 3, option 1 — Families of functionals that see the window and are not the theta modal one (selection memo)

Goal (★): λ_A(T) ≥ 0 for every T, with the definitions of `../phase-211-sign-sandbox/STATEMENT_001.md`.
Question: is there a per-window family, not yet explored, in which the incidence Σ_{d|k}Λ(d) = log k acts on
functionals that do not commute with translations, so that the leakage subtracted by truncation (`REVIEW_002_BC.md`,
Lemma B-1) is compensated exactly by a boundary term with sign, specific to Λ? In particular, does the
Nyquist mesh give a square in the sampled values F̂(ω_k)?
Notation: Q = 1_{I_T}, R = 1 − Q, U_a the translation by a on ℝ, ω_k = πk/(2T) (P46 thm:nyq; the task writes
πj/T, which is the even sublattice), s_k = s_T(ω_k) with the truncated symbol of thm:nyq, N = e^{2T}.
Abbreviations: «GRAM», «GLOBAL» as in `ROUND_002_B.md`. Labels: PROVED / CITED / CONDITIONAL / ARGUED /
OPEN / NO-GO / NUMERICAL.

## Cross-check

### What was searched

grep (case-insensitive) in `03-research/` (all phases), `04-papers/47…/main.tex`, the grid, the
crossword and the `ANNEX_*.md` of this phase, for: truncated translation, traslaciones truncadas, compressed
dilation, Wiener–Hopf, Toeplitz–Hankel, Nyquist, malla de Nyquist, omega_k, Shannon, prolate, Slepian, boundary
jet, collar, leakage, fuga, time-limited, band-limited, Paley–Wiener, de Branges, reproducing kernel; and, within
the files with «Nyquist», for divisor / incidence / mcd / gcd / Λ∗1. The largest concentrations: Nyquist
in 60, 155, 159, 186, 193, 211; collar in 101, 121, 124, 161, 162, 163, 170; prolate/leakage in 72, 106, 114,
116, 186, 199, 200, 211; de Branges/Paley–Wiener in 159, 160, 60, 64. Opened in primary: P46 thm:nyq,
lem:nyq-sampling, prop:nyq-alias, prop:nyq-LK, prop:nearfree, rem:boxes, thm:coer-schur, eq:collar;
R186_052 §§0–1, R186_053 §§0–1, R186_117/118 (verdicts); 204 `P1_BBSTAR_001.md` §3; 211 `ROUND_005_C.md`
§§1, 5.2–5.3 and its entry in `ANNEX_211_FILES_6.md` (with those of ROUND_001_C, ROUND_002_A, ROUND_005_A,
ROUND_006_B); 191 `SPEC_B_SELECTED_FREQUENCY.md` §1. Not opened in primary (only via annex or via the
grep listing): phases 60, 72, 114, 116 (except what `REVIEW_002_BC.md` cites), 121, 124, 155, 159, 161,
170 (except via `RULES_AVOID.md` §I), 199, 200. A search without hits does not prove novelty.

### Inventory of per-window families already written

| # | Family | Where | What it gave | Why it stopped |
|---|---|---|---|---|
| 1 | Truncated translations term by term B_nF = Qτ_{log n}F − F | 204 `P1_BBSTAR_001` §3, Prop. 3.1 | 𝒲 = Σ(v_n/2)‖B_nF‖² + [arch − ⟨F,wF⟩], w ≥ ½Σv_n | remainder costs the mass of the comb (PROVED mod. prop:primeblind); linear in Λ |
| 2 | Truncated translations grouped in a fixed basis | same memo, §3 («grouped Cholesky of A_MU (b) / C8: indexed, not retried»); `REVIEW_002_BC` Lemma B-1 | Q_B = class (i) − leakage | remainder not examined; ungrouped residue K3: «empty class of candidates», OPEN |
| 3 | Words of truncated translations, Krylov of the comb | 211 ROUND_005_A Lemma 3.2, Prop. 3.3 (Π² = Qσ_v²Q − 𝔏*𝔏); ROUND_006_B Prop. 4.1–4.3 (halo/leakage, constant ½) | [Λ∗Λ indefinite] + [mean value ≥ 0] − [leakage] | class NO-GO for bounded j and v-homogeneous generators (cΛ acts only through the bundle) |
| 4 | Compressed J_T, B_T^{−1/2}J_TB_T^{−1/2}, functionals ⟨F,c⟩, ⟨F,s⟩ | R170_301 §§2–5 (via `REVIEW_002_BC` B.1.5) | E_T = Γ_T + 2A_T I − J_T + 2\|c⟩⟨c\| | generic; falsifier a₂ = 100 |
| 5 | Nyquist sampling: diagonal identity in the samples | P46 thm:nyq, prop:nyq-alias, prop:nyq-LK | a_T = (1/4T)Σ_k s_k\|F̂(ω_k)\|² | reformulation (N); 191 SPEC_B §1 classifies it REF-D |
| 6 | Nyquist algebra: two spin structures, cones, Herglotz of the sampled comb | R186_052 Thm. 1.2, 2.1–2.4, 3.1–3.5, §4; R186_053 Thm. 2.1 | a_T = ½[s(D_per) + s(D_anti)]; circulant cone fails in every window | «contact with the sign: none»; Bochner–Herglotz on ℤ is positivity on the circle, not on the half-circle; M₁ |
| 7 | Negative Nyquist block and Schur complement | 211 ROUND_001_C Thm. 1, Prop. 4; ROUND_002_A Thm. F, Prop. M, Cor. M1–M2 | (L2′); deep sample ⟹ near-coincidences n′^{q_n} ≈ n^{q_{n′}} | no criterion on the samples alone decides (Prop. 4); Schur only with floor NO-GO |
| 8 | Responses of the comb on the mesh with Λ∗1 = log | 211 ROUND_005_C Prop. 2 (Πφ_q = φ_qψ_q, Dirichlet polynomials twisted by Λ on the mesh), §5.3 | Selberg identity in the cubic entries; bounds of local Euler factors | class NO-GO (§5.3(iv)): comb identities valid in every Beurling system or for a_P, applied on E_T |
| 9 | Collar / boundary operator 𝓔_N | P46 eq:collar, thm:PCfinite, prop:GEgap; R170_840 Thm. 6.1, 862, 863, 870 (via `RULES_AVOID` §I) | 𝓞B_N = D_N𝓞 − 𝓔_N | two-sided collar law NO-GO by linear composition (840); parity wall (870); conversion of the tail into squares: `ROUND_002_A` + `REVIEW_002_A` |
| 10 | Boundary and Tate jets | 121 atlas («two Tate jets»), R170_862–863, 211 LEDGER C21 (boundary budget (EB_C), OPEN) | Pontryagin inertia; boundary budget | without sign; (EB_C) OPEN |
| 11 | Projection onto P_T, functionals A, B, piecewise Tate exponentials | P46 thm:coer-schur, prop:AM; 211 ROUND_005_C Lemma 1 (Tate gauge) | exact reduction to finite S_{T,k} | reformulation (L2) |
| 12 | Prolates / Slepian / Paley–Wiener / de Branges of the window | phases 72, 114, 155, 159, 186 (R186_044), 199, 200, 211 | prolate sector, reproducing kernels | `RULES_AVOID` C1: «Sonin, prolates, semilocal as a source of sign» closed |
| 13 | Resonators (tests blind to near-coincidences) | P46 prop:nearfree, rem:boxes | a_T(F_b) ≥ c_0‖F_b‖²; Σ_{d\|m}Λ(d) = log m enters the Schur test | barrier: they give no information on the sign (rem:boxes) |

On the concrete question (incidence on the Nyquist mesh): **it is written** in 211 ROUND_005_C. Prop. 2
identifies the responses of the comb on the mesh with Dirichlet polynomials twisted by Λ; §5.3(i) uses
multiplicativity non-linearly (Selberg on the cubic entries, whose cutoff depends only on N = mn) and
§5.3(iv) closes with a class NO-GO the use of Λ∗1 = log, Selberg and the local Euler factors as a sign
mechanism on E_T, because those identities hold literally in Beurling systems and for a_P, where (SL_T)
fails (NUMERICAL example 0.24 and 0.51). The reading of the identity Σ_{n<N}(log n)n^{−s} = Σ_{dm<N}Λ(d)(dm)^{−s}
evaluated at s_k = ½ + iω_k is thm:PCfinite (row K1) on the mesh.

### (1) Closest antecedent

For the mesh: 211 `ROUND_005_C.md` Prop. 2 and §5.3 (read in primary), with R186_052 §4 (the sampled comb
is of positive type, without sign) and P46 thm:nyq. For the grouped truncated translations: 204 `P1_BBSTAR_001.md`
§3 and `REVIEW_002_BC.md` Lemma B-1. For the boundary: P46 eq:collar and R170_840 Thm. 6.1.

### (2) Genuinely new object

None that carries a sign. What this memo adds are three PROVED restrictions (§1) that delimit where a
per-window V_T can be and what the leakage does, and an exact description of why the mesh separates the incidence
from the window (§2). With them, what would remain to be written for a candidate is: a family of functionals bounded
in the norm N_T (Lemma E), supported in the collar (T − log I, T) (Lemma F), that couple distinct nodes of the
mesh with coefficients depending on the values Λ(n) of the comb (Lemma S); ℋ_T, V_T, ρ_T of such a family are not
written and I do not know how to write them.

### (3) Why the change would avoid the difficulty of the antecedent

It does not avoid it. The difficulty recorded in ROUND_005_C §5.3 is that the comb identities used hold in
every Beurling system and for a_P. The incidence on the mesh is exactly one of them (Lemma S: it acts node
by node, as an identity of Dirichlet polynomials at the same s_k). Passing from E_T to the complete mesh does not change
the class of identities.

### (4) Identity that would connect with global positivity

Only reformulations already recorded: thm:nyq (diagonal in the samples), (L2′) of ROUND_001_C, and, for the
truncated translations, Lemma B-1. Lemma F below says which part of ρ_T is the sign obligation: in the
interior it is a symbol form s_T − σ_B on P_{T′}.

### (5) Lines that break for cΛ and a_P

There is no sign step, hence no sign line to point to. The only line that ceases to be true is the
substitution Σ_{d|n}a(d) = log n in the value of each node (c log n for cΛ; the logarithm of the P-rough part
for a_P): it breaks the identity linearly, like the separator; it does not break an inequality. By `OBJECT_SPEC.md` §4
the family is not ready for construction.

**Cross-check verdict: repetition for the mesh with incidence (ROUND_005_C §5.3; K1) and for the truncated
translations grouped in a fixed basis (P1_BBSTAR §3; B-1). No new mechanism.** The pieces of §1 are short and
complete; they are written because they delimit the terrain and require no additional derivation.

## 1. Three PROVED restrictions on a per-window V_T

In all that follows, (G) is a_T(F) = ‖V_TF‖² + ρ_T(F) on P_T ∩ 𝒟_T with ρ_T ≥ 0.

**Control norm.** Let N_T(F)² := (1/2π)∫(1 + log(2 + |τ|))|F̂(τ)|² dτ. There exists C_T with
|a_T(F)| ≤ C_T N_T(F)² on 𝒟_T. *Proof.* |m(τ)| ≤ C + log(2 + |τ|) (asymptotics of ψ; CITED, P46
lem:mbounds) and |Σ_{log n<2T} v_n cos(τ log n)| ≤ 𝒜_T = Σ v_n; hence |s_T(τ)| ≤ C_T(1 + log(2 + |τ|)). ∎

**Lemma E (NO-GO with class, PROVED).** If (G) holds, then V_T is bounded from (P_T ∩ 𝒟_T, N_T) into ℋ_T. In
particular no scalar component of V_T (no ⟨V_TF, e⟩, e ∈ ℋ_T) can be, on functions smooth
up to the boundary, of the form αF^{(j)}(T−) + (N_T-bounded functional) with α ≠ 0, j ≥ 0; likewise at −T and at
any interior point.

*Proof.* ‖V_TF‖² ≤ a_T(F) ≤ C_T N_T(F)² by ρ_T ≥ 0. For the second part, let φ ∈ C^∞[0,∞) with
support in [0,1] and φ^{(j)}(0) = (−1)^j, and g_λ(t) := λ^{−j}φ(λ(T − t)) on I_T. Then g_λ^{(j)}(T−) = 1, and
|ĝ_λ(τ)| ≤ λ^{−j−1}‖φ‖_1 for |τ| ≤ λ, |ĝ_λ(τ)| ≤ Cλ^{−j}/|τ| for |τ| > λ (one integration by parts: the
boundary term at T is λ^{−j}φ(0) and ‖g_λ′‖_1 = λ^{−j}‖φ′‖_1), so that N_T(g_λ)² ≤ C(λ^{−2j−1} log λ) → 0. Fix h_1, h_2 ∈ C_c^∞(−T, 0)
with det[A(h_i), B(h_i)] ≠ 0 (they exist because e^{t/2} and e^{−t/2} are linearly independent on (−T,0)) and
F_λ := g_λ − a_λh_1 − b_λh_2 ∈ P_T with |a_λ| + |b_λ| ≤ C(|A(g_λ)| + |B(g_λ)|) ≤ Cλ^{−j−1}. Then
N_T(F_λ) → 0 (N_T is a norm) and F_λ^{(j)}(T−) = 1. If ⟨V_TF, e⟩ = αF^{(j)}(T−) + β(F) with β N_T-bounded,
|α| ≤ |⟨V_TF_λ, e⟩| + |β(F_λ)| ≤ (C_T^{1/2}‖e‖ + ‖β‖)N_T(F_λ) → 0, contradiction. ∎

Declared class: V_T with some component that is not N_T-bounded on P_T ∩ 𝒟_T. Consequence: the admissible
«boundary functionals» are collar averages ∫F φ with φ ∈ L² (strictly, with φ̂ in the dual of N_T),
not values or jets. It is the per-window counterpart of R-cont (which does not apply here: `OBJECT_SPEC.md` §3
restricts it to the integer-scale carrier of A_0 and to the holomorphy of z ↦ P_z; L²(I_T) with the fixed mesh is not
that case). The samples F̂(ω_k) are N_T-bounded (|F̂(ω)|² ≤ 2T‖F‖²), hence Lemma E does not exclude them.

**Lemma F (localization of the leakage, PROVED).** Let ℓ_i = x_iQU_{log i}, x_i ∈ ℂ, with x_i = 0 for i > I, and
Q_B as in `REVIEW_002_BC.md` Lemma B-1 (σ_B(τ) = Σ_dΛ(d)|Σ_{d|i}x_i i^{iτ}|²). Let T′ := T − ½log I > 0. If
a_T = Q_B + ρ_T with ρ_T ≥ 0 on P_T, then for every F ∈ P_{T′} ∩ 𝒟_{T′}

    a_{T′}(F) ≥ (1/2π)∫σ_B(τ)|F̂(τ)|² dτ.

In particular, every almost-minimizing sequence of a_{T′} on P_{T′} (‖F‖ = 1) satisfies
(1/2π)∫σ_B|F̂|² ≤ λ_A(T′) + o(1).

*Proof.* For G ∈ P_{T′}, let F := U_{−c}G with c = ½log I (support in (−T, T − log I)). (a) P_T: A(F) =
e^{−c/2}A(G), B(F) = e^{c/2}B(G), hence F ∈ P_T. (b) Zero leakage: for i ≤ I, U_{log i}F has support in
(−T + log i, T − log I + log i) ⊂ I_T, so RΣ_{d|i}x_iU_{log i}F = 0 and, by Lemma B-1, Q_B(F) =
(1/2π)∫σ_B|F̂|². (c) a_T is translation invariant (symbol form), and on L²(I_{T′}) it coincides with
a_{T′}: the comb terms with 2T′ ≤ log n < 2T contribute v_n Re c_G(log n) = 0 because sop c_G ⊂ [−2T′, 2T′]
and c_G(±2T′) = 0. (d) |F̂| = |Ĝ|. Then a_{T′}(G) = a_T(F) = Q_B(F) + ρ_T(F) ≥ (1/2π)∫σ_B|Ĝ|². ∎

Reading. In the family of grouped truncated translations, the leakage acts only on the mass of F in the collar
(T − log I, T). On the interior, (G) requires a positivity of the symbol form s_T − σ_B ≤ s_T in the
window T′, that is (★) at T′ with margin (1/2π)∫σ_B|F̂|² ≥ 0 (cf. Lemma B-2). Since λ_A(T′) ≤ 4·10⁹T′e^{−15.449T′}
for T′ ≥ 1 (P46 cor:margin1, CITED), the grouped squares must vanish almost exactly on the
almost-minimizers of all shorter windows. If in addition the x_i do not depend on T and (G) is required for
every T (O5), that condition holds for every large T′. It is not an impossibility: it does not exclude σ_B small where
|F̂*|² lives. Answer to the question of the task: a compensation «leakage = boundary term with sign» can only
occur in the collar of length log I next to the right boundary (and, symmetrically, with negative
translations, next to the left one); outside it there is neither leakage nor boundary.

**Lemma S (the incidence on the mesh is local at the node, PROVED).** (i) The operation n ↦ dn multiplies the mode
e^{iω_k log n} by d^{iω_k}: on the samples it is diag(d^{iω_k}), the restriction to the mesh of the multiplier
e^{iτ log d}, that is the rotation of the circle 𝕋_{4T} by log d. (ii) For 0 ≤ a < 2T and F ∈ L²(I_T),
QU_a^{𝕋}F = QU_aF (the part that wraps around falls in (−2T, a − 3T) ⊂ ℝ∖I_T). (iii) The identity
Σ_{n<N}(log n)n^{−s} = Σ_{dm<N}Λ(d)d^{−s}m^{−s} at s = s_k relates values at the same node k. (iv) In the
identity thm:nyq a_T is diagonal in the samples, and what couples distinct nodes is only the constraint that
(F̂(ω_k))_k be in the image of the compression to the half-circle, a Toeplitz matrix without Λ (sinc
kernel; R186_053 Lemma 1.1). *Proof.* (i), (iii): direct. (ii): U_a^{𝕋}F has support in (−T + a, T + a)
modulo 4T; the points of (2T, T + a) pass to (−2T, a − 3T) and a − 3T < −T. (iv): lem:nyq-sampling (i)–(ii). ∎

**Consequences of the lemmas (PROVED, one line each).**
- If V_T is a multiplier in the sample index, (V_TF)_k = x_kF̂(ω_k), then ρ_T has samples
  s_k − |x_k|² ≤ s_k: it is Lemma B-2 on the circle. (By thm:nyq, ρ_T(F) = (1/4T)Σ(s_k − |x_k|²)|F̂(ω_k)|².)
- By (i)–(ii), every family built with the incidence acting on the modes and with Q is in the algebra
  generated by multipliers of the circle and truncated translations of the line: it is that of rows 2–3 of the
  inventory, not a new family.
- Every component of V_T that factors through (A(F), B(F)) is zero on P_T (projection onto P_T, row 11).
- An incidence on the node indices (squares Σ_dΛ(d)|Σ_{d|j}x_jF̂(ω_j)|², that is [log mcd(j,l)] on
  the mesh) does not contain the weights v_n of the comb: it is the same for Λ, cΛ, a_P and each model of the battery, and all
  the dependence on the comb remains in ρ_T. There is no arithmetic relation between the index j and the n of the comb (the
  phase is πj log n/(2T)). It is an auxiliary energy without sign mechanism (`RULES_AVOID.md` A4); I do not exclude it.

## 2. Against O6, prop:nearfree and K1

- **O6.** The samples see the near-coincidences: a deep sample s_k ≪ 0 requires ω_k log n ≈ 0 mod 2π for
  many n at once, which forces n′^{q_n} ≈ n^{q_{n′}} (211 ROUND_002_A Cor. M1–M2, CITED). But they see them in the
  value s_k, not in a coupling between nodes (Lemma S(iv)); that is why a V_T diagonal in the samples contributes
  nothing (consequence 1) and a non-diagonal one couples nodes only through the matrix without Λ or through an arithmetic of the
  index without comb.
- **prop:nearfree.** The resonators have a_T ≥ c_0‖F‖² with Σ_{d|m}Λ(d) = log m used in a Schur test
  (P46, proof of prop:nearfree; rem:boxes): linear and bounded use of the separator, without sign on the vectors
  that see Near. A useful per-window family would have to live where prop:nearfree gives nothing:
  N_T-bounded vectors (Lemma E) with mass in the collar (Lemma F) that see near-coincidences. I have no such family.
- **K1.** The reading on the mesh of the hyperbolic incidence is thm:PCfinite at s_k; its residue is that of K1 and
  K1′ (tail H_{M,N} added to E_N and Tate), without object.

## Result

**No new mechanism** (repetition of 211 ROUND_005_C §5.3, of K1 and of P1_BBSTAR §3 / Lemma B-1). In addition, one
**NO-GO piece with PROVED class** (Lemma E: non-N_T-bounded components, in particular boundary values and jets) and
two **PROVED** pieces without sign (Lemma F: the leakage of grouped truncated translations acts only in a collar and the
interior remainder is (★) at T′ with margin; Lemma S: the incidence on the mesh is local at the node and its algebra with Q
is that of truncated translations).

## What was proved

- Lemma E (NO-GO, class: V_T with some component not bounded in N_T on P_T ∩ 𝒟_T).
- Lemma F (localization of the leakage; necessary condition on almost-minimizers of shorter windows).
- Lemma S and its four consequences (sample multipliers ⟹ remainder with samples ≤ s_k; the incidence on
  the modes does not generate a new family; Tate functionals zero on P_T; incidence on node indices
  independent of the comb).
None of this is sign progress.

## What failed and why

- On the mesh, the divisor incidence lives in the value of each node and the window in a matrix without Λ that
  couples nodes; I found no operation that joins them into a square, and the one that joins values at a node was already
  used and closed by the Beurling/a_P class (ROUND_005_C §5.3(iv)).
- Pointwise boundary terms are forbidden (Lemma E); collar ones are linear in F and, as components
  of V_T, contribute squares without their own sign; the two-sided collar law by linear composition is closed
  (R170_840 Thm. 6.1, CITED via `RULES_AVOID` I6).
- The leakage of Lemma B-1 helps only in the collar (Lemma F); in the interior the remainder requires more than (★) at T′.

## What remains NOT excluded

- N_T-bounded collar functionals with coefficients depending on the values Λ(n) (outside the hypothesis
  «ℓ_i independent of the weights»); none written.
- Non-diagonal couplings between Nyquist samples with coefficients depending on the comb (not the
  arithmetic of the node index, which is independent of it); none written.
- Grouped truncated translations with x_i chosen so that σ_B is small on the almost-minimizers
  (Lemma F requires it, does not forbid it), with the compensation of the leakage in the collar; without object.
- Families on 𝔸_M and the formulation (S); joint compensation D + E (GLOBAL); the ungrouped residue K3 of
  P1_BBSTAR (empty class of candidates, not NO-GO).
- The phases listed as not opened in primary in the Cross-check.

## Concrete next step

None within this option with an object. For the record (this memo does not edit other files): ledger row
«K2″, per-window families different from the modal one (grouped truncated translations, Nyquist, boundary, P_T): no
new mechanism; NO-GO PROVED for non-N_T-bounded components (boundary values and jets); leakage localized in the
collar (Lemma F); incidence on the mesh local at the node (Lemma S)». Reopening condition: a coupling between
Nyquist nodes, or an N_T-bounded collar functional, whose coefficients depend on the values Λ(n) and whose
identity with a_T does not hold in a Beurling system nor for a_P, pointing out the line.
