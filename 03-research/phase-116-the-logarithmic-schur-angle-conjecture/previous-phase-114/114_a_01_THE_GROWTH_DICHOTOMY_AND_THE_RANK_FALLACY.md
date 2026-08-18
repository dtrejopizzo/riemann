# 114.a.01 — The growth dichotomy, and the rank fallacy in a3

```
+--------------------------------------------------------------------------+
| ROW (a), ITEM a4 — STAGE 1: WHAT QUADRATIC GROWTH ACTUALLY REQUIRES       |
|                                                                          |
| THE DICHOTOMY   For the Connes-Consani absolute dimension on any l1      |
|   (Thm 3.3)     lattice model, h^0(mD) = Theta(m^2) if and only if the   |
|                 divisor grows in BOTH directions: rank AND radius.       |
|                 Proved two-sided, with explicit constants.               |
|                                                                          |
| a3 RE-AUDITED   107_146 Cor C ("Theta(deg D) in every rank") fixes the   |
|   (Cor 3.5)     rank r and grows only the archimedean part.  A surface   |
|                 is exactly the regime r -> infinity.  Cor C is therefore |
|                 SILENT about a4.  It neither closes it nor kills it.     |
|                 The ledger's reading of it as "curve-like, so no         |
|                 surface" is a QUANTIFIER MISMATCH.  a3 stays HAVE; the   |
|                 inference drawn from it in 113_15 sec.6 is withdrawn.    |
|                                                                          |
| 113_10 ROUTE(i) ANSWERED, AND RE-SPECIFIED.  The real-deg / integer-dim  |
|   (Thm 4.4)     mismatch in CC is NOT the mechanism.  CC's Spec Zbar has |
|                 homogeneity degree 1: it is a curve.  A lattice          |
|                 component is NECESSARY but NOT SUFFICIENT; its RANK must |
|                 grow linearly with deg D.  Route (i) restated.           |
|                                                                          |
| O1 DIAGNOSED    O1 = "h^0 is homogeneous of degree 0".  Curve = degree 1.|
|   (Thm 4.1-4.3) Surface = degree 2.  The three cases are separated by a  |
|                 single computable invariant delta, and delta = 2 FORCES  |
|                 an unbounded-rank lattice.  O1-TEST is thus necessary.   |
|                                                                          |
| VERIFIER        114_a_01_the_growth_dichotomy.py — 24 checks, exit 0,    |
|                 VERDICT: ALL CHECKS PASS (output in sec.7)               |
|                                                                          |
| GAPS OPENED     none.  GAPS DISCHARGED: none (this file is stage 1).     |
| CIRCULARITY     CLEAN.  No zero of xi, no sign(Q), no Weil positivity,   |
|                 no Li coefficient enters any definition or any proof.    |
+--------------------------------------------------------------------------+
```

**Depends on:**

- `03-research/phase-107-arithmetic-lefschetz-reconstruction/107_146_ABSOLUTE_DIMENSION_HIGHER_RANK.md`
  — §1 (the definition, quoted verbatim below), Thm A, Thm B, §5 Cor C, Thm D, §8. Read in full.
- `03-research/phase-113-the-trace-on-schwartz-data/113_10_THE_DEGREE_MAP_AND_THE_EFFECTIVE_CONE.md`
  — §5 Prop 5.1, Obstruction O1, routes (i)/(ii), R5–R8. Read in full.
- `03-research/phase-113-the-trace-on-schwartz-data/113_15_THE_FOUR_ROW_LEDGER.md`
  — §1 row (a) table (a1–a5), §6, §7 (R1–R23). Read in full.
- `03-research/THE_BACKWARD_MAP.md` — §4, the growth constraint.
- `00-references/papers-nuevos/A/arXiv-2205.01391v2/RR-J-final.tex`
  — Connes–Consani, *Riemann–Roch for* $\overline{\mathrm{Spec}\,\mathbb Z}$, §2–§3. Intro and §3 read.

---

## 0. What this file does, and what it does not

Item **a4** of the ledger reads, verbatim:

> | a4 | a **product** structure on which the dimension grows quadratically | MISSING | never attempted |

Before building a candidate it is worth knowing exactly what has to be true of
it. This file answers that question completely, in the only setting where the
absolute dimension is actually defined — the Connes–Consani $\mathbb S_\pm$-module
dimension on $\ell^1$ balls in $\mathbb Z^r$. The answer is a clean dichotomy
(Theorem 3.3) with an immediate consequence: the existing ledger entry a3 does
**not** obstruct a4, contrary to how it is used in `113_15` §6, and the reason
is a misplaced quantifier.

This file builds no product. That is `114_a_02`. This file also passes no
verdict on any candidate geometry. That is `114_a_03`. What it produces is the
**test**, made precise enough that a candidate can fail it in one line.

---

## 1. The absolute dimension, quoted from source

Fix integers $r\ge 1$, $n\ge 0$. Write $|v|_1=\sum_j |v_j|$ and

$$
 I_r(n)\ :=\ \{\,v\in\mathbb Z^r\ :\ |v|_1\le n\,\}.
$$

**Definition 1.1 (Connes–Consani §3, transcribed in 107_146 §1).**
A subset $F\subseteq I_r(n)$ *linearly generates* $I_r(n)$ if for every
$m\in I_r(n)$ there exist coefficients $\alpha(f)\in\{-1,0,1\}$, $f\in F$, with

$$
 m=\sum_{f\in F}\alpha(f)\,f
 \qquad\text{and}\qquad
 \sum_{f\in F}\bigl|\alpha(f)f\bigr|_1\ \le\ n .
 \tag{1.1}
$$

Set $\dim_r(n):=\min\{\,|F| : F \text{ linearly generates } I_r(n)\,\}$.

The second condition of (1.1) is the **mass bound**; it is what distinguishes
this from ordinary generation over $\{0,\pm1\}$, and it is CC's condition
verbatim. For $r=1$ this is CC's own case and their Proposition gives

$$
 \dim_1(n)=\Bigl\lceil \tfrac{\log(2n+1)}{\log 3}\Bigr\rceil .
 \tag{1.2}
$$

**Remark 1.2 (fidelity).** Everything below is a statement about
Definition 1.1 and nothing else. To guard against a mis-transcription, the
verifier of §7 re-derives $\dim_1(n)$ by exhaustive minimisation over all
subsets of $I_1(n)$ for $n=1,\dots,24$ and compares with (1.2): 24 of 24 agree,
and the jumps sit exactly at $n=(3^{k-1}+1)/2 = 1,2,5,14$. It further
reproduces the exact higher-rank minima
$\dim_2(1)=2,\ \dim_2(2)=4,\ \dim_2(3)=4,\ \dim_2(4)=6,\ \dim_3(1)=3,\ \dim_3(2)=6$
of `107_146` §7. The implementation is therefore the definition.

**Circularity of Definition 1.1.** CLEAN. $I_r(n)$ is a finite set of integer
vectors; $\dim_r(n)$ is a minimum over finitely many finite subsets. No zeta
value, no zero of $\xi$, no ordering of $\mathrm{Re}\,\rho$, no positivity of a
quadratic form enters. Not vacuous: $\dim_r(n)$ is a finite positive integer for
every $r,n\ge1$, computed exactly for nine pairs in §7.

---

## 2. The two-sided bracket

**Theorem 2.1 (entropy lower bound).** $\dim_r(n)\ \ge\ \log_3\bigl|I_r(n)\bigr|$.

*Proof.* Let $F$ linearly generate, $|F|=d$. Every $m\in I_r(n)$ is
$\sum_{f\in F}\alpha(f)f$ for some $\alpha\in\{-1,0,1\}^F$; the mass bound only
restricts the admissible $\alpha$ further. Hence the map
$\{-1,0,1\}^F\to\mathbb Z^r$, $\alpha\mapsto\sum\alpha(f)f$, has image containing
$I_r(n)$, so $|I_r(n)|\le 3^d$. $\square$

**Theorem 2.2 (digit upper bound; = 107_146 Theorem B, re-proved).**
$\dim_r(n)\ \le\ r\,\lceil \log_2(n+1)\rceil$ for all $r\ge1,\ n\ge1$.

*Proof.* Put $k=\lceil\log_2(n+1)\rceil$, so $n\le 2^k-1$, and take
$F=\{\,2^i e_j : 0\le i\le k-1,\ 1\le j\le r\,\}$, $|F|=rk$. Let $v\in I_r(n)$.
Each $|v_j|\le n\le 2^k-1$, so $|v_j|=\sum_{i\in S_j}2^i$ for a unique
$S_j\subseteq\{0,\dots,k-1\}$. Set $\alpha(2^ie_j)=\operatorname{sign}(v_j)$ for
$i\in S_j$ and $0$ otherwise. Then $\sum_f\alpha(f)f=v$, and the mass is
$$
 \sum_{j=1}^r\sum_{i\in S_j} \bigl|2^ie_j\bigr|_1
 =\sum_{j=1}^r\sum_{i\in S_j}2^i=\sum_{j=1}^r |v_j| = |v|_1 \le n ,
$$
so the mass bound holds with equality to $|v|_1$ and is never the binding
constraint for this $F$. $\square$

**Proposition 2.3.** $\dim_r(1)=r$.

*Proof.* Upper bound: $F=\{e_1,\dots,e_r\}$ works, since every $v\in I_r(1)$ is
$0$ or $\pm e_j$, with mass $\le 1$. Lower bound: if $n=1$, the mass bound
$\sum_f|\alpha(f)f|_1\le 1$ forces **at most one** $f$ with $\alpha(f)\ne0$, and
that $f$ must satisfy $|f|_1\le 1$, i.e. $f=\pm e_j$ for some $j$. So the set of
representable elements is $\{0\}\cup\{\pm f: f\in F,\ |f|_1=1\}$, which has at
most $2|F|+1$ elements; since $|I_r(1)|=2r+1$ we get $|F|\ge r$. $\square$

(Verified exhaustively for $r=1,\dots,5$ in §7, check E.)

**Theorem 2.4 (the bracket).** For $1\le r\le n$,
$$
 r\cdot\log_3\!\bigl(2\lfloor n/r\rfloor+1\bigr)
 \ \le\ \dim_r(n)\ \le\
 r\cdot\bigl\lceil\log_2(n+1)\bigr\rceil .
 \tag{2.1}
$$

*Proof.* Right: Theorem 2.2. Left: the box
$B=\{v\in\mathbb Z^r: |v_j|\le\lfloor n/r\rfloor\ \forall j\}$ satisfies
$|v|_1\le r\lfloor n/r\rfloor\le n$, hence $B\subseteq I_r(n)$ and
$|I_r(n)|\ge(2\lfloor n/r\rfloor+1)^r$; now apply Theorem 2.1. $\square$

**Corollary 2.5 (the shape).** For $1\le r\le n$,
$$
 \dim_r(n)\ =\ \Theta\!\left(r\,\log\frac{n}{r}\right)
 \quad\text{whenever } n\ge r^{1+\varepsilon},\ \varepsilon>0 \text{ fixed},
$$
with the implied constants $1/\log 3$ and $1/\log 2$ up to $o(1)$ and an additive
$r$. Both ends of (2.1) are $r\log n\cdot(1+o(1))$ times a constant in the
regime $\log(n/r)\asymp\log n$.

*Proof.* Immediate from (2.1): the left end is
$r\log_3(2n/r-1)$, the right is $r\log_2(n+1)+r$. $\square$

**Circularity of §2.** CLEAN. Every proof is a finite combinatorial argument
about $\{0,\pm1\}$-combinations of integer vectors.

---

## 3. The dichotomy

To speak of "growth in $\deg D$" one needs a divisor with a degree. The
following is the minimal structure that supports both a rank and an archimedean
size; it is the abstraction of what `114_a_02` will realise geometrically.

**Definition 3.1 (a gauged divisor).** A *gauged divisor* is a pair
$D=(k,a)$ with $k\in\mathbb Z_{\ge0}$ and $a\in\mathbb R_{\ge0}$. Its
*sections* and *dimension* are
$$
 H^0(D):=I_{k+1}\bigl(\lfloor e^{a}\rfloor\bigr),
 \qquad
 h^0(D):=\dim_{k+1}\bigl(\lfloor e^{a}\rfloor\bigr),
$$
and its degree is $\deg D:=k+a$. Multiples are $mD:=(mk,ma)$, so
$\deg(mD)=m\deg D$: the degree is a genuine linear functional on the ray.

**Remark 3.2.** $k$ is the *rank direction* — the number of independent integral
coordinates — and $a$ is the *radius direction* — the archimedean size of the
box. CC's $\overline{\mathrm{Spec}\,\mathbb Z}$ is the sub-family $k=0$: there is
exactly one integral coordinate and only $a$ moves. That is the whole content of
the comparison below.

**Theorem 3.3 (the growth dichotomy).** Let $D=(k,a)$ be a gauged divisor with
$k\ge0$, $a\ge0$, $\deg D>0$. Then, as $m\to\infty$,

1. if $k\ge1$ and $a>0$:
   $$
    \frac{ka}{\log 3}\,m^2\,(1+o(1))\ \le\ h^0(mD)\ \le\ \frac{ka}{\log 2}\,m^2\,(1+o(1)),
   $$
   so $h^0(mD)=\Theta(m^2)=\Theta\bigl((\deg mD)^2\bigr)$;
2. if $k=0$ and $a>0$: $h^0(mD)=\bigl\lceil\log_3(2\lfloor e^{ma}\rfloor+1)\bigr\rceil
   =\frac{a}{\log 3}m+O(1)=\Theta(m)=\Theta(\deg mD)$;
3. if $k\ge1$ and $a=0$: $h^0(mD)=\dim_{mk+1}(1)=mk+1=\Theta(m)=\Theta(\deg mD)$.

Hence **$h^0$ is quadratic in the degree if and only if the divisor grows in both
directions at once.**

*Proof.* (2) is (1.2) with $n=\lfloor e^{ma}\rfloor$, whose logarithm is
$ma+O(e^{-ma})$. (3) is Proposition 2.3 with $r=mk+1$.

(1) Put $r=mk+1$, $n=\lfloor e^{ma}\rfloor$. For $m$ large, $r\le n$. By
Theorem 2.4,
$$
 h^0(mD)\ \ge\ r\log_3\!\bigl(2\lfloor n/r\rfloor+1\bigr)
 \ \ge\ (mk+1)\cdot\frac{\log(2n/r-1)}{\log 3}
 \ =\ (mk+1)\cdot\frac{ma-\log(mk+1)+O(1)}{\log 3},
$$
which is $\frac{ka}{\log3}m^2(1+O(\log m/m))$; and
$$
 h^0(mD)\ \le\ r\lceil\log_2(n+1)\rceil\ \le\ (mk+1)\Bigl(\frac{ma}{\log 2}+1\Bigr)
 \ =\ \frac{ka}{\log2}m^2\bigl(1+O(1/m)\bigr). \qquad\square
$$

Numerically, for $k=a=1$: at $m=80$ the two ends of the bracket are
$0.8790\,m^2$ and $1.4681\,m^2$, against the asymptotic constants
$1/\log 3=0.9102$ and $1/\log 2=1.4427$; the bracket is inside
$[0.83,2.25]\,m^2$ for **every** $m\ge2$ and inside $[0.86,1.50]\,m^2$ for
$m\ge40$ (§7, checks G1–G3b). The two curve regimes give
$h^0(mD)/m^2\to 0$ (check G6).

**Corollary 3.4 (the mechanism, in one line).**
$$
 h^0 \ \approx\ (\text{rank of the section lattice})\times(\log \text{radius}),
$$
and $\deg$ is the **sum** of those two quantities. A product of two growing
factors against a sum of the same two: that is the entire source of the square.
Everything that follows in row (a) is a search for a geometry over
$\mathrm{Spec}\,\mathbb Z$ in which both factors are present and both are charged
to the degree.

**Corollary 3.5 (re-audit of a3 / 107_146 Corollary C).**
`107_146` §5 reads, verbatim:

> In CC's normalisation an archimedean divisor $D=a\{\infty\}$ has $\deg D=a$
> and $n=\lfloor e^a\rfloor$. Theorems A and B give, for $r\ge2$,
> $\frac{\deg D}{\log 2}\le \dim_r(\lfloor e^{\deg D}\rfloor)\le\frac{r\deg D}{\log 2}+r$.
> **Corollary C.** $\dim_{\mathbb S_\pm}M_r$ is $\Theta(\deg D)$ — linear in the
> degree — in **every** rank $r$.

Its quantifier structure is $\forall r\ \exists C_r\ \forall D$, with $C_r=r/\log2$
and, decisively, with $D=a\{\infty\}$ **purely archimedean**: the rank $r$ is a
fixed parameter of the ambient module $M_r$ and contributes nothing to $\deg D$.
In the language of Definition 3.1 this is exactly case (2) of Theorem 3.3 with
an inert spectator rank, i.e. the family $\{(0,a)\}_{a}$ up to the constant $r$.
Therefore:

- Corollary C is **true** and is correctly recorded as a3 = HAVE;
- Corollary C says **nothing** about a4, because a surface is by definition the
  regime in which $r$ itself grows with the degree and is charged to it;
- consequently the inference in `113_15` §6 —
  *"The CC absolute dimension is $\Theta(\deg D)$, curve-like; a surface needs $D^2$"* —
  is a quantifier mismatch and is **withdrawn** here. It is not evidence against
  a4.

*Proof.* Theorem 3.3(1) exhibits a family of gauged divisors, built from the same
Definition 1.1, with $h^0(mD)\asymp(\deg mD)^2$. If Corollary C excluded
quadratic growth, these two statements would contradict each other; they do not,
because Corollary C quantifies over $D$ with $r$ held fixed. $\square$

**Remark 3.6 (this is not a criticism of 107_146).** `107_146` states its own
hypothesis explicitly ("an archimedean divisor $D=a\{\infty\}$") and even flags
the residual doubt in its §8: *"whether the $\ell^1$ mass functional is the right
one for a product at all."* The mismatch is in the *use* made of Corollary C in
the ledger, not in the corollary.

---

## 4. The homogeneity degree: O1, curves, surfaces

**Definition 4.1.** Let $D\mapsto h^0(D)\in[0,\infty]$ be any dimension function
on a divisor set closed under $D\mapsto mD$, $m\in\mathbb Z_{\ge1}$, with
$\deg(mD)=m\deg D$. The *homogeneity degree of $h^0$ at $D$* is
$$
 \delta(D)\ :=\ \lim_{m\to\infty}\frac{\log h^0(mD)}{\log m}
$$
when the limit exists.

**Theorem 4.2 (the three regimes).**

1. **$\delta=0$ is obstruction O1.** If $\mathrm{Div}$ is a real or complex
   vector space and the effective cone is stable under positive scaling, then
   $h^0(mD)=h^0(D)$ for all $m>0$ and $\delta\equiv0$. This is `113_10`
   Prop 5.1 and Obstruction O1 verbatim.
2. **$\delta=1$ is a curve.** Any $h^0$ satisfying
   $c_1\deg D\le h^0(D)\le c_2\deg D+c_3$ has $\delta=1$. CC's
   $\overline{\mathrm{Spec}\,\mathbb Z}$ and every fixed-rank $M_r$ are here, by
   Corollary C.
3. **$\delta=2$ is a surface**, and is what row (a) needs: it is the hypothesis
   under which $\chi(mD)=\tfrac12 m^2 D^2+\dots$ can have a leading quadratic
   term.

*Proof.* (1) is `113_10` Prop 5.1: $\mathrm{rad}\,I_d$ is a linear subspace and
$f\ge0\iff mf\ge0$, so effectivity is scale-invariant and $H^0(mD)=H^0(D)$ as
sets after the bijection $g\mapsto mg$. (2) and (3) are immediate from the
definition of $\delta$. $\square$

**Theorem 4.3 (unbounded rank is necessary for $\delta=2$).** Let
$\{D_m\}$ be a family of gauged divisors (Definition 3.1) with
$\deg D_m=\Theta(m)$, and suppose the ranks are bounded, $k_m\le k_0$ for all
$m$. Then $h^0(D_m)=O(m)$, so $\delta\le1$.

*Proof.* $\deg D_m=k_m+a_m=\Theta(m)$ with $k_m\le k_0$ gives $a_m=O(m)$.
Theorem 2.2 gives
$h^0(D_m)\le(k_0+1)\lceil\log_2(\lfloor e^{a_m}\rfloor+1)\rceil\le(k_0+1)(a_m/\log2+1)=O(m)$.
$\square$

Numerically: for fixed rank $7$ and radius $e^m$, $h^0/m^2\le 11/m\to0$, equal to
$1.01\cdot10^{-4}$ at $m=10^5$ (§7, check I1).

**Theorem 4.4 (route (i) of 113_10, answered and re-specified).**
`113_10` §5 offers as route (i):

> produce a divisor group with a genuine discrete (lattice) component, so that
> "$n$ large" has content — this is what Arakelov theory does, and it is what
> Connes–Consani's Riemann–Roch for $\mathrm{Spec}\,\mathbb Z$ does in its own
> way, since there $\deg$ is real-valued while $\dim H^0$ is integer-valued.

Then:

1. **The discrete/continuous mismatch is real but is not the mechanism.** In
   CC's $\overline{\mathrm{Spec}\,\mathbb Z}$, $\deg$ is real-valued and
   $\dim H^0$ is integer-valued, exactly as stated; and $\delta=1$ there, by
   Theorem 4.2(2) and Corollary C. The mismatch buys the ceiling function in
   (1.2). It does not buy the square.
2. **A lattice component is necessary.** By Theorem 4.3, $\delta=2$ forces the
   rank of the integral component to be unbounded along the ray; in particular
   the divisor group cannot be a fixed finite-dimensional real or complex vector
   space with a scaling-stable cone. So the O1-TEST is a genuine necessary
   condition, not a heuristic.
3. **It is not sufficient.** Route (i) as literally stated is satisfied by CC and
   still yields $\delta=1$. The correct statement of route (i) is:

   > **(i$'$)** produce a divisor group whose integral component is a lattice
   > **whose rank grows linearly with $\deg D$**, with the rank charged to the
   > degree.

*Proof.* (1) is Corollary C plus Definition 4.1. (2) is Theorem 4.3. (3) is (1)
together with Theorem 3.3(1), which shows (i$'$) is achievable. $\square$

**Circularity of §4.** CLEAN. $\delta$ is defined by a limit of ratios of
logarithms of finite integers. Theorem 4.2(1) quotes `113_10` Prop 5.1, itself
proved there from linearity of $\mathrm{rad}\,I_d$ with no zero input. Not
vacuous: all three values $\delta=0,1,2$ are realised by explicit examples
(O1 inside $\mathcal D$; CC's $\overline{\mathrm{Spec}\,\mathbb Z}$; Theorem 3.3(1)).

---

## 5. The two tests, made formal

The task's two cheap tests are now definitions, so that `114_a_03` can apply them
uniformly and a candidate can fail in one line.

**Definition 5.1 (O1-TEST).** A candidate geometry $X$ over
$\mathrm{Spec}\,\mathbb Z$ *passes the O1-TEST* if there is a divisor $D$ with
$\deg D>0$ whose section modules $H^0(mD)$ contain integral lattices
$\Lambda_m\cong\mathbb Z^{r_m}$ with $r_m\to\infty$, and the effective condition
is **not** invariant under $D\mapsto\lambda D$, $\lambda>0$. It *fails* if
$\mathrm{Div}(X)$ is (modulo its radical) a real or complex vector space with a
scaling-stable effective cone, since then $h^0(mD)=h^0(D)$ by `113_10` Prop 5.1.

(The test is on the *sections*, not on the divisor group: in the model of
`114_a_02` the divisor group is $\mathbb Z\oplus\mathbb R$, of integral rank
one, while the section lattices have rank $mk+1\to\infty$. It is the rank of
$H^0$ that Theorem 4.3 constrains.)

**Definition 5.2 (GROWTH-TEST).** A candidate passes the GROWTH-TEST if there is
a divisor $D$ with $\deg D>0$ and $h^0(mD)=\Theta(m^2)$, equivalently
$\delta(D)=2$ in the sense of Definition 4.1. It fails if $\delta(D)\le1$ for
every $D$.

**Proposition 5.3 (the tests are ordered).** GROWTH-TEST passed
$\Longrightarrow$ O1-TEST passed. The converse fails: CC's
$\overline{\mathrm{Spec}\,\mathbb Z}$ passes the O1-TEST in the weak sense of
possessing an integral $\dim H^0$ against a real $\deg$, and fails the
GROWTH-TEST.

*Proof.* Forward: Theorem 4.3 contrapositive plus Theorem 4.2(1). Converse:
Corollary C. $\square$

**Proposition 5.4 (a necessary bookkeeping condition).** If a candidate passes
the GROWTH-TEST at $D$, then $\deg D$ must charge **both** the rank direction and
the radius direction: writing $\deg=\deg_{\mathrm{fin}}+\deg_\infty$, both terms
must be $\Theta(m)$ along $mD$.

*Proof.* If $\deg_{\mathrm{fin}}(mD)=o(m)$ then, since $\deg_{\mathrm{fin}}$
bounds the rank in any model where rank $\le \deg_{\mathrm{fin}}+O(1)$, the rank
is $o(m)$ and Theorem 2.4 gives $h^0=o(m)\cdot O(m)=o(m^2)$. If
$\deg_\infty(mD)=o(m)$ then the radius is $e^{o(m)}$ and Theorem 2.2 gives
$h^0=O(m)\cdot o(m)=o(m^2)$. $\square$

This is the sharpest form of the criterion, and it is what kills most
candidates in `114_a_03` immediately: **a geometry with only one direction
charged to the degree cannot be a surface, however sophisticated it is.**

---

## 6. Gaps

None.

Every statement in §§1–5 is proved here from Definition 1.1 by finite
combinatorics and elementary asymptotics, or is quoted with a file and a
theorem number from a repo file read in full (`107_146` §1/§5/Thm A/Thm B,
`113_10` §5 Prop 5.1 and O1, `113_15` §1/§6/§7). No step is deferred.

The one thing §§1–5 do **not** do is construct a geometry: Definition 3.1 is an
abstraction, not a scheme. That is not a gap in this file, it is the content of
`114_a_02`, and the gaps opened there are recorded there.

---

## 7. Verifier

`114_a_01_the_growth_dichotomy.py`. Run:

```
$ python3 114_a_01_the_growth_dichotomy.py
========================================================================
A  fidelity: rank one reproduces Connes-Consani  dim = ceil(log_3(2n+1))
========================================================================
PASS  A1 exhaustive dim_1(n) = ceil(log_3(2n+1)) for n=1..24   | 24/24 agree
PASS  A2 dim_1 jumps exactly at n = (3^{k-1}+1)/2 = 1,2,5,14   | observed [1, 2, 5, 14], predicted [1, 2, 5, 14]

========================================================================
B  exact higher-rank minima against 107_146 section 7
========================================================================
PASS  B  dim_2(1) = 2   | computed 2
PASS  B  dim_2(2) = 4   | computed 4
PASS  B  dim_2(3) = 4   | computed 4
PASS  B  dim_2(4) = 6   | computed 6
PASS  B  dim_3(1) = 3   | computed 3
PASS  B  dim_3(2) = 6   | computed 6

========================================================================
C  Theorem 2.1 (entropy) and Theorem 2.2 (digits) on every exact value
========================================================================
PASS  C1 dim >= ceil(log_3 |I_r(n)|)  on all exact values   | dim_1(1)=1>=1; dim_1(4)=2>=2; dim_1(13)=3>=3; dim_2(1)=2>=2; dim_2(2)=4>=3; dim_2(3)=4>=3; dim_2(4)=6>=4; dim_3(1)=3>=2; dim_3(2)=6>=3
PASS  C2 dim <= r*ceil(log_2(n+1))    on all exact values   | dim_1(1)=1<=1; dim_1(4)=2<=3; dim_1(13)=3<=4; dim_2(1)=2<=2; dim_2(2)=4<=4; dim_2(3)=4<=4; dim_2(4)=6<=6; dim_3(1)=3<=3; dim_3(2)=6<=6

========================================================================
D  cardinality of the l1 ball
========================================================================
PASS  D  |I_r(n)| = sum_i 2^i C(r,i) C(n,i), r<=4, n<=6

========================================================================
E  Proposition 2.3   dim_r(1) = r
========================================================================
PASS  E  dim_r(1) = r for r = 1..5   | [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]

========================================================================
F  Theorem 2.4   r*log_3(2*floor(n/r)+1) <= dim <= r*ceil(log_2(n+1))
========================================================================
PASS  F1 the two bracket ends are consistent (left <= right) on the grid   | 195 grid points
PASS  F2 the box is inside the ball (proof of the left end)
PASS  F3 the bracket contains every exact value   | (1,1):[1.00,1]  dim=1; (1,4):[2.00,3]  dim=2; (1,13):[3.00,4]  dim=3; (2,1):[0.00,2]  dim=2; (2,2):[2.00,4]  dim=4; (2,3):[2.00,4]  dim=4; (2,4):[2.93,6]  dim=6; (3,1):[0.00,3]  dim=3; (3,2):[0.00,6]  dim=6

========================================================================
G  Theorem 3.2  the growth dichotomy
========================================================================
    m      LB/m^2      UB/m^2      (targets 1/ln3=0.9102, 1/ln2=1.4427)
     5      0.8502      1.9200
    10      0.8306      1.6500
    20      0.8434      1.5225
    40      0.8625      1.4863
    80      0.8790      1.4681
PASS  G1 surface regime: LB/m^2 -> 1/ln 3 = 0.91024   | m=80 gives 0.87898
PASS  G2 surface regime: UB/m^2 -> 1/ln 2 = 1.44270   | m=80 gives 1.46812
PASS  G3a surface regime: 0.83*m^2 <= dim <= 2.25*m^2 for EVERY m >= 2 (uniform Theta)   | min LB/m^2 = 0.8305, max UB/m^2 = 2.2500
PASS  G3b surface regime: the bracket tightens to [0.86,1.50]*m^2 for m >= 40   | min LB/m^2 = 0.8625, max UB/m^2 = 1.4992 (the ceiling in log_2 makes the upper end oscillate; sup is at m=43)
PASS  G4 curve regime A (rank 1, radius e^m): LB/m and UB/m both O(1)   | m=5:[1.037,1.600]; m=10:[0.973,1.500]; m=20:[0.942,1.450]; m=40:[0.926,1.450]; m=80:[0.918,1.450]
PASS  G5 curve regime B (rank 3m+1, radius 1): dim = rank exactly, hence linear
PASS  G6 the two curve regimes are NOT quadratic: (dim/m^2) -> 0   | curve A: UB/m^2 = 0.01812 at m=80

========================================================================
H  Theorem 4.1  the homogeneity degree of h^0
========================================================================
PASS  H1 surface: d log h^0 / d log m = 2   | measured 1.9823
PASS  H2 curve  : d log h^0 / d log m = 1   | measured 1.0000
PASS  H3 surface, lower bracket also has slope 2   | measured 2.0272

========================================================================
I  negative controls
========================================================================
PASS  I1 fixed rank r=7, radius e^m: UB/m^2 <= 11/m -> 0; no fixed-rank model is a surface   | m=10: 1.050e+00; m=100: 1.015e-01; m=1000: 1.010e-02; m=100000: 1.010e-04
PASS  I2 control: a scaling-stable h^0 has slope 0, not 2
PASS  I3 the entropy bound is strictly weaker than dim at (r,n)=(2,4)   | ceil(log_3 41) = 4 < dim_2(4) = 6
PASS  I4 the mass condition is active: {(1,0),(0,1),(1,1)} does NOT generate I_2(2)   | e.g. (2,0) needs mass 2 from (1,0)+(1,0), unavailable

========================================================================
VERDICT: ALL CHECKS PASS
$ echo $?
0
```

Three checks were rewritten during development because the *assertion* was
wrong, never the mathematics: A2 originally named $n=1,4,13$ (the tops of the
constancy ranges) instead of $n=1,2,5,14$ (the jump points); G3b originally
asserted an upper constant $1.49$ where the true supremum over $m\ge40$ is
$1.4992$, attained at $m=43$ because $\lceil\log_2\rceil$ oscillates; I1
originally used $m=160$, at which $11/m$ is $0.069$, not $<0.01$. In each case
the corrected assertion is the true one and is what §§2–4 state.

---

## 8. Refutation conditions, pre-registered (continuing from R23)

- **R24.** If a candidate geometry passes the GROWTH-TEST (Definition 5.2) but
  its degree map charges only one of the two directions — i.e. Proposition 5.4
  fails for it — then the computation of $h^0$ is inconsistent with the
  computation of $\deg$ and the candidate must be rejected, not repaired.
- **R25.** If any construction claims $\delta=2$ while its divisor group has
  bounded integral rank along the ray, it contradicts Theorem 4.3 and is wrong.
  This is the cheapest single test in row (a): *count the rank*.
- **R26.** If a future file re-uses `107_146` Corollary C as evidence against
  a4, it must first quote its hypothesis "$D=a\{\infty\}$ archimedean, $r$ fixed"
  and explain why the candidate falls under it. Corollary 3.5 is the standing
  correction; using Cor C without that quotation fires R26.
- **R27.** If the $\ell^1$ mass functional of Definition 1.1 is replaced by
  another gauge and the growth exponent $\delta$ changes for the family of
  Theorem 3.3(1), then $\delta$ is a gauge artefact and this whole file is
  evidence about $\ell^1$ only. (Tested and not fired in `114_a_02` §5.)

---

## 9. Scope

**Proved here.**

- Theorem 2.1 (entropy lower bound $\dim_r(n)\ge\log_3|I_r(n)|$).
- Theorem 2.2 (digit upper bound $\dim_r(n)\le r\lceil\log_2(n+1)\rceil$) —
  independent re-proof of `107_146` Theorem B, with the observation that the
  binary witness has mass exactly $|v|_1$, so the mass bound is never binding
  for it.
- Proposition 2.3 ($\dim_r(1)=r$), with the mass-bound argument for the lower
  bound.
- Theorem 2.4, the two-sided bracket, and Corollary 2.5.
- Theorem 3.3, the growth dichotomy, all three cases, with explicit constants
  $ka/\log3$ and $ka/\log2$.
- Corollary 3.5, the quantifier re-audit of `107_146` Corollary C, and the
  withdrawal of the inference drawn from it in `113_15` §6.
- Theorem 4.2 (the three homogeneity regimes), Theorem 4.3 (unbounded rank is
  necessary for $\delta=2$), Theorem 4.4 (route (i) answered and re-specified as
  (i$'$)).
- Definitions 5.1, 5.2 and Propositions 5.3, 5.4 (the two tests, ordered, plus
  the both-directions bookkeeping condition).

**Read from source.**

- Definition 1.1 and formula (1.2): Connes–Consani, arXiv:2205.01391v2, §3, as
  transcribed in `107_146` §1.
- `107_146` §5 Corollary C, quoted verbatim in Corollary 3.5; Theorems A, B, D
  and §8 read.
- `113_10` §5 Proposition 5.1, Obstruction O1, routes (i)/(ii), R5–R8, quoted in
  Theorem 4.2(1) and Theorem 4.4.
- `113_15` §1 row (a) table and §6, quoted in §0 and Corollary 3.5.

**Verified numerically.**

- Definition 1.1 reproduces CC's closed formula for $n=1,\dots,24$ (24/24) and
  `107_146`'s exact rank-2 and rank-3 minima (6/6).
- The bracket (2.1) contains all nine exactly computed dimensions.
- The three growth regimes of Theorem 3.3, including the asymptotic constants
  $1/\log3$ and $1/\log2$ and the uniform bracket $[0.83,2.25]m^2$.
- The homogeneity slopes $\delta=2$ (surface) and $\delta=1$ (curve), measured
  as $2.0272/1.9823$ and $1.0000$.
- Negative controls I1–I4, including the fact that the entropy bound is strictly
  weaker than the true dimension at $(r,n)=(2,4)$, so Theorem 2.1 must not be
  mistaken for an equality.

**Not established.**

- That any *geometry over $\mathrm{Spec}\,\mathbb Z$* realises Definition 3.1
  with $k\ge1$. Definition 3.1 is an abstraction; `114_a_02` supplies one
  realisation and `114_a_03` decides the rest.
- The exact constant $\lim h^0(mD)/m^2$ inside $[ka/\log3,\ ka/\log2]$. The
  rank-two constant is `107_146`'s own open conjecture and is not needed here:
  the dichotomy is a $\Theta$ statement.
- Anything about $h^1$, duality, $K$, or an intersection form. Those are
  `114_a_02` §4 and row (d).
- Any consequence for RH. Nothing in this file bears on the location of the
  zeros, and nothing in it may be used as if it did.
