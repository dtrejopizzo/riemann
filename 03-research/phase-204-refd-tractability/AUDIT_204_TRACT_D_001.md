# AUDIT_204_TRACT_D_001 — Audit of the tractability inventory, part D (TRACT_D_README_001)

Phase 204, step 2, part D · audit · labels PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL. Only this
file is written; the index entry goes in §6 for the coordinator to copy.

Sources read: TRACT_D_README_001, TRACT_001, L2_INTERLACE_001, POLAR_CAP_001 (summary and index l.598),
BARRIER_SOUND_001 (header), ROUTES-TRIED-INDEX/README.md (l.55, 135, 138–145, 146–148, 165, 174–178, 186, 205–212,
247–248, 263, 296, 340–382, 390–391, 415, 427, 451, 460, 502, 504, 507, 523, 538, 539, 552, 560, 571, 588, 589,
597–598), INV_U_001 (U0, U2, U5b, 𝒦_cross), BARRIER_W_001 (class header), Paper 47 main.tex lem:monoT (l.502) and
lem:flowdet (l.8134).

## Summary (≤300 words)

The TRACT_D inventory is correct in bulk (G1, G2, G5–G9, G11–G13, G15, G17): the 31 NO and the 46 TRANSFER are well
cited except for citation details (l.571–573) and seven grep omissions, all TRANSFER. **The YES entries do not hold
up.** (a) **G10**: the "identities only" induction L*_j of l.142/347/367 is not the same object as (L2), but it is
also not a distinct induction with a live gap: the gap (θ) was *closed as a specification* (l.367, Prop Θ) and
reduced in CA_R4 (l.369–376) to the near-cancellation of the shifted copies of h*_j read by 𝔄_j^{−1}, which is the
exterior field C*_A of the minimizer (EI_001) = a functional of h* (Theorem X); moreover U0/U5b say that neither λ
nor λ′ jumps at the contact, so "the contact step" transports no information: everything happens between contacts,
in 𝒦_W ∪ 𝒦_H. → TRANSFER. (b) **G14**: the Robbin–Salamon crossing form is ⟨v, Ȧv⟩ on the kernel = lem:flowdet
(Hellmann–Feynman) = BARRIER_W §5; the only thing it adds (signature at degenerate crossings, homotopy invariance)
is already in 𝒦_W. Worse: the requested lemma G14.2 ("Γ > 0 at every crossing") is **impossible** by lem:monoT
(λ_A non-increasing ⇒ Γ ≤ 0). → NO. (c) **G4**: 𝔤_par = W_T(h_par) with
h_par = H₀ − (𝔞_T|𝒬^par)^{−1}𝔞_T(H₀,·): it does invert 𝔞|P_T (POLAR_CAP_001). → TRANSFER. (d) **L′♯ by Fredholm**: the
"missing relative compactness" is free (compact resolvent, S5; R186 Thm A/B PROVED); the residue is the positivity
of the finite block = (L2) = REF-D in bulk. → TRANSFER. (e) **G16** remains as the only YES, weakly conditional,
with G16.0 as gate.

Corrected count (90 entries): **NO 32 · TRANSFER 56 · YES 2** (l.521(f), 523, both G16 conditional). No NO/TRANSFER
is promoted to YES with input for D; two non-sign residues (l.391 G1, l.415 G1) are tractable but are not
reformulations of D. Next construction to launch: G16.0 (descent to the quotient), cheap and decisive.

---

## 0. Corpus and index check

The object of this audit is the inventory itself, not a new route; no construction is proposed that is not already
in the index. The hits relevant to the verdicts are cited inline. For (a) all SPEC_A entries were read
(l.138–145, 345–349, 362–382); for (b) BARRIER_W_001 and Paper 47 lem:monoT, lem:flowdet; for (c) POLAR_CAP_001
(index l.598); for (d) R186 Thm A/B as summarized by L2_INTERLACE_001 §1.

## 1. The 31 NO and the 46 TRANSFER, one by one

Promotion-to-YES criterion (TRACT_D §0's own): there exists a general theorem whose missing hypothesis is not the
sign. I review each row of TRACT_D's §3 table; I group the ones sharing a closing theorem and flag only the
debatable ones.

### 1.1 Verification table

| l. | G | TRACT_D verdict | correct citation and covers the D-only form? | audited verdict |
|---|---|---|---|---|
| 55 | G8 | NO (empty) | yes: at T₀ ≤ 0.3 the window is covered by Theorem A | NO |
| 135 | G8 | TRANSFER | yes (lem:shape-est(i): edge at margin scale) | TRANSFER |
| 165, 174, 263, 377 | G9 | TRANSFER | yes: Theorem X (functional of h*) | TRANSFER |
| 175 | G8 | TRANSFER | yes: T*₃(η) = (S) | TRANSFER |
| 212 | G1 | TRANSFER | yes (cone duality; density ceiling) | TRANSFER |
| 251 | G14 | TRANSFER | yes: "support = 𝔞_T ≻ 0" | TRANSFER |
| 255 | G1 | TRANSFER | yes: thm:sos | TRANSFER |
| 277 | G11 | NO | yes: Cor 6 gives separation, not inequality | NO |
| 284, 306, 357, 387, 389, 524 | G1 | TRANSFER | yes: thm:Z/thm:O; LP/BL duality consumes the sign | TRANSFER |
| 294, 434 | G11 | NO | yes: INVENT Thm 2.3 (concavity ⇒ upper bounds only) | NO |
| 296 | G8 | TRANSFER | yes: Schoenberg/Bochner consumes PD | TRANSFER (debatable, §1.2 D3) |
| 344 | G9 | NO/TRANSFER | yes: interpolation W(α) NO-GO PROVED; central cell = REF-D | NO (W(α)) + TRANSFER (cell) |
| 350 | G11 | TRANSFER | yes: Beurling–Deny; identification PROVED | TRANSFER |
| 353 (D_∃c) | G11 | TRANSFER, weaker | correct citation (AUDIT_203: c=0 negative for T ≥ 0.60) | TRANSFER (debatable, D4) |
| 390 | G8 | TRANSFER | yes: Thm 4 (limit identity only) | TRANSFER |
| 391 | G8 | TRANSFER | yes for the sign statement; **the G1 residue (elliptic lifting) is not REF-D** | TRANSFER + residue ≠ (D5) |
| 392 | G15 | NO | yes: Hölder–Ostrowski, B″ | NO |
| 393 | G8 | NO | yes: 𝓒_G Beurling-generic | NO |
| 394 | G1 | NO | yes: F2 | NO |
| 396 | G15 | NO | yes: K2 (inf s_φ = −∞) | NO |
| 398, 540 | G15 | TRANSFER | yes | TRANSFER |
| 399, 406 | G13 | TRANSFER | yes (weight factors, O_6-stable) | TRANSFER |
| 400 | G1 | TRANSFER | yes: O2 PROVED | TRANSFER |
| 403 | G17 | NO | yes: M1 (not real-stable) | NO |
| 404 | G13 | NO/TRANSFER | yes: P4 wrong orientation | NO + TRANSFER |
| 405 | G13 | NO | yes: 𝒦_mix | NO |
| 407 | G1 | NO/TRANSFER | yes: T3 contractive | NO + TRANSFER |
| 408, 469, 550 | G7 | TRANSFER | yes | TRANSFER |
| 415 | G8 | TRANSFER | yes for (G2); **the (G1) residue, approximate Chebyshev eigenkernels, is not REF-D** | TRANSFER + residue ≠ (D5) |
| 421, 528 | G17 | — (class theorem) | correct: not routes | — |
| 422, 429 | G12 | TRANSFER | yes | TRANSFER |
| 452, 453, 458, 463, 466, 468, 486, 581, 582 | G2 | TRANSFER | yes (R1; lem:shape-est(i)) | TRANSFER |
| 505 | G1 | NO | yes: passivity/small-gain, margin = W_T | NO |
| 514 | G15 | NO | it is the literal objective | NO (better: "= objective", not NO-GO; see note) |
| 516 | G2 | NO | yes: Q1/Q2 tautology | NO |
| 519, 520 | G3 | TRANSFER | yes (Prop C1.1) | TRANSFER |
| 521(a),(d) | G7 | TRANSFER | yes | TRANSFER |
| 536 N1 | G11 | NO | yes | NO |
| 538 | G5 | TRANSFER | yes, the index says "full sign at A_⊥⊥(1) = (★★)" | TRANSFER (debatable, D2) |
| 539 | G15 | NO (≠) | correct: grep false positive | ≠ (outside the inventory) |
| 544 | G7 | NO | yes: Lemma 13.1 | NO |
| 545, 546, 547 | G17 | NO | yes: Φ.13, hyperfinite, Łoś | NO |
| 553 | G15/G5 | NO/TRANSFER | yes | NO + TRANSFER |
| 554 | G15 | TRANSFER | yes: Prop 19.2 | TRANSFER |
| 555, 556, 557 | G6 | NO | yes: Thm 19.25, 21.15, HA, HB | NO |
| 558, 559 | G15 | NO | yes: Thm 3; Thm 3′ is ARGUED (not PROVED) | NO (559 with Thm 3′ ARGUED: mixed label) |
| 567 | G7 | NO | yes: M.1–M.2 | NO |
| 571 | G14 | TRANSFER | **insufficient citation**: the entry only states "branch-2 risk"; the direction is in "?" | UNEVALUATED → TRANSFER by FAMILIES_A's theorem G1 (free ℕ^× does not distinguish ζ from Beurling ⇒ branch 1) |
| 572, 573 | G14 | NO "see 574" | 573 = SPEC_201 B-V1 = same object as 574: correct. **572 (FAMILIES_B V1) is only correct if V1 of FAMILIES_B is the seed of B-V1**; TRACT_D does not verify this | NO (573); NO conditional on the identification (572) |
| 574 | G14 | NO | yes: monotone falsifier (R11) | NO |
| 577, 578 | G17 | NO / cites R12 | yes (C-pos PROVED; (iv) ARGUED) | NO |
| 588 | G2/G10 | TRANSFER | yes; the clause "becomes YES if rewritten as G10" falls with G10 (§2a) | TRANSFER |
| 589 | G11 | TRANSFER | yes | TRANSFER |

Note on l.514: "NO" is used to mean "the statement is the literal objective." Honest label: it is not a NO-GO, it
is an identity with the objective; for the count it is left as NO (contributes no route), but the index should not
read it as impossibility.

### 1.2 Five (plus one) debatable cases, argued

**D1. l.209 / l.427 (BARRIER_W W2: "R2 ⟺ μ_T(Λ) ≥ 0"; W3: crossing = codim 1).** Debatable in the reverse sense:
TRACT_D promoted it to YES; I treat it in §2(b). Here I only note that entry l.427 (omitted by the grep, §3) is the
one that **closes** G14: W1 (monotone index), W3 (vNW only excludes kernels of dim ≥ 2) are class theorems that
cover the D-only form.

**D2. l.538 (A_⊥⊥(1) ≻ 0 in bulk, gap 3.77, identical spectrum for μ = 5, 10, 15).** Candidate general theorem:
Szegő/Avram–Parter for generalized Toeplitz sequences: if A_⊥⊥(1) is asymptotically Toeplitz with explicit symbol
a(θ), its spectrum converges to the range of a. The missing hypothesis would be "a > 0," which is a property of
**a single fixed function**, not of a family of windows. Does it rise to YES? **No.** The index (l.538) says
literally "full sign at A_⊥⊥(1) = (★★)": the symbol contains the full comb and its positivity is that of 𝔞 on the
gauge complement. Moreover the μ-independent spectrum (NUMERICAL) is evidence of a limiting operator, not of
proved Toeplitz structure; and the part that is *not* Toeplitz (C_RR, In = (2,0,dim𝒢−2)) is the one that changes
inertia at c = 1. It remains TRANSFER, with a legitimate side question, non-sign: **"Is A_⊥⊥(1) a generalized
locally Toeplitz (GLT) sequence with explicit symbol?"** — tractable, but an affirmative answer only converts the
transfer into another transfer (positivity of the symbol).

**D3. l.296 (site independence: D ⟺ 𝖡 PSD over sites with ratios → 1; at primes Arch ≥ Near).** General theorem:
Schoenberg (PD functions via restrictions to dense discrete sets) — its hypothesis is PD itself. But there is
another general theorem that does **not** ask for sign: Kreĭn–Langer / extension of PD functions from an interval,
which states that the number of negative squares is stable under refinement. That gives "n₋ independent of the
site set" (analogous to L2_002: n₋ independent of k), not n₋ = 0. **Does not rise**: the non-sign part is already
PROVED in equivalent form (L2_002), and the remaining part is the sign. TRANSFER.

**D4. l.353 (D_∃c: ∀T ∃c > 0 with λ_A(T; cΛ) ≥ 0), weaker than D.** Candidate general theorem: implicit function
theorem / analytic perturbation in c around a c₀ where λ_A(T; c₀Λ) > 0 with a margin uniform in T. The missing
hypothesis would be **"there exists a common c₀ with margin"**, which is not D's sign at c = 1. It is the most
serious of the five cases. **Does not rise to YES** for two documented reasons: (i) at c = 0 the value is
λ_{∞,P}(T) < 0 for T ≥ 0.60 (cor:Tarch, AUDIT_203 l.589), so there is no trivially positive base point; (ii)
concavity in c (Danskin) only gives upper bounds (INVENT Thm 2.3), and the existence of a common c₀ is question
O4^ε, OPEN, whose content is again a positivity of the datum with comb cΛ. Moreover, even if proved, **D_∃c does
not imply D** (it is weaker) and there is no registered argument from c* to 1. It remains TRANSFER and **with no
input for D**. I mark it as "valid side objective, not a priority."

**D5. Non-sign residues inside REF-D entries: l.391 "G1 elliptic lifting OPEN" and l.415 "(G1) approximate
Chebyshev eigenkernels OPEN."** Both are questions whose general theorem (elliptic continuation of Weil
characters; Weyl sequences / pseudospectrum for V^*Ш = 2log|x|Ш) **does not ask for sign**. They are tractable
independently. But **they are not reformulations of D**: entry l.415 itself says that if the control is
identities + Cauchy–Schwarz it falls into N_018 (ARGUED), and l.391 that the free positivity ‖ω_+‖²_HS ≥ 0 does not
see the comb. Verdict: "≠ (tool without D input)"; they do not count as YES in the inventory and should not be
launched as constructors for row D without a statement saying what sign they would produce.

**D6. l.502 (KK.3: Φ decays at most polynomially; certification 15 < μ < 131) and l.451 ((B_μ) ⟺ leak coercivity
L_x(Ω)).** Both omitted by the grep (§3). L_x(Ω) is a Gårding-type inequality with a high-frequency remainder —
general theorem (Gårding, leak inequalities) with hypothesis "symbol ≥ 0 off-band," which the index reports *does*
hold ⪰ 0 (off-band compensators). The missing piece, however, is "Q ≥ … − U" with Q the full in-band form, where
the archimedean block is not positive definite (a(0) = −5.37): sign. TRANSFER. KK.3: "the KK.3 transfer is L′♯
rewritten with prolate calibration" (index). TRANSFER.

**Conclusion §1:** no NO/TRANSFER rises to YES with input for D. The verdicts are well cited except for l.571
(unevaluated, now closed by FAMILIES_A's theorem G1), l.572 (citation conditioned on an unverified identification)
and l.514/559 (mixed labels).

## 2. The 13 YES

### (a) G10 after L2_INTERLACE

**What was the original induction?** (l.140–145, 345–349, 367–376.) SPEC_A: induction in T through contacts
T_j = ½log n_j; step λ_A(T_j) > 0 ⇒ λ_A(T_{j+1}) > 0 **using exact identities only** on the 2ε collar where the new
atom is seen (lem:contA: the entry instant is empty). Induction variable: j (contacts). Induction step: lemma
L*_j(θ). Gap (θ): where log ℕ enters in ‖ℓ_e‖_{𝔄_j^{−1}}.

**Is it the same object as (L2)?** No. (L2) is a Schur complement S_{T,k} in a basis of equal blocks, with
k = number of blocks (L2_INTERLACE §1: k is not tied to the contacts). L*_j is a step between consecutive contact
windows, read by the full resolvent 𝔄_j^{−1} of the problem on P_{T_j}. They are distinct inductions. TRACT_D
identified them too quickly.

**Does it survive as a distinct induction with a live gap?** No, by three registered facts that TRACT_D does not
cite:

1. **The gap (θ) was already closed as a specification** (l.367, CA_R3_001, Prop Θ PROVED): the density/polar part
   cancels; ℤ enters only through d(ψ − u) on [1, n_{j+1}); Lemma C PROVED. And CA_R4_001 (l.369–376) executed the
   first step ½log5 → ½log7: **the quantity whose sign is needed** is the near-cancellation of
   Σ_{n=2..5} Λ(n)n^{−½}h*(t ∓ log n) (+ tail K₁) to precision ≲ 1.6·10⁻⁶ in the dual norm of the collar read by
   𝔄_j^{−1}. The coordinator noted that this expression is EI_001 Thm 1, whose sign content is C*_A / Lemma S. That
   is **a functional of the minimizer h*_j**: Theorem X / restriction 11 / 𝒦_H. TRACT_D's claim "single gap (θ),
   OPEN and ADMISSIBLE" describes the state of l.347 (earlier) and not that of l.367–380 (same day, later).
2. **The contact step transports nothing.** INV_U_001: U0 (no jump in λ), U5b (no jump in λ′), non-analytic germ
   of size v_n a_+a_− η/log(1/η); class 𝒦_cross NO-GO (ARGUED). All variation of λ_A between T_j and T_{j+1} occurs
   **inside the interval**, where the problem is a continuous flow in T — 𝒦_W (BARRIER_W) ∪ 𝒦_H. An induction "by
   contacts" whose step is trivial at the contact is an induction by continuation in T, which is the registered
   class.
3. **The round-R audit (l.380) did not withdraw ADMISSIBLE "merely by the word REF-D"**: it gave a class reason —
   "restricting how the proof is written is not a property of the object → does not satisfy (R)(11)" (fatal H1 for
   "mechanism"). TRACT_D §5 (and §4 G10) summarizes that line poorly.

On the doubly exponential scale: it is true that l.142's death by (γ) used the retracted scale; but l.345–346
redid (γ) with thm:margin (simple exponential) and the version with estimates fails again (ARGUED, not circular);
the identities-only version does not die by (γ) but by the three facts above.

**Verdict G10: TRANSFER** (the step L*_j is REF-D on the collar, its quantity is a functional of h*_j; the (L2)
version via interlacing is NO-GO by L2_INTERLACE). Affected entries: 142, 347, 367, 380 (+06_ l.181,
588-rewritten, 536-N3-via-R13). What remains of G10 that is neither interlacing nor 𝒦_H: **nothing with a
hypothesis other than the sign**. The only registered mechanism to decide the step in a concrete window is
certified enclosure (numerical as mechanism), which gives D up to a finite T, not D.

### (b) G14: spectral flow / Robbin–Salamon crossing forms

Precision: for a C¹ family of self-adjoint A(T) on **a fixed space**, the crossing form at T* is
Γ(T*)(v) = ⟨v, A′(T*)v⟩, v ∈ ker A(T*); a crossing is regular if Γ is nondegenerate, and the local spectral flow is
sign Γ (Robbin–Salamon 1995, CITED). Comparison:

- **lem:flowdet** (P47 l.8134): μ₁′ = ⟨A′φ₁, φ₁⟩ where μ₁ is simple. At a simple crossing μ₁(T*) = 0, φ₁ = v:
  **Γ(v) = μ₁′(T*)**. It is the same formula.
- **BARRIER_W_001 §5:** the only Λ-specific crossing datum is Σ v_n c_{h*}(log n), a functional of the minimizer;
  L2_INTERLACE (3.2) shows that in the finite basis the derivative jumps by −2v_nF(−T)F(T): an edge datum of the
  kernel vector = h*. Γ is that.
- **What Robbin–Salamon adds:** (i) treatment of degenerate crossings via the signature of Γ on a kernel of
  dimension > 1; (ii) homotopy invariance of the spectral flow and additivity under concatenation; (iii) the
  unbounded case with fixed domain. (i) is in BARRIER_W (Kreĭn signature, W3: kernels of dim ≥ 2 are codim ≥ 2 and
  generically do not occur); (ii) is W1 (monotone index, constancy = positivity = transfer, l.209); (iii)
  **does not apply as such**: here the space grows with T (P_T ⊂ P_{T′} by zero extension, lem:monoT), it is not a
  family on a fixed domain; the reduction to a fixed domain by rescaling produces the Hadamard derivative, which is
  again an edge datum of h*.
- **Additional, decisive defect:** TRACT_D formulates G14.2 as "Γ is positive definite at every crossing (the
  eigenvalues only cross upward)." **That is impossible**: by lem:monoT, T ↦ λ_A(T) is non-increasing; at a
  crossing of λ_A through 0 the derivative (when it exists) is ≤ 0, so Γ ≤ 0 in the direction of the window's
  kernel. The alternative "the kernel is never nontrivial" is statement D itself.

**Verdict G14: NO** (inside 𝒦_W: W1, W3, lem:flowdet; G14.2 refuted by lem:monoT). It is not a new tool; it is
exactly lem:flowdet + BARRIER_W §5. Corollary: TRACT_D §5(2)'s "quantitative version of non-crossing"
(det S ≥ c(T) via a lower bound on |Γ|) inherits the same fate: |Γ| is |Σ v_n c_{h*}(log n)| ≲ 10⁻⁷⁰ in the
direction of h* (L2_INTERLACE §3), 𝒦_H.

### (c) G4: does 𝔊_T invert 𝔞|P_T?

Yes. By P47's definition (thm:parityschur l.4176, prop:polarcap l.4316) as transcribed by POLAR_CAP_001 §1 and
index l.598: 𝔤_par = W_T(h_par), h_par = H₀ − (𝔞_T|𝒬^par)^{−1}𝔞_T(H₀,·). It is a bordered Schur complement that
contains (𝔞_T|𝒬^par)^{−1}; every use (Hadamard in T, Weyl–Kreĭn–Langer, non-crossing T6.2) consumes λ_A > 0 on the
primitive sector, and the additive inertia In(W_T) = In(𝔞_T|P_T) + In(𝔊_T) (thm:parityschur) separates the sign of
𝔊 from that of 𝔞 only *given* 𝔞|P_T ≻ 0. The Weyl function M(z) is Nevanlinna in the spectral parameter, but T is
not that parameter. KVB requires S ≥ 0 (l.507). **Verdict G4: TRANSFER** (and P156 already falsified in comb
models). Entries 507, 560 (Kreĭn), 209-boundary.

### (d) "L′♯ by Fredholm/Weyl + finite block, missing relative compactness"

Exact statement (TRACT_001 l.~102, TRACT_D §5(2.1)): if 𝔞_T − 𝔟_T is relatively compact with respect to
dist²(·, 𝒢̄_T) for a neighboring form 𝔟_T with no Λ and exact radical 𝒢̄_T, Weyl gives coercivity of 𝔞_T except on
a finite space; on the finite space positivity must be proved (with the κN^{−A₀} constant from L′♯).

Audit: **the relative compactness is not missing.** The arithmetic part of 𝔞_T on a finite window is a finite sum
(n < e^{2T}) of truncated translations, bounded operators on L²(I_T); the archimedean part has log order and
compact resolvent on L²(I_T) (class S5 of BARRIER_W). Everything bounded is relatively compact with respect to a
form with compact resolvent. Moreover the scheme is **already executed** in R186_025 Thm A/B + Cor (L1) PROVED:
c(T,k) = min 𝔞_T|𝒱_k > 0 for k sufficiently large (coercivity outside a space of dimension 2k − 2), and
λ_A(T) ≥ 0 ⟺ S_{T,k} ⪰ 0 (Haynsworth). The "finite block" **is** (L2). The missing hypothesis is the positivity of
the finite block = D in bulk (REF-D), not a compactness. For L′♯ there is also the uniformity of κN^{−A₀} in N,
restricted by thm:margin (A₀ ≳ 15.4/c), which is likewise not sign-free: it is the scale of the margin.

**Verdict (d): TRANSFER.** TRACT_D's claim "stronger than D with its own path" is false for this item.

### (e) G16 Lemma F

Without waiting for a new round, the definition is evaluated. Three registered gates (l.523): (i) A_ε does not
vanish on 𝒢̄_T (ARGUED) ⇒ F(ε) is not defined on the quotient 𝒬_μ; (ii) n^ε = moving the line to σ = ½ + ε, rule
"do not retry σ-derivatives in Mellin" (l.463) — the next round must declare the new reason; (iii) convexity
requires ⟨h_m, h_n⟩ ≥ 0, not automatic. The question that survives, "three lines with boundary (T10.2) after
projecting to the quotient," is harmonic analysis and its hypothesis (log-convexity of a mixed norm on a strip)
**is not the sign**, provided G16.0 produces a gauge-null A_ε without introducing the minimizer. If the gauge
correction Π_μ uses h* (as in LL_001, gauge Π), it falls into 𝒦_H. **Verdict: weakly conditional YES**, the only
survivor; gate G16.0.

### Summary §2

| TRACT_D YES | entries | audited verdict | reason |
|---|---|---|---|
| G10 induction by contacts | 142, 347, 367, 380, (06_181), 588-rewritten, 536-N3 | TRANSFER | (θ) closed and reduced to C*_A = functional of h*_j; U0/U5b; R(11) |
| G14 Robbin–Salamon | 209 | NO | = lem:flowdet + BARRIER_W W1/W3/§5; G14.2 refuted by lem:monoT |
| G4 polar capacity | 507, 560 | TRANSFER | 𝔊_T contains (𝔞_T|𝒬^par)^{−1} (POLAR_CAP_001) |
| G3 L′♯ Fredholm | 450 | TRANSFER | free compactness (S5; R186 Thm A/B); residue = (L2) |
| G16 Lemma F | 521(f), 523 | weakly conditional YES | gate G16.0 |

## 3. Grep omissions

grep for "tautolog|rewriting|equivalent|⟺" without TRACT_D's keywords over the index README. Entries that are
reformulations of D and do not appear in TRACT_D's table:

| l. | entry | D-only statement | TREATMENT |
|---|---|---|---|
| 148 | SPEC_B T*₂ correlated | (N) correlated Nyquist mesh ⟺ D (B8) | TRANSFER (= G8/G10-B8) |
| 178 | EI_003 Thm 2 "tautology" | σ_T affine in Λ; sign via h*(Λ) | TRANSFER (G9, Theorem X) |
| 247–248 | E front Thm 1 separability | D ⟺ positivity over Euler product vectors (positive = completely positive, PROVED) | TRANSFER (interlacing/Choi witnesses consume positivity; the entry itself records this) |
| 427 | BARRIER_W W2 | R2 ⟺ μ_T(Λ) ≥ 0 | NO for the index/non-crossing version (W1, W3); closes G14 |
| 451 | PROOF_L_SHARP_B (B_μ) | M+V ⪰ 0 ⟺ leak coercivity L_x(Ω) | TRANSFER (arch block not definite; D6) |
| 460 | PROOF_L_SHARP_P residual | (★★_P) = L′♯ | TRANSFER (G2/G3) |
| 502 | KK.3 | prolate transfer = L′♯ rewritten | TRANSFER (D6) |
| 504 | LL_001 (15) | (C_G)(b)_Π ⟺ 𝔔[σ] ≥ I(σ) | TRANSFER (CONDITIONAL; sign of I OPEN = form) |

Not reformulations (false candidates): l.211 (Δ_a ≡ 0 ⟺ FE), l.261 (cΛ at successors), l.552 (Cor B.3 = cor:Tarch,
reading). No omission is YES.

## 4. Final verdict of the corrected D inventory

Over the 90 TRACT_D entries:

| | TRACT_D | audited |
|---|---|---|
| NO | 31 | **32** (+209) |
| TRANSFER | 46 | **56** (+142, 347, 367, 380, 588, 536-N3, 507, 560, 450; 571 confirmed by FAMILIES_A's G1) |
| YES | 13 | **2** (521(f), 523: G16, weakly conditional) |

(06_ l.181 is not among the 90; it moves to TRANSFER together with G10.) Omissions: +8 entries, all TRANSFER/NO.
Non-sign residues outside the inventory: l.391 G1, l.415 G1, l.538 (GLT question) — tractable, with no declared D
input.

**Definitive YES list:**
1. **G16 (Lemma F), weakly conditional.** First lemma: **G16.0** — construct a gauge correction
   A_ε ↦ A_ε − Π_μ(·) **that does not use h*** such that A_ε ≡ 0 on 𝒢̄_T and F(ε) descends to 𝒬_μ; declare the new
   reason against l.463 (σ-derivatives in Mellin). Only if G16.0 succeeds: T10.1 (cheap falsification) and T10.2
   (three lines with boundary on the quotient).

There are no more. In particular: there exists today in the inventory no statement stronger than D with its own
path (the two TRACT_D §5(2) proposed both fall into (d) and (b)).

**First construction to launch: G16.0**, as it is the only YES, finite in scope (a question of gauge algebra: does
there exist a Λ-independent correction of A_ε that annihilates the radical?), and decisive both ways: if the only
possible correction goes through h*, G16 falls into 𝒦_H and the D inventory stays at YES = 0; if one exists without
h*, T10.2 is an interpolation problem with no Λ. Mandatory prompt: index rule + l.463 + l.523 + LL_001 (gauge Π) +
lem:transfer (must fail for F_DH and Epstein: state what feature of Λ is used by F(ε) that those forms lack).
Audit in parallel with the mandate to search for the h* hidden in Π_μ.

## 5. Methodological observations

- TRACT_D read the index by isolated lines; three of its five errors (G10, G4, G14) stem from citing an item's
  *opening* line rather than the later lines from the same day that close it (l.367–380 for G10; l.427 for G14;
  l.598/POLAR_CAP for G4).
- "Discarded by judgment alone" (38/90) overstates: several J's (142, 380) carry a class reason in adjoining lines.

## 6. Index entry

- **AUDIT_204_TRACT_D_001 (audit of TRACT_D_README_001):** YES 13 → 2. G10 (L*_j by contacts) ≠ (L2) but TRANSFER:
  (θ) closed and reduced to C*_A = functional of h*_j (l.367–376), U0/U5b, R(11); G14 Robbin–Salamon =
  lem:flowdet + BARRIER_W W1/W3, NO, and G14.2 ("Γ > 0 at crossings") refuted by lem:monoT; G4 TRANSFER (𝔊_T
  contains (𝔞|𝒬^par)^{−1}); L′♯ Fredholm+finite TRANSFER (free compactness, S5/R186 Thm A/B; residue = (L2)).
  Count: NO 32 · TRANSFER 56 · YES 2 (G16, conditional on G16.0); +8 omissions, all TRANSFER/NO. Do not retry
  G10/G14/G4/Fredholm as "YES." Row D OPEN.
