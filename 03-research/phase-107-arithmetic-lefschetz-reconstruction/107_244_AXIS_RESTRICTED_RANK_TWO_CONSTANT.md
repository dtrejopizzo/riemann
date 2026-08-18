# 107.244 — The rank-two constant: axis-restricted lower bound and $\dim_2(7)$

## 0. Purpose

107_146 §7 leaves one item open: the exact constant in rank two,

\[
 \Big\lceil\log_2(n+1)\Big\rceil
 \;\le\;\dim_2(n)\;\le\;
 2\Big\lceil\log_2(n+1)\Big\rceil ,
 \tag{0.1}
\]

with the conjecture that the upper bound is exact.  That note also records
why a single-orthant refinement cannot close the gap: at $n=8$ the
first-quadrant relaxation admits the six-element witness
$\{(0,2),(0,6),(1,1),(2,0),(2,2),(6,0)\}$ while $2\lceil\log_23^{\,}9\rceil=8$.

This note does two things: it proves the conjecture on the axis-restricted
class, and it settles $n=7$ exhaustively — the first radius at which the two
natural constructions disagree.

Write $k(n):=\lceil\log_2(n+1)\rceil$ throughout.

## 1. The two constructions diverge at $n=7$

107_146 Theorem B uses the powers-of-two family
$F=\{2^ie_j:0\le i<k\}$, of size $2k$.  An earlier candidate used consecutive
integers $\{1,\dots,c\}$ on each axis with $c(c+1)/2\ge n$.  For $n\le6$ both
give the same size and the exhaustive minima $2,4,4,6,6,6$ do not separate
them.  At $n=7$ they differ: powers of two give $6$, consecutive integers
give $8$.

> ### Theorem 1.1 (exhaustive)
> $\dim_2(7)=6$.

**Proof.**  The upper bound is Theorem B of 107_146 with $k(7)=3$.  For the
lower bound, all subsets of the $56$ sign-representatives of $B_7$ of every
size $3,4,5$ were enumerated and none generates.  Sizes $1,2$ are excluded by
107_146 Theorem A.  The enumeration is reproduced by the verifier. $\square$

So the consecutive-integer family is not optimal, and the powers-of-two value
$2k$ is the correct one at the first radius where the question is decidable
between them.

## 2. The Lemma-1 axis filter

The enumeration above is only feasible because of the following consequence of
107_146 Lemma 1, which prunes the search by two orders of magnitude.

> ### Lemma 2.1 (axis necessity at the poles)
> Let $F$ generate $\|H(\mathbb Z^2)\|_n$.  Then the set
> $X:=\{a>0:(a,0)\in\pm F\}$ has a subset summing to $n$, and likewise
> $Y:=\{b>0:(0,b)\in\pm F\}$.

**Proof.**  The point $(n,0)$ lies on the boundary sphere, so by 107_146
Lemma 1 every representation has mass exactly $n$ and all summands lie in a
common closed orthant; as in the proof of Theorem A that orthant is
$\mathbb Z^2_{\ge0}$.  The second coordinates of the summands are then
nonnegative and sum to $0$, hence all vanish, so every summand lies on the
positive $x$-axis.  Their first coordinates form a subset of $X$ summing to
$n$.  The argument at $(0,n)$ gives the statement for $Y$. $\square$

Applied at $n=7$ this reduced $3\,819\,816$ candidate $5$-subsets to $33\,306$
survivors, a factor of about $115$.

## 3. The axis-restricted class

> ### Theorem 3.1
> Let $F$ generate $\|H(\mathbb Z^2)\|_n$ and suppose every element of $F$
> lies on a coordinate axis.  Then
> \[
>  |F|\;\ge\;2k(n),
> \]
> and equality is attained by the powers-of-two family.  Hence on the
> axis-restricted class the conjectured value is exact:
> \[
>  \boxed{\dim_2^{\rm axis}(n)=2\big\lceil\log_2(n+1)\big\rceil . }
> \]

**Proof.**  Write $X,Y$ as in Lemma 2.1, so $|F|=|X|+|Y|$.  Fix
$x\in\{0,\dots,n\}$ and put $v=(x,n-x)$, so $|v|_1=n$.  By 107_146 Lemma 1
every representation of $v$ has mass exactly $n$ with all summands in a common
closed orthant, and by the argument of 107_146 Theorem A that orthant is
$\mathbb Z^2_{\ge0}$.  The available nonnegative axis summands are $(a,0)$
with $a\in X$ and $(0,b)$ with $b\in Y$.  Comparing coordinates,

\[
 x=\sum_{A_X}a,
 \qquad
 n-x=\sum_{A_Y}b
\]

for subsets $A_X\subseteq X$, $A_Y\subseteq Y$.  As $x$ runs over
$\{0,\dots,n\}$ the subset sums of $X$ contain $\{0,\dots,n\}$, whence
$2^{|X|}\ge n+1$ and $|X|\ge k$.  Simultaneously $n-x$ runs over
$\{0,\dots,n\}$, so $|Y|\ge k$ as well.  Therefore $|F|\ge2k$.

Equality: the family $\{2^ie_j:0\le i<k,\ j=1,2\}$ is axis-supported, has
$2k$ elements, and generates by 107_146 Theorem B. $\square$

### Corollary 3.2 (where a counterexample must live)

Decompose $F$ as $X\sqcup Y\sqcup P_0\sqcup N_0$, where $P_0$ are the
off-axis generators whose two coordinates have equal weak sign (normalised
into the first quadrant) and $N_0$ those of opposite sign (normalised into
the fourth).  If $\dim_2(n)<2k(n)$ for some $n$, then **both** $P_0$ and
$N_0$ are nonempty.

**Proof.**  $P_0=N_0=\emptyset$ is Theorem 3.1.  If exactly one is empty, say
$N_0=\emptyset$, then the fourth-quadrant sphere points $(x,-(n-x))$ admit
only axis summands, and the argument of Theorem 3.1 applied to that segment
gives $|X|,|Y|\ge k$ directly. $\square$

This explains the $n=8$ single-orthant witness of 107_146 §7 rather than
merely recording it: that witness has $P_0=\{(1,1),(2,2)\}$ but
$N_0=\emptyset$, and $X\cup Y=\{2,6\}$ has subset sums $\{0,2,6,8\}$, which do
not cover $\{0,\dots,8\}$.  It therefore fails in the opposite quadrant, as
Corollary 3.2 requires.

The obstruction identified in 107_146 §7 is thus not that one orthant is too
weak, but that the asymmetry between $P_0$ and $N_0$ is the feature to exploit.

## 4. Status

Proved here:

* Theorem 1.1: $\dim_2(7)=6$, by exhaustive enumeration plus 107_146 Thm B;
* Lemma 2.1: the axis necessity at the poles, which makes that enumeration
  feasible;
* Theorem 3.1: the conjecture of 107_146 §7 holds **exactly** on the
  axis-restricted class;
* Corollary 3.2: any counterexample needs off-axis generators in both the
  same-signed and the opposite-signed family.

Still open, and **not** claimed:

* the general lower bound $\dim_2(n)\ge2k(n)$.  Theorem 3.1 covers only
  axis-supported $F$; the counting argument of 107_146 Theorem A gives
  $|X|+|Y|+|P_0|\ge k$ and $|X|+|Y|+|N_0|\ge k$, whose minimum over
  $|F|=|X|+|Y|+|P_0|+|N_0|$ is $k$, not $2k$.  A genuine two-orthant argument
  is still missing;
* the constant in rank $r\ge3$;
* nothing here bears on any row status, which is unchanged.

## 5. Verifier

`107_244_axis_restricted_rank_two_constant.py` checks: the axis-restricted
minimum equals $2k(n)$ by exhaustive enumeration for $n=1,\dots,12$; that the
powers-of-two family generates for $n\le39$; that Lemma 2.1 is a valid
necessary condition; the exhaustive nonexistence of a generating set of size
$<6$ at $n=7$; and that the bound $6$ is attained.
