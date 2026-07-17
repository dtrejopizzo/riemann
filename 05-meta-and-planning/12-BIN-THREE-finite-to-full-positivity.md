# Bin three — a genuine attempt at new mathematics, and what the wall said

**Auditor build · 2026-06-05.** Bin three = NEW-THEOREM-REQUIRED: a class $\mathcal C$ with a *new* general
positivity theorem into which ζ's data embeds so the off-line bound is a corollary, bypassing the missing-geometry
root (R1–R3) and the object-special trap (R4). Discipline (the program's ethos): **construct, then destroy in the
same act.** I take the least-explored positivity family for ζ — **total positivity / Pólya frequency functions** —
push it to the wall, and extract the structural theorem the wall forces. No proof of RH is claimed; the deliverable
is a genuinely new *characterization of why bin three is empty* and *the exact shape of its only possible occupant.*

---

## 1. The construction: RH as total positivity of the de Bruijn–Newman kernel

The Jensen/Ξ coefficients are moments of a **positive** kernel: $b(k)=m_{2k}/(2k)!$, $m_{2k}=\int t^{2k}\Phi(t)\,dt$,
with $\Phi(t)>0$ **unconditionally** (classical; $\Phi$ is the dBN kernel, $\Phi=\sum_n(2\pi^2n^4e^{9t/2}-3\pi n^2
e^{5t/2})e^{-\pi n^2e^{2t}}>0$). By **Schoenberg's theorem**, an even kernel $\Phi$ is a **Pólya frequency
function** (the matrix $[\Phi(x_i-x_j)]$ is **totally positive** — *all* minors $\ge0$, all orders) **iff** its
bilateral Laplace transform is $1/E$ with $E$ in the **Laguerre–Pólya class**. Since $\widehat\Phi=\Xi$:

> **(TP-form of RH).** $\mathrm{RH}\iff \Xi\in\mathrm{LP}\iff \Phi$ **is a Pólya frequency function** $\iff$ the
> kernel $[\Phi(x_i-x_j)]$ is **totally positive of every order**.

*(Pólya and Schoenberg are the lineage; the corpus had not recorded ζ in the total-positivity language. This is a
real reformulation — and, by the matcher, it must still be tested for the object-special trap.)*

## 2. The unconditional positivity available — and exactly where it stops

Total positivity is a **hierarchy** $\mathrm{TP}_1\supseteq\mathrm{TP}_2\supseteq\cdots\supseteq\mathrm{TP}_\infty$
($\mathrm{TP}_k$ = all minors up to order $k$ are $\ge0$). For ζ:

| order | meaning | status for ζ |
|---|---|---|
| $\mathrm{TP}_1$ | $\Phi>0$ | **unconditional** (classical) |
| $\mathrm{TP}_2$ | log-concavity / **Turán inequalities** on $b(k)$ | **unconditional** (Csordas–Norfolk–Varga; GORZ) |
| $\mathrm{TP}_k$, fixed $k$ | $k$-th Jensen polynomials hyperbolic | **unconditional for large $n$** (Griffin–Ono–Rolen–Zagier, via Hermite limit) |
| $\mathrm{TP}_\infty$ | full total positivity / $\Xi\in\mathrm{LP}$ | $=$ **RH** |

Every **finite** order is unconditional (or known for large height); the **full** order is RH. The obstruction to
climbing is **uniformity in $n$** (GORZ gives each order eventually; RH needs all orders at all heights). **This is
exactly the cornered target $U$** (uniform gap-universality) reached from a new direction.

## 3. The wall, named precisely: the finite-to-full positivity gap

The TP construction does **not** escape the trap — it reveals its universal form. Run the matcher: is full TP a
*corollary of a general theorem*, or *object-special*? Schoenberg's theorem is general, but it is an
**equivalence** ($\Phi$ PF $\iff$ $\Xi\in$ LP) — it *relabels* RH, it does not *supply* it. Climbing
$\mathrm{TP}_k\to\mathrm{TP}_\infty$ for the specific kernel $\Phi$ is the object-special step (= RH). **REJECT** —
but now with a precise diagnosis that holds across *every* positivity family the program has touched:

> **Structural theorem (finite-to-full gap).** In each positivity family $F$ attached to ζ —
> **intersection/Hodge** (the Weil form / $\lambda_{\min}$), **moment/Hankel** (the $m_{2k}$), **total-positivity/
> Pólya-frequency** ($\Phi$), **combinatorial-Hodge/matroid** (the Jensen polynomials) — there is a hierarchy
> $P_1^F\supseteq\cdots\supseteq P_\infty^F$ such that **every finite level $P_k^F$ is unconditional for ζ**, while
> **$P_\infty^F=\mathrm{RH}$**, and **no general theorem in $F$ bridges $P_k^F\to P_\infty^F$ for the specific
> object** (that bridge is the object-special step = R4). The four families' hierarchies are the *same gap* in four
> languages: Turán $=\mathrm{TP}_2=$ degree-2 Jensen $=$ the leading moment inequality; full LP $=\mathrm{TP}_\infty=$
> all Jensen $=$ the Weil sign.

## 4. The synthesis (the genuinely new content): geometry **finitizes** positivity — CAP and SURF are one

Why does the function-field case **not** have this gap? Because there $P_\infty^F$ is **finite**:
$H^1(C)$ is finite-dimensional ($\dim=2g$), the intersection lattice $\mathrm{NS}(C\times C)$ has finite rank, and
the Hodge index theorem pins **all** $2g$ eigenvalues **at once** — "full" positivity **is** a finite positivity,
so a general theorem reaches it. For ζ the analogous data is **infinite-dimensional** (infinitely many zeros; an
infinite moment sequence), so "full" is a genuine limit no finite-order theorem attains.

> **The unification.** The object-special trap **R4** (finite-to-full gap, = CAP) and the missing geometry
> **R1–R3** (= SURF) are **one phenomenon**: *the geometry's job is to **finitize** the positivity.* A
> finite-dimensional cohomology converts "full positivity" into "finite positivity," which a general theorem
> (Hodge index) then supplies for free. **CAP is the infinite-order positivity; SURF is the finitizing device that
> would make it finite-order; they are the two faces of the single missing ingredient: a finite-dimensional model
> of ζ's positivity.**

This is the precise shape of **bin three's only possible occupant**: not "a new positivity inequality" and not "a
new statistic," but **a finitization** — a construction rendering ζ's full positivity equivalent to a
finite-dimensional one (a finite intersection lattice / finite cohomology / a finite totally-positive matrix whose
total positivity is itself a corollary). The function-field curve is such a finitization; for $\operatorname{Spec}
\mathbb Z$ none is known, and that — not any single inequality — is the missing mathematics.

## 5. Adversarial audit of the synthesis (destroy it)

- **"Is it circular (just RH restated)?"** No. It is a statement about the *structure of the difficulty* — that
  four positivity hierarchies share a finite-to-full gap and that finite-dimensionality of the model collapses it.
  It is **checkable and false-if-wrong**: a counterexample would be a positivity family for ζ whose finite levels
  are unconditional **and** whose full level is a corollary of a finite-order general theorem — i.e., a bin-three
  occupant. None exists; the claim is that the four known families all exhibit the gap, which the table verifies.
- **"Is the TP-form new?"** The Pólya–Schoenberg link of LP to total positivity is classical; *applying it as the
  matcher's test for ζ and extracting the finite-to-full synthesis* is the new step. Honest precedent flagged.
- **"Does it help prove RH?"** **No** — and it must not be sold as such. It sharpens *what to build* (a
  finitization) and *why every reformulation fails* (it stays at finite order or relabels the infinite one).
- **"Could the finitization be non-geometric?"** Unknown — and this is exactly bin three's open question, now
  posed sharply: *is there any finite-dimensional model (geometric or not) of ζ's full positivity?* The synthesis
  does not close this; it states it precisely.

## Verdict

- **Bin three was attacked with a genuine new construction** (RH as total positivity of $\Phi$, via Schoenberg) —
  not a reformulation pulled from bibliography, built from the positive dBN kernel directly.
- **It collapsed**, but the collapse produced **new structure**: the **finite-to-full positivity gap**, identical
  across the four positivity families, and the **synthesis that geometry = finitization**, unifying CAP and SURF as
  the two faces of one missing object — *a finite-dimensional model of ζ's positivity.*
- **Bin three remains empty**, but its only possible occupant is now characterized with precision it never had: not
  a new inequality, but a **finitization of ζ's full positivity**. Whether one exists — geometric (the
  $\operatorname{Spec}\mathbb Z$ surface) or otherwise — is the single open question the entire strategy map now
  points to.
- **No RH proof is claimed.** This is new mathematics in the honest sense the program demands: a sharper true
  statement about the wall, falsifiable, and pointing at exactly one thing to build.
