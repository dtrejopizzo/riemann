# TRACT_F_PHASES000_001 — Phase 204, part F: the «CIRCULAR»/REF-D entries from phases 0–99, one by one

**Audited source:**
`05-meta-and-planning/ROUTES-TRIED-INDEX/03_PHASES_000-099.md` (hereafter `03_`). **Trigger:** AUDIT_204_TRACT_E_001 §4
(«`03_` has 1 REF-D line and 28 "CIRCULAR" omitted in bulk; a single new one, Nyman–Beurling, with no D-only form»).
The entries from phases 0–99 are written in terms of
zeros, depths b_j, de Bruijn–Newman Λ, etc.; here each one is **rewritten D-only** (a statement about the Weil form /
window form W_T on the declared carrier, without zeros) before being evaluated. If it admits no such form, this is
stated and it is excluded. TRAT criterion from TRACT_001 §0: YES = there exists a class 𝒯 of general theorems whose
missing hypothesis is **not** the sign; TRANSFER = the only missing hypothesis is «W_T ⪰ 0» rewritten; NO = closed by
theorem/falsifier. This memo proves nothing new except the observation in §2.3 (reduction of the D-only form of
Nyman–Beurling to K9), labeled as such.

## Summary (≤250 words)

**Corrected base count.** `grep -c CIRCULAR 03_` gives 28, but 2 hits are the header (l.6, l.8, vocabulary
definition). There are **26 real CIRCULAR rows** + **1 REF-D** (l.256, prose note about the phase-199 retry). Total
audited: 27 (plus 5 rows with lowercase «circular», reviewed in appendix §1.3).

**Result.** Of the 26 rows: **8 with no D-only form** (statements about zero location, counts, or Λ: excluded, not
reformulations of D), **18 with a D-only form**, all within an existing K (K1, K2, K3, K4/K5, K7, K8, K9,
K13, K16, K18, K23, K33). TRAT: **0 YES / 13 TRANSFER / 5 NO**. Line 256 (REF-D) is K? = L′♯/G3, already NO-GO as a
retry.

**Nyman–Beurling.** The classical form (density of dilates in L²(0,1)) is not D-only: its Hahn–Banach dual is
«there exists a zero at Re s > ½». But **a D-only window form does exist**: a statement about the angle between two
subspaces of L² (Sonin/prolate vs. Paley–Wiener_T), and that form **is K9** (ρ*(T) < 1 ⟺ D_T, PROVED by all-or-nothing
Müntz). The general density theorems (Müntz–Szász, Beurling–Malliavin, Hahn–Banach) decide *closure* (qualitative),
whereas D_T is an *angle bound* < 1 (quantitative); the missing hypothesis is the number ρ*(T), i.e. the sign. **TRAT
= TRANSFER.** No YES candidate remains at phase 204. Moreover, the index already listed Nyman–Beurling inside W1/REF-D
(`04_` l.12) and as L18 COVERED: TRACT_E's «omission» was one of wording, not of content.

---

## 1. Table of entries

D-only notation: W(f) = Weil form (archimedean side − prime side + poles) on tests f; W_T its restriction to
supp f ⊂ [−T, T] (window form); D_T: W_T ⪰ 0; D: D_T ∀T. «No D-only form» = the statement talks about zero positions,
counts, or a parameter (Λ, b_j) that cannot be expressed as the sign of W_T without going through an external
equivalence, which is not used here.

### 1.1 The 26 CIRCULAR rows

| # | line / phase | original statement (summarized) | D-only statement | K | TRAT and who decides it | reason for the original dismissal |
|---|---|---|---|---|---|---|
| 1 | l.31 MW-6 (NO-GO-LIST:234) | uniform spectral gap sup_X \|λ_min(Q_X)−λ_min(Q_∞)\|→0 | λ_min(W_T) ≥ 0 uniformly over prime truncations X: lim_X λ_min(W_{T,X}) = λ_min(W_T) and ≥ 0 | K8 (uniformity) / K5 | TRANSFER: convergence in X is PROVED (lem:contA, P47); the ≥ 0 limit is D_T | judgment («restates target») |
| 2 | l.33 NG-A1 | ω-class cross sum B(N) ≤ N^ε | no D-only form (Lindelöf-type bound for Dirichlet sums; not a sign of W_T) | — | excluded | judgment |
| 3 | l.37 NG-A5/CIR-6/ES-6 | Li/Jensen/GORZ/Báez-Duarte/finite Weil as progress | W(f) ≥ 0 for a finite family of tests (λ_n, n ≤ N; d_N, N ≤ N₀) | K3 (Li/finite order) | TRANSFER: each finite order holds; uniformity is D (AUDIT_E row K3) | judgment + method NO-GO (finite range does not control ∀f) |
| 4 | l.44 NG-B4/CIR-3 | Beurling–Nyman distance as a lower bound on depths b_j | no D-only form **in this wording** (b_j = zero depth). The D-only form of NB is built in §2 | — (see §2: K9) | excluded here; §2 | judgment |
| 5 | l.46 NG-B6/CIR-4 | Turán inequalities for ξ₀ | positivity of the 2×2 Hankel minors of the moments of the spectral measure associated with W (Turán = order-2 Hamburger/Pólya condition) | K3 / K24 (low-order SOS) | NO as a route: fixed-order Turán is a consequence of finite order, does not imply D (the full Pólya family does; that is K3) | judgment |
| 6 | l.49 CIR-1/2/5/7/8 | Selberg density, Levinson–Conrey proportions, ψ(x)−x=O(x^{½+ε₀}), KV compatibility, chaotic depth F3 | CIR-1/2: no D-only form (zero counts). CIR-5: D-only as «W(f_x) ≥ −C x^{ε₀}‖f_x‖ for step tests» = D-ψ from R186 (K7, thm:Z). CIR-7/8: no content (CIR-8 FALSIFIED) | K7 (CIR-5 only) | CIR-5: TRANSFER (thm:Z: certificate = explicit formula; quantitative ψ is D rewritten). Rest excluded / NO (CIR-8 falsified) | mixed: judgment (CIR-1/2/5/7), falsifier (CIR-8) |
| 7 | l.54 NG-D3 | G_ζ(t) > −G_ana(t) from Euler + EF | the prime part of W_T is dominated by the archimedean part: ⟨P_T f,f⟩ ≤ ⟨A_T f,f⟩ + poles | K5 (A_T/Schur) | TRANSFER; also NO as a method: the Euler product converges absolutely only for Re s>1 (W-lin/I13: a linear inequality is circular) | method theorem (absolute convergence) |
| 8 | l.83 ES-13 | Fejér–Riesz factorization | the symbol of W_T (Toeplitz/Wiener–Hopf function on the window) is ≥ 0 on the boundary and factors as \|h\|² | K4 (Douglas/Wiener–Hopf) | TRANSFER: Fejér–Riesz/Szegő consume the symbol ≥ 0 as data (AUDIT_E row K5) | judgment |
| 9 | l.86 ES-16 | de Branges / Hermite–Biehler | the Herglotz function associated with W (Stieltjes transform of the form) has nonnegative imaginary part; there exists a de Branges space realizing W_T | K1 (Herglotz/dB) | TRANSFER + NO for the known dB certificates (Conrey–Li, FALSIFIED) | falsifier (Conrey–Li) + judgment |
| 10 | l.87 ES-17 | approximants with real zeros → Ξ (Hurwitz) | no D-only form (approximation of an entire function with real zeros; the data is the zero positions) | — | excluded | judgment |
| 11 | l.89 ES-19 | GLT symbol / index / passivity in the limit | the sequence of matrices W_{T,N} has GLT symbol ≥ 0 and W_T is passive | K4/K1 (declared duplicate) | TRANSFER (reduces back to Herglotz, K1) | judgment (duplication) |
| 12 | l.97 ES-27 | real-divisor convergence sensitive to support | no D-only form (real support of divisors) | — | excluded | judgment |
| 13 | l.121 P32-3 | CTP: trace T_λ = 0 ∀λ | W(g_λ) = exact archimedean value for the Connes family of tests g_λ (trace identity = explicit formula) | K13 (exact chains) / K7 | NO as a route (sign-free identity; W12/W-det, AUDIT_E K13) | judgment |
| 14 | l.124 P33-2 | \|ζ\|² ≥ \|ζ_on\|² pointwise | no D-only form (comparison with a fictitious ζ built with zeros on the line) | — | excluded | judgment (requires zeros) |
| 15 | l.127 P33-5 | exponential decay of prime cancellation A^off = Σ_p | the prime part of W on tests B_λ equals the «archimedean+polar» part with exponentially small error in λ | K13 / K14 (estimates) | NO as a route: Prop 3.2 from phase 33 (each side is not provable separately) + lem:shape-est (sign-free estimates) | proposition (Prop 3.2) |
| 16 | l.130 P33-8 | NB variational density δ̃²_λ = 0 (completeness of {e^{iγs}}) | see §2: angle between subspaces in a window | **K9** | TRANSFER (§2) | judgment («completeness ⟺ target») |
| 17 | l.131 P33-9 | sign of dm_full − dm_full,on; extremality | no D-only form (comparison measure built with zeros on the line) | — | excluded | judgment |
| 18 | l.132 P33-10 | F(z) = ξ(z/(z−1)), ODE, Jensen | Jensen excess δ = 0; D-only: positivity of Li coefficients (Jensen on the disc ⟺ Li) | K3 | TRANSFER (K3) | judgment |
| 19 | l.133 P33-11 | relative entropy / KL / Wasserstein / max-entropy | W is the covariance form of a positive measure maximizing entropy under the arithmetic moments | K16 (spectral realization) / K18 (monotone functionals) | NO: W-identification (R168) covers the class; KL requires a positive measure as data (circular by construction) | judgment («all reformulate») |
| 20 | l.134 P33-12 | dBN flow on a Hadamard manifold | no D-only form (Λ = 0 is a statement about the family H_t; the form W has no natural t-parameter without going through zeros) | — | excluded | judgment |
| 21 | l.136 P34-2 | Pontryagin space (𝒦,Q), seven routes to κ = 0 | the negative index κ(W_T) is 0 | K2 (Kreĭn) | TRANSFER (finite κ is PROVED: Thm P n₋ ≤ 5/7/8; κ = 0 is D_T) | square-root barrier (critical a_tail 1): judgment with a computation |
| 22 | l.161 P40-3 | Weil vs. Hodge index on a surface | W_T ⪰ 0 as a Hodge-index inequality on an intersection carrier | K23 (polar/Frobenius) / Hodge transfer theorem (phase 135) | NO (W11; the positivity of CC is spectral, not intersection-theoretic; D.0 refutation) | class theorem (W11) |
| 23 | l.164 P42-1 | dynamical Hodge (Forni/EKZ) | W = Hodge form of a cocycle whose flow is the carrier's scaling flow | K16 | NO (the flow contains ζ: W-identification) | judgment |
| 24 | l.175 P49-3 | Tauberian probe | Tauberian condition on Σ Λ(n) n^{−½} f(log n) implying W(f) ≥ 0 ∀f | K7 (D-ψ) | TRANSFER («sufficient condition = target») | judgment |
| 25 | l.217 P70 | Lee–Yang / dBN monotonicity + Rodgers–Tao | no D-only form in the dBN version; the D-only residue that the record itself names is «Cauchy–Weil positivity» = D | — (residue = D) | excluded (Λ); the residue is D itself | judgment |
| 26 | l.228 P81 | bordered secular zeros as an independent measure | the spectral measure of the bordered (rank-1) form W_T is positive | K1 (inverse Stieltjes) / K33 | TRANSFER (inverse Stieltjes reintroduces the positivity of W) | judgment |

### 1.2 The REF-D entry

| line | statement | D-only | K | TRAT | reason |
|---|---|---|---|---|---|
| l.256 | note: «phase-199 retry PROOF_L_SHARP_OO_001 = NO-GO (retry, REF-D)» | already D-only (window L′♯) | G3 (gauge-minimized L′♯, no K; AUDIT_E §3) | NO as a route (NO-GO recorded in 06_); the target L′♯ remains OPEN | NO-GO (retry) |

### 1.3 Appendix: lowercase «circular» (not requested, reviewed so none is missed)

| line | entry | K | status |
|---|---|---|---|
| l.32 MW-7 | Hadamard barrier | K33 | NO (class barrier) |
| l.145 P35-5 | Bagchi–Voronin | K32 | TRANSFER (AUDIT_E: no D-only form written) |
| l.149 P36-3 | amplifying functor ⊠ | K2 (superadditive κ) | PARTIAL; no non-circular pair: TRANSFER |
| l.151 P36-5 | Lemma 108 | K26 | outside the inventory (AUDIT_E §2.4) |
| l.165, l.181 | Deninger, Gram flow | K23 / K2 | DEAD / PARTIAL; unchanged |

### 1.4 Count for table 1.1

- No D-only form (excluded): **8 rows** (#2, #4, #10, #12, #14, #17, #20, #25). #6 counts as D-only via its
  CIR-5 component (CIR-1/2/7/8 have no D-only form or are falsified). With D-only form: **18**.
- Of the 18: **TRANSFER 13** (#1, #3, #6, #7, #8, #9, #11, #16, #18, #21, #24, #26, and #5 in its K3 version) and
  **NO 5** (#13, #15, #19, #22, #23). #5 is counted in TRANSFER via K3 (fixed-order-only Turán, NO).
- **YES: 0.** No row is a «new» K: all fall into K1, K2, K3, K4/K5, K7, K8, K9, K13/K14, K16/K18, K23, K33.

---

## 2. Nyman–Beurling D-only

### 2.1 What the corpus tried and why it was closed

- **Phase 25** (`phase-25-lower-bounds-bj-audit/01-audit-classical.md`, index l.41 NG-B1): NB as one of 15 mechanisms
  for lower bounds on depths b_j. Closed: «aggregate not individual / circular».
- **NO-GO-LIST:77** (index l.44 NG-B4/CIR-3): «bounding d ⟺ bounding b_j». Judgment.
- **Phase 33, doc 82** (index l.130 P33-8): variational reformulation δ²_λ = 0 in L²(W_λ dm_∞) and completeness of
  the system {e^{iγ_n s}} via Beurling–Malliavin. Doc §7.3: «we do not know how to prove completeness without assuming
  the γ_n are real»; BM does not apply to complex exponents. That is, doc 82 closed it **because it was written over
  zeros**: the completable system was exponentials at the zeros' ordinates.
- **Phase 155 cor:Li / R160_S4 #39** (`04_` l.379, l.444): Li/Keiper and Báez-Duarte as flat-top certificates: Li
  kernel outside W_T (DEAD [OTHER]); REF-D not closed.
- **`04_` l.12 W1/REF-D:** NB appears nominally among the «honest reducers» (reformulations of D, PARTIAL, with no
  provable weaker statement). **No D-only form is written** in any memo: AUDIT_E is right about the content.
- **R186_000 D-NB:** «there is no specific method theorem; the L² approximation form has no window structure».
- **Literature:** L18 COVERED; L61 (arXiv 2203.05030, 2405.06349, 2310.03972, 2023–25, Gram/Hardy) **NOT IN CORPUS**;
  L79 (Báez-Duarte constant, decoupling) in 05b_.

### 2.2 Why the classical form is not D-only

Nyman/Beurling criterion: 𝟙_(0,1) ∈ closure in L²(0,1) of {Σ c_k ρ(θ_k/x) : Σ c_k θ_k = 0}. By Hahn–Banach, the
closure is strict ⟺ there exists g ∈ L²(0,1), g ⊥ every ρ(θ/x), ⟨𝟙,g⟩ ≠ 0; the Mellin transform of such a g factors
through ζ(s)/s and its nonvanishing in the right Hardy half-plane forces a zero of ζ at Re s > ½. The dual of the
statement is **a zero**, and the equivalence with Weil positivity would go through the forbidden equivalence. Under
the methodological rule: the classical form **is not D-only** and is not used.

### 2.3 Building the D-only (window) form

The target's hint is correct in its geometric half: W_T is an indefinite inner product and its positivity is an
**angle** statement. Concretely (everything in L²(ℝ) with the measure of the archimedean part of the carrier):

- Write W_T = A_T − P_T with A_T > 0 (archimedean, PROVED in P47 by the positivity of the Γ kernel) and P_T compact
  (primes + poles, finite in the window). D_T ⟺ ‖A_T^{−½} P_T A_T^{−½}‖_+ ≤ 1 (contraction; K5).
- The Connes–Sonin realization (phase 183, K9): there exists a subspace 𝒮 (Sonin: functions with support and
  Fourier-support outside the window, in the carrier's normalization) and PW_T such that the non-archimedean part of
  W_T reads as the cosine of the angle between 𝒮 and PW_T; ρ*(T) := cos∠(𝒮, PW_T) in the A_T metric. Phase 183/186:
  **D_T ⟺ ρ*(T) < 1**, PROVED (all-or-nothing Müntz: the defect is either 0 or the whole space, so «< 1» is all that
  matters).
- **D-only form of NB (window):** «the fixed vector e_T (the projection of the pole test, which in the Mellin image is
  the analogue of Nyman's 𝟙_(0,1)) is not in the closure, in the A_T metric, of the span of the dilates of the prime
  kernel restricted to the window, with distance ≥ c(T) > 0». By the angle theorem (Friedrichs/Dixmier: two closed
  subspaces have a positive angle ⟺ their sum is closed ⟺ the distance from the unit sphere of one to the other is
  > 0), this positive distance is exactly 1 − ρ*(T)² > 0.

**Label for §2.3:** the existence of the D-only form is ARGUED (it is K9 rewritten in the language of distances; the
identification of the vector e_T with Nyman's «𝟙» is a Mellin analogy, not a theorem). The equivalence with D_T used
is that of K9, PROVED in the corpus; nothing external is invoked.

### 2.4 Is it its own path (TRAT = YES)?

There are three families of general density theorems. For each, what is the missing hypothesis?

1. **Müntz–Szász / Beurling–Malliavin (completeness radius).** These decide *whether a system is complete* (closure
   = everything), as a function of an exponent density. They are qualitative: they do not give the angle constant. In
   the window the system of dilates of the prime kernel has finite effective dimension (primes p ≤ e^T), so
   qualitative completeness is trivial or false by dimension; what D_T asks for is **the angle bound**, which BM does
   not see. Moreover, K9's all-or-nothing Müntz result already *is* the application of this family: what it leaves is
   precisely «ρ*(T) < 1». Missing hypothesis: the number ρ*(T) = the sign. **TRANSFER.**
2. **Hahn–Banach / duality.** Converts «distance > 0» into «no annihilating functional with controlled norm exists»;
   in the window, that functional is a negative eigenvector of W_T. Cone duality = K7 (thm:Z). **TRANSFER** (the dual
   of the statement is its negation, not new input).
3. **Angle theorems (Friedrichs, Kato, Hadamard on variation in T).** These are the only ones with quantitative
   content. Applied here they give continuity/monotonicity of ρ*(T) in T (lem:contA and lem:monoT, PROVED), i.e. they
   reduce D to «ρ*(T) < 1 for large T»; the bound itself is given by no general theorem: it needs the window's
   arithmetic data. This matches TRACT_001's diagnosis for R6 (2×2 polar capacity), already TRANSFER after
   POLAR_CAP_001.

Class falsifier (why no non-arithmetic density hypothesis suffices): the Beurling DMV/Zhang carrier (phase
150, T3; I6) has the same dilate structure, the same archimedean part, and satisfies every qualitative density
hypothesis (the generalized «primes» have the same logarithmic density), and yet its window form has a negative
direction for large T (CITED, DMV; T3 CONDITIONAL on (H-DMV), O-150.1). If T3 is lifted, this is NO-GO for any
NB-window proof using only density; in the meantime the verdict is TRANSFER, not NO.

**Verdict:** the D-only form of Nyman–Beurling **exists** (ARGUED, §2.3) and **is K9** (not a new K). **TRAT =
TRANSFER**: density/angle is equivalent to positivity by angle duality, and the hypothesis the general theorems do
not provide **is** the sign (ρ*(T) < 1). It is not the live candidate the target had in mind. Phase 204 is left
**with no TRAT = YES reformulation**.

Honest residue (OPEN, not a route): the 2023–25 NB literature (L61) is not in the corpus. If any of those works gives
a *quantitative lower bound* on a dilate angle without using zeros, it would be input for K9; reading it is a reading
task, not a construction task, and does not change the verdict without an explicit bound.

---

## 3. Final count and index entry

**Count.** 28 «CIRCULAR» hits = 2 header + 26 rows; + 1 REF-D (l.256) = 27 entries. No D-only form: 8
(excluded). With D-only form: 18 + l.256. TRAT: **0 YES / 13 TRANSFER / 6 NO** (5 rows + l.256). All in existing K's;
Nyman–Beurling D-only = K9 (TRANSFER). AUDIT_E §4 is confirmed in substance and corrected on two points: the
count (26, not 28) and the fact that NB **does** have a D-only form (via K9), though it was not written down.

**Proposed entry for `ROUTES-TRIED-INDEX/README.md` (phase 204 section):**

> - **TRACT_F_PHASES000_001 (phase 204, part F):** the 26 CIRCULAR rows (+2 header hits) and the
>   REF-D (l.256) from `03_` rewritten D-only one by one: 8 with no D-only form (zeros/Λ/counts, excluded), 19 in
>   existing K's; 0 YES / 13 TRANSFER / 6 NO. Nyman–Beurling: the classical form is not D-only (its dual is a zero);
>   the window form exists (ARGUED) and is K9 (Sonin–PW_T angle, ρ*(T) < 1); Müntz–Szász/BM/Hahn–Banach give closure,
>   not the angle bound: TRANSFER. Phase 204 has no TRAT = YES reformulation. Do not retry NB as «density» without a
>   quantitative, zero-free angle bound (L61 unread).
