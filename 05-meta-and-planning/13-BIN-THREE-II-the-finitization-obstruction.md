# Bin three, second attempt: what a finitization *is*, and the obstruction to it

**Auditor build · 2026-06-05.** Bin three's only possible occupant was characterized as a **finitization** of ζ's
full positivity. The honest next move is the fork: **construct** such a finitization, or **prove an obstruction**
to it. I make the finitization concept exact (it is a *Frobenius periodicity*), then find the obstruction — which
is conditional (it rests on the Linear Independence conjecture) but sharp, and it explains, structurally, why the
one live program is hard. No RH proof; a sharper true statement about the wall.

---

## 1. What "finitization" concretely is: a Frobenius periodicity

The function-field case shows the exact form. For $C/\mathbb F_q$, $Z(C,T)=\frac{\prod_{i=1}^{2g}(1-\alpha_iT)}
{(1-T)(1-qT)}$, and in $s$ (via $T=q^{-s}$) the zeros sit at
$$
s=\tfrac12+i\frac{\theta_i+2\pi k}{\log q},\qquad i=1,\dots,2g,\ k\in\mathbb Z,\quad \alpha_i=\sqrt q\,e^{i\theta_i}.
$$
**There are infinitely many zeros, but only $2g$ modulo the period $2\pi/\log q$.** RH is the **finite** condition
"the $2g$ arguments $\theta_i$ are real," delivered for free by the Hodge index theorem on the *finite-rank*
lattice $\mathrm{NS}(C\times C)$.

> **Finitization $=$ a periodicity.** The Frobenius gives a period $2\pi/\log q$ that folds infinitely many zeros
> into $2g$ orbits. *This* is what makes ζ's "infinite-order positivity" a finite one. Bin three's occupant, made
> concrete: **a Frobenius-like periodicity for $\operatorname{Spec}\mathbb Z$** that folds the zeros of $\zeta_
> {\mathbb Q}$ into finitely many per period.

## 2. The obstruction (conditional on the Linear Independence conjecture)

The zeros of $\zeta_{\mathbb Q}$ have **no such period**, and there is a believed reason:

- **Linear Independence (LI) conjecture.** The positive ordinates $\{\gamma_n\}$ are **linearly independent over
  $\mathbb Q$.** (Strongly supported: simplicity of zeros, GUE spacing, no observed resonances.)
- A periodicity that folds $\{\gamma_n\}$ into finitely many orbits modulo some period $\tau$ would force
  $\mathbb Q$-linear **relations** among the $\gamma_n$ (each orbit: $\gamma=\gamma_{i}+k\tau$). **LI forbids
  exactly this.**

> **Obstruction.** Under LI, $\{\gamma_n\}$ admits **no** Frobenius-type periodicity — hence **no finite-dimensional
> algebraic model** (a finite-rank cohomology with the zeros as Frobenius arguments). The function-field
> finitization **cannot transfer** to $\operatorname{Spec}\mathbb Z$: the very independence the zeros are believed
> to possess is the negation of the structure a finitization needs.

This is not an artifact — it is the $\mathbb F_1$ difficulty in exact form:

## 3. Why the live program ($\mathbb F_1$ / Connes–Consani) is structurally hard: the period diverges

The $\mathbb F_1$ idea is to make sense of "$q=1$." But the finitizing structure is the **period**
$2\pi/\log q$, and
$$
q\to1^+\ \Longrightarrow\ \frac{2\pi}{\log q}\to\infty.
$$
**The fundamental domain that holds finitely many zeros becomes infinite exactly in the $\mathbb F_1$ limit.** The
$2g$ folded zeros spread out and fill the line; the finite structure **dissolves precisely where it is needed.**
So the Connes–Consani program is not stalled by a missing lemma but by a **degeneration**: the device that
finitizes ($q>1$ periodicity) is singular at $q=1$. Building $\overline{\operatorname{Spec}\mathbb Z}$ is the
attempt to extract a *finite residue* from this divergence — and that is exactly where it is stuck (the $H^1$/
arithmetic Hodge index, the "$2g$" of $\operatorname{Spec}\mathbb Z$, has no finite home as the period blows up).

## 4. The fork, stated honestly

Under LI, the search splits with no middle:

- **(A) LI is true** ⟹ no Frobenius periodicity ⟹ **no finite-dimensional model** ⟹ bin three is **empty for all
  finitizations of algebraic/geometric type**. RH, if provable, needs a genuinely **infinite-dimensional** general
  positivity theorem — none exists; constructing one is new analysis, *not* a finitization, and the discriminator
  classifies every known infinite-dimensional positivity as object-special (CAP). **The program's pessimism is
  then structurally justified, conditionally on LI.**
- **(B) LI is false** (some $\mathbb Q$-relations among the $\gamma_n$) ⟹ a hidden periodicity *might* exist ⟹ bin
  three *could* be non-empty. But LI-falsity is **strongly disbelieved** and would itself be a sensational result.

> **The new statement.** The geometric/finitization route to RH (the function-field template) is in **tension with
> the Linear Independence of the zeros.** The transfer ζ-function-field $\to\zeta_{\mathbb Q}$ is obstructed not by
> missing ingenuity but by a **dimensional/independence barrier**: finite models need periodicity; LI forbids it;
> the $\mathbb F_1$ limit makes the period diverge. *This is the deepest conditional reason the program has found
> for why RH resists the one method that ever proved an RH.*

## 5. Adversarial audit

- **"LI is only a conjecture — so this proves nothing."** Correct, and stated as such. The contribution is a
  **conditional structural obstruction**, not a theorem: *if* the believed independence holds, the believed-natural
  route (finitization) is blocked. Two strongly-held beliefs (LI; "RH should have a geometric proof") are shown to
  be **in tension** — itself informative.
- **"Connes–Consani know $\mathbb F_1$ is a degeneration."** Yes; the new content is naming the degenerating
  object precisely (*the period $2\pi/\log q\to\infty$*) and tying the stall to it, and connecting it to LI.
- **"Could an infinite-dimensional finitization exist (a 'tame' infinite model)?"** Possibly — Connes' spectral
  realization *is* infinite-dimensional. But then the positivity is infinite-order = CAP = object-special; no
  general finite theorem applies. So "tame infinite model" does **not** escape — it re-enters CAP. The audit holds.
- **"Is the periodicity = finitization claim itself solid?"** Yes — it is exactly the rational-function structure
  of $Z(C,T)$ in $q^{-s}$; verifiable, not heuristic.

## Verdict

- **Bin three, attacked a second way** (construct-or-obstruct the finitization): the finitization is concretely a
  **Frobenius periodicity**, and under the **Linear Independence conjecture** it is **obstructed** — no periodicity
  can fold $\mathbb Q$-independent zeros.
- **The $\mathbb F_1$/Connes–Consani stall is explained structurally:** the finitizing period $2\pi/\log q$
  **diverges** at $q=1$; the live program is fighting a degeneration, not a missing lemma.
- **The fork:** under LI (believed), bin three is empty for geometric finitizations and RH needs new
  infinite-dimensional analysis (which the discriminator already classifies as object-special / CAP). Bin three is
  non-empty only if LI fails — strongly disbelieved.
- **No proof; a sharper conditional truth.** The geometric route to RH is in tension with the independence of the
  zeros — the most precise structural reason the search has produced for why the wall is where it is, and a clean,
  falsifiable statement (it is refuted the day someone exhibits a periodicity, i.e., disproves LI).
