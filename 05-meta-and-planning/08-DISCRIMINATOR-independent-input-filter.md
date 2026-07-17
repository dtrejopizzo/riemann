# The discriminator: an operational filter for "new object" vs "CAP/SURF in disguise"

**Auditor build · 2026-06-05.** Purpose: convert the collapse map into an *instrument*. Given any candidate
structure, decide — cheaply, before deep investment — whether it can possibly escape CAP/SURF, or is ζ re-encoded.
The filter is **calibrated on known objects** (it must correctly classify everything we already understand,
including the one *proven* RH) before it is trusted on unknowns. Working hypothesis (conceded, not proven):

> **H0.** Every RH-directed route built from positivity / spectrum / statistics / moments / explicit formula /
> cohomology / Euler products reduces to **CAP** (a center-definiteness that is RH-equivalent) or **SURF** (a
> missing arithmetic surface). *To refute H0 one needs one non-collapsing node; to prove it one needs to
> characterize all strategies. The search targets refutation.*

---

## The master discriminator

Every collapse in the corpus and the literature shares one root: the structure **re-encodes ζ's own data** (the
explicit-formula prime–zero duality) in a new language, **without injecting an input ζ does not already
determine**. The one escape on record — the function-field proof — does the opposite: it injects a **geometry
richer than the zeta function** (the surface $C\times C$ and its intersection theory are *not* reconstructible
from $Z(C,T)$ alone).

> **Master test (D0).** Does the candidate inject an **independent input** — mathematical structure **not
> reconstructible from ζ / the explicit formula** — *and* use it to constrain individual zeros? If it is "ζ
> re-encoded," it collapses. If it injects independent structure that is prime-distinguishing and
> individual-resolving, it is a genuine new class.

D0 unfolds into four **necessary** sub-conditions (the "richer-than-ζ" signature). A candidate must pass **all
four** to be a non-collapsing node:

- **I1 — Prime-distinguishing.** RH-content depends on *which* primes (prime-identity / Euler structure), not only
  on counts or ζ's coefficients. *Failure → E (self-referential) or F (statistics).*
- **I2 — Independent input.** Carries data ζ does **not** determine (a genuine new invariant of $\mathbb Z$ / the
  primes), not a relabeling of the explicit formula. *Failure → A / B / C / E.*
- **I3 — Individual-resolving.** Constrains a **single** zero (an $O(1)$ signal with bounded noise), not an
  aggregate sum / integral / moment / density. *Failure → A or F (density).*
- **I4 — Arithmetic-aware.** Depends on the actual primes; not invariant under arithmetic-blind deformation.
  *Failure → N5 / N6 (dynamical/monotone no-go).*

**Escape condition: $I1\wedge I2\wedge I3\wedge I4$.** (Necessary for a new class — *not* sufficient for a proof.
Passing means "worth deep investment," not "RH proved.")

## Calibration on known objects (the filter must reproduce what we know)

| Object | I1 prime-disting. | I2 indep. input | I3 individual | I4 arith-aware | Verdict | Matches known outcome? |
|---|---|---|---|---|---|---|
| **Function-field RH** ($C\times C$, Hodge index) | ✅ (points/Frobenius) | ✅ (geometry ⊃ $Z$) | ✅ (index pins each $\|\alpha_i\|$) | ✅ | **PASS all → proves RH** | ✅ the one positive control |
| Weil positivity / CAP | ✅ | ❌ (EF re-encoded) | ✅ | ✅ | **FAIL I2** → sign RH-equivalent | ✅ (the capstone) |
| Motohashi / Kuznetsov | ✅ | ✅ (Maass spectrum) | ❌ (4th moment = aggregate) | ✅ | **FAIL I3** → density | ✅ (density, not absence) |
| Littlewood / zero-density | ✅ | ❌ | ❌ (aggregate) | ✅ | **FAIL I2,I3** → density | ✅ |
| ω-line / $z^\omega$ (M14.3) | ❌ (prime-blind) | ❌ | — | ✅ | **FAIL I1** → self-referential | ✅ (closed) |
| RMT / CFKRS / chaos (F) | ❌ (universal) | ❌ | ❌ | ❌ | **FAIL all** → describes | ✅ (N7) |
| Lee–Yang / Fourier-quasicrystal (HYP) | ✅ | ❌ (ζ re-encoded) | ✅ | ✅ | **FAIL I2** → CAP | ✅ |
| Connes–Consani SURF | ✅ | ◐ (geometry *sought*, not yet ⊃ extra data that pins the sign) | ✅ (if index existed) | ✅ | **FAIL I2 (currently)** → RH-equivalent | ✅ (live, stuck at the index) |
| dlVP anchor | ✅ | ❌ (uses ζ's pole) | ❌ (edge region, aggregate) | ✅ | **FAIL I2,I3** → edge only | ✅ |

**The filter reproduces every known verdict** — including the single PASS (function fields) and the precise reason
each ζ-route fails (almost always **I2**: no independent input; or **I1**: prime-blind; or **I3**: aggregate). It
is therefore trustworthy as a pre-screen.

## What the calibration tells us about the search

1. **The decisive bottleneck is I2 (independent input), not positivity.** Function-field RH *uses* a positivity
   (Hodge index) — it does **not** avoid CAP; it *proves* the CAP-positivity, because the **surface supplies an
   input richer than ζ**. So the search must not seek "a non-positivity trick"; it must seek **an enrichment of
   $\mathbb Z$ richer than its zeta function.**
2. **Reformulations are guaranteed to fail.** Any candidate expressible purely in terms of ζ / the explicit
   formula / the zeros fails I2 by construction. An automated search can **reject 99% of candidates instantly**
   (they are ζ re-encodings) and spend only on enrichment candidates.
3. **Independent input alone is not enough** (Motohashi has it, fails I3). The lever needs $I1\wedge I2\wedge I3$
   together — exactly what a *geometry* provides and what analytic reformulations cannot.

## The search protocol (what to actually run, and how to spend)

> **Generate ← reject ← keep.** Generate candidate structures *attached to $\mathbb Z$ / the primes from anywhere
> in mathematics* (not the RH literature — that is the re-encoding pool). For each, run D0/I1–I4. **Reject** any
> ζ re-encoding (fails I2) at near-zero cost. **Keep** only $I1\wedge I2\wedge I3\wedge I4$ survivors for human/
> deep-compute investment.

- **Where independent input could come from** (the only I2-passing reservoir on record is *geometry*): enrichments
  of $\operatorname{Spec}\mathbb Z$ that carry data beyond ζ. The known candidate (Connes–Consani $\mathbb F_1$ /
  $\overline{\operatorname{Spec}\mathbb Z}$) currently **fails I2** because the sought geometry does not yet supply
  an input that pins the sign — it is RH-equivalent precisely there. A genuinely new node would be a *different*
  enrichment, or a non-geometric source of I2 that no one has exhibited.
- **Spend rule.** The marginal RH-*reformulation* has value ≈ 0 (guaranteed I2-failure). Fund only D0-passing
  candidates. At \$5k: build + harden the discriminator and run it over a broad candidate generator. At \$500k+:
  invest in the rare I2-survivors (if any) and on independently formalizing the function-field PASS to sharpen I2.

## Honest outcomes (both valuable)

- **Outcome A — a D0 survivor is found.** A structure passing $I1\wedge I2\wedge I3\wedge I4$ that is not ζ
  re-encoded = a **new conceptual class** (refutes H0 in spirit). Whether it proves RH is then the next question;
  but it is the first genuinely new degree of freedom the program would have produced.
- **Outcome B — no survivor after wide search.** Strong empirical support for H0: a **"limits of current
  strategies" map** — every constructible RH route is ζ re-encoded except a geometry $\mathbb Z$ is not known to
  possess. That is a publishable meta-result and a precise statement of why RH is hard, *and* it tells the
  community exactly what to build (the I2-enrichment), not what to reformulate.

## Recommendation (direct answer to "what path now")

1. **Pivot the stated goal** from "prove RH" to **"find a D0-non-collapsing node (an I2-enrichment of $\mathbb Z$),
   or map the collapse boundary."** This is the only framing with non-zero discovery probability *and* a valuable
   failure mode.
2. **Ship the discriminator** (this document) as the instrument; it is calibrated and reproduces all known
   verdicts, including the one proven RH.
3. **Run the generate-reject-keep search** with D0 as the gate. Expect to reject nearly everything; that is the
   point — the rare survivor (or its provable absence) is the deliverable.
4. **Stop producing RH reformulations.** By the calibrated filter they fail I2 *a priori*; they cannot be the
   lever, and the program has already enumerated them.
