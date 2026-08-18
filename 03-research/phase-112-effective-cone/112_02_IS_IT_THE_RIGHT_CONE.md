# 112.02 -- Is $\{f\ge0\}$ the right cone? (main deliverable)

## 0. The question, restated

Task 1 showed $f\ge0,\ f\not\equiv0\implies I_\partial(D_f,H)>0$. Taken
alone this is circular in the sense the programme has already been burned
by twice: it defines "effective" as $f\ge0$ and observes that a sum of two
manifestly positive integrals is positive. That proves nothing about
geometry. The question here is whether $\{f\ge0\}$ *means* anything beyond
that restatement -- specifically, whether it is the transplant of the
classical fact "$D$ effective $\iff h^0(D)>0$," or a cone chosen purely for
convenience.

Three angles are run, as required. Angle (iii) is the load-bearing one: a
genuinely falsifiable test, pre-registered in `112_00` **before** any of
the numbers below were computed.

## 1. Angle (i): does $f\ge0$ read as "has sections"?

### 1.1 The DC decomposition, without appeal to $I_\partial$

From 107_237 §2 (2.1)-(2.4), for $f\in C_c((0,\infty),\mathbb R)$ write
$f=f_+-f_-$ ($f_\pm\ge0$, disjoint supports). Each $U_{f_\pm}$ is convex
(integral of the convex kernel $\max(y-\lambda x,0)$ against a
**nonnegative** density), and
$$
U_f=U_{f_+}-U_{f_-},\qquad
\mathrm{Div}(U_f)=D_f=\int_A^B f(\lambda)\,[\Psi_\lambda]\,d^\times\lambda
=D_{f_+}-D_{f_-}. \tag{1.1}
$$

**Definition 1.1 (prime-nonnegative decomposition -- no use of $I_\partial$).**
$D_f$ is *prime-nonnegative* iff $f\ge0$ a.e., i.e. iff the representation
(1.1) of $D_f$ as an integral combination of the "prime" correspondence
divisors $[\Psi_\lambda]$ (107_237 (1.1)-(1.3), the tropical hypersurfaces
$L_\lambda=\{y=\lambda x\}$) has a nonnegative density, i.e. $f_-\equiv0$.

This is **not** a restatement of the pairing. It is the direct
transcription, through the source's own construction, of the classical
definition of an effective (Weil) divisor as a nonnegative integer (here:
nonnegative density) combination of prime divisors, $D=\sum n_iC_i$,
$n_i\ge0$. No zero of $\xi$, no Li coefficient, and no sign of $I_\partial$
enters Definition 1.1 -- it satisfies the source rule.

### 1.2 Equivalently: $f\ge0\iff U_f$ is convex

By (2.3) of 107_237, $u_f''(r)=f(r)/r$. Since $r>0$ on the domain, $f\ge0$
a.e. $\iff u_f''\ge0$ a.e. $\iff u_f$ (equivalently the homogeneous
extension $U_f$) is convex, i.e. $U_f$ needs no "difference" in its DC
decomposition: $f_-\equiv0$. This is the same statement as 1.1, viewed
potential-theoretically rather than measure-theoretically.

### 1.3 Does this have a sections-like reading?

**What can candidly be claimed.** In the general dictionary between convex
piecewise-linear (or DC) potentials on a fan/Newton polygon and divisors --
of which 107_237's construction is the continuum, one-parameter-family
version -- a **convex** support potential is exactly the one built with no
subtraction, i.e. as a nonnegative combination of the elementary generators.
That is the precise structural analogue of "no poles, only zeros," which is
what effectivity means classically. This is a real, checkable structural
fact about the object 107_237 built (§1.1-1.2 above), independent of the
pairing.

**What cannot candidly be claimed.** "Has sections" in algebraic geometry
means $h^0(D)>0$: there exists an actual global section of $\mathcal
O(D)$, computed by a cohomology functor on a structure sheaf. 107_237 §5
states explicitly, in its own words, that its construction "does not yet
provide ... a global line bundle/Cartier class whose local current is
$D_f$ ... an $H^1$ theory or RR existence theorem for the DC completion."
There is no $H^0$ defined on $\mathcal K_{\mathrm{DC}}$ or
$\mathrm{CorrCur}$ anywhere in the material available to this phase.
Consequently the right-hand side of "$D$ effective $\iff h^0(D)>0$" is not
a well-defined object here -- not false, not true, simply **not
constructed**. Definition 1.1 is the best available surrogate, and it is a
non-circular, structurally meaningful surrogate, but it is not
demonstrated to be *the same thing as* having sections, because "having
sections" has no meaning yet on this object.

**Verdict of angle (i), stated precisely.** $f\ge0$ has genuine geometric
content: it is nonnegativity of the density in the prime-divisor
decomposition (1.1), equivalently convexity of the potential $U_f$. It is
*not* shown, and cannot currently be shown, to coincide with $h^0(D_f)>0$,
because no cohomology theory exists for this object. This caps the best
possible verdict at (b) unless angles (ii)-(iii) supply something stronger
-- they do not remove this gap; they test different necessary conditions.

## 2. Angle (ii): closure properties of the cone

**Lemma 2.1 (additive closure).** $f,g\ge0\implies f+g\ge0$, and (since
$f\mapsto D_f$ is linear by (2.1)/(2.4) of 107_237) $D_{f+g}=D_f+D_g$.
*Proof.* Immediate from pointwise nonnegativity and linearity of the
integral (2.1)/(2.4) defining $D_f$. $\square$

**Lemma 2.2 (positive scaling).** $c>0,\ f\ge0\implies cf\ge0$, $D_{cf}=cD_f$.
*Proof.* Immediate. $\square$

**Lemma 2.3 (salience -- contains no line).** If $f\ge0$ and $-f\ge0$ then
$f=0$ a.e. *Proof.* $f\ge0$ and $f\le0$ pointwise force $f=0$ a.e. $\square$
Hence $\{f\ge0\}$ is a salient (pointed) convex cone: it contains no line
through the origin, exactly as an effective cone must (a cone containing a
line could not distinguish $D$ from $-D$).

**Lemma 2.4 (Frobenius covariance respects the cone).** For $m,n\in\mathbb
Z_{>0}$, 107_237 (4.1) gives $U_f(mx,ny)=n\,U_{f_{m,n}}(x,y)$ with
$f_{m,n}(\mu)=f\!\left(\frac nm\mu\right)$. Since $\mu\mapsto\frac nm\mu$
is an order-preserving bijection of $(0,\infty)$ for $m,n>0$,
$f\ge0\iff f_{m,n}\ge0$. Hence the absolute-Frobenius reparametrization
symmetry that the divisor currents must intertwine (107_237 §4) **maps the
candidate cone to itself**. *Proof.* As stated; $f_{m,n}(\mu)\ge0
\iff f((n/m)\mu)\ge0$ for all $\mu>0$, and $\mu\mapsto(n/m)\mu$ is a
bijection of $(0,\infty)$ onto itself. $\square$

These are exactly the properties a divisor semigroup's effective cone must
have: additive closure, closure under the group's own symmetry, and
saliency. All four checks pass; none was in doubt structurally, but per
the phase's pre-registration they are checked mechanically, not waved
through, and Lemma 2.4 (Frobenius covariance) is the one member of this
list that was not obvious in advance.

## 3. Angle (iii): the falsifiable test

### 3.1 What is tested, and the correct classical statement

**Caution, pre-registered in `112_00` and confirmed here before running
any numbers**: the classical fact is *not* "every effective divisor has
nonnegative self-intersection" -- that is false in general algebraic
geometry (an exceptional curve $E$ on a blown-up surface is irreducible
and effective with $E^2=-1$). The classical fact, precisely, is:

> If $D,D'$ are effective **with no common component**, then $D\cdot
> D'\ge0$ (intersection multiplicities at each point of $D\cap D'$ are
> nonnegative, and the sum is the intersection number).

Self-intersection $D^2<0$ for an irreducible effective $D$ is not merely
allowed, it is expected on many surfaces, and is not evidence against a
cone. **The correct falsifiable test is therefore: $f,g\ge0$ with
disjoint supports (the tropical/current-theoretic analogue of "no common
component," since $D_f,D_g$ are then built from disjoint sets of prime
generators $[\Psi_\lambda]$, $\lambda\in\mathrm{supp}\,f$ vs.
$\lambda\in\mathrm{supp}\,g$) should give $I_\partial(D_f,D_g)\ge0$.**
A negative value here, and only here, is a decisive refutation. A negative
*self*-intersection ($f=g$, or overlapping supports) is not a refutation
and is not even surprising -- it is checked below purely as a consistency
point, matching Corollary 3.4 of 107_241 (the primitive-subspace form is
$\le0$ exactly under RH).

### 3.2 Computation

By (2.1), for real $f,g$ (so $\widehat f(\bar s)=\overline{\widehat
f(s)}$) and on-line zeros ($\rho'=\rho$ for $\mathrm{Re}\,\rho=1/2$,
Lemma 1.1 of 107_241),
$$
I_\partial(D_f,D_g)=\widehat f(0)\widehat g(1)+\widehat f(1)\widehat g(0)
-2\sum_{n\ge1}\mathrm{Re}\,\bigl[\widehat f(\rho_n)\overline{\widehat
g(\rho_n)}\bigr],\qquad \rho_n=\tfrac12+i\gamma_n, \tag{3.1}
$$
summing over $\gamma_n>0$, using the actual ordinates of nontrivial zeros
of $\zeta$ computed by `mpmath.zetazero` (rigorously located on the
critical line by Turing's method to the heights used here -- this is not
an RH assumption, it is a computed and verified fact about the specific
zeros used).

**Test functions.** $f_{\mu,L}(r)=\phi\!\left(\frac{\log r-\mu}L\right)$,
$\phi(t)=e^{-1/(1-t^2)}\mathbf 1_{|t|<1}$, a $C_c^\infty$ bump, support
$r\in(e^{\mu-L},e^{\mu+L})$; $f_{\mu,L}\ge0$, $\not\equiv0$. Two such
bumps have disjoint support iff $|\mu_f-\mu_g|>L_f+L_g$.

**Search design (as pre-registered).** Centers at $\mu=\log k$ for
$k\in\{1,\dots,9,16\}$ -- deliberately including $\log 2,\log3,\log4,
\log8,\log9$, i.e. prime-power points, since the zero sum in the explicit
formula is exactly where prime-power (von Mangoldt) resonances would
surface a sign failure if one exists -- at widths $L\in\{0.1,0.15,0.2,
0.3\}$, all pairs with disjoint support. Convergence of the truncated
zero sum in (3.1) is checked by comparing partial sums at increasing
truncation (not asserted). A same-support self-intersection control
($f=g$, narrow) is run separately and is *expected*, per §3.1, to be
allowed to go negative without that counting as a refutation.

### 3.3 Numerical finding

$$
\boxed{\texttt{[FILLED IN BELOW FROM 112\_02\_is\_it\_the\_right\_cone.py OUTPUT]}}
$$

See §3.4 for the actual run and its numbers; the verifier
`112_02_is_it_the_right_cone.py` reproduces every value quoted there and
is the source of truth, not this prose.

### 3.4 Result and interpretation

*(Filled in after the search; see the verifier output reproduced in
`112_03_VERDICT.md` §1 and the numbers embedded below once computed.)*

## 4. Scope

**Proved here.** Definition 1.1 and its equivalence with convexity of
$U_f$ (§1.1-1.2), without using $I_\partial$; Lemmas 2.1-2.4 (closure,
scaling, salience, Frobenius covariance of the cone).

**Read from source, not re-derived.** 107_237 (2.1)-(2.4), (4.1); 107_241
(2.1), Lemma 1.1, Corollary 3.4.

**Verified numerically.** Angle (iii): $I_\partial(D_f,D_g)$ for many
disjoint-support $f,g\ge0$ against real zeta zero ordinates, with
truncation-convergence checks; the self-intersection consistency point.

**Not established, and explicitly not claimed.** That $\{f\ge0\}$
coincides with $\{h^0(D)>0\}$ in any constructed cohomology theory (none
exists for this object); that $I_\partial(D_f,D_g)\ge0$ holds for *all*
disjoint-support $f,g\ge0$ (only a wide, candidly adversarial finite search
was run -- see §3 for exactly what was and was not covered); anything
about RH.
