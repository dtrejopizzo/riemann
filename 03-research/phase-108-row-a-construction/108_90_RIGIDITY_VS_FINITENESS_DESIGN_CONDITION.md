# 108.90 — The rigidity-versus-finiteness design condition, and the pre-test for Stages 3–7

## 0. Status of this note

This is a **synthesis with retrodictive support**, not a theorem.  It extracts
the shared logical form of the eight recorded obstructions of the program,
states it as a design condition, and applies it as a cheap pre-test to the
remaining stages of row (a).

The individual obstructions it abstracts are proved elsewhere and are not
re-proved here.  Nothing in this note uses a zero of $\xi$.

## 1. The earlier framing was wrong

The obstructions were previously described as "continuum source versus
discrete target".  That description **fails**: in the Cartwright case the
polarity is reversed — the source is the continuous angular density of the DC
object (107_237 Thm 2.1) and the target is the finite $\Delta$-complex —
whereas in 106.185 the source is atomic and the target is forced continuous.
A single "continuum vs discrete" axis cannot contain both.

## 2. The actual shared form

> ### The pattern
> Every recorded obstruction has this shape.
>
> * A group $\Gamma$ acts, and $\Gamma$ is **dense** in a larger group $G$
>   (or divisible, or pro-finite with a continuum completion).
> * The construction demands an object that is **simultaneously**
>   * **(a)** equivariant/invariant under $\Gamma$, and
>   * **(b)** a member of a class $\mathcal C$ defined by a **finiteness**
>     condition.
> * $\Gamma$-equivariance propagates to $\bar\Gamma=G$ by continuity, and the
>   $G$-equivariant objects are never in $\mathcal C$ except $0$.

The finiteness condition changes name in each instance; the form does not.

| # | ref | $\Gamma$ dense/divisible in $G$ | finiteness class $\mathcal C$ |
|---|---|---|---|
| 1 | 106.185 | $\log\mathbb Q^+\subset\mathbb R$ | atomic support |
| 2 | 106.205 | scaling | point spectrum |
| 3 | 107_224 | $(\mathbb R,+)$ divisible | finitely generated $NS$ |
| 4 | 107_161 | cross-prime charts | finite restriction data |
| 5 | 107_242 | $\mathbb Q_p$ pro-$p$ | $\mu_{(p)}$, prime to $p$ |
| 6 | Cartwright vs 107_237 | continuous angular density | finite $\Delta$-complex |
| 7 | 108.01 | dilations by $\mathbb N^\times$ | compact support |
| 8 | 108.04/05/10 | descent needs non-compact | pairing needs compact |

So the clash is **rigidity against finiteness**, not continuum against
discrete.

## 3. Instance 8 is the exception, and it shows the escape

In case 8 the resolution (108_05) was **neither** to weaken equivariance
**nor** to enlarge the finiteness class.  It was to observe that the two
objects sit on **opposite sides of a Mellin duality**, and that what gets
regularized is the **pairing** — Burnol's cutoff $[\frac1T,T]$ — rather than
either object.  The graded family is not in the test class; it is in the dual,
and the cutoff is the map between the sides.

> ### Design condition
> **Never require one object to be both $\Gamma$-equivariant and finitely
> supported.  Put the equivariance on one side of a duality, the finiteness
> on the other, and regularize the pairing.**

## 4. Retrodictions

The condition was extracted from instances 1, 6, 7, 8.  It correctly
retrodicts three cases that were not used to build it.

**107_224.**  The demand was an *additive* $c_1:\mathbb R\{\infty\}\to NS$,
i.e. a morphism from a divisible group to a discrete one.  Under the
condition: ask instead for a **pairing**.  This is exactly what Arakelov
theory does — the archimedean place enters through Green's functions, a
pairing, never through a $c_1$ into $NS$.  **The theory that works already
obeys the condition.**

**106.185.**  The demand was a majorant that is invariant *and* atomic: one
object, both properties.  Under the condition: an invariant **pairing**
between an atomic space and its dual — which is a Gelfand triple.

**Cartwright vs 107_237.**  The demand was that the DC object *be* a finite
tropical complex.  Under the condition: pair it against finite-PL objects
rather than convert it into one.

## 5. The pre-test, applied to Stages 3–7

For each remaining stage of row (a), ask: does the stage as posed demand a
single object with both properties?

| stage | $\Gamma$-equivariance demanded | finiteness class demanded | verdict |
|---|---|---|---|
| **3** — correspondences $\Gamma_{p^k}$ | yes (scaling) | **yes** (supported at finitely many places) | **FLAGGED** |
| 4 — archimedean fibre | yes | no | clear |
| 5 — Lefschetz identification | yes | no | clear |
| 6 — primitive inequality | yes | no | clear |
| 7 — scaling compatibility | yes | no | clear |

> ### Prediction for Stage 3
> Paper 40 §10.9.1 item 1 asks for classes $\Gamma_{p^k}$ that are
> scaling-equivariant **and** carry local torsion/incidence at finitely many
> places.  That is precisely the forbidden combination, so the condition
> predicts Stage 3 **fails as posed**.
>
> The prescribed repair: $\Gamma_{p^k}$ should not be a finitely supported
> equivariant divisor, but a **functional on graded sections**, with the
> finiteness residing in the object it is paired against.

This is falsifiable and costs nothing to apply before Stage 3 is attempted.

## 6. Scope

Not proved here:

* the design condition itself — it is an empirical regularity over eight
  instances plus three retrodictions, not a theorem;
* that the Stage-3 prediction is correct;
* that the prescribed repair for Stage 3 is available.

Proved elsewhere and only cited: each of the eight instances.

No status is promoted.  `ROW_A_STATUS` remains `partial`.

## 7. Verifier

`108_90_rigidity_vs_finiteness_design_condition.py`.

**Checks carrying computational content:** density of $\log\mathbb Q^+$ in
$\mathbb R$ by a gap test, and that a single $\log p$ already suffices;
$\mathrm{Hom}((\mathbb R,+),\text{f.g. abelian})=0$ via divisibility;
$\overline{\mathbb F}_p^\times=\mu_{(p)}$ has order prime to $p$; that no
nonzero compactly supported continuous $f$ is even *approximately* invariant
under translation by $\log n$ (minimum relative defect $>0.69$ over three
profiles and $38$ values of $n$); and the duality escape of 108_05, weak
convergence $\langle k_T,\varphi\rangle\to2\pi\varphi(0)$.

**Checks that are structural encodings, not proofs:** the tabulation of the
eight instances (§2), the finite-PL/DC contrast, and the Stage 3–7 pre-test
(§5).  These verify that the recorded data has the stated shape; they do not
establish the underlying mathematics, which is proved in the cited documents.
