# PLAN-RH-MAXIMAL — The Maximal Attempt on the Riemann Hypothesis

**Author:** D. Torres · **Compiled:** 2026-05-31 · **Status:** living document, post-Lise-Science-run-7

---

## 0. The premise (read this first — the plan depends on it)

There is no known sequence of provable steps that ends in RH. If there were, RH would be
proven. So "a real plan to prove RH" cannot mean "the 7 steps that prove it." It means three
things we *can* do, and this plan does all three at once:

1. **Concentrate the entire attack on the single true bottleneck** that all serious RH
   approaches share — *positivity of the Weil functional* — instead of spreading effort.
2. **Push our one working instrument (the localized Weil quadratic form) to the exact edge
   of what is provable**, and convert it from a numerical detector into rigorous theorems.
3. **Name the missing lemma with surgical precision** and attack it on the two deepest live
   structural programs (Connes adelic trace; de Branges canonical systems).

If RH is reachable along this line, this is the plan that finds it. If it is not, we will
know *exactly why* — which, on a 166-year-old problem, is itself a real contribution.

**Honesty clause, kept visible throughout:** the probability that this program *proves* RH is
very low (independent advisors: ~3/10 even for "direct progress"). The probability it
produces *new, publishable mathematics* and a *sharply named obstruction* is high. The plan
is built so we pursue the first while guaranteeing the second.

---

## 1. The foundation v7 handed us

The Lise Science run 7 (`lise-science-research-7/Discovery report...pdf`) settled the terrain:

| Result | Status | Consequence for the plan |
|---|---|---|
| Localized Weil form **Q = M_zeros − M_arith** cleanly flags the one RH-violator (L_DH, λ_min≈−9×10⁴) with **zero false positives** on ζ / L(χ) / L(Δ) | Solid, control-validated | **This is the whole attack surface.** Everything else is secondary. |
| Negativity is **intrinsically local**: appears only when center T₀ sits in the off-line window | Solid | The instrument is a *localized* realization of Weil positivity → matches de Branges / Connes locality |
| **δ² scaling** (α≈2.03) and **super-polynomial J-amplification** (~90 orders at J=20) | Solid, quantified | Gives the *quantitative handle* a proof-by-contradiction needs (see §3) |
| v6's "λ_min(ζ)≈0.866" was a **PSD-only artifact** (zero-side Gram matrix, positive by construction) | Corrected | Lesson: only the *full* explicit-formula Q carries information. Never trust a one-sided form. |
| **The missing lemma**: a uniform-in-basis, explicitly quantified truncation estimate coupling (T₀, σ, J) to the zero-sum and prime-sum cutoffs | Named precisely | **This is Phase 1's target — and it is provable.** |
| ω-class moment **fractions do not stabilize** (Erdős–Kac drift); **growth exponents** separate Euler from non-Euler | Moderate, descriptive | A *side paper* (experimental math), not on the RH path. Park it. |
| TDA H0 is **δ²-insensitive**; L_DH **not** a topological outlier at matched sample | Clean negative | **TDA is dead. Remove from all future work.** |

**Net:** the attack is now one object (localized Weil Q) and one named lemma (uniform
truncation control). That is the cleanest position this program has ever been in.

---

## 1bis. What v8 PROVED (the decisive advance)

The Lise Science run 8 (`lise-science-research-8/`, "Localized Weil Quadratic Form Detector") executed Phase 1
and answered Phase 0.B. It is the most concrete advance the program has made.

| Front | Result | Status |
|---|---|---|
| **A — Forced negativity** | Q = Q₀ + P with Q₀ PSD (all on-line) and P a **negative rank-one** update per off-line zero. Courant–Fischer gives λ_min(Q) ≤ ⟨Q₀⟩ − c(δ,σ,J;γ)·v². The δ² law is **proven** (rank-2 contribution A(γ)=2[φφ′+i(φφ′+φ′φ)] from Taylor expansion); the explicit prefactor c matches simulation to **<0.001% (R²=1.00000)** over 60 grid points. | **PROVEN, explicit constants** |
| **B — Truncation control** | Unconditional bound η(X) ≈ A·exp(−α log²X), α set by the **Hermite–Gauss Fourier decay** (α≈σ²/8), derived from the closed-form basis transform **+ PNT only**. Tracks the empirical floor over 7 decades (Pearson r=0.9988). | **PROVEN, unconditional (PNT)** |
| **C — Logical status (the verdict)** | The lemma **splits in two**: detecting a *fixed* off-line zero (signal>noise at finite X) is **Technical / unconditional** (PNT + basis decay), so the **detector theorem is unconditional**. The **uniform** passage λ_min(Q_X)→λ_min(Q_∞) is **RH-equivalent**. | **Verdict delivered** |

**The single missing inequality, now named with surgical precision:**
> uniform spectral-gap control between $\lambda_{\min}(Q_X)$ and $\lambda_{\min}(Q_\infty)$ —
> a bound $\sup_{X\ge X_0}|\lambda_{\min}(Q_X)-\lambda_{\min}(Q_\infty)|\le\varepsilon(X_0)\to0$.
> This is the (LB) of §3, and it is RH-equivalent (Connes/Bombieri/Lagarias positivity).

**Consequences:**
1. **Phase 0.B confirmed with rigor.** The truncation lemma is *Technical*, not RH-in-disguise — exactly the cartography prediction. The advisor's worry is resolved: the RH-equivalent content is cleanly quarantined in the *uniform* statement, not the truncation lemma.
2. **Phase 1 / P7 essentially delivered.** Front A (forced negativity, explicit constants) + Front B (unconditional truncation) = a **rigorous, unconditional localized Weil detector theorem** — the realistic Tier-1 win. Now to be written up as paper **P7**.
3. **Honesty caveat.** L_DH is **downgraded to a qualitative control**: its arithmetic side (von Mangoldt of a sum of L-functions, "log of a sum") is not benchmark-reproducible from public definitions, so the v7 "λ_min≈−9×10⁴" is not rigorously recoverable. The rigorous results rest on the **ζ_δ artificial deformation** (clean), not on L_DH. The engine still separates L_DH from controls by ~13 orders.

---

## 2. The crux, stated exactly

**Weil's criterion (1952), Guinand–Weil form):** RH ⟺ the Weil functional
$$W(f) = \sum_\rho \hat f(\rho) \;-\; \underbrace{\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat f(\tfrac12+it)\,\frac{\Gamma'}{\Gamma}(\ldots)\,dt}_{\text{archimedean}} \;-\; \underbrace{\sum_{p,k}\frac{\log p}{p^{k/2}}\,f(k\log p)}_{\text{prime side}}$$
is **positive semidefinite**: $W(g \star \tilde g) \ge 0$ for all admissible $g$.

Our instrument is the finite matrix $Q_{jk}=W(\varphi_j \star \tilde\varphi_k)$ on a localized
Hermite–Gauss basis $\{\varphi_j\}$ centered at $T_0$, width $\sigma$, dimension $J$.

- **Easy direction (v7 did this, empirically):** an off-line zero $\rho_0$ with
  $\mathrm{Re}(\rho_0)>\tfrac12$ near $T_0$ forces $\lambda_{\min}(Q)<0$. v7 quantified it:
  the negativity scales as $\delta^2$ in the displacement and amplifies super-polynomially in $J$.
- **Hard direction (= RH, untouched):** proving $\lambda_{\min}(Q)\ge 0$ for *all* admissible
  localizations $\Rightarrow$ RH. No one can do this. This is the wall.

**The plan's job is to attack the hard direction by the only route v7 makes available: a
quantitative proof-by-contradiction (§3), whose one technical prerequisite is the truncation
lemma (Phase 1), and whose one deep prerequisite is a structural positivity (Phase 3).**

---

## 3. The proof architecture (be honest about which links are provable)

Assume RH is false: ∃ zero $\rho_0=\beta_0+i\gamma_0$ with $\beta_0>\tfrac12$. Build $Q$ centered
at $T_0=\gamma_0$, width $\sigma$, dimension $J$. v7 established (numerically) two quantitative facts:

- **(A) Forced negativity:** $\lambda_{\min}(Q) \le -c_1(\beta_0-\tfrac12)^2 \cdot A(J,\sigma)$,
  where $A$ is the super-polynomial amplification factor. *(v7: α≈2 in δ; log A ≈ 0.569 J log J.)*
- **(B) Control floor:** for a GRH-consistent arithmetic, $|\lambda_{\min}(Q)| \le \varepsilon(T_0,\sigma,J,\text{cutoffs})$, the truncation/roundoff floor.

**The contradiction:** if we can prove an *unconditional* upper bound on how negative
$\lambda_{\min}(Q)$ can be for the *true* arithmetic of ζ — a bound smaller than (A) would force —
then no off-line zero can exist. RH follows.

Now the honesty, link by link:

| Link | Provable now? | Where it lives |
|---|---|---|
| (A) forced negativity from an off-line zero | **Yes** (Phase 1) — this is the explicit formula + perturbation theory, finite-dimensional | Phase 1 |
| (B) truncation/floor control for the arithmetic side | **Yes** (Phase 1) — this is the named missing lemma | Phase 1 |
| The *unconditional* lower bound on $\lambda_{\min}(Q)$ for ζ's true arithmetic | **No — this IS RH** | Phase 3 |

So Phases 1–2 are genuinely reachable and produce real theorems. **Phase 3 is the wall**, and
the plan's only shot at the *full* proof is to make the wall's positivity *structural* (a trace
or a canonical system where $\ge 0$ is automatic), not analytic. That is Connes / de Branges.

---

## 4. The phases

### Phase 0 — Foundations & translation (no RH risk, pure groundwork)
**Goal:** rewrite our localized $Q$ *exactly* in the language of the three deepest frameworks,
so our instrument is connected to the machinery that could actually prove positivity.
- 0.1 Master and re-derive: Weil/Guinand explicit formula; Weil positivity criterion; Bombieri's
  exposition; Burnol's convolution-power form; Suzuki's Hilbert-space completion.
- 0.2 Master the **Connes** adelic trace-formula reading of the explicit formula (the
  Connes–Consani "arithmetic site"), where $W(f)$ is a *trace* and positivity would be manifest.
- 0.3 Master the **de Branges** canonical-systems framework: our Hermite–Gauss localized kernels
  are reproducing kernels — identify which de Branges space they generate.
- 0.4 Read the **function-field proof** (Weil/Bombieri/Deligne) as a *positivity of an intersection
  form* — the one place an RH-analogue is actually proven, to extract the structural template.
- **Deliverable:** `phase0-translation.md` — our $Q$ written in all four languages, with the
  precise dictionary entry for each. *Publishable as a survey/expository note on its own.*

### Phase 1 — The truncation theorem (the realistic strong win)
**Goal:** prove the missing lemma v7 named, turning the detector into a rigorous local theorem.
- 1.1 **Forced-negativity theorem (link A):** prove that an off-line zero at distance δ from the
  critical line, within $\sigma$ of $T_0$, forces $\lambda_{\min}(Q) \le -c(\delta,\sigma,J)$ with
  *explicit* constants. (Finite-dim perturbation theory + explicit formula. v7 gives the target shape.)
- 1.2 **Uniform truncation lemma (link B):** prove an explicit bound on the error from truncating
  the prime sum at $X$ and the zero sum at height $H$, *uniform in* $(T_0,\sigma,J)$, that keeps
  the GRH-baseline below the off-critical signal. (v7 showed empirically: prime cutoff $10^5$ +
  full archimedean/polar terms buys $10^{27}$ margin. Make it a theorem with constants.)
- 1.3 **Combine into a rigorous detector theorem:** *"If ζ has a zero with Re>½ in
  $[T_0-\sigma,T_0+\sigma]$, then for explicit $(\sigma,J,X,H)$, $\lambda_{\min}(Q)<0$, and the
  GRH baseline cannot reach it."* This is a genuine, citable theorem.
- **Deliverable:** paper **P7 — "A rigorous localized Weil detector for off-critical zeros"**
  (target: *Experimental Mathematics* / *Math. Comp.*). This is the realistic high-value output.
- **Honest ceiling:** this proves the *easy* direction rigorously. It does **not** prove RH. It
  makes the instrument trustworthy and sets up Phase 2/3.

### Phase 2 — The contradiction architecture (mapping the wall precisely)
**Goal:** assemble §3 into a single conditional theorem and isolate the one unconditional
ingredient that is missing.
- 2.1 Write RH ⟸ {Phase-1 theorems} + {an unconditional lower bound $\lambda_{\min}(Q)\ge -\eta$
  for ζ's true arithmetic, with $\eta$ below the forced-negativity floor}.
- 2.2 State the missing unconditional bound as a clean, quotable conjecture $\mathbf{(LB)}$ with
  explicit dependence on $(T_0,\sigma,J)$. **This conjecture is equivalent to (a localized form of)
  RH** — say so explicitly (R7 discipline). The value is that it is now *one precise inequality*,
  not a vague program.
- 2.3 Test $\mathbf{(LB)}$ computationally across the full 5-control panel + ζ_δ at many
  $(T_0,\sigma,J)$: does the empirical $\lambda_{\min}$ floor for genuine L-functions obey a clean
  law? A clean empirical law for $\eta(T_0,\sigma,J)$ is the strongest possible hint at how to
  prove (LB).
- **Deliverable:** `phase2-conditional-theorem.md` + the empirical floor law. Paper **P8** if the
  floor law is clean: *"A localized Weil inequality equivalent to RH, with computational evidence."*

### Phase 3 — The structural assault (the only real shot at the full proof)
**Goal:** make positivity *structural* — find the space/operator where $Q\ge 0$ is automatic for
genuine L-functions and fails exactly for off-line zeros. This is open research; it may not close.
- 3.1 **Connes flank:** realize $Q$ as a compression of the Connes trace operator to the localized
  basis. Question: is there a positivity of the trace (a manifest $\ge 0$) that *survives* basis
  restriction? v7's report explicitly flags "operator comparisons (Connes–Consani) suggest routes
  to stability under basis restriction." This is the single most promising structural lead.
- 3.2 **de Branges flank:** identify the canonical system / structure function whose reproducing
  kernels are our $\varphi_j$. RH-for-this-space ⟺ a monotonicity (the de Branges chain condition).
  Test the chain condition numerically on the panel before investing in proof.
- 3.3 **Function-field template:** look for the analogue of the *intersection-form positivity*
  (the Hodge-index / Riemann–Roch step) that proves RH for curves. Is there an arithmetic analogue
  of "the intersection form is negative-definite on the primitive part" that maps to (LB)?
- 3.4 Every candidate structure is **filtered by the v7 instrument first**: it must reproduce
  control behavior (positive on ζ/L(χ)/L(Δ), negative on L_DH, monotone in δ) before any proof
  effort. This is the program's unique asset — a fast falsifier of structural guesses.
- **Deliverable:** whichever flank survives → the actual attempt at (LB). Honestly: this is where
  the wall is, and where the attempt most likely stops with "here is precisely the open lemma."

### Phase 4 — Community & dissemination (non-negotiable for a real attempt)
RH will not fall to a closed AI+cloud loop. The maximal attempt *requires* putting the sharpened
objects in front of working analytic number theorists.
- 4.1 Publish P7 (Phase 1) — a clean rigorous result is the credibility that earns expert attention.
- 4.2 Bring (LB) and the empirical floor law (Phase 2) to the people whose tools are nearest:
  Soundararajan / Radziwiłł (moments, resonance), the Rodgers–Tao circle (de Bruijn–Newman flow),
  Connes–Consani (arithmetic site). Our job is to hand them an object so sharp they see the move.
- 4.3 Post the instrument + data openly (arXiv + reproducible repo) so the (LB) inequality gets
  attacked by more than us.

---

## 5. The wall, named — so we don't fool ourselves

The full proof requires the unconditional lower bound **(LB)** on the localized Weil form for
ζ's true arithmetic. **(LB) is equivalent to a localized RH.** No finite computation can establish
it (R7: finite-N positivity ⇏ infinite). It can only come from a *structural* reason positivity
must hold — Phase 3. Every prior RH program has died here; we will too, *unless* the Connes or
de Branges structure genuinely makes positivity automatic. The plan's honesty is that it treats
Phase 3 as a real research gamble, not a guaranteed step, while Phases 0–2 deliver real value
regardless.

---

## 6. Tiered outcomes (what we are actually playing for)

- **Tier 1 — guaranteed if we execute well:** Phase 0 translation note + Phase 1 rigorous detector
  theorem (P7) + the parked ω-moment fingerprint paper. Three real publications. The obstruction
  named to a precision it has never had.
- **Tier 2 — plausible:** the (LB) inequality + a clean empirical floor law (P8), handed to experts
  — a genuine new conditional reformulation of RH with computational backing.
- **Tier 3 — the dream, low probability, honestly pursued:** a structural proof of (LB) via Connes
  or de Branges → the last step before, or a piece of, a proof of RH.

We pursue Tier 3 while *guaranteeing* Tier 1. That is what "maximal attempt" means here.

---

## 7. Immediate next actions

1. **v7 and v8 filed**, Ledger updated. ✅ (§1bis, §8).
2. **Write P7 — the rigorous localized Weil detector theorem.** ◀ IN PROGRESS. Front A
   (forced negativity, explicit constants) + Front B (unconditional truncation) + the Front-C
   dichotomy. This is the Tier-1 result and the program's first new *rigorous* theorem.
3. **Phase 0.A.2–0.A.4** (Connes / de Branges / function-field translation) — now sharply
   targeted at the named (LB): the *uniform spectral-gap inequality*. Needs expert verification.
4. **Phase 3 target is fixed:** prove (or structurally explain) the uniform spectral-gap control
   between λ_min(Q_X) and λ_min(Q_∞). This is the wall; it is RH-equivalent.
5. **Side fill:** P2's moment section ← v7 Discovery 2 (ω-class growth exponents). ✅ being done.

---

## 8. Bottleneck Ledger — updated post-v8 (the program's most valuable artifact)

| Observation | Strongest proven statement | Missing lemma | Route? | Nearest tool |
|---|---|---|---|---|
| **Forced negativity (Front A):** an off-line zero at displacement δ near T₀ forces λ_min(Q)<0 | **PROVEN** — finite-dim rank-one perturbation theorem, Courant–Fischer, explicit prefactor c(δ,σ,J;γ); δ² law, R²=1.00000 | — (complete for the detector) | **done** | Courant–Fischer / Weyl perturbation |
| **Truncation control (Front B):** the noise floor η(X) | **PROVEN unconditional** — η(X)≈A·exp(−α log²X), α≈σ²/8 from Hermite–Gauss Fourier decay + PNT; r=0.9988 over 7 decades | — (complete; PNT only) | **done** | Hermite–Gauss transform + PNT |
| **Detector theorem (A+B):** fixed off-line zero ⇒ detectable in finite-X Q | **PROVEN unconditional** — explicit X_min(T₀,σ,J,m,δ) for SNR≥1 | — | **done** | the two above |
| **Front C verdict:** detector lemma is Technical (unconditional); uniform passage is RH-equivalent | Verdict delivered | **(LB) = uniform spectral-gap control** sup_X\|λ_min(Q_X)−λ_min(Q_∞)\| → 0 | **no (this IS the wall, now named)** | Connes trace / de Branges / Weil positivity |
| **v9 stability probe:** H1 (uniform-in-T₀) and H2 (monotone, no Conrey–Li) BOTH supported on GRH controls; small-σ negativity = truncation not pollution | empirical: faithfulness falsifier did NOT fire; both flanks alive | the **entanglement question** (II-a): self-adjoint bounded-below realization of 𝒯 *without* assuming positivity | **theory (Phase 4)** | Connes regularized space; spectral-pollution theory; de Branges (Conrey–Li absent) |
| ω-class moment growth exponents separate Euler vs non-Euler (v7) | Robust finite-N fingerprint (ζ: a≈5.9,9.2,11.3,14.8,19.3; 4th moment 82% off-diagonal) | No asymptotic C_k law (fractions drift, Erdős–Kac) | unknown | Harper 2020, Keating–Snaith |
| L_DH as a *quantitative* control | — (engine separates it by ~13 orders) | L_DH arithmetic side not benchmark-reproducible (non-Euler "log of a sum") | n/a — use ζ_δ for rigor | — (downgraded to qualitative) |
| TDA H0 δ²-insensitive; L_DH not an outlier at matched sample | Clean negative — TDA removed | — | n/a | — (dropped) |

---

*This plan supersedes the "next program" section of MASTER-PLAN.md. It is the operative
roadmap from here. Update the Ledger and the phase deliverables as each completes.*

---

## 9. Parallel arc — Kreĭn index & arithmetic defect (Phases 21–23, papers P31–P34)

This arc runs in parallel and is connected to the main roadmap at Phase 3 (structural positivity).
It has now reached a definitive negative result for its first spectral strategy, and identified
the precise remaining obstacle.

### 9.1 What was established (Phases 21–23)

| Result | Class | Paper |
|---|---|---|
| Kreĭn negative index κ of localized Weil form; RH ⟺ κ=0 | B | P31 |
| Klein four-group V = {id,σ,ι,j} acting on off-line zeros; orbits of size 4 | B | P32 |
| Kreĭn–Langer factorization ξ = ξ₀·P_{4m} under Hypothesis D (0<κ=2m<∞) | B | P32 |
| Modified explicit formula ψ = ψ₀ − D_m (exact identity) | B | P33 |
| Defect anatomy: D_j(x) = (2x^{σⱼ}/|ρⱼ⁺|)cos(γⱼ log x) + subdominant | B | P33 |
| Defect energy ℰ_j(X) ≍ X^{2bⱼ}, bⱼ=σⱼ−1/2∈(0,1/2) | B | P33 |
| KV bound bⱼ ≤ 1/2 − c₀/(log γⱼ)^{2/3}(log log γⱼ)^{1/3} | B | P33 |
| Paley–Wiener barrier: arithmetic (Re(s)>1) cannot penetrate strip (1/2,1) | B | P33 |
| Three candidate invariants audited and failed (Selberg: circular; Mertens: needs bⱼ>1/2; Weil: reduces to W1) | B | P33 |
| Wall W4-RSRP (Pontryagin Spectral Rigidity): Euler product incompatible with finite non-zero κ; new wall distinct from W1/W2/W3 | B | P33 |
| Exact Hadamard depression: δⱼ log|ζ(1/2+it)| = log(bⱼ²+(t−γⱼ)²)+log(bⱼ²+(t+γⱼ)²) − log|ρⱼ⁺|²−log|ρⱼ⁻|² + O(1) | B | P34 |
| Depression depth 2 log bⱼ + O(1) = O(log log γⱼ) at t=γⱼ | B | P34 |
| Structure function lower bound: S₂(τ,T) ≫ e^{2bⱼT} under Hypothesis D | B | P34 |
| Structure function upper bound: S₂(τ,T) ≤ Ce^T e^{−c√T} (unconditional KV) | B | P34 |
| **Compatibility theorem**: bounds compatible since 2bⱼ<1; no contradiction | Negative | P34 |
| **Chaos compatibility**: Hadamard depression O(log log γⱼ) within CMG extreme values | Negative | P34 |
| **Barrier theorem**: Exclusion Principle requires (F1)/(F2)/(F3), none currently available | B | P34 |

### 9.2 The three necessary inputs (the Kreĭn barrier)

**(F1)** Unconditional bound ψ(x)−x = O(x^{1/2+ε₀}) for ε₀ < min bⱼ. Circular (equivalent to zero-location control).

**(F2)** A property of the Euler product ∏_p(1−p^{−s})^{−1} incompatible with zeros in Re(s)∈(1/2,1). This is Wall W4-RSRP. No proof known.

**(F3)** A property of the multiplicative-chaos model incompatible with a depression of depth |2 log bⱼ|. **CORRECTED (post-review):** the claim "depth = O(log log γⱼ)" was wrong — KV bounds bⱼ from above only, giving no upper bound on |log bⱼ|. The correct picture: CMG minimum ~−c log γⱼ accommodates depth O(log γⱼ) (case bⱼ ≥ γⱼ^{−C}) but NOT depth ≫ log γⱼ (case bⱼ super-polynomially small). Since no lower bound on bⱼ is known, (F3) is regime-dependent and cannot be closed in either direction.

**Net: the spectral strategy (Phases 22–23) is fully exhausted. Route to Phase 24.**

### 9.3 Phase 24 — Lower bounds for bⱼ, local profile, rigorous chaos compatibility

**Status: EXECUTED — negative triple result with two positive sub-results.**

| Sub-phase | Result |
|---|---|
| 24-A | No unconditional lower bound for bⱼ exists; bibliographic gap confirmed; conditional bound bⱼ ≥ γⱼ^{−C} under Selberg CLT at specific points |
| 24-B | Universal Lorentzian profile P(u) = log(1+u²) established (new, class B); geometric incompatibility impossible (profile submerged under field fluctuations for bⱼ→0) |
| 24-C | No rigorous result on log|ζ| restricts bⱼ; on-line zero interference (dilema δ* vs bⱼ) masks off-line signal; obstacle triple G1/G2/G3 named |

**Key positive result (24-B):** The Lorentzian profile P(u) = log(1+u²) is universal (independent of bⱼ), deterministic, and qualitatively distinct from Gaussian fluctuations. This is a new mathematical object in the programme.

**Key negative finding:** Any restriction on bⱼ requires information about the JOINT distribution of on-line and off-line zeros — precisely the content of RH. No weaker handle is available.

**Documents:** `phase-24/00-setup.md`, `phase-24/01-lower-bounds-bj.md`, `phase-24/02-local-profile.md`, `phase-24/03-rigorous-chaos.md`.

### 9.4 Phase 25 — Analytic uniqueness of the Euler product (Wall W4-RSRP)

**Status: EXECUTED — wall confirmed in four formulations; three new structural results.**

| Sub-phase | Result |
|---|---|
| 25-A | Fifteen classical mechanisms audited systematically; all fail as dead ends or known walls |
| 25-B | Kreĭn–de Bruijn–Newman connection: Λ ≥ bⱼ²/2 under Hypothesis D (new quantitative link, class B); but gives UPPER bound on bⱼ, not lower |
| 25-C | LP/Turán reformulation of W4-RSRP: ξ₀ ∈ Laguerre–Pólya class under Hypothesis D; Turán inequalities for ξ₀ are circular; LP reformulation named as W4-LP |

**Complete wall map after Phase 25:**

| Wall | Content |
|---|---|
| W1 (Weil positivity) | W(f∗f̃)≥0 equivalent to RH |
| W2 (Hilbert-Pólya) | Self-adjoint operator with spectrum {γⱼ} |
| W3 (trace formula) | Selberg trace for ζ not available |
| W4-RSRP | Euler product (Re(s)>1) cannot constrain zeros in (1/2,1) |
| W4-LP | LP/Turán reformulation of W4-RSRP |
| W4-dBN | Λ=0 ↔ RH; Λ ≥ bⱼ²/2 under Hypothesis D |

All walls reduce to one question: can arithmetic information from Re(s)>1 propagate into Re(s)∈(1/2,1)?

**New results:** Theorem 25-B.4 (Λ ≥ bⱼ²/2), Theorem 25-C.6 (LP reformulation of W4-RSRP), Prop 25-C.1 (P_{4m}>0 on critical line).

**Documents:** `phase-25/00-setup.md`, `phase-25/01-audit-classical.md`, `phase-25/02-deBruijn-Newman.md`, `phase-25/03-krein-lp.md`, `phase-25/04-verdict.md`.

### 9.5 Phase 26 — Kreĭn index and the Connes operator (the bridge)

**Theme:** Is the Kreĭn negative index κ of the Weil form Q equal to the number of complex eigenvalues of the Connes scaling operator $H_C$ in the Kreĭn space $(\mathcal{K}, Q)$?

**The Bridge Theorem (Conjecture 26-C.2 — to be proved or refuted):**

Under Hypothesis D with κ=2m: the operator $H_C$ viewed as a $Q$-symmetric operator on the Pontryagin space $\mathcal{K} = (L^2(C_\mathbb{Q}), Q)$ has exactly κ=2m complex eigenvalues corresponding to the off-line zeros $\{b_j+i\gamma_j : j=1,...,m\} \cup \{-b_j+i\gamma_j\}$. Moreover:
$$\kappa = 0 \iff H_C \text{ is genuinely self-adjoint in }\mathcal{K} \iff \text{RH.}$$

**Four verification items:**
- **V.1:** Is $H_C$ $Q$-symmetric? (requires computing $Q(H_C f, g) = Q(f, H_C g)$)
- **V.2:** Do the characters $x^{b_j+i\gamma_j}$ lie in $\mathcal{K}$? (requires $Q(f_j,f_j)$ finite)
- **V.3:** Does neg.ind($H_C$ in $\mathcal{K}$) = κ = neg.ind(Q)? (Kreĭn–Langer spectral theorem)
- **V.4:** Is the eigenspace dimension consistent with the Klein V-orbit count?

**Status:** Bridge theorem formulated precisely; technical verification work started.
**Document:** `phase-26/00-bridge-theorem.md`. ✅

### 9.7 Phase 27 — Adelic rigidity (next direction)

**Prerrequisito:** Conjetura 26-C.2 (Teorema Puente) aceptada como hipótesis de trabajo.
**Objetivo:** $\operatorname{neg.ind}(H_C) = 0$ via la estructura de $C_\mathbb{Q}$.

The bridge changes the question entirely: RH is now equivalent to showing that the Connes
scaling operator has no complex eigenvalues, which reduces to excluding non-unitary
Grössencharacters from the scaling spectrum. Phase 27 attacks this via an adelic
local-to-global principle for the Weil form.

**The Phase 27 program:**
- **27-A:** Every negative direction of Q → isolated complex eigenvalue (from bridge + Kreĭn–Langer)
- **27-B:** Every complex eigenvalue → non-unitary character of C_Q (adelic interpretation)
- **27-C:** Non-unitary character → violates adelic Hasse–Minkowski for Q (local-global principle)
- **27-D:** neg.ind(H_C) = 0 → RH

**Why new:** Phases 21–25 exhausted all spectral/analytic tools. Phase 27 brings new tools:
local-global principle, adelic factorization Q = ∏_p Q_p, representation theory of C_Q.

**Documents ejecutados:**
- `phase-27/00-setup.md` ✅
- `phase-27/01-A-B-classification.md` ✅ — 27-A (clasificación) + 27-B (interpretación adélica); Teorema 27-B.4: V.2 = 27-B son el mismo obstáculo
- `phase-27/02-C-wall-analysis.md` ✅ — Wall A (no-factorización de Q_zero, Prop. 27-C.1) + Wall B (Hasse–Minkowski no aplica en dimensión infinita, Prop. 27-C.6); equivalencia Wall A = sitio aritmético de Connes–Consani (Prop. 27-C.5)
- `phase-27/03-verdict.md` ✅ — Veredicto final

**Resultados de Phase 27:**

1. **Identificación V.2 = 27-B** (Teorema 27-B.4): El obstáculo $x^{b_j+i\gamma_j} \notin L^2(C_\mathbb{Q})$ (Phase 26) es idéntico a la no-unitaridad del carácter (Phase 27). Phase 27 no es una ruta alternativa a V.2 — es la misma ruta en lenguaje adélico.

2. **Wall A es no-factorización** (Prop. 27-C.1): El término de ceros $Q_{\rm zero} = \sum_\rho \hat{h}(\rho)$ no factoriza sobre primos. Los ceros de $\zeta$ son objetos globales; los factores de Euler $(1-p^{-s})^{-1}$ nunca se anulan. No existe análogo del "Frobenius en un primo" para $\zeta/\mathbb{Q}$.

3. **Wall A = sitio aritmético de Connes–Consani** (Prop. 27-C.5): La factorización $Q = Q_\infty + \sum_p Q_p$ requiere construir $H^1(\operatorname{Spec}\mathbb{Z}, \mathcal{F})$ con operador de Frobenius aritmético y forma de intersección positiva. Ésto es exactamente el programa de Connes–Consani.

4. **Wall B sin solución conocida** (Prop. 27-C.6): El teorema de Hasse–Minkowski clásico no aplica a formas hermitianas infinito-dimensionales.

**Diagrama de equivalencias completo:**

$$\text{RH} \iff \kappa(Q) = 0 \iff \operatorname{neg.ind}(H_C) = 0 \iff Q \ge 0 \iff \text{Wall A + } Q_p \ge 0 \forall p \iff H^1(\operatorname{Spec}\mathbb{Z}) \ge 0.$$

**Veredicto Phase 27:** Éxito metodológico. Wall W4-RSRP identificado con precisión máxima como el programa de Connes–Consani. El obstáculo final está más precisamente caracterizado que en cualquier fase anterior.

### 9.8 Papers P33–P35 — status

- **P33** ([`06-papers/P33-arithmetic-defect/main.tex`](06-papers/P33-arithmetic-defect/main.tex)): 14 pages, compiles clean. ✅
- **P34** ([`06-papers/P34-two-scale-structure/main.tex`](06-papers/P34-two-scale-structure/main.tex)): 8 pages, compiles clean (3 cosmetic overfull warnings). ✅
- **P35** ([`06-papers/P35-bridge-theorem/main.tex`](06-papers/P35-bridge-theorem/main.tex)): 9 pages, compiles clean. ✅ — Bridge conjecture κ(Q) = neg.ind(H_C), verification program V.1–V.4, Phase 27 direction.
