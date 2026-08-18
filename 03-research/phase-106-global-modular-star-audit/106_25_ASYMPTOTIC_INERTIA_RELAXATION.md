# 106.25 — Asymptotic inertia relaxation and the direction of the Ritz bound

## Purpose

The quantitative Gate SPG of 106.23 asks for

\[
 \beta_L^+\ge c d_8,
 \qquad
 d_8\asymp \lambda^{17}e^{-4\pi\lambda^2},
 \tag{1}
\]

on the orthogonal complement of the parity-corrected moving vector
\(q_L^+\).  That scale is needed for the weighted curvature comparison of
106.07.  It is not needed merely to exclude a fixed negative Weil branch
and hence prove RH.

This note proves the weaker branch theorem actually sufficient for that
purpose.  It also records two binding limitations on the proposed
four-mode/min--max attack.

1. A vanishing operator residual together with the qualitative complement
   estimate \(\beta_L^+\ge-o(1)\) already excludes failure of RH.
2. The constrained prolate ladder supplies Ritz upper bounds, not an
   ambient lower bound for \(\beta_L^+\).
3. The unique minimum of the centered prime--Gamma multiplier cannot, by a
   Gårding or counting argument alone, bound the negative index.  The
   one-atom model of 106.19 has the same strict centering and arbitrarily
   many negative levels.

The first item is a genuine relaxation of the scale budget.  None of the
three items proves the remaining literal-von-Mangoldt complement estimate.

## 1. Abstract asymptotic inertia lemma

Let \(A_L\) be a lower-semibounded self-adjoint operator with compact
resolvent on a Hilbert space \(\mathcal H_L\), and let \(q_L\in
\operatorname{Dom}(A_L)\) be normalized.  Put

\[
 r_L=\|A_Lq_L\|,
 \qquad
 R_L=\langle A_Lq_L,q_L\rangle,
 \tag{2}
\]

and

\[
 \beta_L=
 \inf_{\substack{g\perp q_L\\\|g\|=1}}
 \langle A_Lg,g\rangle.
 \tag{3}
\]

### Theorem 1 — A qualitative complement floor selects the branch

Assume

\[
 \boxed{r_L\longrightarrow0,
 \qquad \beta_L\ge-\delta_L,
 \qquad \delta_L\longrightarrow0.}
 \tag{4}
\]

Then the ground eigenvalue \(\epsilon_L=\inf\sigma(A_L)\) cannot satisfy

\[
 \epsilon_L\le-c
 \tag{5}
\]

for one fixed \(c>0\) along an unbounded sequence of \(L\).

#### Proof

Suppose (5) holds along a subsequence, and let \(\phi_L\) be a normalized
ground eigenvector.  Write its orthogonal decomposition as

\[
 \phi_L=a_Lq_L+u_L,
 \qquad u_L\perp q_L.
 \tag{6}
\]

Self-adjointness gives

\[
 |\epsilon_L|\,|a_L|
 =|\langle A_Lq_L,\phi_L\rangle|
 \le r_L.
 \tag{7}
\]

Hence \(a_L\to0\).  For large \(L\), define the normalized orthogonal
projection

\[
 h_L=
 \frac{u_L}{(1-|a_L|^2)^{1/2}}
 \perp q_L.
 \tag{8}
\]

Using \(A_L\phi_L=\epsilon_L\phi_L\), one obtains exactly

\[
 \langle A_Lh_L,h_L\rangle
 =
 \frac{
  \epsilon_L(1-2|a_L|^2)+|a_L|^2R_L
 }{1-|a_L|^2}.
 \tag{9}
\]

Equation (7) also gives

\[
 |\epsilon_L|\,|a_L|^2
 \le \frac{r_L^2}{|\epsilon_L|}
 \le \frac{r_L^2}{c},
 \tag{9a}
\]

so this conclusion remains uniform even if \(\epsilon_L\to-\infty\).
Since \(|R_L|\le r_L\), the right side of (9) is at most \(-c/2\) for
all sufficiently large members of the subsequence.  This contradicts
\(\langle A_Lh_L,h_L\rangle\ge-\delta_L\).  \(\square\)

The full residual in (2) may equivalently be split as

\[
 A_Lq_L=R_Lq_L+b_L,
 \qquad b_L\perp q_L,
 \qquad r_L^2=|R_L|^2+\|b_L\|^2.
 \tag{10}
\]

Thus it is enough in (4) to prove

\[
 R_L\to0,
 \qquad
 \|b_L\|\to0,
 \qquad
 \beta_L\ge-o(1).
 \tag{11}
\]

### Corollary 2 — Relaxed ordinary-prime RH gate

Apply Theorem 1 to the even semilocal Weil operator \(A_L^+\) and the
parity-corrected moving vector \(q_L^+\) of 106.23.  If

\[
 \boxed{
 |\mathscr R_L^+|+\|b_L^+\|\longrightarrow0,
 \qquad
 \beta_L^+\ge-o(1),}
 \tag{12}
\]

then RH holds.

#### Proof

If RH fails, Corollary 2 of 106.11 supplies a fixed \(c_+>0\) such that
the even ground eigenvalue satisfies

\[
 \epsilon_{0,L}^+\le-c_+
 \tag{13}
\]

for every sufficiently large \(L\).  Equation (10) and the first part of
(12) give \(\|A_L^+q_L^+\|\to0\).  Theorem 1 contradicts (13).  \(\square\)

Consequently, the double-exponential lower scale \(c d_8\) is required by
the weighted ground/model curvature theorem, but not by the shorter
negative-branch contradiction.  The latter needs only the absence of a
macroscopic negative direction in \((q_L^+)^\perp\).

In the compensated physical coordinate of 106.19,

\[
 QW_L(g,g)
 =\mathcal E_*(g)-c_*\|g\|^2-\mathcal A_\Delta(g).
 \tag{13a}
\]

Therefore the relaxed complement condition in (12) is exactly the
following literal-prime inequality: there are \(\delta_L\to0\) such that

\[
 \boxed{
 \mathcal A_\Delta(g)
 \le
 \mathcal E_*(g)-(c_*-\delta_L)\|g\|^2
 }
 \tag{13b}
\]

for every even form-domain vector \(g\perp q_L^+\).  This removes the
\(d_8\) constant from the direct RH target without changing any prime,
prime-power, Gamma, pole, or zero-extension term.  Equation (13b) is an
exact reformulation, not a proof of its sign.

### Residual necessity

The complement condition and a small Rayleigh value do not suffice without
the operator residual.  Fix \(M>1\), let

\[
 A=\begin{pmatrix}-1&0\\0&M\end{pmatrix},
 \qquad
 q=\frac1{\sqrt{M+1}}\binom{\sqrt M}{1}.
 \tag{14}
\]

Then

\[
 \langle Aq,q\rangle=0,
 \qquad
 \inf_{g\perp q,\ \|g\|=1}\langle Ag,g\rangle=M-1>0,
 \tag{15}
\]

while \(\inf\sigma(A)=-1\) and \(\|Aq\|=\sqrt M\).  Thus neither
Rayleigh convergence nor a positive complement floor replaces the
residual hypothesis in (12).  This is the finite-dimensional form of the
anti-orthogonality issue isolated in 106.08.

## 2. Why the four-mode ladder cannot prove the lower floor

Let \(A\) be self-adjoint with compact resolvent and let \(U\) be an
\(m\)-dimensional trial space.  Denote the eigenvalues of \(A\) by
\(\mu_1\le\mu_2\le\cdots\), and the Ritz eigenvalues of the compression
\(P_UA|_U\) by \(\nu_1\le\cdots\le\nu_m\).

### Proposition 3 — The interlacing direction is one-sided

For \(1\le j\le m\),

\[
 \boxed{\mu_j\le\nu_j.}
 \tag{16}
\]

Moreover, if \(q\in U\) is normalized and \(v\in U\cap q^\perp\) is a
unit vector, then

\[
 \boxed{
 \inf_{\substack{g\perp q\\\|g\|=1}}
 \langle Ag,g\rangle
 \le \langle Av,v\rangle.}
 \tag{17}
\]

#### Proof

Equation (16) is the Rayleigh--Ritz min--max principle.  Equation (17)
follows because \(v\) belongs to the admissible set defining the
infimum.  \(\square\)

The two-dimensional constrained four-mode space of 106.12 has angle Ritz
levels \(d_4,d_8\).  Even after a proved transfer of its compressed matrix,
(16)--(17) can provide an upper trial level of order \(d_8\).  They cannot
provide the ambient lower estimate

\[
 \beta_L^+\ge c d_8.
 \tag{18}
\]

To reverse the direction one needs a transverse theorem controlling every
vector outside the trial space, together with its coupling to the trial
space.  That theorem is exactly the missing coupled Weil--angle/inertia
input; it is not contained in the prolate ladder.

## 3. The strict Fourier center does not control inertia

The exact centered square of 106.17 proves that the positive jump
multiplier has a unique minimum at \(t=0\).  This fact is stable under
replacing the ordinary-prime measure by any positive atomic jump measure,
because the Gamma term is already strictly positive away from zero.

The one-atom construction in Section 4 of 106.19 therefore gives a direct
falsifier for a Gårding/counting closure.  For one atom \(w\delta_a\),
the centered multiplier contains

\[
 2w(1-\cos(at))
 \tag{19}
\]

plus the same strict Gamma contribution, and hence still has its unique
minimum at zero.  Nevertheless, on a chain of \(M\) disjoint translated
bumps its shifted atomic compression has eigenvalues

\[
 -2w\cos\frac{k\pi}{M+1},
 \qquad 1\le k\le M.
 \tag{20}
\]

For sufficiently large \(w\), the bounded Gamma and polar terms cannot
prevent at least \(\lfloor M/2\rfloor\) negative levels.  Since \(M\) is
arbitrary, the following data do not even bound the negative index:

\[
 \boxed{
 \text{positive jump measure}
 +\text{strict fundamental Fourier center}
 +\text{Gamma channel}
 +\text{positive polar rank one}.}
 \tag{21}
\]

Thus a Gårding inequality, phase-space count, or rank-one interlacing
argument based only on (21) cannot prove (18), nor its relaxed form
\(\beta_L^+\ge-o(1)\).  Any successful proof must use a property of the
literal locations and magnitudes \(\Lambda(n)/\sqrt n\) which fails in the
one-atom model.

## 4. Semantic audit and status

The nearest predecessors are:

- 106.08: residual divided by ground/model overlap;
- 106.12 and 106.15: the fixed prolate ladder and Gate CWA/SPG;
- 106.14: finite radical frames do not control a negative channel;
- 106.17: the centered positive jump square;
- 106.19: Picone/resolvent equivalence and the one-atom inertia falsifier;
- E77.7h: a Ritz residual cannot omit the complementary coercivity
  denominator.

None states the asymptotic inertia relaxation (4), (11)--(12).  The
relaxation is useful only for the direct RH contradiction.  It does not
supply the weighted curvature rate of 106.07 and does not prove the
literal-prime estimate

\[
 \boxed{\beta_L^+\ge-o(1).}
 \tag{22}
\]

Existing compensated-spectrum diagnostics do not contradict (22) for the
ordinary coefficients; their resolved margins are much larger than
\(d_8\).  They are not sign certificates.  The remaining theorem is still
a signed, literal-von-Mangoldt exclusion of a macroscopic negative mode on
\((q_L^+)^\perp\), coupled with the vanishing residual in (12).
