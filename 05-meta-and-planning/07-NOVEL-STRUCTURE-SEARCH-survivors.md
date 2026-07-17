# Autonomous novel-structure search — literature-merged, adversarially audited

**Auditor build · 2026-06-05.** Objective: not to prove RH, but to find genuinely new structures that survive
collapse + adversarial destruction. Discipline: every candidate is attacked before it is kept; literature
precedent is checked. Honest prior (from the corpus's own track record): most/all RH-directed candidates collapse.
**They do.**

---

## STEP 1–2 — Literature ingestion & graph merge (nodes added to the corpus graph)

| Lit node | What it is | Merge edge to corpus |
|---|---|---|
| **Connes–Consani** "Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$" (2024), "On the Jacobian of $\mathrm{Spec}\,\mathbb Z$" (2026), $\mathbb S[X]$/absolute geometry | the live program building a 2-dim arithmetic geometry over $\mathbb F_1$ | **= SURF** (EQUIVALENT_TO CAP) |
| **Kurasov–Sarnak** Fourier quasicrystals via Lee–Yang polynomials (2020–24) | crystalline measures $\Leftrightarrow$ stable (Lee–Yang) polynomials; *every* 1-D FQ is Lee–Yang | reality of zeros $\to$ **= HYP** (Lee–Yang = stable = Hermite positivity = CAP) |
| **Deninger** dynamical Lefschetz / leafwise cohomology | $\Xi$ as a regularized determinant; RH $\Leftrightarrow$ positivity of a trace pairing | **= CAP** (trace-pairing positivity) |
| **Arias de Reyna / Dyson** explicit formula as a quasicrystal/tempered distribution | RH $\iff$ the zero measure is a tempered distribution | **B/E** (EF restatement) |
| **Nyman–Beurling / Báez-Duarte** | RH $\iff$ $\mathbf 1\in\overline{\mathrm{span}}\{\rho_\theta\}$ in $L^2(0,1)$ | **C** (approximation/positivity) |
| **Li criterion** | RH $\iff\lambda_n\ge0\ \forall n$ | **C** (a positivity) |
| **de Branges** canonical systems / Sonine spaces | structural Hermite–Biehler reality | **= N2 / C** |
| **Carneiro–Littmann–Vaaler** Beurling–Selberg extremal majorants + EF | one-sided bounds on $N(T)$, gaps | **B/C** (majorant = positivity) |
| **Berry–Keating / $xp$** | conjectural $H$ with spectrum $=\{\gamma\}$ | **= Hilbert–Pólya / DEF** |
| **Random matrix / CUE, moments (CFKRS), ratios** | statistics of zeros | **F** |

**Merged-graph headline:** every literature node that touches the **sign/reality** of the zeros lands on **CAP**
(positivity) or **SURF** (Connes–Consani geometry, itself RH-equivalent) or **F** (statistics). The corpus's
five-sided collapse is **independently reproduced by the literature**.

## STEP 3 — Collapse filter (discarded as reducible)

Discarded: Nyman–Beurling, Li, de Branges, Berry–Keating, Weil-criterion variants, Connes trace formula, Deninger
Lefschetz, Carneiro–Littmann majorants (→ known positivity / EF / spectral); zero-density + mollifiers
(Levinson/Conrey/short-mollifier 2024) (→ known density machinery, gives proportion not absence); CFKRS / ratios /
RMT (→ statistics); Arias de Reyna quasicrystal-as-tempered-distribution (→ EF restatement); **the $z^\omega$ /
isobaric line** (→ self-referential, M14.3).

## STEP 4–5 — Candidate structures, each attacked to destruction

Four candidates were constructed to *try* to escape the filter. Each is destroyed; the precedent is named.

### Candidate A — "Crystalline rigidity forces reality without positivity"
*Idea:* the explicit formula makes (zeros, primes) a Fourier-dual pair; Fourier-quasicrystal **rigidity** (Meyer-set
structure) might force the zeros onto a line by *discreteness*, not positivity.
**Attack / verdict — DESTROYED.** Kurasov–Sarnak: *every* 1-D $\mathbb N$-valued Fourier quasicrystal is the
torus zero set of a **Lee–Yang (stable) polynomial**. "Reality of the support" **is** the Lee–Yang property **is**
real-rootedness **is** Hermite-form positivity $=$ **HYP $=$ CAP**. The rigidity is positivity in disguise.
*Cycle:* C5 (corpus) reappears verbatim. Literature precedent: [arXiv:2307.13498].

### Candidate B — "Edge anchor reflected to the center by the functional equation"
*Idea:* `dlVP` gives a cancellation-free **anchor** at $s=1$ (pole); $\zeta(1-s)$ gives one at $s=0$; combine the two
edge anchors through $\xi(s)=\xi(1-s)$ to squeeze toward $s=\tfrac12$.
**Attack / verdict — DESTROYED.** The functional-equation-symmetrized positivity anchored at the center **is**
the Weil/de Branges form — i.e., **CAP**. Reflection creates *symmetry*, not a *new Landau singularity* at
$\tfrac12$ (there is no pole there). This is precisely the Stage-2 finding: the center is reached by
**definiteness**, never by an anchor. *Cycle:* C2. No new object.

### Candidate C — "Integrality index: $N_{\mathrm{off}}=\dim H$ of a group structurally $=0$"
*Idea:* express the off-line zero count as an **integer-valued** cohomological index, forced to vanish by an
integrality/torsion argument (the function-field mechanism: zeros are algebraic integers).
**Attack / verdict — DESTROYED.** Realizing $N_{\mathrm{off}}$ as an index is exactly Deninger's
arithmetic-Lefschetz program, and there **RH $\Leftrightarrow$ positivity of the trace pairing** $=$ **CAP**.
The integrality that does the work in the function-field case is supplied by the **surface $C\times C$** (SURF),
absent for $\mathrm{Spec}\,\mathbb Z$. No new lever. Literature precedent: Deninger; Connes–Consani.

### Candidate D — "Absolute Riemann–Roch inequality as an upper bound"
*Idea:* use Connes–Consani Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$ to derive an $h^0$-type
**inequality** bounding zeros from the *upper* side (escaping the lower-bound capstone).
**Attack / verdict — DESTROYED (= SURF).** This **is** the Connes–Consani program; their published Riemann–Roch
does **not** yield RH precisely because the **$H^1$ / genus term and the Hodge-index (definiteness) at the center
are the missing ingredients** — i.e., it stops at exactly CAP. RH-equivalent, live, **not novel**. Literature
precedent: [Connes–Consani 2024/2026].

### The one survivor — Candidate S = **B2conj** (corpus, P10), re-examined against the literature
*Statement:* a **factorizing** localized-Weil **anatomy** $\mu_u$ $\iff$ an **Euler product**.
**Adversarial audit:**
- *Circularity?* No — it is a statement about the **prime-identity (multiplicative)** structure of an
  $L$-function's localized Weil form, not about its zeros; it does not presuppose RH.
- *Hidden RH?* No — it is RH-**independent** (it discriminates $\zeta$ from $L_{\mathrm{DH}}$ by *anatomy*, a
  classification, not by zero location).
- *Equivalent to a known framework?* Not found. It is adjacent to "converse theorems" (Weil, Cogdell–Piatetski-
  Shapiro: functional equations ⟹ automorphy) and to Selberg-class axioms, **but** those characterize via
  functional equations / Dirichlet-series identities, **not** via a *localized-Weil-form anatomy measure*. No
  literature precedent located for the anatomy-factorization characterization.
- *Trivial reformulation?* The forward direction (Euler product ⇒ factorizing anatomy) is plausibly soft; the
  **converse** (factorizing anatomy ⇒ Euler product) is the non-trivial, un-reduced content.
- **Survives** — as a genuinely new, well-posed, RH-*independent* structural question. *It does not support an RH
  proof:* using its Euler-product side for the zeros routes back through EF (B/A).

## STEP 6 — Surviving proposals (only survivors)

### Proposal S1 — B2conj (anatomy-factorization characterization of Euler products)
- **Precise definition.** For the localized Weil form $Q(L)$ of an $L$-function in a suitable class, let $\mu_u$ be
  its per-prime **anatomy measure** ($\lambda_{\min}=R_\infty-\sum_pR_p$). Conjecture: $\mu_u$ **factorizes over
  primes** $\iff$ $L$ has an **Euler product**.
- **Relation to RH.** None direct. It is a *classification* lever (prime-identity axis), orthogonal to zero
  location. Value: it is the **only** corpus/literature object that survives both collapse and adversarial audit
  while being genuinely new.
- **Novelty assessment.** Medium-high: no precedent found; distinct from converse theorems (those use functional
  equations, not anatomy measures).
- **Failure modes.** (i) The converse may be false (a non-Euler $L$ with accidentally factorizing anatomy). (ii)
  It may reduce to a converse theorem once "anatomy" is unfolded into Dirichlet coefficients. (iii) Even if true,
  RH-irrelevant.
- **Verification roadmap.** (1) Pin a precise function class + the exact meaning of "factorizes." (2) Test
  $\zeta$ (factorizes, has Euler product) vs $L_{\mathrm{DH}}$ (must *not* factorize) numerically via the existing
  P10/P9 anatomy code. (3) Attempt the forward direction rigorously; (4) attack the converse, watching for
  collapse to a converse theorem.

### Proposal S2 — P14 (ω-hierarchy = chaos = moments = BRW) *[reported, not RH-directed]*
- Genuinely new mathematics (the $z=\beta^2$ dictionary, $d_k^2=(k^2)^\omega$, the $\log\log T$-depth BRW giving
  both FHK terms). **RH-independent by construction** (M14.3: prime-blind ⇒ self-referential). Survives novelty;
  fails RH-direction. Listed for completeness as the strongest *new* object the program produced.

## Honest verdict of the search

> **No genuinely-new, RH-*directed* structure survives.** Every candidate that touches the sign/reality of the
> zeros collapses — under both the corpus audit and the independent 2024–2026 literature — to **CAP** (Weil/Lee–
> Yang/Deninger positivity) or to **SURF** (the live, RH-equivalent Connes–Consani geometry) or to **F**
> (statistics) or to **E** (self-reference). The only survivors of adversarial audit are **RH-independent**
> (B2conj; P14). The search reproduces, from the outside, the program's central finding: the wall is a single
> object (definiteness at the center / a missing arithmetic surface), it is RH-equivalent, and no current
> structure — in the corpus or the literature — is a non-RH-equivalent lever on it.

**Sources:** Kurasov–Sarnak Fourier quasicrystals / Lee–Yang ([arXiv:2307.13498](https://arxiv.org/abs/2307.13498));
Connes–Consani Riemann–Roch for $\overline{\mathrm{Spec}\,\mathbb Z}$ ([sciencedirect S0007449723000672](https://www.sciencedirect.com/science/article/abs/pii/S0007449723000672),
[JHU Publ. 2026](https://math.jhu.edu/~kc/Publ2026.pdf)); Connes 2026 RH letter ([arXiv:2602.04022](https://arxiv.org/pdf/2602.04022));
explicit-formula quasicrystal ([arXiv:2402.10604](https://arxiv.org/abs/2402.10604)); Deninger trace-pairing
positivity (ResearchGate 226107260); short mollifiers 2024 (AIM).
