# SPEC_SIGN_OBJECT_004 — Round 9: non-linearity in θ, inertia, Fredholm index. Main candidate and Theorem M200′

Phase 200, round 9. No new numerics:
all cited numbers come from LEMMA_E_EPSTEIN_001, COSH_DEFECT_001, GRAM_INERTIA_001 (phase 199) and
CERT_FALSIFIERS (phase 197). No "closure" is proposed: the output is a candidate developed up to its first exact lemma
and an extended barrier theorem with the list of what remains.

## Summary (≤300 words)

The five canonical non-linear quantities over the families of forms are classified (θ of Euler, t cosh, c of cΛ).
(N1) λ_A^{(θ)} is concave but evaluated at ζ it is the target: **REF-D**. (N2) functionals of g*_θ: **Theorem X / restriction 11**.
(N3) det/inertia in block: the inertia of ζ is D in block (**REF-D**, already indexed: BARRIER_W_001, GRAM_INERTIA_001); the
inertia of Epstein ≥ 1 only by certificate, and the Sylvester–Weyl bounds n₋(X+Y) ≤ n₋(X)+n₋(Y) give **empty**
inequalities because 𝒬_g is indefinite in g. (N4) t₀(T) is a property of the pair (ζ_K, L_ψ): **blind to ζ**. (N5) squares/tensors:
product ↔ convolution only via exponential characters = symbol channel (i) of 𝒦_200, or the EL identity of BB_001
(**comb-generic**).
**New structural fact (PROVED given CITED):** ζ is an *isolated* point for every Euler/cosh family with gamma factor
Γ_ℝ(s), conductor 1 and simple pole at 1 (degree-1 rigidity, Kaczorowski–Perelli): every family non-linear in θ passing through ζ
is constant. The Fredholm index of multiplying by y or by L_ψ/ζ_K is, by the argument principle, a zero count
(zero side) and for ζ it is identically 0 (y ≡ 0): **sees only the non-Euler cases**. NO-GO as a sign object.
**Surviving main candidate:** the *jump index of the pencil in c*, n₋(A_M(c)) with A_M(c) = A_M(1) + (1−c)C_M in block.
By the Haynsworth inertia formula (CITED) one proves (Lemma I.1, PROVED) In A_M(c) = In((1−c)C|_R) + In(Schur), with R the
gauge radical in the block: the only Λ-exact entry is the existence of R at c = 1 (Guo L4.4 = channel (β)). The jump is exact and
integer, but the sign part is the form on the quotient: **REF-D**. **Theorem M200′** is stated (class 𝒦_200 ∪ 𝒦_NL,
ARGUED; pieces PROVED) and the list of four live residues. Ranking: (R1) quantify the jump in c at the escape scale >
(R2) degree-2 family through ζ² > (R3) t₀(T) as calibration.

## 0. Index and corpus check

Grep on `05-meta-and-planning/ROUTES-TRIED-INDEX/README.md` for "inercia", "inertia", "n₋", "Fredholm", "índice", "Sylvester",
"determinante", "tensor", "Hankel", "Morse", "Kreĭn", "spectral flow", "Toeplitz", "argumento":

- **l.39 (Fredholm / determinants / W-det / Birman–Schwinger)** and **l.50 (pencil/inertia, walls W-lin, W-det, W-fam)**: closed
  families. N3 as formulated (det of the Gram of ζ in block, inertia of ζ) is W-det/W-fam: not retried. New reason
  written only for §2: the object there is not det/inertia of ζ, but the *difference* of inertias between ζ and a point of a
  Euler family, and whether that difference is a Fredholm index is measured. The result is NO-GO for a cause different from W-det
  (isolation of ζ + argument principle), and it is recorded.
- **l.424 BARRIER_W_001 (𝒦_W: Morse, spectral flow, Kreĭn signature, non-crossing, homotopies in T and in combs)**: W1 PROVED
  n₋ non-decreasing, W2 R2 ⟺ μ_T(Λ) ≥ 0. The candidate in §3 (pencil in c) is a homotopy in combs: it formally falls in 𝒦_W.
  New reason: there the homotopy was not decomposed by the radical; here the Haynsworth formula *exactly* separates the jump
  contributed by the gauge radical (the only Λ-exact entry per R-Z1/M200) from the rest. The goal is to locate where Λ lives, not
  to retry monotonicity of the index.
- **l.481 GRAM_INERTIA_001**: "do not retry deciding the sign by inertia of the lattice Gram". It is respected: here the
  inertia does not decide sign; the published datum is used (inertia (10,0,1), null vector μ⊕1 at Mori μ=15) as a test of Lemma I.1.
- **l.507 PROOF_L_SHARP_OO_001** (KVB/Kreĭn/restricted index, hypothesis S ≥ 0 = REF-D): §3 reaches the same boundary and
  declares it.
- **l.428 / Theorem X / restriction 11 (AUDIT_CONSTRAINTS_001)**: decides N2.
- **COSH_DEFECT_001** (round 8): restriction C-θ; Lemma N_θ. This memo answers N_θ.
- **BB_001 (l.434)**: EL identity with 2(a⋆a)(N)/√N, comb-generic: decides N5.
- **META_200_BARRIER_001 (l.528)**: class 𝒦_200 and channels (i)–(iv); §5 extends it.
- **SPEC_SIGN_OBJECT_003 C2 (index of D_μ)**: partial NO-GO (D_μ invariant under a_P). The Toeplitz index of §2 is a
  relative: the reason why the quotient L_ψ/ζ_K does not escape that wall (it only sees the difference of two Euler products) is added.

None of the above is retried without the reason written on its line.

## 1. Task A — Table N1–N5

Notation: A_M^{(θ)} ∈ Sym_M(ℝ) the Gram matrix of 𝔞^{L_θ} in a fixed basis {g_1,…,g_M} of P_T (affine in θ, Theorem S(ii));
A_M(t) that of 𝔞^{Z_t} (even polynomial in t, Theorem S(i),(iii)); A_M(c) that of 𝔞^{ζ^c} = arch + pole − c·comb (affine in c).

| | Quantity | Non-linear in the parameter | Does it pass through ζ with the parameter live? | Verdict | Label |
|---|---|---|---|---|---|
| N1 | λ_A^{(θ)}(T) = λ_min(A^{(θ)}) in the limit M→∞ | concave in θ, t (infimum of affine/polynomial functions) | only via c (ζ^c), not via θ, t | evaluated at ζ it is the target; concavity only favors the extremes if the sign at them is known | **REF-D** (PROVED as classification) |
| N2 | Φ(g*_θ): values of the form or the comb at the minimizer | yes | yes (c) | every first-order discriminant is a functional of h*, not of σ | **NO-GO** via Theorem X / restriction 11 |
| N3 | det A_M^{(·)}, inertia n₋(A_M^{(·)}) | det: degree-M polynomial; n₋: integer | inertia of ζ at c = 1 | inertia of ζ = 0 ∀M is D in block; inertia of Epstein ≥ 1 only by certificate, not by counting; difference of inertias bounded by Weyl in an empty way | **REF-D** for ζ; **empty** for the difference (PROVED, §1.3) |
| N4 | t₀(T) = sup{t : λ_A^{Z_t} ≥ 0 on [0,t]} | yes | no: the cosh family through ζ is trivial | property of the pair (ζ_K, L_ψ) | **blind to ζ** (PROVED given Prop 2.1); useful only as calibration |
| N5 | 𝔞^{(θ₁)}·𝔞^{(θ₂)}, four-point forms, 𝔞∘(quadratic operator) | yes (degree 2) | yes | product c(log m)c(log n) ↔ convolution c(log mn) only for exponential c: symbol channel (i); in general comb-generic EL identity | **comb-generic** (ARGUED, §1.5) |

### 1.1 N1
λ_A^{(θ)} = inf_g (affine in θ) is concave: PROVED (COSH_DEFECT §9). On the Euler segment (ζ_K, L_ψ) ζ does not appear. On the pencil
c, λ_A(c) is concave in c and λ_A(1) = λ_A^ζ(T); any statement "λ_A(1) ≥ 0" is the target. Concavity only transports
sign from two known points toward the interior; the only "known" point with sign on the pencil c is c = 0 (archimedean + pole,
sign not defined: m < 0 for |t| < 6.29, SPEC_002 T.1). REF-D.

### 1.2 N2
Restriction 11 + Theorem X: any Φ(g*_θ) is first order in the comb through h* = g*∗g̃*; it does not see σ (the fluctuation
part of the comb) separately from h*. Recorded without new development. NO-GO.

### 1.3 N3 — inertia: what there is and what there isn't
(a) n₋(A_M(c=1)) = 0 ∀M ⟺ λ_A^ζ(T) ≥ 0 (M → ∞ step by density of bases in P_T, standard PROVED): REF-D.
(b) For Epstein Z_Q, n₋(A_M^Q) ≥ 1 for large M and T ≥ 1.59: PROVED, but **by interval certificate**
(λ_A^Q(8/5) ∈ [−0.06194, −0.06194], LEMMA_E §3), not by counting.
(c) **Inertia inequalities (PROVED, Weyl/Sylvester, CITED as linear algebra):** from 𝔞^Q = M̄ + 𝔇, M̄ = ½(𝔞^K+𝔞^ψ),
𝔇 = −𝒬 − R₄ (all quadratic forms in g), n₋(𝔞^Q) ≤ n₋(M̄) + n₋(𝔇) and n₋(M̄) ≥ n₋(𝔞^Q) − n₋(𝔇).
Since 𝔇 is indefinite in g with a numerical range nearly symmetric ([−4.03, 4.02] at T = 1.6, NUMERICAL, COSH_DEFECT §2b) and its
negative inertia in the block grows with M (modulation scheme, COSH_DEFECT §2b: it is a Hankel matrix in u·c_g(u) with alternating
signs in high harmonics), n₋(𝔇) ≥ n₋(𝔞^Q) for large M: the lower bound is ≤ 0, **empty**. For ζ, 𝔇 ≡ 0 and the bound
says n₋(ζ) = n₋(ζ). Conclusion: Sylvester/Weyl do not convert the Epstein failure into information about the Euler extremes
or about ζ.
(d) det A_M^{(θ)} is a polynomial of degree ≤ M in θ; its roots are the θ where the inertia changes. There is no reason (nor
written mechanism) for them to be at ±1: the integer divisor (C-int) is on the zero side and does not fix roots of the window
determinant. OPEN without an object; not pursued.

### 1.4 N4
See Prop 2.1: there is no non-trivial cosh family through ζ with degree-1 data. t₀(T) is a constant of the pair (ζ_K, L_ψ) (at the
witness g_E the crossing is t* ≈ 0.991, COSH_DEFECT §3.3; the infimum is not computed). It serves as a **calibrator** of any
C-E-type object (it must predict t₀ < 1 for the Epstein pair), not as a source of sign for ζ.

### 1.5 N5 — four-point forms
The question: is there an exact identity for 𝔞(g)² or for 𝔞∘(quadratic operator) that makes Λ∗Λ or Λ_cosh appear with sign?
(a) 𝔞(g)² ≥ 0 trivially; it contains no sign information about 𝔞.
(b) 𝔞(g)𝔞(g′) contains Σ_{m,n} Λ(m)Λ(n)(mn)^{−½}c_g(log m)c_{g′}(log n); Λ∗Λ appears when this is rewritten as
Σ_N (Λ∗Λ)(N) N^{−½} c(log N), which requires c_g(x)c_{g′}(y) = c(x+y): only if c is exponential e^{−σx}. That is the Dirichlet
series in real σ, i.e. the symbol channel (i) of 𝒦_200 (or, with σ = ½+it, the symbol on the line).
(c) With a generic quadratic operator Γ: g ↦ G(g) ∈ P_{2T} such that c_{G(g)}(log N) = Σ_{mn=N} c_g(log m)c_g(log n)/…
(Dirichlet convolution of the values of c_g over log ℕ), the identity 𝔞^{(2T)}(G(g)) = ⟨Λ, c_g⋆c_g⟩ is linear in Λ:
to get Λ∗Λ one must use the Leibniz rule (Λ = log·μ∗... ), which is the EL identity of BB_001
(2(a⋆a)(N)/√N), comb-generic: it holds for any comb a with its own formal logarithm.
(d) What *is* specific: 𝒬_g[b] of COSH_DEFECT *is* a four-point form in (g,g;b,b) with multiplicative kernel
w_g(mn); but b ≡ 0 for ζ. Verdict: comb-generic (b),(c) or blind to ζ (d). ARGUED (the exhaustiveness of (b)–(c) is not a
class theorem).

## 2. ζ is isolated: the Fredholm index sees only the non-Euler cases

**Proposition 2.1 (isolation of ζ among degree-1 Euler families; PROVED given CITED).** Let L be an Euler product of the
Selberg class with gamma factor Γ_ℝ(s), conductor 1 and simple pole at s = 1. Then L = ζ (Kaczorowski–Perelli, degree 1,
CITED; Conrey–Ghosh for the weak form). Consequently, for every pair (L₁, L₂) of Euler products with that data, b ≡ 0,
and the families L_θ, Z_t of COSH_DEFECT are constant ≡ ζ. Every non-linear quantity in θ or t evaluated on a family that passes
through ζ with fixed data is the quantity of ζ itself (REF-D) or trivial.

*Proof.* Immediate from the CITED classification and the definition b = ½(ℓ₂ − ℓ₁). ∎

Comment: Epstein lives in data (Γ_ℂ, conductor 20), where there are two distinct Euler products; the "θ direction" exists
because the degree is 2. For ζ there is only the c direction (ζ^c), which is not an integer Euler product except for c ∈ ℕ (C-int), and the
family ζ^c passes through ζ² at c = 2 (which does not have the same data). This motivates residue R2 of §6.

**Proposition 2.2 (Toeplitz index of the quotient; PROVED as identification, NO-GO as sign object).** Let
φ = L_ψ/ζ_K (or e^{2y}) restricted to the boundary ∂R of a rectangle R = {½ ≤ σ ≤ 2, |t| ≤ τ} (or, with FE, to the symmetric
boundary). If φ does not vanish on ∂R, the Toeplitz operator T_φ on H²(∂R) is Fredholm with ind T_φ = −wind(φ, ∂R) (Gohberg–Kreĭn, CITED) and
by the argument principle wind(φ, ∂R) = N_{L_ψ}(R) − N_{ζ_K}(R) (difference of zeros counted in R, CITED). Therefore:
(i) the index is a **zero count**: zero side, not window side; (ii) for the pair (ζ, ζ), φ ≡ 1 and ind ≡ 0 for every R;
(iii) the multiplication operator by y is T_y with y holomorphic for σ > ½ except for branches at zeros; its index is not defined without
cuts, and for ζ it is the null operator.
*Verdict:* the index "sees" the non-Euler cases insofar as two distinct Euler products have different zero distributions; it does not see ζ and says nothing about windows. By the same argument the quotient with a falsifier (L = ζ·exp(εy)) gives an index
equal to the difference of zeros, which has no prescribed sign. **NO-GO** (zero side + blindness to ζ). The question "is the difference
of inertias between ζ and a falsifier a Fredholm index?" has an answer: only in the sense of Prop 2.2, where the index
counts zeros in rectangles, not window inertias; there is no known identity (nor one plausible by degree) between n₋(A_M) and
N_L(R) − N_ζ(R). OPEN as an identity, without a mechanism.

## 3. Task B — Main candidate: the jump index of the pencil in c

What survives of N3 is the only non-trivial family passing through ζ with fixed data: the pencil c ↦ 𝔞^{ζ^c} (comb cΛ). It is a
homotopy in combs (𝒦_W), but it is decomposed by the radical, which is the only place where M200 locates exact Λ.

### 3.1 Definition
Fix T and the block B_M = span{g_1,…,g_M} ⊂ carrier (P_T, or its exterior version L²(λ,∞) with gauge radical 𝒢_T, Paper 46 /
SPEC_003 A.1). Let A_M(c) = A_M^{arch+pole} − c·C_M, with C_M the Gram matrix of the comb Λ. Let R_M := B_M ∩ 𝒢̄_T be the visible gauge
radical in the block. By Guo L4.4 (CITED), A_M(1)|_{R_M} = 0 and A_M(1)(R_M, B_M) = 0. Definition:

  **ι_M(c) := n₋(A_M(c)) − n₋(A_M(1))** (jump index, integer, c in a neighborhood of 1).

### 3.2 Lemma I.1 (PROVED; Haynsworth, CITED)
Decompose B_M = R_M ⊕ R_M^{⊥}. For c ≠ 1 close to 1 with (1−c)C_RR invertible:
In A_M(c) = In((1−c)C_RR) + In(S_M(c)), S_M(c) = A_{⊥⊥}(c) − (1−c)² C_{⊥R}C_RR^{−1}C_{R⊥}.
At c = 1: In A_M(1) = (0, 0, dim R_M) + In(A_{⊥⊥}(1)).
*Proof.* Haynsworth inertia formula for Schur complementation over the RR block, using A_RR(c) = (1−c)C_RR and
A_R⊥(c) = (1−c)C_R⊥ (both because the archimedean+pole term and the comb Λ cancel exactly on the radical at c = 1, Guo L4.4).
∎
**Corollary I.2.** For c → 1: ι_M(c) = n₋((1−c)C_RR) + [n₋(A_{⊥⊥}(c)+O((1−c)²)) − n₋(A_{⊥⊥}(1))]. If A_{⊥⊥}(1) is non-
degenerate, the bracket is 0 for c near 1 and **ι_M(c) = n₋(sign(1−c)·C_RR)**: the jump is an exact count given by the
signature of the comb Λ restricted to the gauge radical.

### 3.3 Where exact Λ enters
Only in the *existence* of R_M (inclusion 𝒢̄_T ⊂ rad 𝒲, Guo L4.4). For a_P, Beurling, DH there is no radical (their form does not annihilate
𝒢_T): Lemma I.1 does not apply and the jump is not defined as a count. This is exactly channel (β) of M200 — dead as
quantitative stability (GUO_QUANT_001) but here used *qualitatively* (existence), which is not the same thing.

### 3.4 Target theorem and why it is REF-D
The theorem that would give D in block would be: n₋(A_{⊥⊥}(1)) = 0, i.e. positivity of the induced form on the complement of the
radical = form on the quotient 𝒬_μ. It is literally 𝒲 ≥ 0 on 𝒬_μ: **REF-D** (M200, branch 2). The jump ι_M contributes
information **only about C_RR** (signature of the comb on the radical), which is independent of the sought sign. Moreover C_RR is
computed by the radical itself: if v ∈ 𝒢_T, A(1)[v] = 0 ⇒ C[v] = A^{arch+pole}[v]: the signature of C_RR is the signature of the
archimedean+pole term on the gauge — an **archimedean** datum (restriction R-Π: projectors with kernel 𝒢̄_T are blind to the
comb). It falls into channel (iii) of 𝒦_200.

### 3.5 Battery filter
| Falsifier | Radical? | ι_M | Result |
|---|---|---|---|
| Epstein Z_Q (h=2) | Z_Q is not Euler: gauge ⊄ radical (C-Guo) | undefined | the candidate does not distinguish it by a count; it excludes it by absence of structure |
| a_P | no | undefined | same |
| cΛ, c ≠ 1 | the pencil *is* cΛ; radical only at c = 1 | n₋(sign(1−c)C_RR) | separates c = 1 from c ≠ 1 only if C_RR is definite (then one side) or indefinite (both sides): consistent with CERT_FALSIFIERS (c → 1 CONDITIONAL on κ_T ≠ 0) |
| DH | no (not Euler) | undefined | same |
| Beurling 𝒫 | gauge radical with Beurling Möbius: yes, if 𝒫 has ζ_𝒫 with FE (not in general) | depends | comb-generic in the FE subclass |

Honest reading: the candidate "separates" the battery by the existence of the radical (identification, like C-int), not by sign.

### 3.6 Tests
**Mori μ = 15 (GRAM_INERTIA_001, published NUMERICAL):** with φ₀, inertia (10,0,1) and null vector = μ⊕1. Lemma I.1 predicts
dim R_M = 1 and n₋(A_{⊥⊥}(1)) = 0 in that block: consistent (not a proof: it is the datum). ι_M(c) = n₋(sign(1−c)·C[μ⊕1]):
a single side of c = 1 gains a negative eigenvalue; the side is given by the sign of C[μ⊕1] = A^{arch+pole}[μ⊕1] (computable; OPEN
as a number, not recomputed here). Consistent with "cΛ falsifies on one side" (phase 197).
**Lemma E (T = 8/5):** Z_Q has no gauge radical; In A_M^Q has n₋ ≥ 1 (certificate). The candidate says nothing about g_E
except "no jump is defined". No sign test is possible: the candidate does not pronounce on Epstein by counting.

### 3.7 First exact lemma (OPEN, decidable)
**Lemma I.3 (signature of the comb on the radical).** *At the exterior carrier at level μ, with R_μ = 𝒢̄_T ∩ B_M, compute
In(C_RR) as a function of M and μ, and decide whether A_{⊥⊥}(1) is non-degenerate (hypothesis of Cor I.2).* If C_RR is
definite, ι signals a single side and c = 1 is the boundary of the positivity interval of the pencil; then the question of D in block
reduces to the distance, along the pencil, between c = 1 and the next root of det A_{⊥⊥}(c) — a problem of *spectral gap of the pencil
in the quotient*, which is the (β)+escape-scale residue of M200 in another coordinate. Risk: high; the last step again becomes
the form on the quotient.

### 3.8 Risk and verdict
The jump index is an exact integer count with Λ inside (via the radical), which satisfies the letter of C-θ (non-linear: it is a
step function of c, discontinuous at c = 1) and that of "count output". But the count is of C_RR, which is archimedean by
R-Π, and the sign sought is the positivity of the Schur complement: **NO-GO as sign object (PROVED: Lemma I.1 + R-Π + M200
branch 2), survivor as coordinate** (the reduction of Cor I.2 to a pencil gap in the quotient is new as a formulation,
ARGUED as not-a-retry).

## 4. Task C — Theorem M200′

### 4.1 Class 𝒦_NL
A method 𝔐 ∈ 𝒦_NL if its conclusion is Φ(F) with F a family of window forms {𝔞^{(p)}}_{p∈P} (P = θ Euler, t cosh, c
comb, or products thereof), affine or polynomial in p (Theorem S), and Φ is one of: infimum/λ_min, det/cofactors of the Gram in block,
inertia/jump index, roots of the determinant (generalized eigenvalues of the pencil), functionals of the minimizer, products
and four-point forms of family members, Fredholm/Toeplitz indices of quotients of family members.

### 4.2 Statement
**Theorem M200′.** Let 𝔐 ∈ 𝒦_200 ∪ 𝒦_NL with a conclusion uniform in T. Then exactly one of the following holds:
1. **comb-generic**: the conclusion holds for a falsifier from the battery {a_P, cΛ (c≠1), Beurling, DH, Epstein} (branch 1 of M200;
   N5);
2. **REF-D**: Φ evaluated at ζ is λ_A^ζ(T) ≥ 0 or 𝒲 ≥ 0 on 𝒬_μ (N1, N3(a), §3.4);
3. **Theorem X**: Φ is a functional of the minimizer h* (N2);
4. **blind to ζ**: the family is constant through ζ (Prop 2.1) or the index is a zero count that is null at ζ (Prop 2.2) (N4, index
   of quotients);
5. **identification without sign**: Φ separates the battery by existence of structure (radical, integer divisor C-int) without
   an inequality (§3.5).

**Labels.** PROVED: Prop 2.1 (given Kaczorowski–Perelli CITED), Prop 2.2 (given Gohberg–Kreĭn and the argument principle
CITED), Lemma I.1 (given Haynsworth, Guo L4.4 CITED), N3(c) (Weyl), N1 (concavity). ARGUED: exhaustiveness of the list of Φ in
𝒦_NL (it is not a class theorem: an arbitrary non-linear Φ in the Gram entries is not covered), N5(b)–(c), and piece (i)
inherited from M200. Therefore **M200′ is ARGUED as a class, PROVED piece by piece**.

### 4.3 What remains (exact list, no "closure")
Outside 𝒦_200 ∪ 𝒦_NL:
- **Q1 (pencil gap in the quotient).** Distance from c = 1 to the next root of det A_{⊥⊥}(c) in the quotient 𝒬_μ, with constants,
  at the escape scale (Cor I.2/Lemma I.3). Coincides with (β)+scale of M200 in another coordinate. OPEN.
- **Q2 (degree 2 through ζ²).** Degree-2 Euler families, conductor 1, factor Γ_ℝ(s)² with double pole: ζ² is the candidate; is there
  another Euler product (Eisenstein-type with the same gamma) giving a non-trivial θ direction whose extreme is ζ²? If it exists, the
  form of ζ² is the extreme of a Euler segment and C-θ could be proved in a case where the extreme contains ζ. By rigidity
  (Kaczorowski–Perelli in degree 2, partially CITED) the expected answer is no; deciding it closes or opens the direction. OPEN.
- **Q3 (non-structural non-linear Φ).** Non-linear functionals of the Gram matrix that are not spectral (e.g. Schur norms of
  entries, positivity of principal minors selected by index arithmetic m ≈ kn — semiring principle).
  No object written. OPEN.
- **Q4 (boundary channel and Tate)** inherited from M200 (W* ≈ J²(ξ′/ξ)(1)/2, coupled Tate mode). OPEN.

## 5. Task D — Ranking and recommendation

1. **Q1 / Lemma I.3** (pencil gap in the quotient). The only point where an exact count with Λ inside (radical) attaches to a
   continuous quantity (gap). First decidable step: In(C_RR) at Mori μ = 15 and non-degeneracy of A_{⊥⊥}(1) (reusable
   datum from GRAM_INERTIA_001). Risk: REF-D at the last step; value: it localizes the sign to a single direction of the pencil.
2. **Q2** (ζ² in degree 2). Classification question, cheap with literature (Kaczorowski–Perelli degree 2; Selberg class
   with double pole). If the answer is "only ζ²", it upgrades M200′ branch 4 to PROVED in degree ≤ 2.
3. **N4 / t₀(T)** only as a mandatory calibrator of any C-E-type object (it must reproduce t* ≈ 0.991 at g_E and t₀ < 1).
4. Q3: no object; keep in the crossword as an empty cell, do not advance constructions without a concrete arithmetic seed.

Recommendation: proceed with round 10 with a construction on Lemma I.3 (Mori block μ = 15, dimension-1 radical) and an
audit with the mandate "show that In(C_RR) is archimedean (R-Π) and that the pencil gap is 𝒲 in the quotient"; in parallel, a
literature review for Q2. Not retried: inertia of ζ in block, Sylvester/Weyl over 𝔞^Q = M̄ + 𝔇, Toeplitz indices
of L-function quotients, squares of the form.

## 6. Entry for the index

- **SPEC_SIGN_OBJECT_004 (phase 200, round 9, synthesizer):** table N1–N5: λ_A^{(θ)} REF-D; functionals of g*_θ Theorem X;
  inertia of ζ in block REF-D, difference of inertias Epstein/Euler by Sylvester–Weyl EMPTY (𝒬_g indefinite in g); t₀(T) blind to
  ζ; squares/four-point forms comb-generic (product ↔ convolution only via exponentials = symbol channel, or EL of BB_001).
  **Prop 2.1 PROVED (given K–P CITED): ζ isolated among degree-1 Euler families ⇒ θ/t families through ζ constant.** **Prop 2.2:
  Toeplitz index of L_ψ/ζ_K = difference of zero counts (zero side, null at ζ): NO-GO.** Jump index candidate
  of the pencil in c: Lemma I.1 PROVED (Haynsworth + Guo L4.4): jump = n₋(sign(1−c)C_RR), C_RR archimedean by R-Π; sign = form in
  the quotient = REF-D. Theorem M200′ (𝒦_200 ∪ 𝒦_NL) ARGUED as a class, pieces PROVED. Residues Q1 (pencil gap in the quotient,
  Lemma I.3), Q2 (ζ² in degree 2), Q3, Q4. Not to be retried: inertia/Fredholm index as a sign count, Sylvester over the
  cosh defect, indices of L-function quotients. Row D OPEN.
