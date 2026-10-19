# Doc 116 — Adversarial audit of Theorem 5.2 of Doc 113 (non-Stepanov-almost-periodicity of ζ in the strip)

**Program:** Riemann Hypothesis — Phase 38, final audit
**Target:** Doc 113 (phase-37-physics/113-lp-112-against-the-literature-is-there.md), §5.2, Theorem 5.2:
*"ζ is not S^p-almost-periodic on any sub-band of the critical strip, for any p ≥ 1 — unconditional"* — cited in P44 as Theorem 4.2 (main.tex, lines 282–288).
**Nature:** audit of definitions, of the proof step by step, of the external references (verified at source via web in this session) and of the use in P44. No numerics. Absolute frankness: what survives and what does not is reported, with exact location.

---

## 0. Executive summary of the attack

The four mandatory lines of attack were carried out plus three additional ones. Anticipated
result (detail in §§1–6, formal verdict in §7):

- **The theorem, AS STATED IN DOC 113, survives intact.** The central reason
  is that Doc 113 states and proves the **band (vector-valued) version**: the
  Stepanov norm the theorem declares infinite is explicitly
  ‖ζ‖_{S^p(B)}^p = sup_x ∫_x^{x+1} ∫_{σ₁}^{σ₂} |ζ(σ+it)|^p dσ dt (§5.2 of the doc, the
  formula precedes the theorem). With that norm, the "2D subharmonicity → 1D window"
  step that the target flagged as the most likely location of an error **does not exist**: the
  disk of the submean inequality is compared directly with the
  band × window rectangle, without Fubini and without any moving σ′. The leak with
  moving σ — real — only appears in the fixed-line version, which **Doc 113 explicitly does NOT claim**
  and declares as an open gap (§5.2, final paragraph: "On the single-line
  version... it does not follow from Theorem 5.2... minor GAP, open").
- **The Ω references were verified at source and are more than enough.** Aistleitner (Math. Ann.
  365 (2016), arXiv:1409.6035, abstract verified in this session): for α ∈ (½,1)
  FIXED, unconditionally, max_{0≤t≤T}|ζ(α+it)| ≥ exp(c_α(log T)^{1−α}/(log log T)^α),
  c_α = 0.18(2α−1)^{1−α} — exactly what Doc 113 cites, verbatim. Moreover the
  real input the proof needs is much weaker: ANY unboundedness of
  ζ on an interior line of the band suffices, and that is unconditional Titchmarsh with
  Ω(exp((log t)^{1−σ−ε})) (Chap. VIII), verified via a secondary source.
- **The only actionable finding is a wording issue, and it is in P44, not in Doc 113:**
  the statement of P44 Theorem 4.2 ("ζ is not Stepanov almost-periodic (S^p, any
  p≥1) on any sub-strip") does not specify the sense (band/vector-valued vs. line
  by line) and admits the stronger, unproved reading. Exact correction in §6.

**VERDICT: SURVIVES INTACT (Doc 113, Thm 5.2). P44 Theorem 4.2: SURVIVES WITH
ONE wording CORRECTION (one clause).**

---

## 1. Attack 1 — Definitions: what is S^p-a.p. for a function of two variables, and does the proof use the definition it states?

### 1.1. The definition Doc 113 uses

Doc 113 §5.1 gives the classical scalar Stepanov norm
‖f‖_{S^p}^p = sup_x ∫_x^{x+1}|f|^p, with f S^p-a.p. if it is a limit in that norm of
trigonometric polynomials (equivalently: relatively dense almost-periods in
that norm). This matches the classical definition (Besicovitch 1932, Chap. II;
Levitan–Zhikov): the two formulations (closure of polynomials / relatively dense
almost-periods à la Bohr in S^p norm) are equivalent for Stepanov — the
equivalence is standard theory and is not questioned here.

For the function of two variables, Doc 113 §5.2 does exactly what the target
required checking: **it declares the form of the statement before proving it**. Quoting the
structure: "the useful version is the band version: for a closed band
B = [σ₁,σ₂] ⊂ (½,1), consider ζ as a function t ↦ ζ(·+it) ∈ L²(B) and the vector-valued
Stepanov norm ‖ζ‖_{S²(B)}² := sup_x ∫_x^{x+1}∫_{σ₁}^{σ₂}|ζ(σ+it)|² dσ dt."
That is: ζ is treated as a function of ONE real variable t with values in the Banach
space L^p(σ₁,σ₂), and the vector-valued Stepanov norm is the classical one with |f(t)|
replaced by ‖ζ(·+it)‖_{L^p(B)}. For general p the formula is the double
integral of |ζ|^p — consistent with what the proof uses. The definition is precise, it is the
standard one in the vector-valued theory of almost-periodicity (Levitan–Zhikov, Banach-valued
a.p. functions), and **the proof uses exactly that norm**: there is no
definitional slippage between statement and proof. First point of attack:
fails.

### 1.2. Is "S^p-a.p. ⟹ S^p-bounded" (Lemma 5.1) a true theorem?

Yes, under both definitions, and this was checked both ways:

- **Via closure (the one the doc uses):** if f is an S^p limit of trigonometric
  polynomials, then ‖f‖_{S^p} ≤ ‖f−P‖_{S^p} + ‖P‖_{S^p} < ε + ‖P‖_{S^p},
  and a trigonometric polynomial (scalar or with coefficients in L^p(B)) is a
  bounded function of t, hence of finite S^p norm. The boundedness obtained is
  **boundedness of the S^p norm** (‖f‖_{S^p} < ∞), NOT pointwise
  boundedness — and this is exactly what the doc uses afterward. The target warned against
  confusing S^p-bounded / pointwise bounded: that confusion is not in the doc. The S^p
  limit of bounded functions can be pointwise unbounded, correct — but its
  S^p norm is finite by convergence, which is the only thing Theorem 5.2 contradicts.
- **Via almost-periods (alternative definition), for adversarial completeness:** if f
  ∈ L^p_loc has relatively dense S^p almost-periods, take ε = 1 and L such that
  every interval of length L contains a 1-almost-period. Given x, there is τ ∈ [x−L, x]
  almost-period... more precisely: τ almost-period in [x, x+L] gives, with y = x−τ ∈
  [−L,0], that ‖f‖_{L^p(x,x+1)} ≤ 1 + ‖f‖_{L^p(y,y+1)} ≤ 1 + sup_{y∈[−L,1]}
  ‖f‖_{L^p(y,y+1)} < ∞ by local integrability (ζ is continuous on the closed band,
  hence locally bounded — the requirement holds). Same conclusion.

Lemma 5.1 is, as the doc says, essentially definitional. Second point of
attack: fails.

### 1.3. Subharmonicity: direction of the inequality and validity for |ζ|^p

- |g|^p is subharmonic for holomorphic g and every p > 0 (log|g| subharmonic and
  composed with exp(p·), convex increasing). The theorem requires p ≥ 1 only so that
  S^p is the classical normed class; subharmonicity is not the restriction. ✓
- The submean inequality is used in the correct direction: u(center) ≤ average over the
  disk, i.e. average ≥ V_n^p. The doc writes V_n^p ≤ (1/πr²)∬_{D(σ+it_n,r)}|ζ|^p dA.
  ✓ No inequality inversion.

---

## 2. Attack 2 — The core: the 2D→1D step and the leak via a moving σ

### 2.1. Exact reconstruction of the proof

Data: B = [σ₁,σ₂] ⊂ (½,1), σ ∈ (σ₁,σ₂) fixed, r = min(σ−σ₁, σ₂−σ, ¼)/2 > 0.
Aistleitner/Titchmarsh give t_n → ∞ with V_n := |ζ(σ+it_n)| → ∞ (on the extraction
of the sequence, see §3.2). Chain:

1. **Submean:** V_n^p ≤ (1/πr²) ∬_{D(σ+it_n, r)} |ζ|^p dA.
2. **Geometric inclusion:** D(σ+it_n, r) ⊂ [σ₁,σ₂] × [t_n−r, t_n+r], because
   r ≤ (σ−σ₁)/2 and r ≤ (σ₂−σ)/2. ✓ The integrand is ≥ 0, so the integral over the
   disk ≤ the integral over the rectangle. ✓
3. **The window fits:** r ≤ ⅛ < ½, so [t_n−r, t_n+r] ⊂ [x_n, x_n+1] with
   x_n = t_n − r. ✓
4. **Conclusion:** ∫_{x_n}^{x_n+1}∫_{σ₁}^{σ₂}|ζ|^p dσ dt ≥ πr² V_n^p → ∞, hence
   ‖ζ‖_{S^p(B)}^p = sup_x (…) = ∞. With Lemma 5.1 (contrapositive): ζ is not
   S^p(B)-a.p. ∎

### 2.2. Where is the Fubini step, where is the moving σ′?

**Nowhere.** This was the main point of attack of the target, and the audit's answer
is categorical: the proof NEVER converts the 2D average into a 1D average at a fixed σ.
The quantity the theorem declares infinite IS the 2D average over
band × unit-window (the vector-valued norm S^p(B)). Step 2 above is a
domain inclusion with positive integrand — monotone, trivial, no loss. There
is no selection of a σ′ depending on n, no accumulation problem for σ′_k, no
need for uniformity in σ. The architecture of the proof is designed
exactly to dodge the leak: the band norm absorbs the two-dimensional character of
the subharmonic information.

The leak via a moving σ is REAL — but only if one wanted to conclude something about the
scalar S^p norm of t ↦ ζ(σ₀+it) on a fixed line σ₀: there "a large point at
(σ,t_n)" + submean only gives "SOME σ′′ (depending on n) has a large 1D average", and
σ′′ cannot be fixed. Does Doc 113 commit that step? **No.** The final paragraph of §5.2
states it explicitly: "if ζ(σ+i·) is S²-bounded on A FIXED line this does not follow
from Theorem 5.2 (subharmonicity spreads the mass over a two-dimensional neighborhood, not
on the line itself)… Declared status: minor GAP, open — and irrelevant for
LP-112". The document not only does not commit the error: it names it, locates it and
dismisses it as irrelevant to its use (Rouché needs area control, the band).
Frankness verified at the most delicate point.

### 2.3. Conclusion of the attack on the core

Of the three options in the target — (a) holds at fixed σ, (b) holds only in the
band/vector-valued version, (c) does not hold — the answer is **(b), and (b) is exactly what
Doc 113 states and proves**. Version (a) (fixed line) remains genuinely open:
the argument does not prove it, the doc does not claim it, and this audit also found no
cheap route to prove it (the Hardy-type logarithmic convexity of
σ ↦ ∫|ζ(σ+it)|^p dt holds for integrals over the whole line, not over windows; and
there is no 1D submean inequality for |hol|^p over vertical segments). Version
(c) is refuted by this audit: the proof of (b) is correct.

---

## 3. Attack 3 — The Ω-theorems: statements, conditionality, sufficiency

### 3.1. Verification at source (this session)

- **Aistleitner, arXiv:1409.6035 / Math. Ann. 365 (2016)** — abstract verified
  on arXiv: for α ∈ (½,1) fixed, **unconditional**, for every large T:
  max_{0≤t≤T}|ζ(α+it)| ≥ exp(c_α(log T)^{1−α}/(log log T)^α), with
  c_α = 0.18(2α−1)^{1−α}, via the resonance method (long resonators). Doc 113's
  citation is verbatim correct, including the attribution of precedent: the paper
  states that "the same result was already obtained by Montgomery, with a smaller value of
  c_α".
- **Montgomery 1977 (Comment. Math. Helv. 52):** Doc 113 cites it "[via Aistleitner,
  original NOT VERIFIED]" — a frank label. A nuance the audit adds: in the
  literature Montgomery's result with denominator (log log T)^σ sometimes appears
  conditional on RH, with the unconditional version from that era in weaker
  form (Levinson: (log T)^{1−σ}/log log T, unconditional — verified via a
  secondary source, a survey of Ω-theorems near Re s = 1, arXiv:1706.07364 and
  hal-01425575). **This is irrelevant to the theorem's validity** because the
  load-bearing reference is Aistleitner (unconditional, verified), but as citation
  hygiene it is better not to rest the word "unconditional" on Montgomery
  (see §6, optional minor correction).
- **Titchmarsh, Chap. VIII (§8.12):** verified via secondary sources: for
  0 < σ < 1 fixed and every ε > 0, |ζ(σ+it)| = Ω(exp((log t)^{1−σ−ε})), unconditional.
  More than enough as independent backing.

### 3.2. Does the Ω input suffice to blow up the S^p norm? Yes — and it is over-determined

The fine point of the target: the Ω value lives at a point; does the proof need the
local average to be unbounded? Answer: the proof needs exactly
V_n = |ζ(σ+it_n)| → ∞ with t_n → ∞, and subharmonicity + domain inclusion does
all the rest (§2.1). To extract the sequence: the results are of the type
max_{0≤t≤T} ≥ Φ(T) → ∞ (Aistleitner) or limsup (Titchmarsh, direct Ω). In the
max case: the maximizers t_T cannot stay in a compact set (ζ is continuous, hence
bounded, on [σ₁,σ₂] × [0,K] for every K), so t_n → ∞ along a
subsequence. ✓ No gap.

Moreover — and this shields the theorem against any citation dispute: **the
quantitative growth rate is irrelevant**. Theorem 5.2 only needs ζ to be
UNBOUNDED on an interior line of each sub-band. The rate exp(c(log T)^{1−σ}…)
is a luxury; mere unboundedness (classical, unconditional, via multiple routes:
Titchmarsh with any ε, or even Voronin's universality, which produces arbitrarily
large values in disks within the strip) already gives V_n → ∞. S^p-a.p. implies
a FIXED finite BOUND on the norm (‖ζ‖_{S^p(B)} = C < ∞); any sequence
V_n → ∞ contradicts it via πr²V_n^p ≤ C^p. There is no need for the growth to
"beat" anything: it only needs to be unbounded. Third point of attack: fails, with
ample margin.

---

## 4. Attack 4 — Does it contradict anything known? Search for contrary literature

- **Sanity check σ > 1:** ζ is uniformly Bohr-a.p. on σ ≥ 1+ε (Bohr 1918,
  absolute convergence) ⟹ S^p-a.p. there (uniform ⟹ Stepanov, classical hierarchy
  Bohr ⊂ S^p ⊂ W^p ⊂ B^p). Theorem 5.2 is restricted to sub-bands of (½,1):
  consistent, no collision. ✓
- **Does anyone claim S-almost-periodicity of ζ in the strip?** Searches in this
  session ("Stepanov almost periodic Riemann zeta function critical strip" and
  variants; review of a recent survey of almost-periodic processes with
  applications to number theory, arXiv:2502.04969, which works in B² and does NOT treat
  ζ in the strip in the Stepanov sense): **no relevant result**. The classical
  notion for ζ in ½ < σ < 1 is Besicovitch B^p almost-periodicity (averages over
  growing intervals — compatible with Theorem 5.2: B^p does not control fixed
  windows) and Bohr's 1922 local-compact notion (RH-equivalent, Doc 113 §2.1).
  On Besicovitch itself: his theory applied to ζ in the strip is B² (this is the
  content of Lemma 2.1 of D112, via the mean-square value); no claim of a
  Stepanov-type result in the strip was found in his work. **There is no literature the
  theorem contradicts.** And the direction of the theorem is the expected one: the
  Stepanov norm is the strongest of the averaging norms (S^p ⊃ fixed windows) and it
  is natural for growth to kill it, just as it kills uniform Bohr (ζ unbounded
  on every line σ ≤ 1).
- **Internal consistency of the program:** Theorem 5.2 is coherent with the table
  of seminorms in Doc 113 §5.4 and with D112 (B² survives because its windows
  grow; Weyl annihilates compacts — the argument of §5.3 of the doc, sup before the
  limit, is correct: for f·1_K the average over windows of length L decays as 1/L
  uniformly in x). Fourth point of attack: fails.

---

## 5. Additional attacks by the auditor (not requested, carried out anyway)

1. **"Non-a.p. by non-membership in the space":** Theorem 5.2 proves something
   stronger than "not a.p.": it proves ‖ζ‖_{S^p(B)} = ∞, i.e. ζ does not even belong to the
   space S^p(B) where a.p. is defined. Does this make the statement "trivially
   true but misleading"? No: it is exactly the useful form (Corollary 5.3 of the
   doc needs the falsity of the premise "ζ ∈ S²(B)-a.p.", and non-membership
   gives it with room to spare). But the prose statement "ζ is not S^p-almost-periodic" is the
   correct consequence and does not overclaim.
2. **Measurability/vector values:** t ↦ ζ(·+it) ∈ L^p(B) is continuous (ζ
   uniformly continuous on B × compacts), so all integrals make
   sense and the vector-valued theory applies. No gap.
3. **Is sup_x attained/legitimately divergent?** The sup over x of a family of
   locally finite integrals (each window gives a finite integral: ζ continuous) can
   be ∞ without contradiction; the proof exhibits the divergence along x_n. No
   gap.
4. **Edge of the band:** σ is taken in the INTERIOR (σ₁,σ₂) and r is calibrated with the
   distance to both edges; the degenerate case σ₁ = σ₂ (a line, not a band) is
   excluded by hypothesis (σ₁ < σ₂ in the statement). No gap.
5. **Use of the theorem within Doc 113 (Cor. 5.3 and table §5.4):** the implication
   "S²-band-a.p. ⟹ LP-112" is used only as motivation (it becomes vacuous); the row of
   the table "Stepanov S^p, band — NO (Theorem 5.2)" says "band" explicitly.
   Doc 113 §5.4 itself and the executive summary (item 5) speak of "ζ is not
   S^p-almost-periodic on any sub-band" — natural reading: as a function on the
   band. Consistent.

---

## 6. The use in P44: the only correction this audit requires

P44 (06-papers/P44-two-lemma-architecture/main.tex, Theorem 4.2 = \thm:stepanov,
lines 282–288) states:

> "ζ is not Stepanov almost-periodic (S^p, any p≥1) on any sub-strip of the open
> critical strip: Stepanov almost-periodicity implies Stepanov boundedness, which
> the unconditional Ω-theorems for large values of ζ (with subharmonicity) violate."

Two possible readings of "Stepanov almost-periodic on a sub-strip":

- **(i) Band (vector-valued) reading:** ζ as an L^p(σ₁,σ₂)-valued function of t, with
  Doc 113's S^p(B) norm. PROVED.
- **(ii) Line-by-line reading:** for each (or some) fixed σ in the sub-band,
  t ↦ ζ(σ+it) is scalar S^p-a.p. NOT PROVED — open, declared as a gap in
  Doc 113 §5.2.

Reading (i) is the natural one ("almost periodic on a region" in the Bohr
tradition for holomorphic functions on bands is a notion of the function on the region)
and is the one Doc 113 (the cited source) defines with a formula. But a strict audit
can read (ii). **Exact recommended correction** — replace the statement of
Theorem 4.2 with:

> "ζ is not Stepanov almost-periodic ($S^p$, any $p\geq 1$) on any sub-strip
> $[\sigma_1,\sigma_2]\subset(\tfrac12,1)$ **in the band sense**: the vectorial
> Stepanov norm $\sup_x \int_x^{x+1}\!\int_{\sigma_1}^{\sigma_2}|\zeta(\sigma+it)|^p\,
> d\sigma\,dt$ is infinite, hence ζ, viewed as an $L^p(\sigma_1,\sigma_2)$-valued
> function of $t$, is not $S^p$-almost-periodic. (The fixed-line scalar version is
> not claimed and remains open.) Stepanov almost-periodicity implies finiteness of
> the Stepanov norm, which the unconditional Ω-theorems for large values of ζ
> (Titchmarsh; Aistleitner 2016), promoted by subharmonicity of $|\zeta|^p$ to
> unit-window area integrals, violate."

Optional minor corrections (hygiene, not validity):

- In Doc 113 and P44, do not rest "unconditional" on Montgomery 1977 (whose version with
  (log log T)^σ appears in the literature associated with RH, with Levinson as the
  weaker coeval unconditional version); the load-bearing unconditional
  reference is Aistleitner 2016 (verified) and, as a minimally sufficient backing,
  Titchmarsh Chap. VIII. Doc 113 already marks Montgomery "[original NOT VERIFIED]";
  it suffices to downgrade it to historical precedent without the word "unconditional" attached.
- The abstract of P44 (lines 68–73) repeats the phrase without the band
  precision; add "in the band (vector-valued) sense" or equivalent.

---

## 7. VERDICT

**SURVIVES INTACT — Doc 113, Theorem 5.2, as stated.**

1. The definition is precise (vector-valued band Stepanov norm, given with a formula
   before the theorem), the proof uses that same definition, and Lemma 5.1
   (a.p. ⟹ finite norm) is correct under both standard definitions of
   S^p-a.p. The proof uses boundedness of the NORM, never pointwise
   boundedness.
2. The step flagged as the most likely location of an error — 2D subharmonicity → 1D
   window — **does not exist in the proof**: the norm being attacked is 2D (band ×
   unit window) and the submean inequality is compared by monotone domain
   inclusion. The leak via a moving σ would only affect the fixed-line version, which the document does not claim
   and declares open explicitly. Of the options (a) fixed σ / (b) band-
   vector-valued / (c) nothing: **(b) holds, and (b) is what is stated**. (a) remains
   genuinely open; (c) is refuted by this audit.
3. The cited Ω-theorems were verified at source (Aistleitner 2016: unconditional,
   fixed σ in (½,1), statement verbatim correct; Titchmarsh Chap. VIII as independent
   unconditional backing), and the input the proof actually needs —
   unboundedness of ζ on an interior line — is over-determined by an order of
   magnitude. Only nuance: the historical conditionality of Montgomery 1977, not
   load-bearing.
4. There is no literature claiming S-almost-periodicity of ζ in the strip (search
   carried out); the classical results (Besicovitch's B², Bohr's local-compact notion) are
   compatible and the theorem's position in the hierarchy Bohr ⊃ S^p ⊃ W^p ⊃ B^p is
   the expected one. The theorem contradicts nothing known.
5. **P44 Theorem 4.2: SURVIVES WITH ONE wording CORRECTION** (clause "in the
   band/vector-valued sense" + note that the fixed-line version remains open;
   exact text in §6). Without that clause, P44's statement admits a
   (line-by-line) reading strictly stronger than what is proved.

The theorem is, moreover, robust: it does not depend on the growth rate (any
unboundedness on an interior line suffices), it does not depend on p (any p > 0 with the
same proof; p ≥ 1 only normalizes the class), and it does not depend on the sub-band (the
radius r is calibrated locally). It is one of the best-shielded statements of the
program, and its internal frankness (the single-line gap declared in §5.2
itself) spared it the only error this audit could have found in it.

---

## Audit references

- Doc 113, §5.1–5.4 (target); D112 (Lemmas 2.1–2.2, Obs. 2.4, Prop. 2.6 — context).
- P44, main.tex, abstract (l. 68–73), Theorem 4.2 (l. 282–288), candid assessment (l. 365).
- C. Aistleitner, *Lower bounds for the maximum of the Riemann zeta function along
  vertical lines*, Math. Ann. 365 (2016); arXiv:1409.6035. [VERIFIED in this
  session: abstract; statement, unconditionality, constant c_α = 0.18(2α−1)^{1−α}.]
- H. L. Montgomery, *Extreme values of the Riemann zeta function*, Comment. Math.
  Helv. 52 (1977). [Via Aistleitner; historical conditionality flagged as a
  hygiene nuance, not load-bearing.]
- E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Chap. VIII
  (Ω-theorems, unconditional, fixed σ). [Verified via secondary sources in this
  session: |ζ(σ+it)| = Ω(exp((log t)^{1−σ−ε})), with the improvements of Levinson and
  Montgomery; survey arXiv:1706.07364, hal-01425575.]
- A. S. Besicovitch, *Almost Periodic Functions*, Cambridge, 1932, Chap. II (classes
  S^p, W^p, B^p; a.p. ⟹ boundedness in the respective norm). B. M. Levitan,
  V. V. Zhikov, *Almost Periodic Functions and Differential Equations* (vector-valued/Banach
  version). [Standard theory; equivalence of definitions and Lemma 5.1
  re-derived independently in §1.2.]
- Negative literature search for "Stepanov almost periodic zeta": no relevant
  results (session search; includes review of arXiv:2502.04969, which
  works in B² and does not touch Stepanov-ζ in the strip).

*End of Document 116.*
