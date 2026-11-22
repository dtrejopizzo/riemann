# LEMMA_I3_001 — Lemma I.3: comb signature on the gauge radical and non-degeneracy of the quotient (phase 200, round 10, Q1)

**Data and scripts:** `LEMMA_I3_001_data/`.
- `lemma_i3.py`: full gauge ⊕ complement block.
- `analyse_i3.py`: inertias, Schur and pencil.
- `gauge_K.py`: P2's `gauge_defect.py` script with renamed output, for stability in K.
- Outputs: `block_mu{5,10,15}_J8.npz`, `analysis_i3.json`, `blk*.log`, `gK*.log`, `sens/`.

**Index and corpus check.** I grepped `ROUTES-TRIED-INDEX/` for "gauge module", "C_RR", "quotient/cociente", "Schur·gauge".
Only SPEC_004 (Lemma I.1, I.3 OPEN) and C1_DUPLICATION (generic Schur complement, no new reason) appear.
The object of this memo, the comb modulo gauge Q/C_RR on the pencil cΛ, does not appear in the index.
The new reason relative to C1 is that here the RR block is exactly the radical. Hence the congruence that separates it
does not depend on c (§4), and that was not present in C1.

## Summary (≤250 words)

(1) **Exact framework.** Guo L4.4 is cited (gauge ⊂ radical of 𝒲_Λ, CITED).
- PROVED: A_RR(c) = (1−c)C and A_R⊥(c) = (1−c)B, with C = Q|_𝒢 and B = Q_⊥R.
- NUMERICAL: A_R⊥(1) vanishes to within 10⁻³ relative (≤ 9·10⁻⁴ absolute against 0.91).
- PROVED: there exists a congruence L **independent of c** such that A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)·Q/C)]L.
  The Schur complement is **affine** in c and there are no O(ε²) terms.
- Correction to SPEC_004: the factor is (1−c), not (1−c)².

(2) **In(C_RR) = (2, 0, dim𝒢−2)**, NUMERICAL for dim𝒢 = 5, 7, 9, and PROVED independent of μ.
- C_RR is **not** definite and is **not** purely archimedean: C = (arch + 2AB)|_𝒢.
- arch|_𝒢 alone has inertia (3, 0, 6).
- The jump at c = 1 goes from n₋ = 2 to n₋ = 7. It is not a jump in dim𝒢.

(3) **A_⊥⊥(1) ≻ 0** on the block, with gap O(1). The minimum eigenvalue is 3.77 in the quotient's L² metric.
- There is no eigenvalue at scale e^{−4πμ}.
- **The block is translation-invariant (PROVED)**, so it does not depend on μ.
- Mori's (10,0,1) near-null vector, μ⊕1, **is not the gauge**: it is a 33-digit cancellation in the Möbius lattice, in a
  different coordinate. The requested identification is false.

(4) The comb modulo gauge Q/C is **indefinite**, with inertia (7,0,1). On the minimal mode of A_⊥⊥(1), uᵀ(Q/C)u = −7.34 < 0.
- The conjecture "≽ 0 on the near-kernel" is **false** (NUMERICAL).
- Its premise, monotonicity in c, requires Q ≽ 0, but In Q = (9,0,8).

**Verdict Q1:** I.3 closes as **NO-GO as a sign object**. What remains is an exact coordinate (affine congruence) that
transfers all the sign to A_⊥⊥(1) = (★★). That is REF-D in block form.

---

## 0. Conventions

T = ½log μ, λ = √μ. Definitions are those of Paper 46 def:ext / prop:ext-gauge / eq:W, in the form used in P2 §1.
- Complete form on the line: 𝒲_a[Ψ] = (1/2π)∫m|Ψ̂|² − Σ_n v_n^{(a)} c_Ψ(log n) + 2A(Ψ)B(Ψ), with v_n = 2Λ(n)/√n.
- Pencil in c: A(c) := P − cQ, with P = arch + pol (the (1/2π)∫m|·|² part plus the polar term 2AB) and Q = comb_Λ
  (Σ v_n c(log n), symmetrized bilinear form).
- Finite block V_M = 𝒢_M ⊕ W_J.
  - 𝒢_M is P2's discretized gauge, raw basis x²(1−x²)³x^{2k}, ∫φ = 0, orthonormal in L²(−1/λ,1/λ), dim 9.
  - W_J = span{Ψ_j}, with Ψ_j(x) = (1−y²)⁴P_j(y), y = (x+T)/r, r = 3, j = 0…7. These are compactly supported functions
    on the line, centered at the edge −T of the tails' support.
  - W_J is **not** L² orthogonal to 𝒢_M. Haynsworth only needs a direct sum. To measure sizes in the quotient I use
    the quotient L² metric G_⊥⊥ − G_⊥R G_RR⁻¹ G_R⊥.

Declared deviation. Mori's block/GRAM_INERTIA (Möbius line basis ρ_m plus φ̂₀ on the outer ω grid) does not
contain an explicit gauge. Hence it cannot be written as 𝒢 ⊕ ⊥. I reuse P2's gauge and pipeline, as the task requires,
and add the complement W_J. The comparison with Mori is made in §3.3.

## 1. Exact framework (task 1)

### 1.1 Lemma I.3-a (PROVED given Guo L4.4, CITED)
Let R = 𝒢_M be a subspace of the radical of the complete form 𝒲_Λ = P − Q. Write C := Q_RR and B := Q_⊥R. Then:
(i) P_RR = Q_RR and P_R⊥ = Q_R⊥.
(ii) A_RR(c) = (1−c)C, A_R⊥(c) = (1−c)Bᵀ and A_⊥⊥(c) = A_⊥⊥(1) + (1−c)Q_⊥⊥.
(iii) A(1) = 0_R ⊕ A_⊥⊥(1), and A_⊥⊥(1) is the form 𝒲_Λ on the quotient V_M/𝒢_M, i.e. (★★) in block form.

*Proof.* Guo L4.4 / prop:ext-gauge gives 𝒲_Λ(Φ_φ, ·) ≡ 0 over the whole test space, not just over 𝒢. That is (i).
(ii) follows by subtraction: P − cQ = (P − Q) + (1−c)Q. (iii) is (ii) evaluated at c = 1. ∎

So the answer to the task is **yes: the gauge is a radical for the entire form**, not only for the diagonal block. This
is CITED (Guo) and PROVED as a formal consequence.

### 1.2 NUMERICAL verification of A_R⊥(1) ≈ 0
`lemma_i3.py` computes the three pieces of P_R⊥ and Q_R⊥:
- **Cross archimedean.** On the Mellin side, (1/π)∫₀^600 m·Re(Φ̂_k·conj Ψ̂_j), with Φ̂ = ζ(½+iτ)φ̃(½+iτ) (P2) and
  Ψ̂ = ∫Ψe^{iτx} via Gauss–Legendre with 600 nodes.
- **Cross polar.** A_Φ B_Ψ + A_Ψ B_Φ, with A_Φ and B_Φ as in P2 and A_Ψ = ∫Ψe^{x/2}, B_Ψ = ∫Ψe^{−x/2}.
- **Cross comb.** With u = e^t and Ψ(t) = e^{t/2}R(e^t), ∫Ψ(t)Φ(t−log n)dt = n^{−½}∫R(u)S(u/n)du. S is evaluated
  by direct summation on a logarithmic grid in v ∈ [10⁻⁵/λ, 1/λ] plus a cubic spline. The sum runs over prime
  powers n < 2·10⁵ (sensitivity: n < 5·10⁴ in `sens/`).

| μ | cross Parseval (rel.) | max\|P_R⊥\| | max\|P_R⊥ − Q_R⊥\| | relative |
|---|---|---|---|---|
| 5 | 1.8e−5 | 0.9126 | 6.1e−4 (3.0e−4 with NC = 5·10⁴) | 7e−4 |
| 10 | 1.8e−5 | 0.9126 | 1.8e−4 | 2e−4 |
| 15 | 1.8e−5 | 0.9126 | 8.8e−4 | 1e−3 |

The residual satisfies three things:
- It is not systematic. It fluctuates between 2·10⁻⁴ and 9·10⁻⁴ when μ changes (the problem is invariant, §3.2) and when
  the cutoff in n changes.
- It concentrates in the first row of the gauge, the widest mode.
- It decays with j.

This is quadrature and S-interpolation noise, not a violation. NUMERICAL verdict: **A_R⊥(1) = 0 to the precision of the
block (≤ 10⁻³ relative)**, consistent with Guo. In §§2–4 I impose (i) exactly (P_RR := Q_RR, P_R⊥ := Q_R⊥), because
any numerical residual in A_R⊥(1) would contaminate the Schur complement at c = 1, where A_RR(1) = 0 is singular.

## 2. In(C_RR) (task 2)

### 2.1 What C_RR is
By 1.1(i), C_RR = Q|_𝒢 = P|_𝒢 = (arch + 2AB)|_𝒢.
- SPEC_004's claim "C_RR archimedean by R-Π" is correct only if "archimedean" includes the polar term.
- **arch|_𝒢 alone is not C_RR.** Inertias: arch|_𝒢 = (3,0,6) and (arch + 2AB)|_𝒢 = (2,0,7). The polar term 2AB, of
  rank ≤ 2, moves one eigenvalue's sign.
- The task's hypothesis ("In(C_RR) = In(arch|_𝒢), positive definite?") is corrected on both counts.

### 2.2 Results (NUMERICAL; independence of μ PROVED)

| block | dim 𝒢 | In(C_RR) | negative eigenvalues | In(arch\|_𝒢) |
|---|---|---|---|---|
| K = 6, μ = 5 | 5 | (2,0,3) | −0.0771, −0.0124 | (2,0,3) |
| K = 8, μ = 5 | 7 | (2,0,5) | −0.1144, −0.0399 | (2,0,5) |
| K = 10, μ = 5/10/15 | 9 | (2,0,7) | −0.1277, −0.0577 | (3,0,6) |

For K = 12 and 14 the orthonormalization of the raw basis fails: the Gram matrix has a negative eigenvalue in float64,
see `gK12.log`. There is no data there.

**Independence of μ (PROVED).** Φ_{φ(λ·)} is the translate of Φ_φ by −log λ. The complete form 𝒲_a is translation
invariant:
- the archimedean part depends on |Ψ̂|;
- the comb depends on autocorrelation;
- the polar part satisfies A(Ψ(·−s))B(Ψ(·−s)) = e^{s/2}e^{−s/2}AB.

This extends P2's "PROVED by scaling" to the whole block V_M, because W_J is also centered at −T (§3.2).

**Lemma I.3-b (NUMERICAL + ARGUED).** n₋(C_RR) = 2 is stable for dim 𝒢 ∈ {5, 7, 9}, while n₊ grows with the dimension.
- ARGUED: n₋(Q|_𝒢̄) = 2 on the full gauge, because the two negative modes stabilize (−0.077 → −0.114 → −0.128 and
  −0.012 → −0.040 → −0.058, monotonically).
- OPEN as a theorem.

### 2.3 Consequence for the jump (Cor I.2 of SPEC_004)
With A_⊥⊥(1) non-degenerate (§3), ι_M(c) = n₋(sign(1−c)C_RR):
- **ι = 2 for c < 1** and **ι = dim𝒢 − 2 = 7 for c > 1**, in the block.
- The jump is not "0 → dim𝒢", as the task assumed. It is "2 → dim𝒢−2", i.e. both sides nonzero.
- Moving c through 1 swaps n₋ and n₊ of C_RR. The only thing that distinguishes c = 1 is the vanishing A_RR(1) = 0,
  which is exactly Guo.

Contrast with the verified pencil. The complete A(c) has n₋ = 2 for c ∈ {0.9, 0.99} and n₋ = 7 for c ∈ {1.01, 1.1, 1.5}
(table §4.3). This matches P2: D_{0.9Λ} has n₋ = 2 and D_{1.1Λ} has n₋ = 7.

Reading: the falsifiers cΛ, c ≠ 1, are negative **already on the gauge**, with defect O(1)·|1−c|. That is P2 (4) in a
different coordinate.

## 3. A_⊥⊥(1): non-degeneracy and spectrum (task 3)

### 3.1 Data (NUMERICAL)
A_⊥⊥(1) = 𝒲_Λ on the quotient V_M/𝒢_M, with dim W_J = 8. Generalized eigenvalues with respect to the quotient L²
metric:

3.774, 5.604, 8.407, 8.609, 8.761, 10.96, 40.22, 605.6, identical at μ = 5, 10 and 15 up to 8 digits.

The inertia is (0,0,8), so **A_⊥⊥(1) ≻ 0 on the block**. All eigenvalues are O(1) or larger. **None is at
scale e^{−4πμ}** (at μ = 15, e^{−4πμ} ≈ 10⁻⁸²), not even at scale 10⁻³.

Hence Cor I.2's hypothesis (non-degeneracy) holds with gap O(1) on this block. ι_M is well defined and takes
the values of §2.3.

### 3.2 Why the block cannot see Mori's scale (PROVED)
V_M = 𝒢_M ⊕ W_J is the rigid translate of a fixed block, since everything is centered at −T. The complete form on the
line is translation invariant (§2.2). Therefore **the spectrum of A(c) on V_M does not depend on μ**.

Mori's smallness 4.76·10⁻⁷⁰ at μ = 15 does not come from 𝒲 on the line. It comes from the **carrier restriction**:
window support, band of f, Tate rows of φ₀, which is what fixes T. A block that does not encode the carrier does not
see λ^W. This matches P2 §5 ("𝔡_a independent of T") and extends it to the quotient.

### 3.3 Does it reproduce (10,0,1) with null vector = gauge? No.
GRAM_INERTIA_001 result 2:
- the inertia (10,0,1) is that of the Gram matrix of Möbius lines {ρ_m} ∪ {φ̂₀} on the outer ω grid;
- the "null" vector has eigenvalue 2.8·10⁵², at the float noise floor (1.9·10⁶⁷·ε);
- its vector is (μ(m)) ⊕ 1, the direction of the **33-digit cancellation** Σμ(m)ρ_m + φ̂₀ = ρ_p.

That direction is Mori's extremal p, with value W(p) ≈ 1.33·W* ≠ 0, not the gauge. It is not a radical vector: it is a
direction of relative scale 10⁻¹⁵ in a Gram matrix of size 10⁶⁷.

**The identification "Mori's null vector = gauge" is false** (NUMERICAL + definitional). SPEC_004 §3.3's test ("Lemma I.1
predicts … null μ⊕1") compares distinct objects:
- the gauge radical is exact (Guo) and infinite-dimensional;
- Mori's near-null vector has dimension 1 and a nonzero value, hidden by scale.

Thus "arena ≥ 12 modes" cannot be quantified with this block. What is quantified is negative: **on the free line, modulo
gauge, the gap is O(1).** All the smallness lies in the carrier restriction. In terms of the task: 0 eigenvalues at
scale e^{−4πμ} and 8 of 8 at O(1).

## 4. What I.3 yields: the affine congruence (task 4)

### 4.1 Lemma I.3-c (PROVED given Guo L4.4; algebraic)
Assume C = Q_RR invertible and define
L = [[I, C⁻¹Bᵀ],[0, I]] (independent of c), Q/C := Q_⊥⊥ − B C⁻¹ Bᵀ (Schur complement of the comb, "comb modulo gauge").
Then, **for all c ∈ ℝ, including c = 1**,
  A(c) = Lᵀ · [ (1−c)C  ⊕  S(c) ] · L,  with S(c) = A_⊥⊥(1) + (1−c)·Q/C.

*Proof.* By I.3-a, A_R⊥(c)·A_RR(c)⁻¹ = (1−c)Bᵀ·((1−c)C)⁻¹ = C⁻¹Bᵀ·(…), and that quotient does not depend on c.
Expanding: Lᵀ diag((1−c)C, S)L = [[(1−c)C, (1−c)Bᵀ],[(1−c)B, S + (1−c)BC⁻¹Bᵀ]].
Also S + (1−c)BC⁻¹Bᵀ = A_⊥⊥(1) + (1−c)Q_⊥⊥ = A_⊥⊥(c). At c = 1 both sides equal 0 ⊕ A_⊥⊥(1). ∎

Consequences:
- (a) **Global Haynsworth:** In A(c) = In((1−c)C) + In(A_⊥⊥(1) + (1−c)Q/C) for all c, with L fixed.
- (b) S(c) is **affine** in c. Hence d/dc S = −Q/C exactly and there are no O(ε²) terms.
  Correction to SPEC_004 §3.2: there it was written as (1−c)²C_⊥RC_RR⁻¹C_R⊥, but the correct factor is (1−c). Cor I.2's
  qualitative consequences do not change.
- (c) The task's key identity, d/dc S|_{c=1} = −Q_⊥⊥ + BC⁻¹Bᵀ, is correct and holds for all c.

### 4.2 Sign of Q/C? (NUMERICAL)
- In(Q/C) = (7,0,1) on the block.
- Quotient L² eigenvalues: −28.06, −4.09, −1.37, −0.78, −0.54, −0.34, −0.083, +1.07, the same for μ = 5, 10, 15.
- Complete In(Q) on V_M = (9,0,8) = In(C) + In(Q/C) = (2,0,7) + (7,0,1). Haynsworth checks out.

**Minimal mode.** Let u be the eigenvector of A_⊥⊥(1)'s minimal eigenvalue, value 3.774. Then **uᵀ(Q/C)u = −7.34 < 0**.

Therefore the task's conjecture, "the comb modulo gauge is ≽ 0 on the near-kernel", is **false on the block**
(NUMERICAL). Its premise ("λ^W(c) non-increasing in c ⇒ S(1−ε) ≽ S(1)") also fails:
- d/dc S = −Q/C is indefinite;
- monotonicity of the complete form would require Q ≽ 0, and In Q = (9,0,8).

For c < 1 the quotient's minimal mode **grows** as c approaches 1 from below (2.58 at c = 0.9, 3.70 at 0.99, 3.77 at 1).
For c > 1 it keeps growing (3.84 at 1.01, 4.31 at 1.1, 5.48 at 1.5). No fixed-sign monotonicity distinguishes c = 1.

### 4.3 Verified pencil (μ = 15; μ = 5 and 10 identical)

| c | In A(c) | In((1−c)C) | In S(c) | λ_min S(c) (quotient L²) |
|---|---|---|---|---|
| 0.5 | (3,0,14) | (2,0,7) | (1,0,7) | −7.47 |
| 0.9 | (2,0,15) | (2,0,7) | (0,0,8) | 2.58 |
| 0.99 | (2,0,15) | (2,0,7) | (0,0,8) | 3.70 |
| 1.01 | (7,0,10) | (7,0,2) | (0,0,8) | 3.84 |
| 1.1 | (7,0,10) | (7,0,2) | (0,0,8) | 4.31 |
| 1.5 | (7,0,10) | (7,0,2) | (0,0,8) | 5.48 |

Haynsworth holds in every row. S loses positivity at some c between 0.5 and 0.9 (not precisely located), which is the
first loss in the quotient: the first-order estimate on u is 1 − c ≈ 3.774/7.34 ≈ 0.51, and the exact value depends on
the block.

### 4.4 New identity, REF-D, or empty?
- **As an identity, new and exact (PROVED given Guo):** the affine congruence I.3-c. To understand the pencil cΛ, a
  fixed object suffices, the pair (C, Q/C), plus the sign datum A_⊥⊥(1).
- **As a source of sign, empty:**
  - C and Q/C are indefinite;
  - Q/C is computed only from the comb, with no carrier restriction;
  - the only summand that can have a definite sign is A_⊥⊥(1) = 𝒲_Λ on the quotient = (★★) in block form. That is
    **REF-D**: the sought positivity, not a tool.
- **"≽ 0 on the near-kernel": NUMERICAL NO-GO.** It is false on the block, and moreover would not follow from any
  available monotonicity.

The structure "the sign lives only in the quotient by the radical" confirms channel (β) of M200 and P2 in a different
coordinate.

## 5. Final

### 5.1 Labels
- I.3-a (gauge radical for the whole form ⇒ A_RR = (1−c)C, A_R⊥ = (1−c)Bᵀ, A(1) = 0 ⊕ A_⊥⊥(1)): **PROVED given Guo L4.4
  (CITED)**. Verification of A_R⊥(1) ≈ 0: **NUMERICAL** (≤ 10⁻³ relative).
- In(C_RR) = (2,0,dim𝒢−2) for dim𝒢 = 5, 7, 9: **NUMERICAL**.
  - Independence of μ: **PROVED** (translation invariance).
  - n₋ = 2 on the full gauge: **ARGUED/OPEN**.
  - C_RR ≠ arch|_𝒢 (the polar part matters): **NUMERICAL**.
  - "C_RR ≻ 0, jump of dim 𝒢": **NO-GO (false)**.
- A_⊥⊥(1) ≻ 0 on the block, with gap O(1) and μ-independent spectrum: **NUMERICAL + PROVED (independence)**. Cor I.2
  applies and gives ι = 2 (c<1), ι = 7 (c>1).
- "Mori's null vector μ⊕1 = gauge": **false** (definitional + NUMERICAL from GRAM_INERTIA). Scale e^{−4πμ} = carrier
  restriction, not the free 𝒲: **PROVED** (for translated blocks).
- I.3-c (affine congruence with fixed L, S(c) = A_⊥⊥(1) + (1−c)Q/C): **PROVED given Guo**. Corrects SPEC_004's (1−c)² factor.
- "Comb modulo gauge ≽ 0 on the near-kernel": **NUMERICAL NO-GO** (In Q/C = (7,0,1), uᵀ(Q/C)u = −7.34).
- Lemma I.3 overall: **closed as NO-GO as a sign object**. The sign is A_⊥⊥(1) = (★★) in block form (REF-D). What
  remains as a valid coordinate: the pencil cΛ reduces exactly to (C, Q/C) plus the quotient. **Row D: OPEN.**

### 5.2 New constraint (for the crossword)
**R-I3.** Every object built on the pencil cΛ and the gauge radical factors through the fixed congruence L into two
parts:
- a comb datum (C = Q|_𝒢 and Q/C), which is indefinite, translation invariant and blind to the carrier;
- the sign datum A_⊥⊥(1) = 𝒲_Λ on the quotient.

Moreover, any smallness at scale e^{−4πμ} must come from the carrier restriction, since translated blocks of the free
line have μ-independent spectrum. A sign object that does not encode the carrier sees gap O(1) and cannot
separate Λ from cΛ beyond |1−c|·O(1).

### 5.3 Entry for the index (paste into ROUTES-TRIED-INDEX/README.md, phase 200 block)
- **LEMMA_I3_001 (round 10, Q1): Lemma I.3 NO-GO as a sign object.**
  - I.3-a PROVED (Guo CITED): gauge radical of the whole form, A_R⊥(1) = 0 (NUMERICAL ≤ 10⁻³).
  - In(C_RR) = (2,0,dim𝒢−2) (NUMERICAL, dim 5/7/9; μ-independent PROVED). C_RR = (arch+2AB)|_𝒢 ≠ arch|_𝒢. Jump
    ι: 2 → 7, not 0 → dim𝒢.
  - I.3-c PROVED: A(c) = Lᵀ[(1−c)C ⊕ (A_⊥⊥(1) + (1−c)Q/C)]L with fixed L (corrects (1−c)² in SPEC_004).
  - Q/C indefinite (7,0,1); "comb mod gauge ≽ 0 on near-kernel" FALSE (uᵀ(Q/C)u = −7.34).
  - A_⊥⊥(1) ≻ 0 with gap O(1), μ-independent: scale e^{−4πμ} comes only from the carrier.
  - Mori's null vector μ⊕1 ≠ gauge.
  - Do not retry: comb signature on the radical / Schur complement of the comb modulo gauge as a source of sign.

### 5.4 Next lemma
**Lemma I.4 (carrier on the quotient).** Repeat I.3-c with V_M replaced by the **carrier** block (outer window +
Tate rows, EXTERIOR/GRAM_INERTIA pipeline at precision ≥ 100 digits), with the explicit gauge embedded.
The question is: is the minimal mode of A_⊥⊥(1) restricted to the carrier exactly Mori's extremal p, and is its value
4.76·10⁻⁷⁰ a quotient Rayleigh quotient controllable by (C, Q/C) plus the carrier restriction?

If the carrier is written as a closed subspace 𝒫_T of V/𝒢, the sign is the positivity of A_⊥⊥(1)|_{𝒫_T}, and the
constructive question becomes the geometry of 𝒫_T relative to the negative eigenvectors of Q/C. That is the only
T-dependent ingredient left. Before launching it, grep the index for "carrier quotient" and
"C1_DUPLICATION" (Schur complement), and give the new reason: 𝒫_T appears explicitly in the quotient by the radical,
and that was not present in C1.
