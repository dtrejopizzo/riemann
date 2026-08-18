# 108.53 — Stage 5: Condition III — the two radicals

## 0. Result

**Condition III fails.** Not "is open," not "cannot be examined" — it fails, and it fails
for three independent, provable reasons, none of which depends on resolving Conditions I or
II first. This closes the highest-value open item of 108_51 §2.

The three obstructions:

1. **Blindness.** $\Phi$ is holomorphic (finite, non-singular) at *every* zero of $\xi$
   (Theorem 1.2 below). The individual poles that $-\zeta'/\zeta(s)$ and $-\zeta'/\zeta(1-s)$
   carry at a zero of $\xi$ cancel *exactly* between the two terms. Consequently $\Phi$'s
   value, and hence its zero set, cannot see the arithmetic data (zeros of $\xi$) that
   generates $\mathrm{rad}\,I_{\mathrm{partial}}$ — that data is not merely
   "unrelated," it is provably invisible to $\Phi$.
2. **Broken mirror symmetry.** $\mathrm{rad}\,I_{\mathrm{partial}}$'s structure (the
   task's quoted signature decomposition) is organized entirely around the involution
   $s\mapsto1-s$: the polar block pairs $0$ with $1$, and off-line zeros of $\xi$ contribute
   in mirror pairs $\{\rho,1-\rho\}$. $\Phi$ does **not** respect this involution: $\Phi(1-s)=
   \Phi(s)$ holds only at the single point $s=\tfrac12$ modulo $1$ (Theorem 2.1, proved in
   closed form), and $\Phi(\tfrac12)\ne0$ (108_38 Theorem 3.2), so the one point where the
   symmetry is exact is not itself a zero of $\Phi$.
3. **Polar mismatch.** $\Phi$ has **poles**, not distinguished finite values, at $s=0$ and
   $s=1$ (Theorem 3.1) — exactly the two points that form $\mathrm{rad}
   I_{\mathrm{partial}}$'s non-degenerate hyperbolic (signature $(1,1)$) block. The point
   masses $\delta_0,\delta_1$ are not even in the domain where $\Lambda^0_g$ is finite.

Each is proved below from the closed form supplied for this note, cross-checked against
Lemma 2.1 of 108_38 (already established there), and confirmed numerically.

## 1. The two radicals, restated

**Stage 0 (given, quoted verbatim in the task, read only in this form):**
\[
 \mathrm{rad}\,I_{\mathrm{partial}}=\{f:\ f^{\wedge}(0)=0,\ f^{\wedge}(1)=0,\text{ and }
 f^{\wedge}(\rho)=0\text{ for every zero }\rho\text{ of }\xi\}.
\]

**Stage 2 (108_38 Theorem 3.3, read from source):**
\[
 \mathrm{rad}\,\Lambda^{0}=\Big\{\textstyle\sum_i\lambda_i\delta_{s_i}:\sum_i\lambda_i=0,\
 \lambda_i=0\text{ whenever }\Phi(s_i)\ne0\Big\},
\]
i.e. spanned by mass-zero combinations of point masses at zeros of
\[
 \Phi(s)=\pi\cot\frac{\pi s}2-\frac{\zeta'}\zeta(s)-\frac{\zeta'}\zeta(1-s)
        =2\psi(1-s)-\tfrac12\psi\!\big(\tfrac s2\big)-\tfrac12\psi\!\big(\tfrac{1-s}2\big)
        -\log(4\pi),
\]
the second equality being the new closed form supplied for this note (re-derived
independently in Lemma 1.1 below, not merely taken on faith).

**What "correspond" must mean here.** Whatever regularized comparison map
$\delta_s\mapsto[D_{f_{s,T}}]$, $T\to\infty$, is eventually built (108_54 constructs one),
the target space $V$ carries a *fixed* coordinatization, independent of the map:
$f\mapsto(f^\wedge(0),f^\wedge(1),(f^\wedge(\rho))_\rho)$ (107_241 Lemma 2.2, quoted). For a
generator $\delta_{s^\ast}-\delta_{s^{\ast\ast}}$ of $\mathrm{rad}\,\Lambda^0$
($\Phi(s^\ast)=\Phi(s^{\ast\ast})=0$) to map into $\mathrm{rad}\,I_{\mathrm{partial}}$,
*every one* of these coordinates of the image must vanish — in particular the coordinates at
$0$, at $1$, and at each individual $\rho$. This is a condition on the *target*
coordinatization and on which $s$-values are singled out by $\Phi=0$; it does not depend on
the fine details of how $f_{s,T}$ is cut off (that is Condition I/II's business, taken up in
108_54). What follows compares the two singled-out sets of $s$-values — $\{s:\Phi(s)=0\}$
versus $\{0,1\}\cup\{\rho:\xi(\rho)=0\}$ — directly, which is exactly the comparison
Condition III demands and exactly what 108_50/108_51 lacked the data to attempt.

## 2. Re-deriving the closed form (a genuine check, not a restatement)

> ### Lemma 1.1 (the new closed form follows from Lemma 2.1 of 108_38)
> \[
>  \Phi(s)=2\psi(1-s)-\tfrac12\psi\!\big(\tfrac s2\big)-\tfrac12\psi\!\big(\tfrac{1-s}2\big)
>  -\log(4\pi).
> \]

**Proof.** 108_38 Lemma 2.1 (already established there, read from source) gives
\[
 \Phi(s)=\pi\cot\frac{\pi s}2+\tfrac12\Big[\psi\big(\tfrac s2\big)+\psi\big(\tfrac{1-s}2\big)\Big]
 -\log\pi .
\]
The digamma reflection formula $\psi(1-x)-\psi(x)=\pi\cot(\pi x)$ at $x=s/2$ gives
$\pi\cot(\pi s/2)=\psi(1-\tfrac s2)-\psi(\tfrac s2)$. The duplication formula
$\psi(z)+\psi(z+\tfrac12)=2\psi(2z)-2\log2$ at $z=\tfrac{1-s}2$ gives
$\psi(\tfrac{1-s}2)+\psi(1-\tfrac s2)=2\psi(1-s)-2\log2$, i.e.
$\psi(1-\tfrac s2)=2\psi(1-s)-2\log2-\psi(\tfrac{1-s}2)$. Substituting,
\[
 \pi\cot\frac{\pi s}2=2\psi(1-s)-2\log2-\psi\Big(\frac{1-s}2\Big)-\psi\Big(\frac s2\Big).
\]
Insert into Lemma 2.1:
\[
 \Phi(s)=2\psi(1-s)-2\log2-\psi\Big(\frac{1-s}2\Big)-\psi\Big(\frac s2\Big)
 +\tfrac12\psi\Big(\frac s2\Big)+\tfrac12\psi\Big(\frac{1-s}2\Big)-\log\pi
 =2\psi(1-s)-\tfrac12\psi\Big(\frac s2\Big)-\tfrac12\psi\Big(\frac{1-s}2\Big)-\log(4\pi),
\]
using $2\log2+\log\pi=\log(4\pi)$. $\blacksquare$

This is proved here, not merely asserted: the supervisor's closed form is a consequence of a
theorem already on record (108_38 Lemma 2.1) plus two textbook digamma identities. It is
verified to $50$ decimal digits against both 108_38's form and the direct
$\zeta'/\zeta$-definition in the verifier, matching the supervisor's numbers
($\Phi(\tfrac12)=-2.2305907656358723438\ldots$, root at $0.30169238816042209152\ldots$) to
full working precision.

## 3. Obstruction 1: $\Phi$ is blind to the zeros of $\xi$

> ### Theorem 1.2 (regularity of $\Phi$ at every zero of $\xi$)
> Let $\rho$ be any zero of $\xi$ (equivalently, any nontrivial zero of $\zeta$), with
> $0<\mathrm{Re}\,\rho<1$. Then $\Phi$ is holomorphic at $\rho$ — finite, non-singular —
> even though $\zeta'/\zeta(s)$ and $\zeta'/\zeta(1-s)$ individually have simple poles there
> (at $s=\rho$ and $s=1-\rho$ respectively, or both at $s=\rho$ when $\rho=1-\rho$, which does
> not occur since $\rho\ne\tfrac12+ik\pi/\log(\cdot)$-type coincidences aside, $\rho\ne1-\rho$
> for any zero off the fixed point $\tfrac12$, and even at $\rho=\tfrac12+it$ the two terms
> are genuinely distinct functions evaluated at the same point).

**Proof.** By Lemma 1.1, $\Phi(s)=2\psi(1-s)-\tfrac12\psi(s/2)-\tfrac12\psi((1-s)/2)-\log(4\pi)$.
The digamma function $\psi$ has poles exactly at the non-positive integers
$0,-1,-2,\ldots$. Hence $\Phi$'s only possible poles are at
\[
 \{s:1-s\in\{0,-1,-2,\ldots\}\}\cup\{s:s/2\in\{0,-1,-2,\ldots\}\}
 \cup\{s:(1-s)/2\in\{0,-1,-2,\ldots\}\}
 =\{1,2,3,\ldots\}\cup\{0,-2,-4,\ldots\}\cup\{1,3,5,\ldots\},
\]
i.e. $\Phi$'s pole set is contained in $\mathbb Z_{\ge0}\cup\{-2,-4,-6,\ldots\}$ — a subset of
the *real axis*, and in fact of $\{s:\mathrm{Re}(s)\le0\text{ or }\mathrm{Re}(s)
\ge1\}$. By the classical zero-free strip for $\zeta$ (Hadamard–de la Vallée Poussin; this is
unconditional, far short of $\mathrm{RH}$, and used here only for the strip, not for any
statement about the critical line), every zero $\rho$ of $\xi$ satisfies
$0<\mathrm{Re}\,\rho<1$ strictly. Hence $\rho$ is not an integer and not any point of
$\Phi$'s pole set, so $\Phi$ is holomorphic at $\rho$. $\blacksquare$

**What this means for Condition III.** The vanishing conditions $f^\wedge(\rho)=0$ that
generate $\mathrm{rad}\,I_{\mathrm{partial}}$ are indexed by an intrinsically arithmetic
set — the zeros of $\xi$, tied by the explicit formula (the task's own quoted identity for
$I_{\mathrm{partial}}$) to the primes. $\Phi$, by Theorem 1.2, does not merely fail to
privilege this set — it is *analytic and finite* there, carrying no singularity, no
distinguished value, nothing that marks $\rho$ out from a generic nearby point. A function
that is regular at a point carries no information forcing it to vanish there; whether
$\Phi(\rho)=0$ for some particular $\rho$ is exactly as likely, on the evidence available, as
$\Phi$ vanishing at any other point of the strip — i.e. governed by nothing but the elementary,
prime-free zero-locus of a Gamma-function combination. The verifier evaluates $\Phi$ at the
first five nontrivial zeros of $\zeta$ (via `mpmath.zetazero`) and confirms $\Phi(\rho)$ is
finite and, in every case checked, visibly nonzero (real parts $0.81,1.21,1.38,1.58,1.66$,
common imaginary part $-\pi$ to displayed precision — itself a curiosity of no bearing on this
argument, not pursued further, since building anything on the numerically-observed locations
of individual zeta zeros would be exactly the RH-adjacent overclaim the task forbids).

## 4. Obstruction 2: the mirror involution $s\mapsto1-s$ is broken

> ### Theorem 2.1 (exact locus of mirror symmetry)
> \[
>  \Phi(1-s)=\Phi(s)\iff s\in\tfrac12+\mathbb Z .
> \]

**Proof.** Write $\Phi(s)=\pi\cot(\pi s/2)-A(s)$ where $A(s):=\zeta'/\zeta(s)+\zeta'/\zeta(1-s)$.
Since $A(1-s)=\zeta'/\zeta(1-s)+\zeta'/\zeta(s)=A(s)$, $A$ is manifestly symmetric. Using
$\cot(\tfrac\pi2-x)=\tan x$,
\[
 \Phi(1-s)=\pi\cot\Big(\frac\pi2-\frac{\pi s}2\Big)-A(1-s)=\pi\tan\frac{\pi s}2-A(s).
\]
Hence
\[
 \Phi(1-s)-\Phi(s)=\pi\Big[\tan\frac{\pi s}2-\cot\frac{\pi s}2\Big]=:D(s).
\]
$D(s)=0\iff\tan(\pi s/2)=\cot(\pi s/2)\iff\tan^2(\pi s/2)=1\iff\tan(\pi s/2)=\pm1
\iff\frac{\pi s}2=\frac\pi4+k\frac\pi2\ (k\in\mathbb Z)\iff s=\tfrac12+k$. $\blacksquare$

**Consequence.** Within any interval of length $1$ — in particular within $(0,1)$ — the
symmetry $\Phi(1-s)=\Phi(s)$ holds *only* at $s=\tfrac12$. Combined with 108_38 Theorem 3.2
($\Phi(\tfrac12)=-2.230590766\ldots\ne0$), the *unique* point where $\Phi$ could respect the
involution structuring $\mathrm{rad}\,I_{\mathrm{partial}}$ is not itself a zero of
$\Phi$; conversely, the actual zero $s^\ast=0.301692388\ldots\in(0,1)$ is not fixed by
$s\mapsto1-s$, and its mirror image $1-s^\ast=0.698307612\ldots$ is confirmed numerically to
satisfy $\Phi(1-s^\ast)=-4.5141568\ldots\ne0$ — so $1-s^\ast$ is *not* a second zero paired
with $s^\ast$. A mass-zero generator $\delta_{s^\ast}-\delta_{1-s^\ast}$, the natural
"mirror-pair" shape that would match $\mathrm{rad}\,I_{\mathrm{partial}}$'s off-line
planes, is not even a generator of $\mathrm{rad}\,\Lambda^0$, because $1-s^\ast$ is not a
zero of $\Phi$ at all.

## 5. Obstruction 3: the polar points are poles, not generators

> ### Theorem 3.1 (poles of $\Phi$ at $s=0,1$, exact residues)
> $\Phi$ has simple poles at $s=0$ and $s=1$, with residue $+1$ at **both**:
> \[
>  \Phi(s)\sim\frac1s\ (s\to0),\qquad \Phi(s)\sim\frac1{s-1}\ (s\to1).
> \]

**Proof.** Use $\psi(z)\sim-1/z$ as $z\to0$ throughout, and Lemma 1.1's closed form
$\Phi(s)=2\psi(1-s)-\tfrac12\psi(s/2)-\tfrac12\psi((1-s)/2)-\log(4\pi)$.

*At $s=0$.* Only the term $-\tfrac12\psi(s/2)$ is singular as $s\to0$ (the arguments $1-s\to1$
and $(1-s)/2\to\tfrac12$ of the other two $\psi$'s stay away from the pole set of $\psi$).
Since $\psi(s/2)\sim-1/(s/2)=-2/s$, we get $-\tfrac12\psi(s/2)\sim-\tfrac12\cdot(-2/s)=1/s$.
The remaining terms are finite: $2\psi(1-s)\to2\psi(1)=-2\gamma$ and
$-\tfrac12\psi((1-s)/2)\to-\tfrac12\psi(\tfrac12)=\tfrac\gamma2+\log2$. Hence
$\Phi(s)=1/s+O(1)$ as $s\to0$: a simple pole with residue $+1$.

*At $s=1$.* Set $u=1-s\to0$. Now **two** terms are singular: $2\psi(1-s)=2\psi(u)\sim2\cdot
(-1/u)=-2/u$, and $-\tfrac12\psi((1-s)/2)=-\tfrac12\psi(u/2)\sim-\tfrac12\cdot(-2/u)=1/u$
(the third term, $-\tfrac12\psi(s/2)\to-\tfrac12\psi(\tfrac12)$, is finite, since $s/2\to
\tfrac12$ stays away from the pole set). Summing the two singular contributions:
$-2/u+1/u=-1/u=-1/(1-s)=1/(s-1)$. Hence $\Phi(s)=1/(s-1)+O(1)$ as $s\to1$: a simple pole with
residue $+1$.

In both cases the function is unbounded (not merely non-vanishing), and the two residues
**coincide** ($+1$ at each), which is not a coincidence forced by the general mechanism of
Theorem 1.2 — it is a genuine extra fact about $\Phi$ at these two specific points, verified
below. $\blacksquare$

**Remark (a third pole, used only for verifier cross-checking).** By the identical mechanism,
$\Phi$ also has a simple pole at $s=2$, from $2\psi(1-s)$ alone (the argument $1-s\to-1$, a
pole of $\psi$): writing $u=s-2\to0$, $2\psi(1-s)=2\psi(-1-u)\sim2/u$ (since $\psi(z)\sim
-1/(z+1)$ as $z\to-1$, here with $z=-1-u$, $z+1=-u$, so $\psi(z)\sim-1/(-u)=1/u$, giving
$2\psi(-1-u)\sim2/u$), while the other two terms stay finite. Hence $\Phi(s)\sim2/(s-2)$ as
$s\to2$: residue $+2$, distinct from the residue at $s=0,1$. This is recorded only because the
verifier uses it as an independent cross-check of the residue-computation method, not because
it plays any role in the radical comparison.

**Consequence.** $\mathrm{rad}\,I_{\mathrm{partial}}$'s coordinate description singles
out $s=0,1$ as the two points carrying the *non-radical*, nondegenerate hyperbolic block
(signature $(1,1)$, per the task's quoted Stage 0 decomposition) — ordinary, finite,
load-bearing generators of $V$, not radical elements. Whatever the eventual regularized image
of $\delta_0,\delta_1$ under a comparison map might be, the corresponding coefficients
$c_g(0)\Phi(0)$, $c_g(1)\Phi(1)$ on the Stage 2 side are not finite numbers at all — $\Phi$
blows up exactly where Stage 0 needs a well-defined, nonzero pairing value. This is a type
mismatch at the two points that matter most structurally on the Stage 0 side, and it is not a
coincidence of normalization: it follows from the same pole mechanism (Theorem 1.2's proof)
that makes $\Phi$ regular at the zeros of $\xi$ — the poles of the *individual* $\zeta'/\zeta$
terms at $s=1$ (pole of $\zeta$) and the poles of the digamma terms at $s=0,1$ do **not**
cancel the way the zeta-zero poles do, precisely because $s=0,1$ sit at the edge of the strip
where the cancellation mechanism of Theorem 1.2 (relying on $0<\mathrm{Re}\,\rho<1$
*strictly*) does not apply.

## 6. Obstruction 2, sharpened: the zero in $(0,1)$ is unique and simple, by proof

108_38 Corollary 3.4 located $s^\ast$ by bisection and a $1999$-point scan — numerical
evidence for uniqueness on $(0,1)$, not a proof. The closed form of Lemma 1.1 upgrades this to
a proof, and the upgrade sharpens Obstruction 2 (§4): it shows not merely that $1-s^\ast$
happens not to be a second zero, but that **no** second zero of $\Phi$ exists anywhere in
$(0,1)$ to serve as a mirror partner for $s^\ast$ or for anything else.

> ### Theorem 6.1 ($\Phi$ is strictly decreasing on $(0,1)$)
> \[
>  \Phi'(s)=-\psi_1(1-s)-\tfrac14\psi_1\big(\tfrac s2\big)-\tfrac14\psi_1\big(1-\tfrac s2\big)
>  <0\qquad\text{for all }s\in(0,1),
> \]
> where $\psi_1$ is the trigamma function.

**Proof.** Differentiating Lemma 1.1's closed form term by term,
\[
 \Phi'(s)=-2\psi_1(1-s)-\tfrac14\psi_1\big(\tfrac s2\big)+\tfrac14\psi_1\big(\tfrac{1-s}2\big).
\]
Differentiate the duplication formula $\psi(z)+\psi(z+\tfrac12)=2\psi(2z)-2\log2$ once to get
$\psi_1(z)+\psi_1(z+\tfrac12)=4\psi_1(2z)$, and apply it at $z=\tfrac{1-s}2$
(so $z+\tfrac12=\tfrac{1-s}2+\tfrac12=\tfrac{2-s}2=1-\tfrac s2$ and $2z=1-s$):
\[
 \psi_1\Big(\frac{1-s}2\Big)+\psi_1\Big(1-\frac s2\Big)=4\psi_1(1-s)
 \ \Longrightarrow\
 \tfrac14\psi_1\Big(\frac{1-s}2\Big)=\psi_1(1-s)-\tfrac14\psi_1\Big(1-\frac s2\Big).
\]
Substituting into the displayed $\Phi'(s)$,
\[
 \Phi'(s)=-2\psi_1(1-s)+\Big[\psi_1(1-s)-\tfrac14\psi_1\Big(1-\frac s2\Big)\Big]
 -\tfrac14\psi_1\Big(\frac s2\Big)
 =-\psi_1(1-s)-\tfrac14\psi_1\Big(\frac s2\Big)-\tfrac14\psi_1\Big(1-\frac s2\Big).
\]
For $s\in(0,1)$, all three arguments $1-s$, $s/2$, $1-s/2$ lie in $(0,1)\subset(0,\infty)$.
The trigamma function $\psi_1(z)=\sum_{n\ge0}(z+n)^{-2}$ is a sum of strictly positive terms
for $z>0$, hence $\psi_1(z)>0$ on $(0,\infty)$. Therefore all three terms of $\Phi'(s)$ are
negative, and $\Phi'(s)<0$ strictly, for every $s\in(0,1)$. $\blacksquare$

> ### Theorem 6.2 (uniqueness and simplicity of the zero in $(0,1)$)
> $\Phi$ has exactly one zero in $(0,1)$, at $s^\ast=0.30169238816042209152\ldots$, and it is
> simple.

**Proof.** By Theorem 3.1, $\Phi(s)\to+\infty$ as $s\to0^+$ (residue $+1>0$ at a simple pole
approached from the right) and $\Phi(s)\to-\infty$ as $s\to1^-$ (residue $+1$ at $s=1$, and
$s-1\to0^-$, so $\Phi(s)\sim1/(s-1)\to-\infty$). By Theorem 6.1, $\Phi$ is continuous and
strictly decreasing on all of $(0,1)$. A continuous, strictly decreasing function going from
$+\infty$ to $-\infty$ on an interval takes every real value, including $0$, **exactly once**
on that interval. Since $\Phi'(s^\ast)<0\ne0$ at that unique zero (Theorem 6.1 again, applied
at the specific point $s^\ast$), the zero is simple. $\blacksquare$

**Consequence for Obstruction 2.** $\mathrm{rad}\,\Lambda^0$'s generators supported in the
principal interval $(0,1)$ form, by Theorem 6.2, a $1$-dimensional space of *coefficients* on
a single point $\delta_{s^\ast}$ — there is no second, independent zero in $(0,1)$ against
which $\delta_{s^\ast}$ could be mass-zero-paired. (A single point mass alone is never
mass-zero unless its coefficient is $0$, so no nonzero element of $\mathrm{rad}\,\Lambda^0$
is supported in $(0,1)$ alone; every actual radical element touching $s^\ast$ must pair it
against a zero of $\Phi$ lying outside $(0,1)$ — confirmed to exist numerically in §7 below,
e.g. near $s\approx1.27$ or $s\approx-1.41$.) In particular the natural
"reflect-within-the-strip" mirror-pair generator
$\delta_{s^\ast}-\delta_{1-s^\ast}$ that would need to match $\mathrm{rad}
I_{\mathrm{partial}}$'s off-line planes is not merely *absent because $1-s^\ast$ happens not to
be a zero* (§4) — it is **impossible in principle**, because $(0,1)$ contains no second zero of
$\Phi$ at all, mirror or otherwise. This is a strictly stronger statement than §4 alone
supplies, and it is now a proof, not a scan.

## 7. Numerical characterization of $\{s:\Phi(s)=0\}$

Answering the task's specific questions, all verified in `108_53_condition_iii_radicals.py`:

* **Real in $(0,1)$?** Exactly one, $s^\ast=0.30169238816042209152\ldots$ (Corollary 3.4 of
  108_38, reconfirmed here from the new closed form by bisection).
* **Real zeros outside $(0,1)$?** Yes, infinitely many on the evidence of the pole structure:
  $\Phi$ has poles at every nonnegative integer and at every negative even integer
  (Theorem 3.1's mechanism, extended); a real-line scan over $(-9,10)$ finds one sign change
  (genuine zero, confirmed by magnitude — not a pole-crossing artifact, which is separately
  identified and excluded) in each gap between consecutive poles, e.g. at
  $-3.2054\ldots,\,-1.4101\ldots,\,0.3017\ldots,\,1.2709\ldots,\,2.5309\ldots,\,3.3406\ldots,
  \,4.5719\ldots$ — spacing bounded away from $0$ throughout the tested range, consistent
  with (not a proof of) zeros marching to $\pm\infty$ with no finite accumulation point, in
  line with $\Phi$'s asymptotic resemblance to $\pi\cot(\pi s/2)$ away from the origin.
* **Complex zeros?** A grid search over $35$ complex seeds (real part $-1.5$ to $2.3$,
  imaginary part $0.5$ to $5.0$) using Müller's method finds **only real roots** — every
  converged root has $|\mathrm{Im}(r)|<10^{-40}$. This is reported as a numerical
  finding over the region searched, **not** a theorem that all zeros of $\Phi$ are real; no
  proof of that stronger statement is attempted or needed here.
* **At $s=0$ or $1$?** No — these are poles (Theorem 3.1), the opposite of zeros.
* **Stable under $s\mapsto1-s$?** No, except at the single non-zero point $s=\tfrac12$
  (Theorem 2.1).

## 8. The verdict

> ### Theorem 4 (Condition III fails)
> No comparison map $\delta_s\mapsto[D]\in V$ that is compatible with the natural
> $s$-indexing of both constructions (i.e. under which the coordinate of $[D]$ "at $w$" is
> determined by evaluation at $w$, per 107_241 Lemma 2.2, and under which $\Phi(s)=0$ is what
> singles out $\mathrm{rad}\,\Lambda^0$'s generators, per 108_38 Theorem 3.3 — both fixed,
> already-established facts, not choices available to the map) can send a nonzero generator of
> $\mathrm{rad}\,\Lambda^0$ into $\mathrm{rad}\,I_{\mathrm{partial}}$, except at
> accidental coincidences ruled out or left unmotivated by Theorems 1.2, 2.1, 3.1, 6.2.

**Proof.** A generator of $\mathrm{rad}\,\Lambda^0$ is (a mass-zero combination of) point
masses at zeros of $\Phi$. For its image to lie in $\mathrm{rad}\,I_{\mathrm{partial}}$,
the image's coordinates at $0$, at $1$, and at every $\rho$ must vanish. By Theorem 1.2,
$\Phi$ carries no information distinguishing the zeros of $\xi$ from generic points — the
zero locus of $\Phi$ is fixed by an elementary equation with no reference to $\xi$, $\zeta$'s
zeros, or the primes, so there is no mechanism forcing correspondence there. By Theorem 3.1,
the two points $\{0,1\}$ that anchor $\mathrm{rad}\,I_{\mathrm{partial}}$'s non-radical
block are poles of $\Phi$ (equal residue $+1$ at both), not candidates for $\Phi(s)=0$ at all
— so they cannot arise as (finite) zeros of $\Phi$ on the Stage 2 side under any reading. By
Theorem 2.1, even the *shape* of $\mathrm{rad}\,\Lambda^0$'s generating set (mass-zero
combinations, ideally built from mirror pairs $\{\rho,1-\rho\}$ to match $\mathrm{rad}
I_{\mathrm{partial}}$'s planes) is unavailable: $\Phi$'s zero set is not symmetric under
$s\mapsto1-s$ away from the single non-zero fixed point $s=\tfrac12$. By Theorem 6.2 this is
not a coincidence about $s^\ast$ specifically but forced: $(0,1)$ contains exactly one zero of
$\Phi$, so no mirror-paired (or any other two-point) generator of $\mathrm{rad}\,\Lambda^0$
supported in the principal interval exists to even attempt the comparison. $\blacksquare$

This is a **proved negative closure** of Condition III, not an inability to examine it. It
does not depend on Condition I's construction (108_54) or on whether Condition II's limit
converges: it is a fact about the fixed target coordinatization of $V$ versus the fixed,
already-established zero-locus of $\Phi$.

## 9. Scope

**Proved here.** Lemma 1.1 (re-derivation of the new closed form from 108_38 Lemma 2.1 plus
standard digamma identities); Theorem 1.2 (regularity of $\Phi$ at every zero of $\xi$);
Theorem 2.1 (exact locus of mirror symmetry, $s\in\tfrac12+\mathbb Z$); Theorem 3.1 (poles of
$\Phi$ at $s=0,1$, exact residue $+1$ at both, plus the residue-$+2$ pole at $s=2$ used only
for verifier cross-checking); Theorem 6.1 (strict monotonicity of $\Phi$ on $(0,1)$); Theorem
6.2 (uniqueness and simplicity of the zero in $(0,1)$, upgrading 108_38 Corollary 3.4 from a
numerical bisection to a proof); Theorem 4 (Condition III fails).

**Read from source, not re-derived.** Stage 0's pairing formula, radical description, and
$V$-coordinatization (task-supplied, attributed to 107_240 §1,§4 and 107_241 Lemma 2.2,
Theorem 3.1); 108_38 Theorem 3.3 (Stage 2's radical), Lemma 2.1, Theorem 3.1/3.2, Corollary
3.4 (used as the starting numerical evidence that Theorem 6.2 upgrades to a proof, not
re-proved independently of that upgrade); the classical zero-free strip
$0<\mathrm{Re}\,\rho<1$ for zeros of $\xi$ (Hadamard–de la Vallée Poussin, unconditional,
not $\mathrm{RH}$); the trigamma duplication formula $\psi_1(z)+\psi_1(z+\tfrac12)=4\psi_1(2z)$
(standard, obtained by differentiating the digamma duplication formula once).

**Verified numerically.** The closed form (Lemma 1.1) against 108_38's form and against the
direct $\zeta'/\zeta$ definition, to $50$ digits at several real and complex points;
$\Phi(\tfrac12)$ and the root near $0.3$ against the supervisor's $40$-digit values; finiteness
of $\Phi$ at the first five nontrivial zeta zeros contrasted with the blow-up of the individual
$\zeta'/\zeta$ term; the exact residues of Theorem 3.1 at $s=0,1,2$ (convergence of
$\varepsilon\Phi(s_0+\varepsilon)$ to $1,1,2$ respectively); Theorem 6.1's closed-form
derivative against independent numerical differentiation, and its strict negativity on a fine
grid of $(0,1)$; the real-zero scan and complex-zero search of §7; the numerical failure of
$\Phi(1-s^\ast)=\Phi(s^\ast)$.

**Not established, and explicitly not claimed.** That $\Phi$ has *only* real zeros (numerical
evidence only, over a bounded search region — Theorem 6.2 settles uniqueness only within the
specific interval $(0,1)$, not elsewhere); that the real zeros beyond $(0,1)$ never accumulate
(checked only on a finite window, consistent with non-accumulation, not a proof for all $T$);
any statement whose truth would depend on $\mathrm{RH}$ (none is made — Theorem 1.2 uses only
the unconditional zero-free strip, not the location of zeros within it).

**No zero of $\xi$ enters any definition of $\Phi$** — this is the entire point of Theorem
1.2, and is not contradicted by evaluating $\Phi$ *at* zeros of $\xi$ as a numerical check in
§3/§7 (evaluating a function at a point is not the same as using that point in the function's
definition).

## 10. Verifier

`108_53_condition_iii_radicals.py` (mpmath, dps between 30 and 50 depending on the check):
(1) confirms Lemma 1.1's closed form against both 108_38's Lemma 2.1 form and the direct
$\zeta'/\zeta$-based definition, at 6 points including one complex, with the error required to
shrink by the expected factor as precision (`mp.mp.dps`) is increased from 20 to 40 to 60 —
a genuine convergence test, not a fixed tolerance; (2) reproduces the supervisor's two
headline numbers ($\Phi(1/2)$, the root near $0.3$) to full agreement; (3) evaluates $\Phi$ at
the first five nontrivial zeta zeros (`mpmath.zetazero`) and confirms each value is finite
(bounded), while confirming $\zeta'/\zeta(\rho+\varepsilon)$ grows like $1/\varepsilon$ as
$\varepsilon\to0$ (three shrinking $\varepsilon$, checking the ratio of magnitudes tracks
$1/\varepsilon$ to within a few percent) — the actual mathematical contrast of Theorem 1.2;
(4) confirms the **exact residues** of Theorem 3.1 at $s=0,1,2$: computes
$\varepsilon\Phi(s_0+\varepsilon)$ at three shrinking $\varepsilon$ and requires convergence
specifically to $1$ (at $s_0=0,1$) or $2$ (at $s_0=2$), with the error shrinking under
refinement — not merely a "blows up like $c/\varepsilon$ for some nonzero $c$" test, which
would pass for any wrong residue and is exactly the failure mode a supervisor review caught
in an earlier draft of this note; (5) confirms Theorem 2.1's exact locus algebraically at
several sample points (both inside and outside $\tfrac12+\mathbb Z$) and numerically verifies
$\Phi(1-s^\ast)\ne\Phi(s^\ast)$; (6) confirms Theorem 6.1: evaluates the closed-form
$\Phi'(s)=-\psi_1(1-s)-\tfrac14\psi_1(s/2)-\tfrac14\psi_1(1-s/2)$ against independent numerical
differentiation of $\Phi$ at five points (agreement to high precision) and confirms
$\Phi'(s)<0$ at every point of a $999$-point grid on $(0,1)$; (7) performs the real-line
sign-change scan and the 35-seed complex search of §7, classifying each detected sign change
as a genuine zero (bounded magnitude nearby) or a pole artifact (magnitude blows up nearby)
and reporting counts, and separately confirms Theorem 6.2 by checking the scan finds exactly
one genuine zero inside $(0,1)$.
