# 108.29 — Route Beta (the ray reading) is correct but vacuous; Route Gamma (a canonical weight normalization) is impossible

## 0. Answer

> **Route Beta.** 108_03 §3 (Proposition 3.1) imposes **no invariance
> requirement at all** — it proves exact covariance of the section $U_s$,
> full stop. The "requires pointwise equality or equality of class/ray"
> question therefore has nothing to answer *in §3*; the invariance
> requirement is entirely Definition 6.1's (§6), a separate, later choice.
> Reading Definition 6.1 at the level of rays, the positivity of
> $\chi_s(m,n)$ **does** make $\mathrm{Div}(U_s)$ and its
> Frobenius-transform lie on a common ray, for **every** real $s$ — but
> this is a content-free triviality of one-dimensional linear algebra
> (§2 below), not a mathematically load-bearing fact about $\chi_s$. Route
> Beta, on its own, is **too weak to justify anything**: it would validate
> literally every weight indiscriminately, for a reason unrelated to why
> any particular weight should count as principal.

> **Route Gamma.** Fails outright. No canonical (chart-independent,
> weight-only) rescaling of $U_s$ or $u_s$ can convert a genuinely
> $n$-dependent character into the trivial one, except at the single point
> where it already is trivial. This is a clean structural no-go (§3), and
> the two candidate loci it could produce ($s=0$ or $s=-1$, depending on
> which homogeneity is normalized) both lie outside, or on the boundary of,
> the open strip $(0,1)$.

Neither route closes Stage 1 on its own terms. §4 records exactly what each
one contributes to the record, and hands off to Route Delta (108_31), which
supplies the substantive argument Beta gestures at without proving.

No zero of $\xi$ is used anywhere.

## 1. What 108_03 §3 actually requires

108_03 Proposition 3.1, quoted precisely: for $s\notin\{0,-1\}$,

\[
 U_s(mx,ny)=n^{1+s}m^{-s}\,U_s(x,y)
 \tag{1.1}
\]

**exactly, with no affine correction** — a statement about the *value* of
the section $U_s$ at the rescaled point, nothing more. Section 3 does not
mention $\mathrm{Div}$, does not mention invariance, and does not
impose any requirement to be satisfied. It is Definition 6.1, in §6, that
first introduces "genuinely invariant (fixed, not merely covariant)" as the
criterion for principality — a definitional choice made three sections
later, using §3's covariance law as *input* but not dictated by it.

**Consequence.** The question "does §3 require pointwise equality of
$\mathrm{Div}$, or equality of class/ray?" is answered: **neither** —
§3 requires nothing about $\mathrm{Div}$ at all. Whatever notion of
invariance is used to define "principal" is supplied entirely by Definition
6.1, and is therefore open to revision on its own merits, which is exactly
what 108_31 undertakes.

## 2. Route Beta: the ray coincidence is real, but vacuous

### Proposition 2.1 (same ray, for every weight, always)

For every $s\in\mathbb R\setminus\{0,-1\}$ and every $m,n\in\mathbb N^\times$,
$\mathrm{Div}(U_s)$ and its Frobenius/chart-transform
$\chi_s(m,n)\mathrm{Div}(U_s)$ lie on the same ray
$\mathbb R_{>0}\cdot\mathrm{Div}(U_s)$ in the space of currents.

**Proof.** By 108_03 Definition 4.1, $\mathcal L_s:=\mathbb R\cdot U_s$ is
**one-dimensional** by construction. Hence $\mathrm{Div}(\mathcal
L_s)=\mathbb R\cdot\mathrm{Div}(U_s)$ is a single line through the
origin, for *every* $s$, independent of any property of $\chi_s$
whatsoever — this is a fact about the dimension of $\mathcal L_s$, proved
already in 108_03/108_26, not re-derived here. Multiplication by any
nonzero scalar preserves this line as a *set*; multiplication by a
*positive* scalar preserves each of its two rays separately, keeping
$\mathrm{Div}(U_s)$ and $\chi_s(m,n)\mathrm{Div}(U_s)$ on the
same ray. Positivity holds because $\chi_s(m,n)=n^{1+s}m^{-s}$ is a real
power of positive integers $m,n>0$, hence strictly positive for *every*
real $s$ (elementary: $x^t>0$ for $x>0$, any real $t$). $\square$

### Proposition 2.2 (the mechanism proving 2.1 is independent of $\chi_s$'s value)

Proposition 2.1's proof used only two facts: (i) $\mathcal L_s$ is
one-dimensional, and (ii) $\chi_s(m,n)>0$. Neither fact depends on $s$ in a
way that could fail: (i) holds for every $s$ by Definition 4.1 unqualified,
and (ii) holds for every $s\in\mathbb R$ because $\chi_s(m,n)$ is *always*
a positive number raised to a real power. **No value of $s$ can violate
Proposition 2.1.** Hence the "same ray" property does not distinguish any
weight from any other, in particular it does not distinguish $s=0$ from
$s=\tfrac12$, and equally does not distinguish $s=\tfrac12$ from, say,
$s=-100$ or $s=1000$.

**Consequence.** If "principal" is redefined as "same ray under Frobenius"
(Route Beta's proposed reading), the resulting notion is satisfied by
**every** nonzero element of **every** weight space of $\mathcal G$,
unconditionally. This *does* place witnesses inside $(0,1)$ — trivially,
along with every other interval — but the mechanism supplying this outcome
(positivity of $n^s$) is not actually load-bearing: the same conclusion
(every weight admitted) would follow from the one-dimensionality of
$\mathcal L_s$ alone, with no reference to the sign or value of $\chi_s$ at
all, as long as invariance is read at the level of the ambient *line*
rather than the ray. Route Beta, in other words, does not supply an
argument for *why* ray-level (or line-level) equivalence is the right
notion of "principal" here — it only observes that, once that notion is
adopted, the ray condition happens to be satisfied everywhere, which is
guaranteed in advance by the shape of $\mathcal G$ and carries no
independent content. A definition that is satisfied unconditionally by an
entire family, for a reason unrelated to the family's actual arithmetic
content, is not by itself a *justification* for adopting that definition.

### 2.3 What Route Beta is missing

Route Beta needs a reason, external to the vacuous computation above, for
why the correct classical transplant of "principal" tolerates positive
rescaling but not the literal identity used in Definition 6.1. That reason
is supplied — with actual content, tied to classical divisor theory rather
than to a triviality of one-dimensional subspaces — by Route Delta (108_31).
Route Beta is recorded here as *consistent with* Route Delta's conclusion,
not as an independent route to it.

## 3. Route Gamma: no canonical normalization can move the invariance locus

### 3.1 The candidate normalization

108_03 (2.1): $u_s(r)=r^{s+1}/(s(s+1))$ for $s\notin\{0,-1\}$.

### Proposition 3.1 (exact homogeneity of $u_s$)

For every $n>0$, $u_s(r/n)=n^{-(s+1)}u_s(r)$ exactly.

**Proof.** $u_s(r/n)=(r/n)^{s+1}/(s(s+1))=n^{-(s+1)}r^{s+1}/(s(s+1))=n^{-(s+1)}u_s(r)$.
$\square$

This is the identity Route Gamma's instructions point to: it exhibits a
second, genuine one-parameter character, $\tau_s(n):=n^{-(s+1)}$, distinct
from $\chi_s(m,n)$ of 108_03 (3.3) and from $\chi(n)=n^s$ of 108_27 — all
three are candid characters of the same family, differing only in which
homogeneity (in $x$, in $y$, or in the ratio $r$) is being tracked.
$\tau_s(n)=1$ for all $n$ iff $s=-1$.

### Lemma 3.2 (no canonical, weight-only rescaling changes a character's dependence on $n$)

Let $V_s$ be any one-parameter family (indexed by $s$) transforming under
an action parametrized by $n$ as $V_s(\text{action by }n) = \lambda_s(n)\,V_s$,
where $\lambda_s(n)=n^{t(s)}$ for some function $t(s)$. Let $k:\mathbb
R\to\mathbb R\setminus\{0\}$ be **any** function of $s$ alone (i.e. not
depending on $n$ or on the chart — the defining property of a "canonical"
normalization, since a normalization that referenced $n$ would just be
another, disguised chart choice). Define $\widetilde V_s:=k(s)\,V_s$. Then

\[
 \widetilde V_s(\text{action by }n) = k(s)\,V_s(\text{action by }n)
 = k(s)\,\lambda_s(n)\,V_s = \lambda_s(n)\,\widetilde V_s .
\]

**$\widetilde V_s$ transforms by exactly the same multiplier $\lambda_s(n)$
as $V_s$.** Consequently $\widetilde V_s$ is invariant under the action for
all $n$ if and only if $V_s$ is, i.e. iff $t(s)=0$ — the identical
condition, for the identical set of $s$.

**Proof.** The computation above is the entire proof: $k(s)$ commutes past
$\lambda_s(n)$ because both are scalars, and $k(s)\ne0$ so it cannot create
or destroy triviality of $\lambda_s(n)$. $\square$

### Corollary 3.3 (Route Gamma fails)

No canonical, weight-only renormalization of $U_s$ (equivalently of $u_s$)
can enlarge the set of weights at which the corresponding object is
literally Frobenius/chart-invariant. Two genuine one-parameter characters
are in play here, and Lemma 3.2 applies to each separately: the
$x$-rescaling-only slice $\chi_s(m,1)=m^{-s}$ of 108_03 (3.3) — the slice
108_27's Theorem 2.1 actually tracks, since 108_27's $\chi(n)=n^{s}$ is
exactly $\chi_s(n,1)$ inverted in the naming convention — is trivial for
all $m$ iff $s=0$; the ratio-homogeneity $\tau_s(n)=n^{-(s+1)}$ of
Proposition 3.1 is trivial for all $n$ iff $s=-1$. (The full two-parameter
$\chi_s(m,n)=n^{1+s}m^{-s}$ is never trivial for *all* $(m,n)$ jointly at
any single $s$, since that would force $s=0$ and $s=-1$ simultaneously —
consistent with 108_03 Proposition 3.1 only asserting affine-corrected,
not exact, covariance at those two degenerate weights.) By Lemma 3.2,
neither one-parameter locus moves under **any** rescaling $U_s\mapsto
k(s)U_s$. Neither locus lies in the open strip $(0,1)$: $s=0$ is its
excluded lower boundary (108_26 Proposition 2.1), and $s=-1$ is not in the
strip at all.

**No canonical weight normalization exists that relocates the invariance
locus into $(0,1)$.** This is not a failure of imagination about which
normalization to try — Lemma 3.2 shows the outcome is the same for *every*
possible choice of $k(s)$, because the mechanism (a character genuinely
depending on $n$ cannot be cancelled by a factor that does not depend on
$n$) is structural.

## 4. What this leaves for Route Delta

Both routes examined here fail to supply an independently justified
resolution:

* Beta's computation is correct but content-free (§2) — it does not
  distinguish $(0,1)$ from any other interval, or indeed from the whole
  real line, and does not explain *why* ray-level equivalence is the right
  notion;
* Gamma is a clean structural impossibility (§3) — no normalization,
  however clever, can move the invariance locus at all, let alone into the
  open strip.

What is needed is an argument, external to the covariance formulas
themselves, for *why* "principal" should not require literal
Frobenius-fixedness in the first place — i.e. a substantive reason to
revise Definition 6.1, not merely a computation that happens to be
satisfied everywhere or nowhere. That argument, grounded in how classical
principal divisors actually behave under a group action (not in a property
special to $\mathcal G$), is Route Delta's contribution, taken up in
108_31.

## 5. Scope

Proved here:

* §1: 108_03 §3 imposes no invariance requirement; Definition 6.1 (§6) is
  the sole source of the invariance criterion under examination;
* Proposition 2.1: $\mathrm{Div}(U_s)$ and its transform lie on a
  common ray, for every real $s$;
* Proposition 2.2: this holds for a reason (one-dimensionality of
  $\mathcal L_s$, positivity of real powers) independent of the value of
  $s$, hence is not discriminating;
* Proposition 3.1: the exact ratio-homogeneity $u_s(r/n)=n^{-(s+1)}u_s(r)$;
* Lemma 3.2 and Corollary 3.3: no canonical weight-only rescaling can move
  the invariance locus of any $n$-dependent character.

Read from source, not re-derived: 108_03 Definition 4.1, Proposition 3.1,
Definition 6.1; 108_26 Proposition 2.1; 108_27 fact (c) and Theorem 2.1.

Not established, and explicitly not claimed:

* that Route Beta or Route Gamma, on their own, resolve 108_26 §4.1's open
  question — both are shown insufficient here;
* any revision to Definition 6.1 — that is 108_31's task;
* anything about complex $s$.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 6. Verifier

`108_29_routes_beta_and_gamma_examined.py` checks: exact positivity of
$\chi_s(m,n)=n^{1+s}m^{-s}$ across a bank of $s$ (including negative $s$)
and $(m,n)$ pairs, confirming Proposition 2.1's hypothesis holds
unconditionally; that the one-dimensionality of $\mathcal L_s$ (by
construction, $\mathrm{Div}(cU_s)$ for varying $c$ always samples a
single line) holds regardless of $s$; the exact ratio-homogeneity of
Proposition 3.1 by direct substitution; and Lemma 3.2 concretely, by
applying several different candidate normalizations $k(s)$ to $\chi_s$ and
$\tau_s$ and confirming the invariance locus (the value of $s$ at which the
rescaled character is trivial for all tested $n$) is unchanged in every
case.
