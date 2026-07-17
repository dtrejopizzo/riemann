# Research Graph — complete audit of the Riemann program corpus

**Auditor build · 2026-06-05.** Scope: map only. No proof attempt, no new conjectures, no gap-filling, no
speculation. Sources: `06-papers/` (P1–P14 + 00-INDEX), `phase-4-handoff/proofs/00-PROOF-LOG.md` (Days 0–36),
`MASTER-CLOSING-the-wall-charted.md`, `00-MAP.md`, `phase-14/*` (N7, M14.1–3, N8, BREAK-N8, anchor framework,
Stages 1–2), Arc-A `eslabones` / `03-arc-A` (P2–P6).

---

## PHASE 1 — RESEARCH OBJECTS

### Group I — RH-equivalence reformulations (the "detectors")

| ID | Name | First | Formal definition | Depends | Purpose | Status |
|---|---|---|---|---|---|---|
| **Q** | Localized Weil quadratic form | P7 | $Q(L)[g]=A_\Phi[g]-P_F[g]$, archimedean Gram minus prime Gram on band-limited $g$ | EF | local detector; $\mathrm{RH}\Leftrightarrow$ local positivity | rigorous detector; sign open |
| **𝒯** | Kreĭn-space realization | P8 | semibounded self-adjoint $\mathcal T$ with $\mathfrak t=E^*JE$ (modulo (H)) | Q, (H) | faithful operator form | Thm A modulo (H) |
| **K** | The contraction | P8 | $\mathrm{RH}\iff\|K\|\le1$ (Thm B) | 𝒯 | collapses program to one axis | rigorous |
| **C** | Band-limited Weil–Carleson constant | P11 | $C(d,T_0)=\lambda_{\max}(P_F,A_\Phi)$; $\mathrm{RH}\iff C\le1$ | Q | finite, intrinsically calibrated detector | rigorous; $C\equiv1$ (N3) |
| **λG** | Regularized Hodge gap | P13 | $\lambda_{\min}(G)=\tfrac{\pi^2}6\beta_{\min}^2$ | Q | Hodge-index route | identity proven; sign open |
| **HYP** | Jensen hyperbolicity | P13 | $\mathrm{RH}\iff$ all Jensen polys of $\Xi$ hyperbolic | — | real-rootedness route | $=$ Hermite positivity |
| **Λ** | de Bruijn–Newman constant | P12 | $\mathrm{RH}\iff\Lambda=0$ (Rodgers–Tao $\Lambda\ge0$) | heat flow | dynamical route | rigorous; $\Lambda$ open |

### Group II — Named obstructions / no-gos

| ID | Name | First | Statement | Status |
|---|---|---|---|---|
| **CAP** | Wrong-sign capstone | P13/MASTER | every unconditional handle on zeros is a positivity (lower-bound / existence oriented); RH is the one-sided **upper/sign** constraint. Confirmed across **8 paradigms** | standing methodological obstruction |
| **N1** | Positivity doesn't localize per prime | phase-6/P10 | $G_p(r)$ indefinite ⇒ no per-prime positivity | proven |
| **N2** | No naive OS Hilbert–Pólya | phase-6 | reflection-positivity recasting correct but would-be Hamiltonian not the zeros' | proven |
| **N3** | Carleson saturation | P11 | $C(d,T_0)\equiv1$ for ζ; prime incoherence buys **zero** margin | proven |
| **N4** | Connes prolate same wall | P11 | adelic prolate contraction $\lambda(c)<1$ but finite-places + $\Lambda\to\infty$ uniformity unproven | proven (same wall) |
| **N5** | Dynamical no-go | P12 | dBN flow arithmetic-blind; $\dot{\mathcal L}=-2\sum\frac{(y_j-y_k)^2}{|z_j-z_k|^2}\le0$; flow-only cannot prove RH | proven |
| **N6** | No arithmetic-aware monotone escape | phase-9 | every flow-monotone functional is arithmetic-blind | proven |
| **N7** | Probabilistic–deterministic barrier | phase-12 | log-correlated/chaos machinery controls **statistics** of real zeros, not the deterministic off-line count — describes, doesn't force | proven (2nd wall) |
| **N8** | Density→absence gap | phase-14 | claimed: absence requires square-root cancellation (RH-equivalent) | **REFUTED** (BREAK-N8) |

### Group III — Identities & exchange rates (RH-neutral structural facts)

| ID | Name | Statement | Status |
|---|---|---|---|
| **ID-Hodge** | Hodge gap = squared gap | $\lambda_{\min}(G)=\tfrac{\pi^2}6\beta_{\min}^2$ | proven |
| **ID-Jensen** | Jensen = dBN moments | $b(k)=(-1)^k a(k)=m_{2k}/(2k)!$ | proven |
| **ID-anat** | Anatomy identity | $\lambda_{\min}=R_\infty-\sum_p R_p$, $R_p=\sum_k p^{-k/2}|\widehat{u_0}(\log p^k)|^2$ | proven |
| **D2** | Gradient | $\partial\lambda_{\min}/\partial\Lambda(n)=-n^{-1/2}|\widehat{u_0}(\log n)|^2$ | proven |
| **T9cal** | Exchange rate | prove $F(\alpha)\le O(1)$ up to $\alpha=A$ ⟹ analytic RH for $\sim A^3$ zeros | proven |
| **B1** | Sine-kernel 2nd order | $C$'s subdominant spectrum = Montgomery pair correlation; $\delta^2$ off-line detection | proven |
| **U** | The cornered target | RH ⟺ unconditional GUE gap-universality / uniform $S(T)$ regularity (extremal, not typical) | the reduced target |

### Group IV — Arc-A ω-class objects (descriptive / RH-independent)

| ID | Name | Statement | Status |
|---|---|---|---|
| **ωdec** | ω-class decomposition (P2) | partition by $\omega(n)$; descriptive structure of Dirichlet partial sums | proven |
| **P2red** | $B(N)\le N^\varepsilon\Rightarrow$ Lindelöf | sufficient condition (plausibly stronger than LH) | proven (sufficiency) |
| **DHnull** | DH null (P3) | off-line zeros of $L_{DH}$ give no power-law growth to $N=10^9$; onset $N^*\gtrsim10^{14}$ | proven null |
| **MEF** | Moment-exponent fingerprint (P2/P5) | per-class moment exponents; the descriptive discriminant | proven |
| **LIOU** | Liouville parity theorem (P4) | parity counterexample; coefficient architecture (not multiplicativity) is the discriminant | proven |
| **P6cor** | Sign reconciliation (P6) | inter-class $r$ conditioning-dependent: constructive at peaks, destructive at troughs, mean 0 | proven (meta-correction) |
| **P5ref** | P5 reframed | ζ slightly **more** constructive than random at peaks; gap decays; **no transition** (transition retracted) | proven (corrected) |

### Group V — Phase 12–14 chaos / ω-spectral objects

| ID | Name | Statement | Status |
|---|---|---|---|
| **STlog** | $S(T)$ log-correlated | covariance $-\tfrac1{2\pi^2}\log|t-t'|$; freezing $\beta_c=1$; FHK max | established (not reproved) |
| **zdict** | $z=\beta^2$ dictionary (P14) | moment exponent $k^2$ = per-prime ω-weight; freezing $z_c=1$; supercritical = ω large deviations | proven core |
| **dk2** | $d_k^2=(k^2)^\omega$ (P14) | on squarefree, $d_k(n)^2=(k^2)^{\omega(n)}$ | proven |
| **BRW** | ω-hierarchy as branching random walk (P14) | depth $\log\log T$, Mertens equal-variance; depth+Bramson give both FHK terms | proven core (max not reproved) |
| **M14.1** | Additive-divisor / Motohashi | $\sum d(n)d(n+h)\sim\tfrac6{\pi^2}\sigma_{-1}(h)x(\log x)^2$; exact spectral identity | verified; gives density |
| **M14.2** | $z^\omega$ spectral modification | $\sum a(n)/n^s=\zeta^2 G_z$, $G_z=\prod_p[1+2(z-1)p^{-s}+(1-z)p^{-2s}]$; Satake $\alpha\beta=1-z$ | NON-TRIVIAL (verified) |
| **M14.3** | Self-referentiality test | $G_z=\prod_N\zeta(Ns)^{c_N}$, $c_N=-\tfrac1N\sum_{k|N}(\alpha^k+\beta^k)\mu(N/k)$ — ζ-isobaric | **SELF-REFERENTIAL** (verified) |
| **B2conj** | Conjecture B2 (P10) | factorizing localized-Weil anatomy $\iff$ Euler product | open, RH-**independent** |
| **P9fp** | Stable arithmetic fingerprints (P9) | $\|Q(L)-Q(L')\|\le Ae^{-\alpha(\log P)^2}$ if local data agree to $P$ | proven, RH-**independent** |

### Group VI — Phase-14 frontier objects (the anchor line)

| ID | Name | Statement | Status |
|---|---|---|---|
| **dlVP** | de la Vallée Poussin absence | $\zeta(1+it)\ne0$ by $2(1+\cos\theta)^2\ge0$ + the pole; **no cancellation** | classical; refutes N8 |
| **ANCH** | Anchor = Landau singularity | the forced real boundary singularity of a positive-measure transform (Landau 1905) | ζ-free object (Stage 1) |
| **ThmA** | Abstract zero-free region | positivity datum + Landau anchor + budget + non-neg cosine poly ⇒ region of reach $1/B(\gamma)$ | proven; = classical edge machinery |
| **Qanch** | Q(anchor) | does a positive structure exist with a forced Landau singularity at $\sigma=\tfrac12$? | **COLLAPSES** (Stage 2) |
| **DEF** | Definiteness (taxon) | signature of a form/operator (Hodge index / Weil / self-adjoint) acting at the **center** | $=$ CAP |
| **SURF** | Missing arithmetic surface | a Hodge index theorem on a 2-dim geometry over $\mathrm{Spec}\,\mathbb Z$ ("$\mathrm{Spec}\,\mathbb Z\times_{\mathbb F_1}\mathrm{Spec}\,\mathbb Z$") | RH-equivalent target (= CAP) |

---

## PHASE 2 — DEPENDENCY GRAPH (edges with justification)

```
EF (explicit formula) ──USES──► Q ──SPECIALIZES──► C (band-limited)
Q ──DERIVES_FROM──► 𝒯 ──EQUIVALENT_TO──► K            [Krein identity 𝔱=E*JE]
Q ──IMPLIES──► ID-anat, D2                              [decomposition + gradient of λ_min]
C ──IMPLIES──► N3                                       [C≡1 saturation]
C ──IMPLIES──► B1                                       [2nd order = pair correlation]
C ──REQUIRES──► N4                                      [Connes prolate, same uniformity gap]
λG ──EQUIVALENT_TO──► C                                 [both = local Weil positivity]
λG ──IMPLIES──► ID-Hodge
HYP ──EQUIVALENT_TO──► CAP                              [real-rootedness IS Hermite positivity]
Λ ──REQUIRES──► N5, N6                                  [flow arithmetic-blind]
Q,C,λG,HYP,𝒯,Λ ──COLLAPSES_TO──► CAP                    [all are positivities; sign undecided]
P8-ThmC ──REFUTES──► (zero-side can decide sign)        [no-go: it cannot]

N1..N6,N7 ──SPECIALIZE──► CAP/U                         [one principle: lower bound ≠ upper/sign]
N7 ──DERIVES_FROM──► STlog                              [chaos controls statistics not count]
U ◄──REQUIRES── C,Λ,λG                                  [all corner to gap-universality]
T9cal ──USES──► B1                                      [support↔Nyquist↔zeros pricing]

ωdec ──IMPLIES──► P2red, MEF
P6cor ──REFUTES──► (P5 "phase transition")  ──► P5ref
MEF ──EQUIVALENT_TO──► zdict ──EQUIVALENT_TO──► BRW ──EQUIVALENT_TO──► STlog   [P14: one object]
zdict ──USES──► dk2
BRW ──IMPLIES──► (both FHK terms)

M14.1 ──USES──► Motohashi ──IMPLIES──► density(not absence)
M14.2 ──DERIVES_FROM──► z^ω weight ──IMPLIES──► G_z
M14.3: G_z ──COLLAPSES_TO──► E (ζ-isobaric)            [constant Satake ⇒ ∏ζ(Ns)^{c_N}]
ω-line ──COLLAPSES_TO──► E                              [prime-blind ⇒ self-referential]

dlVP ──REFUTES──► N8                                    [exact absence, no cancellation]
dlVP ──SPECIALIZES──► ThmA ──DERIVES_FROM──► ANCH
Qanch ──COLLAPSES_TO──► DEF ──EQUIVALENT_TO──► CAP      [Stage 2: function-field anchor = trivial cohomology; RH uses Hodge index]
SURF ──EQUIVALENT_TO──► CAP                             [missing index theorem = Weil positivity]
P9fp, B2conj ──(no edge to RH)──                        [RH-independent]
```

---

## PHASE 3 — COLLAPSE ANALYSIS (per object → category A–G + chain)

Categories: A prime-sum cancellation · B explicit-formula machinery · C Weil positivity · D known spectral
theory · E ζ-isobaric/self-referential · F statistical large-value theory · G genuinely new.

| Object | Cat | Reduction chain |
|---|---|---|
| Q, C, 𝒯, K, λG, HYP | **C** | detector → local Weil positivity → Weil criterion (sign) → CAP |
| Λ (dBN) | **C/D** | flow → Lyapunov attractor → reality = positivity → N5 → CAP |
| N1–N6 | **C** | each → "lower bound ≠ sign" → CAP |
| N7 | **F** | chaos → controls statistics → cannot force count → barrier |
| N8 | **A** (and **refuted**) | density → square-root cancellation … but dlVP shows absence ≠ cancellation ⇒ N8 false as a universal law |
| Littlewood | **A** | $\int\log|\zeta|$ → prime-sum cancellation → density |
| Motohashi / M14.1 | **B/D** | 4th moment → off-diagonal $\sum d(n)d(n+h)$ → spectral (Maass) → density |
| M14.2 / G_z | **E** | $z^\omega$ → constant Satake → ζ-powers |
| M14.3 | **E** | $G_z=\prod_N\zeta(Ns)^{c_N}$ → self-referential |
| ω-line (P14 → zeros) | **E** | prime-blind → ζ-isobaric → self-referential |
| zdict, BRW, dk2 | **F → G** | moments = ω-weight = chaos = BRW; rigorous core is **new** but **RH-independent** |
| ANCH / ThmA | **D** | anchor = Landau singularity → classical positive-coefficient zero-free machinery; ceiling = **edge** |
| Qanch | **C** | center-anchor → (Stage 2) function-field anchor = trivial cohomology (edge); RH via Hodge index = DEF = CAP |
| SURF | **C** | missing arithmetic-surface index theorem = Weil positivity = CAP |
| dlVP | — | the one **uncollapsed-but-classical** fact; refutes N8; only edge regions |
| P9fp | **G** | stability theorem; **new, RH-independent** |
| B2conj | **G** | factorization ⟺ Euler product; **un-reduced, RH-independent** |
| ωdec, P2red, MEF, DHnull, LIOU, P6cor, P5ref | **F** | descriptive ω-statistics / value theory (Arc A) |

**Headline:** every **RH-directed** object collapses to **C (Weil positivity / CAP)** or to **A/E** (cancellation
/ self-referential). The only **G** (genuinely new) objects — P14's BRW/zdict, P9fp, B2conj — are all
**RH-independent**.

---

## PHASE 4 — CYCLE DETECTION

| # | Cycle | Why it is a cycle | Severity |
|---|---|---|---|
| C1 | C → N3 → "$C\equiv1$ = Λ=0 = vanishing Hodge gap" → λG → C | the detectors are **mutually equivalent restatements** of local Weil positivity; proving one "needs" another that needs the first | **structural, benign** (known: all RH-equivalent) — but means no detector is an independent lever |
| C2 | Qanch → SURF → DEF → CAP → (Weil positivity at center) → Qanch | the "new" center-anchor question routes back to Weil positivity, which is the thing it was meant to supply | **high** — hidden RH-equivalence; flagged & resolved in Stage 2 |
| C3 | U ← C, Λ, λG → U (gap-universality) | all roads corner to GUE gap-universality, which is itself RH-strength for the extremal regime | **medium** — the target is RH-hard, not a reduction to something easier |
| C4 | ω-line: M14.2 → G_z → ζ-powers → ζ-zeros → (back into ζ) | the ω-weight "sees" the zeros only because it is built from ζ | **fatal to the line** (self-reference); correctly closed (M14.3) |
| C5 | HYP → real-rootedness → Hermite positivity → CAP → HYP | the "non-positivity" route is a positivity in disguise | **high** — the capstone re-imposed; documented |

**Hidden-RH-assumption audits passed:** N8's claimed RH-equivalence (BREAK-N8 caught the over-reach: dlVP is
absence without RH-strength cancellation); the anchor framework's merge of "anchor" and "definiteness" (Stage 2
caught it — DEF = CAP is RH-equivalent, ANCH is not but is edge-only).

---

## PHASE 5 — NOVELTY DETECTION (category G)

Only three objects are genuinely G. **All are RH-independent.**

1. **P14 BRW/zdict/dk2 (ω-hierarchy = chaos = moments).**
   - *Why not collapsing:* the dictionary $z=\beta^2$ with the rigorous core $d_k(n)^2=(k^2)^{\omega(n)}$ and the
     equal-variance ($\log\log T$-depth) branching structure is a genuine new identification across four
     previously separate descriptions (moments / chaos / ω-large-deviations / BRW). Not a restatement of a single
     prior framework.
   - *Confidence:* high that it is new mathematics; high that it is **RH-independent** (nothing conditional on or
     implying RH — the maximum step is the established chaos picture, not reproved).
   - *Required verification:* the FHK subleading term via Bramson is **cited**, not reproved here; a full
     independent proof of the maximum would be the open verification.

2. **P9fp — exponential stability of localized Weil functionals.**
   - *Why not collapsing:* a quantitative continuity/stability theorem ($\|Q(L)-Q(L')\|\le Ae^{-\alpha(\log
     P)^2}$) about the **functional**, not the zeros. Standalone.
   - *Confidence:* high (proven in P9).
   - *Required verification:* none outstanding for the stated theorem; its RH-relevance is **nil** by design.

3. **B2conj — factorizing anatomy ⟺ Euler product.**
   - *Why not collapsing:* a classification statement about $L$-functions (prime-**identity** structure), not
     about zero location; the audit (AUDIT-P7) found it the **single un-reduced** object in the structural line.
   - *Confidence:* genuinely open; not obviously reducible to A–F.
   - *Required verification:* a precise formulation + a proof/disproof; **but** it is RH-independent — using its
     Euler-product side for the zeros routes through EF (category B/A).

*Borderline (not counted G):* **ANCH (anchor = Landau singularity)** is a real ζ-free object (Stage 1, Theorem A),
but its mechanism **is** the classical positive-coefficient zero-free-region machinery (category D) with an
edge-only ceiling — novelty is conceptual framing, not mechanism.

---

## PHASE 6 — RESEARCH FRONTIER

1. **Strongest surviving object.** **P7's localized Weil form Q** (with its rigorous descendants 𝒯, K, C). It is
   the only object carrying **new rigorous theorems** (explicit-constant forced negativity, unconditional
   truncation control) and it names the RH-equivalent inequality exactly. Surviving = rigorous and central; **not**
   surviving = a lever (its sign is CAP).

2. **Strongest surviving conjecture.** **U — RH ⟺ unconditional GUE gap-universality / uniform extremal $S(T)$
   regularity.** It is the common corner of C, Λ, λG, and T9cal; the most compressed RH-equivalent target the
   program produced. (RH-equivalent, not weaker.)

3. **Strongest surviving non-collapsed direction.** **B2conj** (factorizing anatomy ⟺ Euler product) — the one
   object the collapse audits did not dispose of. **Caveat:** RH-independent (classification, not zero location).
   The strongest *new mathematics* is **P14** (RH-independent).

4. **Strongest surviving RH-directed direction.** **SURF** — a Hodge index theorem on a 2-dimensional arithmetic
   geometry over $\mathrm{Spec}\,\mathbb Z$ (the Connes–Consani / Deninger / Arakelov target). It is the least-
   collapsed *restatement* and is corroborated by the one **proven** RH (function fields use exactly a Hodge index
   theorem on $C\times C$). **Honest caveat:** it is **RH-equivalent** (= CAP via DEF), i.e., a sharper statement
   of the wall, not an independent lever.

5. **Strongest evidence the program has no path to RH (as mapped).**
   - **P8 Theorem C (no-go):** the zero-side cannot decide the sign — the explicit-formula/zero-side line is
     closed from within.
   - **Five-sided convergence:** every RH-directed branch (positivity, dynamics, probability, cohomology,
     cancellation) collapses to the **same** object (CAP / Weil positivity / U). Cycles C1–C5 show the detectors
     are mutually-equivalent restatements, not independent levers.
   - **The function-field control (Stage 2):** even where RH is **true and proven**, the mechanism is a
     definiteness (Hodge index) theorem — exactly the object ζ lacks — and the "anchor" there is the trivial-
     cohomology edge pole, present for ζ already. So the missing ingredient is a **geometry** (SURF), absent for
     $\mathrm{Spec}\,\mathbb Z$, not a technique reachable from the current corpus.
   - **Net:** no mapped object provides an unconditional handle on the sign / the extremal upper bound. Every
     RH-directed lever is RH-equivalent. **No non-RH-equivalent path to RH survives in the corpus.**

---

### One-paragraph map summary
The corpus is a single investigation that (i) built a rigorous localized **Weil-positivity detector** (P7–P11,
objects Q/𝒯/K/C/λG) and proved its sign is the whole problem; (ii) confirmed the **wrong-sign capstone** across
eight positivity paradigms and named two further walls (**N7** probabilistic–deterministic, and the now-**refuted
N8**); (iii) produced genuinely new but **RH-independent** mathematics (P14 ω-hierarchy/chaos/BRW; P9 stability;
B2conj); and (iv) in Phase 14, broke its own over-claims (N8 via de la Vallée Poussin; the anchor framework via
the function-field test), arriving at the sharpest statement of the wall: **a missing Hodge index theorem on a
2-dimensional arithmetic geometry over $\mathrm{Spec}\,\mathbb Z$** — RH-equivalent, corroborated by the one
proven RH, and the single RH-directed direction left standing, with no independent (non-RH-equivalent) lever
anywhere in the graph.
