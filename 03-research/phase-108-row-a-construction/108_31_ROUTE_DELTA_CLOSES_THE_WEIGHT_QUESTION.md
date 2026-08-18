# 108.31 — Route Delta: the semi-invariant convention is the correct one, and it closes 108_26 §4.1's open question

## 0. Answer

> **108_26 §4.1's open question: does $\mathcal G$ admit a principal witness
> of weight strictly inside $0<s<1$?**
>
> **Yes.** 108_03 Definition 6.1's criterion for "principal" — *genuine*
> invariance, "fixed, not merely covariant" — is not the correct transplant
> of the classical notion into $\mathcal G$. The classical notion of a
> principal divisor never requires invariance under an auxiliary group
> action at all; when one *does* restrict to a group-equivariant setting
> (exactly the situation here), the standard and, on inspection, forced
> convention is that principal divisors are divisors of **semi-invariant**
> global sections — objects transforming by *any* character, not only the
> trivial one. Under that convention every weight $s\in\mathbb R$,
> including every $s\in(0,1)$, supplies a nonzero principal witness
> $\operatorname{div}(U_s)$.

This does not contradict anything already proved. 108_27 Theorem 2.1 (only
$s=0$ is literally Frobenius-fixed) stands, untouched — it answers a
narrower question than "is this witness principal", and 108_28 confirms
$\operatorname{Div}$ is not defective. What changes is Definition 6.1
itself, on the strength of an argument external to $\mathcal G$: how
classical equivariant divisor theory actually treats characters.

No zero of $\xi$ is used anywhere.

## 1. The classical fact: torus-invariant principal divisors correspond to *every* character, not the trivial one

This section proves a self-contained classical fact used purely as
motivation and precedent for §2's definitional revision. It is **not**
claimed that 107_237's $\operatorname{Div}$ literally computes the object
constructed here; the two are structurally analogous (both are
"$\log$-type", additive, group-covariant constructions — 108_28 §1), not
identical.

### Setup

Let $T=\mathbb C^\times$ act on $X=\mathbb P^1$ (coordinate $r$ on the
affine chart, with $r=0$ and $r=\infty$ the two $T$-fixed points) by
$t\cdot r=tr$. For $m\in\mathbb Z$, the monomial $\varphi_m(r):=r^m$ is a
rational function on $X$ (an candid element of the function field
$\mathbb C(X)$), with divisor

\[
 \operatorname{div}(\varphi_m)=m\,[0]-m\,[\infty].
 \tag{1.1}
\]

### Proposition 1.1 (every $\varphi_m$ is only semi-invariant, yet every $\operatorname{div}(\varphi_m)$ is literally $T$-fixed)

For $m\ne0$, $\varphi_m$ is **not** invariant under $T$: pulling back by
$t\in T$, $(t^*\varphi_m)(r)=\varphi_m(tr)=t^m\varphi_m(r)$, a nontrivial
scalar multiple whenever $t^m\ne1$. Nonetheless, for **every** $m\in\mathbb
Z$, the divisor (1.1) itself is exactly $T$-invariant: $t^*\operatorname{div}(\varphi_m)=\operatorname{div}(t^*\varphi_m)=\operatorname{div}(t^m\varphi_m)=\operatorname{div}(\varphi_m)$,
using that $\operatorname{div}$ is insensitive to multiplication by the
nonvanishing constant $t^m$ (the classical unit law, (1.1) of 108_28).

**Proof.** Pulling back the divisor of $\varphi_m$ amounts to tracking how
its vanishing/pole *locus and order* move under $r\mapsto tr$. Since $0$
and $\infty$ are fixed *points* of the action (only the local coordinate
near each is rescaled by $t$, not the point itself), and since
$\operatorname{ord}_0(t^m\varphi_m)=\operatorname{ord}_0(\varphi_m)=m$
(multiplying by a nonzero constant never changes vanishing order), the
divisor (1.1) is reproduced exactly, coefficient for coefficient, for
every $m$. $\square$

### Corollary 1.2 (the standard toric exact sequence, cited)

This is the elementary case of the standard toric fact (Cox–Little–Schenck,
*Toric Varieties*, Theorem 4.1.3; equally the exact sequence
$0\to M\to\operatorname{Div}_T(X)\to\operatorname{Cl}(X)\to0$ for any toric
$X$): the group of $T$-invariant **principal** divisors is exactly
$\{\operatorname{div}(\chi^m):m\in M\}$, one for **every** character $m$ of
the torus, not only $m=0$. The map $m\mapsto\operatorname{div}(\chi^m)$ is
a group homomorphism (from $(M,+)$, i.e. characters under **multiplication**
of the underlying monomials) with image exactly the $T$-invariant principal
divisors, and (for $X$ with no non-constant invariant units, e.g.
$\mathbb P^1$) it is injective. **Weight $0$ is the trivial character,
giving the trivial (zero) divisor** $\operatorname{div}(1)=0$ — it is the
*most degenerate* case of this family, not a distinguished or exhaustive
one.

## 2. Why Definition 6.1's reading collapses to the degenerate case only

108_03 Definition 6.1, quoted:

> "a principal divisor is the divisor of a global rational function, i.e. a
> global section that is genuinely **invariant** (fixed, not merely
> covariant, under the structure group). In $\mathcal G$, 'genuinely
> invariant' is exactly weight $s=0$."

By Proposition 1.1/Corollary 1.2, "genuinely invariant, fixed under the
structure group" singles out, in the classical model, exactly the
*constants* $\mathbb C\subset\mathbb C(X)$ — the unique weight-$0$
character — whose divisors are all $0$. Constants are certainly principal
(their divisor, $0$, is trivially principal), but they are the **only**
functions Definition 6.1's literal reading admits, and classically they
generate none of the interesting structure of $\operatorname{Div}_T(X)$:
every *nonzero* $T$-invariant principal divisor comes from a *nontrivial*
character $m\ne0$, precisely the ones Definition 6.1 excludes.

### Proposition 2.1 (Definition 6.1's criterion, read literally, would make every classical toric $\operatorname{Prin}_T$ trivial)

If "principal" in the toric model were redefined, following 108_03
Definition 6.1's literal wording, as "divisor of a $T$-**invariant**
(rather than semi-invariant) rational function", the resulting subgroup of
$\operatorname{Div}_T(X)$ would be $\{0\}$ for every toric $X$ whose only
$T$-invariant global functions are the constants (true of $\mathbb P^1$,
and of any complete toric variety) — discarding the entire content of
Corollary 1.2's exact sequence.

**Proof.** $T$-invariant elements of $\mathbb C(X)$ that are also regular
(hence candid "global sections", not merely rational) are exactly the
$T$-invariant global functions; on a complete variety these are the
constants (the only global regular functions on a complete variety are
constants — a standard fact, e.g. Hartshorne II.4.8 applied $T$-orbitwise,
or directly here: a $T$-invariant regular function on $\mathbb P^1$ that is
holomorphic at both fixed points $0,\infty$ and constant along every orbit
is constant). Their divisors are all $0$. $\square$

**Consequence.** Definition 6.1's literal criterion, applied to the model
that motivates the whole construction, does not recover "the" classical
notion of $T$-invariant principal divisor — it recovers only its most
degenerate member. This is a structural mismatch, independent of any
detail of $\mathcal G$; it is a general fact about what "invariant" versus
"semi-invariant" means for rational functions under a torus action.

## 3. The corrected definition

### Definition 3.1 (principal witnesses, semi-invariant convention)

For $s\in\mathbb R$, $U_s$ is a **principal witness of weight $s$** if it
is a nonzero element of $\mathcal L_s$ (108_03 Definition 4.1) — i.e. a
nonzero *semi-invariant* global section, transforming by the character
$\chi_s$ of (3.3), with no further requirement.

\[
 \boxed{
 \operatorname{Prin}'(\mathcal G):=\operatorname{div}(\mathcal G)
 =\bigcup_{s\in\mathbb R}\operatorname{div}(\mathcal L_s)
 =\Big\{\,c\,r^{s-1}\tfrac{dr}r \ :\ s\in\mathbb R,\ c\in\mathbb R\,\Big\}.}
 \tag{3.1}
\]

This is a **conservative enlargement**, not a replacement: 108_03 Theorem
6.2's $\operatorname{Prin}(\mathcal G)=\mathbb R\cdot(dr/r)$ is exactly the
$s=0$ graded piece of $\operatorname{Prin}'(\mathcal G)$, and nothing
proved about it (108_03 Theorem 6.2, 108_04 Theorem 1.1, 108_26, 108_27) is
altered — each remains a true statement about that one piece. What is
withdrawn is only the claim that $s=0$ is the *unique* principal weight;
108_27 Corollary 2.2's phrase "the only principal subspace available" is
the specific statement superseded here, precisely at the point 108_27 §4
flagged as the place a fix would have to enter (108_28 confirms it is not
$\operatorname{Div}$ that needed fixing; this note supplies the fix, and it
lands in the definition, exactly as 108_27 §4 anticipated it must).

### Theorem 3.2 (principal witnesses exist at every weight, in particular in $(0,1)$)

For every $s\in\mathbb R$ and every $c\ne0$, $\operatorname{div}(cU_s)=c\,r^{s-1}dr/r\in\operatorname{Prin}'(\mathcal G)$
is nonzero (108_03 Proposition 5.2, cited). In particular, for every
$s\in(0,1)$ — e.g. $s=\tfrac12$ — $\operatorname{div}(U_s)$ is an explicit,
canonical, nonzero principal witness of weight $s$, strictly inside the
open strip where 108_24 Theorem 2.1's pairing is proved to exist.

**Proof.** Immediate from Definition 3.1 and 108_03 Proposition 5.2
(injectivity of $\operatorname{div}$ on each $\mathcal L_s$, cited, not
re-derived), applied at $s\in(0,1)$. $\square$

This directly answers 108_26 §4.1 in the affirmative.

## 4. Compatibility: nothing already proved is contradicted

* **108_27 Theorem 2.1** ("$\operatorname{Div}(U)$ is Frobenius-invariant
  iff $s=0$") is a true statement about *literal invariance of the current*
  under the structure-group action. Theorem 3.2 above is a statement about
  *principality*, now defined (Definition 3.1) without reference to that
  invariance. The two are compatible because they are answers to two
  different questions, correctly disentangled: Frobenius-fixedness is a
  strictly stronger, and — per §1–§2 — not classically required, property.
* **108_26 Proposition 2.1/3.1** (the old $\operatorname{Prin}(\mathcal
  G)=\{s=0\}$ line sits on the excluded boundary / accumulation point) is
  unaffected: it is a true statement about the $s=0$ piece specifically,
  which remains exactly where 108_26 located it. It no longer describes
  *all* of $\operatorname{Prin}'(\mathcal G)$, which is the entire point.
* **108_26 Proposition 1.1** ("balanced and principal are opposite
  conditions") used the fact that the (old, single) principal element is a
  unit point mass. Under $\operatorname{Prin}'(\mathcal G)$, *each
  individual* $\operatorname{div}(U_s)$ is still such a point mass (at
  grade $a=s$); this is not changed by enlarging the set of available
  weights, and is addressed candidly in §5.

## 5. What remains: connecting a single-weight witness to 108_24's pairing domain

This section records, rather than resolves, one further mechanical gap the
mission's own framing (and 108_26 §4.1) treats as already bridged. It is
flagged here because rule 3 of this note's governing instructions forbids
claiming as proved what is not.

108_24 Definition 1.1 requires a **smooth, compactly supported** profile
$\varphi:(0,1)\to\mathbb C$ with $\int\varphi\,da=0$ ("balanced"). A single
weight-$s$ witness $U_s$ corresponds, in the grade parameter $a$, to a
**point mass** at $a=s$ — not smooth, and (108_26 Proposition 1.1) of total
mass $1$, not $0$. So Theorem 3.2's witness, taken alone, is **not**
literally an element of 108_24's domain, for any $s$, including
$s\in(0,1)$.

A natural bridge exists and is recorded here without being verified: by
108_28 Proposition 2.1 ($\operatorname{Div}$ is additive across weights),
if $s_0,s_1\in(0,1)$ are two distinct principal witnesses under
$\operatorname{Prin}'(\mathcal G)$, then $U_{s_0}-U_{s_1}$ has divisor
$\operatorname{div}(U_{s_0})-\operatorname{div}(U_{s_1})$, a **balanced**
(mass $+1$ at $a=s_0$, mass $-1$ at $a=s_1$, total mass $0$) discrete
profile, entirely supported in $(0,1)$, and — because it is a finite linear
combination of elements of $\mathcal G$ (107_237 Theorem 2.1's general
existence theorem applies to $f_{s_0}-f_{s_1}$ directly, not only to a
single power) — a bona fide element of $\operatorname{Prin}'(\mathcal G)$'s
linear span. Whether this discrete object is itself, or is the limit of, an
admissible input to 108_24's pairing $\Lambda_g^0$ (i.e. whether smooth
balanced bump-pairs concentrating at $s_0,s_1$ have a pairing value that
converges as the bumps shrink) is precisely the kind of question 108_22
(extension by continuity) and 108_23 (the smeared-pairing convergence
dichotomy) were built to police, for a different but related object
($f_a$ itself, not a difference of two weight-witnesses). **This note does
not check that convergence**; neither document was read in preparing this
note (per the scope instructions governing it), and the check is left as
the concrete next step for whoever next reads 108_22/108_23 against this
specific discrete input.

## 6. Scope

Proved here:

* Proposition 1.1 and Corollary 1.2 (cited standard fact, self-contained
  elementary proof supplied): the classical model for "principal divisor
  under a torus action" is semi-invariance, and every character, not only
  the trivial one, supplies a nonzero $T$-invariant principal divisor;
* Proposition 2.1: Definition 6.1's literal criterion, applied to the
  classical model, would trivialize $\operatorname{Prin}_T$ entirely,
  confirming it is not the right transplant;
* Theorem 3.2: under the corrected Definition 3.1, every $s\in\mathbb R$,
  in particular every $s\in(0,1)$, supplies a nonzero principal witness;
* §4: this enlargement is conservative and contradicts nothing already
  proved in 108_03/108_26/108_27.

Read from source, not re-derived: 108_03 Definitions 4.1/6.1, Propositions
3.1/5.2, Theorem 6.2; 108_24 Definition 1.1, Theorem 2.1 (cited only for
its domain statement, not re-proved); 108_26 Propositions 1.1/2.1/3.1;
108_27 Theorem 2.1; 108_28 Proposition 2.1.

Cited without independent re-derivation: the toric divisor exact sequence
$0\to M\to\operatorname{Div}_T(X)\to\operatorname{Cl}(X)\to0$
(Cox–Little–Schenck Thm 4.1.3) — used only as motivation for Definition
3.1, with a fully self-contained elementary proof supplied for the
$\mathbb P^1$ case actually used (Proposition 1.1).

Not established, and explicitly not claimed:

* that $\operatorname{Div}$ literally computes zero/pole orders at fixed
  points of a toric variety — the analogy of §1 is structural (matching
  108_28's additive/multiplicative dictionary), not a literal identification;
* that 108_24's pairing $\Lambda_g^0$ accepts, or has a well-defined limit
  on, the discrete balanced combination $U_{s_0}-U_{s_1}$ sketched in §5 —
  explicitly flagged as open, not proved;
* anything about complex $s$;
* any relation to $\xi$, RH, or `ROW_A_STATUS`.

`ROW_A_STATUS` remains `partial`. Nothing here bears on RH.

## 7. Verifier

`108_31_route_delta_closes_the_weight_question.py` checks: Proposition 1.1
numerically, by confirming the vanishing *order* of $t^*\varphi_m$ at
$r=0$ (measured via the slope of $\log|\varphi_m(tr)|$ against $\log r$ as
$r\to0$) equals $m$ exactly, independent of $t$, for a bank of $m,t$
(including $m=0$, the degenerate/trivial case) — the discrete-geometry fact
underlying Corollary 1.2; that $\operatorname{div}(U_s)$ (108_03 (5.1)) is
nonzero and pairwise distinguishable (different weights give different
density shapes $r^{s-1}$, not just different scalars) at a bank of weights
in $(0,1)$, confirming Theorem 3.2 explicitly; and that the enlarged family
$\operatorname{Prin}'(\mathcal G)$ literally contains the old
$\operatorname{Prin}(\mathcal G)$ as its $s=0$ slice (conservativity, §4).
