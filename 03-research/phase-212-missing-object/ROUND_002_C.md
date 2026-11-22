# Round 002 C — The two-prime-base channel: selection memo

Notation of `../phase-211-sign-sandbox/STATEMENT_001.md`; N = e^{2T}; ℓ_p = log p. Goal (★):
λ_A(T) ≥ 0 for every T, as the sign of the form a_T on P_T. This memo is a selection memo: it does not derive
beyond what is needed to state the five points of the cross-check.

Candidate. In γ_Λ = μ∗β_Λ = Λ·log − Λ∗Λ (values: ℓ_p² at p^k; −2ℓ_pℓ_q at p^a q^b, p ≠ q; 0 if
ω(n) ≥ 3) the channel −2ℓ_pℓ_q «suggests a square in the lattice of prime bases» (R170_850 §5). Question:
is there an explicit square in F, indexed by pairs (p,q) or by the exponent lattice, whose
expansion gives that cross term with the correct orientation and diagonals that a_T contains, and that
is none of the five cases already closed?

**Cross-check verdict: repetition. No new mechanism.** The memo ends at the cross-check.

## Cross-check

### (1) Closest antecedents (primary sources read)

a. `phase-170-global-prime-inequality/R170_850` §§0, 4, 5 (law (0.2), extracted form (4.2),
   completion «not claimed»); `R170_851` §§0–2 (γ = Λ·log − Λ∗Λ; with W = μ∗log² it returns to the
   pairing without sign); `R170_841` §§4.1–4.3 (β_Λ(12) < 0; even Cauchy–Schwarz versus odd first
   moment; Möbius deconvolution returns to the same point); `R170_854` §3 equation (3.4) and
   §6.3 (every completion by squares of the graded current keeps an indefinite metric;
   squaring the sector gives a ratio-comb or an indefinite supertrace); `R170_855`–`R170_856` §§3–4 (γ + W =
   2Λ·log is a branch sub-identity; in the complete Poisson–Chebyshev identity W cancels
   term by term with the −W of the Poisson block). All CITED.
b. `phase-162-row-d-first-contact-closure/R162_501` Prop. 3.1(a) (PROVED there): positivity of
   coefficients on log ℕ gives no sign to the pairing with c_F′(log n).
c. `phase-70-lee-yang-dbn/E70_10` (Dirichlet square (I−V)*(I−V) = I − T_Λ + V*V; V*V lives on
   the comb of quotients log(n/m) with coefficients ≥ 0 and divergent mass) and `E70_11`–`E70_12`
   (Selberg = Riccati of V = Z⁻¹δZ). `phase-166-omega-closure/R166_502` §5.2 (PROVED there): the Hermitian
   square V*V and the convolution square V² differ, pair of primes by pair of primes, in
   S_{log q^l} ↦ S*_{log q^l}, that is products p^k q^l ↦ quotients p^k/q^l; the non-integer part of
   V*V is exactly Σ_{p≠q} V_p*V_q; Selberg rewrites V², not V*V; «the cancellation would have to come
   from a second sector with sign». **This is the literal antecedent of the candidate**: the «square
   in the lattice of prime bases» is the cross sum Σ_{p≠q}, and what it produces is already written.
d. `phase-204-refd-tractability/P1_BBSTAR_001`: Theorem P1.A (PROVED there: P46 thm:sos holds for
   Dirichlet polynomials with arbitrary real frequencies, including dilations with weights Λ,
   Λ₂, μ, log; there is no convolutive B for T ≥ ½log3), Lemma 2.7 (every decomposition 𝒲 = α𝒞*𝒞 + R
   forces in R atoms −αℓ_pℓ_q/√(pq) at ±log(p/q)) and §2.8 («Selberg enters in 𝒞², not in 𝒞*𝒞»).
e. `phase-211-sign-sandbox/ROUND_005_A` Lemma 3.2 and Prop. 3.3 (PROVED there): in the window,
   ⟨F,Π²F⟩ = [product comb with Λ∗Λ, indefinite] + [mean of the Dirichlet polynomial, ≥ 0,
   quotients] − ‖𝔏F‖² [leakage]; §5.3: (R) and (L) are generic in the comb and nearly cancel; the
   Λ∗Λ content is the minor part and without sign. `ROUND_023_A` Lemma 2.1 (Selberg in operator form,
   Φ(Λ·log) = [M,P] = 𝔇⁻¹[M,[M,𝔇]] − P²) with the «do not retry» of P211-23A.
f. `phase-186-toolbox/R186_005` Lemma S0 and Thm. TB3-neg (PROVED there): the degree-two identity
   holds for every weight b with its own system; the only specific thing is N_b ≡ 1.
g. Index: `ROUTES-TRIED-INDEX/04_PHASES_100-189.md` rows G6C-R162_501, G6C-R162_2301,
   G6C-R166_502, G4C phase-36/107 («the prime×prime block enters with plus sign»), G4C phase-70/E70_10;
   README l.541 (R11_2_ORIGIN: «Selberg Λ∗Λ order 2 NO-GO»), l.596 (P1_BBSTAR), l.651 (node:
   Selberg = retry without new reason), l.1087 (P211-5A). Grid: cell 6C (R162_501 tool;
   R162_2301, R166_502 closed). Crossword: l.516, l.622, l.1594–1598 (Potencias067). Paper 48:
   row «Selberg difference channel» of the routes table (no-go). `RULES_AVOID.md` B1, D17b, I2, I8.
   Phase 212: `ROUND_001_A` Lemma B, `ROUND_001_D` Lemma A.

### (2) The object: what can be written and what is missing

There is no (ℋ_T, V_T, ρ_T) to write. The three possible readings of «square indexed by pairs»
each fall into a case already closed:

- **Coefficient reading** (the matrix of the lattice of prime bases read off law (0.2):
  Γ_pp = ℓ_p², Γ_pq = −ℓ_pℓ_q). With y_p = ℓ_p x_p,
  Σ_p y_p² − 2Σ_{p<q} y_p y_q = 2Σ_p y_p² − (Σ_p y_p)².
  For two primes it is (y_p − y_q)²; for r ≥ 3 primes it has eigenvalues 2 (multiplicity r − 1) and
  2 − r < 0. PROVED (one-line computation; asserts only this about the coefficient matrix). The
  suggestion of R170_850 §5 is thus a two-prime fact: the complete lattice carries a negative
  direction. Moreover γ pairs with c_F′(log n) at distinct nodes (p, q, pq), so not even the
  two-prime case is a square in F: it is a linear use in the autocorrelation. Case (ii) and
  clause O2 (certificate). CITED: R162_501 Prop. 3.1(a).
- **Convolutive Hermitian reading** (V_T F = combination of translations by ±k ℓ_p with weights
  ℓ_p p^{−k/2}; the cross term at log p^a + log q^b comes from pairing a forward translation
  with a backward one). The diagonal of every square of this type is mass ‖F‖² and not a
  translation term; translations in the same direction produce the quotients log(p^a/q^b), which
  a_T does not contain. It is literally E70_10 / R166_502 §5.2 / P1_BBSTAR Lemma 2.7, and the whole class
  (sums of squares with frequencies in log ℚ and weights Λ, Λ₂, μ, log) is closed for T ≥ ½log3
  by P1.A. Case (iv), O8. CITED.
- **Reading compressed to the window** (truncated translations). It is ROUND_005_A Prop. 3.3: product
  (Λ∗Λ, without sign) + quotients (≥ 0, generic) − leakage (≤ 0, generic). CITED. There is no fourth piece.

What is missing, precisely: a family of operators X_p on a Hilbert space such that
(a) X_q*X_p is, for **all** pairs p ≠ q at once, the shift by log p + log q with
coefficient of fixed sign; (b) no atom at log(p/q) appears; (c) Σ_p ℓ_p² X_p*X_p is an
exact part of the archimedean form, uniformly in T. No file in the corpus contains it and
this memo does not have it. OPEN, without object.

### (3) Why the change does not avoid the difficulty of the antecedent

There is no change. The difficulty recorded in R170_851 §2 and R170_841 §4.3 is that the degree-two
content enters paired with a derivative of the correlation, not with a norm; the one recorded in R166_502 §5.2
is that the passage to a norm changes products into quotients. Indexing by pairs (p,q) alters neither
of the two: the pair index **is** the sum Σ_{p≠q} of R166_502. The «correct» orientation of the
cross term is obtained only in the convolution square (linear in c_F), not in the Hermitian one.
The variant «with both diagonals in the same collar» is the completion that R170_854 (3.4) and §6.3
already declare indefinite or ratio-comb-producing. NO-GO in those classes, CITED.

### (4) Identity that would connect it with global positivity

None. Three facts prevent it:

- a_T contains no shift at log(pq), p ≠ q: its arithmetic part is
  −Σ_{n<N} v_n Re c_F(log n) with support on prime powers (STATEMENT §1). A cross term
  −2ℓ_pℓ_q at log p + log q can only enter (G) by cancelling or via Λ∗Λ = μ∗log² − Λ·log; the
  μ∗log² thus introduced is the second jet of the integer comb, and R170_856 §§3–4 proves it cancels
  in the complete identity. CITED.
- γ lives in the scale derivative (virial), paired with c_F′. Joining it to (★) requires the
  first-contact architecture of phase 170 (dependent on (REG), not proved) or the sign of a slope,
  both recorded without sign (R162_501 Prop. 3.1; P211-23A, P211-24A). Not reopened.
- By ROUND_001_D Lemma A the form is affine in the comb: an identity that only rewrites the weight
  (here by the Leibniz rule, ROUND_001_A Lemma B) does not change the form. CITED.

### (5) cΛ and a_P: the line that breaks

There is no line to break because there is no (G). On the channel itself: by R170_854 (4.7), for a
general weight a, μ∗β_a = a·log − (μ∗a)∗log, hence γ_{cΛ} = c·γ_Λ. PROVED (direct substitution, using
μ∗log = Λ). The two-prime-base channel is **linear and homogeneous in the weight**: one of the two
factors ℓ_p, ℓ_q comes from the fixed integer comb, not from the weight. It does not distinguish c = 1 (violates O4 and O10)
and is compatible with ROUND_001_D Lemma A. For a_P: γ_{a_P} = a_P·log − a_P∗Λ is still an explicit
exact law (the cross term equals −2ℓ_pℓ_q if p, q ≥ P and −ℓ_pℓ_q if only one is); nothing fails. The
other falsifiers of `RULES_AVOID.md` §E are not run through for the same reason; for Beurling
systems, R186_005 Lemma S0 (CITED) gives the analogous law with its own system.

### Answer to the five exclusions of the question

(i) Selberg: the candidate **is** that discard (R170_851; R166_502). (ii) Linear use: yes, through c_F′ and
through homogeneity in the weight; R170_869 classifies every linear row on the coefficient space.
(iii) Generic in the weight: yes, by (5). (iv) Arithmetic sum of squares: the Hermitian reading falls
into P1.A. (v) Arithmetic selection at the node: this point is not reached; a pair index in the
dilation is not excluded by R-cont, but there is no square to index.

## Result

**No new mechanism.** Repetition of R170_850–856, R166_502 §5.2, E70_10–12, P1_BBSTAR (P1.A, Lemma
2.7, §2.8) and 211/ROUND_005_A Prop. 3.3. It is not a new impossibility theorem: a second sector
with sign or a non-convolutive object with properties (a)–(c) of (2) is not excluded; it is recorded
that the candidate, as formulated, contributes neither. No construction is warranted.

## What was proved

- The coefficient matrix of the lattice of prime bases read off law (0.2) is
  2·diag − (rank one): a perfect square only with two primes, with a negative direction 2 − r
  from r = 3 on. PROVED (elementary; scope: only the coefficient matrix).
- γ_{cΛ} = c·γ_Λ: the channel is linear and homogeneous in the weight. PROVED (from R170_854 (4.7)).
- The rest is CITED from the sources in (1).

## What failed and why

- The cross term with negative orientation at product shifts appears only in the
  convolution square, which is linear in the autocorrelation of F; on passing to a norm in F the
  products become quotients with coefficient ≥ 0 and the diagonal becomes mass, not the terms
  ℓ_p² c_F′(k ℓ_p) of the law. The identity «Hermitian square = channel γ» fails: the difference is
  exactly Σ_{p≠q} V_p*V_q − Σ_{p≠q} V_pV_q (R166_502 §5.2).
- a_T has no terms at log(pq); the only bridge (Selberg) introduces μ∗log², which cancels in the
  complete identity (R170_856).
- The channel does not break under cΛ nor under a_P.

## Concrete next step

Do not relaunch the two-prime-base channel nor another reading of Λ·log ± Λ∗Λ. Reopening requires first writing
the operators X_p of (2)(a)–(c), in particular the mechanism that eliminates the atoms at
log(p/q) without paying mass, which is the «second sector with sign» of E70_10 and R166_502, never
constructed. Note in `RULES_AVOID.md` I8 that the residue «channel −2 log p log q (850 §5, not
constructed)» is cross-checked as repetition, with the two PROVED observations above, and record
the corresponding row in the routes index and in the grid (not done here: this memo does not edit other
files).
