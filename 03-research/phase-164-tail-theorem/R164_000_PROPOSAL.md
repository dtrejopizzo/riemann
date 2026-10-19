# R164_000 — Phase 164 proposal: the tail theorem

**Status:** proposal. Neither RH nor (★_cell) is asserted. This phase attacks the single point
remaining to close D: R163_401 §4.8, the compensation inequality (★_cell) at the first-contact witness.

Sources read for this proposal: Paper 47 (prob:annihilate, eq:Qspectral), Paper 48 (Problem 6, thm:BFdisc,
walls W1–W12), R163_401 v6 (§4.8, Rem 4.8a, §4.11), R163_801 (Thm 3, Cor 3.1), R163_901/991 (Thm F, family f_t),
R163_1001 (Thm O, f_χ, W3′), R163_602 (F2 Bombieri–Hejhal), R163_603 (L2.1 Riemann–Siegel), grid §6–7
(specification S1–S12), phase 150 (T1/T2/T5, Parseval sterility lemma).

---

## 0. Diagnosis: the form any proof of (★_cell) must take

Everything below is on record and fixes the shape of the closure. Labels follow the cited file.

**P1 (the proof must use primes beyond the window). PROVED-CITED, given the f_t witness (ARGUED).**
R163_901 Thm F: for every N₀ there exists f_t with the same functional equation, the same pole, real
coefficients, zeros with integer multiplicities, and **exactly the same prime side as ζ for log n < 2T₀**,
with T₀ up to the contact, and f_t has an off-line zero. So the datum (Λ(n))_{n<e^{2T_c}} does not distinguish
ζ from f_t and cannot prove (★_cell). Any proof uses Λ(n) with n ≥ e^{2T_c}.

**P2 (where the negative mass lives). PROVED-CITED (R163_801 Thm 3, Cor 3.1).** With X = e^{2T}, for Im x > ½,
$$\sum_\rho\frac{G(t_\rho)^2}{t_\rho-x}=C_T(x)-i\,G(x)^2\,\mathcal T_X(x),\qquad \mathcal T_X(x)=\sum_{n\ge X}\Lambda(n)\,n^{-1/2+ix},$$
with C_T holomorphic off ℝ (except at i/2). Every off-line residue G(t_q)² is carried by the **tail**
G²𝒯_X. P1 and P2 say the same thing from both sides: the closure is a statement about ζ's tail 𝒯_X against
the witness built from the window.

**P3 (which global properties no longer serve as separators).**
- Frequency integrality / modular theta / periodicity: at conductor 1 it identifies (Hamburger), at conductor
  q>1 it is had by f_χ with off-line zeros. **PROVED (R163_1001 Thm O, W3′).**
- On-line abundance (Levinson/Conrey, positive proportion or even 100%): **DEAD as a separator.** Bombieri–Hejhal
  (Duke 1995, PROVED-CITED in R163_602 F2 and G2_B10_R5 Thm H): for DH-type linear combinations, conditionally
  on GRH and an independence hypothesis, 100% of the zeros are on the line and yet infinitely many are off it.
  A mechanism based on abundance would prove "no off-line zeros" for f_χ. Removed from R163_401 §4.11(c)'s
  separator list.
- Riemann–Siegel structure / approximate functional equation: **DEAD as a separator.** It is a functional-equation-only
  datum; f_χ has its own real Hardy function and its AFE (R163_603 L2.1 only uses the FE). Removed from the list.
- Averages over families / character orthogonality / large sieve: **DEAD** by phase 150 (T5, sterility lemma: every
  Parseval-type bound gives κ near 1, not 0; R150_000 §"Parseval-type"). Not repeated.

**P4 (what remains). PROVED as a consequence of P1–P3.** The only datum of ζ that (i) is not shared by f_t,
(ii) is not shared by f_χ, DH, Epstein, M_m or Λ̃, and (iii) is not an identification in itself is the **Euler
product above the window**: the support on prime powers and the multiplicativity of Λ(n)'s values for
n ≥ e^{2T_c}, used non-linearly (S2, S7) and in relation to the window. In the class {Fr ⊂ ℕ, Euler, FE with
Γ(s/2), q free} that is the family of real even Dirichlet L-functions (R163_1001 Thm O.2); at q = 1 it is ζ
alone. There is no falsifier in that class.

**Corollary (the phase's single statement).** Closing D is equivalent to proving:

> **(TC) Tail theorem.** Let F be a real-rooted first-contact witness of ζ at T_c, X = e^{2T_c}, G = F̂. The function
> $C_{T_c}(x)-i\,G(x)^2\,\mathcal T_X(x)$ continues meromorphically to Im x ≤ ½ and **has no poles with Im x ∈ (−½, 0)**.
> Equivalently (R163_801 Cor 3.1): no off-line zeros. The hypothesis the proof may use, and no other proof used:
> 𝒯_X is the tail of −ζ′/ζ, with an Euler product (Λ supported on prime powers, Λ(p^k) = log p).

Rem 4.8a still holds: (TC) at the witness is RH. The phase does not claim (TC) is weaker than RH; it claims the
**hypothesis** it uses (Euler product over p ≥ X versus a witness built with p < X) is the only one not excluded,
and it builds the object that lets it enter before regularizing (S7).

---

## 1. Line L1 (main, new to the corpus): hybrid Euler–Hadamard cutoff at the window's exact edge

**Object.** Gonek–Hughes–Keating (Duke 2007, "A hybrid Euler–Hadamard product for the Riemann zeta function"; CITED
from memory, verify statement and uniformity): unconditionally, for s = ½ + it, X ≥ 2,
$$\zeta(s)=P_X(s)\,Z_X(s)\,\big(1+O(\cdot)\big),\qquad
P_X(s)=\exp\Big(\sum_{n\le X}\frac{\Lambda(n)}{\log n}n^{-s}\Big),\qquad
Z_X(s)=\exp\Big(-\sum_\rho U\big((s-\rho)\log X\big)\Big),$$
with U an explicit transform of a smooth cutoff weight at X and a controlled error term.

**Why it is exactly P1/P2's object.** With X = e^{2T_c}, factor P_X **is the window datum**: it is the exponential
of the prime side that defines the form W_{T_c} and from which the witness comes (R163_401 §4.6). Factor Z_X **is
the tail resummed over zeros**: for Re s > 1, Z_X(s) ≈ ∏_{p>X}(1−p^{−s})^{−1}, the Euler product above the window.
The hybrid cutoff is the only formula on record separating ζ into (window) × (tail) with the **same** parameter X
as first contact, and in which the tail appears **before** regularizing (S7) with the explicit Euler product.

**Novelty.** The hybrid formula was never used for row D (grep: only Goldston–Gonek for S(t) in R163_601 §4.3). Row
4 (Euler product) × column F (global transforms in T): cell 4F, residual O2802.1 ("non-formal property, uniform in
k ≍ log x, of the entire b ≡ 1 book") is the natural cell; also 7F (zero-side tail).

**First falsifiable lemma (round 1).** Write the witness's kernel equation (R163_401 §4.6: archimedean + polar =
window prime side over c_F) as a statement about log Z_X on the critical line:
$$\text{(KZ)}\qquad \int_{\mathbb R}\big|\widehat F(\tau)\big|^2\ \frac{d}{d\tau}\arg Z_X(\tfrac12+i\tau)\,d\tau \;=\;0\quad\text{(or whatever form comes out)},$$
i.e. the witness is orthogonal, in the weight |F̂|², to the logarithmic derivative of the tail factor. Concrete
questions:
1. Is (KZ) exactly the zero-side identity (1.1) with Z_X instead of the sum over zeros? If so, it is E1 and is
   killed in round 1 (the same failure as R163_1001 Thm C.3).
2. If not, what does (KZ) lose when ζ is replaced by f_t? For f_t the hybrid cutoff does not exist as an Euler
   product (f_t is not multiplicative, R163_1001 Thm O proof 2); Z_X^{f_t} is only defined as the quotient f_t/P_X,
   and its "tail" contains the frequencies m/√M. The separator has to appear as a property of Z_X **that only an
   Euler product over p > X has**: for example, that log Z_X(σ) for σ > 1 is a Dirichlet series with coefficients
   ≥ 0 (Λ(n)/log n) supported on n > X. Landau (real singularity at the abscissa of convergence) only gives
   σ_c = 1. One must find the **non-linear** (S2) coefficient-positivity property of log Z_X readable at
   Im x ∈ (−½, 0): candidates to prove/kill: (a) a Jensen–Landau inequality for exp of positive series;
   (b) monotonicity of |Z_X(σ+it)| in σ for σ > 1 inherited by the continuation (false in general, check what
   remains); (c) representation of log Z_X as the Laplace transform of a positive measure on (log X, ∞) and
   Bernstein's criterion (complete monotonicity) — this one is specific to the Euler product and neither f_t nor
   f_χ has it (their "tails" have mixed-sign coefficients: f_χ is a combination of L(s,χ) and L(s,χ̄); −f_χ′/f_χ
   does not have coefficients ≥ 0).
3. Mandatory round-1 falsifier: **Λχ₂** and **deletion Λ1_{n≥5}** have tails with coefficients ≥ 0 and a partial
   Euler product. Every statement coming out of (c) must fail for them through the use of the window (their
   windows differ from ζ's), not through the tail alone. If the mechanism does not look at the window, it is W3.

**What counts as success for L1 in a round.** A PROVED lemma of the form "if F is a first-contact witness of a
system whose P_X is ζ's and whose Z_X comes from a positive measure on (log X, ∞) [tail Euler product], then Z_X
has no zeros in F's cone band." If instead (KZ) is proved E1 for every positive tail measure (there is a positive
Beurling system with ζ's window and an off-line zero in a cone), L1 dies and is recorded with its falsifier.

**Main risk.** That the tail measure's positivity be exactly Beurling positivity, which R163_002/R162_2901 already
showed **does not** follow from ζ's arithmetic for the quotient ζ/E, and that as a class (positive Beurling systems
with ζ's window) it contains systems with off-line zeros: that would be L1's falsifier and also the connection
with L2 (a positive Beurling system with regular N(x)). It is the test deciding L1 in round 1.

---

## 2. Line L2 (independent, 5G): the discrete Beurling frontier below 1/3, in both directions

Thm O.4 (R163_1001): the only place where global integrality has zero-content beyond identification is
BF_θ^disc. Theorem C (R163_803, PROVED): there exist discrete systems with N = ρx + O(x^{θ+ε}), θ ∈ (1/3, ½),
and zeros at Re s = (1+θ)/2. Below 1/3 there is nothing on record.

- **L2a (construction, O163.803a):** negatively correlated rounding (Riemann–Roth-type sums / low-discrepancy
  van-der-Corput constructions over the Witt collar) to push the rounding error below x^{1/3}. If it reaches
  every θ > 0 with off-line zeros, it proves: **"multiplicity integrality is blind to the sign for every θ > 0;
  only N(x) = ⌊x⌋ exact (identification) separates."** That closes Paper 48's Problem 6 negatively and turns P4
  into a theorem: D closes only via a ζ-specific argument (L1), not via any class statement.
- **L2b (positive direction):** prove "discrete system with θ < θ₀ ⟹ RH of the system" for some θ₀ > 0 using
  multiplicity integrality (R163_101 §5: every proof must use it). If it succeeds with θ₀ > 0, ζ (θ = 0) inherits
  RH. Maximum risk; it is a class statement stronger than RH. Only its first lemma is requested: what inequality
  between the variation of N − ρx and ψ_P's oscillation breaks for θ < 1/3 because of integrality? If none can be
  formulated, it is closed.

L2a and L2b are mutually exclusive; one must decide from the evidence and state it.

---

## 3. Line L3 (editor + audit)

- **Editor:** merge grid/R162_2300_part12.jsonl and R163_1001 (W3′, row f_χ, 5E/5F DEAD, 1G sharpened to
  degree-one GRH) into R162_2300_MASTER_grid.json / MASTER_GRID.md and into Paper 48 (tab:falsifiers, §3 walls,
  Problem 6 → θ ≤ 1/3 already there). Update R163_401 §4.11(c) and the box: remove "on-line abundance" and
  "Riemann–Siegel" from the separators (P3), keep only "Euler product above the window" and "BF_θ^disc, θ ≤ 1/3."
  Check pending citations (Zhang 2007, Diamond–Zhang ch. 17, ATAP Thm 19.3, DH's κ, Epstein normalization, DMV,
  Gonek–Hughes–Keating 2007).
- **Audit:** audit L1 (in particular question 1: is (KZ) E1?) and L2 with falsifiers Λχ₂, deletion, ζ_θ, f_t, f_χ,
  M_m, Λ̃; label PROVED / PROVED-CITED / ARGUED / OPEN; check that no "new" statement repeats a DEAD cell of the grid.

---

## 4. Specification against S1–S12 (grid §7)

| | L1 hybrid cutoff | L2 BF_θ^disc |
|---|---|---|
| S1 non-perturbative λ=0 | yes: uses the exact kernel equation | n/a |
| S2 non-linear in the test | yes if it enters via exp/Bernstein; **no** if it stays in linear (KZ) → E1 | yes (integrality) |
| S4 separates from the whole table | only if the positive tail + ζ's window excludes Λχ₂/deletion (round-1 test) | ζ_θ excluded by discreteness; f_t/f_χ are not Beurling |
| S5 not per window | yes: the tail is global | yes |
| S7 Euler before regularizing | yes, it's the hybrid formula's whole point | yes (generalized primes) |
| S11 intermediate step weaker than ⟺ | the lemma "positive-measure Z_X ⟹ no zeros in cones" is class-level | the statement θ<θ₀ ⟹ RH is class-level |
| S12 no numerical margin | yes | yes |

Walls to watch: E1 (L1 question 1), W3 (L1 question 3), W2/M (no margin), W9/T5 (nothing from Parseval).

---

## 5. Round plan (grid first)

- **Round 1:** 2 builders on L1 (one writes (KZ) and settles question 1; another attacks the non-linear property
  (c) Bernstein/Laplace of log Z_X), one construction on L2 (decides L2a vs L2b with a first lemma), one editor
  (L3), one audit. Outputs: R164_101 (KZ), R164_102 (tail measure), R164_201 (frontier), R164_301 (editor),
  R164_190 (audit).
- **L1 cutoff criterion:** if round 1 proves (KZ) is E1 and that the class "positive tail + ζ's window" has a
  falsifier, L1 closes with DEAD label and a named falsifier, and the phase focuses on L2a (class negative
  theorem, closes Problem 6).
- **Phase success criterion:** a PROVED lemma using the Euler tail that is not equivalent to RH, or L2a's negative
  theorem.

Labeling: everything PROVED / PROVED-CITED / ARGUED / OPEN; (★_cell) remains OPEN until proved.
