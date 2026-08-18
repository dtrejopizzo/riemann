# 108.23 — The smeared object converges as a formal sum, but is a
# zero-sourced definition, not a forced extension: the dichotomy settled

## 0. Question and verdict

108_22 showed $\Lambda_g$ admits no continuous extension to $f_a$ along the
canonical (coherent) topology: the net used throughout this Phase to give
$f_a$ operative meaning makes $\Lambda_g$ diverge. The mission's task (2)
asks about a different-looking object, obtained by *smearing* in the grade
$a$: for $\varphi$ a test profile on $(0,1)$,
\[
 \langle\Lambda_g(f_\bullet),\varphi\rangle
 \;:=\;\int_0^1\varphi(a)\,\Lambda_g(f_a)\,da
 \;\overset{\text{formally}}{=}\;
 \sum_{\xi(\rho)=0}{}'\varphi(\mathrm{Re}\,\rho)\,\overline{\hat
 g(\rho')}
 \tag{S}
\]
(dropping the boundary terms $\hat f(0),\hat f(1)$ for now — they require no
new argument, see §3) obtained by formally substituting $\rho\mapsto
\mathrm{Re}\,\rho$ for the "evaluation of $\hat f_a$" into the zero-sum term
of the explicit formula $(*)$ of 108_22 §1.

\[
 \boxed{\text{The right-hand side of (S) is a genuinely convergent sum for
 admissible }(\varphi,g)\text{ (Theorem 2.1, proved unconditionally below,
 no zero location used beyond the classical fact }0<\mathrm{Re}\,\rho<1
 \text{). But it is }\textbf{not}\text{ obtained, and by 108\_22 Theorem 3.1
 cannot be obtained, as the continuous extension of the zero-free functional
 }\Lambda_g\text{: no such extension exists to compare it to. The dichotomy
 resolves to (ii) for general }\varphi\text{: (S), as literally written, is
 one admissible-looking definition that routes through the zero side, not a
 forced consequence of density and continuity, and the source rule of
 108\_00 §2 forbids using it as a definition. §4 identifies exactly the
 sub-case (mean-zero }\varphi\text{) where a genuinely zero-free, forced
 construction }\textit{does}\text{ exist on the arithmetic side —
 developed fully in 108\_24 — sharpening the dichotomy from a strict binary
 into a precise boundary.}}
\]

No zero of $\xi$ enters any definition below (Theorem 2.1's hypotheses use
only the classical, unconditional zero-counting bound). `ROW_A_STATUS`
remains `partial`.

## 1. The dichotomy, made precise

> ### Definition 1.1 (the two readings of "extension")
> **Reading (i).** $\langle\Lambda_g(f_\bullet),\varphi\rangle$ is *the*
> value forced by taking a $\tau$-continuous extension of $\Lambda_g$ (some
> topology of the kind 108_22 sought) and evaluating/integrating it against
> $\varphi$-weighted graded elements. Under this reading, (S) would be a
> **theorem**, derived from density and continuity of a zero-free-defined
> object — no admissibility question about the zero-sum would arise,
> because it would already be forced to hold by 108_22-style reasoning
> applied to the whole family at once.
> **Reading (ii).** $\langle\Lambda_g(f_\bullet),\varphi\rangle$ is *defined*
> to be the right-hand side of (S), obtained by substituting the
> weak-limit reading of $\hat f_a$ (108_05 §4.2, itself explicitly labeled
> "not proved") into the zero-sum term of the explicit formula. Under this
> reading, (S) is a **definition**, and 108_00 §2's source rule applies: no
> zero of $\xi$ may enter a definition.

These are mutually exclusive as accounts of what (S) *is*. Settling the
dichotomy means determining which reading is available.

## 2. First: the formal sum (S) is genuinely convergent

This half is independent of the dichotomy and is proved unconditionally.

> ### Theorem 2.1 (absolute convergence of the zero-sum term of (S))
> Let $\varphi:\mathbb R\to\mathbb C$ be bounded with $\mathrm{supp}\,
> \varphi\subseteq[0,1]$, and let $g$ be such that $\hat g$ is entire with
> $|\hat g(\sigma+it)|=O(e^{-c t^2})$ for some $c>0$, uniformly for $\sigma$
> in bounded sets (satisfied, e.g., by any Gaussian-Mellin $g$, §5). Then
> \[
>  \sum_{\xi(\rho)=0}{}'\big|\varphi(\mathrm{Re}\,\rho)\big|\cdot
>  \big|\hat g(\rho')\big| \;<\;\infty .
> \]

**Proof.** Every nontrivial zero of $\xi$ satisfies $0<\mathrm{Re}\,\rho<1$
(classical: $\xi(s)=\xi(1-s)$ together with the nonvanishing of $\zeta$ on
$\mathrm{Re}(s)\ge1$ and $\mathrm{Re}(s)\le0$ from the Euler product and the
functional equation; this is unconditional, does not touch RH). Hence
$\varphi(\mathrm{Re}\,\rho)$ is always evaluated inside $\varphi$'s domain
and $|\varphi(\mathrm{Re}\,\rho)|\le M:=\sup|\varphi|<\infty$ for every
$\rho$ — the real parts themselves play no further role in the estimate.
Group the zeros by height: let $N(T)$ count zeros with $0<\mathrm{Im}\,
\rho\le T$; the classical Riemann–von Mangoldt formula (unconditional)
gives $N(T)=O(T\log T)$. Writing $\rho'=1-\bar\rho=(1-\mathrm{Re}\,\rho)+
i\,\mathrm{Im}\,\rho$, so $|\mathrm{Im}\,\rho'|=|\mathrm{Im}\,\rho|$ and
$\mathrm{Re}\,\rho'\in(0,1)$ (bounded), the hypothesis on $\hat g$ gives
$|\hat g(\rho')|=O(e^{-c(\mathrm{Im}\,\rho)^2})$. Then
\[
 \sum_\rho|\varphi(\mathrm{Re}\,\rho)||\hat g(\rho')|
 \le M\sum_\rho O(e^{-c(\mathrm{Im}\,\rho)^2})
 = M\int_0^\infty O(e^{-cT^2})\,dN(T)
\]
and integrating by parts against $N(T)=O(T\log T)$, the boundary terms
vanish and the remaining integral $\int_0^\infty O(T\log T)\cdot
O(Te^{-cT^2})\,dT$ converges absolutely (Gaussian decay dominates any
polynomial-times-log growth). $\square$

This is verified numerically in §5 against a *synthetic* zero-ordinate
sequence built only from the classical counting-function asymptotic (no
actual zero locations are used, so nothing here depends on, or could be
mistaken for, information about RH): partial sums stabilize (Cauchy) as more
terms are included when $\hat g$ has Gaussian decay, and demonstrably fail
to stabilize when $\hat g$'s decay is too slow relative to $N(T)$ — showing
the decay hypothesis is load-bearing, not decorative (Rule 6 compliance:
this tests the actual analytic property, not a threshold).

## 3. Reading (i) is unavailable: 108_22 already excludes it

> ### Theorem 3.1 (reading (i) fails)
> Under the hypotheses of 108_22 Theorem 3.1 (coherence), no continuous
> extension of $\Lambda_g$ to $f_a$ exists for *any* $a\in\mathbb C$, hence
> in particular no continuous extension of the family $a\mapsto
> \Lambda_g(f_a)$ exists to be integrated against $\varphi$. Consequently
> (S) cannot be **reading (i)**: there is no density-plus-continuity
> argument to derive it from, because the object it would have to equal
> ($\int\varphi(a)\Lambda_g(f_a)\,da$, built from a continuous extension of
> $\Lambda_g$) does not exist.

**Proof.** Immediate from 108_22 Theorem 3.1, applied pointwise for every
$a$ in $\mathrm{supp}\,\varphi$. A finite or continuum linear combination of
non-existent quantities is not made to exist by combining them; if it were,
that would itself require a separate continuity argument for the combined
functional — which is exactly what 108_24 undertakes for the mean-zero
sub-case, and exactly what is *not* undertaken, or available, for general
$\varphi$ here. $\square$

Concretely: the **candid** arithmetic-side smeared quantity, using the same
canonical net as 108_22,
\[
 \Sigma_g(\varphi,T):=\int_0^1\varphi(a)\,\Lambda_g(f_{a,T})\,da,
\]
diverges as $T\to\infty$ for **general** $\varphi$ — verified in §5(C) — for
the same reason as 108_22 Theorem 3.1: 108_21 Theorem 1.1(a)-(b) shows the
divergent part of $\Lambda_g(f_{a,T})$ has coefficient $\varphi_0=1$,
*independent of $a$*; writing $\Lambda_g(f_{a,T})=D(T)+L_g(a,T)$ with $D(T)$
the (in this program, still-unevaluated) $a$-independent divergent piece and
$L_g(a,T)$ the closed, $a$-dependent piece of 108_11,
\[
 \Sigma_g(\varphi,T)=D(T)\int_0^1\varphi(a)\,da\;+\;\int_0^1\varphi(a)\,
 L_g(a,T)\,da,
\]
and $D(T)\to\infty$ while $\int\varphi\,da\ne0$ for a generic $\varphi$, so
$\Sigma_g(\varphi,T)$ diverges for generic $\varphi$ exactly as
$\Lambda_g(f_{a,T})$ itself does. This is the candid, zero-free-computed
object corresponding to the left side of (S); it does not converge, so (S)'s
right-hand side (which *does* converge, Theorem 2.1) cannot be its limit,
for general $\varphi$.

## 4. Reading (ii) is what remains — and where it stops being arbitrary

> ### Corollary 4.1 (the dichotomy, resolved for general $\varphi$)
> For $\varphi$ with $\int_0^1\varphi\,da\ne0$, (S) is **reading (ii)**: a
> definition obtained by substituting the zero-side representation and
> 108_05 §4.2's admittedly-formal delta reading, not derivable from density
> and continuity of the zero-free $\Lambda_g$ (Theorem 3.1). By 108_00 §2,
> it is therefore **not admissible as a definition** for testing principal
> invariance, however convergent it is as a bare numerical series
> (Theorem 2.1).

This is not a purely negative endpoint. §3's identity
$\Sigma_g(\varphi,T)=D(T)\int\varphi\,da+\int\varphi(a)L_g(a,T)\,da$
isolates *exactly* the mechanism by which reading (i) fails for general
$\varphi$: the $a$-independent divergent piece $D(T)$, multiplied by a
generically-nonzero scalar $\int\varphi\,da$. It also isolates exactly the
condition under which that mechanism is disarmed **without evaluating or
regularizing $D(T)$ at all**: $\int_0^1\varphi(a)\,da=0$. For such $\varphi$,
\[
 \Sigma_g(\varphi,T)=\int_0^1\varphi(a)\,L_g(a,T)\,da
\]
*identically*, at every finite $T$ — not asymptotically, not up to a
vanishing error, but exactly, because $D(T)\cdot 0=0$ regardless of how
divergent $D(T)$ is. If $L_g(a,T)$ itself has a $T\to\infty$ limit (108_11's
already-closed, distributional, $a$-dependent object — cited, not
re-derived here), then $\Sigma_g(\varphi,T)$ converges as $T\to\infty$,
**by a genuine continuity argument on the zero-free arithmetic side, using
no zero of $\xi$ and no formal delta reading.** This is reading (i),
recovered — not for all $\varphi$, but on the mean-zero subspace. 108_24
carries this out as the Phase's positive, usable deliverable.

> ### Remark 4.2 (an open question, flagged, not answered here)
> Whether the mean-zero restriction of (S)'s right-hand side (the formal
> zero-sum) *equals* the mean-zero arithmetic-side construction of 108_24 is
> a natural question — both are built from the same explicit formula in
> principle — but it is **not resolved here**. It would require justifying
> an interchange of the $T\to\infty$ limit with the sum over $\rho$ inside
> (S), term by term, which this note does not undertake (it would need a
> uniform, not merely pointwise, version of 108_05 Theorem 3.1's weak
> convergence, applied with the roles of the grading variable $a$ and the
> zero variable $\rho$ exchanged). It is recorded as open, for future work,
> and is not needed for anything claimed in this Phase: 108_24's
> construction is self-contained on the arithmetic side and does not rely on
> this equality.

## 5. Scope

**Proved here:**

* Theorem 2.1: the zero-sum term of (S) converges absolutely, for bounded
  $\varphi$ compactly supported in $[0,1]$ and $\hat g$ with Gaussian (or
  faster) decay along verticals — unconditionally, using only the classical
  fact $0<\mathrm{Re}\,\rho<1$ and the classical bound $N(T)=O(T\log T)$;
* Theorem 3.1 / Corollary 4.1: the dichotomy resolves to reading (ii) for
  $\varphi$ with $\int\varphi\,da\ne0$ — (S) is a zero-sourced definition,
  inadmissible under 108_00 §2's source rule, not a forced extension;
* the exact (not asymptotic) identity isolating $\int\varphi\,da=0$ as the
  condition disarming the $a$-independent divergence, motivating 108_24.

**Read from source, cited, not re-derived:**

* 108_22 Theorem 3.1 (no continuous extension along the canonical net);
* 108_21 Theorem 1.1(a)-(b) ($a$-independence of the divergence coefficient
  $\varphi_0=1$);
* 108_11's closure of the $a$-dependent distributional piece $L_g(a,T)$'s
  limit (cited by name only; not re-derived, not re-verified here);
* the classical Riemann–von Mangoldt zero-counting asymptotic and the
  classical strip-confinement $0<\mathrm{Re}\,\rho<1$.

**Not established, and explicitly not claimed:**

* Remark 4.2's open equality between (S) restricted to mean-zero $\varphi$
  and 108_24's arithmetic-side construction;
* any value for $D(T)$'s divergent limit, or for $\sum_p C_p$;
* that Theorem 2.1's hypotheses on $\hat g$ (Gaussian decay) are necessary,
  only that some such hypothesis is (§5(B)'s slow-decay control case);
* anything about RH; `ROW_A_STATUS` remains `partial`.

## 6. Verifier

`108_23_smeared_pairing_convergence_and_dichotomy.py` checks: (A) Theorem
2.1's convergence, numerically, on a *synthetic* zero-ordinate sequence
built solely from inverting the classical unconditional counting-function
asymptotic $N(T)=(T/2\pi)\log(T/2\pi e)+7/8$ by bisection (no real zero
locations are used anywhere) — partial sums against a Gaussian-decay $\hat
g$ are shown to stabilize (Cauchy) as more terms are added; (B) the same
sum against an insufficiently-decaying control $\hat g$ is shown to *not*
stabilize, confirming the decay hypothesis is load-bearing; (C) the exact
identity $\Sigma_g(\varphi,T)=D(T)\int\varphi\,da+\int\varphi(a)L_g(a,T)\,da$
on a concrete illustrative model of $D(T)$ (unbounded) and $L_g(a,T)$
(bounded, convergent), confirming numerically that a generic $\varphi$
diverges and a constructed mean-zero $\varphi$ converges to exactly
$\int\varphi(a)L_g(a,T\!\to\!\infty)\,da$.
