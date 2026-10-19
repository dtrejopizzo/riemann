# Document 109 — The critical anchoring principle: what forces Λ=0?

**Program:** Riemann Hypothesis — Phase 37 (physics mode)
**Prerequisites:** P43 (master quantifier), Docs 70–72 (with the corrections of Doc 105), Doc 83 ($d\nu\ge 0$), Doc 102 (Bagchi), Doc 103 (single-scale trace criterion), Doc 108 (value vs inertia, target L8).
**External literature:** de Bruijn (1950); Newman (1976); Csordas–Smith–Varga (1994); Ki–Kim–Lee (2009); Rodgers–Tao (arXiv:1801.05914, Forum of Math. Pi 2020); Polymath15 (Λ ≤ 0.22); Davenport–Heilbronn (1936); Bohr–Landau (1914); Montgomery (1973); Speiser (1934); Levinson–Montgomery (1974); Bagchi (1981).

---

## Summary

Λ ≥ 0 (Rodgers–Tao) together with RH ⟺ Λ = 0 says that, if RH is true, the system of zeros sits **exactly** at the critical point of the de Bruijn–Newman flow — "barely so," in Newman's phrase. In physics no generic system occupies its critical point without a mechanism that forces it there. This document examines the five candidate physical mechanisms — (a) protective symmetry, (b) self-organized criticality, (c) variational principle, (d) renormalization fixed point, (e) fine tuning — and passes each through the master quantifier of P43.

**Main results:**

1. **(§2–§3)** The Rodgers–Tao proof IS an instance of mechanism (b), but structurally **one-sided**: it excludes the post-critical side (Λ < 0) because its order parameter — crystalline rigidity of the spacings — is **extensive** (visible in averages). The pre-critical side (Λ > 0) has order parameter $m$ (number of off-critical quadruples), which is **intensive** and of zero density (Bohr–Landau): invisible to any average. The "extensive/intensive" dualization is the master quantifier in thermodynamic coordinates. The relaxation sandwich is inconceivable from averaged statistics (Prop. 5.2).

2. **(§4)** Symmetry alone does not protect (Davenport–Heilbronn: functional equation, no Euler product, abundant off-critical zeros). The Euler product gives a **proved statistical protection** (zero density of defects) but not an individual one. The sub-question "0 or infinitely many" produces the document's central finding: the **D-109 defect dichotomy** ($m \in \{0,\infty\}$) is an *individual→individual* statement that does NOT require inverting the average→individual quantifier, and the architectural identity
$$\mathrm{RH} \;=\; \underbrace{(m < \infty)}_{\text{L8, bound/sieve side}} \;\wedge\; \underbrace{(m \in \{0,\infty\})}_{\text{D-109, rigidity side}}$$
decomposes RH into two halves of different nature, neither of which is individually equivalent to RH [pending verification otherwise, §4.6].

3. **(§6–§7)** Mechanisms (c) and (d) collapse: every arithmetic free energy is evaluable only at $t=0$ (the heat flow destroys the Euler product — $t=0$ is the only "multiplicative time"), and the integer quantization of the index $\kappa = 2m$ is exactly the non-autonomous inertia of P43.

**VERDICT: PARTIAL** — no mechanism proved, but with a new falsifiable statement (D-109) that lives outside the master-quantifier wall, and with the precise identification of why Rodgers–Tao does not dualize.

---

## §1. Framework: the flow, the constant, and the taxonomy of mechanisms

### §1.1 Established facts (all theorems, literature verified)

Let $\Phi(u) = \sum_{n\ge1}(2\pi^2 n^4 e^{9u} - 3\pi n^2 e^{5u})\exp(-\pi n^2 e^{4u})$ and
$$H_t(x) = \int_0^\infty e^{tu^2}\,\Phi(u)\cos(xu)\,du,$$
so that $H_0(x) = \tfrac18\,\xi\!\left(\tfrac12 + \tfrac{ix}2\right)$ (Rodgers–Tao normalization). Facts:

- **(H1)** [de Bruijn 1950] If the zeros of $H_{t_0}$ are all real, those of $H_t$ are real for all $t \ge t_0$; moreover $H_t$ has only real zeros for $t \ge 1/2$. The forward flow **preserves reality**.
- **(H2)** [Newman 1976] There exists $\Lambda \in (-\infty, 1/2]$ such that the zeros of $H_t$ are all real exactly when $t \ge \Lambda$. RH ⟺ $\Lambda \le 0$.
- **(H3)** [Ki–Kim–Lee 2009] $\Lambda < 1/2$ strictly.
- **(H4)** [Csordas–Smith–Varga 1994] Each "Lehmer pair" (pair of anomalously close consecutive zeros) gives an explicit lower bound for $\Lambda$; with the pair near $\gamma \approx 7005$ they obtained $\Lambda > -5.895\times10^{-9}$. Later improvements with finer pairs pushed the bound close to $-10^{-11}$ [Saouter–Gourdon–Demichel 2011, Math. Comp.; exact value NOT VERIFIED].
- **(H5)** [Rodgers–Tao 2018/2020] $\Lambda \ge 0$ (Newman's conjecture). Hence **RH ⟺ Λ = 0**.
- **(H6)** [Polymath15, 2019] $\Lambda \le 0.22$.
- **(H7)** Under the flow, the real zeros $x_j(t)$ obey (where the sum converges in principal value)
$$\frac{dx_j}{dt} \;=\; -2\sum_{k\neq j}\frac{1}{x_k - x_j} \;=\; 2\sum_{k\neq j}\frac{1}{x_j - x_k},$$
i.e., **deterministic 1D Coulombic repulsion** (Dyson dynamics without noise), with the backward heat equation in $x$: $\partial_t H = -\partial_{xx} H$.
- **(H8)** [Program, D70 with the sign correction from Doc 105] $\Lambda = \inf\{t : T_\lambda(t) = 0\}$, where $T_\lambda(t)$ is the CCM trace of the evolved state.

### §1.2 The starting physical observation

(H2)+(H5) say: **if RH is true, the arithmetic present $t=0$ coincides exactly with the critical point $\Lambda$ of the flow.** Even more strongly, (H5) has a remarkable unconditional reading:

> **For every $t < 0$, $H_t$ has at least one non-real zero.** (This is exactly $\Lambda \ge 0$.)

That is, unconditionally, the entire past of the flow contains complex pairs; RH asserts that the instant at which the last pair touches the real axis is **exactly** the instant $t=0$ — neither before (that would be $\Lambda<0$, already refuted) nor after. The arithmetic state would be the state of **last collision**.

In physics, a system sitting exactly at its critical point demands explanation. Standard taxonomy:

| Mechanism | Physical example | What would make it rigorous here? |
|---|---|---|
| (a) Protective symmetry | symmetry-protected transitions | functional equation + X ⟹ zeros on the axis |
| (b) Self-organized criticality (SOC) | sandpiles, critical point is an attractor | dynamics + statistics exclude $\Lambda \neq 0$ |
| (c) Variational principle | the state minimizes free energy | arithmetic $F(t)$ with forced minimum at $t=0$ |
| (d) Renormalization fixed point | criticality = RG fixed point | $t=0$ a fixed point of a rescaling flow |
| (e) External fine tuning | cosmological constants | — (arithmetic has no tuner) |

The document's question: which of (a)–(d) has a rigorous mathematical counterpart, and produces a new falsifiable statement?

---

## §2. Anatomy of Rodgers–Tao: one-sided SOC with extensive order parameter

### §2.1 The logical structure of the proof (verified against source: arXiv:1801.05914 and Tao's post of 1/19/2018)

The proof is by contradiction with a three-step structure:

**Step 0 (the logical trick).** Suppose $\Lambda < 0$. Then the zeros of $H_0$ are real, i.e., **RH is true under the contradiction hypothesis**. This authorizes the use of all results conditional on RH (Montgomery, conditional Littlewood, etc.) within the argument. This step is crucial and is what breaks the symmetry with the dual side (§2.3).

**Step 1 (relaxation).** If $\Lambda < 0$, the zero system, already all real at $t = \Lambda < 0$, evolves for a time $|\Lambda| > 0$ under the repulsive dynamics (H7) before reaching the present. Rodgers–Tao show that this evolution produces **convergence to local equilibrium**: at $t=0$ the zeros locally resemble (on average) an arithmetic progression, with spacings pinned to the global mean spacing. Tao explicitly describes it as analogous to the Erdős–Schlein–Yau "local relaxation flow" for random matrices; the energy functional $E(t) = \sum_{j<k}\log\frac{1}{|x_j-x_k|}$-type decreases with $\partial_t H(t) = -4E(t)$ (manifest dissipation). Physically: deterministic, noiseless repulsion **crystallizes** the configuration locally.

**Step 2 (statistical contradiction).** The local crystalline rigidity contradicts the pair-correlation estimates for the zeros of ζ — Montgomery (1973, conditional on RH, which is available via Step 0) and related results (Conrey–Ghosh–Goldston–Gonek–Heath-Brown). The real zeros of ζ have spacing fluctuations that are too large (consistent with GUE, inconsistent with a local lattice).

**Conclusion.** The real state at $t=0$ is "too disordered" to be the post-relaxation state of the dynamics. Hence $\Lambda \ge 0$.

### §2.2 SOC reading: answer to question (i), first half

**Yes: the proof is a rigorous instance of mechanism (b), in its exclusionary half.** The exact physical content is:

> *The present state cannot be in the post-critical phase, because the post-critical phase has detectable order (crystalline rigidity of the spacings) and the present state, measurable on average, does not have it.*

Note which type of quantity separates $\Lambda < 0$ from $\Lambda \ge 0$: an **averaged statistic of spacings** — counting variance in mesoscopic windows, the shape of the pair correlation. It is an **extensive** property: if $\Lambda<0$, the rigidity affects *all* zeros (proportion 1), and so an average over $[T, 2T]$ sees it. In the language of P43: the separating quantity on the $\Lambda<0$ side lives on the **average** side of the quantifier, and that is why it is provable.

### §2.3 Why the argument does not run symmetrically: the extensive/intensive asymmetry

Let us try the dual argument. Suppose $\Lambda > 0$. Then:

1. **Step 0 reverses against us.** $\Lambda > 0$ ⟺ ¬RH: there are complex zeros at $t=0$. One can no longer use any tool conditional on RH. The available statistical arsenal shrinks drastically (inventory in §5.1).

2. **The order parameter changes nature.** What distinguishes, at $t=0$, a configuration with $\Lambda = 0$ from one with $\Lambda > 0$? Exactly the presence of $m \ge 1$ off-critical quadruples ($m$ = number of quadruples, $\kappa = 2m$ in the P35 bridge). But:

   - **[THEOREM, Bohr–Landau 1914]** For every $\delta > 0$, $N(\tfrac12+\delta, T) = O(T)$, while $N(T) \sim \tfrac{T}{2\pi}\log T$: the proportion of zeros at distance $\ge \delta$ from the critical axis tends to 0. The defects have **zero density**.
   - Hence the order parameter on the $\Lambda > 0$ side is **intensive**: $m$ can be finite, or infinite but of zero density. In either case, its contribution to any statistic averaged over $[T,2T]$ is $o(1)$.

3. **Consequence.** No averaged statistic of the zeros (real or not) at $t=0$ separates $\Lambda = 0$ from $\Lambda > 0$. The formalization is Proposition 5.2.

**Answer to the key question of (i):** the statistical quantity that separates $\Lambda=0$ from $\Lambda<0$ is of **average** type (spacing variance — that is why Rodgers–Tao exists as a theorem). The quantity that would separate $\Lambda=0$ from $\Lambda>0$ is of **individual** type (existence of $m\ge1$ zero-density defects — that is why the dual side is RH itself and the master quantifier blocks it). The asymmetry of the Rodgers–Tao proof is not a technical accident: it is the master quantifier expressed in thermodynamic coordinates:

$$\boxed{\text{extensive} = \text{average (provable)}, \qquad \text{zero-density intensive} = \text{individual (RH)}}$$

### §2.4 Refinement: what an observer with access to averages would see

It is worth spelling this out because it quantifies the wall. If $\Lambda > 0$ with $m$ finite, the local statistics of the real zeros at $t=0$ differ from those of the case $\Lambda=0$ only in $O(m)$ local windows of size $O(1)$ (the neighborhoods of the heights $\gamma$ of the quadruples, where the local explicit formula and the dynamics couple the complex pair with the neighboring real zeros — see §5.3). Fraction affected: $O(m / (T\log T)) \to 0$. Even $m = \infty$ with zero density gives fraction $o(1)$. An observer who only measures limits of averages obtains **exactly the same numbers** in both worlds. This is the physical version of the P43 phrase: "the arithmetic object lives in the measure-zero exceptional set of its own generic behavior."

---

## §3. The physical meaning of exact Λ = 0: criticality with fluctuations at all scales

### §3.1 What Λ=0 means in terms of the flow's history

Careful answer to the question posed in (iii). $\Lambda = 0$ means, by the definition of infimum, two things at once:

- **(λ1)** For all $t \ge 0$: all zeros of $H_t$ are real. In particular RH.
- **(λ2)** For all $t < 0$: there exists at least one pair of complex zeros of $H_t$.

(λ2) is unconditional (it is Rodgers–Tao). (λ1) is RH. Physically: **the entire past of the flow has living complex pairs, and the present $t=0$ is the first instant of total reality.** It is not that "the last collision occurs at $t=0$" in the sense of a single collision: (λ2) is compatible with an infinite sequence of collisions at times $t_1 < t_2 < \cdots \to 0^-$, accumulating at the present. In fact this is the correct picture, for the following reason.

### §3.2 Lehmer pairs as critical fluctuations [HEURISTIC + CSV theorem]

The Csordas–Smith–Varga mechanism (H4) is the constructive half of the picture: a pair of anomalously close consecutive real zeros at $t=0$ ("Lehmer pair") is, running the flow backward, a pair that **has just collided**: for slightly negative $t$ it was a complex pair. Each Lehmer pair of quality $q$ certifies $\Lambda > -\epsilon(q)$ with $\epsilon(q) \to 0$.

Now, GUE statistics (β=2) predict a spacing density $p(s) \propto s^2$ as $s \to 0$: **there is no minimal gap**. Arbitrarily small spacings (relative to the mean) occur with positive frequency at every scale. If the zeros of ζ follow GUE locally (supported by conditional Montgomery and by all of Odlyzko's numerical evidence), then there are Lehmer pairs of arbitrarily high quality, and by the CSV mechanism, $\Lambda \ge 0$. Rodgers–Tao turned this heuristic into a theorem by another route (rigidity), but the physical picture is the same:

> **The statistics of the present "know" that $\Lambda \ge 0$:** near-collisions at all scales are critical fluctuations visible on average. **The statistics cannot know that $\Lambda \le 0$:** that requires certifying that no near-collision was, in the past, a consummated real collision — an individual event by default.

This completes the answer to (i): the system exhibits the phenomenology of a critical point (scale-free fluctuations, arbitrarily fine near-degeneracies, absence of a gap), and the provable half of that phenomenology (the bound $\Lambda \ge 0$) is proved. **Observable** criticality is established; **exact** criticality ($\Lambda = 0$, not $\Lambda > 0$) is RH.

### §3.3 Frank conceptual tension: noisy equilibrium vs deterministic dynamics [HEURISTIC]

There is a structural observation we have not seen exploited and which we record as a strict heuristic. The flow (H7) is Dyson dynamics **without noise** (deterministic). Its local equilibrium, under confinement, is the **crystal** (equal spacings) — that is what Rodgers–Tao use. GUE statistics, by contrast, is the equilibrium measure of Dyson dynamics **with Brownian noise** (Dyson Brownian motion at β=2). The zeros of ζ:

- evolve (in $t$) under the dynamics WITHOUT noise,
- but exhibit (at $t=0$, conjecturally and, on average, provably up to a certain Fourier range) the equilibrium statistics of the dynamics WITH noise.

That is: the arithmetic state is in the universality class of noisy equilibrium without the flow having any noise. Where does the "noise" come from? The only available source is arithmetic itself (the primes, via the explicit formula, act as frozen disorder — "quenched disorder" — not as dynamical noise). On this reading, RH is the assertion that the frozen disorder of the primes exactly reproduces, at $t=0$, an edge-of-the-noisy-class state that the deterministic flow could not have prepared (if it had prepared it, Rodgers–Tao would be violated). The state at $t=0$ is not the result of the flow's relaxation: it is an **initial condition** dictated from outside the flow (by arithmetic). This rules out the strong version of SOC — the critical point is NOT an attractor of the DBN dynamics; the dynamics did not "choose" $t=0$. What anchors the present to the critical point, if anything does, is not the dynamics: one must look for it in structure that exists only at $t=0$ (§6.2).

---

## §4. Protective symmetry: what the functional equation protects, what Euler protects, and the defect dichotomy

### §4.1 Symmetry alone does not protect [THEOREM, verified]

The functional equation $\xi(s) = \xi(1-s)$ is the $\mathbb{Z}_2$ symmetry of the system (reflection about the critical axis; in $x$ coordinates, reality of $H_0$). Does it alone protect criticality? **No**, and the counterexample is classical and verified:

- **[Davenport–Heilbronn 1936]** The function $f(s) = \sum_n \xi_5(n)n^{-s}$ (explicit linear combination of two Dirichlet L-functions mod 5) satisfies a functional equation of the same type as ζ's and **has infinitely many zeros with $\sigma > 1$** (and, as known today, abundant zeros in the strip $\tfrac12 < \sigma < 1$; explicit computations in Balanzario–Sánchez-Ortiz, Math. Comp. 76 (2007)).
- The decisive structural difference: $f$ **has no Euler product** (it is a linear combination of two functions that do have one, but the combination destroys it).
- Moreover, for non-trivial linear combinations of L-functions there are general existence results for many off-critical zeros via universality (Nakamura–Pańkowski 2012 and later works; the exact order of magnitude of the off-critical count given by those theorems: [NOT VERIFIED in detail], but the infinitude is a theorem).

Rigorous conclusion: **symmetry without multiplicativity protects nothing** — not even statistically: the Davenport–Heilbronn defects are not rare.

### §4.2 What the Euler product does protect (and is proved): statistical protection

For ζ (symmetry + Euler product) the situation is radically different, and the difference is a theorem:

- **[Bohr–Landau 1914]** $N(\sigma, T) = O(T)$ for each $\sigma > 1/2$: zero relative density of defects. The proof essentially uses the Euler product (second moment of $\zeta$/Dirichlet polynomials, mollifiers).
- **[Density theorems, Carlson onward]** $N(\sigma,T) = O(T^{c(\sigma)})$ with $c(\sigma) < 1$ for $\sigma > 1/2$, improving toward the density hypothesis.

That is: the physical statement "symmetry + Euler product ⟹ protected criticality" has a **proved statistical** version (defects have zero density — the off-critical phase is never extensive) and an **individual** version (there are no defects: $m=0$) which is exactly RH and exactly MW-2. The gap between the two is, once again, the master quantifier: zero density (average) vs empty set (individual). Up to this point, everything collapses to the known wall.

### §4.3 The genuine sub-question: 0 or infinitely many? State of the art

Question: can the Euler product coexist with **exactly one** off-critical quadruple? Is there "0 or ∞" rigidity?

**Frank inventory of what is known (of the type "if there is one off-critical zero then [structure]"):**

1. **[Speiser 1934]** RH ⟺ $\zeta'$ has no zeros in $0 < \sigma < 1/2$. Individual contrapositive: an off-critical zero of ζ forces a zero of $\zeta'$ to the left of the axis.
2. **[Levinson–Montgomery 1974]** Quantitative version: $N_1^-(T) = N^-(T) + O(\log T)$ — the counts of zeros of $\zeta$ and $\zeta'$ to the left of the critical axis coincide up to $O(\log T)$. Pairing rigidity defect↔derivative-defect, but it does not produce multiplication of defects.
3. **[Bagchi 1981 + Bohr–Landau; cf. Doc 102]** RH ⟺ ζ is strongly recurrent (self-approximating) in $\tfrac12<\sigma<1$. The relevant direction here is the contrapositive of the easy half: **if ζ has an off-critical zero, then ζ is NOT strongly recurrent.** The proof is the cloning mechanism: if ζ self-approximated with positive density of near-periods, Rouché would clone the off-critical zero into $\gg T$ copies up to height $T$, contradicting Bohr–Landau. This is a genuine theorem of the type sought: **a single individual defect destroys a global dynamical property** (strong recurrence). It is the strongest piece of individual→global rigidity we know of in the literature.
4. **What is NOT known:** no published theorem we know of proves "$m \ge 1 \Rightarrow m = \infty$" for ζ. A literature search does not turn up a dichotomy result; we declare it **open** [state verified as far as our search reaches; NOT VERIFIED exhaustively].

### §4.4 The D-109 defect dichotomy: falsifiable statement

**D-109 statement (defect dichotomy).** *The set of off-critical zeros of ζ is empty or infinite: $m \in \{0, \infty\}$. Equivalently: ζ cannot have a finite positive number of off-critical quadruples.*

Natural generalization (more falsifiable): *no element of the Selberg class has a finite positive number of non-trivial zeros off its critical axis.*

**Why it is physically plausible (declared heuristic):** in systems with long-range interaction, an isolated defect in a critical medium is unstable: it either annihilates or nucleates a phase. Bagchi's cloning is the mathematical shadow of nucleation: a defect + recurrence ⟹ extensive defects. What is missing is the intermediate regime: a defect + weak recurrence ⟹ infinitely many defects (not necessarily extensive).

**Why known routes do not prove it (frankness):** the natural route is to clone the zero via near-periodicity. What is unconditional is $B^2$ near-periodicity (in mean square) of ζ for $\sigma > 1/2$ — near-periods in the mean exist and are relatively dense. But Rouché needs **uniform approximation in a specific disk** around the zero, and mean-square control over the line does not give pointwise control over the individual disk: it is the mean→uniform step, the same wall. The strong version (recurrence with positive density) clones too much ($\gg T$ zeros, contradiction with Bohr–Landau) and that is why it is equivalent to RH (Bagchi); the weak version (cloning along some sequence $\tau_k \to \infty$, which would give exactly D-109) requires pointwise control at the $\tau_k$ — weaker than inverting the quantifier everywhere, but pointwise nonetheless. **OPEN GAP.** What we record: D-109 needs a *sequential* version of the quantifier, not the full inversion; it sits strictly between the unconditional and RH.

### §4.5 Why D-109 matters: the architectural decomposition of RH

Here is the document's structural finding. The P43 ledger left as target L8 (Doc 108, §8.2): a bound on indices per window $\kappa_W \le C\cdot n_W$ would give $m \le C/2$ — that is, **finiteness of the defects** ($m < \infty$), a strictly weaker objective than RH, on the sieve/bound side (what parity does not block: bounding, not distinguishing). Combining it with D-109:

$$\mathrm{RH} \;\Longleftrightarrow\; \big(m < \infty\big) \;\wedge\; \big(m \in \{0, \infty\}\big).$$

The identity is logically trivial; what is non-trivial is that **it splits RH into two halves of different type**:

- **L8 half (finiteness):** it is a BOUND. Bounds are average-compatible: they do not require distinguishing any sign, only majorizing. Doc 108 showed that the available version is behind the wall, but its *form* (upper bound on an index) is the form of statement that averaging methods could in principle reach — it does not require certifying an exact zero, only a finite ceiling.
- **D-109 half (dichotomy):** it is an individual→individual RIGIDITY: "one defect forces infinitely many defects." **It does not require inverting the average→individual quantifier** — its hypothesis and its conclusion are both individual. The P43 wall does not apply *to its statement* (it does, as we saw, to the known proof routes).

Neither half is, separately and obviously, equivalent to RH (verification pending in §4.6). This is the first decomposition of RH the program has produced in which the master quantifier does not block both pieces for the same reason.

### §4.6 Audit of the decomposition [frankness]

Is either half secretly equivalent to RH?

- Does $(m<\infty) \Rightarrow$ RH? Not in any known way: a world with $m=3$ quadruples satisfies finiteness and violates RH. Finiteness is NOT RH in disguise *as a statement*; target L8 is genuinely weaker. (That its proof via the Doc 108 route required RH is a property of the route, not of the statement.)
- Does D-109 $\Rightarrow$ RH? No: D-109 is compatible with $m=\infty$ (a world with infinitely many zero-density defects). Nor does RH ⟹ D-109 trivially... actually yes: if RH, $m=0 \in \{0,\infty\}$. D-109 is a consequence of RH, strictly weaker (a ¬RH world with $m=\infty$ satisfies D-109).
- Do the routes contaminate each other? The real risk: that every conceivable proof of D-109 goes through strong recurrence (=RH, Bagchi). Not proved; the sequential version identified in §4.4 is logically weaker than strong recurrence. OPEN GAP, but no proved collapse.

**Answer to (ii):** symmetry protects only together with the Euler product; the proved protection is statistical (zero density); the most promising new demonstrable partial version is not a density improvement but the D-109 dichotomy, which lives on an axis orthogonal to the wall (individual→individual) and which, combined with the already-named target L8, recomposes RH.

---

## §5. Dyson dynamics and the relaxation sandwich

### §5.1 Inventory of unconditional statistics of the real zeros

To assess whether the $\Lambda \le 0$ side could be proved by "detectable sub-relaxation," we inventory what is known WITHOUT RH (recall §2.3: under $\Lambda>0$, RH is false and conditional results fall away):

| Statistic | Result | Conditional? |
|---|---|---|
| Global count $N(T) = \tfrac{T}{2\pi}\log\tfrac{T}{2\pi e} + \tfrac78 + S(T) + O(1/T)$ | Riemann–von Mangoldt | NO |
| $S(T) = O(\log T)$ | Backlund/classical | NO |
| Moments of $S(T)$: $\int_0^T S(t)^{2k}dt \sim c_k T(\tfrac1{2\pi^2}\log\log T)^k$ (Gaussian CLT) | Selberg | **NO** (the unconditional version exists; under RH the constants improve) |
| Zero off-axis density | Bohr–Landau, Carlson | NO |
| Positive proportion of zeros ON the axis | Selberg; ≥ 41% Conrey/improvements | NO |
| Pair correlation $F(\alpha)$, $|\alpha|<1$ | Montgomery 1973 | **YES (RH)** |
| Spacings: $\liminf \tilde\delta_n < 1 < \limsup \tilde\delta_n$ (gaps smaller and larger than the mean) | Selberg, later improvements (strong improvements under RH) | partially NO |
| Counting variance in windows / Fujii | strong forms under RH | mostly YES |

The essential point: the robust unconditional results are **Selberg** (CLT for $S(T)$: Gaussian fluctuations of size $\sqrt{\log\log T}$) and **zero density**. Fine pair correlation is conditional.

### §5.2 The sandwich is inconceivable from averages [rigorous, nearly tautological, but must be said]

**Proposition 5.2 (invisibility of the pre-critical side).** Let $S$ be any functional of the zero configuration of $H_0$ defined as a limit of local averages: $S = \lim_{T\to\infty}\frac{1}{N(T)}\sum_{\gamma_n \le T} \phi(\text{local normalized configuration at } \gamma_n)$ with $\phi$ bounded (this includes pair correlations with integrable test, spacing distributions, normalized counting variances). Let $Z_0$ be a configuration with $\Lambda = 0$ and $Z_1$ a configuration with $\Lambda > 0$ whose defect set has zero density (which is automatic by Bohr–Landau) and which coincides with $Z_0$ outside the defect windows. Then $S(Z_0) = S(Z_1)$.

*Proof.* The summands where the configurations differ are $o(N(T))$ by zero density, and $\phi$ is bounded; the average's limit does not change. $\square$

The non-tautological content is the Bohr–Landau input: **every** ¬RH world has zero-density defects — nature does not grant us an "extensive" ¬RH world that an average could see. Hence:

> **The sandwich (Λ≥0 via over-relaxation + Λ≤0 via statistical under-relaxation) is inconceivable.** The Λ≥0 half exists (Rodgers–Tao) because over-relaxation is extensive. The Λ≤0 half cannot come from any averaged statistic: it requires individual information. It is the master quantifier, with no escape on the dynamical side.

### §5.3 What would a defect leave behind in the neighboring real zeros? [quantified HEURISTIC]

For completeness: if there is a complex pair $x_0 \pm iy$ at $t=0$ (quadruple with the symmetry), its footprint on the neighboring real zeros is real but local. In the decoupled model, the backward heat equation $\partial_t H = -\partial_{xx}H$ applied to $(x-x_0)^2 + y^2$ gives zeros $x_0 \pm i\sqrt{y^2 - 2t}$: the pair collides at $t = y^2/2$. Before the collision, the pair exerts on a real zero at distance $d$ a force $\sim -2\cdot 2(x-x_0)/((x-x_0)^2+y^2)$ — a dipolar perturbation of range $O(1)$ in units of the local spacing. After the collision ($t > y^2/2$), the two new real zeros push their neighbors and the perturbation relaxes diffusively. Total footprint at future $t=0$: $O(1)$ deformation of $O(1)$ spacings per defect. With $m$ defects: $O(m)$ anomalous spacings among $\sim T\log T$. Detectability by maxima (not averages): a single anomalous spacing is, again, an individual event. This closes coherently with Prop. 5.2.

**Answer to (iii):** Λ=0 means the present is the first instant of total reality with collisions accumulating throughout the immediate past (unconditional λ2); the dual of Rodgers–Tao does not exist because the sub-relaxation that would leave $\Lambda>0$ is local and of zero density — the $\Lambda\le0$ side of the sandwich inevitably requires individual information.

---

## §6. A variational principle? The unique multiplicative time

### §6.1 The program's free energy and its evaluation

The natural candidate from the program: $F(t) := T_\lambda(t)$ (CCM trace of the evolved state), with (H8): $\Lambda = \inf\{t : T_\lambda(t) = 0\}$ (D70, corrected Doc 105). With the single-scale criterion (Doc 103): RH ⟺ $T_{\lambda_0}(0) = 0$. The desired variational structure would be: $F$ computable from the primes, $F \ge 0$, $F(t) = 0$ exactly for $t \ge \Lambda$, and an arithmetic evaluation forcing $F(0) = 0$.

Actual state of each piece:

- $F \ge 0$ and the characterization of the infimum: zero side, rigorous (D70/D103, with $d\nu \ge 0$ from D83).
- Arithmetic side at $t=0$: D72 gives $T_\lambda = A_\lambda^{\mathrm{off}} - \sum_p (\log p/\sqrt p)\,B_\lambda(\log p)$ via the Weil formula — but Doc 105 proved that the prime series **diverges** like $(5\sqrt2/8)\log X$: the formula is strictly formal. A frank arithmetic evaluation of $F(0)$ is not available even formally regularized without going through the zeros.
- $\partial_t F|_0$: D71 showed exact cancellation under RH; Doc 105 corrected that the sign under ¬RH is an OPEN GAP.

### §6.2 The structural obstruction: the flow destroys multiplicativity

There is a deeper reason, cleaner than the details above, why **every** arithmetic variational principle on the flow collapses, and it is worth isolating it:

**Observation 6.2 (the unique multiplicative time).** $H_0$ is, up to normalization, $\xi(\tfrac12 + \tfrac{ix}{2})$: behind it is a Dirichlet series with an Euler product. For $t \neq 0$, $H_t$ is a heat deformation of $\Phi$; the coefficient $e^{tu^2}$ destroys the multiplicative structure — $H_t$ is not (as far as is known, and generically cannot be) the ξ function of any arithmetic object with an Euler product. **The flow's time axis intersects arithmetic at exactly one point: $t=0$.**

Consequences:

1. Any "arithmetic free energy" $F(t)$ can only be evaluated from the primes at $t = 0$. To locate the minimum (or the boundary of the vanishing set) one would need to compare $F$ in a neighborhood of $t=0$ — and for $t \neq 0$ the only access is the zero side. **Transmutation, Doc 99 pattern:** the variational information that would decide RH is obtained exactly from what RH asserts. Mechanism (c) collapses.
2. But the observation reformulates the problem illuminatingly: RH is the assertion that **the flow's critical time coincides with the multiplicative time:**
$$\Lambda \;=\; t_{\mathrm{arith}} \;(=0).$$
Two unrelated structures — the heat equation (additive, analytic) and the Euler product (multiplicative, arithmetic) — share a point, and RH says that this shared point is also the critical point of the first structure. No principle internal to the flow can know where $t_{\mathrm{arith}}$ is (the flow does not see the primes: it commutes with the loss of the Dirichlet series); no principle internal to arithmetic sees the flow (the primes live only at $t=0$). The coupling is exactly the content of RH. This is the "physical" form of MW-2 (multiplicative information does not propagate), now in flow coordinates: **multiplicative information does not propagate in $t$ because multiplicativity does not exist for $t\neq0$.**

**Answer to (iv):** we did not find — and we give the structural reason why it cannot be found by this route — an arithmetic free energy whose minimum locates $\Lambda$: the arithmetic evaluation exists at a single point of the $t$-axis, and a variational principle needs to compare neighboring points. Mechanism (c): collapses by transmutation.

---

## §7. Renormalization or topological protection?

### §7.1 The flow's fixed points and their universality class

The DBN flow has a poor renormalization structure: going forward ($t \to +\infty$, after rescaling) the attractor is the **crystal** (de Bruijn: for $t \ge 1/2$ reality holds; asymptotically the zeros approach a lattice — the "clock" class). It is the trivial/order fixed point. There is no known non-trivial fixed point of the deterministic flow with GUE statistics; GUE is the fixed point of the dynamics **with noise** (§3.3). The state at $t=0$ is not a fixed point of anything: the flow passes through it. Mechanism (d) in the literal sense: **does not apply** — the criticality of $t=0$ is not a rescaling fixed point of the flow itself.

### §7.2 Index quantization: topological protection and its frank reading

The most serious version of (a)/(d) in the program is the integer quantization of the order parameter: $\kappa = \mathrm{neg.ind} = 2m \in 2\mathbb{Z}_{\ge0}$ (P35; each quadruple contributes exactly 2). An integer order parameter is the hallmark of topological protection: it cannot vary continuously, only jump. Does this protect criticality? Analysis:

- What quantization DOES give: the transition $m=0 \to m=1$ is discrete; there is no "almost-true RH." The set of ¬RH worlds is separated from the RH world by an integer jump of the index. This is genuine structure (and it is exactly what makes the D-109 dichotomy falsifiable: $m$ cannot be "half a quadruple").
- What quantization does NOT give: a lower bound on $\Lambda$ as a function of $m$. From the model in §5.3: a quadruple at distance $y$ from the axis realifies at time $\sim y^2/2$; with $y$ arbitrarily small, $\Lambda$ can be arbitrarily small with $m = 1$. **There is no gap theorem "$\Lambda \in \{0\} \cup [c, \infty)$"** and the dynamics does not suggest one: quantization lives in $m$, not in $\Lambda$. (If such a gap existed with explicit $c$, RH would be verifiable by finite computation à la Polymath15 — all the more reason not to expect it cheaply.)
- And the final blow is P43: reading $m$ (the inertia) requires the positions of the zeros — the inertia is not autonomous (Doc 108). Topological protection exists *ontologically* but its detector is not arithmetically accessible. Mechanism (a)/(d) in its topological version: **collapses exactly at the value/inertia wall.**

---

## §8. The pass through the master quantifier (P43)

Final table, mechanism by mechanism — the question in (v): does the mathematical version of the mechanism require inverting average→individual?

| Mechanism | Mathematical version | Where is the quantifier? | Verdict |
|---|---|---|---|
| (a) Protective symmetry | functional eq. + Euler ⟹ zeros on the axis | the proved protection is statistical (zero density); the individual version IS MW-2 | **Collapses** (it is the wall) |
| (b) SOC / Rodgers–Tao | post-critical exclusion by rigidity | Λ<0 side: extensive order parameter → provable (and proved!); Λ>0 side: zero-density intensive parameter → individual | **Half proved, half IS the wall**; dual impossible (Prop. 5.2) |
| (c) Variational | arithmetic $F(t)$ with minimum at Λ | arithmetic exists only at $t=0$ (unique multiplicative time); comparing neighbors = zero side | **Collapses** (transmutation, Doc 99) |
| (d) RG / topological | quantization $\kappa = 2m$ | the invariant is integer (individual) but reading it = non-autonomous inertia | **Collapses** (value/inertia, Doc 108) |
| (e) Fine tuning | — | — | empty: arithmetic has no tuner; if RH is true with no mechanism, it is "accidental" — uninteresting and unfalsifiable |
| **D-109 (new)** | one defect ⟹ infinitely many defects | individual hypothesis, individual conclusion: **no average→individual inversion in the statement** | **Does NOT collapse as a statement**; known proof routes (cloning via recurrence) do re-encounter the wall in a weakened sequential version |

The expected outcome is confirmed: (a), (c), (d) collapse; (b) is half-proved and its other half is the wall. What does not collapse *as a statement* is D-109 — precisely because it is not a mechanism for anchoring Λ but a rigidity of the defect set, orthogonal to the average/individual axis.

A brutally frank caveat, so as not to oversell D-109: that the statement does not require the quantifier inversion does not mean its proof is easier than RH — it means the P43 impossibility argument **does not apply to it**. P43 showed that every form of argument in the program dies at the average→individual inversion; D-109 is the program's first natural target whose statement does not contain that inversion. There may be (and surely are) other walls; the one identified in §4.4 is the mean-square→pointwise-sequential step of near-periodicity, which is a strictly weaker form of the same difficulty (it is needed on a sequence of points, not uniformly). Whether this weakened step is as hard as the original is, today, an OPEN GAP — and it is the right question this document leaves behind.

---

## §9. VERDICT

**PARTIAL.**

**What physics mode established:**

1. **Critical anchoring has its proved half and its impossible-by-averages half.** Rodgers–Tao is genuinely mechanism (b) — exclusion of the post-critical phase by excess disorder — and it works because post-critical order is extensive. The pre-critical side has a zero-density intensive order parameter (guaranteed by Bohr–Landau in EVERY ¬RH world), so no averaged statistic separates $\Lambda = 0$ from $\Lambda > 0$ (Prop. 5.2). The relaxation sandwich is inconceivable; the master quantifier reappears as the extensive/intensive dichotomy. There is no dynamical anchoring mechanism: the critical point is not an attractor of the flow, and $t=0$ is an arithmetic initial condition, not a relaxed state.

2. **The unique multiplicative time (Obs. 6.2).** The heat flow destroys the Euler product; the $t$-axis touches arithmetic at exactly one point. RH = "the flow's critical time coincides with the multiplicative time." This buries the variational mechanism (c) for structural, not technical, reasons, and reformulates MW-2 in flow coordinates.

3. **Quantization protects ontologically, not epistemically.** $\kappa = 2m$ is an integer (real topological protection), but reading it is the non-autonomous inertia of P43. There is no gap theorem for $\Lambda$ ($\Lambda$ can be arbitrarily small with $m=1$).

**The most promising falsifiable statement:**

> **D-109 (defect dichotomy):** the set of off-critical zeros of ζ is empty or infinite ($m \in \{0,\infty\}$). Strong version: no element of the Selberg class has a finite positive number of zeros off its critical axis.

With the architectural identity $\mathrm{RH} = (m<\infty) \wedge (m\in\{0,\infty\})$: the left half is the ledger's target L8 (sieve bound, average-compatible form); the right half is D-109 (individual→individual rigidity, outside the reach of P43's no-go). It is the first partition of RH the program has produced in which the two pieces are not blocked for the same reason.

**Falsifiers of D-109:**
- Direct: construct an element of the Selberg class (with Euler product and functional equation) with exactly one off-critical quadruple, or prove the relative consistency of $m=1$ for ζ with the explicit formula + $d\nu \ge 0$ + sub-resolution positivity (Thm 3.3 of Doc 108).
- Indirect (falsifier of its usefulness): prove that every proof of D-109 requires Bagchi's strong recurrence (= RH), i.e., that the sequential version of the mean→pointwise step identified in §4.4 is equivalent to the uniform version. That would return D-109 to the wall and the verdict would drop to NO MECHANISM.

**Concrete next step (Phase 37 continuation):** attack the sequential version — does there exist a sequence $\tau_k \to \infty$ with $\zeta(s + i\tau_k) \to \zeta(s)$ uniformly on a fixed compact disk in $\tfrac12 < \sigma < 1$, unconditionally? (Note: for D-109 it suffices that *some* such sequence exist; unconditional $B^2$ near-periodicity gives candidates in the mean; the gap is mean→pointwise on a sequence, not on positive density.)

---

## Appendix: cited external references (all verified except as marked)

- N. G. de Bruijn, *The roots of trigonometric integrals*, Duke Math. J. 17 (1950), 197–226.
- C. M. Newman, *Fourier transforms with only real zeros*, Proc. Amer. Math. Soc. 61 (1976), 245–251.
- G. Csordas, W. Smith, R. S. Varga, *Lehmer pairs of zeros, the de Bruijn–Newman constant Λ, and the Riemann Hypothesis*, Constr. Approx. 10 (1994), 107–129.
- H. Ki, Y.-O. Kim, J. Lee, *On the de Bruijn–Newman constant*, Adv. Math. 222 (2009), 281–306.
- B. Rodgers, T. Tao, *The De Bruijn–Newman constant is non-negative*, Forum of Math. Pi 8 (2020), e6; arXiv:1801.05914. [Proof structure verified against source: dynamics $\dot x_j = 2\sum_{k\neq j}(x_j-x_k)^{-1}$, relaxation to local equilibrium in the Erdős–Schlein–Yau style, contradiction with Montgomery's pair correlation and CGGGH-B, use of the fact that $\Lambda<0 \Rightarrow$ RH enables conditional tools.]
- D. H. J. Polymath, *Effective approximation of heat flow evolution of the Riemann ξ-function, and a new upper bound for the de Bruijn–Newman constant*, Res. Math. Sci. (2019); $\Lambda \le 0.22$.
- H. Davenport, H. Heilbronn, *On the zeros of certain Dirichlet series*, J. London Math. Soc. 11 (1936), 181–185 and 307–312.
- E. P. Balanzario, J. Sánchez-Ortiz, *Zeros of the Davenport–Heilbronn counterexample*, Math. Comp. 76 (2007), 2045–2049.
- H. Bohr, E. Landau, *Ein Satz über Dirichletsche Reihen mit Anwendung auf die ζ-Funktion und die L-Funktionen*, Rend. Circ. Mat. Palermo 37 (1914), 269–272. [Zero off-axis density.]
- H. L. Montgomery, *The pair correlation of zeros of the zeta function*, Proc. Symp. Pure Math. 24 (1973), 181–193. [Conditional on RH.]
- A. Speiser, *Geometrisches zur Riemannschen Zetafunktion*, Math. Ann. 110 (1934), 514–521.
- N. Levinson, H. L. Montgomery, *Zeros of the derivatives of the Riemann zeta-function*, Acta Math. 133 (1974), 49–65.
- B. Bagchi, *A joint universality theorem for Dirichlet L-functions* / thesis (1981); strong recurrence ⟺ RH. [Cf. Doc 102 of the program.]
- A. Selberg, *Contributions to the theory of the Riemann zeta-function* (1946). [Unconditional CLT for $S(T)$.]
- T. Nakamura, Ł. Pańkowski, works on off-critical zeros of linear combinations of L-functions (2012–) [infinitude verified; precise counts NOT VERIFIED].
- Y. Saouter, X. Gourdon, P. Demichel, *An improved lower bound for the de Bruijn–Newman constant*, Math. Comp. 80 (2011) [exact value NOT VERIFIED].

Internal program citations: P35, P39, P41, P42, P43; Docs 70, 71, 72 (with Doc 105 corrections), 83, 89, 99, 102, 103, 104, 105, 106, 107, 108.

---

*End of Document 109.*
