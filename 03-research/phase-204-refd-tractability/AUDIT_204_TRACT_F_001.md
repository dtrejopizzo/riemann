# AUDIT_204_TRACT_F_001 — Audit of TRACT_F_PHASES000_001 (phase 204, step 2, phases 0–99)

**Object:** `TRACT_F_PHASES000_001.md` (hereafter F).
**Sources checked:** `05-meta-and-planning/ROUTES-TRIED-INDEX/03_PHASES_000-099.md` (`03_`), own grep
("CIRCULAR", "circular", "REF-D", "equivalen", "reformul", "tautolog", "⟺", "restat"); `phase-33/82` and `phase-33/85`;
`phase-200-sign-object/Q2_LADDER_001.md` (Lemma R, R-Q2); index README l.517, l.521; TRACT_001 §0 criterion.
**Premise:** row D / L′♯ independent goal; no external equivalence is used. Every row is judged only
by its D-only form (a statement about W_T on the declared carrier, with no zeros).
**Label criterion for NO:** a route is closed only by an impossibility theorem within a declared
class or by an explicit falsifier. A "judgment" in the record is not enough for NO.

## Summary (≤250 words)

F is correct in its overall verdict (0 YES) but has errors of counting, exclusion, and labeling.
(1) **Count:** `grep -c CIRCULAR 03_` gives **27**, not 28; actual uppercase rows = **25**; F reaches 26 by including NG-A1
(l.33), which is "NO-GO (circular)" in lowercase. The appendix says "5 rows" and lists 6.
(2) **Excluded:** of the 8 "without D-only form", **4 actually have one** (#10 Hurwitz, #12 ES-27, #20 dBN, #25 P70): all
TRANSFER. Only #2, #14, #17 remain excluded (and #4, absorbed in §2).
(3) **Mis-placed NOs:** #13 (CTP), #15 (Prop 3.2), #23 (dynamical Hodge) rest on judgments, not on class theorems
or falsifiers → TRANSFER. #5 was counted twice.
(4) **Nyman–Beurling/Báez-Duarte:** Báez-Duarte's primal statement contains no zeros, but **it is not a form of D**:
it does not speak of W_T, and its only link with D runs through zeros. The identification "density of dilates = the radical is everything =
negation of positivity" is **false**: Lemma R says that combs of integer dilates are W-null; a large radical
does not decide the sign. NB's D-only form remains only K9 (TRANSFER). F omits doc 85 (unconditional completeness
of the linear span; the gap is the nonlinear class).
(5) **Omissions:** 10 rows with "tautolog/⟺/reformul" not evaluated.
**Corrected:** 22 D-only + l.256: **0 YES / 20 TRANSFER / 3 NO**; 3 excluded; + 10 omitted (4 TRANSFER, 3 NO, 2
excluded, 1 tool).

---

## 0. Count verification

- `grep -c CIRCULAR 03_` = 27 (lines 6, 8, 31, 37, 44, 46, 49, 54, 83, 86, 87, 89, 97, 121, 124, 127, 130–134, 136,
  161, 164, 175, 217, 228). Removing the header (l.6, l.8): **25 rows**. F says 28/26.
- F includes #2 = l.33 NG-A1, whose outcome is "NO-GO (circular)" (lowercase). Reviewing it is legitimate, but then
  the criterion is not "CIRCULAR" but "circular" without case distinction, in which case appendix §1.3 should have been
  merged into the table. Correction: 25 CIRCULAR rows + NG-A1 + 6 from the appendix (l.32, 145, 149, 151, 165, 181; F says "5").
- F's §1.4 counts #5 as TRANSFER while also describing it as NO "of fixed order". One row, one label: **TRANSFER
  (K3)**; "fixed-order Turán does not imply D" is an observation, not a closure.
- F's summary: "5 NO"; §3: "6 NO (5 + l.256)". Consistent only if it is clarified that l.256 is outside the 26.

## 1. The 8 excluded "without D-only form"

Rule applied: if the row is a statement about zero positions/counts or about a function built from zeros,
it has no D-only form. If the row is (or can be rewritten as) a closure/approximation/deformation property of the
form, it does have one.

| # | row | D-only form? | audit rewrite | TRAT |
|---|---|---|---|---|
| 2 | NG-A1, B(N) ≤ N^ε | **No.** It is a growth bound for Dirichlet sums by ω-classes; the record closes it because it is stronger than Lindelöf. There is no sign inequality over W. | — | excluded (and outside uppercase "CIRCULAR") |
| 4 | NG-B4, NB distance vs b_j | Written in terms of depths; F transfers it to §2. Correct. | see §3 | absorbed into #16 |
| 10 | ES-17, real-zero approximants → Ξ (Hurwitz) | **Yes.** The D-only analog of Hurwitz is the *closure of the PSD cone*: construct forms W^{(n)}_T ⪰ 0 (e.g. truncations/regularizations of the carrier) with W^{(n)}_T → W_T weakly on the window; the weak limit of PSD forms is PSD. | "∃ sequence W^{(n)}_T ⪰ 0, W^{(n)}_T(f) → W_T(f) ∀f ∈ C_c(−T,T)" | **TRANSFER.** The convergence is cheap (lem:contA gives it for truncations in X); the positivity of the converging approximants is D_T rewritten (the record says the same: "building convergence is the whole work"). Cross-reference: Thm finZ + reverse track (no finite approximant has a certificate). |
| 12 | ES-27, convergence of real divisors | **Yes**, same rewrite as #10 (preserving the closed property "⪰ 0" in the limit). | same as #10 | **TRANSFER**, duplicate of #10 |
| 14 | P33-2, \|ζ\|² ≥ \|ζ_on\|² | **No.** ζ_on is built from the zeros. | — | excluded |
| 17 | P33-9, dm_full − dm_on | **No.** dm_on is built from the zeros. | — | excluded |
| 20 | P33-12, dBN flow | **Yes, debatable.** The heat deformation has a *formal* D-only version: W^{(t)}(f) := W(G_t∗f) with G_t a Gaussian multiplier on the archimedean side; "λ_min(W^{(t)}_T) ≥ 0 for t ≥ 0 and monotone in t". At t = 0 it is D_T. What does not transfer are the theorems about Λ (Newman, Rodgers–Tao), which are proved on the zero side. | "t ↦ λ_min(W^{(t)}_T) monotone and ≥ 0 at t = 0" | **TRANSFER** (the value at t = 0 is the sign; no general flow theorem gives monotonicity of λ_min for a family that is not the heat family on the form). ARGUED. |
| 25 | P70, Lee–Yang/dBN + Rodgers–Tao | **Yes.** F itself writes "the D-only residue is Cauchy–Weil positivity = D". A row whose residue *is* D has D-only form; excluding it is incoherent. | "D_T" (residue named in `03_` l.217) | **TRANSFER** (trivial) |

**§1 result:** actually excluded **3** (#2, #14, #17) + #4 absorbed. The 4 reclassified (#10, #12, #20, #25)
fall into TRANSFER; none yields YES, because the missing hypothesis is the positivity of the approximant/deformation.

## 2. F's 13 TRANSFER and 6 NO, one by one

| # | F | review | ruling |
|---|---|---|---|
| 1 MW-6 | TRANSFER K8 | Convergence in X is lem:contA (PROVED). The limit ≥ 0 is D_T. Covered. | TRANSFER ✓ |
| 3 NG-A5 | TRANSFER K3 | Correct; the recorded reason ("finite stretch does not control ∀f") is a judgment, not a NO-GO. | TRANSFER ✓ |
| 5 NG-B6 Turán | double TRANSFER/NO | See §0. | TRANSFER (K3) |
| 6 CIR-5 | TRANSFER K7 | Correct for CIR-5; CIR-8 is FALSIFIED but it is "chaotic depth F3", with no D-only form → does not count as a NO for D. | TRANSFER ✓ |
| 7 NG-D3 | TRANSFER + "NO as method" | **Debatable (a).** "Euler converges absolutely only for Re s > 1" is not an impossibility theorem: in the window the prime part is finite (p ≤ e^T) and needs no convergence. The relevant closure is W-lin (NO-GO for linear certificates, P46 rem:bar-lin), which is a different class. Mixing the two overstates the case. | TRANSFER (the "method NO" only holds within W-lin) |
| 8 ES-13 | TRANSFER K4 | Correct; also README l.521(a): Fejér–Riesz over 𝒬_μ NO-GO (symbol null by FE). F does not cite it: that NO-GO is about a different object (𝒬_μ), it does not close K4 on W_T. | TRANSFER ✓ (cite l.521) |
| 9 ES-16 | TRANSFER + NO | Conrey–Li falsifies *concrete dB certificates*, not the Herglotz class. | TRANSFER ✓ |
| 11 ES-19 | TRANSFER | duplicate of #9. | TRANSFER ✓ |
| 13 P32-3 CTP | **NO** "sign-free identity" | **Debatable (b).** The record says "CTP restates target": "trace T_λ = 0 ∀λ" is not an unconditional identity but the goal rewritten (if it were a sign-free identity it would not be CIRCULAR). F confuses CTP with the trace identity = explicit formula (W12/W-det), which is indeed unconditional. There is no theorem or falsifier closing CTP. | **TRANSFER** (K13/K7) |
| 15 P33-5 | **NO** (Prop 3.2) | **Debatable (c).** Phase 33's Prop 3.2 says that *neither side is provable separately* from the information used; it is a method observation with no declared class. lem:shape-est gives sign-free estimates, which describes the transfer, it does not forbid it. | **TRANSFER** |
| 16 P33-8 NB | TRANSFER K9 | see §3. | TRANSFER ✓ |
| 18 P33-10 | TRANSFER K3 | Correct. | TRANSFER ✓ |
| 19 P33-11 KL | NO | W-identification (R168) is a class theorem (spectral realizations whose datum contains ζ). It stands. | NO ✓ |
| 21 P34-2 | TRANSFER K2 | Correct; Thm P (n₋ ≤ 5/7/8) PROVED, κ = 0 is D_T. | TRANSFER ✓ |
| 22 P40-3 | NO (W11) | W11 is a class theorem; refutation D.0. | NO ✓ |
| 23 P42-1 | NO | **Debatable (d).** "The flow contains ζ" is the record's judgment; F attaches W-identification to it, but that covers *spectral* realizations, not dynamical Hodge cocycles (Forni/EKZ), which is a different class. No theorem for this class. | **TRANSFER** (K16) |
| 24 P49-3 | TRANSFER K7 | Correct. | TRANSFER ✓ |
| 26 P81 | TRANSFER K1/K33 | Correct. | TRANSFER ✓ |
| l.256 | NO (retry) | NO-GO recorded in 06_. | NO ✓ |

Debatable cases argued: (a) #7, (b) #13, (c) #15, (d) #23. The last three change from NO to TRANSFER; the
effect on the overall verdict is nil (none becomes YES), but the index must not record them as closed.

## 3. Nyman–Beurling / Báez-Duarte

### 3.1 What F omits from the corpus
F cites doc 82 (§7.3: "we do not know how to prove completeness without real γ_n"), but **not doc 85**
(`phase-33/85-completeness-of-exponential-systems.md`), which corrects 82: the γ_n are always real as imaginary
parts, the *linear span* of {e^{iγ_n s}} is **unconditionally** complete (Thm 5.1), and the gap is that the
Hadamard-critical class is **nonlinear**. The closure reason recorded at l.130 is outdated; the live residue of
phase 33 is "nonlinear approximation", not "completeness". This should be noted in `03_` l.130.

### 3.2 Is Báez-Duarte D-only?
Primal statement: 𝟙 ∈ L²(0,1)-closure of span{ρ(1/(nx))}_{n∈ℕ} (or d_N → 0). It is correct that **it does not mention zeros**:
it is a statement about approximation by integer dilates. But "D-only" requires two things: (i) no zeros and (ii) that
it be a statement about the window form W_T. Báez-Duarte satisfies (i) and **fails (ii)**: there is no bridge in the
corpus or in the known literature, "density of dilates ⟺ W_T ⪰ 0 ∀T", that does not pass through zero localization
(both sides connect to zeros separately). Using it as a reformulation of D would be using a chain of external
equivalences that the rules exclude. Báez-Duarte is a **sibling goal**, not a form of D. Its Hahn–Banach dual
("there exists g ⊥ every ρ(1/(nx)), ⟨𝟙,g⟩ ≠ 0") also does not mention zeros in itself; via Mellin it becomes a zero, and
that confirms that the natural link is with zeros, not with W.

### 3.3 The radical question — made precise, and the proposed identification is false
Lemma R (Q2_LADDER_001 §1, PROVED given Guo L4.4): for A(g) = 0 and P finite, every comb ζP(∂)g — in particular
integer dilates with truncated Möbius weights — is **radical** for W_T (W-null, orthogonal to everything in the form).
R-Q2: levels, p-classes, S-coprime parts are coordinates within the radical.

Precise consequences:
1. The radical of a Hermitian form is irrelevant to its sign: W_T ⪰ 0 ⟺ W_T induces a ⪰ 0 form on the quotient
   by the radical. If the radical were "everything" (dense in the form's topology), W_T ≡ 0 — which is **false**
   because A_T > 0 dominates in directions outside the combs. If it is dense only in the L²(0,1) topology (a different
   one), nothing follows about the sign: the topologies do not coincide and W_T is not continuous with respect to
   L²(0,1) in general.
2. Therefore "density of dilates = the radical is everything = negation of positivity" **does not hold** in either
   direction. The correct statement: **integer dilates are invisible to W_T**; Báez-Duarte density, read in
   the form, has **zero** sign content. This is a restriction (R-Q2 type), not a route.
3. Báez-Duarte's missing hypothesis is neither the sign of W_T nor density in the Müntz sense: in Bohr's
   formulation (Hedenmalm–Lindqvist–Seip; Nikolski), completeness of {φ(nx)} is equivalent to the *cyclicity* of the
   Bohr lift of a Dirichlet series in H²(𝔻^∞), and for ρ that series is of type ζ(s)/s: its cyclicity is a
   non-vanishing statement, i.e. about zeros. The general completeness-of-dilates theorems (Beurling 1945, Wintner, HLS)
   have that cyclicity as their missing hypothesis, which does not reduce to anything about W_T.

**§3 ruling:** Báez-Duarte via integer dilates is **not TRAT = YES** for D: it is TRAT = n/a (not a form of D). The
only D-only form of NB remains F §2.3's window form = K9 (ρ*(T) < 1), **TRANSFER**; the analysis of F §2.4 is accepted
with one correction: the "identification of e_T with Nyman's 𝟙" is an analogy; the window form stands
only as K9 rewritten, not as Nyman–Beurling. Label: ARGUED. Useful new record entry: "Lemma R ⇒ integer
dilates with Möbius weights are W_T-null; Báez-Duarte-type density carries no sign" (PROVED from Lemma R).

## 4. Omissions in `03_`

Grep of synonyms (tautolog, ⟺, reformul, equivalen, restat) outside the CIRCULAR rows:

| line | row | D-only form | TRAT |
|---|---|---|---|
| l.40 NG-A8/ES-4 | zero-side Gram ≈ 0.866, "PSD by construction" | No (zero-side Gram) | excluded |
| l.57 NG-E2 | scalar λ_min(Q), "quasi-tautological" | Yes: λ_min(W_T) ≥ 0 = D_T | TRANSFER (dropped as useless, not as impossible) |
| l.66 NG-F0 | H1 ⟺ ‖A^{−½}BA^{−½}‖ < 1 | Yes: contraction, K5 | TRANSFER |
| l.98 RET-Ω7 | \|λ_n^prime\| < λ_n^arch ∀n | Yes (two-sided coefficient bound) | NO (FALSIFIED at n = 1) |
| l.120 P32-2 | PCN, "Stieltjes reformulation" | Yes (kernel concentration for the form) | NO (Prop 2.1, Fourier) |
| l.151 P36-5 | Lemma 108, "restates target at k=2" | Yes: sup κ_W bounded, K2 | TRANSFER (F left it out of the inventory unevaluated) |
| l.158 P39-1 | R-NC non-circularity test | tool | n/a |
| l.186 P55-3 | energy dichotomy, "half-equivalence" | No (witness density tied to zeros) | excluded |
| l.200 P60-4 | n² ⟺ (T★), Airy/Bessel | Yes (limit operator) | NO (FALSIFIED) |
| l.220 P73 | cell residue; "tautological rowspace version" | Yes (rowspace = D_T) | TRANSFER |

No omission is YES. Also l.32 MW-7 ("every CCM criterion is a reformulation") is in F's appendix and is NO
(barrier): consistent.

## 5. Corrected verdict of inventory F

- CIRCULAR rows in uppercase: 25 (+ lowercase NG-A1 that F included) = 26 reviewed; + l.256.
- Excluded without D-only form: **3** (#2, #14, #17); #4 absorbed into #16.
- With D-only form: **22** + l.256.
- TRAT: **0 YES / 20 TRANSFER / 3 NO** (#19, #22, l.256). Changes relative to F: +4 TRANSFER from the excluded ones
  (#10, #12, #20, #25); #13, #15, #23 from NO to TRANSFER; #5 no longer double-counted.
- Omissions evaluated: 10 (4 TRANSFER, 3 NO, 2 excluded, 1 tool).
- Nyman–Beurling: D-only form = K9, TRANSFER. Báez-Duarte via integer dilates is not a form of D; by Lemma R the
  dilates are W_T-null and carry no sign. Doc 85 not cited by F: phase 33's residue is nonlinear.
- F's overall verdict (phase 204 with no TRAT = YES reformulation) **is confirmed**.

**Index entry (README, phase 204 section):**

> - **AUDIT_204_TRACT_F_001 (audit of TRACT_F):** actual count 25 CIRCULAR (+NG-A1, +l.256);
>   4 "excluded" rows actually have D-only form (Hurwitz/divisors = closure of the PSD cone; dBN = Gaussian deformation of W;
>   P70 = D) → TRANSFER; CTP, P33-5, dynamical Hodge move from NO to TRANSFER (judgments, no theorem). Corrected:
>   0 YES / 20 TRANSFER / 3 NO + 10 omissions (0 YES). Báez-Duarte is not a form of D; by Lemma R integer dilates
>   with Möbius weights are W_T-null (no sign content); "density = total radical = ¬positivity" is false. Cite doc 85
>   in `03_` l.130 (unconditional complete linear span; nonlinear residue).
