# Round 10, A: additive covariance as the mechanism of the sign

Notation of the common brief. a_T(F) = Arch(F) − Σ_n v_n c_F(log n) on P_T, v_n = 2Λ(n)/√n.
In logarithmic coordinate, τ_a F(t) = F(t+a), X = multiplication by t, 𝓕 is the transported additive
transform and M = m(D).

**Lead examined.** No Sonin-type identity can carry the sign by virtue of being unitary and scale-covariant,
because F_S = I·m_∞(D)e^{iφ_S(D)} has those two properties for every phase (ANNEX_SONIN_READING §4). The
property that only the true transform has is additive covariance: canonical commutation relation,
kernel e^{2πixy} and Poisson on ℤ. That covariance would have to be coupled with Σ_{d|n}Λ(d) = log n. Lemma A of
ROUND_009_G2 explains why: a step that uses only divisors is blind to Beurling.

**Result.** The coupling requested by the lead is already written in the corpus. It is the Müntz–Chebyshev
anomaly identity (PC) of phase 161, R161_001 Thm. 3.1. It puts three things in one line: the
Tate–Beckner relation X + 𝓕X𝓕 = M (R160_C8_R1 Thm. 1 and Cor. 2.4), the Poisson defect E_N = S_N𝓕 − JS_N and the
divisor hyperbola H = L_M S_N − K_N, which contains Λ∗1 = log. Phase 161 traversed it between R161_001 and
R161_081.

None of the three directions of the brief passes the gate. The exact residue that remains open is recorded below.

## 0. Primary-source cross-check

| Topic | File and section | What was built | Where it stopped and why |
|---|---|---|---|
| Arch as logarithmic uncertainty, with exact constant C_0 = ψ(¼) − log π | `phase-160-row-d-infinite-T/R160_C8_R1.md`, Thm. 1 and Cor. 2.3–2.5 | a_T is the logarithmic uncertainty functional of the Tate–Fourier involution 𝔉_S. Its archimedean part is Beckner's inequality with exact constant C_0 (PROVED on a dense class, CITED Beckner). For S finite the semilocal constant is κ_S = C_0 − Σ 2log p/(√p−1) | O-1, «window Beckner for all T», remained OPEN and is a reformulation. Row I-12: the Tate multipliers only fix a constant by the product formula (Thm. 3). Row S-8: X + 𝔉X𝔉 is indefinite on L²(ℝ) |
| (i) Contact part as the commutator of log\|x\| with the sum E f(x) = Σ f(nx) | `phase-161-row-d-sum-product-square/R161_001_MUNTZ_CHEBYSHEV_ANOMALY.md` §§1–6 | Identity (PC), PROVED for M_0 and N finite: S_N A_{M_0}𝓕 is expressed through {X, E_N}, L*E_N, JH and H𝓕. Here S_N is the Müntz sum operator, which in coordinate x is Σ n^{−1/2}f(nx), and the «additive covariance» is 𝓕 with E_N. Thm. 4.1: with cΛ and with deletions an interior defect δ_a(k) = Σ_{d\|k}a(d) − log k appears at the first affected k; in Beurling the integer Poisson datum is missing | R161_002 §§0–1: the canonical square ‖S_N A_M 𝓕F‖² sees A², not A, and is therefore blind to the sign. Missing: «an orientation of the Poisson boundary defect» |
| Covariant derivative [X, ·] of the Poisson defect | R161_040; R161_041 §§0, 3, 6 | Poisson identifies the two exterior histories (040). The derivative of the difference E gives the mean U+V; that of the sum C = Z𝓕 + JZ gives the critical jet U − V = ZM𝓕 − {X,C} (041 Thm. 3.1, PROVED) | Only E gives a vanishing linear commutator; only C has no Poisson control. The compressed mixed pairing E–C is needed |
| Mixed pairing E–C (Green) | R161_042–044 | Exact Green identity: leaves the difference of oriented first moments, which is a positive distance-to-boundary energy | The term C_N X f breaks the Tate moments. Its correction has opposite parity and the pairing vanishes (043). The primitive term collides with the horizontal NO-GO (044). RULES_AVOID K1: «residual pieces without sign» |
| Local Toeplitz–Hankel square | R161_045; RULES_AVOID R2 | Rank-one Toeplitz–Hankel | Does not globalize (assembly closed in phase 122) |
| Boundary waves of the Poisson defect | `phase-163-integrality-defect/R163_154_RESCALED_POISSON_BOUNDARY_WAVES.md` l. 68–83 | Rescaled expansion of E_N^ren via Tate–Beckner | l. 83: the principal operator uses only the integer comb and the functional equation, without Λ∗1 = log or the weight of a prime. It is the same for any weight a. Coupling to the Euler jumps is missing (R163_152) |
| Interchange of factors in full PC | `phase-170-.../R170_876` §0 | Exact symmetry of the causal hyperbola | It is not a symmetry of the first-contact operator. The interchanged causal extraction does not exist because PL_N^*P is not invertible (J3) |
| (ii) Differential operator commuting with the cutoff and the transform | `phase-186-toolbox/R186_003` rows 3–4; `R186_006` rows 1, 4, 9; `R186_007` §6; `phase-200-sign-object/SPEC_SIGN_OBJECT_011` (CS-0) | W_λ = −∂(λ²−x²)∂ + (2πλx)² commutes with P_λ and with 𝓕 (PROVED). Used as a spectral and test-function tool (prolates), and as a candidate to commute with P^S | NO-GO PROVED for S = {∞,2}: no function of the semilocal Hermite number added to −𝔰² commutes with P^S (003 row 4), and L + κX never commutes (006 row 4). Never used as an **operator bound dominating the remainders**. That use, however, falls into the classes of §1(b) |
| (iii) Oscillator or metaplectic representation combined with dilation by integers | R186_003 §5 (number N_S and ϖ(k) = πx² − ∂²/4π); R186_006 (W^{mp} with E g(u) = Σ g(2^k u)) | The oscillator was combined with dilation by 2: η_S = E, F_S = EF_∞E^{−1} | Commutation NO-GO (006 row 4). The «ladder» a, a* was never used as a B*B factorization of a_T. That factorization falls into BB* (J8; P1_BBSTAR_001) |
| Hypercontractivity and Bonami–Beckner | `phase-201-untried-families/FAMILIES_B_001.md` F10 | Inventory of the family | No mechanism for the comb |
| Exact theta, Bernoulli summation, nonlocal metrics | 211 `POWER_HYPERBOLIC_MODEL_GRAM.md` §§12.6–12.7; 106_109 §2; memory of the project rules | Theta realization (modular Poisson) of the Gram | Rejected at selection: a positive nonlocal kernel or a Green identity with controlled remainder is missing |
| Meta-ledger | `phase-200-sign-object/LEDGER_L5_META.md` C1 (l. 20) and l. 91 | «Poisson-ℤ» appears as a linear identity generic in the comb | thm:shape(A): survives cΛ and deletions |

Searches without relevant finding (grep over 03-research and 05-meta): «canonical commutation», Eisenbud,
«time delay» (appears only in the phase sense), Lax–Phillips (phase 64, adelic colligation, another object),
Segal–Bargmann (phase 4, another use) and co-Poisson (phase-209 LINK_011/016, Mellin–Gauss and dense range). A
search without textual matches does not prove conceptual novelty.

**Point-by-point answers.**
- (i) Yes. Beckner's identity with exact C_0 is in R160_C8_R1. The contact part as an anomaly between
  X, the sum operator S_N and Poisson is in R161_001 (PC). The line ended in R161_002 (blind square), in
  R161_042–044 (mixed Green without sign) and in K7, which remains open.
- (ii) As a commutation mechanism, yes, and it is NO-GO for S ≥ {∞,2}. As a dominating operator inequality, there
  is no memo. The class falls in any case into B2, B8 and W11′ (§1(b)).
- (iii) Yes, for dilation by 2 (R186_006), in commutation form. It is NO-GO.

## 1. Channel lemma (closes the brief in its general form)

**Lemma C (where additive covariance can enter; ARGUED, with two PROVED pieces).** In a_T the additive
structure of ℝ_x can only enter through three routes:

- (α) **The Tate–Beckner relation X + 𝓕X𝓕 = M**, which is the integrated version of the canonical
  commutation relation. It produces Arch and nothing of the comb. It is blind to the three checks (PROVED: it contains no weights).
  By Paper 47 cor:Tarch (CITED), every piece of this channel that bounds the contacts from above dies before
  T ≈ 0.60.
- (β) **Poisson on ℤ for the integer comb without weights.** It is identical under cΛ and under the deletion of a prime
  power (PROVED trivial: the lattice ℤ and the family {log n} do not change, only the weights). It only detects Beurling
  (R163_154 l. 83, CITED).
- (γ) **The coupling of (β) with Σ_{d|n}Λ(d) = log n.** It is the identity (PC) of R161_001. Its Thm. 4.1 gives the
  correct behaviour against the three checks at the level of the identity.

Consequence: the conjunction of the lead with Lemma A of ROUND_009_G2 points exactly to (γ), which is already
written and traversed. The ARGUED part is the exhaustiveness of the list; what supports it is that a_T is only
covariant under dilations (it is Toeplitz in t), and that the modulation e^{2πiyx} commutes with P_T but does not leave
the form invariant.

**First non-trivial case (contacts 2, 3, 4; T ∈ (log 2, ½log 5]); PROVED as a reading of R161_001 Thm. 4.1
with N, M_0 ≥ 4.** The interior defects are:
- cΛ with c = 2: δ(2) = log 2 at k = 2.
- Deletion of 4: δ(4) = −log 2 at k = 4.
- Beurling: the defect E_N changes operator, because the integer comb is missing.

All three are visible in the identity, but the sign is not: R161_002.

## 2. Candidates (four-point filter; none passes)

### (a) Ladder / number factorization: a_T + (named term ≥ 0) = ⟨F, B*B F⟩, with B built from X, ∂ and integer dilations

1. *Antecedent:* RULES_AVOID J8 and P1_BBSTAR_001 (BB* NO-GO PROVED in the convolutive class and term by term);
   R161_002 §1 (the canonical square of PC); R186_003 §5 (semilocal Hermite number).
2. *New:* B = Σ_n β_n n^{−1/2}τ_{log n}(X + i𝓕X𝓕) or variants, with coefficients β fixed by Poisson and by
   Λ∗1 = log.
3. *Why it would avoid the difficulty:* it does not, for two reasons.
   - If β is linear in Λ, B*B is quadratic in the comb: it is a «Λ∗Λ» sector without a compensating term, the
     class R3-b and K2 (oriented variance, generic).
   - If B is taken from PC, the square is ‖S_N A𝓕F‖², which sees A² (R161_002). The existence of B with B*B = a_T|_{P_T}
     is equivalent to a_T ⪰ 0 (J8: REF-D).
4. *Global connection:* none without an explicit B that does not come from factoring the form itself (J3).

**Breakdown under checks.** Does not apply: there is no object. For the PC square, cΛ produces another square ≥ 0, and the
breakdown is not in the remainder. **Repetition:** R161_002, K2, J8.

### (b) Dominating the Sonin remainders with a second-order differential operator commuting with the cutoff and the transform

1. *Antecedent:* R186_003 and R186_006 (W_λ, semilocal NO-GO); ANNEX_SONIN_READING §§1, 5 (the remainders K_s, C_p
   and κ_S, n₋(R) = ∞); Paper 47, Thm. P (phase 155: negative directions in ≤ 8 prolate modes).
2. *New:* the inequality −⟨g,K_s g⟩ − ⟨g,C_p g⟩ ≥ −Φ(W_λ) and Son + 2ε′𝔅 ≥ Φ(W_λ) on P_T, with explicit Φ.
3. *Why it would avoid the difficulty:* it does not.
   - The only known W commutes with P_λ and with 𝓕_∞, not with F_S (R186_006 row 4, PROVED). For the full
     form (S = S(T)) no local one exists.
   - A Φ(W_λ) is a multiplier in the prolate basis. The requested inequality is a linear certificate in a
     fixed basis (W-lin) or a norm or inertia bound of the remainder (W11′, R184_015 Thm. 2). Moreover it carries slack
     against a margin ≤ 4·10⁹Te^{−15.449T} (B2).
   - C_p is indefinite with ± spectrum of infinite multiplicity (R183_018 Prop. 4.1). Φ(W_λ) would have to
     absorb infinitely many negative directions with superexponentially small margin.
4. *Global connection:* only via «Son ≥ C_ε on P_T», which is the inertia N_T (OPEN, REF-D).

**Breakdown under checks.** Φ(W_λ) does not see the comb. With c = 2 the inequality fails, but because the remainder grows and
not because the sign of some piece changes (pattern B1/B2). **Class repetition:** W-lin, W11′, B2. Item 9 of
R186_006 («is there a second-order operator commuting with P^S and with P̂^S?») remains OPEN, but it is a
commutation question and not a sign question.

### (c) Mixed Bochner on the semiring: positive definiteness in the additive variable x combined with the multiplicative convolution of the contacts

1. *Antecedent:* 211 POWER_HYPERBOLIC_MODEL_GRAM §§12.6–12.7 (exact theta realization; a positive nonlocal kernel
   is missing); 106_109 §2 (summation by parts in theta, signed Bernoulli remainder); LEDGER_L5_META C1
   (Poisson-ℤ is linear in the comb); R163_154.
2. *New:* it would be a statement of the form a_T(F) = ∫ Q_F(y) dμ(y), with μ ≥ 0 a measure on the additive dual and
   Q_F(y) ≥ 0 built with e^{2πixy} and the contacts.
3. *Why it would avoid the difficulty:* it does not.
   - The comb only enters through Poisson-ℤ, channel (β), which is blind to cΛ and to deletions. To see them one must
     go through (γ).
   - Expressing a_T as a signed integral in the additive variable is the theta realization. Its recorded obstruction
     is precisely that the nonlocal kernel is not positive.
   - Bochner positivity in x of Σ v_n e^{2πi(log n)…} is positivity of the contact measure: PC branch 2,
     CPOS_CLASS_001.
4. *Global connection:* no new one.

**Breakdown under checks.** Under cΛ, μ remains positive, because it is the Poisson part and has no weights.
**Repetition:** memory of rejected selections («nonlocal metrics», «summation by parts in theta») and channel
(β) of Lemma C.

### (d) Others

The two variants of additive covariance are covered by Lemma C, each in its channel:
- the canonical commutation relation as a Green identity ([X, ·] on E and C) falls into (γ) and into R161_042–044;
- the kernel e^{2πixy} as an intertwiner of the sum S_N falls into (β)/(γ) and into R161_040.

I find no other defensible route.

## 3. Precise residue (the best of the three)

The only point of this line not closed by a NO-GO is RULES_AVOID K7, open:

  SP-161 / L161.1 (R161_002 §§4–5):
    a_T = Σ_N w_N Re⟨RF, S_N𝓕F⟩ + leakage squares of C_T = (1−P_T)𝓕P_T, on all of P_T.

Only the branch w_N ≥ 0 died (R161_002 Thm. 8.1). Signed weights, or discrete derivatives in N, were not
written.

**Missing operation.** An explicit signed sequence w_N, not taken from an optimizer, is needed that satisfies
two things. First, that Σ w_N H_{M,N} cancel the positive hyperbola remainder h(k) = Σ_{dm=k, d≤M, m≤N} Λ(d) for
k > e^{2T}; a finite difference in N is a natural candidate, because h is monotone in N. Second, that the resulting
Poisson term, Σ w_N E_N, be oriented: that it be an exterior leakage ‖(1−P_T)·‖² and not a support
commutator [P,S].

This is the «identity connecting a leakage square with the PC defect» that the reopening of K1 requires. The
additive covariance enters through E_N; the multiplicative one, through h(k). Under cΛ the interior cancellation would fail at k = 2
by δ = log 2 (R161_001 Thm. 4.1); under Beurling E_N is missing. I do not propose it as a candidate because I do not have the
w_N, and announcing it without them would repeat K7.

## 4. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | The lead «additive covariance + Λ∗1 = log» is the content of R161_001 (PC) plus R160_C8_R1 (Tate–Beckner) | CITED (primary-source reading) |
| 2 | Arch is the logarithmic uncertainty with exact constant C_0 = ψ(¼) − log π | CITED (R160_C8_R1 Cor. 2.4) |
| 3 | The canonical PC square is blind to the sign | CITED (R161_002) |
| 4 | The mixed E–C Green leaves pieces without sign; the Tate correction vanishes by parity | CITED (R161_042–044) |
| 5 | The commuting prolate operator does not exist in local form for S ⊇ {∞,2} | CITED (R186_003 row 4, R186_006 row 4) |
| 6 | Oscillator plus dilation by 2: commutation NO-GO | CITED (R186_006) |
| 7 | Lemma C, piece (α): the Tate–Beckner relation contains no weights | PROVED (trivial) |
| 8 | Lemma C, piece (β): weightless Poisson-ℤ is invariant under cΛ and under deletions | PROVED (trivial) |
| 9 | Lemma C, exhaustiveness of the three channels | ARGUED |
| 10 | Interior defects in the case 2, 3, 4: log 2 at k = 2 (c = 2), −log 2 at k = 4 (deletion of 4) | PROVED (reading of R161_001 Thm. 4.1) |
| 11 | (a) repeats R161_002, K2 and J8 | ARGUED (cross-check) |
| 12 | (b) falls into W-lin, W11′ and B2 | ARGUED (cross-check) |
| 13 | (c) repeats the selection of nonlocal metrics and that of theta, and falls into channel (β) | ARGUED (cross-check) |
| 14 | Residue: K7, signed weights w_N in SP-161 | OPEN |
| 15 | Global sign of a_T | OPEN |
