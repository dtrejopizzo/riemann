# 106.32 — Atomwise prime tails and the conditional-variance hierarchy

## Purpose

The full-kernel identity of 106.31 rewrites the even Weil form as

\[
 QW(Kr,Kr)=\mathscr E_K(r)-\frac12\mathrm{Var}_{\mu_K}(r).
 \tag{1}
\]

This note asks whether the sharp inequality in (1) can be proved after
retaining only finitely many primes, finitely many prime towers, or any
proper subcollection of the von Mangoldt atoms.  The answer is no, and the
reason is exact rather than asymptotic.

Every individual prime-power atom is load-bearing for the universal
Poincare inequality.  If even one positive von Mangoldt atom is deleted,
compactly supported smooth even tests obtained from the Riemann radical
violate the resulting inequality.  On the radical, the deficit of a
truncated prime system is exactly the omitted positive tail.  That tail also
has an exact conditional-variance representation.

This is a structural theorem about the new full-kernel coordinate.  It does
not prove the all-prime inequality and therefore does not prove RH.

## 1. Atom and tower energies

Keep the normalization and notation of 106.31.  In particular,

\[
 \widehat K=\Xi,\qquad c_K=\frac12,\qquad
 d\mu_K(x)=2\cosh(x/2)K(x)\,dx.
 \tag{2}
\]

For \(u>0\) and an even multiplier \(r\), define

\[
 \mathcal J_u(r)
 :=\int_{\mathbb R}K(x)K(x-u)
       |r(x)-r(x-u)|^2\,dx.
 \tag{3}
\]

Thus

\[
 \mathscr E_K(r)
 =\mathscr E_\Gamma(r)
  +\sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
       \mathcal J_{\log m}(r).
 \tag{4}
\]

For a set \(S\) of prime powers, put

\[
 \mathscr E_S(r)
 :=\mathscr E_\Gamma(r)
  +\sum_{m\in S}\frac{\Lambda(m)}{\sqrt m}
       \mathcal J_{\log m}(r).
 \tag{5}
\]

All series in this note converge on the tests used below.  The reason is
that \(K\) and each fixed derivative of \(K\) have double-exponential
decay, whereas the aggregate von Mangoldt mass at logarithmic height \(u\)
is only \(e^{u/2+o(u)}\).

### Proposition 1 — Exact monotonicity and prime-tower decomposition

If \(S\subset S'\), then

\[
 \boxed{
 \mathscr E_{S'}(r)-\mathscr E_S(r)
 =\sum_{m\in S'\setminus S}\frac{\Lambda(m)}{\sqrt m}
   \mathcal J_{\log m}(r)\ge0.}
 \tag{6}
\]

Grouping the atoms by prime gives

\[
 \boxed{
 \mathscr E_K(r)=\mathscr E_\Gamma(r)+\sum_p\mathscr T_p(r),
 \qquad
 \mathscr T_p(r)
 =\log p\sum_{k\ge1}p^{-k/2}\mathcal J_{k\log p}(r).}
 \tag{7}
\]

Both statements follow directly from \(\Lambda(p^k)=\log p\) and the
nonnegativity of (3).  Notice that (6) is a statement about the energy, not
about the signed Weil form: the latter also contains the fixed variance
threshold in (1).

## 2. Conditional-variance form of an atom

Set

\[
 Z_u:=\int_{\mathbb R}K(x)K(x-u)\,dx>0,
 \qquad
 d\pi_u(x):=\frac{K(x)K(x-u)}{Z_u}\,dx.
 \tag{8}
\]

Let \(X_u\) have law \(\pi_u\), let \(B\) be an independent fair
Bernoulli variable, and define

\[
 Y_u=
 \begin{cases}
 r(X_u),&B=0,\\
 r(X_u-u),&B=1.
 \end{cases}
 \tag{9}
\]

Then, also for complex \(r\),

\[
 \boxed{
 \mathcal J_u(r)
 =4Z_u\,\mathbb E\!\left[
   \mathrm{Var}(Y_u\mid X_u)\right].}
 \tag{10}
\]

Indeed, conditionally on \(X_u=x\), the two possible values in (9) have
variance \(|r(x)-r(x-u)|^2/4\).

The same representation applies to a whole omitted set.  If \(A\) is a
nonempty set of prime powers and

\[
 Z_A:=\sum_{m\in A}\frac{\Lambda(m)}{\sqrt m}Z_{\log m}<\infty,
 \tag{11}
\]

first choose \(M\in A\) with probability proportional to
\(\Lambda(m)Z_{\log m}/\sqrt m\), and then use (8)--(9) at
\(u=\log M\).  The omitted tail becomes

\[
 \boxed{
 \sum_{m\in A}\frac{\Lambda(m)}{\sqrt m}
       \mathcal J_{\log m}(r)
 =4Z_A\,\mathbb E\!\left[
   \mathrm{Var}(Y\mid M,X_M)\right].}
 \tag{12}
\]

For a prime tower, (12) uses the geometric weights
\(p^{-k/2}Z_{k\log p}\).  This is the precise conditional-variance content
of the tower hierarchy.  It is nonnegative, but it is not a new source of
cross-tower sign.

## 3. Every von Mangoldt atom is load-bearing

Let \(\chi_a\) be the even cutoff family of 106.09 and define

\[
 f_a(x):=\chi_a(x)K''(x),
 \qquad
 r_a(x):=\frac{f_a(x)}{K(x)}
 =\chi_a(x)\frac{K''(x)}{K(x)}.
 \tag{13}
\]

Because \(K>0\), each \(r_a\) is an even member of
\(C_c^\infty(\mathbb R)\).  The transform identity

\[
 \widehat {K''}(z)=-z^2\Xi(z)
 \tag{14}
\]

makes \(K''\) an exact Weil radical.  The cutoff estimate of 106.09,
Theorem 2, therefore gives

\[
 |QW(f_a,f_a)|\le
 C\exp\!\left(\frac M2L-ce^L\right)\longrightarrow0,
 \qquad L=2a.
 \tag{15}
\]

### Lemma 2 — Strict energy at every fixed displacement

For every fixed \(u>0\),

\[
 \mathcal J_u(r_a)\longrightarrow
 \mathcal J_u(r_*),
 \qquad r_*:=K''/K,
 \tag{16}
\]

and

\[
 0<\mathcal J_u(r_*)<\infty.
 \tag{17}
\]

#### Proof

The derivative estimate (15) of 106.09 and the theta-series asymptotics
give an integrable majorant for the integrand in (3), at each fixed \(u\).
Dominated convergence proves (16) and finiteness in (17).

If \(\mathcal J_u(r_*)=0\), positivity of both \(K(x)\) and \(K(x-u)\)
would imply \(r_*(x)=r_*(x-u)\) for every \(x\).  Hence \(r_*\) would be
\(u\)-periodic.  But the leading theta term shows that
\(K''(x)/K(x)\) is unbounded as \(x\to+\infty\); in fact it has polynomial
growth in \(e^{2x}\).  It cannot be periodic.  Thus (17) is strict.
\(\square\)

### Theorem 3 — Atomwise indispensability

Let \(S\) be any collection of prime powers which omits at least one
prime power \(m_0\).  Then the sharp Poincare inequality with the
truncated arithmetic energy is false.  More precisely, for all sufficiently
large \(a\),

\[
 \boxed{
 \mathscr E_S(r_a)
 <\frac12\mathrm{Var}_{\mu_K}(r_a).}
 \tag{18}
\]

#### Proof

Apply the full identity (1) to \(r_a\), and subtract the omitted positive
atoms by (6):

\[
 \begin{aligned}
 \mathscr E_S(r_a)-\frac12\mathrm{Var}_{\mu_K}(r_a)
 &=QW(f_a,f_a)\\
 &\quad-
 \sum_{m\notin S}\frac{\Lambda(m)}{\sqrt m}
       \mathcal J_{\log m}(r_a).
 \end{aligned}
 \tag{19}
\]

Retain only the term \(m=m_0\) in the nonnegative sum.  By (15)--(17),

\[
 \limsup_{a\to\infty}
 \left(
 \mathscr E_S(r_a)-\frac12\mathrm{Var}_{\mu_K}(r_a)
 \right)
 \le-\frac{\Lambda(m_0)}{\sqrt {m_0}}
       \mathcal J_{\log m_0}(r_*)<0.
 \tag{20}
\]

This proves (18).  \(\square\)

### Corollary 4 — No finite-prime or finite-tower closure

The target in 106.31 cannot be proved by discarding all sufficiently large
prime powers, by retaining only finitely many prime towers, or even by
deleting one prescribed prime-power atom and keeping every other atom.
For the compact near-radicals (13), the exact missing amount is the positive
conditional-variance tail (12), up to the super-exponentially small quantity
(15).

The derivative bounds of 106.09 also give

\[
 r_a\longrightarrow r_*=K''/K
 \quad\hbox{in }L^2(\mu_K)
 \quad\hbox{and in the Gamma energy}.                 \tag{20a}
\]

Together with (15), (1) and monotone convergence of the prime energies,
this extends the full-kernel identity to \(r_*\) and gives

\[
 \mathscr E_K(r_*)=\frac12\mathrm{Var}_{\mu_K}(r_*).
 \tag{20b}
\]

Thus the following tail equalities are identities in the extended form
domain, not merely formal limits.

In particular, if the prime powers are revealed in any enumeration
\(m_1,m_2,\ldots\), then on the exact radical \(r_*=K''/K\) the deficits

\[
 D_J:=\frac12\mathrm{Var}_{\mu_K}(r_*)
 -\mathscr E_{\{m_1,\ldots,m_J\}}(r_*)
 \tag{21}
\]

form a decreasing positive tail,

\[
 D_J=\sum_{j>J}\frac{\Lambda(m_j)}{\sqrt {m_j}}
       \mathcal J_{\log m_j}(r_*)\downarrow0.
 \tag{22}
\]

Equation (22) is a deterministic reverse-tail identity.  Calling it a
martingale would add no information; its precise probabilistic content is
the conditional variance (12).

## 4. Theta-dilation lower bound and its sharp obstruction

There is an exact arithmetic dilation inside the positive theta series, but
Theorem 3 shows why using it only as a lower bound cannot close the sharp
constant.

For \(x\ge0\), write, with the common positive normalization suppressed,

\[
 k_m(x)=\pi m^2e^{5x/2}
 \left(2\pi m^2e^{2x}-3\right)e^{-\pi m^2e^{2x}},
 \qquad K(x)=\sum_{m\ge1}k_m(x).
 \tag{23}
\]

For every integer \(n\ge2\), direct substitution gives

\[
 \boxed{
 k_{nm}(x-\log n)=n^{-1/2}k_m(x).}
 \tag{24}
\]

Consequently, for \(x\ge\log n\),

\[
 K(x-\log n)
 =n^{-1/2}K(x)
 +\sum_{\substack{j\ge1\\n\nmid j}}k_j(x-\log n)
 >n^{-1/2}K(x).
 \tag{25}
\]

For even \(r\), reflection of the region \(x\le0\) onto
\(x\ge\log n\) therefore yields the rigorous atom bound

\[
 \boxed{
 \mathcal J_{\log n}(r)
 \ge2n^{-1/2}\int_{\log n}^{\infty}K(x)^2
 |r(x)-r(x-\log n)|^2\,dx.}
 \tag{26}
\]

After multiplication by \(\Lambda(n)/\sqrt n\), summation produces the
natural reduced prime energy

\[
 \widetilde{\mathscr E}_{p}(r)
 :=2\sum_{n\ge2}\frac{\Lambda(n)}{n}
 \int_{\log n}^{\infty}K(x)^2
 |r(x)-r(x-\log n)|^2\,dx.
 \tag{27}
\]

This is the proposed \(\Lambda(n)/n\) canonical-path coordinate.  It is
unconditional and retains all prime powers.  Nevertheless it is too small
for the sharp Poincare inequality.

### Proposition 5 — The dilation lower bound cannot attain the sharp constant

For all sufficiently large \(a\), the compact even tests (13) satisfy

\[
 \boxed{
 \mathscr E_\Gamma(r_a)+\widetilde{\mathscr E}_{p}(r_a)
 <\frac12\mathrm{Var}_{\mu_K}(r_a).}
 \tag{28}
\]

#### Proof

For \(r_*=K''/K\), the difference
\(r_*(x)-r_*(x-\log2)\) is not identically zero on
\([\log2,\infty)\): otherwise analyticity would make \(r_*\) periodic,
contradicting its unbounded theta asymptotic.  The strict remainder in (25)
(and, independently, the nonnegative middle region \(0<x<\log2\)) shows
that the exact \(n=2\) atom energy is strictly larger than its right side
in (26).
Dominated convergence transfers this strict deficit to \(r_a\).

Subtract (27) from the full energy in (1).  The omitted quantity is a sum
of nonnegative atomwise remainders and its \(n=2\) remainder converges to a
strictly positive number.  Meanwhile \(QW(Kr_a,Kr_a)\to0\) by (15).
Hence

\[
 \begin{aligned}
 &\mathscr E_\Gamma(r_a)+\widetilde{\mathscr E}_{p}(r_a)
 -\frac12\mathrm{Var}_{\mu_K}(r_a)\\
 &\qquad=QW(f_a,f_a)
 -\bigl(\mathscr E_p(r_a)-\widetilde{\mathscr E}_p(r_a)\bigr)<0
 \end{aligned}
\]

for all large \(a\).  \(\square\)

Thus the exact dilation (24) is new and useful bookkeeping, but the
inequality step (26) discards precisely the nondivisible theta indices and
the central crossing region that are load-bearing at the sharp constant.
No canonical-path proof based only on (26), even after summing all
\(\Lambda(n)/n\), can prove (1).

## 5. Relation to prior gates

The nearest earlier mechanisms were checked before stating Theorem 3.

1. Documents 104.43, 104.49 and 104.50 derive Palm, renewal and conditional
   variance identities on abstract prime towers.  Centering removes their
   cross-tower terms, and the resulting positivity also holds in shifted
   Euler countermodels.
2. Document 104.53 proves that additive polynomial tower identities collapse
   to single-tower cumulants and cannot supply the missing signed coupling.
3. Document 106.19 proves the generic Picone identity and gives a one-atom
   positive-jump countermodel.

The new statement is not a generic Mecke or tower-positivity claim.  It uses
the zeta-specific radical \(\widehat {K''}=-z^2\Xi\) and the full-kernel
variance identity to prove the opposite kind of fact: every literal
von Mangoldt atom is necessary for the universal sharp constant.

## 6. Verdict

The full-kernel coordinate has an exact monotone prime hierarchy, and its
omitted tail is a sum of genuine conditional variances.  This does not yield
the required lower bound.  Instead, the Riemann radical proves that no
proper atomwise truncation can yield it.

Consequently the remaining proof cannot come from a finite low-prime
certificate followed only by positivity of the tail.  It must establish the
sharp inequality using the complete infinite collection of ordinary
von Mangoldt atoms together with Gamma and the polar variance, with equality
on the known Riemann-radical family.
