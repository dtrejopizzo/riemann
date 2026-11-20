# Round 8, item A — the boundary concomitant that would convert the product channel into the ratio channel

Phase notation: a_T(F) = Arch(F) − Σ_n v_n c_F(log n), F real, supp F ⊂ [−T,T], F ∈ P_T.

## 0. Preliminary step: was the requirement of R161_034 §0 attempted after it was written?

Yes. It was carried out and closed within phase 161 itself. Primary-source reading:

- `phase-161-row-d-sum-product-square/R161_034_MELLIN_GRAM_AND_PRODUCT_RATIO_COLLISION.md` §§0–7. The symbol of
  each atom is q_k(τ) = k^{−s}u_∞(τ) − k^{−(1−s)} (1.3). The cross Gram splits into a ratio channel
  cos(τ log(k/l)) and a product channel Re{u_∞(τ)e^{−iτ log kl}} (3.2). On the full line there is no cancellation
  (§4, ARGUED). The candidate it leaves is the compressed coherent leakage L_{N,T} = ‖(I−P)Σ(log k)d_kPF‖² (5.2), which
  involves the commutator [P,d_k] (5.1). u_∞ is exactly the interchange of orientations ξ ↔ −ξ.
- `R161_035` builds the requested object in its strongest form. With U_N = K_N𝓕 and V_N = JK_N (the two
  orientations, previously synthesized via Λ∗1 = log, (4.1)), the parallelogram identity gives
  D_N^coh = ¼‖(U_N − V_N)f‖² ≥ 0 (3.2), keeping all of the Gram k/l and kl. The boundary component is
  ¼‖(I−P)(U_N−V_N)f‖² (5.1). What is missing is saturation (5.2)–(5.3).
- `R161_037`: if there is saturation, then F = 0. `R161_038`: an exact 2×2 countermodel satisfies (PC),
  radicality and parity without saturating. `R161_039`: terminal equivalence; a physical Green identity is missing
  (3.1).
- `R161_057`–`R161_065`: the «support concomitant / Hermitian power / Lagrangian» family. R161_065 (1.2)
  proves that the candidate concomitant is K_P(S;g,w) = ⟨g,[P,S]w⟩, i.e. the already audited support
  commutator, which is indefinite. R161_064 (4.2), which expanded it as a sum of nonnegative energies, is withdrawn.
  According to R161_065 §4, what is missing is an exterior arithmetic theorem, e.g. Re⟨g, P_R C_log g + εg⟩ = 0.
- `R161_050`: a three-block countermodel shows that central cancellation, self-adjoint unitarity and
  scattering parity do not transfer the sign to the exterior.
- `R161_075` and `R161_081` treat the domain of the multiplier and the test Q ≥ 0, which is excluded in the primitive
  space. Neither reopens the above.
- Routes index (`04_PHASES_100-189.md`, lines 746, 763, 769): G1C-R161_061-065 DEAD (concomitant = support
  commutator); G4C-R161_035-038 PARTIAL; G8B-161 R161_037-039 DEAD (2×2 countermodel). README l. 2457 records the
  countermodels 038/050. RULES_AVOID §Q3 and REVIEW_007 R7-c record the repetition of round 7.
- 211 «Extensión factorial» and 106_109 (§2, (9)–(10)) already appear in the memory of rejected selections. They
  contain no compressed version of the concomitant different from the above.

**Verdict of step 0: repetition.** The operation «compressed product channel = compressed ratio
channel + boundary concomitant with a sign» was executed in R161_035 (with a sign, thanks to the parallelogram) and in
R161_057–065 (the concomitant is computed and turns out to be [P,S], without sign). It was closed in two ways: the countermodel
R161_038/050 and the reduction R161_065 (1.2). In accordance with the rule, **the construction stops here**. The
following sections derive nothing new. They only fix, with the formulas of the brief, where the sign remains and which
hypothesis of the closure is not forced.

## 1. Four-point filter (written after step 0)

1. **Antecedent:** R161_035 §§3–5 and R161_065 §§1–4, with the countermodels R161_038 and R161_050.
2. **New object:** none. The «compressed ratio channel + concomitant» is D_N^coh of R161_035, and the
   concomitant is ⟨g,[P,S]w⟩ of R161_065.
3. **Avoidance of the difficulty:** it does not avoid it. The sign remains in saturation (R161_039 (2.1)), or else in the
   indefinite commutator.
4. **Global connection:** the only existing one is that of R161_037–039: saturation ⇒ absence of a first-contact
   state ⇒ a_T ≥ 0 on P_T for all T, via the nesting theorems. That implication is CITED;
   saturation remains OPEN.

It does not pass the gate.

## 2. Precision on (a)–(d) without new derivation

**(a) Statement.** With u_∞ as in R161_034 (1.1), the full operator of one orientation is τ_{log k}𝓕 and that of
the other is Jτ_{log k}. Reflection enters through J: for F real, F̂(−ξ) = conj F̂(ξ). In Mellin, A(ξ)A(ξ) versus
A(ξ)A(−ξ) is exactly «opposite orientations» versus «same» ((3.1) of 034). u_∞ is the only factor that
links ξ with −ξ in the full weight. Compressed to the window:

- compressed ratio channel = ‖P(U_N+V_N)Pf‖² and ‖P U_N P f‖² + ‖P V_N P f‖²;
- compressed product channel = Re⟨PU_NPf, PV_NPf⟩.

(PROVED as a rewriting of R161_035 (3.1)–(3.2).)

**(b) Difference.** Product minus ratio is −¼‖(U_N−V_N)f‖² plus the boundary term that separates the compressed
version from the full version. That term is exactly ⟨f,[P,·]f⟩ (R161_065 (1.2)–(1.3)). The bulk part
is the square of the parallelogram. Neither as T → ∞ nor under the two moment restrictions (F ∈ P_T) does the boundary
term acquire a sign: R161_064 (4.2) was withdrawn. (CITED.)

**(c) a_T of degree one.** The objects of 035 are quadratic in the operator K_N, which is linear in Λ ∗ 1 = log, and
hence of degree two in the synthesis. a_T only appears through linear radicality (PC-ren). The passage from the
degree-two statement (saturation) to a_T ≥ 0 exists, but it is indirect: by contradiction on a first-contact
state and by R161_037 (CITED). By R161_038, no statement that uses only (PC) + radicality + parity
forces the degree-two object. (PROVED in the formal 2×2 class. Outside it: OPEN.)

**(d) Term with a sign and checks.** The only term with a manifest sign is ¼‖(U_N−V_N)f‖². That term is
≥ 0 for every weight, also with c = 2, with a deleted prime power and with a Beurling weight. It is blind, and
does not break: it is pattern J2/L3. The term that should break is saturation, or the commutator [P,S]. Neither
has a sign in the corpus, so there is no named sign that is lost. (ARGUED.)

## 3. The hypothesis of the closure that is not forced

The countermodels R161_038 (2×2) and R161_050 (3×3) refute only the **purely algebraic** transfer. R161_050 says
so explicitly: «does not reproduce the integer translation semigroup, the explicit zeta product port, or
the Gamma/Tate collars». The unforced hypothesis of the closure is, therefore, this:

> that saturation (or the sign of the concomitant [P,S]) must be deduced without using the semigroup law
> τ_{log k}τ_{log l} = τ_{log kl} on ℕ coupled to the compression P_T.

In the finite models S is nilpotent or a permutation, without multiplicative integer structure. To reopen
one would need a statement that uses that law inside the commutator, of the form [P,τ_{log kl}] = [P,τ_{log k}]τ_{log l}
+ τ_{log k}[P,τ_{log l}] (Leibniz rule of the commutator, PROVED trivially). Moreover, it would have to be summed with
weights Λ∗Λ, and not only with Λ∗1. That statement would have to produce a square and not an indefinite form. It is not
built here. Beforehand it would have to be cross-checked with R161_045 (local Toeplitz–Hankel) and with the transport family
of the memory of rejected selections.

## 4. List of claims

| # | Claim | Label |
|---|---|---|
| 1 | The requirement of R161_034 §0 was executed in R161_035 and R161_057–065 and closed | CITED (primary-source reading) |
| 2 | Candidate concomitant = ⟨g,[P,S]w⟩, indefinite | CITED (R161_065 (1.2)) |
| 3 | Saturation does not follow from (PC) + radicality + parity | CITED (R161_038, R161_050) |
| 4 | This round: repetition; the construction stops | NO-GO (repetition) |
| 5 | (a)–(b) as a rewriting of the parallelogram of 035 | PROVED (rewriting) |
| 6 | The term with a sign is blind to the weight (c = 2, deletion, Beurling) | ARGUED |
| 7 | Unforced hypothesis: absence of the semigroup law of ℕ in the countermodels | ARGUED |
| 8 | Leibniz rule of the commutator on τ_{log kl} | PROVED (trivial) |
| 9 | That this rule gives a square | OPEN |
| 10 | Global sign | OPEN |
