# Round 3, option 6 — Joint conversion of the finite Poisson–Chebyshev identity without recombining (selection memo)

Selection memo, not a construction memo. Goal (★): λ_A(T) ≥ 0 for every T, with the definitions of
`../phase-211-sign-sandbox/STATEMENT_001.md`; N ≥ e^{2T}, M ≥ N. Notation of P47 §sec:firstcontact
(`04-papers/47-row-d-dual-certificates/main.tex`: S_N, S′_N, L_M, A_M = 𝓜 − L_M − L_M*, E_N = S_N𝓕 − JS_N,
H_{M,N} = L_MS_N − S′_N, thm:PCfinite). Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO /
NUMERICAL.

Question: can the interior block k ≤ N (annihilated by Σ_{d|k}Λ(d) = log k) be kept separate from the
exterior one, so that the sum (tail H_{M,N} + block of E_N + Tate) is an explicit Hermitian form
on P_T with legible sign, using the interior cancellation as input to an inequality?

## Cross-check

Searches done (grep by keyword and synonyms, then primary reading of what was found):
«envelope / envolvente / infimum over / supremum over / F-dependent test / test dependiente» in
phases 161, 162, 170, 182, 211, 212, the grid and the index (hits only in unrelated uses: envelopes
of symbols and of certificates in 211 and 162, none on the parameters (M, N, L, δ) of thm:PCfinite);
«(c − 1) / c > 1» in phase 170 (no hits); «Möbius inverse / causal Möbius / M_N S_N» in
161, 162, 170, 182, 211 and P47 (hits in R170_853–858, 860, 878, 883 and R161_066). Read in
primary: P47 l. 6625–6946 (thm:PCfinite, eq:Gammaenergy, eq:collar, eq:Qbalance, eq:Qrecombine,
eq:Qspectral, prop:GEgap, eq:equivgate, prob:annihilate, rem:returnremarks); `R170_816` §§1–2;
`R170_819`, `820`, `821`, `835`, `838`, `856`, `900` in their setup and verdict; `R170_837` §§5–6
in full; `R170_840` §§0–2; `R170_878` §0; `R161_033` §§5–8; `ROUND_002_A`, `REVIEW_002_A`, `LEDGER`.
Not opened in primary: `R162_405`–`408` nor `R182_201` beyond their title; what is said about them
below comes from `R170_840` §2, which cites `R162_406`. A search without hits does not prove
novelty.

### (1) Closest antecedent

**`R170_837` §6, equations (6.1)–(6.10)** (read in primary). It is the question of this memo, written:
for a weight a, H^a_{M,N} = 𝒟_a^{≤N} + H^{a,>N}_{M,N} with 𝒟_a^{≤N} = Σ_{k≤N} δ_a(k)k^{−1/2}τ_{log k},
δ_a(k) = Σ_{d|k}a(d) − log k (6.2)–(6.4); the interior defect enters PC as −J𝒟_a^{≤N} − 𝒟_a^{≤N}𝓕
(6.5); after substituting S′_N = L_M^aS_N − H^a_{M,N} the mixed form is **independent of a** (6.7); and
«the arithmetic only carries if the projection of interior coefficients (6.8) is used **before** (6.6)
… a form meeting the requirement must use (6.8) to transform a residue, not merely rewrite
(6.6)». The monitor (6.9) vanishes for Λ (6.10) and «gives no sign when it is zero».

**`R170_840` §0** (read in primary): NO-GO with class PROVED in phase 170 for two-sided
expressions formed with (1) the minimality identity between windows, (2) the two orientations of the
collar and J, (3) **finite PC, raw or renormalized, before or after the cancellation Λ∗1 = log**,
(4) the compressed Chebyshev identity, (5) the detector R_L, the Gamma–Euler collar and the
Schur/Feshbach of `R162_408`: every such expression has the normal form (0.1)/(0.3), and «(0.4) eliminates
a block of coefficients, but orients none of the three terms». The minimal datum they propose
(0.5) is a two-sided virial law that «must be obtained before recombining PC and use (0.4)
essentially»; OPEN, without object.

**`R161_033` §5**: the two OPEN exits it leaves on withdrawing the discrete realization are
**A. isometric source dilation** (an explicit isometry V_N from additive
Poisson/Fourier data whose physical synthesis is the coherent port of (PC-ren)) and **B. exact compensation
of the cross Gram** I_N(f) = Σ_{k≠l}(log k)(log l)(kl)^{−1/2}Re⟨Δ_kf, Δ_lf⟩ by the polar/Gamma terms
and Tate terms oriented by parity. B was taken up by `R161_034` (it identifies the cross Gram with the
product–quotient channel of phase 106; index row DEAD: it does not cancel with the rank-two Tate in the
translation-invariant algebra). A has no object in the corpus consulted (ARGUED: search, not
proof).

**Möbius test**: `R170_853` and `R170_878` (0.1)–(0.4) already invert the compression of S_N* by the
Möbius comb, (PS_N*P)^{−1} = PM*P for N ≥ e^{2T}, and obtain an exterior Möbius loop. The test
used below in §(4) is that same inversion, in the truncated variant.

### (2) Genuinely new object

There is no object (ℋ_T, V_T, ρ_T). What this memo writes is:

(a) an exact identity on all of P_T, with an explicit non-local test, that expresses a_T(F) through the
blocks of thm:PCfinite without recombining (identity (4.3)); its content is not new (it is the Möbius
inversion of `R170_878` applied to thm:PCfinite) and is written only to fix the blocks;

(b) a short lemma, PROVED, of blindness to the weight of the separated blocks (Lemma 1 and Corollary 2 of §(4)):
along the family cΛ, each separated block is independent of c or exactly proportional to c,
and the only written quantity that separates c = 1 from c ≠ 1 is (c − 1) times a form that, as a
quadratic form on P_T, is b_T(F) minus exterior blocks (Lemma 3). Consequence: every positively
homogeneous property of the separated exterior block —its sign, that of any envelope in
(M, N, L, δ), that of its limit L → ∞, that of its evaluation with a test chosen according to F without using the weight,
its writing as Σ h(k)|ℓ_k|² + ρ— is the same for every c > 0. This closes, against the falsifier
cΛ, three of the operations that `REVIEW_002_A` §5.2 (points 1, 4 and 6) left unexamined, in the class
declared in Corollary 2. It contributes no sign.

What remains to be written for a candidate: a form Ψ on P_T, built with the blocks of (4.3),
that is not affine in the weight (for example, with a test depending on the values of the weight), whose
equality with a_T uses δ_Λ = 0 in a term of degree ≥ 2 in the weight, and that is manifestly ≥ 0.
None of this is written, neither here nor in the corpus consulted.

### (3) Does it avoid the difficulty of the antecedent?

No. The difficulty of `R170_837` (6.7) is that, recombined, the form forgets the weight; that of
`R170_840` is that, before or after the cancellation, (0.4) only erases a block. Lemma 1 shows
that **not recombining does not change that situation** for the listed operations: the separated blocks
are affine in the weight, the interior block appears with coefficient (c − 1) in front of a fixed form, and
the cancellation at c = 1 can only act as the erasure of a term of an affine identity. Using it as
input to an inequality requires an operation non-affine in the weight, which this memo does not have.

### (4) Identity connecting with the complete form on P_T

We work on the dense subspace of P_T of smooth functions supported in I_T = [−T, T]; the
extension to all of P_T is the usual one of the form domain (CONDITIONAL on the continuity of each
block in the graph norm, which is not verified here). Conventions of P47: V_{−log n}F(t) = F(t + log n),
𝓕* = 𝓕^{−1} = 𝓕.

**Step 1 (PROVED).** For F supported in I_T and M ≥ N ≥ e^{2T},

    a_T(F) = Re⟨A_MF, F⟩.                                                      (4.1)

The terms of L_M with log d ≥ 2T translate the support outside I_T and do not pair; the remaining ones are
those of B_N + B_N* (P47 §subsec:collars).

**Step 2: the truncated Möbius test (PROVED).** Let M_N = Σ_{n≤N} μ(n)n^{−1/2}V_{−log n}. The translates
commute with each other, with 𝓜 and with L_M, L_M*. One has

    M_NS_N = I + U_N,    U_N = Σ_{N<k≤N²} c_N(k) k^{−1/2}V_{−log k},
    c_N(k) = Σ_{d|k, d≤N, k/d≤N} μ(d),

because for 1 < k ≤ N all divisors appear and Σ_{d|k}μ(d) = 0. Therefore

    Re⟨S_NA_MF, M_N*F⟩ = Re⟨M_NS_NA_MF, F⟩ = a_T(F) + R(F),                   (4.2)
    R(F) = Σ_{N<k≤N²} c_N(k)k^{−1/2} Re[ ⟨𝓜V_{−log k}F, F⟩
             − Σ_{d≤M, |log(k/d)|<2T} Λ(d)d^{−1/2}⟨V_{log d−log k}F, F⟩ ].

In R(F), V_{−log k}F has support in I_T − log k, disjoint from I_T (log k > 2T); the L_M term does not pair;
the L_M* term pairs only if |log(k/d)| < 2T: R sees exactly the near-coincidences d ≈ k with
k ∈ (N, N²] and d a prime power ≤ M, with Möbius weights c_N(k) without sign, plus the non-local part of
𝓜 between I_T and its translate.

**Step 3: substitution of PC (PROVED on the Schwartz core; CONDITIONAL on the form domain).**
Applying thm:PCfinite to 𝓕F and using 𝓕² = I:

    a_T(F) = Re⟨({X, E_N} − L_M*E_N − JH_{M,N} − H_{M,N}𝓕)𝓕F, M_N*F⟩ − R(F).   (4.3)

Answer to «which test»: the theorem is paired with a test, and the requested identity on all of P_T requires
a non-local one. That of R170_816 is z = S_N𝓕Σ_LF and connects with a_T only on the radical (eq:Qbalance,
eq:Qrecombine). That of (4.3) is M_N*F with the variable shifted to 𝓕F; **z = F has no exact
per-window substitute**: the exact substitute (truncated Möbius) costs the remainder R(F), which is another
exterior tail k > N, with coefficients c_N(k) of variable sign. On all of P_T no Tate vector appears:
the Tate comes from the weak equation of the radical and enters only in the eq:Qbalance version.

**Hermitian form that remains without recombining.** With F ∈ P_T,

    f_0(F) = Re⟨{X, E_N}𝓕F, M_N*F⟩                         (Poisson block; does not see the weight)
    f_1(F) = Re⟨(L_M*E_N + JH_{M,N} + H_{M,N}𝓕)𝓕F, M_N*F⟩  (polar of E_N and tail k > N)
    g(F)   = Re⟨(JS′_N + S′_N𝓕)𝓕F, M_N*F⟩                  (interior Chebyshev jet)
    R(F) = R_0(F) − R_1(F)                                  (𝓜 part and primes part of (4.2))

(4.3) says a_T = f_0 − f_1 − R_0 + R_1. Each of the five is an explicit Hermitian form on
P_T; none has a known sign.

**Lemma 1 (affine blindness, PROVED).** For the weight cΛ, c real, with a_T^{(c)} the form with cΛ instead
of Λ, and all other data fixed,

    a_T^{(c)}(F) = f_0(F) − c f_1(F) − (c − 1) g(F) − R_0(F) + c R_1(F)    for every F ∈ P_T,   (4.4)

with f_0, f_1, g, R_0, R_1 the forms above, which do not depend on c.

*Proof.* L_M^{cΛ} = cL_M, hence H^{cΛ}_{M,N} = cL_MS_N − S′_N = cH_{M,N} + (c − 1)S′_N, and
A_M^{(c)} = 𝓜 − c(L_M + L_M*). E_N, X, 𝓕, S_N, S′_N, M_N do not depend on the weight. The proof of
thm:PCfinite does not use the values of the weight (only [X,S_N] = −S′_N and the Fourier identities), hence
S_NA_M^{(c)}𝓕 = {X,E_N} − cL_M*E_N − JH^{cΛ} − H^{cΛ}𝓕. Steps 1–2 hold for A_M^{(c)} with R^{(c)} =
R_0 − cR_1. Substituting gives (4.4). ∎

**Corollary 2 (NO-GO with class against cΛ, PROVED).** Class 𝒞_sep: sign statements about the
separated exterior block f_1 (tail k > N plus polar L_M*E_N), or about its components (the tail alone, the
polar alone, or Σ_{k>N}h(k)|ℓ_k|² + ρ as a writing of the tail), obtained by any of these
operations: (i) evaluation with any test, including F-dependent ones, provided its choice does not
use the values of the weight; (ii) infimum, supremum or average with positive measure over (M, N, L, δ, test);
(iii) limit L → ∞ or M → ∞ when it exists; (iv) multiplication by positive functions of F. Every
statement of 𝒞_sep holds for cΛ with some c > 0 if and only if it holds for every c > 0. In particular none
can break at c ≠ 1 (clause O4), not even combined with f_0, which does not see the weight.

*Proof.* By Lemma 1, f_1^{(c)} = c f_1 (and each component is multiplied by c: the tail has
coefficients c·h_{M,N}(k), the polar −cL_M*E_N). The operations (i)–(iv) commute with multiplication
by c > 0 and preserve the sign. ∎

The same holds, word for word, for the exterior remainder R_1 of (4.2). For the block f_0 the
statement is stronger: it depends on no weight (only on the integer comb of S_N and on 𝓕), hence it
also survives a_P, finite erasures and amplifications and every system with the same S_N.

**Lemma 3 (what separates c = 1 from c ≠ 1, PROVED).** With b_T(F) = Re⟨(L_M + L_M*)F, F⟩ the primes form
of a_T,

    g(F) = b_T(F) − f_1(F) + R_1(F)    on P_T.                                  (4.5)

*Proof.* (4.4) at c = 0 and c = 1 gives m_T = f_0 + g − R_0 and a_T = f_0 − f_1 − R_0 + R_1; subtract and
use a_T = m_T − b_T. ∎

Consequence: in (4.4) the difference between c and 1 is a_T^{(c)} − a_T = −(c − 1)b_T(F), as it should be; the
interior cancellation contributes nothing other than the term (c − 1)g which, by (4.5), is reabsorbed into b_T with
the exterior blocks. The written quantity that distinguishes c > 1 from c = 1 is (c − 1)b_T(F); for
an inequality to use it one would need to control b_T(F) with zero margin against f_0 − R_0, which is (★)
itself. **No quantity written in the corpus consulted distinguishes c > 1 from c = 1 by other means**
(ARGUED: search result). Since the form is affine in the comb (OBJECT_SPEC O2), every quantity
that is affine in the weight has the same defect; one that distinguishes it by itself must be of
degree ≥ 2 in the weight, of the type (c − 1)²‖v‖² or c(c − 1)X, and vanish at c = 1 by δ_Λ = 0. None
is written.

**What operation could give the sign.** The three of the question, on the separated blocks: the
envelope in (M, N, L, δ) and the limit L → ∞ fall into 𝒞_sep if applied to the exterior block alone; the
choice of an F-dependent test falls into 𝒞_sep if it does not use the weight. Applied to the complete sum
f_0 − f_1 − R_0 + R_1 they are not excluded, but that sum is a_T(F) by (4.3) for every value of the
parameters: its envelope in (M, N, L, δ) is a_T(F) itself (the parameters do not appear on the left
side), and there is nothing to optimize. The only thing (4.3) lets vary is the distribution among blocks.

### (5) Lines that break for cΛ and a_P

- **cΛ, c ≠ 1.** In (4.3) the term −(c − 1)g(F) appears (Lemma 1). Any sign writing that
  uses only f_1 or R_1 separately does not break (Corollary 2): it survives cΛ and, therefore, is wrong as a
  sign step. A writing that uses the complete sum breaks only through the term (c − 1)b_T(F) of
  Lemma 3, that is, through the recombination.
- **a_P with P > N.** L_M^{a_P} contains no d < P, so that inside the window a_T^{(a_P)} = m_T and
  H^{a_P}_{M,N} = −S′_N + (tail with d ≥ P). In (4.3) the line that changes is the interior block:
  −Re⟨(J𝒟 + 𝒟𝓕)𝓕F, M_N*F⟩ appears with 𝒟 = 𝒟_{a_P}^{≤N} = −S′_N (for P > N, δ_{a_P}(k) = −log k at every
  k ≤ N), that is, the whole term +g(F); the exterior tail loses all terms with d < P and
  is not proportional to that of Λ, so Corollary 2 does not apply to a_P. The cancellation of the interior
  block is what breaks. f_0 does not change: the Poisson block survives a_P, as it does every
  falsifier with the same integer comb.

## Result

Repetition in essence, plus a short NO-GO with class. The question —using the interior cancellation before
recombining, as input and not as cancellation— is posed literally in `R170_837` §6
(6.8)–(6.9) and closed for two-sided expressions in the class of `R170_840` §0; the Möbius test that
gives an identity on all of P_T is in `R170_853`/`R170_878`. No new mechanism for the sign. There
is no candidate ready for construction.

## What was proved

1. (4.1)–(4.3), PROVED on the smooth core (CONDITIONAL on the form domain): a_T expressed on
   all of P_T through the blocks of thm:PCfinite without recombining, with the test M_N*F and the remainder R(F) of
   near-coincidences d ≈ k, k ∈ (N, N²], with Möbius weights. Content not new (`R170_878`).
2. Lemma 1, PROVED: along cΛ the separated blocks are independent of c or proportional to
   c; the interior enters with coefficient (c − 1).
3. Corollary 2, NO-GO with class 𝒞_sep, PROVED: no sign statement about the separated exterior block
   obtained by a weight-independent test, envelope or positive average over (M, N, L, δ,
   test), limit L → ∞ or positive rescaling breaks at c ≠ 1.
4. Lemma 3, PROVED: the interior form g is b_T − f_1 + R_1; the only written quantity that separates c = 1
   from c ≠ 1 is (c − 1)b_T.
5. The two exits of `R161_033`: A (isometric source dilation) without object in the corpus
   consulted; B (compensation of the cross Gram) taken up by `R161_034`, DEAD in the index.

## What failed and why

- The separation gives no sign because the identity is affine in the weight: the interior block is an
  erased term of an affine identity (Lemma 1), not an equation that can be used to orient another term.
- The envelope in the parameters is trivial on the complete sum (it equals a_T for every parameter) and
  blind to the weight on the separated exterior block (Corollary 2).
- z = F has no exact per-window substitute; the Möbius one costs another exterior tail R(F) without sign.

NOT excluded (delimitation; none of this has a written object):
1. tests or functionals that use the **values of the weight** (for example, built with L_M or with Λ on
   [2, N)), which make the blocks non-affine in c and allow δ_Λ = 0 to annihilate a term of degree ≥ 2
   in the weight; it is the only path this memo leaves open for «cancellation as input», and it must pass
   OBJECT_SPEC O2 (non-linearity in how V_T acts on F, not only in products of weights);
2. operations non-linear in F applied to the complete sum with an F-dependent distribution among blocks
   (Corollary 2 only covers the exterior block alone);
3. the two-sided virial law (0.5) of `R170_840`, OPEN, and exit A of `R161_033`;
4. the remainder R(F) of (4.2) as an object in its own right: it is an explicit form of near-coincidences d ≈ k
   (clause O6) with Möbius weights; its sign was not examined;
5. a_P and the falsifiers not proportional to Λ: Corollary 2 does not cover them.

## Concrete next step

Do not build on this zone without a test depending on the values of the weight and a term of degree
≥ 2 in the weight written explicitly (point 1 of the list). Record in the index and in the grid: «Phase
212, joint PC conversion without recombining: repetition of `R170_837` §6 and `R170_840` §0; NO-GO with
class 𝒞_sep PROVED (`ROUND_003_6` Corollary 2): without a weight-dependent test, envelopes, limits and
F-dependent tests on the separated exterior block are blind to cΛ; Lemma 3: the interior cancellation
is reabsorbed into (c − 1)b_T. Global sign OPEN.» Before recording it, a second reader must
verify (4.2) (sign and range of c_N(k), support of R) and Corollary 2.
