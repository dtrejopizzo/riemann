# 108.54 — Stage 5: the regularized route — Conditions I and II

## 0. Result

**Condition I is settled positively**, by an explicit construction (§1), upgrading 108_51's
"architecturally unproblematic" into a genuine theorem, modulo one named, minimal assumption
about Stage 0's category.

**Condition II fails for the natural renormalization**, and in a specific, informative way
(§2): the divergence identified in 108_51 Proposition 3.1 can be cancelled by an
$s$-dependent counter-term, but (a) the counter-term is provably **not unique** — the finite
remainder can be shifted to *any* value by an admissible change of scheme — and (b) under the
one canonical, parameter-free scheme (minimal subtraction: cancel exactly the growing terms
and nothing else), the remainder is **identically $0$**, for every mass-zero pair, which can
never equal $c_g(s)\Phi(s)$ except at accidental zeros of the latter, since $\Phi$ is
non-constant (108_38 Theorem 3.1) and generically nonzero (Theorem 3.2). This is a genuine
no-go **for the toy model**, stated with the toy/real distinction kept explicit throughout, as
the task requires.

## 1. Condition I: an explicit cutoff family

> ### Construction 1.1 (the cutoff family)
> Fix once and for all a $C^\infty$ bump $\chi:\mathbb R\to[0,1]$ with $\chi(u)=1$ for
> $|u|\le1$ and $\chi(u)=0$ for $|u|\ge2$ (the standard mollifier-type construction: with
> $\psi(t)=e^{-1/t}$ for $t>0$, $\psi(t)=0$ for $t\le0$, set $h(t)=\psi(t)/(\psi(t)+\psi(1-t))$,
> smooth, $0$ for $t\le0$, $1$ for $t\ge1$; put $\chi(u)=h(2-|u|)$ for $1\le|u|\le2$, $\chi(u)=1$
> for $|u|\le1$, $\chi(u)=0$ for $|u|\ge2$). For $s$ in the graded index set and $T>1$, define
> \[
>  f_{s,T}(x)=x^{s-1}\,\chi\!\Big(\frac{\log x}{\log T}\Big),\qquad x>0.
> \]

> ### Theorem 1.2 (compact support, for every finite $T$)
> $\mathrm{supp}\,f_{s,T}\subseteq[T^{-2},T^{2}]$, a compact subset of $(0,\infty)$, and
> $f_{s,T}\in C^\infty_c((0,\infty))$.

**Proof.** $\chi(\log x/\log T)\ne0$ requires $|\log x/\log T|\le2$, i.e.
$T^{-2}\le x\le T^{2}$ (using $T>1$ so $\log T>0$). Both $x\mapsto x^{s-1}$ and
$x\mapsto\log x/\log T$ are $C^\infty$ on $(0,\infty)$, and $\chi\in C^\infty(\mathbb R)$, so
$f_{s,T}$, a product of a composition of smooth maps, is $C^\infty$ on $(0,\infty)$; combined
with the compact support just shown, $f_{s,T}\in C^\infty_c((0,\infty))$. $\blacksquare$

> ### Theorem 1.3 ($f_{s,T}\to f_s$ locally uniformly, with all derivatives)
> For every compact $K\subset(0,\infty)$ there is $T_0=T_0(K)$ such that $f_{s,T}|_K=f_s|_K$
> **exactly** (not merely approximately) for every $T>T_0$; consequently
> $f_{s,T}\to f_s=(x\mapsto x^{s-1})$ in the topology of uniform convergence, on compact
> subsets of $(0,\infty)$, of every derivative (the $C^\infty_{\mathrm{loc}}$/compact-open
> $C^\infty$ topology).

**Proof.** $K\subset(0,\infty)$ compact means $K\subseteq[m,M]$ for some $0<m\le M<\infty$.
Choose $T_0$ large enough that $\log T_0>\max(|\log m|,|\log M|)$; then for $T>T_0$ and $x\in
K$, $|\log x/\log T|<1$, so $\chi(\log x/\log T)=1$ by construction, giving
$f_{s,T}(x)=x^{s-1}=f_s(x)$ identically on $K$. Since the two functions agree exactly (not
just approximately) on $K$ for $T>T_0(K)$, every derivative agrees too, and the convergence
claim follows immediately (a sequence that is eventually exactly constant on $K$ converges to
that constant in every topology defined by seminorms on $K$). $\blacksquare$

**What fails, and what this construction does not claim.** $f_{s,T}\not\to f_s$ in $L^p((0,
\infty),dx)$ for any $p\in[1,\infty]$, because $f_s(x)=x^{s-1}$ is not itself in $L^p$ (it does
not decay as $x\to0$ or $x\to\infty$ for any real $s$) — this is exactly Theorem 1.2 of 108_50
restated: no member of the *un*truncated family lies in a category built from decaying data,
so no truncated approximation can converge there either. The convergence proved above is
strictly weaker than $L^p$: it is termwise/local convergence, adequate for defining a limit of
the *pairing* (Condition II) if and only if the pairing itself has good enough continuity
properties in the cutoff — which is exactly what §2 shows is not automatic.

**Named assumption.** This construction resolves Condition I under the assumption that Stage
0's category of admissible compactly supported data includes $C^\infty_c((0,\infty))$ — the
minimal, standard reading of "compactly supported data" and consistent with everything about
Stage 0 quoted in the task (107_240's pairing formula, the quotient $V$, its nondegeneracy).
Nothing in the material available to this note indicates a narrower category (e.g. requiring
real-analyticity, or an algebraicity condition tied to the arithmetic side); if such a
restriction exists in Stage 0's own unread definitions, this construction would need revision,
but there is no evidence for it in the supplied material, so it is not manufactured here.
Under this assumption, **Condition I is proved**, not merely argued architecturally.

## 2. Condition II: does renormalization repair the divergence?

108_51 Proposition 3.1 (re-verified here, not re-proved) exhibits, for the toy pairing
$P(T;a)=\int_{1/T}^{T}x^{a-1}\,dx=(T^a-T^{-a})/a$ ($a\ne0$), a mass-zero pair
$s_1=0.3,s_2=0.7$, $\lambda_1=1,\lambda_2=-1$, with
\[
 Q(T)=\lambda_1P(T;s_1)+\lambda_2P(T;s_2)\xrightarrow[T\to\infty]{}-\infty .
\]
This section asks whether an $s$-dependent counter-term repairs this.

> ### Definition 2.1 (admissible counter-term)
> Fix $0<s_1<s_2<1$ (so both terms genuinely diverge) and $\lambda_1+\lambda_2=0$. A function
> $C(T)$, possibly depending on $s_1,s_2,\lambda_1,\lambda_2$ but not otherwise adjustable, is
> an **admissible counter-term** if $Q(T)-C(T)$ converges to a finite limit as $T\to\infty$,
> and $C(T)$ carries the same leading power-law growth as $Q(T)$ (i.e.
> $C(T)/(\lambda_2T^{s_2}/s_2)\to1$), so that it genuinely *removes* the divergence rather than
> adding an unrelated one.

> ### Proposition 2.2 (the minimal counter-term, and its remainder)
> $C_0(T):=\lambda_1T^{s_1}/s_1+\lambda_2T^{s_2}/s_2$ is admissible, and
> \[
>  \lim_{T\to\infty}\big(Q(T)-C_0(T)\big)=0 .
> \]

**Proof.** $Q(T)-C_0(T)=-\lambda_1T^{-s_1}/s_1-\lambda_2T^{-s_2}/s_2\to0$ since $s_1,s_2>0$.
Admissibility is immediate: $C_0(T)$ literally is the sum of the two growing terms of $Q(T)$.
$\blacksquare$

> ### Proposition 2.3 (the counter-term is not unique — a genuine ambiguity)
> For every $K\in\mathbb C$, $C_K(T):=C_0(T)+K$ is admissible, and
> $\lim_{T\to\infty}(Q(T)-C_K(T))=-K$. Hence the class of admissible counter-terms produces
> **every possible finite value** as the "renormalized limit," with no member of the class
> singled out except by an extra, unmotivated convention.

**Proof.** $C_K(T)-C_0(T)=K$ is bounded, hence does not affect the leading power-law growth
condition in Definition 2.1, so $C_K$ is admissible whenever $C_0$ is. And
$Q(T)-C_K(T)=(Q(T)-C_0(T))-K\to0-K=-K$ by Proposition 2.2. $\blacksquare$

**Consequence.** Renormalization by leading-term subtraction does not, by itself, produce a
well-defined finite limit: it produces a one-real-parameter (or one-complex-parameter) family
of possible limits, indexed by the free choice of $K$, and nothing internal to the toy model
selects a value. This is exactly the "genuine no-go" the task flagged as a live possibility:
**the toy-model limit is scheme-dependent.**

> ### Proposition 2.4 (the canonical scheme, if forced to choose, gives the wrong answer)
> If one adopts the parameter-free convention $K=0$ (subtract exactly the growing part and
> nothing else — the only choice requiring no extra input), the resulting remainder is
> identically $0$ for **every** admissible mass-zero pair $(s_1,\lambda_1;s_2,\lambda_2)$ with
> $0<s_1<s_2<1$, $\lambda_1+\lambda_2=0$. Consequently this scheme cannot reproduce
> $c_g(s)\Phi(s)$ except where the latter is itself $0$: $\Phi$ is non-constant (108_38
> Theorem 3.1) and not identically zero (Theorem 3.2), so the toy model's minimal-subtraction
> remainder and Stage 3's target function disagree on a set of full measure.

**Proof.** Immediate from Proposition 2.2, which holds for arbitrary $0<s_1<s_2<1$: the
remainder $0$ does not depend on $s_1,s_2$ at all, whereas $c_g(s)\Phi(s)$ is a nonconstant
function of $s$ by 108_38 Theorem 3.1. Two functions of $s$, one identically $0$ and the other
not, agree on at most the (measure-zero, and on the evidence of 108_38 Corollary 3.4, at most
countable) zero set of the second. $\blacksquare$

**What transfers to the real $I_{\mathrm{partial}}$, and what does not.**

*Transfers (architectural, not model-specific).* (i) A mass-zero condition on the
coefficients $\lambda_i$ alone does not, by itself, cancel a $T$-dependent divergence whose
*rate* depends on $s_i$ — this was already 108_51 Proposition 3.1's point, reconfirmed here.
(ii) Cancelling a power-law divergence by subtracting its own leading term is, generically, an
operation with a residual additive ambiguity — this is a soft fact about asymptotic expansions
(subtracting a divergent asymptotic series termwise is only defined up to whatever is *not*
divergent, i.e. up to a bounded correction), not special to this toy integral, and should be
expected to recur in any comparably naive regularization of a genuine Mellin-type pairing.

*Does not transfer (toy-specific, genuinely unknown for the real object).* Whether Stage 0's
actual pairing operator $T(\cdot)$ (never examined in this programme — 108_50 §5, 108_51 §5,
and this note all flag it as unread) already incorporates a **canonical** regularization that
sidesteps Proposition 2.3's ambiguity. The classical proof of Weil's explicit formula itself is
*not* a naive sharp-truncate-and-limit argument: it typically proceeds by a controlled contour
shift or a smoothed/Cesàro-summed count with an explicit, provably vanishing error term, which
is a specific, non-arbitrary regularization, not a free choice among a family as in
Proposition 2.3. It is entirely possible — and not excluded by anything proved here — that
Stage 0's $T$ is exactly such a canonical procedure, in which case Condition II might hold via
a route this toy model cannot see (the toy model uses a bare, unsmoothed truncation on
purpose, matching 108_51's construction, precisely *because* that is the naive case that needs
to be tested first). **This is not established either way here**; it is named as the one
remaining possible escape for Condition II, and is exactly the kind of fact this note does not
have the source material to check (Stage 0's internal definition of $T$ is out of read-scope,
per the task's instructions).

## 3. Scope

**Proved here.** Theorem 1.2 (compact support of $f_{s,T}$ for every finite $T$); Theorem 1.3
(convergence to $f_s$, locally uniformly with all derivatives, on compacts of $(0,\infty)$);
Propositions 2.2–2.4 (existence, non-uniqueness, and canonical-scheme failure of the
counter-term for the toy model $P(T;a)$).

**Read from source, not re-derived.** 108_51 Proposition 3.1 (the divergence itself, restated
and numerically reconfirmed, not reproved from scratch); 108_38 Theorem 3.1 (non-constancy of
$\Phi$), Theorem 3.2 (non-vanishing of $\Phi$), used only for the qualifying clause of
Proposition 2.4.

**Verified numerically.** Proposition 2.2's remainder $\to0$ for three different mass-zero
pairs across a range of $T$ up to $10^8$; Proposition 2.3's exact linear shift by $-K$ for
several values of $K$.

**Not established, and explicitly not claimed.** Whether Stage 0's actual, unread pairing
operator $T$ possesses a canonical (non-ambiguous) regularization that would make Condition II
hold by a route not captured by this toy model — flagged explicitly in §2 as the single
remaining open channel, not resolved here for lack of source access, and not claimed to be
either true or false. Whether a smoothed cutoff (as in Construction 1.1, rather than the sharp
truncation of the toy model) changes the *leading-order* divergence exponent — not computed
here; only the sharp-cutoff toy model (matching 108_51's own construction) is analyzed in §2,
and the qualitative persistence of an additive scheme ambiguity under smoothing is asserted
only as a plausible expectation (architectural, stated as such), not proved.

**No zero of $\xi$ enters any definition in this note.**

## 4. Verifier

`108_54_regularized_route.py`: (1) numerically confirms $f_{s,T}$'s support is contained in
$[T^{-2},T^2]$ and that $f_{s,T}$ agrees exactly with $f_s$ on a fixed compact interval once
$T$ exceeds the threshold from Theorem 1.3's proof, checked across growing $T$ (a genuine
convergence/refinement test: the difference $\sup_K|f_{s,T}-f_s|$ is shown to be **exactly**
$0$, not merely small, once $T>T_0(K)$, and nonzero before); (2) recomputes $Q(T)$ and
confirms it diverges (cross-checking 108_51's closed form, not re-deriving Proposition 3.1);
(3) computes $C_0(T)$, confirms $Q(T)-C_0(T)\to0$ for three mass-zero pairs across $T$ from
$10$ to $10^{50}$, with the error shrinking as $T$ grows and staying below the closed-form
bound $2T^{-s_1}/s_1$ (an actual convergence test against the proved rate, not an arbitrary
tolerance — the remainder at $T=10^{50}$ must be smaller in magnitude than at $T=10^{5}$,
which must be smaller than at $T=10$); (4) confirms the exact $-K$ shift of Proposition 2.3
for several $K$; (5)
confirms that the minimal-subtraction remainder ($\equiv0$) disagrees with $\Phi(s_1)-\Phi(s_2)$
type target values (using the closed form of 108_53) away from accidental coincidences,
illustrating Proposition 2.4 concretely.
