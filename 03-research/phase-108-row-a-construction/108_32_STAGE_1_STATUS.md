# 108.32 — Stage 1, terminal status after the corrected definition of principal

## 0. Terminal verdict

> **108_26 §4.1's open question — "does $\mathcal G$ admit a principal
> witness of weight strictly inside $0<s<1$?" — is resolved: YES.**
>
> The resolution is definitional, not analytic: 108_03 Definition 6.1's
> criterion for "principal" (literal, "genuine" Frobenius/chart-invariance)
> is not the correct transplant of the classical notion, and a corrected,
> classically-grounded definition (108_31 Definition 3.1) admits a nonzero
> principal witness at **every** real weight $s$, in particular at every
> $s\in(0,1)$, where 108_24 Theorem 2.1's pairing is already proved to
> exist and be zero-free.
>
> **Stage 1's identified blocker (108_26 §4.1) is closed.** One further,
> candidly flagged, mechanical step (§3 below) remains before the
> resulting testability claim is airtight end-to-end; it does not reopen
> the weight question itself.

`ROW_A_STATUS` remains `partial`. This note promotes no status beyond what
is proved below, and nothing here bears on RH.

## 1. The chain, assembled

| step | what it established | status |
|---|---|---|
| 108_24 Thm 2.1 | a forced, zero-free pairing exists on *balanced* smearing profiles in the open strip $0<a<1$ | proved (inherited) |
| 108_26 | 108_03's principal line sits at $s=0$: excluded boundary of the strip, accumulation point of the singular set — unreachable | proved (inherited) |
| 108_26 §4.1 | poses the open question: is $s=0$ forced, or does a witness exist in $(0,1)$? | open (inherited) |
| 108_27 Thm 2.1 | $\mathrm{Div}(U)$ is literally Frobenius-invariant iff $s=0$ | proved (inherited) — **stands**, unaltered |
| 108_27 §4 | proposes searching for a "logarithmic" $\mathrm{Div}$ as the fix | shown misconceived (108_28) |
| 108_28 | $\mathrm{Div}$ already satisfies every classical logarithmic-divisor law, correctly translated; $\mathrm{Div}(cU)=c\mathrm{Div}(U)$ is the *correct* power-law behaviour, not a defect | proved here |
| 108_29 (Route Beta) | the "same ray" reading of invariance holds, but for every weight unconditionally — vacuous, not discriminating | proved here (insufficient alone) |
| 108_29 (Route Gamma) | no canonical, weight-only rescaling can relocate the invariance locus of any $n$-dependent character | proved here (fails) |
| 108_31 (Route Delta) | Definition 6.1's literal-invariance criterion, applied to the classical model (a torus acting on $\mathbb P^1$), would trivialize the entire classical notion of $T$-invariant principal divisor; the correct classical criterion is semi-invariance, admitting **every** character | proved here (self-contained classical lemma, Proposition 1.1) |
| 108_31 Def 3.1 / Thm 3.2 | corrected definition; nonzero principal witnesses exist at every $s\in\mathbb R$, in particular every $s\in(0,1)$ | proved here |
| 108_31 §5 | connecting an individual weight-$s$ point-mass witness to 108_24's smooth, mean-zero pairing domain needs one further bridging step (e.g. a balanced pair $U_{s_0}-U_{s_1}$, $s_0,s_1\in(0,1)$) | **identified, not verified** — see §3 |

## 2. What was proved, what was verified numerically, what is inherited

**Proved (written proof, this batch of notes):**

* 108_28 Proposition 2.1: $\mathrm{Div}$ is additive over sums of
  potentials of different weights.
* 108_28 Proposition 3.1: the diagnostic $D_{\log}$ of 108_27 §3 is blind
  to $s$ entirely — a second, independent reason it could never have
  supplied the fix 108_27 §4 sought.
* 108_29 Proposition 2.1/2.2: the "same ray" reading (Route Beta) holds for
  every real weight unconditionally, hence carries no discriminating
  content on its own.
* 108_29 Lemma 3.2/Corollary 3.3: no canonical weight-only rescaling
  (Route Gamma) can move the invariance locus of any genuinely
  $n$-dependent character; applied to $\mathcal G$'s two natural
  characters, the loci are exactly $\{s=0\}$ and $\{s=-1\}$, neither in
  $(0,1)$.
* 108_31 Proposition 1.1/Corollary 1.2 (self-contained classical lemma):
  on $\mathbb P^1$ under a torus action, every character $m\in\mathbb Z$,
  not only $m=0$, gives a divisor that is exactly torus-invariant, despite
  the underlying function being only semi-invariant.
* 108_31 Proposition 2.1: Definition 6.1's literal criterion, applied to
  that classical model, trivializes the entire group of $T$-invariant
  principal divisors down to $\{0\}$ — confirming the literal reading is
  the wrong transplant.
* 108_31 Theorem 3.2: under the corrected Definition 3.1, nonzero principal
  witnesses exist at every $s\in\mathbb R$, in particular every
  $s\in(0,1)$.

**Verified numerically (all verifiers below, exit 0):** linearity and
additivity of $\mathrm{Div}$ across weights; positivity of
$\chi_s(m,n)$ for a wide bank of real $s$ (including large positive and
negative values); one-dimensionality of $\mathcal L_s$'s image under
$\mathrm{Div}$; exact ratio-homogeneity $u_s(r/n)=n^{-(s+1)}u_s(r)$;
invariance of $D_{\log}$'s discrepancy across weights; invariance-locus
stability of $\chi_s$ under four different candidate canonical rescalings;
exact vanishing order of $t^*\varphi_m$ at $r=0$ on the classical model,
independent of $t$; nonzero and pairwise-distinguishable
$\mathrm{div}(U_s)$ at five weights inside $(0,1)$; conservativity of
the enlarged $\mathrm{Prin}'(\mathcal G)$ against the old
$\mathrm{Prin}(\mathcal G)$.

**Read from source, not re-derived:** 107_237 (2.3) and Theorem 2.1; 108_02
Theorem 4.1; 108_03 Definitions 4.1/6.1, Propositions 3.1/5.2, Theorem 6.2;
108_04 Theorem 1.1 and (2.1); 108_24 Definition 1.1, Theorem 2.1; 108_26
Propositions 1.1/2.1/3.1; the toric divisor exact sequence
(Cox–Little–Schenck, cited for context only — the case actually used is
proved from scratch in 108_31).

## 3. The one candidly remaining item

108_31 §5 identifies, but does not check, a bridging step: 108_24's pairing
domain is *smooth, compactly supported, mean-zero* profiles on $(0,1)$
(108_24 Definition 1.1), while a single principal witness $U_s$ corresponds
to a point mass at $a=s$ — not smooth, and of mass $1$, not $0$ (108_26
Proposition 1.1). The natural fix — pairing a **difference** of two
in-strip witnesses, $U_{s_0}-U_{s_1}$ with $s_0,s_1\in(0,1)$, which is
balanced by construction and lies in the linear span of
$\mathrm{Prin}'(\mathcal G)$ (108_28's additivity) — is sketched but
not verified: whether smooth balanced approximations to this discrete
combination have a convergent pairing value is exactly the sort of
question 108_22 (extension by continuity) and 108_23 (the smeared-pairing
convergence dichotomy) were built to answer for a related but different
object ($f_a$ itself). Neither document was read while producing 108_28,
108_29, or 108_31 (per those notes' scope instructions), so this note does
not certify the bridge — it names it as the concrete next step.

This gap concerns *how* to feed a resolved-weight witness into 108_24's
existing pairing, not *whether* a resolved-weight witness exists — the
question 108_26 §4.1 actually posed, and the one this batch of notes
answers.

## 4. Updated status table (supersedes 108_21 §4, 108_26 §4, for the items below)

| object | location | status |
|---|---|---|
| pairing on individual $f_a$ | — | impossible (108_22, inherited) |
| pairing on balanced, smooth, compactly supported profiles | $0<a<1$ | exists, proved (108_24, inherited) |
| $\mathrm{Prin}(\mathcal G)$, literal-invariance reading (108_03 Def 6.1) | $s=0$ only | excluded and unreachable (108_26, inherited) — **superseded as the definition of "principal"** |
| $\mathrm{Prin}'(\mathcal G)$, semi-invariance reading (108_31 Def 3.1) | every $s\in\mathbb R$ | nonzero witnesses exist throughout, including $(0,1)$ (108_31, this batch) |
| bridging a weight-$s$ witness into 108_24's smooth mean-zero domain | — | identified, not checked (108_31 §5, this batch) |
| Stage 1's blocking question (108_26 §4.1) | — | **resolved: yes** |

## 5. Scope

Proved here: the assembled chain of §1–§2, drawing on 108_28, 108_29,
108_31 (this batch).

Not established, and explicitly not claimed:

* that the bridging step of §3 succeeds — it is not attempted here;
* that principal invariance (108_04 (2.1)) actually *holds* for any
  witness — Stage 1's mandate, per 108_26 §4, was to make the question
  testable, not to evaluate the test; nothing here evaluates it;
* anything about complex $s$;
* any relation between this note and $\xi$, its zeros, Li's coefficients,
  or RH. None is used, and none follows from anything here.

`ROW_A_STATUS` remains `partial`.

## 6. Verifier

`108_32_stage_1_status.py` performs a lightweight, self-contained
cross-check (not a re-derivation) of the load-bearing numeric facts from
108_28/108_29/108_31: additivity of $\mathrm{Div}$; positivity of
$\chi_s(m,n)$ on a wide weight bank; the two invariance loci $\{s=0\}$,
$\{s=-1\}$; nonzero, pairwise-distinguishable $\mathrm{div}(U_s)$ at
five weights in $(0,1)$; and conservativity of $\mathrm{Prin}'$
against $\mathrm{Prin}$. It prints the assembled status table and a
final verdict line.
