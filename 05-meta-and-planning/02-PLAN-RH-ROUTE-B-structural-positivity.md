# PLAN — RH Route B: Structural Positivity (is the Weil operator a square?)

**Author:** David Alejandro Trejo Pizzo · **Opened:** 2026-06-03 · **Status:** the only open route to RH
after P8.

This is the companion plan to **P8** (`06-papers/P8-weil-krein-realization/`). P8 closed the
explicit-formula / **zero-side** line: it built a faithful semibounded realization $\mathcal T$ of the Weil
form with $\mathrm{RH}\iff\inf\operatorname{spec}(\mathcal T)\ge0\iff\|K\|\le1$, **and proved a no-go**
(P8 Thm C) — the zero side cannot decide the sign, because the off-line depths enter only through
$\mathfrak t$ itself. **Route B is what remains: produce the sign from an *independently-given* positive
structure.**

---

## 0. The premise, and what P8 Theorem C forces on us

RH $\iff$ $\mathcal T\succeq0$ (the sign). The only known way to force the sign of a self-adjoint operator
is **manifest positivity**:
$$
\boxed{\ \mathcal T = A^*A\quad(\text{a square})\ \Longrightarrow\ \mathcal T\succeq0\ \Longrightarrow\ \mathrm{RH}.\ }
$$
or an equivalent structural certificate (a positive trace, a de Branges ordering, a Hilbert–Pólya
self-adjointness).

**The hard constraint from P8 Thm C (read this before doing anything).** The square $A$ — or whatever
positive structure we exhibit — **must be built from data independent of the off-line zeros.** Any $A$
assembled from the zero-evaluations $E$ is circular (P8 Cor. C′): it presupposes the answer. Concretely:

> **Guardrail B0 (the lesson of the whole program).** A candidate structure is *admissible* only if it can
> be written down **without knowing whether RH is true** — i.e. from the archimedean/adelic local data, the
> prime data, or an abstract space — and its positivity is then *manifest by construction*, not *checked
> against the zeros*. If a step needs the zeros to be on the line, it is the optimistic-pillar trap again.

This single constraint is why route B is hard and why the field is stuck here: it is exactly the
Connes–Consani / Hilbert–Pólya problem. We enter with **eyes open: prior of success very low.** The value
of the plan is to (a) attack the *one* well-posed question, (b) fail *informatively* (more no-go theorems
of the P8-Thm-C type are themselves the durable output), and (c) not waste a month on circular routes.

---

## 1. The single question

$$
\boxed{\ \textbf{Is the Weil/Connes operator } \mathcal T \textbf{ a square } A^*A \textbf{ — manifestly positive — for a }A\textbf{ built independently of the zeros?}\ }
$$

Everything below is a way of attacking this, or of proving it cannot be done (a no-go), which is equally
publishable.

---

## 2. Three fronts (run in the stated order — "define before factoring")

The order matters and is itself a lesson from P8: you cannot search for $\mathcal T=A^*A$ until you know
*which* $\mathcal T$ (which self-adjoint realization, which domain). Different self-adjoint extensions
(Friedrichs vs Krein) can have different bottom signs; choosing the wrong one fabricates or destroys
positivity. So **B3 (identify the object) precedes B1 (factor it).**

### Front B3 — Identify $\mathcal T$ against the archimedean/de Branges objects (do this FIRST)
**Goal:** decide whether $\mathcal T$ (or its *useful*, zero-independent cousin) is already a known object
whose positivity structure is studied.
- **B3.1 — Connes–Consani comparison.** Their positive object is the compression of the scaling action
  $\vartheta$ onto **Sonin's space** $\mathbf S$ (zero-independent!): $\mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$.
  Question: is $\mathcal T_{\text{archimedean}}$ (the realization built from $\mathfrak a$, not from $E$) a
  compression of a *positive* operator? Is $\mathbf S\,\vartheta(g)$ the square root $A$? Read
  `papers-referencia/2006.13771v1.pdf` §§4–6 and Thm 6.11 carefully; locate the exact operator whose
  eigenvalues-below-1 give positivity. **Deliverable:** a precise statement of what is positive
  *by construction* there, and whether our $\mathfrak t$ inherits it.
- **B3.2 — de Branges chain.** Under RH the completion is $\mathcal H(E_\xi)$, $E_\xi=\xi(\tfrac12-iz)+\xi'(\tfrac12-iz)$
  (Suzuki/Lagarias). De Branges' approach forces positivity via an **ordering** of subspaces (a chain). The
  zero-independent content is the *structure functions* $A,B$ with $E=A-iB$. Question: does the chain
  condition (the de Branges inequality $|E(z)|>|E(\bar z)|$ on the upper half-plane, the Hermite–Biehler
  property) admit an *unconditional* substitute that would give a square? **Deliverable:** state the exact
  de Branges positivity certificate and whether it can be checked without RH. (Known to be very hard — de
  Branges' own attempts. Time-box, but the structure functions are the right zero-independent handle.)
- **B3.3 — Hilbert–Pólya / self-adjoint model.** Suzuki notes $\mathcal H_W$ realizes the zeros as
  eigenvalues of the multiplication operator's self-adjoint extensions. Question: is there a *natural*
  self-adjoint operator (a Hamiltonian) whose spectrum is $\{t_\rho\}$ and whose self-adjointness is
  manifest (hence real spectrum = RH)? This is the classical Hilbert–Pólya dream; admissible only if the
  Hamiltonian is given independently of the zeros. **Deliverable:** map our $\mathcal T$ to/against the
  Berry–Keating / Connes Hamiltonian; identify the obstruction (the cutoff / Sonin "quantum cell").

### Front B2 — The Connes route as the concrete square (the most promising sub-front)
**Goal:** turn the Connes–Consani lower bound into an actual factorization.
- **B2.1.** Their inequality $W_\infty(g*g^*)\ge\mathrm{Tr}(\vartheta(g)\mathbf S\vartheta(g)^*)$ already
  exhibits a **positive** right-hand side ($\mathbf S\ge0$ is a projection, so the trace is
  $\|\mathbf S\vartheta(g)^*\|_{HS}^2\ge0$ — a manifest square!). The gap to RH is the **residual**
  $W_\infty(g*g^*)-\mathrm{Tr}(\cdots)$, which they control up to $-c|\hat g(0)|^2$ (Thm 6.11). Question:
  is the residual itself a square (or non-negative) on the relevant test space, after the archimedean +
  finite-prime places are all included (the semi-local case)? **This is the actual frontier of RH and is
  exactly where Connes–Consani stop.** Our contribution can only be at the margins; identify if the
  band-limited $PW_d$ structure (our P8 setting) sharpens the prolate/Toeplitz control of the residual.
- **B2.2.** The Toeplitz / prolate-spheroidal "eigenvalue below 1" device: is there a $PW_d$-native version
  (Slepian functions are exactly the prolate eigenfunctions of the band-limiting operator) that makes the
  residual estimate cleaner? **Deliverable:** either a sharper residual bound, or a no-go explaining why the
  band-limited structure does not help (another P8-Thm-C-style result).

### Front B1 — Direct factorization $\mathcal T=A^*A$ (LAST — only after B3 fixes the object)
**Goal:** given the correctly identified, zero-independent realization, look for an explicit square.
- **B1.1.** Write $\mathcal T = \mathcal T_{\rm arch} + \mathcal T_{\rm pole} - \mathcal T_{\rm prime}$. The
  archimedean part $\mathcal T_{\rm arch}$ (from $\mathfrak a$, $\re\psi(\tfrac14+\tfrac{ir}2)-\log\pi$) is
  **explicit and zero-independent**; is it $\ge0$ / a square on $PW_d$? The prime part is the obstruction.
- **B1.2.** Is there a "creation/annihilation" factorization (a Bost–Connes-type $C^*$-algebra, a Fock
  structure) in which $\mathcal T=A^*A$ with $A$ the annihilation-like operator? *(Note: the program's
  Day-4 Fock pivot was retracted as a truncation artifact — re-enter only with the zero-independence
  guardrail B0.)*
- **B1.3.** Refutation track: prove $\mathcal T$ is **not** a square in any admissible way (a structural
  no-go), e.g. by exhibiting an essential negative-type obstruction in the prime part. A clean no-go here
  would be a strong result and would *close route B* honestly.

---

## 3. What success / partial success / failure looks like (tiered, honest)

| Outcome | Probability (honest) | Value |
|---|---|---|
| Full square $\mathcal T=A^*A$, admissible ⟹ **RH** | $<1\%$ | the theorem |
| Sharper residual control (Connes route) on $PW_d$ | $\sim10\%$ | real contribution, not RH |
| Clean **no-go** (structural obstruction to the square) | $\sim25\%$ | durable; closes route B honestly |
| Precise identification $\mathcal T \leftrightarrow$ Connes/de Branges object | $\sim40\%$ | expository/structural, publishable |
| Nothing new beyond P8 | remainder | time-boxed, cut losses |

**The realistic target is a no-go or an identification, not RH.** That is not defeatism — it is the same
honesty that made P8's Theorem C the most valuable output of the zero-side line.

---

## 4. Guardrails (learned the hard way)

- **B0 (zero-independence):** every admissible structure must be writable without assuming RH. Re-check
  every candidate $A$ against this. *(This is the formalized lesson of P8 Thm C.)*
- **Audit before pillarizing:** no step becomes a foundation until hostile-audited. The optimistic pillar
  is where the crack hides.
- **$O$ vs $o$, magnitude vs sign:** keep the P8 distinction front of mind — bounds give magnitude (B-2),
  the sign needs structure. Do not re-derive magnitude bounds and mistake them for progress.
- **Define before factoring:** B3 before B1. Do not search for a square of an unidentified operator.
- **Retraction is cheap, false victory is expensive.** Convert relative dates; log every dead end.

---

## 5. Milestones / deliverables (each → proof log + map)

1. **M1 (B3.1):** precise reading of Connes–Consani's positive object (Sonin compression) and a written
   statement of whether $\mathfrak t$ inherits it. → new file `phase-5-structural/B3.1-connes-comparison.md`.
2. **M2 (B3.2/B3.3):** the de Branges structure-function / Hilbert–Pólya identification or obstruction.
3. **M3 (B2.1):** the residual-positivity question stated exactly; the $PW_d$/Slepian angle assessed.
4. **M4 (B1.3):** attempt a structural no-go for the admissible square; if it lands, **route B closes**.
5. **Each milestone** updates `00-MAP.md` (route-B branch) and `phase-4-handoff/proofs/00-PROOF-LOG.md`
   (or a new `phase-5-structural/` log), and the project memory.

---

## 6. Where this lives (for the map and log)

- **Plan:** this file, `riemann-program/PLAN-RH-ROUTE-B-structural-positivity.md`.
- **Work folder (to create at M1):** `riemann-program/phase-5-structural/`.
- **Map:** add a "ROUTE B — structural positivity" branch under the RH end-game node in `00-MAP.md`
  (pointing here), parallel to the now-closed zero-side line (P8).
- **Log:** route-B entries continue the chronology; the first entry records the opening of this plan and the
  P8 no-go as the reason the zero side is closed.

**One-line framing for the team.** *P8 proved the zero side cannot reach the sign; route B asks the only
remaining question — does $\mathcal T$ carry an independently-given positive structure (a square)? — with
the honest expectation that the deliverable is most likely another no-go or a clean identification with
Connes/de Branges, not RH itself.*
