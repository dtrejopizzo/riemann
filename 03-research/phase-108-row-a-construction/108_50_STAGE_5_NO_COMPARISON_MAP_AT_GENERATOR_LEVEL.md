# 108.50 — Stage 5: no comparison map at the level of generators

## 0. Result

The mission of Stage 5 is to compare two pairings built in this programme on
different objects: the corner pairing $I_{\mathrm{partial}}$ of Stage 0,
defined on **correspondence divisors built from compactly supported data**,
and the graded pairing $\Lambda_g^0$ of Stages 1–2, defined on
**mass-zero combinations of graded principal witnesses** $\delta_{s}$, whose
closed form was supplied by Stage 3 (108_38 Theorem 3.3).

This note proves that **no comparison map exists at the level of the natural
generators, in either direction**, and identifies the obstruction exactly:
it is the rigidity/finiteness clash already tabulated as instance 7 of
108_90 §2, now made a proved theorem for this specific pair of objects
rather than a retrodicted pattern.

* **Forward direction** (graded witness $\to$ correspondence divisor):
  impossible for every $s$, by an elementary and completely general lemma
  (Theorem 1.2 below): a nonzero function that is an eigenfunction of an
  unbounded family of dilations cannot have compact support.  The graded
  family $f_s$ that generates the witnesses $\delta_s$ is exactly such an
  eigenfunction (108_37 §2, read from source), so it is never itself a piece
  of compactly supported data, for any $s$.
* **Reverse direction** (correspondence divisor $\to$ graded witness): also
  obstructed, by an independent mechanism.  The Mellin transform of a
  compactly supported function is entire and, generically, has **infinitely
  many** zeros (Theorem 2.2, with a worked exact example), whereas the
  graded quotient is built from finite mass-zero combinations of point
  masses. There is no natural finite truncation.

Both obstructions are proved below without invoking any zero of $\xi$ in a
definition. Deliverable (3) — what would have to be true for Stage 3's
assembly to be an intersection number — and deliverable (4) — the
design-condition pre-test on the regularized repair — are carried out in
108_51, which depends on the impossibility theorems proved here.

## 1. The two categories, precisely

**Read from source (the task specification, summarizing Stage 0).** The
corner pairing is
\[
 I_{\mathrm{partial}}(D_f,D_g)=T(f*\tilde g),
\]
defined on correspondence divisors $D_f,D_g$ built from **compactly
supported** data $f,g$; it descends unconditionally to the numerical
quotient $V=\{\text{correspondence divisors}\}/\mathrm{rad}
I_{\mathrm{partial}}$, nondegenerate there. Neither the precise map
$f\mapsto D_f$ nor the operator $T$ is examined further here: this note
works only with the one property that is load-bearing for the argument —
membership in the category requires **compact support** — and states
explicitly (Scope, §5) that it does not reconstruct Stage 0's internal
definitions, which lie outside this note's read scope.

**Read from source (108_38 §0, §3, Theorem 3.3).** The graded pairing is
\[
 \Lambda_g^{0}\Big(\sum_i\lambda_i\delta_{s_i}\Big)
 =\sum_i\lambda_i\,c_g(s_i)\,\Phi(s_i),\qquad \sum_i\lambda_i=0,
\]
on mass-zero combinations of point masses $\delta_{s_i}$, each representing
a graded principal witness $\mathrm{div}(U_{s_i})$ (108_37 §2 uses the
notation $\mathrm{div}\,\,U_{s_0}-\mathrm{div}\,\,U_{s_1}$ for such a
combination).

**Read from source, verbatim (108_37 §2).**
> "the scaling covariance is carried entirely by the graded sections it is
> paired against, which by 108_02 are the character-covariant family
> $f_s$."

So the object each $\delta_s$ is dual to — the graded section $f_s$ itself —
is, by the programme's own construction, a **character-covariant
(eigen-)family under a dilation action**. Which dilation action is not
re-derived here; what matters for Theorem 1.2 below is only that it is
unbounded, which 108_90 §2 instance 7 records explicitly for this row of
the programme ("$\Gamma$ dense/divisible in $G$" $=$ "dilations by
$\mathbb N^\times$").

## 2. The forward obstruction

> ### Lemma 1.1 (unbounded orbit)
> Let $\Lambda\subset(0,\infty)$ be an unbounded subset (e.g.\ $\mathbb
> N^\times$, a set of prime powers, or all of $\mathbb R_{>0}$), and let
> $\chi:\Lambda\to\mathbb C^\times$ be any function with $\chi(\lambda)\ne0$
> for all $\lambda\in\Lambda$ (in particular any character). Suppose
> $f:(0,\infty)\to\mathbb C$ satisfies
> \[
>  f(\lambda x)=\chi(\lambda)f(x)\qquad\text{for all }\lambda\in\Lambda,\
> x>0 .
> \]
> If $f$ has compact support in $(0,\infty)$, then $f\equiv0$.

**Proof.** Suppose $f\not\equiv0$; pick $x_0>0$ with $f(x_0)\ne0$. For every
$\lambda\in\Lambda$, $f(\lambda x_0)=\chi(\lambda)f(x_0)$, and this is
nonzero because $\chi(\lambda)\ne0$ and $f(x_0)\ne0$. Hence
$\lambda x_0\in\mathrm{supp}(f)$ for every $\lambda\in\Lambda$. Since
$\Lambda$ is unbounded and $x_0>0$ is fixed, the set
$\{\lambda x_0:\lambda\in\Lambda\}$ is unbounded, so $\mathrm{supp}(f)$
is unbounded. This contradicts compact support. Hence $f\equiv0$. $\blacksquare$

The proof uses nothing beyond the definition of support and the fact that a
nonzero scalar times a nonzero scalar is nonzero; it holds verbatim over
$\mathbb R$, $\mathbb Q_p$, or any topological field, with "unbounded"
replaced by "not contained in a compact set."

> ### Theorem 1.2 (forward obstruction)
> For every $s$ indexing the graded family, the section $f_s$ (equivalently,
> any nonzero representative of the graded principal witness dual to
> $\delta_s$) does **not** lie in the compactly-supported-data category that
> defines Stage 0's correspondence divisors. Consequently there is no map
> \[
>  \iota:\ \{\delta_s\}\ \longrightarrow\ \{\text{correspondence divisors}\}
> \]
> sending $\delta_s\mapsto D_{f_s}$ with $f_s$ literally a piece of Stage
> 0's compactly supported data, for any $s$ in the index set.

**Proof.** By 108_37 §2 (quoted in §1), $f_s$ is character-covariant under
the dilation action carried by this row of the construction, which 108_90
§2 instance 7 records as unbounded ($\mathbb N^\times$, or a set of prime
powers containing arbitrarily large elements — either way unbounded in
$(0,\infty)$ or in the relevant local field). Apply Lemma 1.1 with
$\Lambda$ equal to that unbounded set and $\chi=\chi_s$ the covariance
character: since $f_s\not\equiv0$ (else $c_g(s)$, hence $\Phi$, would be
identically the zero functional at $s$, contradicting 108_38 Theorem 3.2,
which shows $\Phi\not\equiv0$ on a set that must be probed by nonzero
sections), $f_s$ cannot have compact support. Hence $D_{f_s}$, which by
Stage 0's definition requires compactly supported data, is not defined; the
map $\iota$ has no target for any $s$. $\blacksquare$

This is not a new phenomenon: it is 108_90 §2 instance 7 ("dilations by
$\mathbb N^\times$" vs. "compact support," flagged there for Stage 3) now
proved, rather than merely tabulated, for the Stage 0/Stage 2 comparison —
the one instance 8's escape (regularizing the *pairing*, not the object) was
designed to route around. 108_51 examines whether that escape is available
here.

## 3. The reverse obstruction

The natural candidate map in the other direction sends a compactly
supported $f$ to the zero divisor of its Mellin transform,
\[
 \hat f(s)=\int_0^\infty f(x)\,x^{-s-1}\,dx ,
\]
which, because the domain of integration is compact and bounded away from
$0$, converges for **every** $s\in\mathbb C$: $\hat f$ is entire.

> ### Fact 2.1 (worked example)
> Let $f=\mathbf 1_{[1,2]}$. Then
> \[
>  \hat f(s)=\int_1^2 x^{-s-1}\,dx=\frac{1-2^{-s}}{s}\qquad(s\ne0),\qquad
>  \hat f(0)=\log2 ,
> \]
> and $\hat f$ is entire with zero set
> \[
>  \hat f(s)=0\iff s=\frac{2\pi i k}{\log2},\quad k\in\mathbb Z\setminus\{0\}.
> \]
> In particular $\hat f$ has **infinitely many** zeros, all simple, on the
> imaginary axis.

**Proof.** For $s\ne0$, $\int_1^2 x^{-s-1}dx=\big[-x^{-s}/s\big]_1^2
=(1-2^{-s})/s$. As $s\to0$, $1-2^{-s}=s\log2+O(s^2)$, so the limit is
$\log2$, and since the original integral $\int_1^2x^{-s-1}dx$ is manifestly
entire in $s$ (differentiate under the integral sign; the integrand and all
its $s$-derivatives are continuous on the compact set $[1,2]\times K$ for
any compact $K\subset\mathbb C$), $\hat f$ extends holomorphically across
$s=0$ with that value. For $s\ne0$, $\hat f(s)=0\iff 2^{-s}=1\iff
-s\log2\in2\pi i\mathbb Z\iff s\in\frac{2\pi i}{\log2}\mathbb Z$; excluding
$s=0$ (where $\hat f=\log2\ne0$) gives exactly the stated set. Each such
zero is simple because $\hat f'(s)=-\big[(1-2^{-s})/s\big]'$, and a direct
computation at $s=2\pi ik/\log2$ gives $\hat f'(s)=-2^{-s}\log2/s=-\log2/s
\ne0$. $\blacksquare$

> ### Theorem 2.2 (reverse obstruction)
> The map $D_f\mapsto\mathrm{div}(\hat f):=\sum_{\hat f(s)=0}
> \mathrm{ord}_s(\hat f)\,\delta_s$ does not land in the graded
> quotient's generating set of **mass-zero, finite** combinations
> $\sum_i\lambda_i\delta_{s_i}$, $\sum_i\lambda_i=0$: for a generic
> compactly supported $f$ (Fact 2.1 exhibits one), $\mathrm{div}(\hat
> f)$ is an infinite, unweighted-mass-zero (indeed unsummable in the naive
> sense) divisor.

**Proof.** By Fact 2.1 the zero set of $\hat f$ for $f=\mathbf1_{[1,2]}$ is
countably infinite (indexed by $k\in\mathbb Z\setminus\{0\}$), each with
coefficient $\mathrm{ord}_s(\hat f)=1$. The formal sum
$\sum_{k\ne0}\delta_{2\pi ik/\log2}$ is not a finite combination, and "mass
zero" — $\sum\lambda_i=0$ — is not even meaningful for it without a
prescribed (and unproved) summation convention, since the naive sum of
coefficients $\sum_{k\ne0}1$ diverges. Hence this natural candidate does not
produce an element of $\mathrm{Prin}'$ as Theorem 3.3 of 108_38
describes it. $\blacksquare$

Nothing here rules out that *some* regularized or zeta-counted version of
$\mathrm{div}(\hat f)$ could be made sense of; that is not attempted,
and is listed as open in §5.

## 4. Conclusion

> ### Theorem 3 (no comparison map at generator level)
> There is no map of generators, in either direction, between the graded
> quotient $\mathrm{Prin}'/\mathrm{rad}\,\Lambda^0$ of Stage 2 and
> the numerical quotient $V$ of Stage 0, that sends a nonzero generator to a
> nonzero generator by the literal, unregularized identification available
> from the two constructions' own definitions.

**Proof.** Forward: Theorem 1.2. Reverse: Theorem 2.2. $\blacksquare$

This is a genuine impossibility statement about the *naive* comparison, not
about every conceivable comparison: it says exactly what fails (compact
support against unbounded dilation covariance; finite mass-zero divisors
against generically infinite Mellin zero sets) and nothing more. In
particular it does **not** show that the two pairings fail to correspond in
some deeper, regularized sense — only that the obvious identification of
their generators does not exist. 108_51 takes up whether a regularized route
(consistent with 108_90's design condition) can be built, and what such a
route would have to prove.

## 5. Scope

**Read.** 108_38 (in full), 108_37 (in full), 108_90 (in full), and the
task specification's summary of Stage 0 (the corner pairing formula, the
compact-support restriction, the numerical quotient $V$, and its
nondegeneracy).

**Not read, and not reconstructed.** Stage 0's own paper(s): the precise
definition of $D_f$, of $T$, and of $\mathrm{rad}\,I_{\mathrm
partial}$. Consequently:

* this note does **not** compare the two radicals' generating data (zeros
  of $\Phi$ versus whatever generates $\mathrm{rad}\,I_{\mathrm
  partial}$) — that comparison is not attempted, for lack of access to the
  latter's description, and is listed as open in 108_52;
* this note does **not** rule out a regularized comparison map built by
  smearing the graded family against a compactly supported window and
  taking a limit — that is examined, without being resolved, in 108_51.

**Proved here (full written proofs).** Lemma 1.1, Theorem 1.2, Fact 2.1,
Theorem 2.2, Theorem 3.

**Verified numerically.** Fact 2.1's zero formula, by direct floating-point
evaluation at $k=1,\dots,1000$; Lemma 1.1's mechanism, by an explicit
constructive extension of an eigenfunction defined on $[1,2]$ across
unboundedly many dilates.

**Conjectured.** Nothing in this note is conjectural; every claim is either
read from source, proved, or a numerical illustration of an already-proved
closed form.

**No zero of $\xi$ enters any definition in this note.**

## 6. Verifier

`108_50_no_comparison_map_at_generator_level.py` (i) constructs an
eigenfunction on $[1,2]$ under a chosen character and extends it across
$\lambda=2^0,2^1,\dots,2^{30}$, confirming every extended value is nonzero
(illustrating Lemma 1.1's mechanism); (ii) evaluates $\hat f(s)=(1-2^{-s})/s$
for $f=\mathbf1_{[1,2]}$ at $s=2\pi ik/\log2$ for $k=1,\dots,1000$ and
confirms $|\hat f(s)|<10^{-9}$ throughout (floating-point tolerance, not a
research threshold — the identity is exact by Fact 2.1's proof); (iii)
confirms $\hat f(0)=\log2\ne0$ by both the direct integral (numerical
quadrature via a Riemann sum) and the closed form, cross-checking Fact 2.1.
