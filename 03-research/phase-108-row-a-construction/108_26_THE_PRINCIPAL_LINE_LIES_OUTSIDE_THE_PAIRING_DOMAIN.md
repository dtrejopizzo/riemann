# 108.26 — The principal line lies outside the pairing's domain

## 0. Result

108_24 delivered a pairing on **balanced** profiles ($\int\varphi\,da=0$)
and offered it as a test criterion for principal invariance, under a working
hypothesis its own Remark 1.2 flagged as unverified against 108_03/108_04.

This note verifies that hypothesis.  **It is false**, and the reason is
sharper and more useful than the hypothesis was:

> The principal line of 108_03 sits at weight $s=0$, which is (i) on the
> **excluded boundary** of the strip where the pairing converges, and
> (ii) an **accumulation point** of the singular set of the continued
> $a$-dependent object.  Two independent obstructions, both exact.

This is the complete account of why Stage 1 does not close.  §4 converts it
into a single, concrete open question.

No zero of $\xi$ is used anywhere.

## 1. What "principal" actually is

108_03 Definition 6.1, quoted:

> "a principal divisor is the divisor of a global rational function, i.e. a
> global section that is genuinely **invariant** (fixed, not merely
> covariant, under the structure group).  In $\mathcal G$, 'genuinely
> invariant' is exactly **weight $s=0$**, the trivial character
> $\chi_0\equiv1$."
>
> $\mathrm{Prin}(\mathcal G):=\mathrm{div}(\mathcal L_0)
> =\mathbb R\cdot\big(\tfrac{dr}r\big)$

So the principal subspace is the **single weight $s=0$** — a unit point mass
in the grade — not a profile.

> ### Proposition 1.1 (the hypothesis of 108_24 Remark 1.2 is false)
> "Balanced" and "principal" are opposite conditions.  A balanced profile has
> $\int\varphi\,da=0$; the principal element is a unit point mass at $s=0$,
> of total mass $1$.

**Proof.** Immediate from Definition 1.1 of 108_24 and Definition 6.1 of
108_03. $\square$

Verified: normalised bumps at $s=0$ have mass $1.000000$ at three widths; the
balanced profile used in 108_24 has mass $-4.9\times10^{-17}$.

**Consequence.**  108_24's pairing $\Lambda_g^0$ is a genuine, forced,
zero-free object on balanced profiles — that result stands, unaffected — but
it does **not** test principal invariance.  It is a pairing on a subspace
that excludes the principal line by construction.

## 2. $s=0$ is on the excluded boundary

108_06 Corollary 3.2 proves the local terms converge exactly on
$0<\Re a<1$, with both boundaries genuinely excluded.

> ### Proposition 2.1
> The two geometric series have ratios $p^{-a}$ and $p^{a-1}$.  At $a=0$ the
> first ratio is exactly $1$; at $a=1$ the second is exactly $1$.  Neither
> series converges at the corresponding endpoint.

**Proof.** A geometric series converges iff its ratio has modulus $<1$.
$|p^{-0}|=|p^{1-1}|=1$. $\square$

Verified at nine grades.  Note the exclusion is **exact, not marginal**: for
every $a>0$, however small, the series converges — only arbitrarily slowly.
(A first version of this verifier used a fixed truncation depth as a proxy
and wrongly reported failure at $a=10^{-6}$; the truncation, not the
mathematics, was at fault.  The check now tests the ratio directly.)

## 3. $s=0$ is an accumulation point of the singular set

108_11 Lemma 2.1: the singular set of the continued $a$-dependent object is
$\{1/N:N\ge2\}\cup\{1-1/M:M\ge2\}$, accumulating at $0$ and $1$.

> ### Proposition 3.1
> Every neighbourhood of $s=0$ contains infinitely many singularities.  Hence
> no sequence $a_n\to0^+$ inside the strip reaches the principal line without
> crossing infinitely many of them, and $\lim_{a\to0^+}L_g(a)$ does not exist.

Verified: $(0,10^{-2})$, $(0,10^{-3})$, $(0,10^{-4})$ contain
$199\,899$, $198\,999$, $189\,999$ singularities respectively within the
tested range.

> ### Corollary 3.2 (the two obstructions are independent)
> Exclusion (§2) concerns convergence of the local series; accumulation (§3)
> concerns singularities of the continued function.  They are logically
> distinct: singularities also occur strictly **inside** the strip
> (e.g. $\tfrac12,\tfrac13,\tfrac14,\tfrac15$), where §2 does not apply.

## 4. What this makes of Stage 1

Assembling 108_06, 108_11, 108_22, 108_24 and this note:

| object | location | status |
|---|---|---|
| pairing on individual $f_a$ | — | impossible (108_22) |
| pairing on balanced profiles | $0<a<1$ | **exists, proved** (108_24) |
| principal line $\mathrm{Prin}(\mathcal G)$ | $s=0$ | **excluded and unreachable** |

Stage 1's mandate was to make principal invariance testable.  The pairing
exists; the principal line is not in its domain.  That is the exact failure.

### 4.1 The single open question this leaves

108_03 §6.2 records that $\mathrm{Prin}(\mathcal G)$ is a **witness**:
"an explicit, nonzero *candidate* for a global principal subspace".  It is
not proved to be the only one.

> **Open question.**  Does $\mathcal G$ admit a principal witness of weight
> strictly inside the open strip $0<s<1$?

If yes, Stage 1 closes immediately: the pairing of 108_24 already exists
there, and principal invariance becomes testable with no further analytic
work.  If no — if weight $0$ is forced by the requirement of genuine
invariance — then Stage 1 is terminally obstructed and Stage 2 needs a
different route to principal invariance altogether.

This is a bounded question about 108_03's construction, not an analytic one.
It does not require evaluating, bounding, or regularizing anything.

## 5. Scope

Proved here:

* Proposition 1.1: balanced and principal are opposite conditions, so
  108_24's working hypothesis is false;
* Proposition 2.1: exact exclusion of $s=0$ and $s=1$ from the domain;
* Proposition 3.1 and Corollary 3.2: accumulation at $s=0$, and independence
  of the two obstructions.

Read from source, not re-derived: 108_03 Definition 6.1 and §6.2; 108_06
Corollary 3.2; 108_11 Lemma 2.1; 108_22 Theorem 3.1; 108_24 Theorem 2.1.

Not established:

* whether a principal witness exists strictly inside the strip (§4.1) — this
  is the open question, deliberately not guessed at here;
* anything about complex $a$;
* any change to 108_24's own theorem, which is untouched and stands.

`ROW_A_STATUS` remains `partial`.  Nothing here bears on RH.

## 6. Verifier

`108_26_principal_line_outside_pairing_domain.py` checks: unit mass of a
point mass at $s=0$ against zero mass of a balanced profile; the exact
geometric-ratio criterion at nine grades including both endpoints, and that
the endpoint ratios equal $1$ exactly; accumulation of $\{1/N\}$ at $0$ with
singularity counts in three shrinking neighbourhoods; the existence of
interior singularities establishing independence of the two obstructions;
and that any approach to $s=0$ from inside crosses infinitely many.
