# Phase B — operationalizing I2b, and surviving the circularity attack

**Auditor build · 2026-06-05.** Phase A localized the entire fragility of D0 to one clause, **I2b** ("the
independent input comes with a *decisive theorem* that supplies the constraint"). For a *search* — screening
candidates *before* a proof exists — I2b must be (i) checkable without already having the proof, and (ii)
**non-circular**: it must not secretly equal "proves RH," which would make D0 vacuous. This is the make-or-break
test for the whole instrument. I operationalize I2b, then attack it.

---

## The operational definition

A naïve I2b — *"a theorem exists that pins the constraint"* — is useless for search: it only recognizes finished
proofs. The function-field case shows the right form. There the constraint $|\alpha_i|=\sqrt q$ is **not** a
property one establishes specially for $C\times C$; it is a **corollary of the Hodge index theorem**, a *general*
result holding for **all** algebraic surfaces, proven for reasons internal to algebraic geometry and **independent
of RH**. The structure $C\times C$ merely *lands in the class* where the general theorem already applies.

> **I2b (operational).** The candidate structure $X$ lies in a class $\mathcal C$ carrying a **general theorem
> $T$** — proven independently, for reasons internal to $\mathcal C$, holding for *every* object of $\mathcal C$ —
> such that $T$ *applied to $X$* yields the off-line-zero / eigenvalue constraint as a **corollary**. I2b
> **fails** when the constraint is instead a property *special to $X$* that must be established by hand (that
> special property, for the zeros of $\zeta$, **is** RH).

This is checkable pre-proof: one asks *"is the needed bound a corollary of a general, already-proven theorem about
a class $X$ belongs to — or is it a bespoke fact about $X$ alone?"* — without proving the bound oneself.

## The circularity attack (the decisive test)

**Attack.** *"For function fields, $T$ = Hodge index = a positivity (a signature condition). So I2b just relocates
the wrong-sign capstone CAP into $T$. Every PASS still rests on a positivity; I2b is CAP wearing a category hat,
and for $\zeta$ that positivity is RH. So I2b is circular — it passes only what already proves RH."*

**Response — it is non-circular, but only as a *classifier*, and the honesty is in stating exactly what it does
not do.**
- I2b does **not** escape CAP. $T$ *is* a positivity. What I2b discriminates is **whether that positivity is
  PROVEN GENERALLY** (for the whole class $\mathcal C$, independently — as the Hodge index theorem is, for all
  surfaces) **or is UNPROVEN / object-special** (as Weil positivity is, for $\zeta$).
- That distinction is real and not RH in disguise: *"is the bound a corollary of a general proven theorem?"* is a
  **category-placement** question, decided by exhibiting $\mathcal C$ and $T$ — **not** an inequality one must
  prove about $\zeta$. The function-field history is the proof of non-triviality: **Weil first found the category
  (varieties + cohomology); the inequality then followed from general geometry.** Finding the category and proving
  the inequality by hand are different acts.
- **What I2b therefore *is*:** not an escape from CAP, but a **classifier of CAP** into *CAP-proven-by-general-
  geometry* (function fields — PASS) versus *CAP-object-special* ($\zeta$, Connes, de Branges, Li, … — FAIL/OPEN).
  The instrument survives the circularity attack **at the cost of admitting it does not bypass the wall; it
  locates the precise form a crossing must take.**

## Re-validation: I2b is now three-valued (and that is the point)

A binary pass/fail would mis-handle the live frontier. Operational I2b yields three states, and they match reality:

| State | Meaning | Calibration members |
|---|---|---|
| **RECOGNIZE-PASS** | a *known* general theorem $T$ applies to $X$ for free | **function-field RH** (Hodge index; Stepanov) — and the cross-problem controls (modularity; Heegner/Gross–Zagier) |
| **OPEN** | a class $X$ is being built so a general $T$ *would* apply, but $T$ is **not yet established** for that class | **Connes–Consani** (RR for $\overline{\mathrm{Spec}\,\mathbb Z}$ exists; the arithmetic Hodge index / $H^1$ does **not**); Deninger |
| **REJECT** | no general theorem is in sight; the bound is object-special to $\zeta$ | Weil criterion, Hilbert–Pólya, de Branges, Nyman–Beurling, Li, Montgomery, RMT, mollifiers, dBN, the corpus's own detectors, **HYP** |
| | | |

**Every Phase-A verdict is preserved**, and the one genuinely live program (Connes–Consani) gets its correct
status — **OPEN, not dead** — which a binary filter could not express. This three-valued output is exactly what a
search needs: spend **only** on OPEN candidates; REJECT is the ζ-reformulation graveyard; RECOGNIZE-PASS is rare
and already cashed.

## The sharpened search target (what "find a new node" concretely means)

> **Target.** Exhibit a class $\mathcal C$ and a general, independently-proven theorem $T$ such that **$\zeta$'s
> zeros lie in $\mathcal C$** and $T$ delivers the off-line constraint as a corollary. Success is **category
> placement**, not inequality-proving.

The reservoir of theorems $T$ that have ever delivered such constraints is small and specific — the **Hodge-type
positivity theorems**: the Hodge index theorem (surfaces), the Hodge–Riemann bilinear relations (Kähler / and,
recently, **combinatorial** classes), Lorentzian / completely-log-concave polynomials, the Hodge standard
conjectures. The recent **Adiprasito–Huh–Katz** program proved Hodge–Riemann positivity for **matroids** —
*non-geometric* objects — settling old combinatorial conjectures. That is the precise template: a general
positivity theorem established for a **new** class.

**Honest caveat — and the calibration bites here too.** The obvious attempt to place $\zeta$ in a Hodge–Riemann /
stable-polynomial class **already exists in the corpus as HYP** (Jensen-polynomial hyperbolicity = Lee–Yang /
Lorentzian-type positivity), and **HYP is REJECT**: proving the hyperbolicity *is* RH; no general theorem supplies
it for $\zeta$'s Jensen polynomials. So the reservoir is the right *type*, but every *known* embedding of $\zeta$
into it lands on the object-special instance (= RH), not a corollary. **The open problem is therefore precise:**
not "use Hodge theory" (tried, → HYP → REJECT) but **"find an embedding of $\zeta$'s data into a Hodge-type class
for which the positivity is a corollary of the general theorem rather than the special case."** That embedding is
unknown; whether it exists is the genuine frontier; it is the same gap as Connes–Consani's missing arithmetic
Hodge index, now stated as a category-placement problem with a checkable success criterion.

## Phase-B verdict

- **I2b is operationalized** as a category-placement test (*"corollary of a general independently-proven theorem,
  vs object-special property"*) — checkable before a proof exists.
- **It survives the circularity attack**, but only as a **classifier of CAP**, not an escape: every PASS rests on a
  positivity that is *generally proven* for a class; ζ's required positivity is *object-special* (= RH) under every
  known embedding.
- **D0 is now three-valued** (RECOGNIZE-PASS / OPEN / REJECT) and reproduces all calibration verdicts including the
  correct *OPEN* status of the one live program.
- **The search target is sharp and fundable:** find a class $\mathcal C$ + general theorem $T$ placing ζ's zeros
  where the constraint is a corollary. The only known theorem-reservoir is Hodge-type positivity; the only known
  ζ-embeddings into it are REJECT (HYP = RH); a non-special embedding is the open frontier.
- **Residual honesty.** I2b is now checkable but still requires expert judgment to *recognize* whether a proposed
  $\mathcal C/T$ is "general and independent." Full machine automation (Phase C) needs a library of admissible
  general theorems $T$ and a matcher; that library is finite and writable, but adjudicating a *novel* $\mathcal C$
  remains a research act, not a lookup. **D0 is a validated expert filter with a sharp, non-circular I2b — not yet
  a push-button oracle, and the gap to "push-button" is exactly the gap to recognizing new mathematics.**
