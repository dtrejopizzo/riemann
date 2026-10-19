# 104_52 — Connected two-tower Hessian and quadratic flux gate

**Attack goal.** Construct a second-order form that simultaneously keeps
the real weights \(\Lambda(p^k)=\log p\), the pole, the Gamma factor, and
the Laguerre phase, and search within it for a coercive bound for

\[
 H_n:=\lambda_n-{501\over2002}A_n
 ={1501\over2002}A_n-B_n\ge0,\qquad n\ge150.              \tag{1}
\]

An exact representation is obtained. Let

\[
 F(s)=(s-1)\zeta(s),\qquad
 G(s)={1\over2}s\pi^{-s/2}\Gamma(s/2),\qquad
 \kappa={1501\over2002},                                  \tag{2}
\]

and \(J_\kappa=\log F+\kappa\log G\), with the real branches on
\(s>1\). Then the complete connected Hessian is

\[
 \boxed{
 J_\kappa''(s)=
 \sum_{p}\sum_{k\ge1}\sum_{j=1}^{k}
       (\log p)^2p^{-ks}
 -{1\over(s-1)^2}
 +\kappa\sum_{r\ge1}{1\over(s+2r)^2}.}                   \tag{3}
\]

The first sum is a pair ordered **nested within the same tower**;
the second is its continuous polar analogue and the third preserves exactly
the Gamma channel. The decisive conclusion is negative: before reaching
(3), all pairs between distinct prime towers and all prime--pole crossings
cancel identically when passing from the second moment to the Hessian of
\(\log F\). No covariance between \(p\ne q\) remains for a
non-alignment bound to act on.

Moreover, the right side of (3) has no fixed sign even on the real ray: its
continuation is \(<0\) at \(s=1\) and \(>0\) at \(s=10\), with
rational certificates. The mixed cocycle of the Laguerre test also has
both signs for every \(n\ge4\). Hence the representation does not produce
the proportional coercivity of (1). The same connected mechanism exists
for \(\zeta(s+c)\zeta(s-c)\), whose completed system has zeros off
the critical line.

The narrow mechanism

```text
second moment of two marks / two-tower covariance
+ connected subtraction
+ sign of the real Hessian or the mixed Laguerre cocycle
    => H_n >= 0.
```

is ruled out. The same cancellation extends to every finite-order connected
cumulant of the derivative hierarchy of \(\log F\): simply raising from two
to three or more marks of the additive observable \(\log N\) also creates
no interaction between distinct primes. This says nothing about cumulants
of arbitrary nonlinear observables of \(N\). A nonlinear inequality on
**disconnected** moments applied before the logarithm and surviving the
cancellation is not ruled out. This document does not prove (1), A1, or RH.

## 0. Non-duplication audit

`103_68` already factors a completed function as a quotient of Laplace
transforms and computes its first two cumulants. `104_43`--`104_45`
build a single size-biased mark; `104_49` proves the cancellation of the
full moments against the cumulants order by order. Those results are not
recounted here.

The narrow addition here is different: the second moment is literally
polarized in two tower marks, the connected part surviving the logarithm is
computed, and the Gamma factor is incorporated with the exact coefficient
\(1501/2002\) required by A1. The cancellation of all pairs
\(p\ne q\), the complete formula (3), its rational sign change, and the
quadratic flux of section 6 are the content of this gate.

## 1. Two divisor marks and the `lcm` kernel

Fix \(s>1\). Under the zeta law

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad X=\log N,  \tag{4}
\]

conditioned on \(N\), choose two independent marks \(D_1,D_2\) with

\[
 \mathbb P(D_i=d\mid N)
 ={\Lambda(d)\over X}\mathbf1_{d\mid N}.                 \tag{5}
\]

The identity \(\sum_{d\mid N}\Lambda(d)=\log N\) makes (5) a
probability when \(N>1\); at \(N=1\) a cemetery state is used, whose
contribution vanishes due to the factor \(X^2\). For every test \(Q\) for
which the sums converge,

\[
 \boxed{
 \mathbb E_s\{X^2Q(\log D_1,\log D_2)\}
 =\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
       \mathrm{lcm}(d,e)^s}Q(\log d,\log e).}       \tag{6}
\]

Indeed, after canceling \(X^2\), the sum over multiples of
\(\mathrm{lcm}(d,e)\) equals
\(\zeta(s)\mathrm{lcm}(d,e)^{-s}\).

The polar comparator has an exactly parallel formula. Let
\(X_0\sim\mathrm{Exp}(s-1)\) and, conditioned on \(X_0=L\), choose
\(U_1,U_2\) independent and uniform on \([0,L]\). Then

\[
 \boxed{
 \mathbb E\{X_0^2Q(U_1,U_2)\}
 =\int_0^\infty\!\int_0^\infty
 e^{-(s-1)\max(x,y)}Q(x,y)\,dx\,dy.}                     \tag{7}
\]

Equations (6)--(7) are a complete two-mark comparison; they do not
separate prime powers nor take absolute values.

But their connected part is already local to a single tower. Subtracting
the product of the one-mark intensities, the arithmetic kernel is

\[
 C_s(d,e)=\Lambda(d)\Lambda(e)
 \{\mathrm{lcm}(d,e)^{-s}-(de)^{-s}\}.             \tag{8}
\]

If \(d=p^k,e=q^\ell\) and \(p\ne q\), then
\(\mathrm{lcm}(d,e)=de\), so

\[
 \boxed{C_s(p^k,q^\ell)=0\qquad(p\ne q).}                \tag{9}
\]

If \(p=q\), (8) is positive and depends on \(\max(k,\ell)\). Thus the
divisibility covariance detects repetitions within a tower, not an
interaction between different towers. This is also a direct consequence of
the independence of the geometric exponents \(A_p\) in (4).

## 2. Exact cancellation of the disconnected pairs

Write

\[
 \mathcal L(s)=\sum_{m\ge2}{\Lambda(m)\over m^s},\qquad
 \mathcal K_2(s)=\sum_{m\ge2}{\Lambda(m)\log m\over m^s}.\tag{10}
\]

Since \(\zeta'/\zeta=-\mathcal L\), absolute differentiation at
\(s>1\) gives

\[
 {F''(s)\over F(s)}
 =\mathcal L(s)^2+\mathcal K_2(s)
       -{2\mathcal L(s)\over s-1}.                        \tag{11}
\]

The three terms of (11) are, respectively, pairs of independent prime
powers, the nested collision, and the two prime--pole crossings. On the
other hand,

\[
 \left({F'(s)\over F(s)}\right)^2
 ={1\over(s-1)^2}+\mathcal L(s)^2
       -{2\mathcal L(s)\over s-1}.                        \tag{12}
\]

Subtracting (12) from (11),

\[
 \boxed{(\log F)''(s)=\mathcal K_2(s)-{1\over(s-1)^2}.}  \tag{13}
\]

In particular, \(\mathcal L^2\), including all products
\(p^{-ks}q^{-\ell s}\) with \(p\ne q\), vanishes with
**exactly zero** coefficient. The same happens with the prime--pole
crossings. This is not a bound or a loss caused by Cauchy--Schwarz: it is
the moment--cumulant subtraction that defines the logarithm.

The unit renewal turns (13) into a nested-pair form:

\[
 \begin{aligned}
 \mathcal K_2(s)
 &=\sum_m{\Lambda(m)\over m^s}\sum_{d\mid m}\Lambda(d)\\
 &=\sum_p\sum_{k\ge1}\sum_{j=1}^{k}
       (\log p)^2p^{-ks},                                  \tag{14}\\
 {1\over(s-1)^2}
 &=\int_{0\le y\le x<\infty}e^{-(s-1)x}\,dy\,dx.        \tag{15}
 \end{aligned}
\]

Since \(\Lambda(m)\ne0\) forces \(m=p^k\), the marked divisor in (14)
necessarily belongs to the same tower as the outer divisor.

### 2.1. The obstruction holds at every connected order

Interactions between towers are not recovered by passing to the third
cumulant. For every integer \(r\ge2\), absolute differentiation at
\(s>1\) gives

\[
 \boxed{
 (\log F)^{(r)}(s)=(-1)^r
 \left\{
  \sum_{m\ge2}{\Lambda(m)(\log m)^{r-1}\over m^s}
  -{(r-1)!\over(s-1)^r}
 \right\}.}                                               \tag{15a}
\]

If \(m=p^k\), then

\[
 \Lambda(m)(\log m)^{r-1}
 =(\log p)^r
 \sum_{j_1,\ldots,j_{r-1}=1}^{k}1.                       \tag{15b}
\]

Thus each order-\(r\) cumulant is an outer mark plus \(r-1\) marks nested
in **the same** tower. This is not peculiar to second order: it is the
additivity of \(\log\zeta=\sum_p-\log(1-p^{-s})\). All mixed cumulants of
distinct Euler factors are zero.

The Gamma factor does not change this conclusion either. Differentiating
(18), for \(r\ge2\),

\[
 (\log G)^{(r)}(s)
 =(-1)^r(r-1)!\sum_{j\ge1}{1\over(s+2j)^r}.               \tag{15c}
\]

Consequently

\[
 \boxed{
 J_\kappa^{(r)}(s)=(-1)^r\left\{
 \sum_m{\Lambda(m)(\log m)^{r-1}\over m^s}
 -{(r-1)!\over(s-1)^r}
 +\kappa(r-1)!\sum_{j\ge1}{1\over(s+2j)^r}
 \right\}.}                                               \tag{15d}
\]

Therefore no finite-order connected cumulant **of this additive
hierarchy** can be the missing multi-tower mechanism. A future route could
use a different nonlinear observable; if it stays within the hierarchy of
\(\log F\), it would have to apply an inequality to the disconnected
moments before the logarithm removes them, and jointly control the terms
that afterward cancel.

## 3. Exact incorporation of Gamma and the A1 margin

The completed factorization is \(\xi=FG\), up to the constant already
included in (2). With the Phase 104 normalization,

\[
 A_n=n[z^n]\log G((1-z)^{-1}),\qquad
 B_n=-n[z^n]\log F((1-z)^{-1}).                           \tag{16}
\]

Hence (1) is exactly equivalent to

\[
 \boxed{H_n=n[z^n]J_\kappa((1-z)^{-1})\ge0.}              \tag{17}
\]

The Gamma block has not been approximated. Its Hessian is explicit. If
\(\psi_1\) denotes the trigamma function,

\[
 \begin{aligned}
 (\log G)''(s)
 &=-{1\over s^2}+{1\over4}\psi_1(s/2)\\
 &=-{1\over s^2}+\sum_{r\ge0}{1\over(s+2r)^2}
 =\sum_{r\ge1}{1\over(s+2r)^2}.                          \tag{18}
 \end{aligned}
\]

Combining (13), (14), (15), and (18) proves (3). The Gamma channel is also
a continuous pair form, since

\[
 {1\over(s+2r)^2}
 =\int_{0\le y\le x<\infty}e^{-(s+2r)x}\,dy\,dx.         \tag{19}
\]

Thus (3) genuinely keeps prime towers, pole, and Gamma coupled in a
single signed form.

To avoid any illegitimate use of the Euler series at \(s=1\), take
\(a>1\), \(s_a(z)=a/(1-z)\), and define

\[
 \mathcal H_{n,a}=n[z^n]J_\kappa(s_a(z)).                 \tag{20}
\]

On a small disk the whole path between \(a\) and \(s_a(z)\) remains in
\(\Re s>1\), and

\[
 \boxed{
 \mathcal H_{n,a}
 =a[z^{n-1}]{1\over(1-z)^2}
 \left\{J_\kappa'(a)+\int_a^{s_a(z)}J_\kappa''(u)\,du\right\}.} \tag{21}
\]

The expression in braces is \(J_\kappa'(s_a(z))\). Letting
\(a\downarrow1\), (20)--(21) converge coefficient by coefficient to (17).
This is the requested exact two-tower representation. Proving that its
limit is nonnegative for every \(n\ge150\) is still exactly (1).

## 4. The complete Hessian has both signs

The analytic continuation of (3) to \(s=1\) can be evaluated with the
expansion

\[
 (s-1)\zeta(s)=1+\gamma(s-1)-\gamma_1(s-1)^2+O((s-1)^3).
\]

From this and (18),

\[
 \boxed{
 J_\kappa''(1)=-\gamma^2-2\gamma_1
      +\kappa\left({\pi^2\over8}-1\right)<0.}             \tag{22}
\]

The sign does not depend on floating-point decimals. The rational bounds
already used in `103_68`,

\[
 \gamma>{577\over1000},\qquad
 \gamma_1>-{73\over1000},\qquad
 \pi^2<{987\over100},                                    \tag{23}
\]

give the exact ceiling

\[
 J_\kappa''(1)
 <-\left({577\over1000}\right)^2+{146\over1000}
 +{1501\over2002}\left({987\over800}-1\right)
 =-{531207\over45500000}<0.                               \tag{24}
\]

In the other direction, (3) and (18) imply

\[
 J_\kappa''(10)
 >-{1\over81}+\kappa\sum_{r\ge1}{1\over(10+2r)^2}
 \ge-{1\over81}+{\kappa\over24}>0,                      \tag{25}
\]

because for the decreasing function \((10+2x)^{-2}\),
the sum from \(r=1\) dominates its integral from \(1\), which equals
\(1/24\), and \(81\cdot1501>24\cdot2002\). The term \(\mathcal K_2(10)\) is
positive and only improves (25).

By continuity, the Hessian of the **exact margin functional** changes
sign on \((1,10)\). There is no global real convexity that could
supply (1).

## 5. The Laguerre phase cocycle also has no fixed sign

The natural interaction of two tower increments \(x,y>0\) on

\[
 P_n(t)=L_{n-1}^{(1)}(t)
\]

is the mixed cocycle

\[
 \Delta_{x,y}P_n(t)
 =P_n(t+x+y)-P_n(t+x)-P_n(t+y)+P_n(t).                    \tag{26}
\]

For \(n\ge3\), the Laguerre derivative identity gives

\[
 \boxed{
 \Delta_{x,y}P_n(t)
 =\int_0^x\!\int_0^y L_{n-3}^{(3)}(t+u+v)\,dv\,du.}       \tag{27}
\]

If \(n\ge4\), \(L_{n-3}^{(3)}\) has \(n-3\) simple positive zeros and
alternates sign between them. Choosing \(t\) inside an interval of fixed
sign and then \(x,y>0\) sufficiently small, (27) takes both signs. This
includes every degree \(n\ge150\).

The phenomenon is already visible without asymptotics:

\[
 P_4(t)=4-6t+2t^2-{t^3\over6},\qquad
 \Delta_{x,y}P_4(t)=xy\left(4-t-{x+y\over2}\right).       \tag{28}
\]

Hence neither the connected part of the two marks nor its Laguerre test
has the sign needed for a pointwise inequality. Integrating them without
separating them returns exactly (21).

## 6. Second-order homotopy flux

Let \(D=a\partial_a\). The first-order law of `104_47` holds for
any logarithm composed with \(a/(1-z)\), in particular for
\(\mathcal H_{n,a}\):

\[
 D\mathcal H_{n,a}
 =n(\mathcal H_{n+1,a}-\mathcal H_{n,a}).                 \tag{29}
\]

Applying it a second time and subtracting (29),

\[
 \boxed{
 D(D-1)\mathcal H_{n,a}
 =n(n+1)
 \{\mathcal H_{n+2,a}-2\mathcal H_{n+1,a}
                         +\mathcal H_{n,a}\}.}            \tag{30}
\]

This is the exact quadratic flux. It does not create a positive energy: the
right side is a signed second difference, and by (21) its integral with
the boundary data reconstructs \(H_n\) without remainder. Estimating it
with a fixed sign would be another formulation of the missing coercivity,
not a consequence of the identity.

## 7. Shifted falsifier

For \(0<c<1/2\), normalize

\[
 F_c(s)=\{s-1-c\}\{s-1+c\}\zeta(s+c)\zeta(s-c).          \tag{31}
\]

In its Euler half-plane,

\[
 \mathcal L_c(s)=\mathcal L(s-c)+\mathcal L(s+c)
 =\sum_m{2\Lambda(m)\cosh(c\log m)\over m^s}.            \tag{32}
\]

The same cancellation as (11)--(13) gives

\[
 \boxed{
 (\log F_c)''(s)
 =\sum_m{2\Lambda(m)\cosh(c\log m)\log m\over m^s}
 -{1\over(s-1-c)^2}-{1\over(s-1+c)^2}.}                  \tag{33}
\]

The completion also introduces no crossed pairs:

\[
 \{\log G(s+c)+\log G(s-c)\}''
 =(\log G)''(s+c)+(\log G)''(s-c).                        \tag{33a}
\]

Again, no pairs between distinct primes survive. Moreover
\(\log(p^k)=\sum_{j=1}^k\log p\), so the first term of (33)
admits the same uniform nested marking as (14), even though its outer
weight depends on \(k\). The completion \(\xi(s+c)\xi(s-c)\) has zeros on
both sides of \(\Re s=1/2\) and exponentially negative Li coefficients
along a subsequence (`104_48`, (21)--(23c)).

Thus second moment, connected subtraction, uniform interior mark, and
polar and Gamma channels do not suffice as abstract axioms. A valid
inequality could still use the exact outer value
\(\Lambda(p^k)=\log p\), which (32) loses; but the second-order Hessian
generates no interaction between towers to exploit it.

## 8. Verdict

The following is proved unconditionally:

1. the exact two-mark selector and its `lcm` kernels (6)--(9);
2. the connected cancellation of all pairs \(p\ne q\) and of the
   prime--pole crossings (11)--(13);
3. the nested tower--pole--Gamma form (3), (14)--(19);
4. the exact reconstruction of the margin (17), (20)--(21);
5. the rational sign change of the complete Hessian (22)--(25);
6. both signs of the Laguerre cocycle (26)--(28);
7. the quadratic flux (30) and its shifted analogue (33).

The result is not the bound (1). The surviving front narrows once more:
a proportional bound must retain a **disconnected and nonlinear**
correlation before the logarithm removes the interactions between towers.
Raising the order of the connected cumulant of the additive observable
\(\log N\) does not help, by (15a)--(15d). The mechanism must also use the
unit outer multiplicity to reject (32). That inequality has not been
constructed.

## 9. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 connected_two_tower_flux_gate_check.py
```

The checker uses only integers and `Fraction`. It verifies the symbolic
cancellation of (11)--(13), the finite nested renewal, the `lcm` kernel,
the rational certificates (24)--(25), the two exact signs of the Laguerre
cocycle at degree 151, and the flux identity (30). It does not evaluate A1
or RH.
