# R170_850 — Arithmetic law of the Wronskian extracted by Möbius

> **Corpus collision (R170_851).** The coefficient law is correct,
> but it also satisfies
> `gamma=Lambda log-Lambda*Lambda`. Together with Selberg's
> `W=Lambda log+Lambda*Lambda`, it returns exactly to the
> signless deconvolution audited in R162_501 and R170_841 §4.3. The
> synchronized tail of R170_841 does not provide `W` on the low fibers:
> there it is zero. Hence (0.2) does not yet constitute a new positive
> completion.

## 0. Result

The finite causal inverse of R170_849 is exactly the compression of the
Möbius comb. When applied to the arithmetic Wronskian of R170_843, the
resulting convolution has a closed law:

\[
 \boxed{
 \gamma_\Lambda(n):=(\mu*\beta_\Lambda)(n)
 =-\sum_{d\mid n}\mu(d)(\log d)^2.}
 \tag{0.1}
\]

By unique factorization,

\[
 \boxed{
 \gamma_\Lambda(n)=
 \begin{cases}
  (\log p)^2,& n=p^k,\ k\ge1,\\
  -2\log p\log q,&n=p^a q^b,\ p\ne q,\ a,b\ge1,\\
  0,&\omega(n)\ge3,
 \end{cases}}
 \tag{0.2}
\]

and `gamma(1)=0`. This is a uniform, exact, and specifically
arithmetic law: it retains the prime bases and their two-color
products.

## 1. The compressed inverse is Möbius

Define the formal causal combs

\[
 S=\sum_{n\ge1}{1\over\sqrt n}\tau_{\log n},
 \qquad
 M=\sum_{n\ge1}{\mu(n)\over\sqrt n}\tau_{\log n}.
 \tag{1.1}
\]

In every region where the sums are locally finite,

\[
 MS=SM=I                                                   \tag{1.2}
\]

by `mu*1=delta_1`.

Let `P=P_T` and `N>=e^(2T)`. Only shifts `log n<2T` can act
inside the window, so

\[
 PS_NP=PSP.                                                 \tag{1.3}
\]

All shifts of `S` and `M` have the same causal orientation. A
trajectory that leaves the window cannot re-enter. Hence the
intermediate `P/Q` do not create a return term:

\[
 (PSP)(PMP)=PSMP=P,
 \qquad
 (PMP)(PSP)=PMSP=P.                                        \tag{1.4}
\]

Comparing with R170_849 (1.3),

\[
 \boxed{B_{N,T}=PMP.}                                      \tag{1.5}
\]

Although `M` is infinite, (1.5) is a finite sum in each window.

## 2. Extraction of the Wronskian without hidden ports

The raw causal Wronskian is

\[
 \mathcal A_\Lambda^{\rm raw}
 =-\sum_{n\ge2}{\beta_\Lambda(n)\over\sqrt n}
       \partial_t\tau_{\log n}                             \tag{2.1}
\]

on every complete fiber. The Möbius comb has the same orientation;
by the same absence of return used in (1.4),

\[
 B_{N,T}P\mathcal A_\Lambda^{\rm raw}P
 =PM\mathcal A_\Lambda^{\rm raw}P                          \tag{2.2}
\]

for the coefficients visible in the window. Composing the shifts turns
the product into a Dirichlet convolution:

\[
 \boxed{
 M\mathcal A_\Lambda^{\rm raw}
 =-\sum_{n\ge2}{\gamma_\Lambda(n)\over\sqrt n}
       \partial_t\tau_{\log n},
 \qquad \gamma_\Lambda=\mu*\beta_\Lambda.}                 \tag{2.3}
\]

The incomplete hyperbola requires keeping the terms whose product
crosses the cutoff `N`; (2.2)--(2.3) are asserted for the visible
inner block. The finite-cutoff differences remain terminal ports, and
are not declared zero.

## 3. Computation of the law

R170_843 proves, for `Re s>1`,

\[
 B_\Lambda(s)
 :=\sum_{n\ge2}{\beta_\Lambda(n)\over n^s}
 =-\zeta(s)^2\left({1\over\zeta(s)}\right)''.
 \tag{3.1}
\]

Multiplying by `1/zeta(s)` gives

\[
 \sum_{n\ge2}{\gamma_\Lambda(n)\over n^s}
 ={B_\Lambda(s)\over\zeta(s)}
 =-\zeta(s)\left({1\over\zeta(s)}\right)''.                \tag{3.2}
\]

Since

\[
 \left({1\over\zeta(s)}\right)''
 =\sum_{d\ge1}{\mu(d)(\log d)^2\over d^s},                 \tag{3.3}
\]

comparing coefficients in a region of absolute convergence proves
(0.1).

Let `rad(n)=p_1...p_r`. Only square-free divisors contribute and

\[
 \sum_{d\mid n}\mu(d)(\log d)^2
 =\sum_{J\subseteq\{1,\dots,r\}}(-1)^{|J|}
       \left(\sum_{j\in J}\log p_j\right)^2.                \tag{3.4}
\]

The sum is the total finite difference of a quadratic polynomial:

* for `r=1` it equals `-(log p_1)^2`;
* for `r=2` it equals `2 log p_1 log p_2`;
* for `r>=3` it equals zero.

The outer sign of (0.1) proves (0.2).

## 4. Extracted physical form

For `F` supported in the window, the Wronskian block of the physical
extraction R170_849 (3.1) becomes

\[
\begin{aligned}
 &-\operatorname{Re}
  \langle B_{N,T}^*F,P\mathcal A_\Lambda^{\rm raw}F\rangle\\
 &\qquad=\operatorname{Re}\sum_{n<e^{2T}}
   {\gamma_\Lambda(n)\over\sqrt n}
   \langle F,\partial_t\tau_{\log n}F\rangle
   +\mathcal T_{N,T}^{\rm cut}(F),                           \tag{4.1}
\end{aligned}

where `T_cut` retains the finite-hyperbola routes that cross the
cutoff before compression. It has no declared sign.

The inner part of (4.1) is explicitly

\[
\begin{aligned}
 &\sum_p(\log p)^2
   \sum_{k\ge1\atop p^k<e^{2T}}
       {\operatorname{Re}\langle F,
          \partial_t\tau_{k\log p}F\rangle\over p^{k/2}}\\
 &\quad-2\sum_{p<q}\log p\log q
   \sum_{a,b\ge1\atop p^aq^b<e^{2T}}
       {\operatorname{Re}\langle F,
          \partial_t\tau_{a\log p+b\log q}F\rangle
        \over p^{a/2}q^{b/2}}.                               \tag{4.2}
\end{aligned}

This is the exact interaction that the physical metric sees after
extracting the full comb.

## 5. What it contributes and what is missing

Law (0.2) meets two structural conditions of the problem:

1. it uses the inverse of the comb over **all integers**, so it fails
   if unique factorization is altered;
2. it is uniform in `T`; the window only truncates a fixed global
   law.

It does not yet meet the sign condition. The two-prime-base channel
is negative and the correlations derived from (4.2) have no
individual sign. The next piece must jointly control the two
lines of (4.2), together with `T_cut` and the Tate/polar/outer ports of
R170_849. Treating only the first line would be false.

The structure suggests a rank-two object on the lattice of prime
bases: the negative channel is exactly the cross term
`-2 log p log q`. To obtain positivity, the full square with both its
diagonals would have to appear in the same physical collar; this
completion is not asserted here.

## 6. Status

```text
B_N,T = compression of the Möbius comb                       PROVED
inner extraction M A_raw                                     PROVED
law gamma=mu*beta                                             PROVED
support omega(n)<=2 and exact values                          PROVED
uniformity in T                                               PROVED
cutoff port T_cut                                             RETAINED / OPEN
signed completion of the two-prime-base channel               OPEN
MET--WARD / VIR--LB / D                                       OPEN
```
