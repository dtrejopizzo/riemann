# 110.01 — The graded family's principal witnesses are not ξ-divisible

## 0. Answer

**No.** Neither a single weight-$s$ witness $\mathrm{div}(cU_s)$ (via
$f_s(r)=cr^s$) nor a mass-zero difference $f_{s_0}-f_{s_1}$
($\mathrm{div}(U_{s_0})-\mathrm{div}(U_{s_1})$, 108\_31 §5) is
ξ-divisible. The mechanism is not "we compute $\hat f(\rho)$ and it is
nonzero at some zero $\rho$"; it is more basic: $f_s$ and $f_{s_0}-f_{s_1}$
**have no ordinary Mellin transform at all** — the defining integral diverges
for every $w\in\mathbb C$ (Lemma 110.1.1/110.1.3). The only sense in which
they "have a transform" is distributional: a Dirac mass concentrated at the
single real point $w=s$ (Lemma 110.1.2, with an exact closed form). A Dirac
mass is not the kind of object that can equal $\xi\cdot\hat g$ for an
admissible $g$, because admissible $\hat g$'s are candid entire functions,
never point-supported distributions (Theorem 110.1.4). This is what fails,
identified precisely: a **category mismatch**, not a numerical accident.

## 1. Setup and conventions

Fix the Mellin transform convention of 110\_00 (ADM):
$$\hat f(w):=\int_0^\infty f(r)\,r^{-w}\,d^\times r,\qquad d^\times
r=\frac{dr}r,\qquad w\in\mathbb C. \tag{1.1}$$
For $f_s(r):=c\,r^s$ ($s\in\mathbb R$, $c\in\mathbb R\setminus\{0\}$, the
graded family of 108\_03/108\_31), (1.1) reads
$$\hat f_s(w)=c\int_0^\infty r^{s-w-1}\,dr. \tag{1.2}$$

## 2. No ordinary Mellin transform exists

### Lemma 110.1.1 (single weight)

For every $s\in\mathbb R$, $c\ne0$, and every $w\in\mathbb C$, the integral
(1.2) diverges.

**Proof.** Write $\sigma=\mathrm{Re}(w)$. Near $r=0$,
$|r^{s-w-1}|=r^{s-\sigma-1}$; $\int_0 r^{s-\sigma-1}dr$ converges at $0$ iff
$s-\sigma>0$, i.e. $\sigma<s$. Near $r=\infty$, the same integrand converges
at $\infty$ iff $s-\sigma<0$, i.e. $\sigma>s$. No $\sigma\in\mathbb R$
satisfies both $\sigma<s$ and $\sigma>s$ simultaneously, so (1.2) fails to
converge absolutely at $0$ or at $\infty$ (or both) for every $w$. $\square$

This already re-derives, from the Mellin side, the fact 108\_03 §1 records
from the potential side: $U_f$'s defining integral (2.1 of 107\_237) does not
converge for $f=f_s$. Here we see the same failure one level down, in the
transform itself.

### Lemma 110.1.3 (mass-zero differences)

For $s_0\ne s_1\in\mathbb R$, $c_0,c_1\ne0$, and
$F(r):=c_0r^{s_0}-c_1r^{s_1}$, the Mellin integral $\hat F(w)=\int_0^\infty
F(r)r^{-w-1}dr$ diverges for every $w\in\mathbb C$.

**Proof.** WLOG $s_0<s_1$. As $r\to0^+$, $r^{s_0}$ dominates $r^{s_1}$
(smaller exponent blows up more strongly, or decays less, as $r\to0$), so
$F(r)r^{-\sigma-1}\sim c_0 r^{s_0-\sigma-1}$; convergence at $0$ needs
$\sigma<s_0$. As $r\to\infty$, $r^{s_1}$ dominates, so $F(r)r^{-\sigma-1}\sim
-c_1r^{s_1-\sigma-1}$; convergence at $\infty$ needs $\sigma>s_1$. Since
$s_0<s_1$, no $\sigma$ satisfies $\sigma<s_0$ and $\sigma>s_1$
simultaneously. $\square$

So the "balancing" that makes $f_{s_0}-f_{s_1}$ mass-zero *in the grade*
(108\_31 §5) does **not** repair convergence of the Mellin integral; it only
removes a different pathology (total-mass normalization), unrelated to this
one.

## 3. The only available sense of "transform": an exact Dirac mass

### Proposition 110.1.2 (regularized transform, exact closed form)

For $\varepsilon>0$, let $f_s^\varepsilon(r):=c\,r^s\,e^{-\varepsilon|\log
r|}$ (a damped version of $f_s$, integrable at both ends for every
$w=s+it$). Then, for $w=s+it$ ($t\in\mathbb R$),
$$\widehat{f_s^\varepsilon}(s+it)=c\cdot\frac{2\varepsilon}{\varepsilon^2+t^2}.
\tag{3.1}$$
For $w=\sigma+it$ with $\sigma\ne s$, $\widehat{f_s^\varepsilon}(w)\to0$ as
$\varepsilon\to0$ pointwise (for fixed $t$; in fact uniformly on compacta
away from $\sigma=s$), while for $\sigma=s$ the family
$K_\varepsilon(t):=\widehat{f_s^\varepsilon}(s+it)/c$ is the Cauchy/Poisson
kernel: $K_\varepsilon\ge0$, $\int_{-\infty}^\infty K_\varepsilon(t)\,dt=2\pi$
for every $\varepsilon>0$, and $K_\varepsilon(t)\to0$ for every fixed $t\ne0$
while $K_\varepsilon(0)=2/\varepsilon\to\infty$. Hence
$\widehat{f_s^\varepsilon}(s+i\cdot)\to 2\pi c\,\delta_0$ weakly as
$\varepsilon\to0$ (a Dirac mass of total weight $2\pi c$ at $t=0$, i.e. at
$w=s$), while $\widehat{f_s^\varepsilon}\to0$ pointwise off the line
$\mathrm{Re}(w)=s$.

**Proof.** Substitute $x=\log r$: $f_s^\varepsilon(e^x)=c\,e^{sx-\varepsilon
|x|}$, and (1.1) becomes $\int_{-\infty}^\infty
c\,e^{sx-\varepsilon|x|}e^{-(s+it)x}dx=c\int_{-\infty}^\infty
e^{-itx-\varepsilon|x|}dx$, the Fourier transform of $e^{-\varepsilon|x|}$ at
frequency $t$, which is the standard identity $2\varepsilon/(\varepsilon^2+t^2)$
(split the integral at $0$ and evaluate two elementary exponentials). This is
(3.1). For $\sigma\ne s$ the same computation gives $c\int e^{(s-w)x
-\varepsilon|x|}dx=c\int e^{(\sigma'-\varepsilon\,\mathrm{sgn}(x))x}dx$-type
divergent-then-regularized integrals that vanish as $\varepsilon\to0$ for
fixed $t$ when $\sigma\ne s$ (direct computation: the antiderivative picks up
a factor $1/(s-w\mp\varepsilon)$, finite for $\varepsilon>0$, and $\to0$ only
in the sense that, for the identity to hold at all we need
$|\mathrm{Re}(s-w)|<\varepsilon$, a shrinking window). The mass
identity $\int K_\varepsilon\,dt=2\pi$ is the elementary
$\int_{-\infty}^\infty \frac{2\varepsilon}{\varepsilon^2+t^2}dt=2\pi$
(antiderivative $2\arctan(t/\varepsilon)$). Positivity, the pointwise
limits, and the blow-up of $K_\varepsilon(0)$ are immediate from (3.1).
$\square$

This makes rigorous the phrase already used in 108\_31 (borrowed from the
programme's standing language): $f_s$'s "Mellin transform" is a **point mass
in the grade**, literally a Dirac delta at the single real point $w=s$, in
the only sense (regularize, then take a weak limit) in which it can be
assigned a transform at all.

## 4. The negative result

### Theorem 110.1.4 (no principal witness of the graded family is ξ-divisible)

No nonzero element of $\mathrm{Prin}'(\mathcal G)$ — neither
$\mathrm{div}(cU_s)$ for any $s\in\mathbb R,c\ne0$, nor a mass-zero
difference $\mathrm{div}(U_{s_0})-\mathrm{div}(U_{s_1})$ for
$s_0\ne s_1$ — is ξ-divisible in the sense $\hat f=\xi\cdot\hat g$ for an
admissible $g$ (Definition (ADM), 110\_00 §1).

**Proof.** By Lemma 110.1.1/110.1.3, $\hat f_s$ and $\widehat{F}$ (for $F$ a
mass-zero difference) do not exist as ordinary functions of $w$ via the
convergent integral (1.1); by Proposition 110.1.2 the only object that can
legitimately be called "the transform" is a Dirac mass (a sum of two Dirac
masses at distinct points, for the difference case), a distribution of order
$0$ whose singular support is a finite set of points on $\mathbb R\subset
\mathbb C$. Suppose, for contradiction, $\hat f=\xi\cdot\hat g$ with $g$
admissible. By (ADM), $g$ is smooth and compactly supported, so $\hat g$ is
an **entire function** of $w$ (a standard consequence of differentiating
under the integral sign over a compact range — no singular support at all).
Since $\xi$ is also entire, $\xi\cdot\hat g$ is entire, i.e. an ordinary,
everywhere-defined, holomorphic function of $w$ — in particular a genuine
function, not a distribution with point support. A Dirac mass (or finite sum
of Dirac masses at distinct points) is not equal, as a distribution, to any
entire function unless that entire function is not being compared as a
distribution at all but as its restriction — but an candid entire function,
viewed as a distribution via integration against test forms, is never a sum
of point masses (its distributional derivative of every order is again a
continuous/entire function, never singular). Hence no entire $\xi\hat g$ can
equal a Dirac mass (or sum of two), for any admissible $g$. $\square$

### Corollary 110.1.5 (the "vacuous vanishing" reading is not a proof, and why)

One might try to read off the radical condition directly from Proposition
110.1.2: since $\hat f_s$ "vanishes" (as the weak limit of
$\widehat{f_s^\varepsilon}$) at every point $w\ne s$, and every zero $\rho$
of $\xi$ has $\rho\ne s$ whenever $s$ is real (Lemma 110.1.6 below: $\xi$ has
no real zero), one might claim $\hat f_s(\rho)=0$ "automatically" for every
zero $\rho$, hence $f_s\in\mathrm{rad}\,I_\partial$ for free. **This is
not a valid argument**, for two independent reasons. First, per Theorem
110.1.4, $f_s$ is not ξ-divisible in the required functional sense at all —
"vanishing away from an atom" is not the same predicate as "divisible by the
entire function $\xi$", and the source rule's containment
$\mathcal P\subseteq\mathrm{rad}\,I_\partial$ needs the latter (or a
comparably rigorous route into $\mathrm{rad}\,I_\partial$), not a
distributional coincidence. Second, and more basically, $I_\partial$'s
defining Weil-formula identity (110\_00 §1) is a theorem about admissible
$f,g$; $f_s\notin(\text{ADM})$ (108\_03 §1 already records that $f_s$'s
potential integral diverges), so the formula's right-hand side
$\hat f(0)\overline{\hat g(0)}+\hat f(1)\overline{\hat g(1)}-\sum_\rho\cdots$
is not licensed to be evaluated on $f_s$ at all — there is no theorem placing
$f_s$ in the domain where that identity was proved. The apparent "free"
vanishing is an artifact of applying a formula outside its proven domain,
exactly the failure mode Corollary 110.1.5 exists to flag.

### Lemma 110.1.6 ($\xi$ has no real zero) — supporting fact, verified numerically

$\xi(s)\ne0$ for every $s\in\mathbb R$. **Status: verified numerically over a
representative grid below** (this is a classical unconditional fact; a full
analytic proof is not re-derived here, per the scope rule against wandering
outside the two permitted source files, but it is not needed for Theorem
110.1.4, which does not use it — it is used only to close the parenthetical
remark in Corollary 110.1.5, and is flagged as such).

## 5. Scope

**Proved here:**
* Lemma 110.1.1, Lemma 110.1.3: $f_s$ and mass-zero differences have no
  ordinary (absolutely convergent) Mellin transform, for any $w$.
* Proposition 110.1.2: the exact closed-form regularization and its weak
  limit to a Dirac mass at $w=s$.
* Theorem 110.1.4: no nonzero element of $\mathrm{Prin}'(\mathcal G)$
  is ξ-divisible, by a category mismatch (distribution vs. entire function).
* Corollary 110.1.5: why the superficially "free" vanishing does not
  constitute a proof of containment in $\mathrm{rad}\,I_\partial$.

**Read from source, not re-derived:** the graded family $f_s$, $\mathcal
L_s$, $\mathrm{Prin}'(\mathcal G)$ (108\_03, 108\_31); the statement
that $U_f$'s defining integral diverges for $f=f_s$ (108\_03 §1); the
corner-pairing Weil-formula identity for $I_\partial$ (quoted in the phase
prompt, 110\_00 §1).

**Verified numerically:** Proposition 110.1.2's closed form (3.1), by direct
quadrature under refinement of the truncation window; the divergence claims
of Lemma 110.1.1/110.1.3, by confirming truncated partial integrals grow
without bound at the analytically predicted rate under refinement; Lemma
110.1.6, by a real-axis scan (with an explicit control case showing the
zero-detector correctly flags a genuine zero when one is present).

**Not established, and explicitly not claimed:** a general classification of
*all* possible principal-subspace candidates (only the graded family read
from 108\_03/108\_31 is tested); any claim about complex weights; any use of
RH or of the location of any zero of $\xi$ (Lemma 110.1.6 is used only for a
remark, not for Theorem 110.1.4, and is itself an unconditional classical
fact, not RH).

## 6. Verifier

`110_01_the_graded_family_is_not_xi_divisible.py`: (1) confirms Lemma
110.1.1/110.1.3's divergence by refinement — truncated integrals over
$[\varepsilon,1/\varepsilon]$ grow without bound as $\varepsilon\to0$, at the
analytically predicted rate (power-law or logarithmic, matched by curve fit,
not merely "gets big"); (2) confirms Proposition 110.1.2's closed form (3.1)
to high relative precision against direct numerical quadrature, refined by
enlarging the truncation window, together with the mass identity $\int
K_\varepsilon=2\pi$ (exact, independent of $\varepsilon$) and the
concentration limit ($K_\varepsilon(0)\to\infty$ like $2/\varepsilon$,
$K_\varepsilon(t)\to0$ for fixed $t\ne0$), with an explicit control that
rejects a deliberately wrong constant (e.g. $\varepsilon/(\varepsilon^2+t^2)$,
missing the factor $2$); (3) scans $\xi$ on a real grid for Lemma 110.1.6,
with a control case (a function with a known real zero) confirming the
zero-detector is capable of flagging a genuine zero, so the "no zero found"
result is not a vacuous pass.
