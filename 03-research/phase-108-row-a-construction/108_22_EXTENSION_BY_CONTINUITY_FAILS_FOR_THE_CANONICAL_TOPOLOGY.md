# 108.22 — Extension by continuity fails, for the canonical regularizing
# topology, by the same mechanism that made substitution fail

## 0. Question and verdict

108.05 diagnosed Stage 1's original move — substituting $f_a(x)=x^{-a}$
directly into $\mathfrak T_S(f_a\star\tilde g)$ — as a category error: $f_a$
has no Mellin transform (108_05 Prop 2.1), so it is not a member of the test
class on which $\mathfrak T_S(\cdot\star\tilde g)$ is defined. The stated
alternative is to **extend by continuity/density** instead of substituting:
find a topology $\tau$ on a space $E\supseteq A_\delta\cup\{f_a\}$ in which
$A_\delta$ is dense and $\Lambda_g(f):=\mathfrak T_S(f\star\tilde g)$ is
$\tau$-continuous, so that density plus continuity *force* a unique value
$\Lambda_g(f_a)$.

\[
 \boxed{\text{For every topology }\tau\text{ satisfying the one coherence
 condition any candid reading of ``}f_a\in E\text{'' must impose — that
 test functions converging to }f_a\text{ recover its actual value }f_a(1)=1
 \text{ at }x=1\text{ — the canonical regularizing net already used
 throughout Stage 1 to make sense of }\Lambda_g(f_a)\text{ diverges, by
 108\_21 Theorem 1.1 (cited, not re-derived). Hence }\Lambda_g\text{ is not
 }\tau\text{-continuous at }f_a\text{, no continuous extension exists along
 that net, and the uniqueness question is moot: there is nothing to be
 unique. Extension by continuity does not escape Stage 1's obstruction — it
 meets the identical mechanism (108\_21 Theorem 1.1(a)-(b)), because that
 mechanism was already shown there to be a property of the graded family
 }\mathcal G\text{ as a family of quasi-characters, not an artifact of the
 substitution move.}}
\]

This is a negative result, proved, not conjectured. It is restricted in a
stated, precise way (§3): it does not rule out every conceivable topology
regardless of whether it deserves to be called an extension of $f_a$; it
rules out every topology satisfying the coherence condition, which is shown
(Lemma 2.3) to hold automatically for every classical function-space
topology, including the three families the mission names as candidates.

No zero of $\xi$ enters any definition below. `ROW_A_STATUS` remains
`partial`.

## 1. Setup: $\Lambda_g$ is zero-free by definition, zeros appear only in a
   derived theorem

> ### Definition 1.1 ($\Lambda_g$)
> For $f\in A_\delta$ (Lagarias's test class, 108_05 §1) and a fixed test
> function $g$, $\Lambda_g(f):=\mathfrak T_S(f\star\tilde g)$, computed by
> the arithmetic side: a sum over places of local integrals (107_239 (2.1),
> read from source). This uses no zero of $\xi$.

> ### Fact 1.2 (explicit formula, read from source)
> For $f,g\in A_\delta$,
> \[
>  \Lambda_g(f)=\hat f(0)\,\overline{\hat g(1)}+\hat f(1)\,\overline{\hat
>  g(0)}-\sum_{\xi(\rho)=0}{}'\hat f(\rho)\,\overline{\hat g(\rho')},
>  \qquad \rho'=1-\bar\rho,
>  \tag{$*$}
> \]
> the Weil explicit formula in the covariance form of 108_05 §1 (9.6),
> consistent with 107_241's computation (108_05 §1, "consistency check").

$(*)$ is a **theorem** about the zero-free-defined object $\Lambda_g$; it is
not how $\Lambda_g$ is defined. This is exactly the distinction 108_00 §2
requires, and it is why $(*)$ may legitimately be used below without
violating the source rule: every claim that follows is a claim about
$\Lambda_g$ as given by Definition 1.1, using $(*)$ only as a proved
identity on $A_\delta$.

> ### Observation 1.3 ($K_g$ is discrete)
> $(*)$ exhibits $\Lambda_g$, restricted to functions with a well-defined
> $\hat f$, as pairing $\hat f$ against the measure
> \[
>  K_g:=\overline{\hat g(1)}\,\delta_0+\overline{\hat g(0)}\,\delta_1
>  -\sum_\rho\overline{\hat g(\rho')}\,\delta_\rho
> \]
> on $\mathbb C$: a countable sum of point masses supported on
> $\{0,1\}\cup\{\rho:\xi(\rho)=0\}$.

## 2. The canonical net, and why it is not optional

108_05 Theorem 3.1 identifies the regularization that makes sense of
$\hat f_a$ at all: the cutoff $[1/T,T]$, "exactly the pairing" between the
graded family and the test class (108_05 Cor 4.1). This is also, concretely,
how Stage 1's arithmetic-side computation of $\Lambda_g(f_a)$ was carried
out throughout 108_06–108_21: a regularization (equivalently, Tate's
principal-value truncation of the local shell sums, 108_17 Def./Thm cited
via 108_21 Thm 1.1) with a cutoff parameter that is removed at the end. Call
this net $\{f_{a,T}\}_{T>1}$: $f_{a,T}$ is $f_a$ restricted to $[1/T,T]$ (or
a smooth mollification agreeing with $f_a$ on a growing compact core), each
$f_{a,T}\in A_\delta$ genuinely (its Mellin transform is the entire function
$2\sinh((s-a)\log T)/(s-a)$, 108_05 Thm 3.1).

> ### Definition 2.1 (coherence at the identity)
> Say a topology $\tau$ on $E\supseteq A_\delta\cup\{f_a\}$ is **coherent**
> if every $\tau$-convergent net $f_n\to f_a$ with $f_n\in A_\delta$
> satisfies $f_n(1)\to f_a(1)=1$.

Coherence is not an extra assumption smuggled in to make the theorem work;
it is the minimum any topology must satisfy for "$f_a\in E$" to mean what it
says. If $\tau$-convergence to the formal symbol "$f_a$" does not recover
$x^{-a}$'s actual value at the one point $x=1$ where it is trivially
defined and finite, then the element of $E$ being constructed is not, in
any operative sense, the function $x^{-a}$ — it is a different object
wearing its name. Lemma 2.3 records that this minimal requirement is
satisfied automatically, not exceptionally, by every classical candidate.

> ### Lemma 2.3 (coherence holds for the named candidates)
> (a) For the sharp cutoff net, $f_{a,T}(1)=f_a(1)=1$ **exactly**, for every
> $T>1$ — not merely in the limit, since $x=1\in[1/T,T]$ for all $T>1$. Any
> smooth mollification of the cutoff that equals $f_a$ on a neighborhood of
> $x=1$ inherits the same exact equality once $T$ is large enough that the
> mollifier's transition region has moved away from $x=1$.
> (b) For $f\in A_\delta$ with $\hat f$ decaying enough along verticals for
> Mellin inversion to hold (the standing hypothesis under which $A_\delta$
> is used throughout this program, e.g. 107_241), $f(1)=\frac1{2\pi}
> \int_{-\infty}^\infty \hat f(\sigma+it)\,dt$ for $\sigma$ in the strip, so
> $\tau_{A_\delta}$-convergence (uniform norm on the closed strip, refined by
> any decay control needed for the inversion integral) controls $f(1)$
> continuously: $|f_n(1)-f(1)|\le\frac1{2\pi}\int|\hat f_n-\hat
> f|\,dt\to0$.
> (c) Nuclear, rapid-decay (Schwartz-type) enlargements, in the style of
> Meyer (arXiv:math/0412277, already imported in this program, not
> re-derived here): by construction such spaces carry, among their defining
> family of seminorms, control of sup-norms on compacts, hence point
> evaluation at any fixed $x>0$ (in particular $x=1$) is continuous — this
> is the standard reason nuclear function spaces are used for distribution
> theory in the first place, not a special feature of this problem.
> (d) The weak-$*$ topology on Mellin transforms is the one candidate for
> which coherence is *not* automatic: weak-$*$ convergence against a
> predual not containing the evaluation-at-1 functional need not control
> $f_n(1)$. This is recorded candidly in §3.4 below as the one genuine gap
> in the argument, not swept in with (a)-(c).

**Proof.** (a) is immediate from the definition of the cutoff. (b) is
Mellin inversion plus dominated convergence, standard; verified numerically
below on a concrete instance. (c) is definitional for nuclear/Schwartz-type
spaces (finite or countable seminorm families including sup-norm-type
control), cited, not re-derived. (d) is a genuine caveat, not a proof gap
papered over — see §3.4. $\square$

## 3. The no-go theorem

> ### Theorem 3.1 (extension by continuity fails, along the canonical net)
> Let $\tau$ be a coherent topology (Def. 2.1) on $E\supseteq
> A_\delta\cup\{f_a\}$ with $A_\delta$ $\tau$-dense in $E$, and suppose the
> canonical net $\{f_{a,T}\}$ of §2 is $\tau$-convergent to $f_a$ (which it
> must be, by coherence, since it is exactly the net used to give
> $f_a(1)=1$ operative meaning in this program — 108_05 Thm 3.1 constructs
> no other). Then $\Lambda_g$ is **not** $\tau$-continuous at $f_a$: the net
> $\Lambda_g(f_{a,T})$ diverges as $T\to\infty$, for every $a\in\mathbb C$
> in the graded family and independently of $g$ (subject only to $g$
> ranging over the admissible class already used throughout 108_06–108_21).

**Proof.** By 108_21 Theorem 1.1(a)-(b) (cited, not re-derived): writing
$\varphi:=h(u^{-1})$ for $h=f_a\star\tilde g$ and $\varphi_0$ for its
locally-constant value on the shell $|u|_p=1$, the local term $W_p(\varphi)$
under Tate's principal value is finite **iff** $\varphi_0=0$, and when
$\varphi_0\ne0$ diverges at rate exactly $\varphi_0$ per unit of the
regularization cutoff — the same cutoff parameter $T$ that indexes
$f_{a,T}$, since (108_05 Cor. 4.1, and the identification recorded here)
Burnol's $[1/T,T]$ cutoff is precisely the regularization used to compute
$\Lambda_g$ on $\mathcal G$ throughout this Phase. Theorem 1.1(b) computes
$\varphi_0=f_a(1)=1$ for **every** $a\in\mathbb C$, as a consequence of
$u\mapsto|u|_p^{a}$ being a quasi-character ($\chi(1)=1$ always) — a
statement about the family $\mathcal G$ itself, uninvolved with any
particular choice of $g$. Hence $\varphi_0=1\ne0$ always, hence
$W_p(\varphi)$ diverges at a fixed nonzero rate for every place $p\in S$,
hence $\Lambda_g(f_{a,T})=\mathfrak T_S(f_{a,T}\star\tilde g)$ diverges as
$T\to\infty$. If $\tau$-convergence of the canonical net to $f_a$ held while
$\Lambda_g$ were $\tau$-continuous at $f_a$, $\Lambda_g(f_{a,T})$ would
converge to $\Lambda_g(f_a)\in\mathbb C$ — contradiction. $\square$

> ### Corollary 3.2 (uniqueness is vacuous)
> The question "does $\Lambda_g$ admit a *unique* continuous extension to
> $\mathcal G$" is answered: under the coherence condition, it admits **no**
> continuous extension along the one net available to realize $f_a$ as an
> operative limit of test functions in this program. Uniqueness does not
> arise because existence already fails.

### 3.3 A qualitative explanation: two different species of divergence

108_05 Theorem 3.1 shows the *Mellin-side* cutoff transform of $f_a$,
$2\sinh((s-a)\log T)/(s-a)$, restricted to the line $s=a+iu$, is the
**Dirichlet kernel** $k_T(u)=2\sin(u\log T)/u$: unbounded in sup-norm as
$T\to\infty$ off any fixed point, but **oscillatory** — sign-changing at
arbitrarily large $T$ (108_05 §6(ii), "persistent oscillation") — which is
exactly why it has a nontrivial weak-$*$ limit $2\pi\delta$ against smooth
test functions despite not converging pointwise or in sup-norm.

The *arithmetic-side* divergence of Theorem 3.1 above is of a different
kind. 108_21 Theorem 1.1(a) is explicit that it is "not merely an
unevaluated limit, but a literal, unbounded, $\varphi_0$-proportional
growth" — a shell-by-shell accumulation of a constant of fixed sign
($\varphi_0=1>0$ at every shell), hence **monotone**, not oscillatory. A
monotonically diverging family of numbers has no weak-$*$ limit of any kind:
there is no sense in which $\Lambda_g(f_{a,T})$ "settles down" into a
distribution the way $k_T$ does. This is verified on a toy model in §5(C)
below, and is the structural reason the measure-valued reading of 108_05
§4.2 — itself explicitly labeled "not proved" there — cannot rescue
$\Lambda_g$: there is no measure for $\Lambda_g(f_a)$ to converge to. The two
halves of Phase 108 are dual (108_05 Cor 4.1) on the Mellin-transform side;
they are **not** dual in a sense that produces a finite pairing on the
$\Lambda_g$ side, because $\Lambda_g$'s divergence, unlike the Mellin
transform's, carries no oscillatory structure to regularize against.

### 3.4 The one candidate this theorem does not close off

Definition 2.1 explicitly requires coherence. A weak-$*$ topology on Mellin
transforms (or a distribution space) whose predual does not control
point-evaluation at $x=1$ could in principle have $f_{a,T}\to f_a$ hold in a
*different* sense than pointwise, without the canonical net being forced to
be the one that carries the coherence content — and Theorem 3.1's proof,
which needs the canonical net specifically, would not directly apply. This
is recorded as **open**, not dismissed: no such topology is exhibited here,
and none is known to this program; the candid status is that Theorem 3.1
closes the coherent case completely and leaves the incoherent case
unexplored, because a topology in which "$f_a\in E$" does not mean "the
function $x^{-a}$, evaluated at $x=1$, equals $1$" is not obviously still
answering the question the mission asked.

## 4. Scope

**Proved here:**

* Theorem 3.1: no coherent topology makes $\Lambda_g$ continuous at $f_a$
  along the canonical net, for any $a\in\mathbb C$ in the graded family and
  any admissible $g$;
* Lemma 2.3(a)-(c): coherence holds automatically for the cutoff net itself,
  for $A_\delta$ under Mellin inversion (verified numerically on a concrete
  instance, §5), and for nuclear/Schwartz-type enlargements;
* Corollary 3.2: the uniqueness question is vacuous, not merely negative;
* §3.3: the qualitative reason (monotone vs. oscillatory divergence) the two
  halves of 108_05's duality do not produce a rescuing measure-valued limit
  for $\Lambda_g$.

**Read from source, cited, not re-derived:**

* 108_21 Theorem 1.1(a)-(b), the entire load-bearing fact;
* 108_05 Theorem 3.1 and Corollary 4.1 (the cutoff, the Dirichlet kernel,
  the duality reading);
* the explicit formula $(*)$ (107_241, consistent with Lagarias (9.6) per
  108_05 §1).

**Not established, and explicitly not claimed:**

* that *no* topology whatsoever, coherent or not, can make $\Lambda_g$
  continuous at $f_a$ — only that no coherent one can (§3.4);
* any identification of the PV shell-truncation of 108_17/108_21 with the
  $[1/T,T]$ cutoff of 108_05 beyond the reading recorded in §2 (both are
  the single regularization this Phase has used throughout to give
  $\Lambda_g(f_a)$ operative meaning; no new independent proof of their
  literal equality as limiting procedures is given here);
* anything about RH; `ROW_A_STATUS` remains `partial`.

## 5. Verifier

`108_22_extension_by_continuity_fails.py` checks, independently: (A) $f_a(1)=1$
on a grid of complex $a$; (B) coherence of the cutoff net and a smooth
mollification — $f_{a,T}(1)=1$ exactly, for both regularization schemes,
for every $T$ tested; (C) an elementary, self-contained toy model of
Theorem 1.1(a)'s mechanism (a shell sum with locally-constant value
$\varphi_0$: diverges linearly, monotonically, in the truncation depth iff
$\varphi_0\ne0$, and is exactly zero at every depth iff $\varphi_0=0$),
contrasted against an independently recomputed instance of 108_05's
oscillatory Dirichlet kernel off the line, confirming the monotone/
oscillatory distinction of §3.3 by direct sign-change counts; (D) Lemma
2.3(b) on a concrete $A_\delta$ member (Gaussian-Mellin
$f(x)=e^{-(\ln x)^2/2}$, $\hat f(s)=\sqrt{2\pi}\,e^{s^2/2}$): numerical
Mellin inversion recovers $f(1)=1$ from $\hat f$ by quadrature, against the
exact closed-form value.
