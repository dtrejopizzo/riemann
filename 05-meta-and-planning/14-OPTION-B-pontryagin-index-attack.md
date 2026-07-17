# Option (b), attacked: the infinite-dimensional route via the Pontryagin index — pushed to its quantitative core

**Auditor build · 2026-06-05.** Option (b): an *infinite-dimensional* general positivity that supplies $\zeta$'s
constraint without being object-special. The classifier predicts re-entry into CAP. Instead of accepting that, I
push the most aggressive concrete realization — the **Pontryagin negative-index** $\kappa$ — until it gives a
*new intermediate target* and a *single explicit inequality* whose crossing is the whole game. The wall is not a
stopping point; it is reduced to one functional-analytic statement, and the precise reason it is hard ($\sqrt N$
vs $\log N$) is exposed and connected across the program.

---

## 1. The right infinite-dimensional invariant: the negative index $\kappa$, not the sign

P8 realized the Weil functional as a quadratic form $\mathfrak t$ on a Kre\u\i n space. Sharpen the binary sign
(RH $\iff \mathfrak t\succeq0$) to an **integer**:
$$
\kappa \;=\; \#\{\text{negative squares of }\mathfrak t\}\;=\;\#\{\text{off-line zeros, with multiplicity}\}.
$$
The hierarchy is $\kappa=0\ (\RH)\ \subset\ \kappa<\infty\ \subset\ \kappa=\infty$. In infinite dimensions the
analogue of "finite-dimensional model" (P15 §4) is **finite negative index**: a space with $\kappa<\infty$ is a
**Pontryagin space** $\Pi_\kappa$, and there is a genuine *general* theory (Kre\u\i n--Langer,
Iohvidov--Kre\u\i n--Langer) of self-adjoint operators on $\Pi_\kappa$.

> **The new intermediate target.** Not RH directly, but: **is $\mathfrak t$ a Pontryagin form, $\kappa<\infty$?**
> ($\kappa<\infty \iff$ finitely many off-line zeros.) This is strictly weaker than RH, strictly stronger than
> every zero-density estimate, and is the infinite-dimensional substitute for finitization: *finite defect* in
> place of *finite dimension*.

**Why this is a real lever (Kre\u\i n--Langer).** A self-adjoint operator on $\Pi_\kappa$ has **at most $\kappa$**
non-real eigenvalues (in conjugate pairs), and if it is *definitizable* its real spectrum is governed by a scalar
*definitizing polynomial*. So $\kappa<\infty$ would (i) bound the off-line zeros by $\kappa$ and (ii) bring the
general Pontryagin structure theory to bear on forcing $\kappa\to0$. This is a general theorem (the Kre\u\i n--Langer
bound), so the route passes $I_{2b}$ **provided** $\kappa<\infty$ is itself secured by something not object-special.
That proviso is the whole question; we now reduce it.

## 2. Reduction of $\kappa<\infty$ to a relative form bound on the prime tail

Write the localized Weil form on band-limited test functions as
$$
\mathfrak t[g]\;=\;\underbrace{\mathfrak a[g]}_{\text{archimedean}\succeq0}\;-\;\underbrace{\mathfrak p[g]}_{\text{prime form}},
\qquad
\mathfrak p[g]=2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,\mathrm{Re}\,(g\star\tilde g)(\log n).
$$
Split the prime form at a cutoff $X$: $\mathfrak p=\mathfrak p_{\le X}+\mathfrak p_{>X}$. The piece
$\mathfrak p_{\le X}$ is a **finite-rank** form (finitely many primes), so it contributes at most a finite number
of negative squares. Therefore:

> **Reduction.** If for some $X$ the tail is **relatively form-bounded by the archimedean form with bound $<1$**,
> $$
> \bigl|\mathfrak p_{>X}[g]\bigr|\ \le\ a\,\mathfrak a[g]+C\|g\|^2,\qquad a<1,\tag{RFB$_X$}
> $$
> then $\mathfrak t=\mathfrak a-\mathfrak p_{\le X}-\mathfrak p_{>X}\succeq(1-a)\mathfrak a-\mathfrak p_{\le X}-C$,
> a finite-rank perturbation of a semibounded form $\Rightarrow$ $\kappa<\infty$. Hence **(RFB$_X$) for some $X$
> $\Rightarrow$ finitely many off-line zeros**, and the Kre\u\i n--Langer machinery then targets $\kappa=0$.

So the infinite-dimensional route does **not** dead-end at "object-special": it converts to a concrete, classical
inequality (RFB$_X$) on the prime tail. This is the crossing point.

## 3. The quantitative core: why (RFB$_X$) is hard --- $\sqrt N$ versus $\log N$

(RFB$_X$) is exactly the relative-boundedness question the corpus met at the very start (proof log Day 0, B2.3),
now correctly framed at the level of negative index. Its difficulty is explicit. The archimedean form has energy
$\mathfrak a\sim\log|r|$ (the gamma-factor multiplier $\Omega(r)=\mathrm{Re}\,\psi(\tfrac14+\tfrac{ir}2)-\log\pi$).
The prime tail's energy, for a test function probing primes up to $N=e^{1/\varepsilon}$, is governed by
$$
\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}\ \sim\ 2\sqrt N \qquad(\text{Chebyshev/PNT}),
$$
which **dominates** $\log$ by a power. So the *unsigned* tail is not subordinate: $a<1$ **fails** if the prime
contributions add coherently. (RFB$_X$) can hold only through **cancellation**: the oscillatory factors
$(g\star\tilde g)(\log n)$ must beat the $\sqrt N$ amplitude down to $\le a\cdot\log$.

> **Crossing condition (sharp).** (RFB$_X$), hence $\kappa<\infty$, hence the Pontryagin route, holds **iff** the
> prime tail exhibits **square-root cancellation in the relative-form-bound sense** --- the $\sqrt N$ amplitude of
> $\sum_{n\le N}\Lambda(n)n^{-1/2}(g\star\tilde g)(\log n)$ is reduced, uniformly over admissible $g$, to size
> $a\,\mathfrak a[g]+O(\|g\|^2)$ with $a<1$.

This unifies, as one quantitative statement, four things the program had kept separate: the Day-0 KLMN failure
($\mathfrak p$ form-larger than $\mathfrak a$), the band-limited saturation **N3** ($C\equiv1$: primes align just
to the boundary, $a=1$ marginal), the **finite-to-full gap** (P15: $\sqrt N\to\log N$ is the finite-to-full step),
and the **square-root barrier**. They are the single inequality (RFB$_X$).

## 4. Aggressive analysis: can (RFB$_X$) be forced, even partially?

Three angles, each pushed:

1. **Coherence budget (N3 says $a=1$, not $a>1$).** N3 established that for the *full* band-limited form the
   Carleson constant is **exactly** $1$ --- the primes saturate the archimedean form but do **not** overshoot.
   Translated: the marginal bound $a=1$ is *attained*, not exceeded. (RFB$_X$) needs $a<1$ on the **tail**. Since
   the finite head $\mathfrak p_{\le X}$ carries the dominant coherent mass (small primes, largest
   $\Lambda(n)/\sqrt n$), the tail's coherence is *weaker*, and $a_{\text{tail}}(X)\to$ a limit $\le1$ as
   $X\to\infty$. **The open quantitative question: is $a_{\text{tail}}(X)<1$ for some finite $X$, or exactly $1$
   in the limit?** If the former, $\kappa<\infty$ unconditionally. If $a_{\text{tail}}\equiv1$, the route is
   marginal --- the *same* knife-edge as N3, now isolated to the tail.

2. **Sign-definiteness of the tail (a softer target).** (RFB$_X$) with $a<1$ is stronger than needed:
   $\kappa<\infty$ follows already if $\mathfrak p_{>X}$ is **bounded above** on the unit ball of the archimedean
   norm by *any* finite constant on a co-finite-rank subspace. This is a **one-sided** (upper) tail bound, the
   exact mismatch the wrong-sign capstone names --- but here it is demanded only of the *tail*, where the
   archimedean $\log$ grows and the primes thin. **New sub-question: does the archimedean $\log|r|$ growth
   eventually dominate the tail prime form on a co-finite-rank subspace?** This is a cleaner inequality than full
   RH and is not obviously object-special: it is a competition between two explicit kernels.

3. **Kre\u\i n--Langer descent (if $\kappa<\infty$ were granted).** Given $\kappa<\infty$, $\mathfrak t$ is a
   $\Pi_\kappa$ self-adjoint form; the off-line zeros are its $\le\kappa$ non-real eigenvalue pairs. The
   **definitizing-polynomial** structure plus the **functional equation** symmetry (zeros symmetric about
   $\tfrac12$) would constrain these pairs; whether the symmetry forces $\kappa=0$ is a finite, concrete
   eigenvalue problem --- the first point in the program where RH becomes a *finite* statement (matching P15's
   finitization, now as finite defect rather than finite dimension).

## 5. Status and the single open inequality

- The infinite-dimensional route does **not** collapse to "object-special'' on contact: it converts to the
  explicit, classical inequality **(RFB$_X$)** on the prime tail, whose truth gives $\kappa<\infty$ (finitely many
  off-line zeros) and unlocks Pontryagin descent toward $\kappa=0$.
- (RFB$_X$) is hard for one exposed reason: the prime tail's amplitude is $\sqrt N$, the archimedean form's is
  $\log N$; crossing demands **square-root cancellation in the relative-form sense**, with the marginal constant
  pinned to $a=1$ by N3. The open quantitative fork is **$a_{\text{tail}}(X)<1$ vs $\equiv1$**.
- This is a genuine new front, not a restatement: it isolates RH's difficulty to a **tail** relative-form bound, a
  one-sided inequality between two explicit kernels, with a finite-defect descent waiting behind it. It does not
  cross the wall --- but it converts "the wall'' into a single inequality with a measurable constant
  $a_{\text{tail}}(X)$, which is computable and the natural next experiment.

> **The one thing to attack next, concretely:** compute $a_{\text{tail}}(X)=\sup_{g}\,
> \mathfrak p_{>X}[g]/\mathfrak a[g]$ (over admissible band-limited $g$, after removing the finite-rank head) as a
> function of $X$, and decide the fork $a_{\text{tail}}(X)<1$ vs $a_{\text{tail}}\equiv1$. Below $1$:
> $\kappa<\infty$ unconditionally, a result strictly between zero-density and RH. At $1$: the knife-edge is
> intrinsic to the tail, and the Pontryagin route shares N3's marginality --- a precise, falsifiable verdict
> either way.
