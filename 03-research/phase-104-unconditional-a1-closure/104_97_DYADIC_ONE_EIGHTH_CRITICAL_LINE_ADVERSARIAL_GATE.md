# 104_97 — Critical adversarial gate for the dyadic constant $1/8$

## Result

The candidate bound from `104_96`,

\[
 \Delta_j\le {1\over8j^2},
 \tag{C}
\]

is a sufficient target for RH, but **is not a consequence of the
critical scale** \(\Re\rho=1/2\). More precisely, given
\(c>0\), \(\gamma>0\) and \(\phi\in\mathbb R\), define

\[
 B_m^{c,\gamma,\phi}
 ={c\sqrt m\over\log m}\cos(\gamma\log m+\phi),
 \qquad
 \Delta_j^{c,\gamma,\phi}
 =\sum_{2^{j-1}<m\le2^j}
 {\{B_m^{c,\gamma,\phi}\}^2\over m(m+1)}.
 \tag{1}
\]

If \(L=\log2\), then

\[
 \boxed{
 j^2\Delta_j^{c,\gamma,\phi}
 ={c^2\over L^2}
 \int_{(j-1)L}^{jL}\cos^2(\gamma t+\phi)\,dt+o(1).}
 \tag{2}
\]

In particular,

\[
 \liminf_{j\to\infty}j^2\Delta_j^{c,\gamma,\phi}
 \ge c^2\left\{
 {1\over2L}-{ |\sin(\gamma L)|\over2\gamma L^2}
 \right}.
 \tag{3}
\]

For \(c=1\), \(\gamma=7\), the right-hand side of (3) is

\[
 0.5741254552\ldots>{1\over8}.
 \tag{4}
\]

Thus, this purely critical control violates (C) for all sufficiently
large \(j\), even though its total energy converges. The power
\(j^{-2}\) is the correct scale; the universal constant \(1/8\) is not.

There is also a normalization that exactly reproduces the residue of a
critical zero. A pair of multiplicity \(M\) at
\(\rho=1/2\pm i\gamma\) contributes, in the first asymptotic term of the
explicit formula for \(J(x)\),

\[
 B_m^{[M,\gamma]}
 =-2M\Re {m^{1/2+i\gamma}\over
                   (1/2+i\gamma)\log m}.
 \tag{5}
\]

This is (1) with

\[
 c={2M\over\sqrt{1/4+\gamma^2}}
 \tag{6}
\]

and a fixed phase. Taking the first Riemann ordinate
\(\gamma_1=14.13472514173469\ldots\) and \(M=4\), (3) gives

\[
 \liminf j^2\Delta_j^{[4,\gamma_1]}
 \ge0.2222079232\ldots>{1\over8}.
 \tag{7}
\]

Example (5)--(7) is a **spectral witness on the line**, not the
Riemann zeta: the first zero of \(\zeta\) is simple in the verified range,
and modifying its multiplicity modifies the function and its Euler
weights. Hence (7) does not refute (C) for the ordinary weights. It does
rigorously refute any proof that claims to obtain the constant
\(1/8\) using only that all spectral exponents have real
part \(1/2\).

If one wishes to realize that spectrum literally as a completion,

\[
 \Xi_{M,\gamma}(s)
 =\{(s-1/2)^2+\gamma^2\}^{M}
 \tag{7a}
\]

is entire, real-symmetric, satisfies
\(\Xi_{M,\gamma}(1-s)=\Xi_{M,\gamma}(s)\), and all its zeros are
\(1/2\pm i\gamma\). Its logarithmic derivative has exactly those two
residues of multiplicity \(M\), which produce (5) on the formal
spectral side of an explicit formula. Model (7a) has no associated prime
arithmetic nor the ordinary Euler product; its sole purpose is to prove that
"functional equation + all zeros on the line" does not determine the
constant \(1/8\) either.

The correct status of (C) for \(\zeta\) is then as follows:

* (C) for the ordinary weights would imply RH by `104_93`;
* RH implies \(\sum_j\Delta_j<\infty\), but that summability does not imply
  any prescribed envelope \(Cj^{-2}\);
* neither `104_93`, nor the localization of the zeros on the line, proves (C);
* (7) is not a counterexample to (C) for \(\zeta\).

Consequently, (C) must be withdrawn as a supposed "critical control" and
kept only as an additional arithmetic conjecture, falsifiable and of
at least RH-strength. This document neither proves nor refutes (C) for the
ordinary weights, and does not prove RH.

---

## 1. Proof of the asymptotic formula

Set \(X=2^{j-1}\). The summand of (1) is

\[
 {c^2\cos^2(\gamma\log m+\phi)
  \over (m+1)\log^2m}.
 \tag{8}
\]

Replacing \((m+1)^{-1}\) by \(m^{-1}\) costs

\[
 O_{c}\!\left(\sum_{X<m\le2X}{1\over m^2\log^2m}\right)
 =O_c\!\left({1\over X\log^2X}\right).
 \tag{9}
\]

For

\[
 f(x)={\cos^2(\gamma\log x+\phi)\over x\log^2x},
\]

one has, uniformly in the block,

\[
 |f'(x)|\ll_\gamma {1\over x^2\log^2x}.
 \tag{10}
\]

Comparing each \(f(m)\) with its integral on \([m-1,m]\), and summing (10),
gives

\[
 \sum_{X<m\le2X}f(m)
 =\int_X^{2X}f(x)\,dx
 +O_\gamma\!\left({1\over X\log^2X}\right).
 \tag{11}
\]

After \(x=e^t\),

\[
 \int_X^{2X}f(x)\,dx
 =\int_{(j-1)L}^{jL}{\cos^2(\gamma t+\phi)\over t^2}\,dt.
 \tag{12}
\]

On that interval,

\[
 {j^2\over t^2}={1\over L^2}+O(1/j)
 \tag{13}
\]

uniformly. Multiplying (9)--(12) by \(j^2\) proves (2).

Finally,

\[
 \begin{aligned}
 \int_{(j-1)L}^{jL}\cos^2(\gamma t+\phi)\,dt
  ={L\over2}
  +{\sin(\gamma L)\over2\gamma}
    \cos\{\gamma(2j-1)L+2\phi\}.
 \end{aligned}
 \tag{14}
\]

The lower bound from (14) proves (3). Evaluations (4) and (7) are
mere substitution into a closed expression.

## 2. Exact relation with the explicit formula

The explicit formula for Riemann's function \(J\) contains
\(-\mathrm{Li}(x^\rho)\) for each zero, with symmetric
pairing. For any **finite** set of critical zeros,

\[
 \mathrm{Li}(x^\rho)
 ={x^\rho\over\rho\log x}
 +O_\rho\!\left({x^{1/2}\over\log^2x}\right),
 \qquad x\to\infty.
 \tag{15}
\]

The pair \(1/2\pm i\gamma\), repeated \(M\) times, produces (5) plus a
lower-order error. This justifies (5) as the critical control
with the correct residue normalization, rather than a simple made-up
power profile.

For the ordinary zeta one must sum all its zeros and keep the
cross terms. If, under RH, one truncates to \(0<\gamma\le T\), the
leading polynomial is

\[
 F_T(t)=-2\Re\sum_{0<\gamma\le T}
 {e^{i\gamma t}\over1/2+i\gamma}.
 \tag{16}
\]

Its local energy is

\[
 {1\over L^2}\int_{(j-1)L}^{jL}F_T(t)^2\,dt.
 \tag{17}
\]

The cross terms of (17) have no sign. For this reason it is not legitimate to
sum individual bounds like (3), nor to discard a finite block to obtain a
lower bound of the full square. Passing
uniformly from (17) to all zeros with a constant \(1/8\) is an
additional-frame local inequality; it is not the content of the RH
statement.

## 3. Valid critical substitute

The only general control that does follow from `104_93` under RH is

\[
 \boxed{
 \sum_{j\ge1}\Delta_j<\infty,
 \qquad
 \Delta_j=o(1).}
 \tag{18}
\]

One cannot promote (18), by pure positive-series theory, to
\(O(j^{-2})\): a summable sequence can have peaks arbitrarily
larger than \(j^{-2}\) on a sparse subsequence. To close RH
unconditionally it still suffices to have any summable majorant proved
directly for the ordinary weights, or the equivalent condition
\(\sum_j\Delta_j<\infty\); the number \(1/8\) should not be treated as a
constant imposed by the critical line.

## 4. Reproduction

From `tools/`:

```bash
python3 dyadic_one_eighth_critical_gate_check.py
```

The checker evaluates the closed-form constants of (3), verifies the normalized
witness (7), and compares (2) with the discrete sums of (1). Its
computations are diagnostics of the formula; the proof is (8)--(14).
