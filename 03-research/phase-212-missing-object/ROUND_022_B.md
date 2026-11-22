# Round 22, memo B — the «soft» reformulation with a strong norm

Assigned standpoint: soft goal, a_T(F) ≥ −ε(T)·N(F) with ε(T) → 0 and N a fixed norm, independent of T,
as strong as desired. Anticipated conclusion: the reformulation is **exactly** the goal for *every*
finite N on a form core. The cause is freezing (P46 lem:wit-freeze): for fixed F, a_T(F) does not
depend on T, so there is no quantity that can tend to 0. There is no gap in the lemma and no hidden
condition on the strength of N. It is case (a) of the assignment, in a stronger form than anticipated, and the filter
detects repetition.

## Four-point filter (cross-check first)

1. **Closest antecedent (read in primary sources).** P46 `thm:wit-Tc`(i),(iv) (main.tex l.6995–7027):
   extension by zero preserves a_T, and λ_A ≥ −ε(T) with ε → 0 is equivalent to the goal. P46 `lem:wit-freeze`
   (l.7029–7043): for a frozen F, a_T, c_F, the comb term and membership in P_T do not depend on T.
   P46 `thm:wit-asym` (l.7045–7060) and the comment following it: «any limit law … says nothing about frozen
   witnesses beyond what the corresponding statement at the window T_0 says». P46 prop. «no asymptotic slack»
   (e) (l.8848–8851). Master index: l.109 (`λ_A ≥ −ε(T)` already suffices, R6), l.3953 and l.11663 (lem:wit-freeze,
   NO-GO: «frozen tests see nothing new as T grows»), l.4394 and l.12909 (R6, lower half of the
   bilateral law, OPEN). RULES_AVOID §F: the lower half is the goal plus a margin (211/ROUND_007_D Lemma 4.6,
   l.193), and 211/LEDGER C20 gives NO-GO for the simple exponential law.
2. **What is new.** The statement with N(F) instead of ‖F‖² or 1 does not appear textually in the corpus.
   Lemma 1 below proves that it contributes nothing, not even weakly: for any N the soft version
   is literally equivalent to the goal, and the equivalence holds pointwise in each F.
3. **Does it avoid the difficulty of the antecedent?** No. The difficulty of thm:wit-Tc(iv) is that the slack ε(T)
   cannot act on frozen tests. A strong norm does not change that, because N(ιF) = N(F) is also
   frozen.
4. **Connection with global positivity.** It is a logical identity (Lemma 1), of REF type (filter F5): there
   is no sign mechanism.

There is repetition: the reformulation is absorbed by lem:wit-freeze + thm:wit-asym. Below are the exact
statement (requested by the assignment), the answers to questions 1–2 and the diagnosis of the falsifier.

## §1 The exact soft lemma

Notation: a(F) := a_T(F) for any T with supp F ⊂ [−T,T]. By thm:wit-Tc(i) it does not depend on T.
Let 𝒫 := ∪_T P_T (real compactly supported functions, ∫F e^{±t/2} = 0, in the form domain).

**Lemma 1 (PROVED).** Let 𝒞 ⊂ 𝒫 be such that, for every T_0, 𝒞 ∩ P_{T_0} is dense in P_{T_0} ∩ 𝒟_{T_0} for the
form norm. Let N: 𝒞 → [0,∞) be *any* function: it need not be a norm, a seminorm or even
continuous; it suffices that it be finite and depend only on F, not on the window. The following are equivalent:
(i) there exist T_1 and an ε(T) → 0 such that a(F) ≥ −ε(T)N(F) for all T ≥ T_1 and all F ∈ 𝒞 ∩ P_T;
(ii) a(F) ≥ 0 for all F ∈ 𝒞;
(iii) λ_A(T) ≥ 0 for all T.

*Proof.* (i)⇒(ii): given F ∈ 𝒞 ∩ P_{T_0}, one has ιF ∈ 𝒞 ∩ P_T for all T ≥ T_0, with a(ιF) = a(F) and
N(ιF) = N(F) (they are the same object). Then a(F) ≥ −ε(T)N(F) for all large T, and since N(F) < ∞, letting
T → ∞ gives a(F) ≥ 0.
(ii)⇒(iii): a_{T_0} is a closed form bounded below (P46 lem:compact), so it is continuous in
the form norm, and density carries a ≥ 0 to P_{T_0} ∩ 𝒟_{T_0}.
(iii)⇒(i): take ε ≡ 0. ∎

**Density (PROVED).** For 𝒞 = C_c^∞ ∩ 𝒫 the hypothesis holds. C_c^∞(I_T) is a form core (P46,
proof at l.1832–1837, by dilation and mollification). To preserve the two constraints, fix
φ_±, χ ∈ C_c^∞(I_T) dual to the functionals A, B (they are L²-continuous and linearly independent) and
correct the approximation with a combination of φ_±; the corrections tend to 0. Hence N(F) can be
‖F‖²_{H^s} + ‖e^{α|t|}F‖², the archimedean energy + ‖F‖², or any finite quantity on C_c^∞.

**What the lemma forces.** It does not force N to be weak. It forces ε(T) to act on a quantity that does not
move. Every estimate uniform on P_T at large window, restricted to the F with support ⊂ [−T_0,T_0], is a
bound of the fixed number a(F) by −ε(T)N(F) with T free: that is, the exact sign of a(F). A stronger N only
shrinks the class of F where the bound must be exact, without emptying it (it contains C_c^∞ ∩ 𝒫, which is dense).
Hence the answer is the strongest variant of (a): *every* admissible N gives a statement identical to the
goal. There is no gap (b) and nothing real (c).

## §2 Question 1: which barriers apply

- **thm:shape (B′)/cor:shape(e)** (estimate with remainder, ARGUED in general, PROVED at precision
  4·10⁹Te^{−15.449T}). (B′) measures the remainder in the normalization of the infimum over the L² sphere. With strong N,
  the bound −ε(T)N(F) on the L² sphere is small only on F with N(F) ≲ ‖F‖², i.e. in the «bulk». (B′) does not
  *literally* exclude the format −ε(T)N(F). But it does not matter, because Lemma 1 reduces it to (ii), which does fall
  under cor:shape(a)–(e): it is the goal without slack.
- **lem:wit-freeze / thm:wit-asym** (PROVED, class: «asymptotic arguments in T», any limit law).
  **Applies fully.** It is exactly the step (i)⇒(ii).
- **cor:shape(c)** (no bounded functional of the weights decides). Applies to half (ii): an ε(T)N(F) that
  depends on the weights only through bounded functionals cannot be 0 in the limit for Λ and not for
  (1+δ)Λ.
- **TV-robust class / closed under finite modification (thm:shape(A), O_1–O_4).** Applies to (ii): deleting a
  finite number of prime powers changes a(F) at a frozen F with c_F(log n_0) ≠ 0, and the conclusion
  (ii) becomes false (see §4).
- **R6 / «W-fam does not exclude the lower half»** (index l.4394). This does not contradict the above. W-fam does not
  exclude λ_A ≥ L(1−o(1)), and Lemma 1 shows that with any N that statement *is* (ii). Not excluded does not
  mean easier (RULES_AVOID §F).

**The decisive question: does the classical error of the prime number theorem give an ε(T) → 0 for some N?**
(ARGUED, with a PROVED core.) For F ∈ C_c^∞ ∩ P_{T_0}, the term Σ_n v_n c_F(log n) is a
*finite* sum (n < e^{2T_0}). The explicit formula writes a(F) as the sum over zeros Σ_ρ Φ_F(ρ)Φ_F(1−ρ) (P46,
reading after def:wit-model; we use it only here, as context). P_T removes exactly the polar terms
(A = B = 0). If ψ(x) is replaced by x + E(x), with |E(x)| ≪ x·exp(−c√log x), one gets
a(F) = [main term + archimedean] − ∫ c_F(u) e^{−u/2} dE(e^u), with remainder bounded by
R(F) ≍ ∫_0^{2T_0} |(c_F e^{−u/2})′(u)|·e^{u}exp(−c√u) du. This bound is **a fixed number** depending on F,
not on T, and grows like e^{u/2}exp(−c√u) at the scale of the support. No N such that R(F) ≤ ε(T)N(F) can
have ε(T) → 0: R(F) does not depend on T and is in general > 0. For the computations to close with ε → 0 one would need
R(F) = 0 or a signed bound for the remainder, which is (ii) unmodified. No strength of N changes this: N
can annihilate the contribution of F with distant support (weights e^{α|t|}) or with high frequency (H^s), but
any F ∈ C_c^∞ ∩ P_{T_0} with c_F ≢ 0 on (0, 2T_0) still demands the exact sign. The smooth «bulk» cannot be
isolated: frozen F of unit scale are already bulk.

## §3 Question 2: cross-check of antecedents

- P46 thm:wit-Tc(iv), lem:wit-freeze, thm:wit-asym, prop. (e) «no asymptotic slack». They already contain Lemma 1
  with N = ‖F‖² and with the observation about frozen tests; the step to general N is immediate and is not
  written.
- 211/ROUND_007_D Lemma 4.6 and LEDGER C20. The lower half of the bilateral law is equivalent to (N1′)
  μ₁ ≥ L + Tate bound; there is no weaker soft version.
- Index: l.109 (R6), l.3953/l.11663 (wit-freeze NO-GO), l.4394/l.12909 (R6 OPEN), l.4556 (phase 104:
  «deep limit ⟺ Blaschke = 1 [REF-D]», stopping gates). I did not reread in primary sources phase 160 (R160_*),
  phase 164 (tail theorem), the «Cesàro closure» of phase 62 or gates 102–104; the
  cross-check of those sources rests on the cited index entries. None suggests that an asymptotic
  slack is rescued by strong norms. The rule «positivity data do not imply margin data» goes in the
  opposite direction and does not affect Lemma 1.

## §4 Falsifiers (R3-i)

Lemma 1 is a tautology and holds also for the controls: for 2Λ, for deletion of a prime
power and for a Beurling-type weight. What fails for each is hypothesis (i), at the step (i)⇒(ii):

- **2Λ.** There is an F_⋆ ∈ C_c^∞ ∩ P_{T_0} with a^{2Λ}(F_⋆) < 0 (P46 thm:shape(A), O_4 with c = 1). Once
  frozen, a^{2Λ}(ιF_⋆) = a^{2Λ}(F_⋆) < 0 for all T, so no ε(T)N(F_⋆) → 0 bounds it: the remainder
  stays fixed at a negative value and does not decay.
- **Deletion of n_0.** a^{del}(F) = a(F) + v_{n_0}c_F(log n_0). If one takes F with support < ½log n_0 next to a
  negative witness, or an F_⋆ with c_{F_⋆}(log n_0) of suitable sign (O_5, CONDITIONAL), the difference is
  constant in T and the same step fails.
- **Beurling.** Likewise, with the P46 witness in the named window.

Reading: the true weight must give a(F) ≥ 0 *exactly* at each frozen F. The parameter T contributes
no information. «Smoothness in T» is not a resource: what the weight must provide is the
exact sign in each finite window.

## Verdict

**REPETITION / REF (F5).** Lemma 1 (PROVED) shows that «a_T(F) ≥ −ε(T)N(F), ε → 0» is equivalent to the
goal for *every* finite N on a dense core, because a(F) and N(F) stay frozen when the
window is enlarged (lem:wit-freeze). The strong norm weakens nothing, the classical error produces no ε(T) → 0 and the
reformulation has no gap. What is new relative to the corpus is only the step from ‖F‖² to an arbitrary N,
immediate from thm:wit-asym. There is no intermediate result worth keeping. Next operation: none
within this standpoint.
