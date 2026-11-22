# DH_TRANSFER_001: transfer lemma to Davenport–Heilbronn (phase 200, round 17A)

Objective: close piece Φ.3 (channel (i), input I3 "symbol of Z on Re s = ½"), which is the only
ARGUED piece of branches 1–2 of Φ200 (META_200_BARRIER_001 §1.4 and Addendum A1; SPEC_SIGN_OBJECT_006 §B.3; R-Z1 in
Z_CARRIER_001). F_DH appears only as a falsifier of window
positivity.

## Summary (≤250 words)

The transfer lemma, as stated in META_200 §1.4 ("everything that is deduced from ζ using only its symbol on the
line holds for DH"), is **false if read as an information restriction** (Prop. 2.1, PROVED). The function
t ↦ ζ(½+it) is real-analytic and determines ζ, and with it the Euler product. So "using only the symbol" restricts
nothing. The lemma is **true, and PROVED, if read as a restriction of premises** (Theorem 3.1). For that one
fixes a degree-1 theory 𝔗₁: functional equation with (ε, δ, q), real bounded coefficients, order 1, pole with residue r ≥ 0 and no
multiplicativity. F_DH is a model of 𝔗₁ with δ = 1, q = 5, r = 0, ε = 1 (verified in §1). The window form
𝔞_T^{(L)} is defined uniformly across models (§1.3).

Full classification (§4) of the symbol properties a lower bound of λ_A can use:
- **S1**: identities of 𝔗₁, including the null symbol F4. They transfer (PROVED).
- **S2**: upper and order bounds for |L(½+it)| and its moments. They transfer (CITED/PROVED).
- **S3**: localization of zeros. Goes to REF-D.
- **S4**: arithmetic readings across the line: moment constants with Euler factor, lower bounds of
  exact order (log T)^{k²}, mollifiers with μ. **They do not transfer**, and are not channel (i): they consume premises outside
  𝔗₁ and are reassigned to I10 or to C-data (Φ.10, branch 2 or 5).

That reassignment of nonlinear S4 (order ≥ 2 in the coefficients) to C-data is ARGUED: it is the **candidate** of the round.

F4 transfers pointwise. Distributionally, the mass on the ordinates only sees zeros on the line. Pairs of
zeros off the line cancel in the boundary value and enter the form only via analytic continuation of the test.

Record correction: in the corpus **there is no certified witness** for DH. Ziad is UNVERIFIED and CERT_FALSIFIERS
has no DH row. The existence of a witness is CITED/ARGUED (§1.4).

## 0. Corpus and index check

- Checked: ROUTES-TRIED-INDEX (families C1 "linear in Λ / comb-generic", in LEDGER_L5_META), P46 rem:twohalves
  (l.3330), rem:FDH (l.8334), thm:ext-half, rem:ext-killing, lem:K/eq:m, MECH_001 (F-DH, K_{3/4}, conductor 5),
  GUO_QUANT_001 (Prop. 1.3: Φ_f^{DH} ∈ rad 𝒲_{DH}, PROVED), AUDIT_200_SPEC_002 (unconditional F4) and
  A_MU_FACTORIZATION_001 (§1(a): Fejér–Riesz NO-GO by F4 + P4).
- This memo does not retry any route. It is a classification lemma of premises that had not been written. No entry
  in the index contains it: searching for "transfer", "Davenport", "𝔗₁" and "degree-1 theory" gave only the uses of
  DH as a falsifier.
- **Record correction, for the editor.** The brief states that DH has negative witnesses certified in
  phase-198 CERT_FALSIFIERS. That is not the case. CERT_FALSIFIERS_001 certifies rows Y1, AA (zero comb, a_P, cΛ) and row 11
  of Epstein x²+5y². **There is no DH row.** Across the whole corpus, F-DH appears as "CITED Ziad, UNVERIFIED / PLAUSIBLE"
  (P46 rem:FDH; PROOF_L_SHARP_A/C/E/F/H; MECH_001 l.160). CERT_FALSIFIERS's "zero comb" is the comb a = 0 in
  the odd sector, which is not DH.

## 1. Data on F_DH and parametric window form

### 1.1 The function (CITED: Davenport–Heilbronn 1936; Titchmarsh §10.25; own verification)

Let χ be the character mod 5 with χ(2) = i. Then χ(−1) = χ(4) = χ(2)² = −1, so χ is **odd** (δ = 1). Set

  κ = (√(10−2√5) − 2)/(√5 − 1) ≈ 0.2840790,

and the definition is

  F_DH(s) = ½(1 − iκ) L(s,χ) + ½(1 + iκ) L(s,χ̄).

Numerical check of the constant: √(10−2√5) = 2.3511410…, and (2.3511410 − 2)/1.2360680 = 0.2840790. Matches
Titchmarsh.

The coefficients are periodic mod 5 and real: a₁ = 1, a₂ = κ, a₃ = −κ, a₄ = −1, a₅ = 0 (and a_n = a_{n mod 5}). The
functional equation is

  Λ_DH(s) := (5/π)^{s/2} Γ((s+1)/2) F_DH(s) = Λ_DH(1 − s),

with ε = 1. The constant κ is chosen precisely so that the root numbers of χ and χ̄ combine into ε = 1. Hence
the factor is Γ_ℝ(s+1)·5^{s/2} up to a constant.

Other properties: F_DH is entire (no pole), has no Euler product, and has infinitely many zeros in Re s > 1
(Davenport–Heilbronn 1936, CITED). It also has infinitely many zeros in ½ < Re s < 1 (CITED: Voronin; Spira numerically).

### 1.2 The theory 𝔗₁ (definition)

𝔗₁ is the theory of triples (L, θ, r) with θ = (ε, δ, q), δ ∈ {0,1}, q ≥ 1, r ≥ 0, satisfying:

- **(A1)** L(s) = Σ a_n n^{−s} with a_n ∈ ℝ, a₁ = 1 and |a_n| ≤ C, absolutely convergent for Re s > 1.
- **(A2)** (s − 1)^{𝟙[r>0]}·L(s) is entire of order 1, with residue r at s = 1.
- **(A3)** Λ_L(s) = q^{s/2} Γ_ℝ(s+δ) L(s) satisfies Λ_L(s) = εΛ_L(1−s), with ε = ±1.

There is no multiplicativity axiom, nor one on the support of −L′/L on prime powers, nor on zero localization.

Models: ζ is a model with θ = (1, 0, 1) and r = 1. F_DH is a model with θ = (1, 1, 5) and r = 0.

### 1.3 Parametric window form (verified against P46 lem:K, eq:m, def:W and eq:Aform)

For a model L, write −L′/L(s) = Σ_{n≥2} b_n n^{−s} for large Re s. This exists because a₁ = 1, and the b_n are
real. Define:

- the comb v_n^{(L)} = 2b_n/√n;
- the archimedean symbol m_L(t) = log(q/π) + Re ψ((½+δ)/2 + it/2), which is 2Re of the logarithmic derivative of the Γ
  factor at ½ + it;
- the kernel K_δ(u) = 2Σ_k e^{−(2k+½+δ)u} (for DH, K_{3/4}, as in MECH_001);
- the constant C₀^{(L)} = m_L(0).

For δ = 0 and q = 1 this reproduces exactly eq:m (C₀ = ψ(¼) − log π) and the kernel K of lem:K.

The form 𝔞_T^{(L)}(F) is the "Method" formula of CERT_FALSIFIERS, with (C₀, K, v) replaced by
(C₀^{(L)}, K_δ, v^{(L)}), plus the polar term r·(A,B) of eq:Aform. This term vanishes on P_T, and for r = 0 it does not
exist. P_T is defined the same way as in P46 l.121 (A = B = 0) for every model. For DH it is a codimension-2
restriction with no polar content.

### 1.4 Status of the DH falsifier (honest)

- **(F-DH-ex) CITED + ARGUED.** Let ρ₀ = β₀ + iγ₀ be a zero of F_DH with β₀ ≠ ½. By F_DH's explicit formula (which holds
  in 𝔗₁, S1), the Weil form of F_DH is a Σ_ρ Φ(ρ)·Φ̄(1−ρ̄)-type sum. Weil's argument (1952) applied to F_DH builds
  compactly supported tests with negative value. The argument consists in interpolating at finitely many Mellin
  nodes within Paley–Wiener, and adding the two nodes s = 0, 1 of P_T is compatible with that interpolation. By
  monotonicity in T, there exists T_DH < ∞ such that 𝔞_T^{(DH)} ≱ 0 on P_T for every T ≥ T_DH. Label: **ARGUED** (standard
  argument not written out in full detail here; T_DH not quantified).
- **(F-DH-Ziad) UNVERIFIED.** The ratio −6.169·10^{−9} for a < 9/5 (rem:FDH) has not been reproduced.
- **Consequence for M200.** Every time branch 1 is closed with "DH" at a fixed window T, it depends on
  (F-DH-Ziad). For T ≥ T_DH it depends only on (F-DH-ex). The editor is advised to note in the grid that **DH is not
  certified**, and that at a fixed window, the certified falsifier closest in spirit is Epstein x²+5y² (row 11,
  PROVED). The latter shares a functional equation and Γ factor (of degree 2), has a pole, and has no Euler product.

## 2. The information-theoretic reading is false

**Proposition 2.1 (PROVED).** The datum 𝔇(L) = (θ, r, t ↦ L(½+it)) determines L, and hence determines whether L has
an Euler product. Consequently, the class "properties of L that depend on L only through 𝔇(L)" is the class of **all**
properties of L. ζ and F_DH do not share all their properties: for example, "the continuation of t ↦ L(½+it) to
Re s > 1 is Π_p (1−p^{−s})^{−1}".

*Proof.* t ↦ L(½+it) is the restriction of a meromorphic function to a line. By the identity principle, it determines
L on all of ℂ, and then its coefficients a_n = lim_{X} (1/2X)∫_{−X}^{X} L(2+it) n^{2+it} dt. ∎

**Reading.** R-Z1 ("Z used only via its symbol on the line") and piece Φ.3 cannot be an information statement. They must
be a statement about **premises**: which facts about L are invoked, not which data are looked at. That is the correct
restatement of the lemma requested by META_200 §1.4, and it follows next. The "tautological" case of the question is
exactly Theorem 3.1. The non-tautological part is checking that the corpus's channel (i) fits inside 𝔗₁ (§4) and
locating what does not fit (S4).

## 3. Transfer theorem

**Definition.** A channel-(i) inference is a deduction of an inequality Ψ(T; L) ≤ λ_A(T; L) whose premises
about L are theorems of 𝔗₁, possibly with constants depending only on (θ, r, C), and whose steps are the
operations of 𝒦_Φ (§B.1). The constants C must hold uniformly for |a_n| ≤ C.

**Theorem 3.1 (transfer, PROVED).** If Ψ(T; ·) is a channel-(i) soundness statement, then Ψ(T; F_DH) ≤ λ_A(T; F_DH). In
particular, if Ψ is uniform (depending on L only through θ, r and C) and Ψ(T; ζ) > 0 for some T ≥ T_DH, then
Ψ(T; F_DH) holds the same with DH's constants, which contradicts (F-DH-ex). Hence, a uniform channel-(i) Ψ
**does not decide** any window T ≥ T_DH. It falls into branch 1 of M200, or is blind to the difference.

*Proof.* It is the soundness of the deduction: each premise is a theorem of 𝔗₁, and F_DH is a model of 𝔗₁ (§1.1).
Each operation of 𝒦_Φ is defined in terms of 𝔞_T^{(L)}, which is defined uniformly across models (§1.3). A
deduction valid in every model holds for F_DH. ∎

**Remark.** The uniform part is what matters. If Ψ uses a constant that holds for ζ but not for every model
(for example, the numerical value of ζ(½+it) from a table), then the premise is not a theorem of 𝔗₁: it is a
specific datum (S4 or C-data).

## 4. Full classification of symbol properties

For each property the corpus has used or might use in channel (i), we state which class it falls into and whether it transfers.

### S1. Identities of 𝔗₁ — transfer (PROVED)

1. **Functional equation and reality on the line.** With real a_n and ε = 1, Λ_L(½+it) ∈ ℝ. Holds for DH.
2. **Hadamard factorization and explicit formula** with b_n in place of Λ(n). Holds in 𝔗₁.
3. **Smooth AFE and Riemann–Siegel AFE.** Lavrik's holds for any degree-1 functional equation with bounded coefficients. For
   DH it is additionally the linear combination of the AFEs of L(s,χ) and L(s,χ̄).
4. **T.1 (SPEC_002), 𝓕Ψ̌ = ĝ·D_μ(½+it).** The Fourier identity holds in 𝔗₁ whenever the radical is available.
   For DH it is: GUO_QUANT_001 Prop. 1.3 gives Φ^{DH}_f ∈ rad 𝒲_{DH} (PROVED). The difference lies in D_μ: for ζ,
   D_μ is truncated Möbius. For DH it is the truncation of 1/F_DH, whose coefficients are not multiplicative. This is **not**
   channel (i): it is the gap c_N = 0, site (γ) of R-Z1 and channel (iv), already PROVED in M200.
5. **The null symbol F4.** See §5.

### S2. Inequalities on |L(½+it)| and its moments (upper and order bounds) — transfer

1. **Convexity / Phragmén–Lindelöf**, |L(½+it)| ≪ (q|t|)^{¼+ε}. Theorem of 𝔗₁: PROVED.
2. **Subconvexity** (Weyl/Burgess, Bourgain for ζ). For DH: CITED for L(s,χ) mod 5, and by triangle inequality
   for F_DH. The exponent transfers; the constants change depending on θ and C.
3. **Second moment (Ingham, Montgomery–Vaughan).** ∫_0^X |L(½+it)|² ~ (Σ|ĉ_j|²)·X log X. Uses only |a_n| ≤ C and the
   AFE. For DH the constant is ½(1+κ²)·(φ(5)/5) with MV's normalization. CITED. The order transfers; the constant
   differs, but no lower bound of λ_A can use the exact constant without entering S4.
4. **Upper bounds of 2k-th moments.** Via MV applied to L^k, with coefficients ≤ C^k d_k(n). For DH these give the same
   order as for ζ. PROVED in 𝔗₁.
5. **Weak lower bounds on moments** (Hölder from the second moment, ≫ X(log X)^k). Theorem of 𝔗₁: PROVED.

### S3. Properties of the zeros — go to REF-D

This includes the count N(T) (S1, transfers), the proportion of zeros on the line, simplicity, Levinson/Conrey, and
localization.

- Hardy/Selberg on-the-line results have an analogue for DH: infinitely many zeros on the line, and for linear
  combinations there is a positive proportion (Selberg 1989, Bombieri–Hejhal 1995, CITED).
- Levinson/Conrey (≥ 40%) uses a mollifier with μ. That is a premise outside 𝔗₁ and is handled in S4.
- Any lower bound of λ_A that uses where the zeros are enters the representation of rem:ext-killing(iii),
  W_T(Ef) = Σ_ρ Φ_{Ψ_f}(ρ)Φ_{Ψ_f}(1−ρ). A premise fixing the sign of the summands is, by P4 of the corpus, positivity
  itself restricted to the class. Branch 2, REF-D. (This is the classification already made by
  A_MU_FACTORIZATION §1(a) and Φ.11; here it is only reused.)

### S4. Arithmetic readings across the line — do NOT transfer, and are not channel (i)

| property of ζ(½+it) | does F_DH share it? | premise outside 𝔗₁ | actual channel |
|---|---|---|---|
| continuation with Euler product (Prop. 2.1) | no | multiplicativity | I10 (Φ.10) |
| exact constant of the 4th moment, (1/2π²)X log⁴X (Ingham), and in general a_k g_k (Keating–Snaith) | no: DH's constant is a different combination of (1±iκ)/2 with cross terms | Σd(n)²n^{−s} = ζ⁴/ζ(2s) (Ramanujan) | I10 / C-data (order 2 in the coefficients) |
| lower bounds of exact order ∫|ζ|^{2k} ≫ X(log X)^{k²} (Ramachandra, Heath-Brown, Radziwiłł–Soundararajan) | order for DH not established by that method (Bombieri–Hejhal suggest the same order, with a different constant) | Euler product in the test Dirichlet polynomial | I10 |
| mollifiers with μ (Levinson/Conrey, D_μ of T.1) | no: 1/F_DH is not multiplicative | 1∗μ = δ | channel (iv), gap c_N = 0 (PROVED in M200) |
| Selberg CLT with independent structure over primes | DH: log|F| is Gaussian, but via dominance of one summand (Bombieri–Hejhal) | independence of p^{−it} | I10 |
| negative moments of ζ′(ρ) (Gonek–Hejhal) | — | simple zeros / on the line | S3 → REF-D |

**Lemma 4.1 (reassignment, PROVED as a classification of premises).** Every premise about L used in an inference that
reads the symbol is one of two kinds:

- it is a theorem of 𝔗₁ (S1, S2, or the count of S3), and it transfers by Theorem 3.1; or
- it invokes at least one of these facts: (P-mult) multiplicativity of a_n or of 1/L; (P-sop) support of b_n on prime
  powers; (P-pol) r > 0 with a specific residue; (P-cer) zero localization; (P-val) specific numerical values of ζ.

*Proof.* 𝔗₁ is exactly (A1)–(A3). A premise that is not a theorem of 𝔗₁ is false in some model. The list
(P-mult)–(P-val) runs through the features in which the relevant models differ (ζ, F_DH, Epstein, cΛ via b_n):

- multiplicativity, which separates ζ from DH;
- support of b_n, which separates ζ from cΛ, DH and Epstein;
- residue, which separates ζ from DH;
- zeros, which separate ζ from DH;
- values.

Exhaustiveness is relative to this battery: two models of 𝔗₁ with equal θ, r, multiplicativity, support of b_n and
zeros coincide. They have the same zeros and the same Γ factor, so by Hadamard they are equal up to e^{a+bs}, and a₁ = 1 plus
the functional equation fix the constant. ∎

Destination of each class:

- (P-mult) goes to I10, Φ.10.
- (P-sop) is "linear in Λ", C1, goes to branch 2 via Φ.1.
- (P-pol) goes to I5, Φ.5.
- (P-cer) goes to S3, REF-D.
- (P-val) is C-data, branch 5, or a numerical certificate (branch 2 via thm:D1 if used on fixed tests).

## 5. The null symbol F4 for F_DH (requested precision)

**Proposition 5.1 (PROVED).** Set m_DH(t) = log(5/π) + Re ψ(¾ + it/2). Then:

**(a) Pointwise.** m_DH(t) + 2Re(F_DH′/F_DH)(½+it) = 0 for every real t that is not the ordinate of a zero **on**
the line.

*Proof of (a).* Λ_DH(½+it) is real (FE + real coefficients + ε = 1). Hence 2Re(Λ_DH′/Λ_DH)(½+it) = 0 wherever it
does not vanish. Also, 2Re of the logarithmic derivative of the factor (5/π)^{s/2}Γ((s+1)/2) at ½ + it is exactly m_DH(t). There
is no polar term. (For ζ, the polar term Re[1/(s−1) + 1/s] vanishes on the line, which gives F4 exactly as verified by
AUDIT_200_SPEC_002.) ∎

**(b) Boundary value.** As distributions in t, as σ ↓ ½,

  m_DH(t) + 2Re(F_DH′/F_DH)(σ+it) → 2π Σ_{ρ: Re ρ = ½} δ(t − γ_ρ).

*Proof of (b).* By Hadamard, Λ′/Λ(s) = B + Σ_ρ 1/(s−ρ), with Re B = −Σ Re 1/ρ (the standard degree-1 normalization). For a
zero ρ = ½ + iγ, Re 1/(σ−½ + i(t−γ)) is the Poisson kernel, which tends to πδ(t−γ). For a pair
off the line, ρ = β + iγ and 1 − ρ̄ = 1 − β + iγ, with β ≠ ½, the sum is

  (σ−β)/((σ−β)² + u²) + (σ−1+β)/((σ−1+β)² + u²),  with u = t − γ.

At σ = ½ this equals (½−β)/((½−β)² + u²) − (½−β)/((½−β)² + u²) = 0, and the convergence is locally uniform in u. The
factor 2 of "2Re" produces the 2π. ∎

**(c) Off-line pairs in the form.** Zeros off the line **do not** appear as mass in the boundary value.
They enter 𝔞_T^{(DH)} only via the explicit formula with a Paley–Wiener test, as values ĝ(γ − i(β−½))·conj(ĝ)(…)
of the entire extension of the test. For F ∈ P_T with window T ≥ T_DH, those terms can be negative (F-DH-ex).

*Proof of (c).* By the explicit formula in 𝔗₁ and (b). ∎

**Consequence.** The F4 identity transfers as is, in (a) and in (b). What does not transfer is the statement "all the
mass of 𝔞 is on the ordinates, as a positive measure." For DH it fails by (c), and for ζ that statement is a premise
(P-cer): S3, REF-D. This is compatible with, and makes precise, A_MU_FACTORIZATION §1(a) ("σ ≡ 0 as a function; the
form lives only with mass on zeros"). The Fejér–Riesz NO-GO is therefore pure channel (i) and is PROVED without the
ARGUED lemma.

## 6. Result on Φ200

**Theorem 6.1 (Φ.3 restated).** Channel (i) is defined as the set of premises that are theorems of 𝔗₁ (§3).
Then Φ.3 is **PROVED**: every uniform channel-(i) Ψ is comb-generic, with DH as the falsifier. The DH-falsification
of a fixed window is ARGUED (F-DH-ex) or UNVERIFIED (Ziad).

For windows where DH is not certified, the degree-1 part with no Euler product and with a pole is also covered
by Epstein (row 11 PROVED, T = 1.59, and negative for T ≥ 1.59 by Lemma M). But Epstein is degree 2 and a model of an
analogous 𝔗₂, so it covers the Ψ that hold uniformly in 𝔗₁ ∪ 𝔗₂. This extension is ARGUED: uniformity across
degree has not been checked piece by piece.

**What shifts.** By Lemma 4.1, what the corpus called "channel (i) ARGUED" is distributed as follows:

| part | content | status |
|---|---|---|
| S1, S2, S3-count | transfer | PROVED |
| (P-sop), (P-pol), (P-cer), (linear P-mult) | pieces Φ.1, Φ.5, S3, Φ.10 | already PROVED |
| (P-mult) of order ≥ 2 read across the line | arithmetic moment constants (Ingham's 4th moment, Σd², a_k g_k), lower bounds of exact order (log)^{k²} | reassigned to C-data (branch 5) or Φ.10: **ARGUED** |

In the last row, the argument is that an order-2 relation between data (Λ∗Λ, d∗d) does not enter an inequality
with variables (C-data). It is not proved for the case where the arithmetic constant enters as a coefficient of a
moment inequality weighted by |ĝ|²|D_μ|² depending on the test.

**Candidate of the round (OPEN).** This is the only symbol property that does not transfer and is not already assigned to a
PROVED piece:

> **Weighted moments of |ζ(½+it)|^{2k}, k ≥ 2, with exact arithmetic constant and explicit error at finite scale.**
> Its content is the order-2 Euler product (d∗d, a_k g_k). It is false for F_DH with the same constant and is not
> REF-D.

Whether it is useful for the sign is doubtful. What is clear is where it would appear: in T.1 the effective symbol is
|D_μ(½+it)|²·[m − Σv_n cos(t log n)], and |ζ|^{2k} does not appear directly. It would only appear after rewriting D_μ ≈ 1/ζ, and
that rewriting is the Möbius tail (channel (iv)). That is why the candidate is **weak**, and it is recorded as the exact
residue of Φ.3, not as a route.

## 7. Labels

| statement | label |
|---|---|
| data on F_DH (κ, odd χ, Γ_ℝ(s+1), q = 5, ε = 1) | CITED + verified |
| Prop. 2.1 (the information-theoretic reading of the lemma is false) | PROVED |
| Theorem 3.1 (transfer for premises in 𝔗₁) | PROVED |
| Lemma 4.1 (reassignment of premises) | PROVED (exhaustive relative to the battery) |
| Prop. 5.1 (F4 for DH pointwise and on the boundary; off-line pairs) | PROVED |
| (F-DH-ex): DH falsifies for T ≥ T_DH | ARGUED (Weil + DH 1936 CITED) |
| (F-DH-Ziad) a < 9/5 | UNVERIFIED |
| Φ.3 restated | PROVED |
| S4 residue of order ≥ 2 → C-data | ARGUED |
| candidate (moments with arithmetic constant) | OPEN |
| L′♯ / row D | OPEN |

**Pending for the editor:**

1. Note in ROUTES-TRIED-INDEX: "DH transfer lemma, channel (i): PROVED in 𝔗₁ form; the information-theoretic reading
   is false (Prop. 2.1); residue = order-≥2 S4".
2. Note in the grid and in the crossword that DH is **not** certified in CERT_FALSIFIERS.
3. If Φ.3 is wanted at a fixed window, certify a DH witness with CERT_FALSIFIERS's method, replacing (C₀, K, v)
   with those of §1.3.
