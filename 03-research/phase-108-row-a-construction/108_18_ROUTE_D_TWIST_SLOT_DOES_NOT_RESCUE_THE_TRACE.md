# 108.18 — Route D (the twist slot): a well-defined alternative exists, but
# it is a different object, and it does not rescue $\mathfrak T_S(f_a)$

## 0. Result

Route D asks whether the descent classification (108_02) forces the graded
family into Tate's *twist* slot (the free complex variable $s$ of a local
zeta integral $Z(h,s)$) rather than into the *test* slot (the argument $h$
itself), and whether assembling through the twist slot avoids ever summing
a divergent constant.

> **The twist-slot construction exists, is completely standard, and is
> finite with no leftover constant at every place (Theorem 2.1–2.2). But it
> is provably a different object from $\mathfrak T_S(f_a\star\tilde g)$, not
> a repair of it (Theorem 3.1–3.2): it discards exactly the singular kernel
> $1/|1-u|_v$ that gives $\mathfrak T_S$ its defining property
> $\mathfrak T_S(h)=N(h)$ (108_06 §1). Route D therefore fails to dispose of
> the constant in the construction Stage 1 actually uses — but it explains,
> independently of 108_17, exactly why: the divergence is intrinsic to
> pairing an identity-valued object with a kernel singular exactly at the
> identity (108_17 Theorem 3.1), and removing that kernel is the only way
> to avoid it, at the cost of the object's meaning.**

No zero of $\xi$ is used anywhere. `ROW_A_STATUS` remains `partial`.

## 1. What the descent classification actually forces

108_02 Theorem 4.1 (cited, proved there) forces $f=c\,r^s$ — the *only*
repair of Frobenius covariance — and 108_02 §6 states the structural
reading explicitly: descent forces $f$ to be "promoted to a Mellin kernel
graded by $s$," not to an ordinary test function. Independently, 108_05
Proposition 2.1 (cited, proved there) shows $f_a$ has **no Mellin
transform**: $\int_0^\infty x^{-a}x^s\,\frac{dx}x$ converges for no
$s\in\mathbb C$.

These two facts, read together, say the same thing from two directions:

* 108_02 says $f_a$ *is* the Mellin-dual kernel, i.e. it belongs on the
  spectral (twist) side of a Mellin pairing;
* 108_05 says $f_a$ *cannot itself* be Mellin-transformed, i.e. it cannot
  play the role of an ordinary test function whose Mellin transform
  $\hat h(0),\hat h(1),\hat h(\rho)$ the defining identity
  $\mathfrak T_S(h)=N(h)$ (108_06 §1, 107_239 (2.1)) requires to exist.

So substituting $h:=f_a$ directly into $\mathfrak T_S(h)$ is, from the
outset, an extension of the identity $\mathfrak T_S(h)=N(h)$ **beyond the
regime in which both sides are simultaneously defined** — $N(f_a)$ does not
literally make sense either, since $\hat f_a$ does not exist. 108_06 Prop
2.1 already uses $f_a$ correctly, in the *only* role 108_02/108_05 license:
as the kernel that extracts a Mellin coefficient of the genuine test
function $g$,
\[
 f_a\star\tilde g=c_g(a)f_a,\qquad c_g(a)=\int_0^\infty t^{-a}\overline{g(t)}\,d^\times t,
\]
i.e. $a$ indexes a *coefficient of $g$*, not an argument fed to $\mathfrak
T_S$ in place of $g$ itself.

## 2. The standard twist-slot alternative

> ### Definition 2.1 (Tate local zeta integral)
> For $g$ Schwartz–Bruhat on $\mathbb Q_p$ (locally constant, compactly
> supported) and $s\in\mathbb C$,
> \[
>  Z_p(g,s):=\int_{\mathbb Q_p^\times}g(u)\,|u|_p^{s}\,d^\times u .
> \]

This is the classical object of Tate's thesis (read from source /
classical; not re-derived here beyond the elementary computation below).
Unlike $W_p(h)$, its kernel is $|u|_p^s$ alone — **no factor
$1/|1-u|_p$, hence no singularity at $u=1$, hence no principal value is ever
needed.**

> ### Theorem 2.2 (the unramified local factor, elementary)
> For $g=\mathbf 1_{\mathbb Z_p}$,
> \[
>  Z_p(\mathbf 1_{\mathbb Z_p},s)=\sum_{n\ge0}p^{-ns}=\frac1{1-p^{-s}}=\zeta_p(s),
>  \qquad \Re s>0,
> \]
> continued meromorphically to $\mathbb C\setminus\{2\pi i k/\log p\}$; and
> for $g$ compactly supported **away from $0$** (finitely many nonzero
> shells), $Z_p(g,s)$ is a finite Laurent sum in $p^{-s}$, hence **entire**
> in $s$ — no pole at all.

**Proof.** $\mathbf 1_{\mathbb Z_p}$ is the indicator of shells $n\ge0$
(measure $1$ each in $d^\times u$ after the usual convention on $\mathbb
Z_p^\times$-cosets), each contributing $p^{-ns}$; sum the geometric series.
For finitely supported $g$ the sum is finite by definition, hence entire.
$\square$

Verified numerically: the truncated geometric series matches $1/(1-p^{-s})$
to machine precision, for several $p$ and several $s$ in $\Re s>0$.

> ### Corollary 2.3 (global assembly, classical)
> \[
>  \prod_p Z_p(\mathbf1_{\mathbb Z_p},s)=\prod_p\frac1{1-p^{-s}}=\zeta(s),
>  \qquad\Re s>1,
> \]
> convergent as a genuine infinite product (Euler product), continued
> meromorphically thereafter — **exactly** the contrast the mission
> statement records: local *factors* $\to1$ multiply to a convergent
> product, unlike local *terms* $\to1$ summing to $\pi(x)$-type divergence.

This confirms the numerics already present throughout 108_06–108_16: the
$C_p$-type divergence is a phenomenon of **summing** local terms of a
singular kernel, and it simply does not occur when the local data is
assembled by the standard **product** of ordinary (non-singular) local zeta
integrals.

## 3. Why this does not rescue $\mathfrak T_S(f_a)$

> ### Theorem 3.1 ($Z_S(g,a)$ is a different construction)
> Define $Z_S(g,a):=\sum_{v\in S}Z_v(g,a)$ (finite sum over places). Then
> $Z_S(g,a)$ is finite for every $a$ off the discrete pole set (Theorem
> 2.2), with **no** $C_v$-type leftover constant at any place — the
> mechanism of 108_17 Theorem 2.2 never activates, because the kernel
> $|u|_p^s$ has $\varphi_0$-type behaviour at $u=1$ equal to
> $g(1)\cdot1^{s}=g(1)$, a perfectly ordinary finite number, not multiplied
> by any divergent $C_p$: **there is no $C_p$ in this construction at all**,
> because there is no factor $1/|1-u|_p$ in the integrand to be singular in
> the first place.
>
> But $Z_S(g,a)\ne\mathfrak T_S(f_a\star\tilde g)$: the defining property
> that makes $\mathfrak T_S$ meaningful, $\mathfrak T_S(h)=N(h)$ for
> compactly supported $h$ (108_06 §1, quoting 107_239 (2.1)), is a statement
> about the kernel $1/|1-u|_v$ — it is what ties the finite-place sum to the
> zero side $N(h)=\hat h(0)+\hat h(1)-\sum_\rho\hat h(\rho)$. $Z_S(g,a)$
> carries no such property: for $g=\mathbf1_{\mathbb Z_p}$ at almost every
> place, Corollary 2.3 shows the natural global assembly of $Z_S$-type data
> is literally $\zeta(s)$ itself — an ordinary $L$-function value, with no
> relation of the $N(h)$ type to a sum over zeros.

**Proof.** The first paragraph is Theorem 2.2 read off directly (no term of
the form "$\varphi_0\cdot C_p$" appears in $Z_p(g,s)$ for any $g,s$, since
the integrand never has a $1/|1-u|_p$ factor). The second paragraph is the
definitional fact, already recorded at 108_06 §1, that $\mathfrak T_S$'s
role in Stage 1 is fixed by its agreement with $N(h)$ on compactly supported
data — a property $Z_S$ is not asserted, and does not appear, to share.
$\square$

> ### Theorem 3.2 (the two constructions coincide only where both apply to
> nothing new)
> On the class of $h$ for which $\mathfrak T_S(h)=N(h)$ holds (108_06 §1:
> compactly supported $h$), $h$ is *not* the graded family — 108_05 Prop 2.1
> rules $f_a$ out of that class entirely (§1 above). So there is no overlap
> instance in which $\mathfrak T_S(f_a\star\tilde g)$ and $Z_S(g,a)$ could be
> checked against each other and found equal or unequal on data both accept:
> **they are simply different constructions with disjoint domains of
> original validity**, one ($\mathfrak T_S$) forced beyond its founding
> identity to accept $f_a$ at all (108_06's extension, which is what
> produces $C_p$), the other ($Z_S$) never requiring such an extension
> because it never used the singular kernel that the founding identity
> needed.

**Proof.** Immediate from §1 and Theorem 3.1: $\mathfrak T_S(h)=N(h)$'s
domain is compactly supported $h$; $f_a\notin$ that domain (108_05 Prop
2.1); $Z_S(g,a)$'s natural domain is Schwartz–Bruhat $g$ with $a$ free —
disjoint roles for $f_a$ in the two constructions, by design. $\square$

> ### Corollary 3.3 (Route D fails as a disposal, but not vacuously)
> Route D does **not** show the constant in $\mathfrak T_S(f_a\star\tilde
> g)$ is zero, absorbed, or an artifact — outcome (i) requires exactly that,
> for *this* construction, and Theorem 3.1–3.2 show no such identification
> is available. What Route D **does** establish, candidly and as a genuine
> partial result: a mathematically legitimate, completely standard, and
> convergent way to pair the graded family's grading variable $a$ with test
> data $g$ exists (Tate's $Z_S(g,a)$), confirming that *some* extension of
> the corner-pairing idea to $\mathcal G$ is unproblematic — **provided one
> gives up the singular kernel that made $\mathfrak T_S$ equal to the zero
> side in the first place.** This is consistent with, and gives an
> independent derivation of, 108_17's finding: the obstruction lives
> entirely in the kernel $1/|1-u|_v$'s singularity at the group identity,
> and $f_a(1)=1$ (108_17 Theorem 3.1) is exactly what that kernel is
> singular against.

## 4. Scope

Proved here:

* §1: the descent classification (108_02) and the non-existence of
  $\hat f_a$ (108_05) jointly show $f_a$ was never in the domain where
  $\mathfrak T_S(h)=N(h)$'s two sides are simultaneously meaningful — cited
  from those notes' own theorems, not re-derived;
* Theorem 2.2, Corollary 2.3: the classical Tate local zeta integral and
  Euler product, elementary computation, no PV, no leftover constant, for
  any $g$;
* Theorem 3.1–3.2: $Z_S(g,a)$ is a well-defined, distinct construction from
  $\mathfrak T_S(f_a\star\tilde g)$, with disjoint domains of original
  validity, so its finiteness does not transfer;
* Corollary 3.3: Route D fails to dispose of the constant, with the failure
  mode identified precisely and tied to 108_17's mechanism.

Not established, and explicitly not claimed:

* that $Z_S(g,a)$ is "the" correct replacement for Stage 1's intended
  object — that is an interpretive question about 107_239's original intent
  this note does not have the source material to settle (this note works
  only from the (2.1) formula as quoted in 108_06 §1, per the working
  constraints of this phase);
* any numerical value of $\sum_pC_p$;
* any comparison with the zero side beyond the domain remark of §1;
* that Route D constitutes a fourth independent disproof beyond 108_16
  Theorem 5.1's three — it is better read as an independent *derivation* of
  the same mechanism 108_17 isolates, from the opposite direction (removing
  the kernel, rather than analyzing the kernel's criterion).

## 5. Verifier

`108_18_route_d_twist_slot_does_not_rescue_the_trace.py` checks: Theorem
2.2's closed form for $Z_p(\mathbf1_{\mathbb Z_p},s)$ against direct
truncated-geometric-series summation, for several primes and several $s$
with $\Re s>0$; entirety (polynomial-in-$p^{-s}$, no pole) of $Z_p(g,s)$ for
finitely supported $g$ away from $0$, checked by evaluating at points
approaching a shell boundary and confirming boundedness where the singular
$W_p$ construction would blow up; and Corollary 2.3's Euler product against
a direct partial-sum evaluation of $\zeta(s)$ for $\Re s>1$.
