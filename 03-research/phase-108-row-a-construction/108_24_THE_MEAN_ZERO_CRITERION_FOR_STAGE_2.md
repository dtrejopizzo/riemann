# 108.24 — The mean-zero criterion: testing principal invariance without a
# globally defined number-valued pairing on the graded family

## 0. The question and the deliverable

107_240 Theorem C proved the local principal subspace is $\{0\}$, forcing
principal invariance to be posed globally; 108_03/108_04 built the graded
divisor group carrying that global structure
(`GLOBAL_PRINCIPAL_SUBSPACE_NONZERO: YES`, read from source, not re-derived
here). What that construction has always lacked is a pairing: 108_22 proves
none exists pointwise on individual graded elements $f_a$, and 108_23 proves
the naive zero-sourced repair (smearing with an arbitrary profile) is not a
legitimate definition and, on the arithmetic side, diverges for generic
profiles anyway.

\[
 \boxed{\text{Principal invariance }\textit{can}\text{ be tested without a
 globally defined number-valued pairing on all of }\mathcal G\text{: restrict
 to }\textbf{mean-zero}\text{ smearing profiles (§1). On that subspace a
 genuine, forced, zero-free pairing }\Lambda_g^0\text{ exists (Theorem 2.1),
 by an EXACT cancellation of 108\_21's divergent constant that holds at
 every finite regularization depth, not merely in a limit. §3 states the
 usable criterion this gives Stage 2, and §5 states, without softening,
 exactly what it does and does not certify.}}
\]

No zero of $\xi$ enters any definition below. `ROW_A_STATUS` remains
`partial`.

## 1. Balanced profiles, and why they are the natural test directions

> ### Definition 1.1 (balanced profile)
> A smooth, compactly supported $\varphi:(0,1)\to\mathbb C$ is **balanced**
> if $\int_0^1\varphi(a)\,da=0$.

> ### Remark 1.2 (why this is the natural reading of a principal test
>   direction — flagged, not verified against 108_03/108_04's literal
>   definitions)
> Classically, the divisor of a rational function has degree $0$: principal
> divisors are, by their very construction, the degree-zero elements of a
> divisor group. If the grade $a$ plays the role of degree in 108_03/108_04's
> graded divisor group — a reading suggested by the name "graded divisor
> group" and by nothing else examined in this note, since 108_03/108_04 are
> not read here beyond the one status line quoted above — then principal
> elements of that group are exactly the ones expressible as balanced
> (mean-zero) combinations or profiles in $a$. This is recorded as a working
> hypothesis for §3's criterion, explicitly not confirmed against 108_03's
> or 108_04's actual construction. It is also exactly the mission's own
> suggested strategy "test it on differences only": a difference of two
> graded elements, or more generally a virtual combination with total mass
> zero, is a balanced profile in the sense of Definition 1.1.

> ### Remark 1.3 (this is not the previously-refuted combination trick)
> 108_19 §3 records that a **finite** combination $\sum_i\lambda_if_{a_i}$
> with $\sum_i\lambda_i=0$, aimed at forcing $\sum_i\lambda_ic_g(a_i)=0$ for
> *every* $g$, is vacuous: Mellin/Fourier injectivity forces every
> $\lambda_i=0$ once the vanishing is demanded for all $g$ simultaneously.
> That trick targets the **$a$-dependent** piece and tries to annihilate it
> entirely. Definition 1.1's balanced profiles target something different:
> not the $a$-dependent piece (which is left alone, and is generically
> nonzero — that is the point, §4), but the **$a$-independent** divergent
> constant identified in 108_21 Theorem 1.1(b). Because that constant's
> coefficient does not vary with $a$, killing its contribution needs only
> $\int\varphi\,da=0$ — a single linear condition, imposed once, not a
> demand that forces every coefficient to vanish. The two mechanisms are
> different, and Remark 1.3 makes the difference explicit so the criterion
> below is not mistaken for a repeat of an already-refuted idea.

## 2. The pairing exists on balanced profiles, exactly

> ### Theorem 2.1 (the mean-zero pairing)
> For every admissible $g$ and every balanced $\varphi$ (Def. 1.1), the
> limit
> \[
>  \Lambda_g^0(\varphi):=\lim_{T\to\infty}\int_0^1\varphi(a)\,
>  \Lambda_g(f_{a,T})\,da
> \]
> exists (is finite), equals $\int_0^1\varphi(a)\,L_g(a)\,da$ where
> $L_g(a):=\lim_{T\to\infty}L_g(a,T)$ is 108_11's already-closed, $a$-dependent
> distributional object (cited, not re-derived), and this equality holds
> with the divergent constant of 108_21 contributing **exactly zero at every
> finite $T$**, not merely in the limit.

**Proof.** By 108_21 Theorem 1.1(a)-(b) (cited, exactly as used in 108_22
Theorem 3.1 and 108_23 §3), for every $a\in\mathbb C$ in the graded family
the divergent part of $\Lambda_g(f_{a,T})$ as $T\to\infty$ has coefficient
$\varphi_0=f_a(1)=1$, independent of $a$. Writing
$\Lambda_g(f_{a,T})=D(T)+L_g(a,T)$ with $D(T)$ the $a$-independent divergent
piece and $L_g(a,T)$ the $a$-dependent piece assembled in 108_11 (cited),
\[
 \int_0^1\varphi(a)\,\Lambda_g(f_{a,T})\,da
 = D(T)\underbrace{\int_0^1\varphi(a)\,da}_{=0\text{ by Def. 1.1}}
 \;+\;\int_0^1\varphi(a)\,L_g(a,T)\,da
 = \int_0^1\varphi(a)\,L_g(a,T)\,da
\]
identically, for every $T$, however large or divergent $D(T)$ is — this uses
nothing about $D(T)$'s value, only that it does not depend on $a$ and that
$\int\varphi=0$. Since 108_11 establishes $L_g(a,T)\to L_g(a)$ (cited,
"global, $a$-dependent part, distributional | closed"), and $\varphi$ is
fixed, smooth, and compactly supported, $\int\varphi(a)L_g(a,T)\,da\to
\int\varphi(a)L_g(a)\,da$ as $T\to\infty$ (dominated convergence on a
compact interval, given 108_11's closure supplies a $T$-uniform bound —
inherited, not separately proved here). $\square$

This is the precise sense in which reading (i) of 108_23 Definition 1.1 is
**recovered**, but only on the balanced subspace: $\Lambda_g^0$ is a forced,
zero-free, density-and-continuity consequence of $\Lambda_g$ — no zero of
$\xi$ enters its construction — restricted to the test directions on which
the argument above actually closes.

## 3. The criterion

> ### Criterion 3.1 (mean-zero invariance test, for Stage 2)
> Let $\pi$ be a candidate principal element of 108_03/108_04's graded
> divisor group, represented (Remark 1.2) by a balanced profile $\varphi_\pi$
> on $(0,1)$. For a fixed admissible test function $g$:
> * if $\Lambda_g^0(\varphi_\pi)=0$, the pairing **does not detect**
>   non-invariance of $\pi$ against $g$;
> * if $\Lambda_g^0(\varphi_\pi)\ne0$ for some admissible $g$, $\pi$ is
>   **certified non-invariant** in the mean-zero-pairing sense: an explicit,
>   finite, zero-free-computed number witnesses the failure.
> Both cases are computed entirely from $L_g$ (108_11, cited) via Theorem
> 2.1; the divergent constant $\sum_pC_p$ of 108_21 is never evaluated,
> estimated, or assumed finite — it is cancelled exactly, by construction,
> before any number is computed.

§6 exhibits this operating on a concrete illustrative model: one balanced
$\varphi$ constructed (by an exact symmetry, not a numerical coincidence) to
pair to zero against a model $L_g$, and one constructed to pair to a
nonzero, explicitly computed value.

## 4. Corroboration: this is not a new, ad hoc functional

108_19 built, for its own (different) purpose — testing whether the
constant's contribution lies in the radical of $I_\partial$ — the functional
$\Phi(g,\varphi):=\int_0^1\varphi(a)c_g(a)\,da$ ($c_g$ from 108_06 Prop 2.1,
entire in $a$), and proved (108_19 Theorem 2.1, cited) $\Phi\not\equiv0$: an
explicit witness pair $(g,\varphi)$ with $\varphi$ a bump on $[0.3,0.7]$
gives $\Phi\ne0$.

$\Phi$ and $\Lambda_g^0$ are built the same way — "smear the closed,
$a$-dependent piece of the assembled pairing against a compactly supported
profile" — and 108_19's witness bump has $\int\varphi\,da\ne0$ in general
(it is not asserted there to be balanced), so $\Phi$ and $\Lambda_g^0$ are
not shown identical here. What 108_19 Theorem 2.1 does supply, without
further work, is independent evidence that objects of exactly this shape are
**non-degenerate**: the $a$-dependent piece $c_g$ (plausibly the same object
as, or built from the same source as, 108_11's $L_g$ — not verified here,
108_06 and 108_11 are not read in this note) is not identically zero on any
open subinterval of $(0,1)$, for any $g\ne0$. That non-degeneracy is exactly
what makes Criterion 3.1 non-vacuous: it is not testing a pairing that is
secretly zero on everything by construction. If the identification
$L_g\leftrightarrow c_g$ holds, 108_19's own witness could likely be
re-purposed (after subtracting its mean to enforce Definition 1.1) into an
explicit non-invariance witness for Criterion 3.1; this note does not carry
that out and flags it, candidly, as unverified rather than claiming it.

## 5. What this criterion does and does not certify

**Certifies:**

* a finite, computable, zero-free-*defined* number $\Lambda_g^0(\varphi_\pi)$
  for every balanced $\varphi_\pi$ and admissible $g$ (Theorem 2.1);
* an operational test distinguishing "no detected non-invariance" from
  "certified non-invariant," usable by Stage 2 without ever evaluating,
  bounding, or regularizing $\sum_pC_p$;
* that the test is non-vacuous in structure, by analogy/likely identity
  (§4, flagged) with 108_19's already-proved nonvanishing witness.

**Does not certify:**

* anything about individual, non-smeared graded elements $f_a$ — 108_22's
  negative result stands unchanged; there is still no pointwise pairing;
* anything about non-balanced profiles or about elements of the graded
  divisor group not expressible (even approximately) as balanced profiles
  — if 108_03/108_04's principal subspace contains such elements, this
  criterion is silent on them, and Remark 1.2's structural reading is not
  checked against those notes' literal definitions;
* any value, finiteness, or vanishing of $\sum_pC_p$ or of the unsmeared
  constant's contribution — 108_21's terminal verdict on that question is
  untouched and is not reopened by anything here;
* that "$\Lambda_g^0(\varphi_\pi)=0$ for every $g$" is *sufficient* for
  whatever precise technical notion of principal invariance 107_240 and
  108_03/108_04 intend — only that it is a natural necessary-looking
  consistency check; sufficiency is not addressed;
* the identification $L_g\leftrightarrow c_g$ of §4, which is flagged, not
  proved;
* the alternative route the mission also names — testing after passing to
  107_240 §5's numerical quotient, where 108_19 §4 records (quoting 108_00
  §3) that a pairing exists unconditionally. This note does not attempt to
  relate $\Lambda_g^0$ to that quotient's pairing; whether they coincide,
  refine one another, or are independent is open;
* anything about RH. `ROW_A_STATUS` remains `partial`.

## 6. Scope

**Proved here:**

* Theorem 2.1: the mean-zero pairing $\Lambda_g^0$ exists on balanced
  profiles, with the divergent constant cancelling exactly at every finite
  regularization depth (an identity, not an asymptotic approximation);
* Criterion 3.1: the explicit, usable test for Stage 2;
* Remark 1.3: this is a structurally different mechanism from the
  already-refuted finite-combination trick of 108_19 §3, not a repeat of it.

**Read from source, cited, not re-derived:**

* 107_240 Theorem C (local principal subspace $\{0\}$) and the
  `GLOBAL_PRINCIPAL_SUBSPACE_NONZERO: YES` flag from 108_03/108_04, quoted
  from the mission statement, not re-derived or independently checked here;
* 108_21 Theorem 1.1(a)-(b);
* 108_11's closure of the $a$-dependent distributional object;
* 108_19 Theorem 2.1 (the nonvanishing witness for $\Phi$).

**Not established, and explicitly not claimed:**

* Remark 1.2's identification of "balanced profile" with "principal
  element," against 108_03/108_04's actual definitions;
* §4's identification $L_g\leftrightarrow c_g$;
* sufficiency (as opposed to necessity) of Criterion 3.1 for the intended
  notion of principal invariance;
* any relation to 107_240 §5's numerical quotient;
* anything about $\sum_pC_p$'s value or about RH.

## 7. Verifier

`108_24_the_mean_zero_criterion_for_stage_2.py` checks: (A) the exact
cancellation identity of Theorem 2.1 on a concrete illustrative model
($D(T)=\log T$, unbounded; a model entire $L_g(a)$), reused independently
from 108_23's model with a different, symmetric $L_g$ chosen specifically to
support an exact-zero witness; (B) Criterion 3.1 operating on two explicit
balanced profiles: one constructed by an odd-symmetry argument to pair to
exactly $0$ against the model $L_g$ (the "not detected" case), and one
constructed to pair to a nonzero, explicitly computed value (the "certified
non-invariant" case) — both computed as genuine $T\to\infty$ limits of the
arithmetic-side smeared quantity, confirmed against the closed-form
$\int\varphi L_g\,da$; (C) that a non-balanced control profile applied to the
same model diverges as $T\to\infty$, confirming the balanced restriction is
load-bearing, not cosmetic.
