# Phase C — the library of admissible constraint-theorems, the matcher, and the systematic blocker map

**Auditor build · 2026-06-05.** Phase B made I2b checkable but expert-bound: it needs (1) a finite **library** of
admissible general theorems $T$ (the only ones that have ever *forced* eigenvalues/zeros to a locus), and (2) a
**matcher** protocol. Phase C builds both and *runs* the matcher over the library against $\zeta$, producing the
complete table: *for each general positivity theorem, the precise structure that would let it apply to $\zeta$,
and the exact blocker.* No gap is filled; every row carries its identified obstruction. The blockers then cluster.

---

## 1. The library of admissible $T$ (constraint-supplying general theorems)

These are the theorems that, in their native class, deliver a *forced* locus for eigenvalues/zeros as a
**corollary** (not an object-special fact). The reservoir is small.

| $T$ | Native class $\mathcal C$ | What it forces (corollary) | Mechanism type |
|---|---|---|---|
| **T1 Hodge index** | smooth projective **surfaces** | signature $(1,\rho{-}1)$ on $\mathrm{NS}$ ⟹ $\|\alpha_i\|=\sqrt q$ | intersection positivity |
| **T2 Weil II / purity** (Deligne) | varieties over $\mathbb F_q$, $\ell$-adic sheaves | $\|$Frobenius eigenvalues$\|=q^{w/2}$ | weight/purity |
| **T3 Hodge–Riemann** (Kähler) | compact Kähler / proj. varieties | signature on primitive $H^k$ | Kähler positivity |
| **T4 combinatorial Hodge–Riemann** (Adiprasito–Huh–Katz) | matroids, Lorentzian polys, fans | log-concavity / real-rootedness of char. polys | combinatorial HR |
| **T5 spectral theorem** | self-adjoint operators (spectrum independently known) | real spectrum | self-adjointness |
| **T6 Stepanov auxiliary-function** | curves with a function field richer than $Z$ | point-count bound ⟹ $\|\alpha_i\|=\sqrt q$ | Riemann–Roch existence |

*(Bochner/positive-definiteness and the Weil explicit-formula pairing are deliberately **excluded**: there the
constraint is the object-special positivity itself — that is CAP, not a general $T$.)*

## 2. The matcher protocol (runnable filter)

> Given a candidate structure $X$ purporting to constrain $\zeta$'s zeros:
> 1. **Identify the class.** What $\mathcal C$ does $X$ inhabit?
> 2. **Library lookup.** Is there $T\in\{T1..T6\}$ (or a *new*, independently-proven general theorem) holding for
>    all of $\mathcal C$?
> 3. **Corollary test (I2b).** Does $T$ applied to $X$ yield the off-line bound as a *corollary*, or must the
>    bound be established *specially for $X$*? Special ⟹ **REJECT** (= RH restated).
> 4. **Existence test (I2a).** Is $X$ (the object placing ζ in $\mathcal C$) actually *constructed*, or only
>    wished for? Wished ⟹ **OPEN** (if a $T$ would apply) or **REJECT** (if none would).
> 5. **No library match.** If $X$'s class carries *no* known general $T$, flag **NEW-THEOREM-REQUIRED** — the
>    genuine-discovery zone.

This is mechanical **except** steps 2/5 for a *novel* $\mathcal C$ — recognizing whether a new class admits a
general positivity theorem is a research act (Phase B's residual).

## 3. Running the matcher: the ζ-embedding table (every row blocked, blocker named)

| $T$ | What ζ-embedding would be needed | Precise blocker | Status |
|---|---|---|---|
| **T1 Hodge index** | a **surface** $\operatorname{Spec}\mathbb Z\times_{\mathbb F_1}\operatorname{Spec}\mathbb Z$ with intersection theory | the surface / $\mathbb F_1$-base does not exist as a geometric object with a working intersection form (RR exists; the $H^1$/index does not) | **OPEN** (Connes–Consani) |
| **T2 Weil II** | a **finite base** under $\operatorname{Spec}\mathbb Z$ so zeros are Frobenius weights | $\operatorname{Spec}\mathbb Z$ has no finite base; the archimedean place is not a closed point of a curve | **REJECT/OPEN** |
| **T3 Hodge–Riemann** | an independently-defined **Hodge structure / cohomology** whose Frobenius-analogue has the zeros as eigenvalues | no such cohomology on $\operatorname{Spec}\mathbb Z$ (Deninger's missing $H^1$) | **OPEN** (Deninger) |
| **T4 combinatorial HR** | ζ's **Jensen polynomials** realized as char. polys of a matroid / Lorentzian object | placing them there = proving hyperbolicity = **RH itself** (object-special) | **REJECT** (= HYP) |
| **T5 spectral theorem** | a self-adjoint operator whose spectrum is **independently** the zeros | every candidate operator is reverse-engineered from the zeros, or (Berry–Keating) does not actually have them as spectrum | **REJECT** (Hilbert–Pólya) |
| **T6 Stepanov** | a **function field richer than ζ** over $\operatorname{Spec}\mathbb Z$ | $\mathbb Q$'s "functions" (the rationals) do not form a field over a base providing the auxiliary-function room | **REJECT/OPEN** |

**No row passes.** Each general theorem has a single, named obstruction to applying to ζ.

## 4. The blockers cluster (the systematic payoff)

The six blockers are **not independent**. They reduce to a small root set:

- **R1 — no second dimension / no $\mathbb F_1$-base.** $\operatorname{Spec}\mathbb Z$ is "one-dimensional" with
  nothing under it; no surface, no finite base, no Frobenius. *Blocks T1, T2, T6.*
- **R2 — no independent cohomology/Hodge structure** carrying the zeros as eigenvalues. *Blocks T3.*
- **R3 — no independent self-adjoint operator** with the zeros as spectrum. *Blocks T5.*
- **R4 — the object-special trap.** Any *known* embedding into a positivity class (T4/HR, Bochner) requires proving
  the positivity by hand = RH. *Blocks T4 and the CAP detectors.*

And **R1, R2, R3 are facets of one thing** — the absence of an *arithmetic geometry of $\operatorname{Spec}\mathbb Z$
richer than ζ* (a surface ⟺ a cohomology ⟺ a geometric operator; in the function-field world these three are the
same object, supplied by the curve). This is **SURF**, re-derived a third time, now as the common root of every
library blocker. **R4 is the separate trap that catches every attempt to skip the geometry and assert the
positivity directly.**

> **Phase-C structural result.** Across the complete library of constraint-supplying general theorems, **every**
> route to RH is blocked by either **R1–R3 (the missing $\operatorname{Spec}\mathbb Z$-geometry richer than ζ =
> SURF)** or **R4 (the object-special trap = CAP)**. There is no third blocker, and no library theorem evades both.

## 5. What this hands to a search (the only fundable targets)

The matcher partitions all future candidates into exactly three actionable bins:

1. **REJECT** — fails the corollary test (R4) or inhabits a class with no general $T$. *Cost: ~0. This is the
   entire ζ-reformulation corpus and most "new" ideas.*
2. **OPEN-on-SURF** — attempts to build the missing $\operatorname{Spec}\mathbb Z$-geometry so T1/T2/T3 apply
   (Connes–Consani, Deninger). *Live, RH-equivalent, pursued by the field's strongest groups; fund only marginal/
   complementary contributions.*
3. **NEW-THEOREM-REQUIRED** — a candidate class $\mathcal C$ carrying a *new* general positivity theorem (the
   Adiprasito–Huh–Katz template: a positivity proven for a genuinely new class) into which ζ's data embeds
   **without** the object-special trap. *This is the only bin that could refute H0. It is empty today; whether it
   is non-empty is the genuine open question, and it is where a high-risk search has its only non-zero-probability
   payoff.*

> **The fundable question, final form.** Not "prove RH," not "reformulate RH," but: **does there exist a new
> general positivity theorem $T$ for a class $\mathcal C$ such that ζ's zeros embed in $\mathcal C$ and the
> off-line bound is a corollary of $T$ — bypassing both the missing-geometry root (R1–R3) and the object-special
> trap (R4)?** A positive answer is a new conceptual class (and likely RH). A thorough negative — no such $T$
> findable — upgrades H0 from working hypothesis toward a *characterization theorem of why RH resists*: every
> constraint-supplying general theorem is blocked by the missing $\operatorname{Spec}\mathbb Z$-geometry or the
> object-special trap.

## Phase-C verdict

- **Library built** (T1–T6, the complete reservoir of constraint-supplying general theorems) and **matcher
  specified** (a runnable 5-step protocol, mechanical except for recognizing a *novel* class).
- **Matcher run over the library × ζ:** every general theorem has a **single named blocker**; no row passes.
- **Blockers cluster to two roots:** **SURF** (R1–R3, the missing arithmetic geometry of $\operatorname{Spec}\mathbb Z$,
  = the same wall, third derivation) and the **object-special trap** (R4, = CAP). No third root.
- **The instrument is complete:** D0 + library + matcher partition all candidates into REJECT / OPEN-on-SURF /
  NEW-THEOREM-REQUIRED. The last bin is empty and is the only place a genuinely new node could live.
- **Honest standing:** this is not progress toward a proof. It is the completed, validated **strategy map** —
  the deliverable the audit identified as the program's real output — now sharp enough to route every future idea
  in one of three directions and to spend only where a new degree of freedom is even logically possible.
