# R184_001 — The discrete Beurling frontier below 1/3 (cell 5G, O164.201a)

Pure mathematics, no numerics, no web.
Corpus inputs (all read for this file): R171_FINAL §0–§1; R164_201 (Theorem L, §1, §3, §3.5);
R164_503 (**already existed**: frontier outside the lattice, items 1–10, ledger O164.503a–d); R163_803/R163_891 (BFdisc, via
R171_FINAL and R164_201); R162_2601 §6 (O2601.1); R162_2300_MASTER_GRID (5G, wall W-identification §3);
00-references/beurling-dmv (BDV 2004.11501 §1; Broucke 2409.10051 Thm 1.2, §6, Thm 6.3; DMV 2006 **not** present,
only via secondary sources). Gate 1, row D and (★_cell) remain **OPEN**. RH is not claimed, nor closure of row D.

**Corpus rule.** The question Q of this objective largely coincides with R164_503. It is not redone:
it is cited, and only what is new is added (§2.1–§2.3 and the table in §1.3).

## State

| # | Statement | Label |
|---|---|---|
| 1 | Exact source of the loss of Theorem L: only the linear Witt-level term k = 1, T₁(X)=Σ_{p≤X} ε_p p^{−a}Φ(X/p), with a=θ/(1−θ), X=x^{1−θ}; its variance X^{2a}Σ_{p≤X}p^{−2a} | PROVED on record (R164_201 §1) |
| 2 | Exponent of the rounding method: e(θ)=max(θ,(1−θ)/2); e(θ)=θ ⟺ θ ≥ 1/3 | random upper bound: PROVED on record (R163_803, read in R164_201 §3.5); lower bound: PROVED in power form (Theorem L, δ(θ)=θ(1−3θ)/(5−3θ)), ARGUED in sharp form (L*) |
| 3 | The dominant primes of the loss are those of level k=1 with p ∈ (X^{1−ε},X], i.e. generalized primes v=p^{1/(1−θ)} ∈ (x^{1−ε′},x]; the number of such points is ≍ x^{1−θ}/log x and its square root is x^{(1−θ)/2} | PROVED (reading from R164_201 §3.5) / ARGUED (that no deterministic choice cancels this: = L*) |
| 4 | **Prop. 2.1 (new).** If Π, Π₀ are prime-counting functions (Π integer-valued, Π₀ continuous) supported on [u₀,∞), u₀>1, with \|Π−Π₀\| ≤ C, then ζ_P = ζ₀·exp G̃ with G̃ holomorphic in Re s>0 and \|G̃(s)\| ≤ C\|s\|u₀^{−σ}/(σ(1−u₀^{−σ})). In particular **ζ_P and ζ₀ have exactly the same zeros and poles in Re s>0** | PROVED (§2.1) |
| 5 | Prop. 2.2: for such a placement, N_P=cx+O(x^θ) implies \|ζ₀(s)e^{G̃(s)}\| ≪_σ \|t\| in Re s>θ; conversely that bound in Re s ≥ θ+ε gives N_P=cx+O(x^{θ+2ε}) up to log factors (smoothed Perron) | PROVED (necessity); PROVED-standard (sufficiency with loss ε) |
| 6 | Hence greedy/quantile placement at the prime level **preserves the zeros at 11/16 for free**; the entire difficulty is transferred to the growth bound of e^{G̃} in θ<Re s<1/2 | PROVED (consequence of 4–5) |
| 7 | With a smooth target Π₀ (Π₀′ ≍ 1/log u) and quantile placement, e^{G̃} has super-polynomial growth in Re s<1/2: ceiling x^{1/2+o(1)} | ARGUED (R164_503 §3.3, O164.503a; not closed here) |
| 8 | Literature: all published discrete realizations with zeros off the line and N=Ax+O(x^θ) have θ ≥ 1/2 (DMV θ∈(1/2,1); Broucke Thm 6.3 θ∈[1/2,1)); Broucke §6 only proves the optimality of the range (1+θ)/2 for θ>1/2 | CITED (secondary source / 2409.10051) |
| 9 | Restriction on any counterexample with θ<1/3: N(ζ_P;α,T) ≪ T^{4(1−α)/(3−2α−θ)}(log T)^9 for α ≥ (1+θ)/2; this does not exclude zeros | CITED (Broucke Thm 1.2) |
| 10 | Rigidity "discrete, θ<θ₀ ⟹ no zeros in Re s>1/2" with θ₀>0 implies RH (ℕ, θ=0) | PROVED (logical; R164_503 item 2) |
| 11 | Q (θ<1/3, discrete, zero with β>1/2) | **OPEN**. Neither counterexample nor rigidity |
| 12 | Row D movement | **NO-GO for this objective**: none; 5G remains ◧ |

## 1. Why Theorem L blocks θ < 1/3

### 1.1 The source of the loss (PROVED on record)
Notation from R164_201 §1: a=θ/(1−θ), w=(s−θ)/(1−θ), X=x^{1−θ}, generalized primes v_{p,k}=p^{k/(1−θ)} with multiplicity
b_{p,k} = c_{p,k}(p^a)+ε_{p,k}, \|ε\| ≤ C. Then

  N_P(x) = (1−θ)xΣ_{m≤X}γ_m/m + ζ(−a)Σ_{m≤X}γ_m m^a + x^θ T(X),  T(X)=Σ_{m≤X}γ_mΦ(X/m).

All the order-≥2 chaos and all levels k ≥ 2 converge for every a>0 (R164_201 §1). The only piece that depends on θ
is the linear chaos of level k=1:

  T₁(X) = Σ_{p≤X} ε_{p,1} p^{−a} Φ(X/p),   Var_{random} T₁ ≍ Σ_{p≤X} p^{−2a}.

### 1.2 The sharp exponent as a function of θ
- a>1/2 (⟺ θ>1/3): Σ_p p^{−2a} converges, x^θ T(X) = O(x^{θ+ε}). Exponent θ. (BFdisc, PROVED.)
- a<1/2 (⟺ θ<1/3): Σ_{p≤X}p^{−2a} ≍ X^{1−2a}/log X, so x^θ·T₁ ≍ X^a·X^{1/2−a} = X^{1/2} = x^{(1−θ)/2}.

Thus e(θ)=max(θ,(1−θ)/2), and θ=(1−θ)/2 ⟺ θ=1/3. Lower bound for **any** bounded rounding (not just random):
Theorem L gives exponent ≥ θ+δ(θ), δ(θ)=θ(1−3θ)/(5−3θ)>0 (PROVED after R164_291); L* would give ≥ (1−θ)/2 ≥ 1/3 (ARGUED; gap:
equidistribution of h_n mod p for p ≤ Y^{1−ε}, R164_201 §3.5). Not redone here.

### 1.3 Which k and which p dominate (new reading of the same count)

| Level / range | Contribution to E_rms | Label |
|---|---|---|
| k ≥ 2, all p | O(x^{θ+ε}) | PROVED (R164_201 §1) |
| k = 1, p ≤ Y^κ (κ<a/(5/2+a)) | ≫ x^{θ+δ}: this is what Theorem L **proves** | PROVED |
| k = 1, Y^κ < p ≤ Y^{1−ε} | pushes the exponent up to (1−θ)/2; this is the L* gap | ARGUED |

Interpretation: the loss is not "the size of ε" but rather that the Witt lattice fixes the positions v=p^{1/(1−θ)} and
leaves ≍ x^{1−θ}/log x integer degrees of freedom in (x^{1−ε},x]; the Franel tests ψ(X/p) (R164_201 §3.1–3.4) are nearly
orthogonal and number ≍ Y^{1−ε}, so a single sequence ε_p cannot have small discrepancy against all of them.
Hence the natural exit is to move the **positions** (off the lattice), which is the question of §2.

## 2. Off-lattice constructions: prime-level placement

### 2.1 Proposition 2.1 (PROVED; new)
*Let Π (step function, integer jumps ≥0) and Π₀ (continuous, non-decreasing, Π₀(u) ≪ u) vanish on [1,u₀], u₀>1, with
S:=Π−Π₀ bounded, \|S\| ≤ C. Let ζ₀(s)=exp(Σ_{k≥1}k^{−1}∫u^{−ks}dΠ₀(u)) be the continuous target system. Then, in Re s>1,*

  ζ_P(s) = ζ₀(s)·exp G̃(s),  G̃(s) = s∫_{u₀}^∞ S(u) u^{−s−1}(1−u^{−s})^{−1} du,

*and G̃ extends holomorphically to Re s>0 with \|G̃(σ+it)\| ≤ C\|s\|u₀^{−σ}/(σ(1−u₀^{−σ})).*

*Proof.* log ζ_P − log ζ₀ = Σ_k k^{−1}∫u^{−ks}dS(u). For σ>0, S bounded and vanishing near u₀: integrating by parts
(no boundary terms) ∫u^{−ks}dS = ks∫S(u)u^{−ks−1}du. Σ_k ∫\|S\|u^{−kσ−1}du ≤ C Σ_k u₀^{−kσ}/(kσ) <∞ justifies the
interchange, and Σ_k u^{−ks} = u^{−s}/(1−u^{−s}); \|1−u^{−s}\| ≥ 1−u₀^{−σ}. Holomorphy by uniform convergence on
compacta in Re s>0. ∎

*Corollary.* exp G̃ has no zeros or poles in Re s>0; therefore ζ_P continues exactly where ζ₀ continues and
has there **the same zeros with multiplicity**. This extends to Re s>0 the observation of R164_201 §1 (greedy on the
lattice, Re w>0) and that of R164_503 §3.1 (only Re s>1/2, with a separate prime-power factor): here the prime
powers are included in G̃. Consequence for Q: if ζ₀ has zeros on Re s=11/16 (e.g. the continuous target of R171/BFdisc,
or any target with zeros off the line), **greedy placement Π(x)=⌊Π₀(x)⌋ (or quantile p_j=Π₀^{−1}(j)) produces
a discrete system with those same zeros**. The zeros are free at the prime level.

### 2.2 Proposition 2.2 (exact reduction of the remainder of N)
By R164_503 item 1 (standard): N_P=cx+O(x^θ) ⟹ ζ_P(s)−cs/(s−1) holomorphic and ≪_σ \|t\| in Re s>θ. With 2.1:

  **(necessity)** \|ζ₀(s)e^{G̃(s)}\| ≪_σ \|t\| in θ<Re s, \|t\|≥1.  — PROVED.

Conversely, if ζ₀e^{G̃} continues to Re s ≥ θ+ε with a single simple pole at 1 and growth ≪\|t\|^{A}, smoothed Perron
with a kernel of order A+2 gives N_P = cx + O(x^{θ+2ε}) — PROVED-standard (loss ε; the kernel is not written out).
Thus, at the prime level, **Q ⟺ there exist a target ζ₀ with zeros in Re s>1/2 and a bounded entire function J (the
rounding decisions) such that ζ₀·exp(G̃_{−ψ(Π₀)}+G̃_J) is polynomial in Re s>θ** (up to ε). This is a reformulation, not a
solution.

### 2.3 What this gives and what it does not give (achievable exponent off the lattice)
- **Smooth target + quantile.** S = −ψ(Π₀(u)) + O(1/u-scale). The stationary phase of the modes e(kΠ₀(u)) against
  t log u gives G̃ a term of power size in \|t\| in Re s<1/2 (R164_503 §3.3, ARGUED, O164.503a). By 2.2 this
  implies that the exponent of N is ≥ 1/2 − o(1). This is the ceiling of DMV/BDV/Broucke (all with θ ≥ 1/2, §2.4). **ARGUED.**
- **Smooth target + free J.** J=Π−⌊Π₀⌋ bounded integer-valued can be just as oscillatory as ψ(Π₀), so 2.2 does not give an
  a priori lower bound: cancellation of G̃_{−ψ} by G̃_J is not excluded by any argument in this file. Example
  that the cancellation exists in principle: ℕ against the continuous target Π₀ = linear interpolation of π between primes has \|S\| ≤ 1, G̃
  holomorphic in Re s>0 and θ=0 — but then ζ₀ = ζ·e^{−G̃} and the zeros are those of ζ. Example that it
  is not automatic: ℕ against Π₀ = li has S=π−li **not** bounded; the smooth target is not a good reference below
  1/2 (R164_503 §3.4). **PROVED** (the two examples); the general statement remains **OPEN**.
- **Best achievable θ off the lattice with what exists:** the same as on the lattice, 2/5 (R171) / λ+ε for λ∈(1/3,1/2)
  (BFdisc); no θ ≤ 1/3 is obtained. **NO-GO** for this objective in the sense "not constructed."

### 2.4 Literature (CITED)
- BDV 2004.11501 §1: DMV construct, for 1/2<θ<1, discrete systems with N=ρx+O(x^θ) and π−Li = Ω±(x exp(−c√log x));
  method: continuous system + discrete approximation (CITED, secondary source; DMV not read).
- Broucke 2409.10051, Thm 1.2: N(ζ_P;α,T) ≪ T^{4(1−α)/(3−2α−θ)}(log T)^9 for α ≥ (1+θ)/2, for any θ-well-behaved
  system (CITED). Thm 6.3: for θ∈[1/2,1) there exists a discrete system with N=Ax+O(x^θ(1+1_{θ=1/2}log x)) and
  N(ζ_P;(1+θ)/2,T) ~ ((1−θ)T/2π)log((1−θ)T/2π) (CITED). §6: the optimality of the range (1+θ)/2 is only proved for
  θ>1/2; Broucke presents it as expected for all θ and notes that ζ_DMV = ζ_c e^{Z} inherits it from its continuous model
  (CITED). Reading: the literature contains no discrete system with θ<1/2 and zeros off the line, other than those of the
  record (BFdisc, θ>1/3).
- Consequence of Thm 1.2 for a hypothetical counterexample with θ<1/3: zeros with β ≥ (1+θ)/2 have density
  ≪ T^{4(1−β)/(3−2β−θ)+ε}; for β=11/16 and θ→0 this is T^{5/7+ε}: there is room for infinitely many zeros (R171 only needs
  infinitely many). **PROVED** (arithmetic applied to the citation).

## 3. Rigidity and honest classification

### 3.1 Rigidity
A theorem "discrete with θ<θ₀ ⟹ no zeros in Re s>1/2", θ₀>0, applied to ℕ (θ=0) is RH, and with θ₀>131/416 would contain
GRH for quadratic characters (R164_503 items 2–4; Huxley exponent cited from memory, O164.503b). Moreover it is
**strictly stronger** than RH: RH says nothing about other discrete systems. Hence rigidity ⟹ RH, not ⟺.
**PROVED** (logical). Proof of rigidity: not attempted as a route (RH-hard). Proof for ℕ alone = identification
(W-identification, grid §3): the class {θ<θ₀, discrete} contains ℕ, quadratic ideals and all the systems of 2.1
with ζ₀ = ζ·(entire without zeros); it does not reduce to {ζ}, so a proof of rigidity would **not** go through identification —
but precisely for that reason it would have to contain RH for ℕ as a particular case. **ARGUED.**

### 3.2 If counterexamples existed for every θ>0
Then no class property of the form "N=cx+O(x^θ)", θ>0, together with discreteness, proves RH; the only remaining
discrete property would be exactness N=⌊x⌋, which is identification (R169_101 §6; W-identification) and reduces again to
RH without change. This would **close** O2601.1 in its "integrality + power remainder" version and would leave only "exact
values of Λ" (R162_2601 §6). **PROVED** (logical implication); the hypothesis is **OPEN**.

### 3.3 If they only existed for θ>θ*>0
Then θ ∈ (0,θ*] would be a class property with content; by 3.1 it could not prove anything without proving RH for ℕ.
Nothing in this file decides between 3.2 and 3.3. **OPEN.**

### 3.4 Row D movement
None. 5G remains ◧. O164.201a remains OPEN, with reduction 2.2 added. No previous label changes.

## Ledger

| id | item | status |
|---|---|---|
| O184.001a | Lower bound for G̃_{−ψ(Π₀)}+G̃_J uniform over bounded integer-valued J (does a J exist that cancels it?) | OPEN; this is O164.503a strengthened |
| O184.001b | Non-smooth target: ζ₀ = (discrete system with θ₀<1/3)·(factor with zeros in Re s>1/2 and polynomial growth below 1/2) — does such a factor with nonnegative prime measure exist? | OPEN; the only gap that 2.1 leaves open |
| O184.001c | Write out the smoothed Perron of 2.2 (sufficiency) | OPEN (routine) |

## For the audit

1. **Prop. 2.1.** Verify there is no boundary term: S(u₀)=0 by hypothesis and S·u^{−ks}→0 for σ>0. The bound uses
   \|1−u^{−s}\| ≥ 1−u^{−σ} ≥ 1−u₀^{−σ}; correct for u ≥ u₀. Check that ζ₀ is well defined (requires Π₀(u) ≪ u).
2. **"Free zeros."** The corollary is correct but cheap: it says nothing about the remainder of N. Do not read it as progress on Q.
3. **§1.3.** The identification "p∈(Y^{1−ε},Y] dominate" is exact for the random variance; for deterministic roundings
   only Theorem L (p ≤ Y^κ) is PROVED. Do not promote L* to PROVED.
4. **§2.3, examples.** The example ℕ with Π₀ = linear interpolation of π shows that bounded S does not obstruct; check that no
   general obstruction for bounded S has been claimed (none is claimed).
5. **Citations.** DMV is not held locally; everything attributed to DMV is via BDV §1 and Broucke §6 (secondary CITED). The figure
   131/416 is from memory (O164.503b).
6. **Duplication.** R164_503 already covered ideas (i)–(ii) of the objective; this file only adds 2.1 (extension to Re s>0 with
   prime powers), 2.2 (reduction), §1.3, the reading of Broucke Thm 6.3/§6, and 3.2–3.3. If 2.2 is judged to be
   standard, downgrade to "PROVED (standard)" without changing the verdict.

## Note (R184_091)

* Broucke exponent with β=11/16, θ→0: 10/13, not 5/7. "Strictly stronger than RH" → "a priori stronger." BFdisc forces θ₀ ≤ 1/3. J is not free (Π is non-decreasing). Cite Hilberdink 2005 (errors of N and Π cannot both fit below x^{1/2} simultaneously).
