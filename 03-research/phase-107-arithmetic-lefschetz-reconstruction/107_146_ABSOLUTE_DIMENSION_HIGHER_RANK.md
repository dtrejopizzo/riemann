# 107.146 — The absolute dimension in higher rank: base 3 is a rank-one accident

## 0. Source and independence

Base: Connes–Consani, *Riemann-Roch for $\overline{\Spec\Z}$*, arXiv:2205.01391
(folder `A/arXiv-2205.01391v2`), §2–§3.

Nothing below uses a zero of $\xi$, a Li coefficient, the sign of the Weil
form, or a positive part extracted from that form.  The source rule of
107_00 §2 is respected.  All objects are finite and combinatorial.

## 1. Setting

Fix integers $r\ge 1$ and $n\ge 1$.  Following CC §2, let

\[
 M_r(n):=\|H(\Z^r)\|_n:\Gamma^{o}\to\Se_*,\qquad
 M_r(n)(F)=\Big\{\varphi:F\to\Z^r\ \Big|\ \varphi(*)=0,\
 \sum_{x\in F\setminus\{*\}}|\varphi(x)|_1\le n\Big\},
\]

an $\spm$-module, where $|\cdot|_1$ is the $\ell^1$ norm.  Its value on
$1_+$ is the $\ell^1$ ball

\[
 I_r(n):=M_r(n)(1_+)=\{v\in\Z^r:\ |v|_1\le n\}.
\]

**Definition (CC §3).**  A subset $F\subseteq I_r(n)$ *linearly generates*
if for every $m\in I_r(n)$ there exist $\alpha(f)\in\{-1,0,1\}$ with

\[
 m=\sum_{f\in F}\alpha(f)f
 \qquad\text{and}\qquad
 \sum_{f\in F}|\alpha(f)f|_1\le n .
 \tag{1}
\]

Set $\dim_r(n):=\min\{|F|:F\text{ linearly generates}\}$.

The second condition in (1) — the *mass bound* — is what distinguishes this
from ordinary generation.  It is CC's condition verbatim.

For $r=1$ this is CC's case, and their Proposition gives

\[
 \dim_1(n)=\Big\lceil\tfrac{\log(2n+1)}{\log 3}\Big\rceil .
 \tag{2}
\]

(Reproduced here by exhaustive minimisation for $n=1,\dots,40$; jumps at
$n=1,4,13,40=(3^k-1)/2$, matching their footnote.)

The question of this note is what happens for $r\ge2$, i.e. on a product.
It is not addressed in the literature.

## 2. Two lemmas

### Lemma 1 (no cancellation on the boundary sphere)

Let $v\in I_r(n)$ with $|v|_1=n$, and let $v=\sum_{f\in A}\alpha_f f$ with
$\alpha_f\in\{\pm1\}$ and $\sum_{f\in A}|\alpha_f f|_1\le n$.  Write
$w_f:=\alpha_f f$.  Then

1. $\sum_{f\in A}|w_f|_1=n$;
2. there is a closed orthant $O\subseteq\R^r$ with $w_f\in O$ for every
   $f\in A$; equivalently, for each coordinate $i$ the numbers $(w_f)_i$,
   $f\in A$, all have one weak sign.

**Proof.**  $n=|v|_1=\big|\sum_f w_f\big|_1\le\sum_f|w_f|_1\le n$, so both
inequalities are equalities, giving (1).  Equality in the $\ell^1$
triangle inequality is coordinatewise:
$\big|\sum_f (w_f)_i\big|=\sum_f|(w_f)_i|$ for every $i$, which holds
exactly when all $(w_f)_i$ share a weak sign. $\square$

Interpretation: on the boundary sphere the whole mass budget is consumed,
so **no cancellation is available**.  In rank one this is harmless because
the sphere is two points.  In rank $\ge2$ the sphere carries $\Theta(n^{r-1})$
points, and the loss is structural.

### Lemma 2 (sign rigidity)

For $f\in\Z^r\setminus\{0\}$, at most one of $f,-f$ lies in $\Z^r_{\ge0}$.

**Proof.**  If both, then $f\ge0$ and $f\le0$, so $f=0$. $\square$

## 3. Theorem A — lower bound in rank $\ge 2$

> **Theorem A.**  For $r\ge2$ and $n\ge1$,
> \[
>  \dim_r(n)\ \ge\ \big\lceil \log_2(n+1)\big\rceil .
> \]

**Proof.**  Let $F$ linearly generate, $d=|F|$.  For $x=0,1,\dots,n$ put

\[
 v_x:=x\,e_1+(n-x)\,e_2\in I_r(n),\qquad |v_x|_1=n .
\]

Fix a representation $v_x=\sum_{f\in A_x}\alpha^{(x)}_f f$ satisfying (1),
and set $w^{(x)}_f=\alpha^{(x)}_f f$.

*Step 1: the summands are nonnegative.*  By Lemma 1 there are signs
$\varepsilon_i\in\{\pm1\}$ with $\varepsilon_i (w^{(x)}_f)_i\ge0$ for all
$f\in A_x$ and all $i$.  Fix $i$.  If $(v_x)_i>0$ then
$\varepsilon_i(v_x)_i=\sum_f \varepsilon_i (w^{(x)}_f)_i\ge 0$ forces
$\varepsilon_i=+1$.  If $(v_x)_i=0$ then all $(w^{(x)}_f)_i$ share a weak
sign and sum to $0$, hence all vanish, and we may set $\varepsilon_i=+1$
harmlessly.  Since $(v_x)_i\ge0$ for every $i$, we may take
$\varepsilon_i=+1$ for all $i$, i.e.

\[
 w^{(x)}_f\in\Z^r_{\ge0}\qquad\text{for all }f\in A_x .
\]

*Step 2: the signs are not free.*  By Lemma 2, for each $f\in F$ at most
one of $\pm f$ lies in $\Z^r_{\ge0}$.  Hence the sign $\alpha^{(x)}_f$ is
determined by $f$ alone and does not depend on $x$: write it $\sigma(f)$.
Therefore

\[
 v_x=\sum_{f\in A_x}\sigma(f)f ,
\]

so $v_x$ is a function of the **set** $A_x\subseteq F$ only.

*Step 3: counting.*  The map $x\mapsto v_x$ is injective, hence so is
$x\mapsto A_x$.  The $n+1$ values $x=0,\dots,n$ give $n+1$ distinct
subsets of $F$, so $n+1\le 2^{d}$, i.e. $d\ge\log_2(n+1)$.  As $d$ is an
integer, $d\ge\lceil\log_2(n+1)\rceil$. $\square$

## 4. Theorem B — upper bound in every rank

> **Theorem B.**  For every $r\ge1$ and $n\ge1$, with
> $k:=\lceil\log_2(n+1)\rceil$,
> \[
>  \dim_r(n)\ \le\ r\,k ,
> \]
> witnessed by $F=\{\,2^ie_j\ :\ 0\le i<k,\ 1\le j\le r\,\}$.

**Proof.**  Minimality of $k$ gives $2^{k-1}<n+1$, i.e. $2^{k-1}\le n$, so
$|2^ie_j|_1=2^i\le n$ and $F\subseteq I_r(n)$.

Let $v\in I_r(n)$.  For each $j$, $|v_j|\le|v|_1\le n<2^k$, so there is a
unique $S_j\subseteq\{0,\dots,k-1\}$ with $|v_j|=\sum_{i\in S_j}2^i$.
Define $\alpha(2^ie_j):=\mathrm{sign}(v_j)$ for $i\in S_j$ and $0$
otherwise.  Then

\[
 \sum\alpha(f)f=\sum_j \mathrm{sign}(v_j)\,|v_j|\,e_j=v,
\]

and the mass is

\[
 \sum|\alpha(f)f|_1=\sum_j\sum_{i\in S_j}2^i=\sum_j|v_j|=|v|_1\le n .
\]

Both conditions of (1) hold. $\square$

Note the mass is used **exactly**, with no cancellation — which is why the
alphabet is $\{0,1\}$ (base $2$) rather than $\{0,\pm1\}$ (base $3$).

## 5. Corollary C — Riemann–Roch-compatible growth in every rank

In CC's normalisation an archimedean divisor $D=a\{\infty\}$ has
$\deg D=a$ and $n=\lfloor e^a\rfloor$.  Theorems A and B give, for $r\ge2$,

\[
 \frac{\deg D}{\log 2}\ \le\ \dim_r\big(\lfloor e^{\deg D}\rfloor\big)
 \ \le\ \frac{r\,\deg D}{\log 2}+r .
\]

> **Corollary C.**  $\dim_{\spm}M_r$ is $\Theta(\deg D)$ — linear in the
> degree — in **every** rank $r$.

This is the growth a Riemann–Roch formula requires.  In particular the
dimension growth is *not* an obstruction to a Riemann–Roch theorem on a
product.

## 6. Theorem D — the base-$3$ phenomenon is strictly rank one

> **Theorem D.**  For all $n\ge1$ and all $r\ge2$,
> \[
>  \dim_r(n)\ \ge\ \big\lceil\log_2(n+1)\big\rceil
>  \ \ge\ \big\lceil\log_3(2n+1)\big\rceil=\dim_1(n),
> \]
> and
> \[
>  \liminf_{n\to\infty}\frac{\dim_r(n)}{\dim_1(n)}
>  \ \ge\ \frac{\log 3}{\log 2}=1.5849\ldots
> \]
> The inequality is strict for infinitely many $n$ (e.g. $n=4,8,\dots$).

**Proof.**  The first inequality is Theorem A.  For the second it suffices
that $\log_2(n+1)\ge\log_3(2n+1)$, i.e.
$\log 3\cdot\log(n+1)\ge\log 2\cdot\log(2n+1)$.  At $n=1$ both sides equal
$\log2\log3$.  Writing $\phi(n)=\log3\log(n+1)-\log2\log(2n+1)$ one has
$\phi'(n)=\frac{\log3}{n+1}-\frac{2\log2}{2n+1}$, which is $\ge0$ iff
$\log3\,(2n+1)\ge 2\log2\,(n+1)$, i.e.
$n(2\log3-2\log2)\ge 2\log2-\log3$; since $2\log3-2\log2=0.811>0$ and
$2\log2-\log3=0.288$, this holds for all $n\ge1$.  Hence $\phi\ge\phi(1)=0$
for $n\ge1$, and ceilings preserve the inequality.  The ratio statement
follows from $\log_2(n+1)/\log_3(2n+1)\to\log3/\log2$. $\square$

### 6.1 What this means

CC attach an explicit arithmetic meaning to the base $3$ (arXiv:2205.01391,
Introduction):

> "for $p=3$ (and only for this rational prime) the Witt vectors with only
> finitely many non-zero components form a subring inside the ring of
> $p$-adic integers, which turns out to be isomorphic to $\Z$."

Theorem D says this is a **rank-one accident of the mass functional**, not
a feature that transports to products.  The mechanism is Lemma 1: on the
boundary sphere the mass budget is saturated, cancellation is unavailable,
and the digit alphabet collapses

\[
 \spm=\{0,\pm1\}\ \rightsquigarrow\ \{0,1\},
 \qquad\text{base }3\ \rightsquigarrow\ \text{base }2 .
\]

**Prediction.**  Any Riemann–Roch formula for divisors on a product
$\overline{\Spec\Z}\times\overline{\Spec\Z}$, in CC's absolute framework
with the $\ell^1$ mass functional, has normalising constant $\log 2$, not
$\log 3$.  Their one-dimensional formula
$\dim H^0-\dim H^1=\lceil \deg'D+\log'2\rceil'-\mathbf1_L$ with
$\deg'=\deg/\log3$ cannot be the shape of the answer on the square.

## 7. Exact values in rank two, and one open constant

Exhaustive minimisation over all subsets (not a heuristic):

| $n$ | $|I_2(n)|$ | $\lceil\log_3|I_2(n)|\rceil$ | $\dim_2(n)$ exact | $2\lceil\log_2(n+1)\rceil$ |
|---|---|---|---|---|
| 1 | 5 | 2 | **2** | 2 |
| 2 | 13 | 3 | **4** | 4 |
| 3 | 25 | 3 | **4** | 4 |
| 4 | 41 | 4 | **6** | 6 |
| 5 | 61 | 4 | **6** | 6 |
| 6 | 85 | 5 | **6** | 6 |

Two consequences already visible:

* the naive counting bound $\lceil\log_3|I_2(n)|\rceil$, which is **tight**
  in rank one for all $n\le40$, **fails** in rank two from $n=4$ on;
* the exact values agree with the Theorem B bound $2\lceil\log_2(n+1)\rceil$
  throughout.

> **Conjecture.**  $\dim_2(n)=2\lceil\log_2(n+1)\rceil$ for all $n\ge1$.

Status: upper bound proved (Theorem B); lower bound proved only up to the
factor $r$ (Theorem A gives $\lceil\log_2(n+1)\rceil$, not
$2\lceil\log_2(n+1)\rceil$).  A single-orthant refinement does **not**
close the gap: exhaustive search shows the first-quadrant relaxation
admits $6$ generators at $n=8$ while $2\lceil\log_2 9\rceil=8$, e.g.
$\{(0,2),(0,6),(1,1),(2,0),(2,2),(6,0)\}$.  Closing the constant requires
combining two opposite orthants and is left open.

The constant does not affect Corollary C or Theorem D, which are proved
unconditionally.

## 8. Status

Proved, unconditionally, with no zero input:

* Lemma 1 (no cancellation on the boundary sphere) and Lemma 2;
* Theorem A: $\dim_r(n)\ge\lceil\log_2(n+1)\rceil$ for $r\ge2$;
* Theorem B: $\dim_r(n)\le r\lceil\log_2(n+1)\rceil$ for all $r\ge1$;
* Corollary C: $\dim_r=\Theta(\deg D)$ in every rank;
* Theorem D: $\dim_r\ge\dim_1$ with asymptotic ratio $\ge\log3/\log2$;
  the base $3$ does not survive to rank $\ge2$.

Verified computationally:

* CC's rank-one formula (2) reproduced exactly for $n=1,\dots,40$;
* exact rank-two minima for $n=1,\dots,6$;
* Theorem B construction checked for $r=1,2,3$ and $n\le7$, and for $r=2$,
  $n\le39$.

Open:

* the constant in rank two (Conjecture, §7);
* whether the $\ell^1$ mass functional is the right one for a product at
  all.

`107_150` resolves the tensor-norm part of the second item.  The
projective tensor product of two \(\ell^1\) factors is entrywise
\(\ell^1\), not the trace norm; the latter comes from Euclidean factors.
Thus the coordinate-\(\ell^1\) branch is the tensorial continuation of
the published CC mass and remains Riemann--Roch-compatible by the
theorems above.  `107_147` closes only the alternative Euclidean
trace-norm branch.  The open exact constant remains separate.
