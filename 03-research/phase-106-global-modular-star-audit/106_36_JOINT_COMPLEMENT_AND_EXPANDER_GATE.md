# 106.36 — The joint complement floor and the arithmetic-expander gate

## Purpose

Document 106.35 removes the invalid separation into Lemmas A and B.  The
remaining finite assertion is the single coupled estimate

\[
 \boxed{
 \beta_L^+
 :=\inf_{\substack{g\perp q_L^+\\g\ {m even}\\\|g\|_2=1}}
 \left[
  \mathcal D_{p,N}(g,g)+\mathcal D_\Gamma(g,g)
  +2|\langle h_L,g\rangle|^2-\kappa_N
 \right]
 \ge c_0d_8.}
 \tag{1}
\]

This note tests a new proof mechanism suggested by (1): regard the literal
translations \(\log p^k\) as a weighted arithmetic expander and try to
show that the pole removes the unique low mode.  The mechanism has the
correct coupling and fails in the one-atom model.

The test produces one positive result and one binding obstruction.

1. The exact coupled operator is a weighted translation graph plus one
   polar rank-one lift; no divisor covariance is needed.
2. Any local expansion or canonical-path proof with a nonzero positive
   remainder is incompatible with the known infinite Riemann-radical
   equality family.  The sharp proof, if it exists, must be a globally
   signed identity which is exactly saturated by every radical derivative.

Thus the arithmetic-expander route does not prove (1).  It identifies the
precise sharpness condition that a successor must satisfy.

## 1. Exact graph form

Let

\[
 \nu_N(du)
 =\sum_{n\le N}\frac{\Lambda(n)}{\sqrt n}\,
   \delta_{\log n}(du)
 +\frac{e^{-u/2}}{1-e^{-2u}}\,du.
 \tag{2}
\]

For zero-extended \(g\in L^2(I_L)\), set

\[
 \mathcal D_N(g,g)
 =\int_{(0,\infty)}\|g-\tau_ug\|_2^2\,\nu_N(du).
 \tag{3}
\]

Then the exact centered prime--Gamma square is

\[
 \boxed{
 \langle A_L^+g,g\rangle
 =\mathcal D_N(g,g)-\kappa_N\|g\|_2^2
  +2|\langle h_L,g\rangle|^2.}
 \tag{4}
\]

Consequently (1) is a spectral statement for the literal weighted graph
whose edges are the zero-extended translations in (2).  The scalar
\(\kappa_N\) is its full diagonal mass, and the pole is not a perturbative
error: it lifts the coherent continuous-PNT mode.

The physical compensation of 106.19 gives the equivalent formula

\[
 \langle A_L^+g,g\rangle
 =\mathcal E_*(g)-c_*\|g\|_2^2-\mathcal A_\Delta(g),
 \tag{5}
\]

where

\[
 \begin{aligned}
 \mathcal E_*(g)
 &=\int_0^\infty
   \frac{e^{-5u/2}}{1-e^{-2u}}
   \|g-\tau_ug\|_2^2\,du,\\
 \mathcal A_\Delta(g)
 &=\int_{(0,L]}F_g(u)e^{-u/2}
   d\bigl(\psi(e^u)-e^u\bigr),
 \end{aligned}
 \tag{6}
\]

and \(F_g(u)=\langle g,\tau_ug\rangle+langle g,\tau_{-u}g\rangle\).
Thus the arithmetic-expander theorem would have to prove

\[
 \mathcal A_\Delta(g)
 \le\mathcal E_*(g)-(c_*+c_0d_8)\|g\|_2^2
 \tag{7}
\]

on \((q_L^+)^\perp\).  Formula (7) keeps every source term coupled.

## 2. Full-line sharpness constraint

Let \(K>0\) be Riemann's even kernel normalized by

\[
 \widehat K(z)=\Xi(z).
 \tag{8}
\]

The full-kernel identity of 106.31 is

\[
 QW(Kr,Kr)
 =\mathscr E_K(r)-\frac12\operatorname {Var}_{\mu_K}(r).
 \tag{9}
\]

For every integer \(j\ge1\), define

\[
 r_j(x)=\frac{K^{(2j)}(x)}{K(x)}.
 \tag{10}
\]

Since

\[
 \widehat {K^{(2j)}}(z)=(-1)^jz^{2j}\Xi(z),
 \tag{11}
\]

each \(K^{(2j)}\) belongs to the complete Weil radical.  Hence, in the
extended form domain,

\[
 \boxed{
 \mathscr E_K(r_j)
 =\frac12\operatorname {Var}_{\mu_K}(r_j)
 \qquad(j\ge1).}
 \tag{12}
\]

The equality family (12) is infinite-dimensional.

## 3. No positive local remainder

### Theorem 1 — Radical saturation obstruction

Suppose a proposed proof of the sharp all-prime inequality has the form

\[
 \mathscr E_K(r)-\frac12\operatorname {Var}_{\mu_K}(r)
 =\sum_{\alpha}\mathcal S_\alpha(r),
 \qquad \mathcal S_\alpha(r)\ge0,
 \tag{13}
\]

and suppose one summand contains a nonzero local edge square

\[
 \mathcal S_{\alpha_0}(r)
 \ge\int_0^\infty\!\int_{\mathbb R}
 w(x,u)|r(x)-r(x-u)|^2\,dx\,du
 \tag{14}
\]

with \(w\ge0\) positive on a set of positive measure.  Then (13) is
impossible.

#### Proof

Take \(r_1=K''/K\).  Equation (12) makes the left side of (13) zero, so
every nonnegative summand must vanish.  In particular, (14) gives

\[
 r_1(x)=r_1(x-u)
 \tag{15}
\]

for almost every \((x,u)\) in the positive set of \(w\).  The function
\(r_1\) is real analytic.  Fubini and analytic continuation therefore
make it periodic for at least one nonzero displacement \(u\).

This is impossible.  The leading positive theta term gives

\[
 \frac{K''(x)}{K(x)}\asymp e^{4x}
 \qquad(x\to+\infty),
 \tag{16}
\]

up to a nonzero positive constant, so \(r_1\) is unbounded and cannot be
periodic.  This contradiction proves the theorem.  \(\square\)

### Consequence

A strict expander estimate obtained by routing pairs through prime-power
edges, applying Cauchy--Schwarz along paths, or discarding a positive
subset of theta indices necessarily leaves a positive local remainder.
Theorem 1 shows that such a remainder contradicts the exact radical
equalities.  This includes:

1. a canonical-path comparison using only divisible theta indices;
2. an Efron--Stein decomposition over individual prime towers;
3. a Cheeger estimate with a strict edge surplus;
4. any sum-of-squares proof whose individual squares are local translation
   differences.

This does not rule out a signed global decomposition.  It proves that a
successful decomposition must have cancellations between different prime
towers, Gamma and the polar variance before its final nonnegative term is
formed.

## 4. Finite-window implication

The endpoint-corrected vector satisfies

\[
 |\mathscr R_L^+|+\|b_L^+\|\longrightarrow0.
 \tag{17}
\]

Therefore either of the estimates

\[
 \beta_L^+\ge c_0d_8
 \tag{18}
\]

or merely

\[
 \beta_L^+\ge-o(1)
 \tag{19}
\]

excludes the fixed negative even branch supplied by failure of RH.  Thus a
proof of (7), (18), or (19) completes RH through the already proved
asymptotic-inertia lemma.  Theorem 1 explains why the proposed arithmetic
expander does not provide that proof: every lossy positive comparison is
strict on a known equality vector.

## 5. Corrected research target

The next admissible theorem cannot be a separate Lemma A, a separate Lemma
B, or a positive canonical-path surplus.  It must be an exact globally
signed factorization

\[
 \boxed{
 \mathcal E_*(g)-c_*\|g\|_2^2-\mathcal A_\Delta(g)
 =\|\mathcal T_Lg\|^2+\mathcal R_L^{\rm glob}(g),}
 \tag{20}
\]

on \((q_L^+)^\perp\), where

\[
 \mathcal R_L^{\rm glob}(g)\ge-o(1)\|g\|_2^2,
 \tag{21}
\]

and both terms on the right of (20) vanish on the limiting Riemann-radical
family.  Any construction which does not pass this saturation test is
strictly too lossy to prove the required sharp floor.

## 6. Verdict

The literal-prime translation graph is the correct coupled object, but a
standard expansion proof cannot be sharp enough.  The known radical
derivatives saturate the desired inequality and force every positive local
remainder to vanish identically.  The surviving mechanism is a nonlocal
signed factorization retaining cross-tower interference; no such
factorization is proved in this note.
