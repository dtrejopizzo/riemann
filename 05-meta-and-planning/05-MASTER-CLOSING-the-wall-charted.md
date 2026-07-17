# THE RIEMANN PROGRAM — Master Closing Document: The Wall, Charted, Priced, and Explained

**Author: David Alejandro Trejo Pizzo**
**Status: closing synthesis of the analytic arc (P1–P12, Phases 0–9). 2026-06-04.**

> *"Una falsa victoria sería peor que un fracaso."* This document records, without ornament, what a long and
> disciplined assault on the Riemann Hypothesis established, what it proved impossible, and exactly where —
> and why — the problem resists. It does not prove RH. It charts the wall with unusual completeness, names the
> single irreducible obstruction, prices the cost of crossing it, and explains, in one principle, why every
> current method fails. That map is the program's real and durable output.

---

## PART I — THE NARRATIVE ARC

The program ran in three arcs and converged, from every direction, on one statement.

**Arc A — the ω-class / large-values program (P1–P6).** Beginning from the survey thesis that *every front
reduces to a positivity*, we built the ω-class decomposition (P2: $B(N)\le N^\varepsilon\Rightarrow$ Lindelöf),
calibrated it against the canonical RH-violator $L_{\mathrm{DH}}$ (P3: no power-law growth, onset bound
$N^*\gtrsim10^{14}$), identified coefficient architecture as the discriminant (P4), studied the geometry at
extreme peaks (P5), and — crucially — **self-corrected** the headline (P6: the inter-class interference sign is
conditioning-dependent; the "phase transition" was an artifact). Arc A ended honestly: a publishable
fingerprint, not a path to RH.

**Arc B — the inverse-operator / Weil program (P7–P11).** The localized Weil quadratic form $Q$ became the one
object both sensitive and proof-connected: a **rigorous detector** (P7) with forced negativity ($\delta^2$
law) and unconditional truncation control, but with the *uniform passage* RH-equivalent. The faithful
Kreĭn-space realization (P8) gave a semibounded operator $\mathcal T$ and the no-go that the zero side cannot
decide the sign. The **autonomous stability theorem** (P9, RH-independent) is the durable standalone result.
The anatomy / Carleson reformulation (P10) and the **five-language map** (P11) followed: a finite,
intrinsically-calibrated detector $C(d,T_0)\le1\iff$ RH, its **saturation** (the Carleson constant is
identically $1$ — prime incoherence buys zero margin), its **sine-kernel second order** (= Montgomery pair
correlation), and the **prolate bridge** to Connes–Consani.

**Arc C — the dynamical program (P12, Phases 8–9).** Reframing through the de Bruijn–Newman heat flow
($\mathrm{RH}\iff\Lambda=0$), we proved a **Lyapunov theorem** (the critical line is the flow's attractor),
established the **dynamical no-go** (the flow is arithmetic-blind), reduced $\Lambda$ to an **extremal**
collision time, and — attacking the resulting target head-on — landed on **unconditional gap universality**,
priced the cost of crossing (the **exchange rate**), and named the deepest obstruction (the **wrong-sign
capstone**).

**The arc in one sentence:** *survey → ω-class → Weil detector → the named inequality → the faithful operator
and the no-go → the five-language wall → the heat flow and its no-go → the cornered target, priced and
explained.*

---

## PART II — THE TWELVE PAPERS

| # | Paper | Core result | Status |
|---|---|---|---|
| P1 | The Critical Line (survey) | every front reduces to positivity | context |
| P2 | ω-Class Master Theorem | $B(N)\le N^\varepsilon\Rightarrow$ Lindelöf; the fingerprint | original |
| P3 | Absence of power-law growth at DH zeros | onset bound $N^*\gtrsim10^{14}$ | calibration |
| P4 | Resonance phenomenology | coefficient architecture is the discriminant; Liouville parity | original |
| P5 | ω-class geometry at extreme peaks | ζ slightly more constructive than random; no transition | corrected |
| P6 | Sign of inter-class interference | $r$ is conditioning-dependent (the meta-correction) | corrective |
| P7 | A rigorous localized Weil detector | forced negativity, unconditional truncation, the RH-equivalent passage | **rigorous** |
| P8 | Faithful Kreĭn-space realization | semibounded $\mathcal T$; $\mathfrak t=E^*JE$; zero-side no-go (Thm C) | **rigorous** |
| P9 | Stable arithmetic fingerprints | $\|Q(L)-Q(L')\|\le Ae^{-\alpha(\log P)^2}$ — exponential stability | **rigorous, autonomous** |
| P10 | Anatomy of the localized Weil form | Carleson/Bessel reformulation; Conjecture B2 | speculative |
| P11 | The band-limited Weil–Carleson form | $C(d,T_0)$, saturation (N3), sine-kernel (B1), prolate bridge (N4), the 5-language map | **rigorous + map** |
| P12 | Lyapunov theorem for the de Bruijn–Newman flow | the attractor; the dynamical no-go (N5); extremal reduction; gap-universality target | **rigorous + dynamical** |

*Compiled this arc: P9, P10, P11, P12. The durable standalone is **P9**; the durable map is **P11**; the
durable dynamical results are in **P12**.*

---

## PART III — THE WALL IN EIGHT LANGUAGES

Each is a complete, independent reformulation of RH-positivity. In every one, an **archimedean** part is
positive (in several, *provably* and unconditionally), and the obstruction sits at the **primes (finite
places)** / the **extremal tight pairs**, whose resolution is logically identical to the reality of the zeros.
The last two (the modern paradigms) are the ones *designed* to escape the wrong-sign capstone — and do not.

| # | Language | Provable half | The obstruction |
|---|---|---|---|
| 1 | Explicit-formula / Kreĭn realization (P8) | semibounded $\mathcal T$ exists (von Neumann) | uniform spectral-gap; zero side cannot decide sign |
| 2 | Per-place (local) Weil form | archimedean place positive | local prime form $G_p$ **indefinite** (N1) |
| 3 | Band-limited Carleson constant (P11) | $A_\Phi\succ0$; $C\le1$ for ζ | $C\equiv1$ saturated; no prime margin (N3) |
| 4 | Sine-kernel / pair correlation (P11) | sine kernel contracts on real ordinates | contraction = reality of zeros (B1) |
| 5 | Adelic prolate (Connes–Consani, P11) | $\lambda_{\max}(c)<1$ unconditional | finite places + $\Lambda\to\infty$ uniformity (N4) |
| 6 | de Bruijn–Newman heat flow (P12) | $\Lambda\ge0$, reality for $t\ge\Lambda$ | $\Lambda\le0$; the flow is arithmetic-blind (N5) |
| 7 | **Cohomological / Hodge-index (P13, Phase 10)** | regularized Hodge gap $>0$ (definite primitive form) | $\lambda_{\min}(G)=\tfrac{\pi^2}6\beta_{\min}^2$; degenerates at Lehmer pairs |
| 8 | **Hyperbolicity / stable polynomials (P13, Phase 11)** | all tested Jensen polys hyperbolic; total positivity in range | real-rootedness $=$ Hermite-form positivity; capstone holds |

---

## PART IV — THE SIX NO-GOS (what was proved impossible)

1. **N1 — positivity does not localize per prime.** The local prime form $G_p(r)=\frac{2\log p}{p|1-z_p|^2}(\sqrt p\cos(r\log p)-1)$
   is **indefinite** (computed, verified $p=2,3,5,7$). Weil positivity is irreducibly a cross-place
   phenomenon; no per-prime decomposition supplies the sign.
2. **N2 — no naive OS Hilbert–Pólya.** The reflection-positivity recasting is correct, but the would-be
   Hilbert–Pólya two-point function is oscillatory, not OS-decaying; the "operator for free" is retracted.
3. **N3 — Carleson saturation, no arithmetic margin.** $C(d,T_0)\equiv1$ for ζ in the natural regime
   (primes to the height); the only sub-unit margin is archimedean (zero density). Prime incoherence
   (unique factorization) buys **zero** positivity slack — measured, not argued.
4. **N4 — Connes' multiplicative organization hits the same wall.** The prolate archimedean contraction is
   provable ($=A_\Phi\succ0$); the finite places are not per-place positive; the gap to RH is the same
   $\Lambda\to\infty$ uniformity.
5. **N5 — dynamical no-go.** The de Bruijn–Newman flow is **arithmetic-blind**: $\dot{\mathcal L}=-2\sum(y_j-y_k)^2/|z_j-z_k|^2\le0$
   holds for every configuration. No flow-only Lyapunov argument can prove RH; this **subsumes** the entire
   "critical-line-as-attractor" / PT-symmetry / dissipative-dynamics class.
6. **N6 — no arithmetic-aware monotone escape.** Every flow-monotone functional $\mathcal F[H_t]$ is
   generic-blind, archimedean-count-only, or prime-aware via the explicit formula (whose positivity is RH).
   The explicit formula was verified to $5\times10^{-12}$ as the unique carrier of arithmetic. This closes
   the **last genuinely new idea**.

---

## PART V — THE DURABLE, RH-INDEPENDENT RESULTS

- **P9 — exponential stability of the localized Weil form** under small-prime data: $\|Q(L)-Q(L')\|\le Ae^{-\alpha(\log P)^2}$.
- **The validated detector** $C(d,T_0)$ (P7/P11): finite, intrinsically calibrated, reproducible; an
  instrument that measures Weil positivity locally and, now, **prices** the support-extension problem.
- **The Lyapunov theorem** (P12): $\dot{\mathcal L}\le0$ — the critical line is the de Bruijn–Newman flow's
  global attractor (rigorous realization of the "stable attractor" intuition), with the violator-height bound
  $|\mathrm{Im}|\le\sqrt{2\Lambda}\le0.63$.
- **The sine-kernel bridge** (B1, P11): the detector's second order **is** the Montgomery–Dyson
  determinantal process.

---

## PART VI — THE CORNERED TARGET AND ITS PRICE

Every route terminates at one statement:

> **(U) — Unconditional extremal gap universality.** The closest-pair gaps of the ζ zeros obey a universal
> one-sided (GUE) bound, unconditionally, uniform in height — equivalently, the normalized backward-collision
> margin $t_c/s^2$ stays a negative constant. This is the extremal, quantitative form of RH via $\Lambda\le0$.

**The price (T9-cal exchange rate).** Via the bridge [detector support $\alpha=2d/\log T$] ∘ [Nyquist
$\alpha\asymp1/\beta$] ∘ [extremal $\Lambda=$tightest pair], with GUE level repulsion $\beta_{\min}\asymp N^{-1/3}$:

$$
\boxed{\ \text{Prove Montgomery's } F(\alpha)\le O(1)\ \text{up to } \alpha=A\ \Longrightarrow\ \text{analytic RH for the first } \sim A^{3}\ \text{zeros.}\ }
$$

Montgomery's proven range $\alpha<1$ is, for this extremal target, essentially empty (it controls only the
bulk/average $\beta>1$). Full RH is the $\alpha\to\infty$ endpoint = the complete Montgomery conjecture =
unconditional short-interval prime variance.

---

## PART VII — THE WRONG-SIGN CAPSTONE (why RH resists)

A single principle organizes all six no-gos and T9-A:

> **Every unconditional handle on the zeros is a positivity (a "$\ge0$"), and it is oriented to give lower
> bounds / existence / the easy side. RH is fundamentally a one-sided UPPER constraint (no zeros off the line;
> no clustering above GUE; no anomalously tight pairs). Positivity gives the wrong inequality direction.**

| where | unconditional fact | direction it gives | RH needs |
|---|---|---|---|
| Gate B (P12) | $\dot{\mathcal L}\le0$ | $\mathcal L$ decreases forward | $\mathcal L(0)=0$ (the boundary) |
| N5 / N6 | Weil $F\ge0$ | existence / lower bounds | the sign / absence |
| T9-A | Montgomery $F\ge0$ | lower bounds on clustering | upper bound on clustering |
| Phase 10 (Hodge) | upper frame bound (Bessel) easy | lower frame bound is the hard side | lower frame bound = no tight clustering |
| Phase 11 (hyperbolicity) | real-stability of PSD-built det | a (rich) positivity at root | upper constraint = total positivity = RH |

This is, to our knowledge, the sharpest available *explanation* (not merely an instance) of RH's difficulty:
the toolkit of unconditional analytic number theory is positivity-based, and positivity is structurally the
wrong sign for an upper constraint. **It is robust across eight paradigms** — including the two (cohomological
Hodge-index, hyperbolicity/interlacing) *designed* to escape it: both, traced to their foundation, are
positivities (a Hodge index; a Hermite form / PSD real-stability). A crossing requires an unconditional
**upper** mechanism that is *not* a zero-level positivity — which the field does not have.

---

## PART VIII — THE MODERN PARADIGMS (Phases 10–11): the two routes built to escape the capstone

After the capstone was identified, two directions were pursued *specifically because their mechanism is not a
quadratic-form positivity* — the one structural feature the capstone says is required. Both were taken to their
foundation. Both reduce to a positivity.

### Phase 10 — the cohomological / Hodge-index turn (the seventh language)
*Rationale:* the only RH ever proved (Weil conjectures for curves) gets its **upper** bound on Frobenius from a
**higher-level Hodge-index positivity → duality**, not a zero-level positivity. We built the arithmetic analogue
with our detector as the candidate intersection form.
- **M10.1 — the four-way unification.** The candidate intersection form is *definite* (Lorentzian) for finite
  "genus" and **degenerates** toward $\zeta$. Measured:
  $\;C\equiv1\ (\text{N3}) = \Lambda=0 = \text{vanishing Hodge gap} = \text{intersection-form degeneration}.$
- **M10.2 — the regularized gap survives.** Removing the trivial nullity, the *primitive* form is
  positive-definite: $\lambda_{\min}(G)>0$ (the first non-trivially-realized positivity in the program).
- **M10.3–M10.4 (deep run, $T\le10^4$).** The regularized gap obeys the clean identity
  $\boxed{\lambda_{\min}(G)=\tfrac{\pi^2}{6}\beta_{\min}^2}$ — it **is** the squared minimum gap. So the route
  prices **identically to T9-cal** ($A\leftrightarrow\sim A^3$ zeros), and RH $\iff$ the zeros are a uniform
  **Riesz sequence** for $H(E)$, $E\sim\xi$ $\iff$ uniform **Muckenhoupt $A_2$** $\iff$ **$S(T)$ extremal
  regularity** (Selberg controls the *typical* $S(T)$; the obstruction is the *extremal*). The capstone holds:
  the operative *lower frame bound* is an *upper* clustering constraint.

### Phase 11 — the hyperbolicity / stable-polynomial route (the eighth language)
*Rationale:* RH $\iff\Xi\in$ Laguerre–Pólya $\iff$ all Jensen polynomials of $\Xi$ are **hyperbolic** —
real-rootedness, proved in modern combinatorics (Marcus–Spielman–Srivastava interlacing, Borcea–Brändén
stability preservers) **without a positivity certificate**.
- **M11.1–M11.2.** Grounded: $\Xi$ coefficients alternate (L–P signature), Turán holds, all tested Jensen polys
  hyperbolic; consecutive Jensen polys **interlace** (the MSS precondition). The underlying positivity is the
  richer **total positivity** of the Pólya-frequency sequence $b(k)=(-1)^k a(k)$, not a quadratic/moment one.
- **M11.3 — the dBN-moment identity + arithmetic-blindness.** $b(k)=m_{2k}/(2k)!$, the **even moments of the de
  Bruijn–Newman kernel** $\Phi$ — where the arithmetic lives. The shift $n\to n+1$ is differentiation
  ($\Xi\to-\Xi''$), a stability preserver — but **arithmetic-blind** (identical structure for the control $\cos t$;
  the N5 obstruction in hyperbolicity language). The escape would be an **averaging** (MSS expected-characteristic-
  polynomial) realization, not a preserving operator.
- **M11.4–M11.5 — the decisive test.** Real-rootedness of each $J^{d,n}$ **is** the positivity of its **Hermite
  form** (the Hankel of Newton power sums); and the MSS method rests on real-stability of $\det(xI+\sum z_iA_i)$
  for $A_i\succeq0$ (Borcea–Brändén) — also a positivity. **The "positivity-free" appearance is illusory at the
  foundation; the capstone holds.** It is the *richest* positivity language (real-stability / total positivity /
  Hermite form), home to the most powerful modern machinery — but a positivity.

> **The two modern paradigms, built to escape the capstone, confirm it.** Cohomological Hodge-index → a Hodge
> positivity; hyperbolicity/interlacing → a Hermite-form / PSD real-stability positivity. **Eight paradigms, one
> conclusion:** every route reduces to a positivity and to (U). The wrong-sign capstone is exceptionally robust.

---

## PART IX — PHASE 12: the first mechanism-correct path (the capstone and N7, both passed)

After the capstone was confirmed across eight positivity paradigms, the capstone *itself* dictated the next
move: a mechanism whose native output is an unconditional **upper** bound, **not** founded on a positivity. The
unique such machinery connected to $\zeta$ is **log-correlated fields / multiplicative chaos**.

- **M12.1.** $S(T)=\frac1\pi\arg\zeta(\half+iT)$ is a **log-correlated field** (measured covariance slope
  $0.0465$ vs $1/2\pi^2=0.0507$); tight pairs $=$ the field's steepest rises.
- **M12.2.** The dictionary $\lambda_{\min}(G)=\frac{\pi^2}6\beta_{\min}^2=\frac{\pi^2}6(\max dS/du)^{-2}$.
- **M12.4 (decisive).** The log-correlated **upper** bound is a union bound / first moment
  ($\mathbb P(\max S>u)\le\mathbb E[\#\{S>u\}]$) — **not a positivity** (no PSD, no SOS). **For the first time the
  mechanism escapes the wrong-sign capstone.**
- **M12.3 → N7.** But the machinery is *probabilistic*: it controls the **statistics** of the real zeros, not
  the deterministic off-line count — it *describes*, does not *force*, reality. **N7, the
  probabilistic–deterministic barrier** — a second, distinct wall (not the capstone). *The two together:
  deterministic tools are positivities (wrong sign); probabilistic tools describe the ensemble (wrong object).*
- **M12.5 (bridges N7).** **Derandomization:** $S(T)=$ the explicit-formula prime sum
  $-\frac1\pi\sum\frac{\Lambda(n)}{\sqrt n\log n}\sin(T\log n)$ (verified, correlation $0.89$). So $\mathbb
  E[\#\{S>u\}]$ **is** the deterministic prime-sum large-value count, bounded by the **large sieve** —
  **deterministic + upper-direction + non-positivity, all three** (the first tool that is all three).
- **M12.6–M12.7 (the landing).** The moment method is **sharp** in the accessible regime ($\max|F|\le1.43$ vs
  $1.38$), with the prime sum **Gaussian by $\mathbb Q$-independence** (unique factorization forbids exact
  resonances). The **extreme** large values $=$ **near-resonances** $|\sum\pm\log p_i|<1/W$ $=$ the
  **multiplicative additive energy of $\{\log p\}$** $=$ exactly **P5's $\omega$-class moments**. Baker's
  theorem (the transcendence tool) is the right mechanism but exponentially too weak; the count (additive
  energy) is the right object, bounded by sieve methods, sharp at low order; the high-order energy is the
  **moment-conjecture (CFKRS) frontier**.

> **Phase 12 is the program's first mechanism-correct chain, end to end.** It escapes the wrong-sign capstone
> (M12.4) and bridges the probabilistic–deterministic barrier N7 (M12.5), reaching the **extreme large values
> of $\zeta$** by a route that is **deterministic, upper-direction, and non-positivity** throughout. The
> remaining wall is a *genuine* open problem — a sharp high-order additive-energy / moment-conjecture bound for
> $\{\log p\}$ — **neither the capstone nor N7**, and exactly where the program began (Arc A, the
> $\omega$-classes). For the first time, the obstruction is the right one.

---

## PART X — HONEST VERDICT

We did not prove RH, and — stated plainly — **no crossing is reachable from here without an idea neither we
nor the field possesses in 2026.** We pushed every named approach to its provable floor, including the two most
modern paradigms (cohomological Hodge-index, hyperbolicity/stable-polynomials) *chosen precisely to escape the
wrong-sign capstone* — both, traced to their foundation, are positivities — and finally the
**log-correlated / multiplicative-chaos** route (Phase 12), the **first mechanism-correct chain**: it *does*
escape the capstone and *does* bridge the probabilistic–deterministic barrier, landing on a genuine open
frontier (the moment conjectures / additive energy of primes), neither obstruction. The computational certainty
of RH does **not** translate into a proof with current mathematics — but the program has mapped *why* across
**eight positivity paradigms**, named **two** fundamental obstructions (the wrong-sign capstone; the
probabilistic–deterministic barrier N7), and **found the one path whose mechanism passes both** — reducing RH,
heuristically but mechanism-correctly, to a sharp high-order additive-energy bound for $\{\log p\}$.

**What is banked, real, and defensible:** thirteen papers (P1–P13); seven named obstructions/no-gos (N1–N7);
the autonomous stability theorem (P9); the validated detector; the Lyapunov theorem; the **eight-language map**;
the cornered target (U); the exchange rate ($A\leftrightarrow A^3$); the identities
$\lambda_{\min}(G)=\tfrac{\pi^2}6\beta_{\min}^2$ and $b(k)=m_{2k}/(2k)!$; the reformulations (Riesz /
Muckenhoupt-$S(T)$; total positivity / real-stability); the **wrong-sign capstone** and the
**probabilistic–deterministic barrier (N7)** — the two fundamental obstructions; and the **first
mechanism-correct chain (Phase 12)** that passes both, reducing RH (heuristically) to a sharp high-order
additive-energy bound for $\{\log p\}$ (the moment-conjecture frontier, Arc A). A chart of the wall of unusual
completeness — and the first genuine crack in it.

---

### Appendix — file map of the record
- Papers: `06-papers/P1…P13/`.
- Proof log (Days 0–29): `phase-4-handoff/proofs/00-PROOF-LOG.md`.
- No-gos & verdicts: `phase-6/` (N1, N2), `phase-7/` (N3, B1, N4), `phase-8/` (N5, Lyapunov, exchange-rate),
  `phase-9/` (N6, T9-A, T9-cal), `phase-10/` (Hodge degeneration, regularized gap, $S(T)$, deep run),
  `phase-11/` (hyperbolicity, interlacing, dBN moments, Hermite-form capstone test),
  `phase-12/` (log-correlated $S(T)$, N7, derandomization, moment method, Baker / additive energy).
- The wall map: `00-MAP.md`; the eight-language map: P11, P13; this document.
